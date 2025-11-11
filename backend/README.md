# Backend Projeto

## 🚀 Como executar o projeto

Siga o passo a passo abaixo para configurar e executar o projeto corretamente em sua máquina.

### 1 Criar e ativar o ambiente virtual

Primeiro abra o terminal e entre na pasta chamada backend. Depois siga o passo a passo abaixo:

```bash
cd backend
```

💻 Windows
```bash
python -m venv .venv   # Cria o ambiente virtual
.venv\Scripts\activate  # Ativa o ambiente virtual
```

💻 Linux
```bash
python3 -m venv .venv   # Cria o ambiente virtual
source .venv/bin/activate  # Ativa o ambiente virtual
```

### 2 Instalar as dependências
```bash
pip install -r requirements.txt #Aqui vai instalar todas as dependencias do projeto
```

Verifique se os pacotes foram instalados corretamente:
```bash
pip list
```

### 3 Cria um arquivo chamado **.env** com as configurações do banco. Na raiz do projeto
```bash
FLASK_ENV=development
FLASK_APP=app.py
SECRET_KEY=uma_chave_secreta_aleatoria_123
DATABASE_USER= #seu usuario
DATABASE_PASSWORD= #sua senha
DATABASE_HOST=127.0.0.1
DATABASE_PORT=3306
DATABASE_NAME=brilhance_db #Nome do nosso banco

```
Nossa recomendação é utilizar o banco Mysql + Workbench

### 4 Cria um arquivo chamado **.env.prod** com as configurações do banco para produção. Na raiz do projeto
```bash
FLASK_ENV=production
FLASK_APP=app.py
FLASK_RUN_HOST=0.0.0.0
FLASK_RUN_PORT=5000 # Ou porta de sua preferencia

# Configuração do MySQL
DATABASE_USER= #Seu usuário
DATABASE_PASSWORD= # Sua senha
DATABASE_HOST=localhost
DATABASE_PORT=3306
DATABASE_NAME=brilhance_db #Nome do nosso banco

# Chave secreta 
SECRET_KEY=minha_chave_supersecreta

```
Nossa recomendação é utilizar o banco Mysql + 

### 🗄️ Banco de Dados
O projeto necessita de um banco de dados **MySQL** instalado na sua máquina.

1. Instale o [MySQL Server + Workbench](https://dev.mysql.com/downloads/installer/).  
2. Crie um banco de dados chamado **brilhance_db**.  
3. Configure as credenciais nos arquivos de ambiente `.env` (desenvolvimento).  


### 5 Caso necessario, ser é a primeira vez que esta rodando o projeto, realize as migrações do modelo para o banco de dados.

Primeiro verificar instalação da dependencia
```bash

pip list # Veja se tem algo parecido com Flask-Migrate

pip install Flask-Migrate

```

A pós isso iniciar as migrações
```bash

flask db init
flask db migrate -m "Mensagem descritiva da migração"
flask db upgrade

```

### 6 Roda Api

Com todos os passo seguido rode a api 
```bash
python app.py # Rodando apenas em sua maquina

ou

flask run --host=0.0.0.0 # Rodando em sua rede local *Acessivel a outros dispositivos.
```
---

## 🔄 Fluxo de trabalho com o Git
Quando estiver com o projeto em sua maquina sempre siga o fluxo abaixo para evitar conflitos e manter o código atualizado.

### 1️⃣ Antes de começar qualquer modificação
```bash
git pull origin main # Baixa todas as atualizações do repositório remoto antes de começar a trabalhar.
```

### 2️⃣ Após realizar alterações
Adicione todos os arquivos modificados:

```bash
git add .
```

Crie um commit com uma mensagem descritiva:

```bash
git commit -m "Descrição das alterações feitas"
```

Envie suas mudanças para o repositório remoto:

```bash
git push origin main # Envia suas alterações para o repositório
```

---