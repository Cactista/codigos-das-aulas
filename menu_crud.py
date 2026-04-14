import sqlite3

#conectando ao banco de dados
conn = sqlite3.connect("bd_senai")
cursor = conn.cursor()

#criando a tabela com o campo id
cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT  NOT NULL,
        nota INTEGER                
        )"""
    )

# --- Adicionando aluno via imput do usuario
print("\n --- Adicionar Novo aluno ---")
nome_novo_aluno = input("Digite o nome do Novo aluno: ")
while True:
    try:
        nota_novo_aluno = int(input("Digite a nota do aluno novo (numero inteiro): "))
        break
    except ValueError:

        print("Entrada invalida, por favor digite um numero inteiro para a nota.")
cursor.execute("INSERT INTO alunos (nome, nota) VALUES (?,?)",(nome_novo_aluno, nota_novo_aluno))

conn.commit()

print(f"Aluno {nome_novo_aluno} com a nota {nota_novo_aluno} adicionado com sucesso ao banco de dados!\n")

print("=== Dados da tabela (sem ordenação)===\n")
cursor.execute("SELECT * FROM alunos")
alunos = cursor.fetchall()

for aluno in alunos:
    print(aluno) #mostra (id, nome, nota)
    print("\n" + "="*50)
