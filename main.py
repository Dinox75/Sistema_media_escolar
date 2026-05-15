def mostrar_linha():
    print("-" * 50)


def ler_numero(mensagem):
    while True:
        entrada = input(mensagem).strip()

        if entrada == "":
            print("Entrada inválida. Este campo não pode ficar em branco.\n")
            continue

        entrada = entrada.replace(",", ".")

        try:
            valor = float(entrada)

            if valor < 0 or valor > 10:
                print("Valor inválido. Digite um número entre 0 e 10.\n")
                continue

            return valor

        except ValueError:
            print("Entrada inválida. Digite apenas números. Exemplo: 7.5\n")


def cadastrar_materias():
    materias = []

    print("\n=== CADASTRO DE MATÉRIAS ===")
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

        materias_normalizadas = [m.lower() for m in materias]

        if materia.lower() in materias_normalizadas:
            print("Essa matéria já foi cadastrada. Digite outra.\n")
            continue

        materias.append(materia)
        print(f"Matéria adicionada: {materia}\n")

    return materias


def configurar_medias():
    print("\n=== CONFIGURAÇÃO DAS MÉDIAS ===")
    print("Defina as regras de aprovação e recuperação.")
    mostrar_linha()

    while True:
        media_aprovacao = ler_numero("Digite a média mínima para aprovação: ")
        media_recuperacao = ler_numero("Digite a média mínima para recuperação: ")

        if media_recuperacao >= media_aprovacao:
            print("\nA média de recuperação precisa ser menor que a média de aprovação.")
            print("Configure os valores novamente.\n")
            continue

        return media_aprovacao, media_recuperacao


def registrar_notas(materias):
    notas = {}

    print("\n=== REGISTRO DE NOTAS ===")
    print("Agora informe as notas de cada matéria.")
    print("As notas devem estar entre 0 e 10.")
    mostrar_linha()

    for materia in materias:
        nota = ler_numero(f"Digite a nota de {materia}: ")
        notas[materia] = nota

    return notas


def calcular_media(notas):
    soma = sum(notas.values())
    media = soma / len(notas)
    return media


def exibir_boletim(notas):
    print("\n=== BOLETIM DO ALUNO ===")

    for materia, nota in notas.items():
        print(f"{materia}: {nota:.2f}")


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


def main():
    print("\n=== SISTEMA DE MÉDIA ESCOLAR ===")

    materias = cadastrar_materias()

    if len(materias) == 0:
        print("\nNenhuma matéria foi cadastrada.")
        print("Não é possível calcular a média sem matérias.")
        print("Programa encerrado.")
        return

    media_aprovacao, media_recuperacao = configurar_medias()

    notas = registrar_notas(materias)

    exibir_boletim(notas)

    media_final = calcular_media(notas)

    verificar_aprovacao(media_final, media_aprovacao, media_recuperacao)


if __name__ == "__main__":
    main()