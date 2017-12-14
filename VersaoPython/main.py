import arvoreB
import pecaquebrada

tree = arvoreB.arvoreB(50)

a = pecaquebrada.base("data.txt")
chaves = a.getChave()
prr = a.getPRR()

for i, j in zip(chaves, prr):
    tree.inserir([i, j])

print tree
