from nodescript.sly import Lexer
from nodescript.type_system import *

class NodeLexer(Lexer):

    tokens = {
        ID, LET, MODE, FUNC, AS,
        TYPE, NUMBER, STRING, BOOL,
        EQUALS,
        COLON,
        COMMA,
        DOT,
        RETURNS,
        COMMENT
    }

    literals = { '(', ')', '{', '}', '#' }

    ignore = ' \t'

    EQUALS  = r'='
    COLON   = r'\:'
    COMMA   = r'\,'
    DOT     = r'\.'
    RETURNS = r'->'
    COMMENT = r'#[^\n]*\n'

    @_(r'\d+(\.\d+)?')
    def NUMBER(self, t):
        t.value = float(t.value)
        return t

    @_(r'[\"][^\"]*[\"]')
    def STRING(self, t):
        t.value = t.value.replace('"', '')
        return t
    
    @_(r'(True)|(False)')
    def BOOL(self, t):
        t.value = t.value == 'True'
        return t

    @_(r'(Vector)|(Value)|(Color)|(Shader)|(Node)')
    def TYPE(self, t):
        t.value = BType(t.value)
        return t

    @_(r'(shader)|(compositing)|(geometry)')
    def MODE(self, t):
        t.value = GraphMode(t.value)
        return t

    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['let'] = LET
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


def lex(script: str) -> List[List[any]]:
    lexer = NodeLexer()
    toks = list(lexer.tokenize(script.strip()))
    trees = []

    tok_types = [t.type for t in toks]
    while any(tt == 'FUNC' for tt in tok_types):
        i = tok_types.index('FUNC')
        j = i + tok_types[i:].index('}')
    
        trees.append(iter(toks[i-1:j+1]))
        toks[i-1:j+1] = []
        tok_types = [t.type for t in toks]

    if 'MODE' in tok_types:
        trees.append(iter(toks))

    return trees