import seaborn as sns
import matplotlib.pyplot as plt

# Função para criar gráfico de barras
def graficoBarras(df_agrupado):
    sns.barplot(data=df_agrupado, x='fabricante', y='valor_venda', color='gray', width=0.5)
    plt.title('Vendas por Fabricante')
    plt.xlabel('Fabricantes')
    plt.ylabel('Vendas')
    plt.xticks(rotation=45)
    plt.show()

# Função para gráfico de barras horizontal
def graficoBarraDeitado(df_agrupado):
    if df_agrupado.empty or df_agrupado.isna().any().any():
        print("Erro: o DataFrame está vazio.")
        return
    sns.barplot(data=df_agrupado, x='valor_venda', y='modelo', hue='modelo', legend=False)
    plt.title('Valor Total de Vendas por Modelo')
    plt.xlabel('Valor Total de Vendas')
    plt.show()

# Função para gráfico de pizza
def graficoPizza(moda, media, mediana, total, fabricante):
    valores = [moda, media, mediana]
    labels = ['Moda das Vendas', 'Média das Vendas', 'Mediana das Vendas']
    cores = ['#66b3ff', '#99ff99', '#ffcc99']
    plt.figure(figsize=(8, 6))
    plt.pie(
        valores,
        labels=labels,
        colors=cores,
        autopct=lambda p: f'{p:.1f}%\n(R${p * sum(valores) / 100:,.2f})',
        startangle=90
    )
    plt.title(f"Estatísticas do Fabricante: {fabricante}\n(Total: R${total:,.2f})", fontsize=14)
    plt.tight_layout()
    plt.show()
