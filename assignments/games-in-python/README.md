
# 📘 Assignment: Games in Python

## 🎯 Objective

Build a simple word game in Python that helps students practice strings, loops, conditionals, and user input while creating an interactive and playable experience.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Descrição
Create a Python program that selects a secret word from a predefined list and prepares the game state for the player.

#### Requisitos
O programa completo deve:

- Definir uma lista de palavras para o jogo
- Escolher uma palavra aleatoriamente no início de cada rodada
- Exibir a palavra escondida com espaços ou underscores, como _ _ _ _ _
- Manter a palavra escolhida oculta até que o jogador faça palpites

### 🛠️ Gameplay and Win/Loss Logic

#### Descrição
Implement the game loop that lets the player guess letters, updates the visible progress, and ends the game when the user wins or runs out of attempts.

#### Requisitos
O programa completo deve:

- Solicitar ao jogador que insira uma letra por vez
- Verificar se a letra pertence à palavra secreta
- Revelar as letras corretas na posição adequada
- Contar as tentativas erradas e as restantes
- Encerrar o jogo com uma mensagem de vitória quando a palavra for completada
- Encerrar o jogo com uma mensagem de derrota quando as tentativas acabarem