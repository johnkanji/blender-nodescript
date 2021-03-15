from nodescript.sly import Lexer
from nodescript.type_system import *

class NodeLexer(Lexer):

    tokens = { 
        ID, LET, SHADER, FUNC, AS,
        TYPE,
        TRUE, FALSE,
        NUMBER,
        STRING,
        EQUALS,
        COLON,
        COMMA,
        DOT,
        RETURNS
    }

    literals = { '(', ')', '{', '}' }

    ignore = ' \t'

    TRUE  = r'True'
    FALSE = r'False'
    EQUALS  = r'='
    COLON   = r'\:'
    COMMA   = r'\,'
    DOT     = r'\.'
    RETURNS = r'->'

    @_(r'\d+(\.\d+)?')
    def NUMBER(self, t):
        t.value = float(t.value)
        return t

    @_(r'[\"][^\"]*[\"]')
    def STRING(self, t):
        t.value = t.value.replace('"', '')
        return t

    @_(r'(Vector)|(Value)|(Color)|(Shader)|(Node)')
    def TYPE(self, t):
        t.value = BType(t.value)
        return t

    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['let'] = LET
    ID['shader'] = SHADER
    ID['func'] = FUNC
    ID['as'] = AS

    ignore_comment = r'\#.*'

    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1
