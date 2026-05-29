# 🛒 Sistema de Análise de Compras com Apriori

## 📌 Descrição

Este projeto implementa um **sistema simples de análise de padrões de compras** utilizando o algoritmo **Apriori**, uma técnica de **mineração de dados** usada para identificar combinações frequentes de itens em históricos de transações.

O sistema analisa compras anteriores e verifica se uma nova combinação de itens informada pelo usuário está **dentro dos padrões históricos** ou se representa uma **compra incomum**.

---

## 🎯 Objetivo

O objetivo do projeto é demonstrar, de forma prática, como a técnica de **Data Mining (Mineração de Dados)** pode ser aplicada para identificar padrões de comportamento em compras, ajudando na detecção de transações fora do padrão.

Esse tipo de análise pode ser utilizado em:

* Sistemas de recomendação de produtos
* Detecção de fraudes
* Análise de comportamento do consumidor
* Inteligência de negócios (Business Intelligence)

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Pandas** → Manipulação de dados
* **Mlxtend** → Implementação do algoritmo Apriori

---

## 📂 Estrutura do Código

O sistema segue as seguintes etapas:

1. **Definição do histórico de compras**

   * São armazenadas transações contendo combinações de itens comprados anteriormente.

2. **Transformação dos dados**

   * O `TransactionEncoder` converte os dados para um formato binário compatível com o algoritmo Apriori.

3. **Mineração de padrões**

   * O algoritmo `apriori()` identifica conjuntos de itens frequentes com suporte mínimo de **40%**.

4. **Entrada do usuário**

   * O usuário informa uma nova compra digitando os itens separados por vírgula.

5. **Validação da compra**

   * O sistema verifica se a combinação já existe nos padrões históricos.
   * Caso exista, a compra é considerada **normal**.
   * Caso contrário, é exibido um **alerta de comportamento incomum**.

---

## 📊 Histórico de Compras Utilizado

O sistema trabalha inicialmente com o seguinte histórico:

| Compra | Itens                   |
| ------ | ----------------------- |
| 1      | Passagem, Hotel         |
| 2      | Passagem, Seguro        |
| 3      | Passagem, Hotel, Seguro |
| 4      | Passagem, Hotel         |
| 5      | Passagem, Seguro        |

Itens disponíveis:

* Passagem
* Hotel
* Seguro

---

## ▶️ Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/Gihyaa/Fraudes-com-Apriori
```

### 2. Instale as dependências

```bash
pip install pandas mlxtend
```

### 3. Execute o programa

```bash
python main.py
```

---

## 💻 Exemplo de Uso

### Entrada do usuário:

```text
Digite os itens comprados separados por vírgula: Passagem, Hotel
```

### Saída:

```text
✅ Compra dentro dos padrões históricos.
```

---

### Entrada incomum:

```text
Digite os itens comprados separados por vírgula: Hotel, Seguro
```

### Saída:

```text
⚠️ ALERTA!
Combinação de compra incomum ou fora do padrão.
```

---

## 📚 Conceitos Aplicados

* Mineração de Dados (Data Mining)
* Algoritmo Apriori
* Análise de padrões frequentes
* Suporte mínimo (*minimum support*)
* Segurança e detecção de anomalias

---

## 👨‍💻 Autor

Projeto desenvolvido para fins acadêmicos e aprendizado sobre **mineração de dados e análise de padrões de compra**.

