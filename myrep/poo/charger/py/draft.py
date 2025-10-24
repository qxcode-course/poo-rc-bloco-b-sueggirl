class Bateria:
    def __init__(self, capacidade: int):
        self.__capacidade = capacidade
        self.__carga = capacidade

    def getBateria(self):
        return f"{self.__carga}/{self.__capacidade}"
    
    def usaBateria(self, tempo:int):
        self.__carga -= tempo
        if self.__carga < 0:
            self.__carga = 0

    def temCarga(self):
        return self.__carga > 0
    
    def getCarga(self):
        return self.__carga
    
    def getCapacidade(self):
        return self.__capacidade
    
    def carregar(self, potencia:int , tempo:int):
        self.__carga += potencia * tempo
        if self.__carga > self.__capacidade:
            self.__carga = self.__capacidade
    
    

class Carregador:
    def __init__(self, potencia:int):
        self.__potencia = potencia
    def getPotencia(self):
        return self.__potencia
    
class Notebook:
    def __init__(self):
        self.__ligado = False
        self.__tempoUsado = 0
        self.__bateria: Bateria | None = None
        self.__carregador: Carregador | None = None

    def ligar(self):
        if self.__bateria and self.__bateria.temCarga():
            self.__ligado = True
        elif self.__carregador:
            self.__ligado = True
        else:
            print("fail: não foi possível ligar")

    def desligar(self):
        if not self.__ligado:
            print("fail: já desligado")
            return
        self.__ligado = False
        
    def setBateria(self, capacidade:int):
        if self.__bateria:
            print("fail: bateria ja conectada")
            return
        self.__bateria = Bateria(capacidade)

    def rmBateria(self):
        if not self.__bateria:
            print("fail: Sem bateria")
            return
        print(f"Removido {self.__bateria.getBateria()}")
        self.__bateria = None
        if not self.__carregador:
            self.__ligado = False

    def setCarregador(self, potencia:int):
        if self.__carregador:
            print("fail: carregador já conectado")
            return
        self.__carregador = Carregador(potencia)
    def rmCarregador(self):
        if not self.__carregador:
            print("fail: Sem carregador")
            return
        
        print(f"Removido {self.__carregador.getPotencia()}W")
        self.__carregador = None
        if not self.__bateria:
            self.__ligado = False

    def usar(self, tempo: int):
        tempo = int(tempo)
        if not self.__ligado:
            print("fail: desligado")
            return
        self.__tempoUsado += tempo
        if self.__bateria and self.__carregador:
            self.__bateria.carregar(self.__carregador.getPotencia(),tempo)
           
        elif self.__bateria:
            carga_inicio = self.__bateria.getCarga()
            self.__bateria.usaBateria(tempo)
            if not self.__bateria.temCarga():
                print("fail: descarregou")
                self.__ligado = False
                self.__tempoUsado -= (tempo - carga_inicio)
        elif self.__carregador:
            pass
        else:
            print("fail: desligado")
            self.__ligado = False

    def show(self):
        status = "ligado" if self.__ligado else "desligado"
        
        texto = f"Notebook: {status}"
        if self.__ligado:
            texto += f" por {self.__tempoUsado} min"
        imprimir = []
        if self.__carregador:
            imprimir.append(f"Carregador {self.__carregador.getPotencia()}W")
        if self.__bateria:
            imprimir.append(f"Bateria {self.__bateria.getBateria()}")
        if imprimir:
            texto += ", " + ", " .join(imprimir)
        
        print(texto)


def main():
    notebook = Notebook()
    while True:
        line = input()
        print("$" + line)
        args:list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            notebook.show()
        elif args[0] == "turn_on":
            notebook.ligar()
        elif args[0] == "turn_off":
            notebook.desligar()
        elif args[0] == "use":
            notebook.usar(int(args[1]))
        elif args[0] == "set_charger":
            notebook.setCarregador(int(args[1]))
        elif args[0] == "rm_charger":
            notebook.rmCarregador()
        elif args[0] == "set_battery":
            notebook.setBateria(int(args[1]))
        elif args[0] == "rm_battery":
            notebook.rmBateria()
        else:
            print("fail: comando invalido")

main()