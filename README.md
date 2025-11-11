# 🛒 E-commerce Natalia - Frontend + Backend

<p align="start">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vuejs/vuejs-original.svg" alt="Vue.js" width="40" height="40"/>
  &nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" alt="JavaScript" width="40" height="40"/>
</p>

Projeto de E-commerce em desenvolvido com **VUE JS**, com o objetivo de criar uma aplicação web funcional e organizada para fins acadêmicos e de aprendizado.

---

## 🚀 Funcionalidades Implementadas
**Home Page**
- Estruturada com componentes dinâmicos.
- Seções de produtos, categorias e carrosséis.
- Responsividade (em ajustes finais).

**Autenticação**
- Sistema de **cadastro e login** funcional.
- Armazenamento do nome do usuário logado via **LocalStorage**.
- Exibição condicional do nome do usuário no header.

**Administração**
- Página administrativa acessível via rota:  
  ```
  /adm
  ```
- **(Ainda sem restrição de rotas)** – qualquer usuário pode acessar diretamente via URL.

**Design & Responsividade**
- Interface otimizada para desktop e mobile em andamento.
- Menu hamburguer com navegação em andamento.
- Ajustes de responsividade em andamento.

---

## 🌐 Integração com API

O frontend está **conectado ao backend via Axios**, consumindo dados e rotas disponibilizadas pela API.

- Backend desenvolvido em **Flask** (Python)
- Banco de dados utilizado: **MySQL**
- Comunicação realizada por **requisições HTTP (REST API)**

📘 Mais detalhes sobre a estrutura e endpoints da API podem ser encontrados no arquivo  
[`README.md` do Backend](./backend/README.md)

---

## 🚀 Como executar o projeto

Siga o passo a passo abaixo para configurar e executar o projeto corretamente em sua máquina.

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/mateus-gondev/E-commerce_Frontend_Natalia.git
cd E-commerce_Frontend_Natalia #Ou nome da pasta do projeto
```

### 2️ Instalar as dependências

**Ter Node.Js instalado no projeto**

Site com passo a passo completo -> https://nodejs.org/en/download
```bash
node -v # Versão node
```

```bash
npm install
 
# Utilize o npm vue-router para trabalhar com as rotas
npm instal vue-router

```

Verifique se os pacotes foram instalados corretamente:
```bash
npm list vue

#E tambem utilize o npm list para as outras dependencias
npm list
```

### 3️⃣ Executar o projeto
```bash
npm run dev #Para rodar o projeto
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
