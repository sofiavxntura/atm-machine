# Menu
saldo = 0.0

def ver_saldo():
  print(f"\nSeu saldo atual: R$ {saldo:.2f}")

def depositar():
  global saldo
  valor = float(input("\nValor do depósito: "))

  if valor > 0:
    saldo = saldo + valor
    print(f"O depósito de R$ {valor:.2f} foi efetuado com sucesso!")

  else:
    print("Valor inválido! Por favor, digite um valor positivo!")

def saque():
  global saldo
  sacar = float(input("\nValor do saque: "))

  if sacar > saldo:
    print(f"O seu saldo é insuficiente (R$ {saldo:.2f}). Por favor, saque uma quantia menor.")

  elif sacar > 0:
    saldo = saldo - sacar
    print(f"O saque de R$ {sacar:.2f} foi efe
