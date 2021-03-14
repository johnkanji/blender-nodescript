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

script = '''
input Tex: TextureCoordinate
input Cam: CameraData
input Geo: Geometry
let ax = Math.Multiply(vec.x, fac)
let ay = Math.Multiply(vec.y, fac)
let az = Math.Multiply(vec.z, fac)
output vector = CombineXYZ(ax, ay, az)
let tex = ImageTexture(vector: mapping, interpolation: "Smart", extension: "Clip").color
tex = HueSatVal(color: tex)
tex = MixRGB(blend_type: "Color", fac: 1, color1: tex, color2: HSV(0.459866, 0.484069, 0.330132))
output surface = tex
'''

if __name__ == '__main__':
    data = 'let geoNorm = VectorTransform(vector: geo, vector_type: "Normal", convert_to: "Camera")'
    lexer = NodeLexer()
    for tok in lexer.tokenize(script):
        print('type=%r, value=%r' % (tok.type, tok.value))
