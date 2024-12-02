from .baseTelas import baseTelas
from .Abas.moto import AbaMotos
from .Abas.venda import AbaVendas
from .Abas.revisao import AbaAgenda

class SecretariaApp(baseTelas):
    def __init__(self, root):
        super().__init__(root,"secretária")
    
        self.aba_motos = AbaMotos(root,self.notebook,"secretaria")
        self.aba_vendas = AbaVendas(root,self.notebook,"secretaria")
        self.aba_agenda = AbaAgenda(root,self.notebook,"secretaria")
