class Orcamentos():
    def __init__(self, pac, nomeorc, proc1, val1, pag1, proc2, val2, pag2, proc3, val3, pag3, proc4, val4, pag4, proc5, val5, pag5, proc6, val6, pag6, descr,data=""):
        self.__nomeorc = nomeorc
        self.__descr = descr
        self.__proc1 = proc1
        self.__val1 = val1
        self.__pag1 = pag1
        self.__proc2 = proc2
        self.__val2 = val2
        self.__pag2 = pag2
        self.__proc3 = proc3
        self.__val3 = val3
        self.__pag3 = pag3
        self.__proc4 = proc4
        self.__val4 = val4
        self.__pag4 = pag4
        self.__proc5 = proc5
        self.__val5 = val5
        self.__pag5 = pag5
        self.__proc6 = proc6
        self.__val6 = val6
        self.__pag6 = pag6
        self.__data = data
        self.__pac = pac

    @property
    def pac(self):
        return self.__pac

    @pac.setter
    def pac(self, pac):
        self.__pac = pac

    @property
    def nomeorc(self):
        return self.__nomeorc

    @nomeorc.setter
    def nomeorc(self, nomeorc):
        self.__nomeorc = nomeorc

    @property
    def descr(self):
        return self.__descr

    @descr.setter
    def descr(self, descr):
        self.__descr = descr

    @property
    def proc1(self):
        return self.__proc1

    @proc1.setter
    def proc1(self, proc1):
        self.__proc1 = proc1

    @property
    def val1(self):
        return self.__val1

    @val1.setter
    def val1(self, val1):
        self.__val1 = val1

    @property
    def pag1(self):
        return self.__pag1

    @pag1.setter
    def pag1(self, pag1):
        self.__pag1 = pag1

    @property
    def proc2(self):
        return self.__proc2

    @proc2.setter
    def proc2(self, proc2):
        self.__proc2 = proc2

    @property
    def val2(self):
        return self.__val2

    @val2.setter
    def val2(self, val2):
        self.__val2 = val2

    @property
    def pag2(self):
        return self.__pag2

    @pag2.setter
    def pag2(self, pag2):
        self.__pag2 = pag2

    @property
    def proc3(self):
        return self.__proc3

    @proc3.setter
    def proc3(self, proc3):
        self.__proc3 = proc3

    @property
    def val3(self):
        return self.__val3

    @val3.setter
    def val3(self, val3):
        self.__val3 = val3

    @property
    def pag3(self):
        return self.__pag3

    @pag3.setter
    def pag3(self, pag3):
        self.__pag3 = pag3

    @property
    def proc4(self):
        return self.__proc4

    @proc4.setter
    def proc4(self, proc4):
        self.__proc4 = proc4

    @property
    def val4(self):
        return self.__val4

    @val4.setter
    def val4(self, val4):
        self.__val4 = val4

    @property
    def pag4(self):
        return self.__pag4

    @pag4.setter
    def pag4(self, pag4):
        self.__pag4 = pag4

    @property
    def proc5(self):
        return self.__proc5

    @proc5.setter
    def proc5(self, proc5):
        self.__proc5 = proc5

    @property
    def val5(self):
        return self.__val5

    @val5.setter
    def val5(self, val5):
        self.__val5 = val5

    @property
    def pag5(self):
        return self.__pag5

    @pag5.setter
    def pag5(self, pag5):
        self.__pag5 = pag5

    @property
    def proc6(self):
        return self.__proc6

    @proc6.setter
    def proc6(self, proc6):
        self.__proc6 = proc6

    @property
    def val6(self):
        return self.__val6

    @val6.setter
    def val6(self, val6):
        self.__val6 = val6

    @property
    def pag6(self):
        return self.__pag6

    @pag6.setter
    def pag6(self, pag6):
        self.__pag6 = pag6

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data