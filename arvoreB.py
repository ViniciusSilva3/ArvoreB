class No(object):

    def __init__(self, folha=False):
        self.folha = folha  # booleano, indica se o no eh folha
        self.chaves = []  # lista de chaves
        self.prr = [] # lista de prr's
        self.c = []  # lista de descendentes

    def __str__(self):  # definicao de print informal do no

        if self.folha:
            return "Folha com {0} chaves\n\tChaves:{1}\n\tFilhos:{2}\n".format(len(self.chaves), self.chaves, self.c)

        else:
            return "No interno com {0} chaves, {1} filhos\n\tChaves:{2}\n\n".format(len(self.chaves), len(self.c),
                                                                                    self.chaves, self.c)


class ArvoreB(object):
    def __init__(self, t):
        self.raiz = No(folha=True)  # inicia no raiz como folha
        self.t = t  # ordem da arvore

    def buscar(self, k, x=None):

        if isinstance(x, No):  # realiza busca no no indicado
            i = 0
            while i < len(x.chaves) and k > x.chaves[i]:  # procura chave no no x
                i += 1
            if i < len(x.chaves) and k == x.chaves[i]:  # encontrou a chave
                return x, i
            elif x.folha:  # se ofr folha e chave nao encontrada, chave nao existe
                return None
            else:  # se for no interno, busca nos descendentes
                return self.buscar(k, x.c[i])
        else:  # se nao for fornecido um no de busca, comecar pela raiz
            return self.buscar(k, self.raiz)

    def inserir(self, k, p):
        r = self.raiz
        if len(r.chaves) == self.t - 1:  # se no estiver cheio, dividir
            s = No()
            self.raiz = s
            s.c.insert(0, r)  # antiga raiz se torna primeiro filho de s
            self.dividirInserir(s, 0)
            self.inseirNormal(s, k, p)
        else:
            self.inseirNormal(r, k, p)

    def inseirNormal(self, x, k, p):
        i = len(x.chaves) - 1
        if x.folha:
            # inserir chave se no for folha
            x.chaves.append(0)
            x.prr.append(0)
            while i >= 0 and k < x.chaves[i]:
                x.chaves[i + 1] = x.chaves[i]
                x.prr[i + 1] = x.prr[i]
                i -= 1
            x.chaves[i + 1] = k
            x.prr[i + 1] = p

        else:
            # tentar inserir em descendentes
            while i >= 0 and k < x.chaves[i]:
                i -= 1
            i += 1

            if len(x.c[i].chaves) == self.t - 1:
                self.dividirInserir(x, i)

                if k > x.chaves[i]:
                    i += 1
            self.inseirNormal(x.c[i], k, p)

    def dividirInserir(self, x, i):
        t = self.t
        y = x.c[i]
        z = No(folha=y.folha)

        # passa filhos de x para direita e insere z em i + 1
        x.c.insert(i + 1, z)
        x.chaves.insert(i, y.chaves[t/2 - 1])
        x.prr.insert(i, y.prr[t/2 -1])

        z.chaves = y.chaves[t/2:(t - 1)]
        z.prr = y.prr[t/2:(t - 1)]
        y.chaves = y.chaves[0:(t/2 - 1)]
        y.prr = y.prr[0:(t/2 - 1)]

        if not y.folha:
            z.c = y.c[t/2:t]
            y.c = y.c[0:(t/2 - 1)]

    def __str__(self):
        r = self.raiz
        return r.__str__() + '\n'.join([child.__str__() for child in r.c])
