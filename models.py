class BusinessInfo:
    def __init__(self):
        self.Name = ""
        self.TradeName = ""
        self.Type = ''
        self.NUI = ''
        self.BusinessNo = ""
        self.FiscalNo = ""
        self.NoOfEmployees = 0
        self.RegistrationDate = None
        self.Municipality = ""
        self.Address = ""
        self.PhoneNo = ""
        self.Email = ''
        self.KBRAStatus = ''
        self.TAKStatus = ''
        self.BaseURL = ''

    def __str__(self):
        info = f'Emri i biznesit: {self.Name}\n{"="* 50}\n'
        info += f'Emri tregtar: {self.TradeName}\n{"="* 50}\n'
        info += f'Lloji biznesit: {self.Type}\n{"="* 50}\n'
        info += f'Numri unik identifikues: {self.NUI}\n{"="* 50}\n'
        info += f'Numri i biznesit: {self.BusinessNo}\n{"="* 50}\n'
        info += f'Numri Fiskal: {self.FiscalNo}\n{"="* 50}\n'
        info += f'Numri punëtorëve: {self.NoOfEmployees}\n{"="* 50}\n'
        info += f'Data e regjistrimit: {self.RegistrationDate}\n{"="* 50}\n'
        info += f'Komuna: {self.Municipality}\n{"="* 50}\n'
        info += f'Adresa: {self.Address}\n{"="* 50}\n'
        info += f'Telefoni: {self.PhoneNo}\n{"="* 50}\n'
        info += f'E-mail: {self.Email}\n{"="* 50}\n'
        info += f'Statusi në ARBK: {self.KBRAStatus}\n{"="* 50}\n'
        info += f'Statusi në ATK: {self.TAKStatus}\n{"="* 50}\n'
        info += f'URL: {self.BaseURL}\n{"="* 50}\n'

        return info
