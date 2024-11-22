import pandas as pd

# Estatísticas
def estatisticasFabricante(df, fabricante):
    if isinstance(df, pd.DataFrame):
        # Filtra os dados para o fabricante
        df_fabricante = df[df['fabricante'] == fabricante]

        if fabricante not in df['fabricante'].values:
            print(f"Erro: O fabricante '{fabricante}' não foi encontrado na base de dados.")
            return None  # Se o fabricante não for encontrado, retorna None

        df_fabricante = df_fabricante.dropna(subset=['valor_venda'])
        df_fabricante['valor_venda'] = pd.to_numeric(df_fabricante['valor_venda'], errors='coerce')

        media = df_fabricante['valor_venda'].mean()
        moda = df_fabricante['valor_venda'].mode()[0]
        mediana = df_fabricante['valor_venda'].median()
        total = df_fabricante['valor_venda'].sum()
        
        return media, moda, mediana, total
    return None
