#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a menssagem 
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada exp:

    export LANG=pt_BR

Execução:

    Python3 hello.py
"""
__version__ = "0.0.1"
__author__ = "João Henrique Cavalheiro Grillo"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == 'it_IT':
    msg = "Ciao, Mondo!"

print(msg)