materias = []
notas = {}


def mostrar_linha():
    print("-" * 50)


def ler_media_configurada(nome_media):
    while True:
        entrada = input(f"Digite a {nome_media}: ").strip()

        if entrada == "":
            print("Esse campo não pode ficar em branco.\n")
            continue

        entrada = entrada.replace(",", ".")

        try:
            valor = float(entrada)

            if valor < 0 or valor > 10:
                print("Digite um valor entre 0 e 10.\n")
                continue

            return valor

        except ValueError:
            print("Entrada inválida. Digite apenas números. Exemplo: 7.0\n")


def calcular_media(notas):
    soma = sum(notas.values())
    media = soma / len(notas)
    return media


def verificar_aprovacao(media, media_aprovacao, media_recuperacao):
    mostrar_linha()

    if media >= media_aprovacao:
        print("SITUAÇÃO FINAL: APROVADO")
        print(f"Média final: {media:.2f}")
        print(f"Média necessária para aprovação: {media_aprovacao:.2f}")
        print("Parabéns! O aluno atingiu a média necessária.")

    elif media >= media_recuperacao:
        print("SITUAÇÃO FINAL: RECUPERAÇÃO")
        print(f"Média final: {media:.2f}")
        print(f"Média mínima para recuperação: {media_recuperacao:.2f}")
        print("O aluno ainda tem chance de recuperar a nota.")

    else:
        print("SITUAÇÃO FINAL: REPROVADO")
        print(f"Média final: {media:.2f}")
        print(f"Média mínima para recuperação: {media_recuperacao:.2f}")
        print("O aluno não atingiu a média mínima necessária.")

    mostrar_linha()


print("\n=== SISTEMA DE MÉDIA ESCOLAR ===")
print("Cadastre as matérias ou módulos da grade curricular.")
print("Digite 'sair' quando terminar o cadastro.")
mostrar_linha()


while True:
    materia = input("Digite o nome da matéria/módulo: ").strip()

    if materia == "":
        print("Entrada inválida. O nome da matéria não pode ficar em branco.\n")
        continue

    if materia.lower() == "sair":
        break

    if materia.lower() in [m.lower() for m in materias]:
        print("Essa matéria já foi cadastrada. Digite outra.\n")
        continue

    materias.append(materia)
    print(f"Matéria adicionada: {materia}\n")


if len(materias) == 0:
    print("\nNenhuma matéria foi cadastrada.")
    print("Não é possível calcular a média sem matérias.")
    print("Programa encerrado.")

else:
    print("\n=== CONFIGURAÇÃO DAS MÉDIAS ===")
    print("Agora defina as regras de aprovação do aluno.")
    mostrar_linha()

    media_aprovacao = ler_media_configurada("média mínima para aprovação")
    media_recuperacao = ler_media_configurada("média mínima para recuperação")

    while media_recuperacao >= media_aprovacao:
        print("\nA média de recuperação precisa ser menor que a média de aprovação.")
        print("Configure novamente os valores.\n")

        media_aprovacao = ler_media_configurada("média mínima para aprovação")
        media_recuperacao = ler_media_configurada("média mínima para recuperação")

    print("\n=== MATÉRIAS CADASTRADAS ===")

    for index, materia in enumerate(materias, start=1):
        print(f"{index} - {materia}")

    mostrar_linha()
    print("Agora informe as notas de cada matéria.")
    print("As notas devem estar entre 0 e 10.")
    mostrar_linha()

    for materia in materias:
        while True:
            entrada = input(f"Digite a nota de {materia}: ").strip()

            if entrada == "":
                print("A nota não pode ficar em branco.\n")
                continue

            entrada = entrada.replace(",", ".")

            try:
                nota = float(entrada)

                if nota < 0 or nota > 10:
                    print("Nota inválida. Digite um valor entre 0 e 10.\n")
                    continue

                notas[materia] = nota
                break

            except ValueError:
                print("Entrada inválida. Digite apenas números. Exemplo: 7.5\n")

    print("\n=== BOLETIM DO ALUNO ===")

    for materia, nota in notas.items():
        print(f"{materia}: {nota:.2f}")

    media_final = calcular_media(notas)

    verificar_aprovacao(media_final, media_aprovacao, media_recuperacao)