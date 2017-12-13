import arvoreB
import pecaquebrada

"""a = pecaquebrada.base("data.txt")
chaves = []
chaves, tamanho = a.getChave() 
prr = []
prr = a.getPRR()"""

arvore = arvoreB.ArvoreB(15)
chaves = [300, 20, 150, 12, 25, 80, 142, 176, 297, 430, 480, 520, 380, 395, 412, 451, 493, 506, 521, 600]
prr = [300, 20, 150, 12, 25, 80, 142, 176, 297, 430, 480, 520, 380, 395, 412, 451, 493, 506, 521, 600]
i = 0
while(i < 21):
    arvore.inserir(chaves[i], prr[i])
    i += 1

print arvore

#no, p = arvore.buscar('404309')

#print no.prr[p]

