import pandas as pd

# Função para tratar os dados gerais
def tratandoDados(df):
    df = df.dropna(subset=['fabricante', 'valor_venda'])
    df['valor_venda'] = pd.to_numeric(df['valor_venda'], errors='coerce')
    return agruparDados(df)

# Função para agrupar os dados por fabricante
def agruparDados(df):
    fabricante_valor = df.groupby('fabricante')['valor_venda'].sum().reset_index()
    fabricante_valor = fabricante_valor.sort_values(by='valor_venda', ascending=False)
    return fabricante_valor

# Função para tratar dados específicos de uma marca ou modelo
def tratandoDadosMarca(df, modelo):
    df = df.dropna(subset=['fabricante', 'valor_venda', 'modelo'])
    df['valor_venda'] = pd.to_numeric(df['valor_venda'], errors='coerce')
    df_filtrado = df[df['fabricante'] == modelo]
    modelo_valor = df_filtrado.groupby('modelo')['valor_venda'].sum().reset_index()
    modelo_valor = modelo_valor.sort_values(by='valor_venda', ascending=False)
    return modelo_valor
