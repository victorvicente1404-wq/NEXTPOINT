from iara.config import (
    NOME_PROJETO,
    NOME_IA,
    VERSAO
)

from iara.motor_conversa import conversar


def main():

    print("=" * 40)
    print(f"{NOME_PROJETO} - {NOME_IA}")
    print(f"Versão {VERSAO}")
    print("=" * 40)

    while True:

        usuario = input("\nVocê: ")

        if usuario.lower() == "sair":
            break

        resposta = conversar(usuario)

        print(f"{NOME_IA}: {resposta}")


if __name__ == "__main__":
    main()
