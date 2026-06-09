def se(condicao,valor_se_verdadeiro,valor_se_falso):
    return (valor_se_verdadeiro if condicao else valor_se_falso)

alunos = [
    ("joao",40),
    ("maria",60),
    ("jose",94),
    ("pedro",70),
    ("ricardo",91),
    ("bruno",56),
    ("bruna",54),
    ("silas",51),
    ("patricia",36),
    ("tatiana",82),
    ("roseane",36),
    ("rebeca",62),
    ("carlos",65),
    ("marcos",73),
    ("adriana",91),
    ("adriano",92)
]
print(f"{'Aluno':^15} {'Nota':^6} {'situação':^12}")
print("-" * 38)

aprovados = 0
recuperacao = 0
reprovado = 0

print("\n --- Boletim escolar ---")
for nome, nota in alunos:
    situacao = se(nota >= 70,"APROVADO", se(nota >= 50, "RECUPERAÇÃO","REPROVADO"))
    print(f"{nome} | {nota} | {situacao}")

    if nota >= 70:
        aprovados += 1

    elif nota >= 50:
        recuperacao += 1

    else:
        reprovado += 1

print("-" * 38)
print(f"\nAprovados: {aprovados}\nRecuperação: {recuperacao}\nReprovados: {reprovado}\n")


