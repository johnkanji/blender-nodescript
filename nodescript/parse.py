from nodescript.sly import Parser

from nodescript import lex
from nodescript.nodes import get_node_func, Namespace
from nodescript.type_system import *


class NodeParser(Parser):
    # debugfile = 'parser.out'
    tokens = lex.NodeLexer.tokens

    def __init__(self):
        self.env = {}
        self.nodes = {}
        self.edges = []
        self.name = None
        self.mode = GraphMode.SHADER
        
        for cls in Namespace.__subclasses__():
            self.env[cls.__name__] = Value(cls(), BType.NAMESPACE)

    @_('SHADER ID "{" statements "}"')
    def shader(self, p):
        self.mode = GraphMode.SHADER
        self.name = p.ID
        return p.statements

    @_('statement statements')
    def statements(self, p):
        return [p.statement] + p.statements

    @_('statement')
    def statements(self, p):
        return [p.statement]

    @_('declaration')
    def statement(self, p):
        return ('let', p.declaration)

    @_('assignment')
    def statement(self, p):
        return ('assign', p.assignment)

    @_('expr')
    def statement(self, p):
        return ('expr', p.expr)

    @_('LET assignment_body',
       'LET assignment_body_typed')
    def declaration(self, p):
        new = p[1]
        assert new.name not in self.env
        self.env[new.name] = new
        return new

    @_('assignment_body',
       'assignment_body_typed')
    def assignment(self, p):
        new = p[0]
        assert new.name in self.env
        old = self.env[new.name]
        assert old.static == False or old.btype == new.btype
        self.env[new.name] = new
        return new

    @_('ID EQUALS expr')
    def assignment_body(self, p):
        return Variable(p.ID, p.expr, p.expr.btype)

    @_('name_typed EQUALS expr')
    def assignment_body_typed(self, p):
        name = p.name_typed[0]
        btype = p.name_typed[1]
        value = p.expr
        return Variable(name, value, btype, True)

    @_('ID')
    def expr(self, p):
        if p.ID in self.env:
            return self.env[p.ID]
        else:
            return Value(get_node_func(p.ID, self.mode), BType.NODE_FUNC)
        
    @_('TYPE')
    def expr(self, p):
            return Value(get_node_func(p.TYPE.value, self.mode), BType.NODE_FUNC)

    @_('NUMBER')
    def expr(self, p):
        return Value(p.NUMBER, BType.VALUE)

    @_('STRING')
    def expr(self, p):
        return Value(p.STRING, BType.STRING)
    
    @_('TRUE', 'FALSE')
    def expr(self, p):
        return Value(p[0] == 'True', BType.BOOL)

    @_('node_expr')
    def expr(self, p):
        return p.node_expr

    @_('accessor_expr')
    def expr(self, p):
        return p.accessor_expr
    
    @_('cast_expr')
    def expr(self, p):
        return p.cast_expr

    @_('expr "(" params_list ")"')
    def node_expr(self, p):
        assert p.expr.btype == BType.NODE_FUNC
        new = p.expr.value(p.params_list)
        self.nodes[new.id] = new
        return new

    @_('expr DOT ID')
    def accessor_expr(self, p):
        if p.expr.btype == BType.NODE or p.expr.btype == BType.NAMESPACE:
            return p.expr.value.access(p.ID)
        return (p.expr, p.ID)
    
    @_('expr AS TYPE')
    def cast_expr(self, p):
        btype = p.TYPE
        expr = p.expr
        expr.btype = btype
        return expr
    
    
    @_('empty')
    def params_list(self, p):
        return []
    
    @_('pos')
    def params_list(self, p):
        return [p.pos]
    
    @_('pos COMMA params_list')
    def params_list(self, p):
        return [p.pos] + p.params_list
    
    @_('pos COMMA named_params_list')
    def params_list(self, p):
        return [p.pos]
    
    @_('named_params_list')
    def params_list(self, p):
        return p.named_params_list
    
    @_('named')
    def named_params_list(self, p):
        return [p.named]
    
    @_('named COMMA named_params_list')
    def named_params_list(self, p):
        return [p.named] + p.named_params_list
    
    @_('ID COLON expr')
    def named(self, p):
        return (p.ID, p.expr)
    
    @_('expr')
    def pos(self, p):
        return (None, p.expr)
    

    @_('ID COLON TYPE')
    def name_typed(self, p):
        return (p.ID, p.TYPE)

    @_('')
    def empty(self, p):
        pass
    
    def error(self, p):
        print('error')
        print(p)
        print(self.state, self.statestack)
        for s in self.symstack:
            print(s)


def parse(script):
    lexer = lex.NodeLexer()
    parser = NodeParser()
    
    for text in [script]:
        result = parser.parse(lexer.tokenize(text.strip()))
    return parser
