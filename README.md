# OrganizaMeAPI 📝

O OrganizaMeAPI é o back-end da plataforma OrganizaMe, uma aplicação de gerenciamento de tarefas, semelhante a um todolist. Este projeto foi desenvolvido utilizando o framework Django e oferece endpoints para o gerenciamento de tarefas e usuários.

## 🛠️ Tecnologias
- Django: Framework web Python utilizado para o desenvolvimento da web API.
- SQLite: Banco de dados leve e embutido escolhido para armazenamento dos dados.
- JWT (JSON Web Tokens): Autenticação utilizada nas operações de manipulação de tarefas.

## 🔑 Funcionalidades
- Autenticação e autorização de usuários via JWT.
- CRUD completo (Criar, Ler, Atualizar, Deletar) para gerenciar tarefas.
- Suporte a paginação e filtros na consulta das tarefas.
- Login e cadastro de usuários, permitindo que cada um visualize e gerencie suas próprias tarefas.

## 🚀 Como Executar o Projeto:
### 🛠️ Pré-requisitos  

Certifique-se de ter instalado:  
- [Python 3.8+](https://www.python.org/downloads/)  
- [Git](https://git-scm.com/)  

### 1️ - Clonagem do Repositório  

```bash
git clone https://github.com/MartinRenz/organizame-api.git
cd organizame-api
```

### 2 - Criação e Ativação do Ambiente Virtual  

```bash
python -m venv venv
```
- Windows:
```bash
venv\Scripts\activate
```
- Linux:
```bash
source venv/bin/activate
```

### 3 - Instalação das Dependências  
```bash
pip install -r requirements.txt
```

### 4 - Configuração do Banco de Dados  
```bash
python manage.py migrate
```

### 5 - Iniciando o Servidor  
```bash
python manage.py runserver
```

O backend estará disponível em http://127.0.0.1:8000/



