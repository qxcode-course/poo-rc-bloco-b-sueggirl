class Lead:
    def __init__(self, thickness:float = 0.0, hardness:str = "", size:int = 0 ):
        self.__thickness = thickness
        self.__hardness = hardness
        self.__size = size

    def usagePerPage(self):
        usage = {"HB" : 1, "2B" : 2, "4B" : 4, "6B" : 6}
        for tip in usage:
            if self.__hardness == tip:
                return usage[tip]
        return 0
    
    def getThickness(self):
        return self.__thickness
    def getHardness(self):
        return self.__hardness
    def getSize(self):
        return self.__size
    
    def setSize(self, size:int):
        self.__size = size

    def __str__(self):
        return f"{self.__thickness}:{self.__hardness}:{self.__size}"
    
class Pencil:
    def __init__(self, thickness:float = 0.0):
        self.__thickness = thickness
        self.__tip: Lead | None = None

    def insertLead(self, tip:Lead):
        if self.hasLead():
            print("fail: ja existe grafite")
            return
        elif tip.getThickness() != self.__thickness:
            print("fail: calibre incompativel")
            return
        
        else:
            self.__tip = tip

    def hasLead(self):
        return self.__tip is not None
    
    
    def removeLead(self):
        if not self.hasLead():
            print("fail: nao existe grafite")
            return
        else:
            self.__tip = None


    def writePage(self):
        if not self.hasLead():
            print("fail: nao existe grafite")
            return
        uso = self.__tip.usagePerPage()
        if self.__tip.getSize() <= 10:
            print("fail: tamanho insuficiente")
            return
        elif self.__tip.getSize() - uso < 10:
            self.__tip.setSize(10)
            print("fail: folha incompleta")
            return
        
        self.__tip.setSize(self.__tip.getSize() - uso)
        
    def __str__(self):
        if self.hasLead():
            return f"calibre: {self.__thickness}, grafite: [{self.__tip}]"
        else:
            return f"calibre: {self.__thickness}, grafite: null"


def main():
    pencil:Pencil = Pencil()
    while True:
        line = input()
        print("$"+line) 
        args:list[str]=line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "init":
            pencil = Pencil(float(args[1]))
        elif args[0] == "show":
            print(pencil)
        elif args[0] == "insert":
            tip = Lead(float(args[1]), args[2], int(args[3]))
            pencil.insertLead(tip)
        elif args[0] == "remove":
            pencil.removeLead()
        elif args[0] == "write":
            pencil.writePage()
        else:
            print("fail: comando invalido")

main()