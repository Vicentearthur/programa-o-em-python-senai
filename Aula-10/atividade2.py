# NOTAS DO ALUNOS 


senha_u = "arthur1345"
usuario = "arthur silva"

for c in range(3):

    login = input("digite su nome para ter acesso a sua conta ")
    senha = input("senha: ")

    if senha == senha_u and login == usuario:
        print("acesso permtido")

        nota1 = 7
        nota2 = 7
        nota3 = 10

        resultado =  (nota1, nota2, nota3)
        media = resultado/3

        if media <= 4:
         print ("sua nota foi", resultado, "voce esta reprovado")

        else: 
         

         print("sua nota foi,",resultado,"voce foi aprovado!")





    else:
        print("senha incoreta")   
else:
    print("senha bloqueada") 


input("digite enter para sair")


