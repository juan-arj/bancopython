
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_DIARIO = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor a ser depositado: "))
        
        if valor > 0:
            saldo = valor + saldo
            extrato += f"Despósito: R$ {valor}\n"
        else:
            print("Operação falhou! O valor informado não é valido") 
        
    elif opcao == "s":
        valor = float(input("Digite o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques > LIMITE_DIARIO

        if excedeu_saldo:
            print('Você não possui saldo suficiente, tente novamente!')
        elif excedeu_limite:
            print("Operação falhou, o valor de saque excedeu o limite! ")
        elif excedeu_saques:
            print("Operação falhou! Limite de saque diário excedido. ")
        elif valor > 0:
            saldo = saldo - valor
            extrato += f"Saque R$ {valor:.2f}\n"
            


    elif opcao == "e":
        print("\n================ Extrato ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")
    
    elif opcao == "q":
        break

    else:
        print("Operação invalida, selecione novamente a opção desejada")
        