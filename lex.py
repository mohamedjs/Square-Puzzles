import ply.lex as lex
import sys

tokens=[
    'NAME',
    'CL' ,
    'CR' ,
    'LP',
    'RP',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'EQUALS',
    'COMMA',
    'LESSEQUAL' ,
    'GREATEREQUAL' ,
      'GREATER' ,
      'LESS',
]
reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'return': 'RETURN',
    'void': 'VOID',
    'if': 'IF',
}
tokens += list(reserved.values())
t_PLUS = r'\+'
t_MINUS =r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'\='
t_COMMA = r'\,'
t_CL = r'\{'
t_CR = r'\}'
t_LP = r'\('
t_RP = r'\)'
t_NUMBER = r'\d+'
t_LESSEQUAL = r'\<\='
t_GREATEREQUAL = r'\>\='
t_GREATER = r'\>'
t_LESS = r'\<'
t_ignore = r' '

def t_NAME(t):
    r'[a-zA-Z_][a-zAZ_0-9]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    else:
        t.type = 'NAME'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value=int(t.value)
    return t
def t_error(t):
    print("Illegal character !")
    t.lexer.skip(1)

lexer = lex.lex()
