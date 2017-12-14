import arvoreB
import pecaquebrada

tree = arvoreB.arvoreB(25)

a = pecaquebrada.base("data.txt")
chaves, tamanho = a.getChave()
prr = a.getPRR()

for i,j in zip(chaves, prr):
	tree.inserir([i, j])

#CRIACAO DO ARQUIVO APOS O USO DA ARVORE

arquivo = open("BTREE.txt", "w")
b = 0
while(b<tamanho):
	arquivo.write("Chave : %s, PRR: %d\n"%(chaves[b], prr[b]))
	b +=1
arquivo.close()
#print tree
