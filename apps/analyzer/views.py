from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io
import sys
from .lexer import (
    LexerCR7,
    find_column
)
from .yacc import parser
import json


@csrf_exempt
def analyzer(request):
    """Function that analyze the code written in the frontend

    Args:
        request (HttpRequest): Request sent from the frontend

    Returns:
        JsonResponse: json object that contains the tokens and the lexer and yacc output
    """
    body = json.loads(request.body)
    data = body.get('code', '')

    lexer = LexerCR7()
    tokens = get_tokens(lexer, data)

    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    new_stderr = io.StringIO()
    sys.stderr = new_stderr

    lexer = LexerCR7()
    parser.parse(data, lexer=lexer)
    lex_output = new_stdout.getvalue()
    syntax_output = new_stderr.getvalue()

    return JsonResponse({
        'tokens': tokens,
        'lex_output': lex_output,
        'syntax_output': syntax_output
    })


def get_tokens(lexer, data):
    """Function that obtain the tokens from the data string

    Args:
        lexer (Lexer): lexer built to identify tokens of Dart CR7 version
        data (str): String to be analyzed

    Returns:
        list: A list of tokens found by the lexer
    """
    lexer.input(data)
    tokens = []
    id = 0
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        tokens.append({
            'id': id,
            'tipo': tok.type,
            'token': tok.value,
            'linea': tok.lineno,
            'colno': find_column(data, tok)
        })
        id += 1

    return tokens
