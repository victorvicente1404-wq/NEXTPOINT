"""
Padrões de interpretação da Iara.

Cada intenção possui uma ou mais expressões
regulares para identificar diferentes formas
de escrita.
"""

PADROES = {

    "cumprimento": [

        r"^(oi|ola|opa|eae|fala)$",

        r"^bom dia$",

        r"^boa tarde$",

        r"^boa noite$"

    ],

    "despedida": [

        r"^(tchau|falou)$",

        r"^ate logo$",

        r"^ate mais$"

    ],

    "consultar_nome": [

        r".*qual.*meu nome.*",

        r".*como.*me chamo.*",

        r".*quem sou eu.*",

        r".*lembra.*meu nome.*",

        r".*voce sabe.*meu nome.*"

    ]

}
