class Person:
    def __init__(self, name:str, dinheiro:int):
        self.__name = name
        self.__dinheiro = dinheiro

    def pagamento(self, amount:int):
        if amount <= self.__dinheiro:
            self.__dinheiro -= amount
            return amount
        else:
            pago = self.__dinheiro
            self.__dinheiro = 0
            return pago
    def earn(self, amout:int):
        self.__dinheiro += amout

    def getName(self):
        return self.__name
    
    def getDinheiro(self):
        return self.__dinheiro
    def __str__(self):
        return f"{self.getName()}:{self.getDinheiro()}"
    
class Moto:
    def __init__(self):
        self.__cost = 0
        self.__driver:Person|None = None
        self.__passenger:Person|None = None
    def setDrive(self, person:Person):
        self.__driver = person

    def setPassenger(self, person:Person):
        if self.__driver is None:
            print("fail: no driver")
            return
        elif self.__passenger is not None:
            print("fail: passenger is already in the motorcycle")
            return
        else:
            self.__passenger = person
    def drive(self, distance:int):
        if self.__driver is None:
            print("fail: no driver")
            return
        elif self.__passenger is None:
            print("fail: no passenger")
            return
        else:
            self.__cost += distance

    def leave(self):
        if self.__passenger is None:
            print("fail: no passenger")
            return
        
        payment = self.__cost
        paid = self.__passenger.pagamento(payment)

        if paid < payment:
            print("fail: Passenger does not have enough money")
        self.__driver.earn(payment)
        print(f"{self.__passenger.getName()}:{self.__passenger.getDinheiro()} left")

        self.__cost = 0
        self.__passenger = None
    def __str__(self):
        driver = str(self.__driver) if self.__driver else "None"
        passenger = str(self.__passenger) if self.__passenger else "None"


        return f"Cost: {self.__cost}, Driver: {driver}, Passenger: {passenger}"
    


def main():
    moto = Moto()

    while True:
        line = input()
        print("$"+line)
        args:list[str] = line.split(" ")
        
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(moto)
        elif args[0] == "setPass":
            moto.setPassenger(Person(args[1], int(args[2])))
        elif args[0] == "setDriver":
            moto.setDrive(Person(args[1], int(args[2])))
        elif args[0] == "drive":
            moto.drive(int(args[1]))
        elif args[0] == "leavePass":
            moto.leave()
        else:
            print("fail: comando invalido")
main()