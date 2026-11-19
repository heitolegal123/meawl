#w write
#r read 
#r+ read and write 
#a append

#b binary


'''arquivo = open ("arquivo,txt","")

arquivo.close()'''

nome = "joao vitor"

#with open("arquivo.txt","w") as arquivo:
   # arquivo.write(f"ola,boa noite meu nome e: {nome}")
    

#with open("arquivo.txt","r", encoding="utf-8") as arquivo:
    #arquivo.write(f"ola,boa noite meu nome e: {nome}")

def abcde(parametro):
    with open("nomes.txt","w", encoding="utf-8")as arquivo :
        arquivo.write(parametro)


























