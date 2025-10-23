class Camisa:
    def __init__(self):
        self.__tamanho: str = ""

    def getTamanho(self) -> str:
        return self.__tamanho

    def setTamanho(self, valor: str):
        if valor in ["PP", "P", "M", "G", "GG", "XG"]:
            self.__tamanho = valor
        else:
            print("fail: tamanho inválido. Tente PP, P, M, G, GG ou XG.")


def main():
    blusa = Camisa()
    while blusa.getTamanho() == "":
        tamanho = input()
        blusa.setTamanho(tamanho)

    print("Parabéns, você comprou uma roupa tamanho", blusa.getTamanho())

main()