
def register () :
    name = str(input("Digite o seu nome completo : "))
    age = int(input("\nDigite a sua idade : "))
    number = int(input("\nDigite o seu número de telefone : "))
    return name,age,number

def createLogin () :
    while True :
        email = str(input("\nDigite seu email : "))
        email0 = str(input("\nConfirme seu email : "))
        password = str(input("\nCrie uma senha : "))
        password0 = str(input("Confirme sua senha : "))
        if password != password0  or email != email0 :
                print("\nEmail ou senha diferente!")
                                   
        else:
            print ("\nCadastro realizado com sucesso!")
            return email,password
            break
                        
def enter () :
     while True :
          confirmEmail = (input("Login :"))
          confirmPassword =  (input("\nSenha : "))
          if confirmEmail == email  and  password == confirmPassword:
               print("Sucesso")
               return confirmEmail,confirmPassword
               break
          elif confirmPassword == '#' or confirmEmail == '#' :
               break
          else : 
               print("Tente novamente")
               print("OU digite  #  para SAIR ")

def main () :
     register()
     email,password = createLogin()
     enter()
main()