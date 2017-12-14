
import numbers


class arvoreB(object):

    def __init__(self, ordem, coll=None):

        self.ocupMin = ordem // 2 - 1  # minimo de chaves no no
        self.ocupMax = ordem - 1  # maximo de chaves no no

        self.clear()
        if coll is not None:
            for x in coll:
                self.inserir(x)

    def __len__(self):
        return self.tamanho

    def clear(self):
        self.raiz = arvoreB.No(self.ocupMax, True)
        self.tamanho = 0

    def __contains__(self, x):
        No = self.raiz
        while True:
            indice = No.busca(x)
            if indice >= 0:
                return True
            elif No.is_folha():
                return False
            else:  # no interno
                No = No.children[~indice]

    def inserir(self, x):
        # primeiro eh tratada a divisao
        raiz = self.raiz
        if len(raiz.chaves) == self.ocupMax:
            direita, meio = raiz.dividir()
            left = raiz
            self.raiz = arvoreB.No(self.ocupMax, False)  # Increment tree height
            raiz = self.raiz
            raiz.chaves.append(meio)
            raiz.filhos.append(left)
            raiz.filhos.append(direita)

        # percorre a arvore
        No = raiz
        while True:
            # procura posicao no no atual
            indice = No.busca(x)
            if indice >= 0:
                return  # nao insere se chave ja existir
            indice = ~indice

            if No.is_folha():  # insere normalmente em folha
                No.chaves.insert(indice, x)
                self.tamanho += 1
                return
            else:  # trata nos internos
                filho = No.filhos[indice]
                if len(filho.chaves) == self.ocupMax:  # divide filho
                    direita, meio = filho.dividir()
                    No.filhos.insert(indice + 1, direita)
                    No.chaves.insert(indice, meio)
                    if x == meio:
                        return False  # nao insere se chave ja existir
                    elif x > meio:
                        filho = direita
                No = filho

    def remove(self, x):
        if not self._remove(x):
            raise KeyError(str(x))

    def discard(self, x):
        self._remove(x)

    def _remove(self, x):
        # percorre arvore
        raiz = self.raiz
        indice = raiz.busca(x)
        No = raiz
        while True:
            if No.is_folha():
                if indice >= 0:  # remove normalmente de folha
                    No.remove_chave(indice)
                    self.tamanho -= 1
                    return True
                else:
                    return False

            else:  # trata nos internos
                if indice >= 0:  # chave esta no no atual
                    esquerda, direita = No.filhos[indice: indice + 2]
                    if len(esquerda.chaves) > self.ocupMin:  # substituir chave
                        No.chaves[indice] = esquerda.remove_max()
                        self.tamanho -= 1
                        return True
                    elif len(direita.chaves) > self.ocupMin:
                        No.chaves[indice] = direita.remove_min()
                        self.tamanho -= 1
                        return True
                    elif len(esquerda.chaves) == self.ocupMin and len(direita.chaves) == self.ocupMin:
                        # faz uniao do no da esquerda e direita
                        if not esquerda.is_folha():
                            esquerda.filhos.extend(direita.children)
                        esquerda.chaves.append(No.remove_chave_e_filho(indice, indice + 1))
                        esquerda.chaves.extend(direita.chaves)
                        if No is raiz and len(raiz.chaves) == 0:
                            self.raiz = raiz.filhos[0]  # diminui altura
                            raiz = self.raiz
                        No = esquerda
                        indice = self.ocupMin
                    else:
                        raise AssertionError("Condicao inesperada")
                else:  # procura chave em filhos
                    filho = No.verifica_remocao(~indice)
                    if No is raiz and len(raiz.chaves) == 0:
                        self.raiz = raiz.filhos[0]  # diminui altura
                        raiz = self.raiz
                    No = filho
                    indice = No.busca(x)

    # metodo para iterar pelas chaves de forma ordenada
    def __iter__(self):
        if self.tamanho == 0:
            return

        pilhaNo = []
        indicePilha = []
        No = self.raiz
        while True:
            pilhaNo.append(No)
            indicePilha.append(0)
            if No.is_folha():
                break
            No = No.filhos[0]

        while len(pilhaNo) > 0:
            No = pilhaNo.pop()
            indice = indicePilha.pop()
            if No.is_folha():
                for x in No.chaves:
                    yield x
            else:
                yield No.chaves[indice]
                indice += 1
                if indice < len(No.chaves):
                    pilhaNo.append(No)
                    indicePilha.append(indice)
                No = No.filhos[indice]
                while True:
                    pilhaNo.append(No)
                    indicePilha.append(0)
                    if No.is_folha():
                        break
                    No = No.filhos[0]

    def __str__(self):
        return self.raiz.__str__()

    class No(object): # estrutura de um no

        def __init__(self, ocupMax, folha):
            self.ocupMax = ocupMax
            self.chaves = []
            self.filhos = None if folha else []

        def is_folha(self):
            return self.filhos is None

        def busca(self, x):
            chaves = self.chaves
            i = 0
            while i < len(chaves):
                if x == chaves[i]:
                    return i  # chave encontrada
                elif x > chaves[i]:
                    i += 1
                else:
                    break
            return ~i  # chave nao esta no no

        # remove menor chave encontra na subarvore desse no
        def remove_min(self):
            ocupMin = len(self.chaves) // 2
            No = self
            while not No.is_folha():
                No = No.verifica_remocao(0)
            return No.remove_chave(0)

        # remove maior chave encontrada em subarvore desse no
        def remove_max(self):
            ocupMin = len(self.chaves) // 2
            No = self
            while not No.is_folha():
                No = No.verifica_remocao(len(No.filhos) - 1)
            return No.remove_chave(len(No.chaves) - 1)

        # remove chave no indice passado
        def remove_chave(self, indice):
            if indice < 0 or indice >= len(self.chaves):
                raise indiceError()
            return self.chaves.pop(indice)

        # realiza remocao de chave em no, removendo tambem filho
        def remove_chave_e_filho(self, chave_i, filho_i):
            if chave_i < 0 or chave_i >= len(self.chaves):
                raise indiceError()
            if self.is_folha():
                if filho_i is not None:
                    raise ValueError()
            else:
                if filho_i < 0 or filho_i >= len(self.filhos):
                    raise indiceError()
                del self.filhos[filho_i]
            return self.remove_chave(chave_i)

        # rotina para insercao em no cheio
        def dividir(self):
            if len(self.chaves) != self.ocupMax:
                raise RuntimeError("No nao esta cheio")
            ocupMin = self.ocupMax // 2
            no_direita = arvoreB.No(self.ocupMax, self.is_folha())
            meio = self.chaves[ocupMin]
            no_direita.chaves.extend(self.chaves[ocupMin + 1:])
            del self.chaves[ocupMin:]
            if not self.is_folha():
                no_direita.filhos.extend(self.filhos[ocupMin + 1:])
                del self.filhos[ocupMin + 1:]
            return no_direita, meio

        # verifica se remocao requer tratamentos adicionais
        def verifica_remocao(self, indice):
            ocupMin = self.ocupMax // 2
            filho = self.filhos[indice]
            if len(filho.keys) > ocupMin:  # no e preciso tratar esse caso
                return filho

            # pega nos irmaos
            esquerda = self.filhos[indice - 1] if indice >= 1 else None
            direita = self.filhos[indice + 1] if indice < len(self.chaves) else None
            interno = not filho.is_folha()

            if esquerda is not None and len(esquerda.chaves) > ocupMin:  # pega chave mais a direita da irmao da esquerda
                if interno:
                    filho.filhos.insert(0, esquerda.filhos.pop(-1))
                filho.chaves.insert(0, self.chaves[indice - 1])
                self.chaves[indice - 1] = esquerda.remove_chave(len(esquerda.chaves) - 1)
                return filho
            elif direita is not None and len(direita.chaves) > ocupMin:  # pega chave mais a esquerda de irmao a direita
                if interno:
                    filho.filhos.append(direita.filhos.pop(0))
                filho.chaves.append(self.chaves[indice])
                self.chaves[indice] = direita.remove_chave(0)
                return filho
            elif esquerda is not None:  # faz uniao de filho com irmao da esquerda
                if interno:
                    esquerda.fihos.extend(filho.children)
                esquerda.chaves.append(self.remove_chave_e_filho(indice - 1, indice))
                esquerda.chaves.extend(filho.keys)
                return esquerda
            elif direita is not None:  # faz uniao de filho com irmao da direita
                if interno:
                    filho.filhos.extend(direita.filhos)
                filho.chaves.append(self.remove_chave_e_filho(indice, indice + 1))
                filho.chaves.extend(direita.chaves)
                return filho
            else:
                raise AssertionError("Condicao inesperada")

        def __str__(self, nivel = 0):
                if self.is_folha():
                    return "\tNo folha com {0} chaves no nivel {1}\n\tChaves: {2}\n".format(len(self.chaves), nivel, self.chaves)
                else:
                    return "No interno com com {0} chaves e {1} filhos no nivel {2}\n\tChaves: {3}\n\n".format(len(self.chaves), len(self.filhos), nivel, self.chaves)+'\n'.join([filho.__str__(nivel + 1) for filho in self.filhos])
