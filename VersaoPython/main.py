import arvoreB
import arquivo
tree = arvoreB.arvoreB(50)

a = arquivo.base("data.txt")
chaves, tamanho = a.getChave()
prr = a.getPRR()

for i, j in zip(chaves, prr):
    tree.inserir(i, j)

print(chaves[0],prr[0])
print(chaves[tamanho-1],prr[tamanho-1])
#print tree 
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
  		chave = raw_input("Digite a chave do registro a ser inserido: ")
  		V= 0
  		verifique = 0
  		while(V<tamanho):
  			if (chaves[V] == chave):
  				print("A chave ja existe")
  				verifique = 1
  			V+=1
  		if (verifique == 0):
	  		A = open("data.txt","r+")
	  		A.seek(prr[tamanho-1])
	  		line = A.readline()
	  		A.write("%s,\n"%chave)
	  		A.close()
	  		chaves.append(chave)
	  		R = prr[tamanho-1]
	  		tamanho += 1
	  		soma = R + len(line)
	  		prr.append(soma)
	  		tree.inserir(chave,soma)

	elif escolha == 2:
		chave = raw_input("Digite a chave do registro a ser removido: ")
		
		try:
			V = 0
			L = tree.buscar(str(chave))
			while(V<tamanho):
				if(prr[V] == L):
					break
				V+=1
			chaves.pop(V)
			prr.pop(V)
			tamanho = tamanho - 1

			A = open("data.txt").read()
			A = A.replace('\r', '\n')
			A1 = A.split("\n")
			new = open("data.txt","w")
			i = 0
			while(i < tamanho + 2):
				if(chave not in A1[i]):
					new.write(A1[i])
					new.write("\n")
					

				i+=1
			new.close()
			tree.remove(chave)

		except:	
			print("Chave nao encontrada")
	elif escolha == 3:
		chave = raw_input("Digite a chave do registro a ser procurado: ")
		p = tree.buscar(str(chave))
		try:
			A = open("data.txt", "r")
			A.seek(p,0)
			Registro = A.readline(142) 
			B = Registro.replace('\r', '\n')
			C,D= B.split("\n")
			print(C)
			A.close()
		except:
			print("Chave nao encontrada")
	elif escolha == 4:
		break
	elif escolha == 5:
		print("Encerrando programa")
		break
	else:
		print("Opcao inexistente!")


#CRIACAO DO ARQUIVO APOS O USO DA ARVORE
Origem = tree.raiz
arquivo = open("BTREE.txt", "w")
b = 0
#Escreve primeiro as chaves da raiz:
tam = len(Origem.chaves)
arquivo.write("0,")
while(b<tam):
	arquivo.write("%s,%d;"%(Origem.chaves[b], Origem.prr[b]))
	b +=1
arquivo.write("\n")
#Escreve o filho mais a esquerda da raiz
#trata a excecao caso nao exista filhos na raiz
tipo0 = Origem.filhos
if (tipo0!=None):
    b = len(Origem.filhos)
else:
    b=0
#tratou a excecao
aux = 0
Filho = Origem.filhos
while(aux<b):
	p = 0
	tam1 = len(Filho[aux].chaves)
	arquivo.write("1,")
	while(p<tam1):
		arquivo.write("%s,%d;"%(Filho[aux].chaves[p], Filho[aux].prr[p]))
		p += 1
    #tratando excecao caso nao existam filhos
    	tipo1 = Filho[aux].filhos
    	if(tipo1 != None):
        	teste = len(Filho[aux].filhos)
    	else:
        	teste = 0
    #fim da excecao
	d = 0
	if(teste != 0):
		Neto = Filho[aux].filhos
		while(d<teste):
			tam2 = len(Neto[d].chaves)
			aux2 = 0
			arquivo.write("2,")
			while(aux2<tam2):
				arquivo.write("%s,%d;"%(Neto[d].chaves[aux2], Neto[d].prr[aux2]))
				aux2 +=1
			arquivo.write("\n")
            		tipo2 = Neto[d].filhos
            		if(tipo2 != None):
				teste1 = len(Neto[d].filhos)
        	    	else:
                		teste1 = 0
	        	e = 0
	        	if(teste1 != 0):
		       		BisNeto = Neto[d].filhos
		       	while(e<teste1):
		        	tam3 = len(BisNeto[e].chaves)
		        	aux3 = 0
				arquivo.write("3,")
		       		while(aux3<tam3):
			        	arquivo.write("%s,%d;"%(BisNeto[e].chaves[aux3], BisNeto[e].prr[aux3]))
				        aux3 +=1
				e += 1
		    		arquivo.write("\n")
			d += 1
	aux += 1
arquivo.close()
#print tree


