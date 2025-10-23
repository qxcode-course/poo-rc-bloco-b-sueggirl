class Chinela:
    def __init__(self):
        self.tamanho: int = 0

    def __str__(self) -> str:
        return f"tamanho: {self.tamanho}"

    def setTamanho(self, valor: int) -> None:
        if valor < 20 or valor > 50:
            print("fail: tamanho de chinela inválido")
        elif valor % 2 != 0:
            print("fail: o tamanho deve ser par")
        else:
            self.tamanho = valor
            print(f"tamanho {valor} definido com sucesso")

    def getTamanho(self) -> int:
        return self.tamanho


def main():
    chinela = Chinela()

    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(chinela)
        elif args[0] == "set":
            valor: int = int(args[1])
            chinela.setTamanho(valor)
        elif args[0] == "get":
            print(f"Tamanho atual: {chinela.getTamanho()}")
        else:
            print("fail: comando inválido")

main()

