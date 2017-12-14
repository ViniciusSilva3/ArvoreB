import arvoreB
import arquivo
tree = arvoreB.arvoreB(50)

a = arquivo.base("data.txt")
chaves = a.getChave()
prr = a.getPRR()

for i, j in zip(chaves, prr):
    tree.inserir(i, j)

print tree 
while 1:
	print 30 * "-" , "MENU" , 30 * "-"
	print "[1]: Inserir elemento"
	print "[2]: Remover elemento"
	print "[3]: Buscar elemento"
	print "[4]: Atualizar registro"
	print "[5]: Sair do programa"
	print 67 * "-"
  	i = 1
  	while i == 1:
	  	try:
	  		escolha = input("Entre com a opcao desejada: ")
	  		i = 0
	  	except:
	  		print("Opcao inexistente!")

  	if escolha == 1:
  		break
	elif escolha == 2:
		break
	elif escolha == 3:
		break
	elif escolha == 4:
		break
	elif escolha == 5:
		break
	else:
		print("Opcao inexistente!")

p = tree.buscar('999971')
print(p)


