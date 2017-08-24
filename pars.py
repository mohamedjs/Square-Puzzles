from lex import tokens
import ply.yacc as yacc

################### function one ############################
def p_function(p):
    '''
     function : input_type NAME LP parameter RP CL term RETURN NAME CR
    '''
def p_parameter(p):
    '''
    parameter : input_type NAME
              | parameter COMMA parameter
              | empty
    '''
def p_term(p):
    '''
    term : NAME PLUS NAME
         | NAME MINUS NAME
         | NAME MULTIPLY NAME
         | NAME DIVIDE NAME
         | NAME EQUALS term
    '''
def p_input_type(p):
    '''
    input_type : INT
               | FLOAT
               | CHAR
               | VOID
    '''


################### function one ############################

################### if statement ############################
def p_if_state(p):
    '''
        if_state : IF LP expression RP CL terms CR
    '''

def p_expression(p):
    '''
          expression : NAME GREATER terms
                     | NAME LESS terms
                     | NAME GREATEREQUAL terms
                     | NAME LESSEQUAL terms
                     | empty
    '''
def p_terms(p):
    '''
        terms : NAME PLUS NUMBER
              | NAME MINUS NUMBER
              | NAME MULTIPLY NUMBER
              | NAME DIVIDE NUMBER
    '''
################### if statement ############################
def p_error(p):
    print("Syntax error !")

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None
parser = yacc.yacc()

while True:
    try:
        s=input(">>")
    except EOFError:
        break

    parser.parse(s)