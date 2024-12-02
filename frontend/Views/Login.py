from .baseTelas import baseTelas
from .Abas.login import AbaLogin


class LoginApp(baseTelas):
    def __init__(self, root, open_view_callback):
        super().__init__(root,"Login")

        self.aba_login = AbaLogin(root,open_view_callback) 