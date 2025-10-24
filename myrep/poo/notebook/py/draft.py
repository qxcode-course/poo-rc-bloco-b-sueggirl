class Bateria:
    def __init__(self, capacidade: int):
        self.__capacidade = capacidade
        self.__carga = capacidade

    def getBateria(self):
        return f"{self.__carga}/{self.__capacidade}"

    def usar(self, tempo: int):
        self.__carga -= tempo
        if self.__carga < 0:
            self.__carga = 0

    def carregar(self, potencia: int, tempo: int):
        self.__carga += potencia * tempo
        if self.__carga > self.__capacidade:
            self.__carga = self.__capacidade

    def temCarga(self):
        return self.__carga > 0


class Carregador:
    def __init__(self, potencia: int):
        self.__potencia = potencia

    def getPotencia(self):
        return self.__potencia


class Notebook:
    def __init__(self):
        self.__ligado = False
        self.__bateria: Bateria | None = None
        self.__carregador: Carregador | None = None

    def ligar(self):
        if self.__bateria and self.__bateria.temCarga():
            self.__ligado = True
            print("msg: notebook ligado")
        elif self.__carregador:
            self.__ligado = True
            print("msg: notebook ligado pelo carregador")
        else:
            print("fail: sem bateria ou carregador")

    def desligar(self):
        if self.__ligado:
            self.__ligado = False
            print("msg: notebook desligado")
        else:
            print("fail: notebook já está desligado")

    def usar(self, tempo: int):
        if not self.__ligado:
            print("fail: ligue o notebook primeiro")
            return

        if not self.__bateria and not self.__carregador:
            print("fail: sem bateria e sem carregador")
            self.__ligado = False
            return

        print(f"msg: Usando por {tempo} minutos")

        # Se tiver carregador, carrega bateria
        if self.__bateria and self.__carregador:
            self.__bateria.carregar(self.__carregador.getPotencia(), tempo)

        # Se tiver só bateria, consome carga
        elif self.__bateria and not self.__carregador:
            self.__bateria.usar(tempo)
            if not self.__bateria.temCarga():
                print("fail: bateria zerada, notebook desligado")
                self.__ligado = False

    def setBateria(self, bateria: Bateria):
        self.__bateria = bateria
        print("msg: bateria conectada")

    def rmBateria(self):
        if self.__bateria:
            self.__bateria = None
            print("msg: bateria removida")
        else:
            print("fail: sem bateria conectada")

    def setCarregador(self, carregador: Carregador):
        self.__carregador = carregador
        print("msg: carregador conectado")

    def rmCarregador(self):
        if self.__carregador:
            self.__carregador = None
            print("msg: carregador desconectado")
        else:
            print("fail: sem carregador conectado")

    def show(self):
        status = "ligado" if self.__ligado else "desligado"
        print(f"Notebook: {status}")

        if self.__bateria:
            print(f"bateria: {self.__bateria.getBateria()}")
        else:
            print("bateria: none")

        if self.__carregador:
            print(f"carregador: {self.__carregador.getPotencia()}W")
        else:
            print("carregador: none")


def main():
    notebook = Notebook()
    bateria = None
    carregador = None

    while True:
        try:
            line = input()
        except EOFError:
            break 
        if not line:
            continue

        print("$" + line)
        args = line.split()
        cmd = args[0]

        if cmd == "end":
            break

        elif cmd == "init":
            notebook = Notebook()

        elif cmd == "show":
            notebook.show()

        elif cmd == "bateria":
            capacidade = int(args[1])
            bateria = Bateria(capacidade)
            notebook.setBateria(bateria)

        elif cmd == "removeBateria":
            notebook.rmBateria()

        elif cmd == "carregador":
            potencia = int(args[1])
            carregador = Carregador(potencia)
            notebook.setCarregador(carregador)

        elif cmd == "removeCarregador":
            notebook.rmCarregador()

        elif cmd == "ligar":
            notebook.ligar()

        elif cmd == "desligar":
            notebook.desligar()

        elif cmd == "usar":
            tempo = int(args[1])
            notebook.usar(tempo)

main()
