class Tamagochi:
    def __init__(self, carregado: int, limpo: int):
        self.carregado = carregado
        self.limpo = limpo
        self.energy = carregado
        self.limpeza = limpo
        self.age = 0
        self.vivo = True

    def setEnergy(self, energy: int):
        self.energy = max(0, min(energy, self.carregado))
        if self.energy == 0:
            self.vivo = False

    def setLimpeza(self, limpeza: int):
        self.limpeza = max(0, min(limpeza, self.limpo))
        if self.limpeza == 0:
            self.vivo = False

    def setAge(self, age: int):
        self.age = age

    def getEnergy(self):
        return self.energy

    def getLimpeza(self):
        return self.limpeza

    def getAge(self):
        return self.age

    def isAlive(self):
        return self.vivo

    def play(self):
        if not self.vivo:
            print("fail: pet esta morto")
            return
        self.setEnergy(self.energy - 2)
        self.setLimpeza(self.limpeza - 3)
        self.setAge(self.age + 1)
        if self.energy == 0:
            print("fail: pet morreu de fraqueza")
        if self.limpeza == 0:
            print("fail: pet morreu de sujeira")

    def sleep(self):
        if not self.vivo:
            print("fail: pet esta morto")
            return
        if self.energy >= self.carregado - 5:
            print("fail: nao esta com sono")
            return
        
        energy_before_sleep = self.energy
        self.setEnergy(self.carregado)
        recarregado = self.carregado - energy_before_sleep
        self.setAge(self.age + recarregado)

    def shower(self):
        if not self.vivo:
            print("fail: pet esta morto")
            return
        self.setEnergy(self.energy - 3)
        self.setLimpeza(self.limpo)
        self.setAge(self.age + 2)

    def __str__(self):
        return f"E:{self.energy}/{self.carregado}, L:{self.limpeza}/{self.limpo}, I:{self.age}"

class Game:

    def __init__(self):
        self.pet = None

    def initPet(self, carregado: int, limpo: int):
        self.pet = Tamagochi(carregado, limpo)

    def show(self):
        if self.pet is None:
            print("fail: nenhum pet")
        else:
            print(self.pet)

    def play(self):
        if self.pet is None:
            print("fail: nenhum pet")
        else:
            self.pet.play()

    def sleep(self):
        if self.pet is None:
            print("fail: nenhum pet")
        else:
            self.pet.sleep()

    def shower(self):
        if self.pet is None:
            print("fail: nenhum pet")
        else:
            self.pet.shower()

def main():
    game = Game()
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "init":
            carregado = int(args[1])
            limpo = int(args[2])
            game.initPet(carregado, limpo)
        elif args[0] == "show":
            game.show()
        elif args[0] == "play":
            game.play()
        elif args[0] == "sleep":
            game.sleep()
        elif args[0] == "shower":
            game.shower()
        else:
            print("fail: comando invalido")

main()