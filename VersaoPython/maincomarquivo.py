import arvoreB
import pecaquebrada

tree = arvoreB.arvoreB(25)

a = pecaquebrada.base("data.txt")
chaves, tamanho = a.getChave()
prr = a.getPRR()

for i,j in zip(chaves, prr):
	tree.inserir(i, j)
Origem = tree.raiz
#CRIACAO DO ARQUIVO APOS O USO DA ARVORE

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
b = len(Origem.filhos)
aux = 0
Filho = Origem.filhos
while(aux<b):
	p = 0
	tam1 = len(Filho[aux].chaves)
	arquivo.write("1,")
	while(p<tam1):
		arquivo.write("%s,%d;"%(Filho[aux].chaves[p], Filho[aux].prr[p]))
		p += 1
	teste = len(Filho[aux].filhos)
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
			teste1 = len(Neto[d].filhos)
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
