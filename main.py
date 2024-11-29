import tkinter as tk
from frontend.Views.Gerente import GerenteApp
from frontend.Views.Vendedor import VendedorApp
from frontend.Views.Mecanico import MecanicoApp
from frontend.Views.Secretaria import SecretariaApp
from frontend.Views.Login import LoginApp  # Importa a tela de login

# Função para abrir a view correta com base na função do usuário
def open_view(root, role):
    if role == "Gerente":
        GerenteApp(root)
    elif role == "Vendedor":
        VendedorApp(root)
    elif role == "Mecanico":
        MecanicoApp(root)
    elif role == "Secretaria":
        SecretariaApp(root)

# Iniciando a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root, open_view)  # Passa a função para abrir a view correta
    root.mainloop()

# troquei super por estilos
# revisar: em funcionário senha_atual
# revisar: ao atualizar moto duplicada na revisão muda para as duas

# readme github
# revisar comentários
# aviso caso cliente já cadastrado

# Placa das motos
# moto nova e usada
# cpf chave estrangeira
# adicionar botão sair

