class kalkulator(object):

    def jumlah(self,a,b):
        return (a+b)
    def kurang (self,a,b):
        return (a-b)

if __name__ == "__main__":
    k = kalkulator()
    print(k.jumlah(50,60))