import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
import os

# 1. Dados de conexão com o PostgreSQL
#private_code

# 2. Cria a engine de conexão
engine = create_engine(f"postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}")

# 3. Caminho da pasta com os arquivos
caminho_pasta = r"C:\Users\tomas\OneDrive\Downloads\Linkedin\Projeto sales portfólio 12072025"

# 4. Mapeamento dos arquivos e nomes das tabelas de destino
arquivos_tabelas = {
    "dim_vendedores.xlsx": "d_salesman",
    "dim_produtos.xlsx": "d_products",
    "base_vendas_desagregada.xlsx": "f_sales"
}

# 5. Itera sobre os arquivos e insere os dados no banco
for arquivo, nome_tabela in arquivos_tabelas.items():
    caminho_arquivo = os.path.join(caminho_pasta, arquivo)
    
    # Lê o Excel
    df = pd.read_excel(caminho_arquivo)
    
    # Adiciona a data de carga
    df['data_carga_dados'] = datetime.now()
    
    # Substitui os dados da tabela
    df.to_sql(
        name=nome_tabela,
        con=engine,
        schema="sales_portfolio",
        if_exists="replace",  # substitui a tabela inteira
        index=False
    )

print("Avanti Palestra")

