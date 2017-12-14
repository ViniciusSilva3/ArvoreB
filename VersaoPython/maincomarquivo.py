import arvoreB
import pecaquebrada

tree = arvoreB.arvoreB(25)

a = pecaquebrada.base("data.txt")
chaves, tamanho = a.getChave()
prr = a.getPRR()

for i,j in zip(chaves, prr):
	tree.inserir([i, j])
Origem = tree.raiz
#CRIACAO DO ARQUIVO APOS O USO DA ARVORE

arquivo = open("BTREE.txt", "w")
b = 0
#Escreve primeiro as chaves da raiz:
tam = len(Origem.chaves)
while(b<tam):
	arquivo.write("Chave:%s,PRR:%s;"%(Origem.chaves[b][0], Origem.chaves[b][1]))
	b +=1
arquivo.write("\n")
#Escreve o filho mais a esquerda da raiz
b = len(Origem.filhos)
aux = 0
Filho = Origem.filhos
while(aux<b):
	p = 0
	tam1 = len(Filho[aux].chaves)
	while(p<tam1):
		arquivo.write("Chave:%s,PRR:%s;"%(Filho[aux].chaves[p][0], Filho[aux].chaves[p][1]))
		p += 1
	teste = len(Filho[aux].filhos)
	d = 0
	if(teste != 0):
		Neto = Filho[aux].filhos
		while(d<teste):
			tam2 = len(Neto[d].chaves)
			aux2 = 0
			while(aux2<tam2):
				arquivo.write("Chave:%s,PRR:%s"%(Neto[d].chaves[aux2][0], Neto[d].chaves[aux2][1]))
				aux2 +=1
			arquivo.write("\n")
			teste1 = len(Neto[d].filhos)
	        	e = 0
	        	if(teste1 != 0):
		        	BisNeto = Neto[d].filhos
		        	while(e<teste1):
			        	tam3 = len(BisNeto[e].chaves)
			        	aux3 = 0
			       		while(aux3<tam3):
				        	arquivo.write("Chave:%s,PRR:%s"%(BisNeto[e].chaves[aux3][0], BisNeto[e].chaves[aux3][1]))
					        aux3 +=1
					e += 1
			    		arquivo.write("\n")
			d += 1
	aux += 1
arquivo.close()
#print tree
