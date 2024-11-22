import pandas as pd
from funcoes.dados import tratandoDados, tratandoDadosMarca
from funcoes.estatisticas import estatisticasFabricante
from funcoes.graficos import graficoBarras, graficoBarraDeitado, graficoPizza

# URL do Google Sheets
url = "https://docs.google.com/spreadsheets/d/1wuAEPvbt8m8soW-tV73jTru114NjKR6jMBxfMj6jf88/edit?usp=sharing"

# Usando pandas para ler diretamente a planilha do Google Sheets
sheet_url = url.replace("/edit?usp=sharing", "/gviz/tq?tqx=out:csv")
df = pd.read_csv(sheet_url)

print('Nomes dos Fabricantes\n')
for fabricante in df['fabricante'].unique():
    print(fabricante)
print('--- --- ---\n')

# Solicita o nome da marca ou modelo do carro
fabricante = input('Insira o Fabricante:\n')

# Verificar se o fabricante existe no DataFrame
if fabricante in df['fabricante'].values:
    print(f"\nExecutando análises para o fabricante: {fabricante}\n")
    
    # Obter dados agrupados para o fabricante
    df_agrupado = tratandoDados(df)

    # Gráficos de vendas por fabricante
    graficoBarras(df_agrupado)
    print('\n')

    # Dados da marca/modelo
    carro = tratandoDadosMarca(df, fabricante)
    print('\n')
    graficoBarraDeitado(carro)
    print('\n')

    # Estatísticas do fabricante
    media, moda, mediana, total = estatisticasFabricante(df, fabricante)
    if media and moda and mediana and total:
        graficoPizza(moda, media, mediana, total, fabricante)
else:
    print(f"Erro: O fabricante '{fabricante}' não foi encontrado na base de dados.")
