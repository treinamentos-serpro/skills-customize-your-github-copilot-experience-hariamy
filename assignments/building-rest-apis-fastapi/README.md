# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objetivo

Aprenda a construir uma API REST com FastAPI, definir modelos de dados com validação e implementar endpoints HTTP para consultar e cadastrar recursos.

## 📝 Tarefas

### 🛠️ Criar e Executar a API

#### Descrição

Complete a configuração inicial do projeto no arquivo `starter-code.py`, instale as dependências necessárias e execute a aplicação FastAPI com Uvicorn. Verifique a documentação interativa gerada automaticamente em `/docs`.

#### Requisitos

O programa concluído deve:

- Criar uma instância de `FastAPI` com um título descritivo
- Disponibilizar um endpoint `GET /health` que retorne o status da API
- Iniciar localmente com Uvicorn sem apresentar erros
- Exibir documentação OpenAPI acessível em `/docs`

### 🛠️ Modelar e Listar Livros

#### Descrição

Use um modelo Pydantic para representar livros e implemente o endpoint que retorna todos os livros armazenados em memória.

#### Requisitos

O programa concluído deve:

- Definir um modelo `Book` com `title`, `author` e `year`
- Validar os dados recebidos usando o modelo Pydantic
- Implementar `GET /books` com resposta JSON contendo uma lista de livros
- Retornar pelo menos dois livros de exemplo quando a aplicação iniciar

### 🛠️ Criar e Buscar Livros

#### Descrição

Implemente os endpoints para cadastrar um livro e buscar um livro específico pelo seu identificador. A API deve informar ao cliente quando o recurso solicitado não existir.

#### Requisitos

O programa concluído deve:

- Implementar `POST /books` recebendo um objeto `Book`
- Atribuir um identificador único ao novo livro e retorná-lo na resposta
- Implementar `GET /books/{book_id}` para buscar um livro pelo identificador
- Retornar status HTTP `404` quando o identificador não existir
- Testar os endpoints usando a documentação em `/docs` ou um cliente HTTP
