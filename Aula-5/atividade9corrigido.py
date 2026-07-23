
Nome = input('digite seu nome por favor ')

email = input("digite seu email para contato... ")

idade = input('informe sua idade' )

cidade = input('em que cidade mora ? ')

graduacao = input('me fale seu nivel de graduaçao ')

estado_civil =input('informe seu estado civil ')

print("confirme seus dados para finalizar seu cadastro ")

print("voce é...",Nome)
print('seu email',email)
print(idade,"anos")
print("voce é de", cidade)
print(graduacao)
print("por fim voce esta", estado_civil)

dados= (input("os dados estao corretos ? "))

dados == "S" and print("ok, seu cadastro esta concluido...")
dados == "N" and print("falhamos ao colhetar seus dasos, digite novamente mais tarde")



resposta= (input("uma ultima coisa, poderia avaliar o nosso sitema ?"))


resposta == "S" and print(" obrigado vamos para avalicão")
resposta == "N" and print("tudo bem tenha um bom dia...")

 
nota_sitema= int(input("de 0 a 10 quanto gostou do nosso sitema?"))

nota_sitema >=5 and print("agradeço sua avaliação")
nota_sitema <5 and print('desculpe vamos melhorar')
nota_sitema == 10 and print("Fico muito feliz em saber que gostou do nosso sitema XD")

print("encerando sitema....")

