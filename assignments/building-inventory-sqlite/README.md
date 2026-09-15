# 📘 Atividade: Sistema de Inventário com SQLite

## 🎯 Objetivo

Construa um sistema de inventário em Python que armazene produtos de forma persistente usando SQLite. Você praticará modelagem de dados, consultas SQL, operações CRUD e validação de entradas em uma aplicação de linha de comando.

## 📝 Tarefas

### 🛠️ Criar o Banco de Dados e o Modelo de Produtos

#### Descrição

Implemente a inicialização de um banco SQLite local e crie a tabela `products`. Cada produto deve ter um identificador, nome, categoria, quantidade e preço.

#### Requisitos

O programa concluído deve:

- Abrir ou criar o arquivo `inventory.db` usando a biblioteca padrão `sqlite3`.
- Criar a tabela `products` automaticamente quando o programa iniciar.
- Definir `id` como chave primária e usar tipos adequados para os demais campos.
- Inserir pelo menos três produtos de exemplo somente quando a tabela estiver vazia.
- Fechar a conexão com o banco de dados corretamente.

### 🛠️ Implementar as Operações de Inventário

#### Descrição

Complete as funções do starter code para permitir o gerenciamento dos produtos. As operações devem usar consultas parametrizadas e retornar dados úteis para o restante do programa.

#### Requisitos

O programa concluído deve:

- Cadastrar um produto com nome, categoria, quantidade e preço.
- Listar todos os produtos ordenados pelo nome.
- Buscar produtos por nome ou categoria sem diferenciar maiúsculas e minúsculas.
- Atualizar a quantidade de um produto existente.
- Remover um produto pelo seu identificador.
- Informar claramente quando um produto não for encontrado.
- Usar parâmetros nas consultas SQL em vez de concatenar valores fornecidos pelo usuário.

### 🛠️ Criar a Interface e os Relatórios do Inventário

#### Descrição

Crie um menu de linha de comando para reunir as operações e adicione um relatório que ajude a acompanhar o estoque.

#### Requisitos

O programa concluído deve:

- Exibir opções para cadastrar, listar, buscar, atualizar, remover e sair.
- Validar entradas numéricas, impedindo quantidades negativas e preços menores ou iguais a zero.
- Tratar erros de banco de dados sem encerrar a aplicação inesperadamente.
- Exibir o valor total do estoque, calculado como `quantidade × preço` para cada produto.
- Mostrar quais produtos precisam de reposição quando a quantidade for menor ou igual a 5.
- Permitir executar várias operações até que o usuário escolha sair.
