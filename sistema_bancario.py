def menu():
    menu = """
    == Sistema bancario ==
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar Usuario
    [5] Criar Conta
    [0] Sair

    => """
    return input(menu)


def deposito(saldo, extrato, /):

    deposito = float(input("Informe o valor do deposito: "))

    if deposito <= 0:
        print("O valor informado e invalido")
        return saldo, extrato

    saldo += deposito
    extrato += f"Deposito: R$ {deposito:5.2f}\n"
    print(f"Deposito de R$ {deposito:5.2f} realizado com sucesso!")
    return saldo, extrato


def saque(*, saldo, limite, extrato, numero_saques, limite_saques):

    if numero_saques >= limite_saques:
        print("Limite de saque diario atingido!")
        return saldo, numero_saques, extrato

    saque = float(input("Informe o valor do saque: "))

    if saque > limite:
        print(f"O valor limite = R$ {limite:5.2f}")
        return saldo, numero_saques, extrato

    if saque > saldo:
        print("Saldo insuficiente!")
        return saldo, numero_saques, extrato

    if saque <= 0:
        print("O valor informado e invalido")
        return saldo, numero_saques, extrato

    print(f"Saque de R$ {saque:5.2f} realizado com sucesso!")
    saldo -= saque
    extrato += f"Saque:    R$ {saque:5.2f}\n"
    numero_saques += 1
    return saldo, numero_saques, extrato


def exibir_extrato(saldo, /, *, extrato):
    print(f"\nExtrato bancario\n{extrato}")
    print()
    print(f"Saldo: R$ {saldo:.2f}")


def criar_usuario(usuarios):
    nome = input("Digite o nome: ")
    cpf = input("Digite o cpf: ")
    if check_usuario(usuarios, cpf):
        print("CPF ja cadastrado!")
        return
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
    endereco = input(
        "Digite o endereco (logradouro, nro - bairro - cidade/sigla estado): "
    )
    usuarios.append(
        {
            "nome": nome,
            "cpf": cpf,
            "data_nascimento": data_nascimento,
            "endereco": endereco,
        }
    )
    print("Cadastro realizado com sucesso!")


def check_usuario(usuarios, cpf):
    for usuarios in usuarios:
        if usuarios["cpf"] == cpf:
            return True


def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o cpf do cliente: ")

    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        numero_conta += 1
        contas.append(
            {
                "agencia": agencia,
                "numero_conta": numero_conta,
                "usuarios": usuario_encontrado,
            }
        )
        print("Conta criada  com sucesso!")
        return numero_conta

    print("CPF nao encontrado!")
    return numero_conta


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    numero_conta = 0

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "1":
            saldo, extrato = deposito(saldo, extrato)

        elif opcao == "2":
            saldo, numero_saques, extrato = saque(
                saldo=saldo,
                limite=limite,
                extrato=extrato,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = criar_conta(AGENCIA, numero_conta, usuarios, contas)

        elif opcao == "0":
            break

        else:
            print(
                "Operacao invalida, por favor selecione novamente a operacao desejada."
            )


main()
