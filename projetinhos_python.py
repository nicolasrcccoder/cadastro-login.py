import time
todas_senhas = []

def cadastrar_login():
  print('---REGISTRANDO USUÁRIO---')
  nome_escolhido = str(input('seu nome :'))
  senha_escolhida = str(input('sua senha :'))
  senhas = {'nome': nome_escolhido ,
            'senha':senha_escolhida
            }
  todas_senhas.append(senhas)
  print('usuario cadastrado com sucesso!!!')
  print('voltando ao menu...')

def fazendo_login():
  while True:
    print('---ENTRE NO SEU PERFIL---')
    nome_validando = str(input('digite seu nome (s para sair):'))
    senha_validando = str(input('digite sua senha (s para sair) :'))
    if nome_validando.lower() == 's' or senha_validando.lower() == 's':
      print('voltando ao menu...')
      break
    for senhas in todas_senhas:
       if nome_validando != senhas['nome'] or  senha_validando !=  senhas['senha']:
        print('nome ou senha estão invalidos , tente novamente por favor. ')
        continue
       else:
         print('carregando...')
         time.sleep(2)
         print(f' seu nome : {senhas["nome"]} | sua senha : {senhas["senha"]}')
         print('acesso concedido.')
         print('-pagina aberta.')
         time.sleep(2)
         break

def trocar_login():
 while True:
  print('---ESQUECEU SUA SENHA? QUER TROCA-LA?---')
  nome_verificando = str(input('digite seu nome atual (s para sair): '))
  senha_verificando = str(input('digite sua senha atual (s para sair) :'))
  if nome_verificando.lower() == 's' or senha_verificando.lower() == 's':
     print('voltando ao menu...')
     break
  for senhas in todas_senhas:
     if nome_verificando == senhas['nome'] and senha_verificando == senhas['senha']:
       novo_nome = str(input('digite seu novo nome :'))
       nova_senha = str(input('digite sua nova senha :'))
       senhas['nome'] = novo_nome
       senhas['senha'] = nova_senha
       print(' novo nome e senha cadastradas com sucesso!')
       break
  else:
    print('nome ou senha incorretos! tente novamente.')
 

def menu():
  print('==== CENTRAL DE CONTAS ====')
  print(' 1 - cadastrar nome e senha ')
  print(' 2 - fazer login com nome e senha ')
  print(' 3 - trocar nome e senha ')
  print(' 4 - SAIR')


def main():
 while True:
  try:
   menu()
   opcao = int(input('qual a opcao :'))
   if opcao == 1 :
     cadastrar_login()
   elif opcao == 2 :
     fazendo_login()
   elif opcao == 3 :
     trocar_login()
   elif opcao == 4 :
     sim_ou_nao = input('tem certeza que deseja sair? (s ou n)')
     if sim_ou_nao == 's':
       print('encerrando o programa... até mais.')
       break
     elif sim_ou_nao == 'n':
       print('voltando.')
   else:
     print('opção invalida!')
  except ValueError:
    print('apenas números!')

main()


