class auto:

    def setSnelheid(self, s):
        if s > 239:
            print("Dat gaat veel te hard!")
        elif s < 0:
            print("Je kunt geen negatieve snelheid hebben!")
        else:
            self.__snelheid = s

    def getSnelheid(self):
        return self.__snelheid


if __name__ == '__main__':
    audi_tt = auto()
    audi_tt.setSnelheid(40)
    print(audi_tt.getSnelheid())


    maserati = auto()
    maserati.setSnelheid(350)
    print(maserati.getSnelheid())