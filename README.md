# Sistema de Gerenciamento de Concessionária de Motos

## 📋 Descrição

Este sistema de gerenciamento foi desenvolvido como parte da disciplina **Paradigmas Orientados a Objetos para Desenvolvimento de Software**, no curso de **Ciência da Computação** da **Universidade Estadual do Norte Fluminense (UENF)**. 

O projeto tem como objetivo atender às necessidades de uma concessionária de motos, aplicando conceitos de programação orientada a objetos (POO). Construído em Python, o sistema utiliza a biblioteca Tkinter para criar a interface gráfica e SQLite para gerenciar o banco de dados, oferecendo funcionalidades como administração de clientes, vendas, motos e agendamentos de revisões.

O sistema é estruturado para diferentes papéis dentro da concessionária: gerentes, vendedores, mecânicos e secretárias, cada um com permissões específicas para realizar suas funções, refletindo a separação de responsabilidades e o encapsulamento, fundamentos da POO.


## 🎯 Funcionalidades por Papel

### Gerente
- Acesso completo ao sistema.
- Visualizar, Adicionar, editar e remover:
  - **Motos**
  - **Clientes**
  - **Vendas**
  - **Revisões**
  - **Funcionários**
    
### Vendedor
- Visualizar motos cadastradas.
- Adicionar e editar clientes.
- Cadastrar e visualizar vendas.

### Mecânico
- Visualizar agendamentos de revisão.
- Atualizar o status das revisões.

### Secretária
- Visualizar motos e vendas.
- Criar e visualizar agendamentos de revisão.

## 📦 Funcionalidades Gerais

- **Cadastro de Clientes**: 
  - Adicionar, atualizar, listar e remover clientes no sistema, com registro de **nome**, **CPF** e **e-mail**.

- **Gerenciamento de Vendas**: 
  - Registro de vendas utilizando o **CPF do cliente** e o **chassi da moto** para associar a transação.
  - Visualização e edição de vendas realizadas.

- **Cadastro de Motos**: 
  - Adicionar novas motos ao sistema com os seguintes dados: **modelo**, **ano**, **preço**, **cor** e **chassi**.
  - Atualizar informações ou remover motos do estoque.

- **Agendamento de Revisões**: 
  - Criar agendamentos de revisões, vinculando a revisão ao **chassi da moto** e ao **CPF do cliente**.
  - Registrar o mecânico responsável e a data programada.

- **Cadastro de Funcionários**:
  - Gerenciar funcionários, registrando **nome**, **CPF** e **cargo**.

## 🛠️ Tecnologias Utilizadas

- **Python**: 
  - Linguagem principal para desenvolvimento.
- **Tkinter**: 
  - Biblioteca nativa do Python para interfaces gráficas.
- **SQLite**: 
  - Sistema de banco de dados leve e eficiente integrado ao Python.

