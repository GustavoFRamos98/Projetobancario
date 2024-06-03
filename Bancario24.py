saldo = 0.0
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(valor):
    global saldo
    if valor <= 0:
        print("\nDepósito não pode ser de valor negativo ou zero.")
    else:
        saldo += valor
        extrato.append(f"Depósito: +R${valor:.2f}")
        print(f"\nDepósito de R${valor:.2f} realizado com sucesso.")

def sacar(valor):
    global saldo, numero_saques
    if numero_saques >= LIMITE_SAQUES:
        print("Limite de saques diários atingido. Não é possível realizar mais saques.")
    elif valor <= 0:
        print("Saque não pode ser de valor negativo ou zero.")
    elif valor > 1100:
        print("Limite de saque é de R$1100.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    else:
        saldo -= valor
        numero_saques += 1
        extrato.append(f"\nSaque: -R${valor:.2f}")
        print(f"\nSaque de R${valor:.2f} realizado com sucesso.")

def ver_extrato():
    print("\n=====================EXTRATO=======================")
    print("Extrato bancário:")
    for operacao in extrato:
        print(operacao)
    print(f"\nSaldo atual: R${saldo:.2f}")

def menu():
    while True:
        print("\n--- Sistema Bancário ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Ver Extrato")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor para depósito: "))
            depositar(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor para saque: "))
            sacar(valor)
        elif opcao == '3':
            ver_extrato()
        elif opcao == '4':
            print("Obrigado pela preferência. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
