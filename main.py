from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
import pandas as pd

# Histórico de compras
historico = [
    ['Passagem', 'Hotel'],
    ['Passagem', 'Seguro'],
    ['Passagem', 'Hotel', 'Seguro'],
    ['Passagem', 'Hotel'],
    ['Passagem', 'Seguro']
]

# Preparação dos dados para o Apriori
te = TransactionEncoder()
te_array = te.fit(historico).transform(historico)

df = pd.DataFrame(te_array, columns=te.columns_)

# Descobre padrões frequentes
frequentes = apriori(df, min_support=0.4, use_colnames=True)

print("=== Sistema de Análise de Compras ===")
print("Itens disponíveis: Passagem, Hotel, Seguro")

# Usuário digita a compra
entrada = input("Digite os itens comprados separados por vírgula: ")

nova_compra = set(item.strip() for item in entrada.split(","))

# Verifica se existe algum padrão conhecido
encontrou = False

for itemset in frequentes["itemsets"]:
    if itemset == nova_compra:
        encontrou = True
        break

if encontrou:
    print("\n✅ Compra dentro dos padrões históricos.")
else:
    print("\n⚠️ ALERTA!")
    print("Combinação de compra incomum ou fora do padrão.")