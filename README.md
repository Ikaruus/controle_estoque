# 📦 Controle de Estoque - FastAPI

Sistema de gerenciamento de estoque desenvolvido com **FastAPI**, seguindo arquitetura em camadas e boas práticas de organização de backend.

---

## 🎯 Contexto de Negócio (Simulação Real)
📌 Pedido da Área Comercial / Operações

A empresa enfrenta dificuldades para:

- Controlar produtos disponíveis em estoque
- Evitar vendas de itens indisponíveis
- Ter visibilidade rápida da quantidade atual
- Reduzir erros manuais em planilhas
- Centralizar informações em um único sistema

Atualmente, o controle é feito de forma manual (Excel), o que gera:

- Inconsistência de dados
- Falta de rastreabilidade
- Retrabalho
- Risco de prejuízo por falhas operacionais

💡 Solução Proposta

Desenvolvimento de uma API REST com interface web integrada, permitindo:

- Cadastro estruturado de produtos
- Armazenamento seguro em banco de dados
- Organização por arquitetura em camadas
- Interface simples para uso interno

---

## 🚀 Tecnologias Utilizadas

- Python 3.14
- FastAPI
- SQLAlchemy
- SQLite
- Jinja2
- Bootstrap 5
- Git & GitHub

---

## 🏗 Arquitetura

O projeto foi estruturado seguindo separação de responsabilidades:
controle_estoque/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── routes/
│ └── produtos.py
├── templates/
│ └── index.html
└── .gitignore


---

## ▶ Como executar o projeto

1. Clone o repositório:

git clone https://github.com/Ikaruus/controle_estoque.git

2. Instale as dependências:

pip install fastapi uvicorn sqlalchemy jinja2

3. Execute o servidor:

uvicorn main:app --reload

4. Acesse no navegador:

http://127.0.0.1:8000/interface

📌 Funcionalidades

✅ Cadastro de produtos
✅ Organização em camadas
✅ Banco SQLite
✅ Interface Web com Bootstrap
🚧 Evolução futura: edição, exclusão e deploy

👨‍💻 Desenvolvedor

Projeto desenvolvido por Dikson Ikaro Araujo Brizolara
Estudante de Ciência da Computação focado em Backend e Arquitetura de Software.

⭐ Se este projeto te ajudou ou chamou atenção, deixe uma estrela!

