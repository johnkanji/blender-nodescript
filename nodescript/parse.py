from nodescript.sly import Parser

from nodescript import lex
from nodescript.nodes import get_node_func, Namespace
from nodescript.type_system import *


class NodeParser(Parser):
    tokens = lex.NodeLexer.tokens

    def __init__(self):
        self.env = {}
        self.nodes = {}
        self.edges = []
        self.mode = GraphMode.SHADER
        
        print([cls.__name__ for cls in Namespace.__subclasses__()])
        for cls in Namespace.__subclasses__():
            print(cls.__name__)
            self.env[cls.__name__] = Value(cls(), BType.NAMESPACE)

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
        print('parse ID', p.ID)
        print(' ', self.env.keys())
        if p.ID in self.env:
            return self.env[p.ID]
        else:
            return Value(get_node_func(p.ID, self.mode), BType.NODE_FUNC)

    @_('NUMBER')
    def expr(self, p):
        return Value(p.NUMBER, BType.VALUE)

    @_('STRING')
    def expr(self, p):
        return Value(p.STRING, BType.STRING)
    
    @_('TRUE', 'FALSE')
    def expr(self, p):
        print(p[0])
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
    
    @_('expr AS ID')
    def cast_expr(self, p):
        btype = BType(p.ID)
        expr = p.expr
        expr.btype = btype
        return expr

    @_('params_positional COMMA params_named')
    def params_list(self, p):
        return p.params_positional + p.params_named

    @_('params_positional')
    def params_list(self, p):
        return p.params_positional

    @_('params_named')
    def params_list(self, p):
        return p.params_named

    @_('empty')
    def params_list(self, p):
        pass

    @_('expr')
    def params_positional(self, p):
        return [(None, p.expr)]

    @_('expr COMMA params_positional')
    def params_positional(self, p):
        return [(None, p.expr)] + p.params_positional

    @_('param_named')
    def params_named(self, p):
        return [p.param_named]

    @_('param_named COMMA params_named')
    def params_named(self, p):
        return [p.param_named] + p.params_named

    @_('ID COLON expr')
    def param_named(self, p):
        return (p.ID, p.expr)

    @_('ID COLON ID')
    def name_typed(self, p):
        return (p.ID0, BType(p.ID1))

    @_('')
    def empty(self, p):
        pass


script = '''
let geo = Geometry()
let h = BrightContrast(color: geo.pointiness as Color, contrast: 15)
let v = VMath.Dot(geo.normal, Vector(1,0,0.8))
v = MapRange(value: v, clamp: True, to_max: 0.1)
let col = CombineHSV(h as Value, 1, v)
MaterialOutput(surface: col as Shader)
'''

def main():
    lexer = lex.NodeLexer()
    parser = NodeParser()

    # for text in script.splitlines():
    for text in [script]:
        # print(list(lexer.tokenize(text)))
        result = parser.parse(lexer.tokenize(text.strip()))
        for s in result:
            print(s)
        print()
    print('env')
    for e in parser.env.items():
        print(e)
    print('nodes')
    for n in parser.nodes.values():
        print(n.id, n)
        for p in n.params.items():
            print(' ', p)
