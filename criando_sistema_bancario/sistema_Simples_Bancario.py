menu = """
O que você deseja!
[d] Depositar
[s] Sacar
[e] Extrato
[q] sair
"""

saldo = 0
limite = 500
extrato = " "
numero_saque = 0
LIMITE_SAQUE = 3


while True:
    opcao = input(menu)
     
    if opcao == "d":
        valor = float(input("Informe o vlor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depóito : R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        execedeu_saldo = valor > saldo
        execedeu_limite = valor > limite
        execedeu_saque = numero_saque >= LIMITE_SAQUE

        if execedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif execedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        
        elif execedeu_saque:
            print("Operação falhou! Número máximo de saques excedido")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1

        else: 
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n============== EXTRATO ==============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=======================================")

    elif opcao =="q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")