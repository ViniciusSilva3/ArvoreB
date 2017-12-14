# Metodo que vai realizar a leitura do arquivo e o gravamento dos vetores de chaves e PRR

class base:
    def __init__(self, arquivo):
        self.arq = arquivo
        self.chave = [] # Aqui cria uma lista vazia para cada 'base' que for instanciada
        self.PRR = []

    def getChave(self):
        i = 0
        arv = open(self.arq, "r").read()
        arv = arv.replace('\r', '\n')
        arv1 = arv.split('\n')
        while(1):
        #Esse tratamento de excecoes vai verificar quando o elemento arv1[i] nao existe mais
            try:
                foo = arv1[i]
            except (IndexError):
                foo = None
                break
            self.chave.append(arv1[i].split(',')[0])
            i = i+1
        return self.chave, i

    def getPRR(self):
        some = 0
        i = 0
        arv = open(self.arq, "r").read()
        arv = arv.replace('\r', '\n')
        arv1 = arv.split('\n')
        while(1):
        #Esse tratamento de excecoes vai verificar quando o elemento arv1[i] nao existe mais
            try:
                foo = arv1[i]
            except (IndexError):
                foo = None
                break

            self.PRR.append(some)
            some = some + len(arv1[i]) + 1
            i = i+1
        return self.PRR

# aqui estao alguns testes para testar a classe 'base'

"""a = base("data.txt")
chaves = []
chaves = a.getChave()
print(chaves[0])
prr = []
prr = a.getPRR()
#print(prr)
"""
