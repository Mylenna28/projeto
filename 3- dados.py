import sqlite3

# 1- Conectando no BD
conexao = sqlite3.connect('titulo.db')

cursor = conexao.cursor()

# 2-Inserindo Dados
cursor.execute(
    """
        INSERT INTO time(nome, ano, titulo)
        VALUES ('flamengo', 1985, 3.7)
    """
)

conexao.commit()
conexao.close()