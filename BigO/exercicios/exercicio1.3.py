"""
voce tem um nome e deseja encontrar o numero de telefone para esse nome em uma agenda telefonica 
"""
from data import lista_telefonica


        

def busca_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1 
    tentativas = 0

    while baixo <= alto:
        tentativas += 1
        meio = (baixo + alto ) // 2
        chute = lista[meio]

        print(f"🔍 Tentativa {tentativas}:")
        print(f"  Índices => baixo: {baixo}, meio: {meio}, alto: {alto}")
        print(f"  Comparando {chute} com {item}")

        if chute == item:
            print("✅ Encontrado!")
            return meio
        elif chute > item:
            print(f"  {chute} é maior que {item}, buscando na metade de baixo\n")
            alto = meio - 1
        else:
            print(f"  {chute} é menor que {item}, buscando na metade de cima\n")
            baixo = meio + 1
    print("Nome não encontrado.")
    return None


def main():
    resultado = busca_binaria(lista_telefonica.data_lista_telefonica[], "Miguel Macedo")
    print(f"Resultado final: {resultado}")


if __name__ == "__main__":
    main()