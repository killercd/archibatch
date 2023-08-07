from ply import lex
import ply.yacc as yacc


VARS = {}

tokens = (
    'ASSIGN',
    'NUMBER',
    'PRINT',
    'ID',
)

t_ignore = ' \t'


def t_PRINT(t):
   r'PRINT'
   return t
def t_ASSIGN(t):
   r'='
   return t
def t_ID(t):
   r'[a-zA-Z][a-zA-Z0-9]*'
   return t

def t_NUMBER( t ) :
    r'[0-9]+'
    t.value = int( t.value )
    return t

def t_newline( t ):
  r'\n+'
  t.lexer.lineno += len( t.value )

def t_error( t ):
  print("Invalid Token:",t.value[0])
  t.lexer.skip( 1 )

lexer = lex.lex()


def p_assign(p):
    """assign : ID ASSIGN NUMBER"""
    VARS[p[1]] = p[3]

def p_print(p):
    """print : PRINT ID"""
    print(VARS[p[2]])
    
def p_error( p ):
    print("Syntax error in input!")

parser = yacc.yacc()

line = input("ARCHI-BATCH> ")
while line!="quit":
    res = parser.parse(line)
    line = input("ARCHI-BATCH> ")
