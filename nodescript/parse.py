from nodescript.sly import Parser

from nodescript import lex
from nodescript.nodes import get_node_func, Namespace
from nodescript.nodes.group import _GroupInput, _GroupOutput
from nodescript.type_system import *


class NodeParser(Parser):
    debugfile = "parser.out"
    tokens = lex.NodeLexer.tokens

    precedence = (
        ("left", "+", "-"),
        ("left", "*", "/", "@"),
        ("right", UMINUS),
    )

    def __init__(self):
        self.env = {}
        self.nodes = {}
        self.name = None
        self.mode = None
        self.is_func = False

        # Load namespaces
        # TODO: Should be based on mode
        for cls in Namespace.__subclasses__():
            self.env[cls.__name__] = Variable(
                cls.__name__, Value(cls(), BType.NAMESPACE), BType.NAMESPACE
            )

    @_("MODE seen_mode ID tree_body")
    def start(self, p):
        self.mode = p.MODE
        self.name = p.ID
        return p.tree_body

    @_("")
    def seen_mode(self, p):
        self.mode = p[-1]

    @_("func_def")
    def start(self, p):
        self.link_outputs()
        return p.func_def

    # FUNCTIONS
    @_("func_signature tree_body")
    def func_def(self, p):
        pass

    @_("MODE FUNC ID args RETURNS args")
    def func_signature(self, p):
        self.mode = p.MODE
        self.name = p.ID
        self.is_func = True
        self.setup_inputs(p.args0)
        self.outputs = p.args1
        self.setup_outputs(p.args1)

    @_('"(" args_list ")"')
    def args(self, p):
        return p.args_list

    @_("name_typed")
    def args_list(self, p):
        return {p.name_typed[0]: p.name_typed[1]}

    @_("name_typed COMMA args_list")
    def args_list(self, p):
        return {p.name_typed[0]: p.name_typed[1], **p.args_list}

    @_("empty")
    def args_list(self, p):
        return {}

    @_('"{" statements "}"')
    def tree_body(self, p):
        return p.statements

    @_("statement statements")
    def statements(self, p):
        return [p.statement] + p.statements

    @_("statement")
    def statements(self, p):
        return [p.statement]

    @_("declaration")
    def statement(self, p):
        return ("let", p.declaration)

    @_("assignment")
    def statement(self, p):
        return ("assign", p.assignment)

    @_("expr")
    def statement(self, p):
        return ("expr", p.expr)

    @_("COMMENT")
    def statement(self, p):
        pass

    @_("LET ID EQUALS expr", "LET name_typed EQUALS expr")
    def declaration(self, p):
        try:
            name, btype = p[1]
        except ValueError:
            name = p[1]
            btype = None
        assert name not in self.env
        var = Variable(name, p.expr, btype)
        self.env[name] = var
        return var

    @_("ID EQUALS expr")
    def assignment(self, p):
        name = p.ID
        assert name in self.env
        new_val = p.expr
        var = self.env[name]

        if var.btype is None or var.btype == new_val.btype:
            var.value = new_val
        elif new_val.btype == BType.NODE:
            new_val = new_val.value.default()
            if var.btype == new_val.btype:
                var.value = new_val
        else:
            raise AttributeError()

        self.env[name] = var
        return var

    @_("ID")
    def expr(self, p):
        if p.ID in self.env:
            return self.env[p.ID].value
        else:
            return Value(get_node_func(p.ID, self.mode), BType.NODE_FUNC)

    @_("TYPE")
    def expr(self, p):
        return Value(get_node_func(p.TYPE.value, self.mode), BType.NODE_FUNC)

    @_("NUMBER")
    def expr(self, p):
        return Value(p.NUMBER, BType.VALUE)

    @_("STRING")
    def expr(self, p):
        return Value(p.STRING, BType.STRING)

    @_("BOOL")
    def expr(self, p):
        return Value(p.BOOL, BType.BOOL)

    @_("vector_literal")
    def expr(self, p):
        return p.vector_literal

    @_("node_expr")
    def expr(self, p):
        return p.node_expr

    @_("accessor_expr")
    def expr(self, p):
        return p.accessor_expr

    @_("cast_expr")
    def expr(self, p):
        return p.cast_expr

    @_('"[" NUMBER COMMA NUMBER COMMA NUMBER "]"')
    def vector_literal(self, p):
        return Value([p.NUMBER0, p.NUMBER1, p.NUMBER2], BType.VECTOR)

    @_('expr "(" params_list ")"')
    def node_expr(self, p):
        assert p.expr.btype == BType.NODE_FUNC
        new = p.expr.value(p.params_list)
        self.nodes[new.id] = new
        return Value(new, BType.NODE)

    @_("expr DOT ID")
    def accessor_expr(self, p):
        assert p.expr.btype == BType.NODE or p.expr.btype == BType.NAMESPACE
        return p.expr.value.access(p.ID)

    @_("expr AS TYPE")
    def cast_expr(self, p):
        expr = p.expr
        if expr.btype == BType.NODE and p.TYPE != BType.NODE:
            expr = expr.value.default()
        btype = p.TYPE
        expr.btype = btype
        return expr

    @_("empty")
    def params_list(self, p):
        return []

    @_("pos")
    def params_list(self, p):
        return [p.pos]

    @_("pos COMMA params_list")
    def params_list(self, p):
        return [p.pos] + p.params_list

    @_("pos COMMA named_params_list")
    def params_list(self, p):
        return [p.pos]

    @_("named_params_list")
    def params_list(self, p):
        return p.named_params_list

    @_("named")
    def named_params_list(self, p):
        return [p.named]

    @_("named COMMA named_params_list")
    def named_params_list(self, p):
        return [p.named] + p.named_params_list

    @_("ID COLON expr")
    def named(self, p):
        return (p.ID, p.expr)

    @_("expr")
    def pos(self, p):
        return (None, p.expr)

    @_("ID COLON TYPE")
    def name_typed(self, p):
        return (p.ID, p.TYPE)

    # MARK:  Operators
    #
    @_("expr '+' expr")
    def expr(self, p):
        return self.create_op("Add", p.expr0, p.expr1)

    @_("expr '-' expr")
    def expr(self, p):
        return self.create_op("Sub", p.expr0, p.expr1)

    @_("expr '*' expr")
    def expr(self, p):
        return self.create_op("Mul", p.expr0, p.expr1)

    @_("expr '/' expr")
    def expr(self, p):
        return self.create_op("Div", p.expr0, p.expr1)

    @_("expr '@' expr")
    def expr(self, p):
        return self.create_op("Dot", p.expr0, p.expr1)

    @_("'(' expr ')'")
    def expr(self, p):
        return p.expr

    @_("'-' expr %prec UMINUS")
    def expr(self, p):
        if p.expr.get_type() == BType.VECTOR:
            lhs = Value([0, 0, 0], BType.VECTOR)
        elif p.expr.get_type() == BType.VALUE:
            lhs = Value(0, BType.VALUE)
        else:
            raise TypeError
        return self.create_op("Sub", lhs, p.expr)

    @_("")
    def empty(self, p):
        pass

    def error(self, p):
        print("error")
        print(
            f'{self.cls_module}.{self.cls_name}:{getattr(p,"lineno","")}: '
            f'Syntax error at {getattr(p,"value","EOC")}'
        )

    def setup_inputs(self, inps):
        assert self.is_func == True
        new = _GroupInput(inps)
        self.nodes[new.id] = new
        for inp in inps:
            self.env[inp] = Variable(inp, new.access(inp), inps[inp])

    def setup_outputs(self, outs):
        assert self.is_func == True
        for out in outs:
            self.env[out] = Variable(out, None, outs[out])

    def link_outputs(self):
        assert self.is_func == True
        new = _GroupOutput(self.outputs, [(k, self.env[k].value) for k in self.outputs])
        self.nodes[new.id] = new

    def create_op(self, op, lhs, rhs):
        if lhs.get_type() == BType.VECTOR and rhs.get_type() == BType.VECTOR:
            nspace = "VMath"
        elif lhs.get_type() == BType.VECTOR or rhs.get_type() == BType.VECTOR:
            nspace = "VMath"
            if lhs.get_type() == BType.VALUE:
                lhs.get_value().btype = BType.VECTOR
            elif rhs.get_type() == BType.VALUE:
                rhs.get_value().btype = BType.VECTOR
            else:
                raise TypeError
        elif lhs.get_type() == BType.VALUE and rhs.get_type() == BType.VALUE:
            if op == "Dot":
                raise TypeError
            nspace = "Math"
        else:
            raise TypeError
        params = [(None, lhs), (None, rhs)]
        new = self.env[nspace].value.value.access(op).value(params)
        self.nodes[new.id] = new
        return Value(new, BType.NODE)

    def to_tree(self):
        return Tree(self.name, self.mode, self.is_func, self.nodes)


def parse(script):
    trees = lex.lex(script)

    for f in trees:
        parser = NodeParser()
        parser.parse(f)
        yield parser.to_tree()
