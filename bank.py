def clear():
   try:
      import os
      lines = os.get_terminal_size().lines
   except AttributeError:
      lines = 130
   print("\n" * lines)

menu = """
1. [e] Extrato(Check Balance)
2. [d] Deposito (Deposit)
3. [s] Saque (Withdraw)
4. [q] Sair (Exit)
"""

saldo=0
LIMITE_VALOR_SAQUE=500
extrato=""
numero_saques=0
LIMITE_SAQUES=3

while True:
   print(menu)
   opcao = input("Digite uma opção: ")
   opcao=opcao.lower()
   if opcao == "e" or opcao=="1":
      clear()
      print("="*50)
      print("Sem operações executadas" if not extrato else extrato)
      print("="*50)
      print("Seu saldo é de R${:.2f}".format(saldo))
   elif opcao == "d" or opcao=="2":
      deposito = input("Digite o valor do deposito: ")
      try:
         deposito = float(deposito)
      except:
         print("Valor digitado inválido")
         continue
      if deposito>0:
         extrato+= "Deposito de R${:.2f}\n".format(deposito)
         saldo += deposito
      else:
         print("Deposito inválido")
   elif opcao == "s" or opcao=="3":
      saque = input("Digite o valor do saque: ")
      try:
         saque = float(saque)
      except:
         print("Valor inválido")
         continue
      if saque>500:
         print("Limite de valor de saque excedido")
      elif numero_saques >= LIMITE_SAQUES:
         print("Você já efetuou seu limite de {} saques hoje".format(numero_saques))
      elif saque>0:
         if saque>(LIMITE_VALOR_SAQUE):
            print("Essa operação ultrapassa o limite da operacao")
         elif saque>(saldo):
            print("Essa operação ultrapassa o seu saldo")
         else:
            numero_saques += 1
            extrato +="{}".format(numero_saques) + ".o saque de R${:.2f}\n".format(saque)
            saldo -= saque
      else:
         print("Saque inválido")
   elif opcao == "q" or opcao=="4":
      break
   else:
      print("Opção inválida")
