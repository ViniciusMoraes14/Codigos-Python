CLIENTES = []
CNPJs = []
def add_cliente(cnpj):
  print()
  print('Digite X - quando não quiser adiocionar mais Clientes!')
  print('Deve ser digitado apenas os números do CNPJ para consulta!')
  print('EXEMPLO: 00000000000000')
  print()
  
  while True:
    cnpj = input("Digite o CNPJ: ").upper()
    if cnpj == 'X':
      break
    if cnpj not in CNPJs:
      if len(cnpj) == 14:
        import requests
        consulta = requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj))
        var = consulta.json()
        if var == {'status': 'ERROR', 'message': 'CNPJ inválido'}:
          print('cnpj inválido!')
          continue
        if var != {'status': 'ERROR', 'message': 'CNPJ inválido'}:
          print()
          for k,v in var.items():
            print(k,v)
          print("-"*60)
          print()
          print('Deseja cadastrar o cliente?')
          while True:
            print("Digite o número da opção desejada!")
            cliente = input('1.Sim ou 2.Não?: ').upper()
            if cliente == '1':
              NOME = var['nome']
              CNPJ = var['cnpj']
              RAZAO_SOCIAL = var['fantasia']
              Cliente = [NOME,CNPJ,RAZAO_SOCIAL]
              CNPJs.append(cnpj)
              CLIENTES.append(Cliente)
              print('Digite X - quando não quiser adiocionar mais Clientes!')
              print('Cliente registrado!')
              break
            if cliente == '2':
              break
            else:
              print('Ops...não entendi!')
              print('Tente novamente!')
      else:
        print('cnpj inválido!')
    else:
      print('CNPJ inválido!')
      print('Digite novamente!')
  print('Concluido')
  print("-"*60)
  print()

while True:
  print()
  print('Olá,Bem-Vindo!')
  print('Quais opções deseja navegar?\n   1.Exibir todos os clientes cadastrados\n   2.Adicionar um novo cliente\nDigite X - Se não quiser fazer mais nada!')
  print("-"*60)
  operacao = input('Digite o número da opção que deseja navegar: ').upper()
  if operacao == "X":
      break
  if operacao == "1":
    if len(CLIENTES) == 0:
      print("-"*60)
      print("Ainda não temos clientes cadastrados no nosso banco de dados!")
      print("-"*60)
    else:
      print('Todos os CNPJs cadastrados!')
      print("*"*60)
      count = 1
      for x in CLIENTES:
        print(f'CLIENTES-{count}: {x}')
        count+=1
        print("-*-*"*60)
  elif operacao == "2":
    print()
    print('Você escolheu cadastrar um novo cliente!')
    print()
    add_cliente(CLIENTES)

