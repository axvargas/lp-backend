'''
Created Date: Friday July 2nd 2021 1:28:27 am
Author: Andrés X. Vargas
-----
Last Modified: Monday July 5th 2021 2:14:21 pm
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''
import ply.lex as lex


tokens = [
    # Enmanuel Magannales
    'AND',
    'ARROW',  # @ replace => in arrow function
    'ASSIGN',
    'ASIGSUM',
    'ASIGTIMES',
    'ASIGDIV',
    'MOD',
    'COMMA',
    'DIVISION',
    'DDOTS',
    'EQ',
    'EQ_V',
    'GT',
    'DOT',
    # Andres Vargas
    'GTE',
    'IDENT',
    'INT',
    'FLOAT',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'LT',
    'LTE',
    'NEGATION',
    'NE',
    # Josue Cobos
    'MINUS',
    'MINUSMINUS',
    'OR',
    'ASIGMINUS',
    'TIMES',
    'LPAREN',
    'PLUS',
    'PLUSPLUS',
    'RPAREN',
    'SEMICOLON',
    'STRING',
    'VIR',
    'DOUBLE'
]

reserved_words = {
    # Josue Cobos
    'abstract': 'ABSTRACT',
    'as': 'AS',
    'assert': 'ASSERT',
    'async': 'ASYNC',
    'await': 'AWAIT',
    'bool': 'BOOLEAN',
    'break': 'BREAK',
    'dynamic': 'DYNAMIC',
    'double': 'DOUBLE_TYPE',
    'float': 'FLOAT_TYPE',
    'else': 'ELSE',
    'enum': 'ENUM',
    'export': 'EXPORT',
    'extends': 'EXTENDS',
    'implements': 'IMPLEMENTS',
    'interface': 'INTERFACE',
    'super': 'SUPER',
    'switch': 'SWITCH',
    'case': 'CASE',
    # Andres Vargar
    'catch': 'CATCH',
    'class': 'CLASS',
    'const': 'CONST',
    'continue': 'CONTINUE',
    'do': 'DO',
    'for': 'FOR',
    'function': 'FUNCTION',
    'if': 'IF',
    # Enmanuel Magallanes
    'int': 'INT_TYPE',
    'return': 'RETURN',
    'var': 'VAR',
    'void': 'VOID',
    'while': 'WHILE',
    'false': 'FALSE',
    'finally': 'FINALLY',
    'true': 'TRUE',
    'typedef': 'TYPEDEF',
    'siu': 'PRINT',
    'String': 'STRING_TYPE',
    'List': 'LIST',
    'Map': 'MAP',
    'Set': 'SET',
    'clear': 'CLEAR_FUNC',
    'toString': 'TOSTRING_FUNC',
    'remove': 'REMOVE_FUNC',
    'trim': "TRIM_FUNC",
    'endsWith': "ENDSWITH_FUNC",
    'substring': "SUBSTRING_FUNC",
    'codeUnitAt':"CODEUNITAT_FUNC",
    'compareTo':"COMPARETO_FUNC",
    'join': "JOIN_FUNC",
    'contains': "CONTAINS_FUNC",
    'elementAt': "ELEMENTAT_FUNC",
    'add': "ADD_FUNC",
    'shuffle': "SHUFFLE_FUNC",
    'getRange': "GETRANGE_FUNC",
    'addAll': 'ADD_ALL_FUNC',
    'containsKey': 'CONTAINS_DICT_FUNC',
    'containsValue': 'CONTAINS_VALUE_FUNC'
}

tokens = tokens + list(reserved_words.values())


def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1
    
    
def LexerCR7():

    t_ignore = ' \t\x0c'
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_EQ_V = r'='
    t_COMMA = r','
    t_DIVISION = r'/'
    t_EQ = r'=='
    t_GT = r'>'
    # Josue Cobos
    t_GTE = r'>='
    t_LBRACE = r'{'
    t_RBRACE = r'}'
    t_LBRACKET = r'\['
    t_RBRACKET = r'\]'
    t_LT = r'<'
    t_LTE = r'<='
    t_NEGATION = r'!'
    t_NE = r'!='
    # Enmanuel Magallanes
    t_SEMICOLON = r';'
    t_ARROW = r'@'
    t_DDOTS = r':'
    t_VIR = r'~'
    t_ASIGSUM = r'\+='
    t_ASIGMINUS = r'-='
    t_ASIGTIMES = r'\*='
    t_ASIGDIV = r'/='
    t_MOD = r'%'
    t_PLUSPLUS = r'\+\+'
    t_MINUSMINUS = r'--'
    t_AND = r'&&'
    t_OR = r'\|\|'
    t_DOT = r'\.'

    #re_SIG = t_MINUS + r'?'
    t_INT = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'
    t_FLOAT = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'
    t_DOUBLE = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'
    t_STRING = r'(\"|\')([^\\\n]|(\\.))*?(\"|\')'


    def t_IDENT(t):
        r'[A-Za-z_][\w_]*'
        t.type = reserved_words.get(t.value, 'IDENT')
        return t


    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)


    def t_error(t):
        col = find_column(t.lexer.lexdata, t)
        print(f"Illegal character '{t.value}' at line {t.lineno}, col {col}")
        t.lexer.skip(1)


    def t_preprocessor(t):
        r'\#(.)*?\n'
        t.lexer.lineno += 1

    return lex.lex()
