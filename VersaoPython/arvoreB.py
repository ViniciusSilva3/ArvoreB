
import numbers


class arvoreB(object):

    # grau representa o numero minimo de filhos do no
    def __init__(self, grau, coll=None):

        self.ocupMin = grau - 1  # minimo de chaves no no
        self.ocupMax = grau * 2 - 1  # maximo de chaves no no

        self.clear()
        if coll is not None:
            for obj in coll:
                self.inserir(obj)

    def __len__(self):
        return self.size

    def clear(self):
        self.raiz = arvoreB.No(self.ocupMax, True)
        self.size = 0

    def __contains__(self, obj):
        No = self.raiz
        while True:
            index = No.busca(obj)
            if index >= 0:
                return True
            elif No.is_folha():
                return False
            else:  # no interno
                No = No.children[~index]

    def inserir(self, obj):
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
            assert len(No.chaves) < self.ocupMax
            assert No is raiz or len(No.chaves) >= self.ocupMin
            index = No.busca(obj)
            if index >= 0:
                return  # nao insere se chave ja existir
            index = ~index
            assert index >= 0

            if No.is_folha():  # insere normalmente em folha
                No.chaves.insert(index, obj)
                self.size += 1
                return
            else:  # trata nos internos
                filho = No.filhos[index]
                if len(filho.chaves) == self.ocupMax:  # divide filho
                    direita, meio = filho.dividir()
                    No.filhos.insert(index + 1, direita)
                    No.chaves.insert(index, meio)
                    if obj == meio:
                        return False  # nao insere se chave ja existir
                    elif obj > meio:
                        filho = direita
                No = filho

    def remove(self, obj):
        if not self._remove(obj):
            raise KeyError(str(obj))

    def discard(self, obj):
        self._remove(obj)

    def _remove(self, obj):
        # percorre arvore
        raiz = self.raiz
        index = raiz.busca(obj)
        No = raiz
        while True:
            assert len(No.chaves) <= self.ocupMax
            assert No is raiz or len(No.chaves) > self.ocupMin
            if No.is_folha():
                if index >= 0:  # remove normalmente de folha
                    No.remove_chave(index)
                    self.size -= 1
                    return True
                else:
                    return False

            else:  # trata nos internos
                if index >= 0:  # chave esta no no atual
                    esquerda, direita = No.filhos[index: index + 2]
                    if len(esquerda.chaves) > self.ocupMin:  # substituir chave
                        No.chaves[index] = esquerda.remove_max()
                        self.size -= 1
                        return True
                    elif len(direita.chaves) > self.ocupMin:
                        No.chaves[index] = direita.remove_min()
                        self.size -= 1
                        return True
                    elif len(esquerda.chaves) == self.ocupMin and len(direita.chaves) == self.ocupMin:
                        # faz uniao do no da esquerda e direita
                        if not esquerda.is_folha():
                            esquerda.filhos.extend(direita.children)
                        esquerda.chaves.append(No.remove_chave_e_filho(index, index + 1))
                        esquerda.chaves.extend(direita.chaves)
                        if No is raiz and len(raiz.chaves) == 0:
                            self.raiz = raiz.filhos[0]  # diminui altura
                            raiz = self.raiz
                        No = esquerda
                        index = self.ocupMin
                    else:
                        raise AssertionError("Condicao inesperada")
                else:  # Key might be found in some child
                    filho = No.verifica_remocao(~index)
                    if No is raiz and len(raiz.chaves) == 0:
                        self.raiz = raiz.filhos[0]  # diminui altura
                        raiz = self.raiz
                    No = filho
                    index = No.busca(obj)

    # metodo para iterar pelas chaves de forma ordenada
    def __iter__(self):
        if self.size == 0:
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

        # Generate elements
        while len(pilhaNo) > 0:
            No = pilhaNo.pop()
            index = indicePilha.pop()
            if No.is_folha():
                assert index == 0
                for obj in No.chaves:
                    yield obj
            else:
                yield No.chaves[index]
                index += 1
                if index < len(No.chaves):
                    pilhaNo.append(No)
                    indicePilha.append(index)
                No = No.filhos[index]
                while True:
                    pilhaNo.append(No)
                    indicePilha.append(0)
                    if No.is_folha():
                        break
                    No = No.filhos[0]

    class No(object): # estrutura de um no

        def __init__(self, ocupMax, folha):
            assert ocupMax >= 3 and ocupMax % 2 == 1
            self.ocupMax = ocupMax
            self.chaves = []
            self.filhos = None if folha else []

        def is_folha(self):
            return self.filhos is None

        def busca(self, obj):
            chaves = self.chaves
            i = 0
            while i < len(chaves):
                if obj == chaves[i]:
                    return i  # chave encontrada
                elif obj > chaves[i]:
                    i += 1
                else:
                    break
            return ~i  # chave nao esta no no

        # remove menor chave encontra na subarvore desse no
        def remove_min(self):
            ocupMin = len(self.chaves) // 2
            No = self
            while not No.is_folha():
                assert len(No.chaves) > ocupMin
                No = No.verifica_remocao(0)
            assert len(No.chaves) > ocupMin
            return No.remove_chave(0)

        # remove maior chave encontrada em subarvore desse no
        def remove_max(self):
            ocupMin = len(self.chaves) // 2
            No = self
            while not No.is_folha():
                assert len(No.chaves) > ocupMin
                No = No.verifica_remocao(len(No.filhos) - 1)
            assert len(No.chaves) > ocupMin
            return No.remove_chave(len(No.chaves) - 1)

        # remove chave no indice passado
        def remove_chave(self, index):
            if index < 0 or index >= len(self.chaves):
                raise IndexError()
            return self.chaves.pop(index)

        # realiza remocao de chave em no, removendo tambem filho
        def remove_chave_e_filho(self, chave_i, filho_i):
            if chave_i < 0 or chave_i >= len(self.chaves):
                raise IndexError()
            if self.is_folha():
                if filho_i is not None:
                    raise ValueError()
            else:
                if filho_i < 0 or filho_i >= len(self.filhos):
                    raise IndexError()
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
        def verifica_remocao(self, index):
            assert not self.is_folha()
            ocupMin = self.ocupMax // 2
            filho = self.filhos[index]
            if len(filho.keys) > ocupMin:  # no e preciso tratar esse caso
                return filho
            assert len(filho.keys) == ocupMin

            # pega nos irmaos
            esquerda = self.filhos[index - 1] if index >= 1 else None
            direita = self.filhos[index + 1] if index < len(self.chaves) else None
            interno = not filho.is_folha()
            assert esquerda is not None or direita is not None
            assert esquerda is None or esquerda.is_folha() != interno # verifica se os irmaos sao ambos folhas
            assert direita is None or direita.is_folha() != interno   # ou nos internos

            if esquerda is not None and len(esquerda.chaves) > ocupMin:  # pega chave mais a direita da irmao da esquerda
                if interno:
                    filho.filhos.insert(0, esquerda.filhos.pop(-1))
                filho.chaves.insert(0, self.chaves[index - 1])
                self.chaves[index - 1] = esquerda.remove_chave(len(esquerda.chaves) - 1)
                return filho
            elif direita is not None and len(direita.chaves) > ocupMin:  # pega chave mais a esquerda de irmao a direita
                if interno:
                    filho.filhos.append(direita.filhos.pop(0))
                filho.chaves.append(self.chaves[index])
                self.chaves[index] = direita.remove_chave(0)
                return filho
            elif esquerda is not None:  # faz uniao de filho com irmao da esquerda
                assert len(esquerda.chaves) == ocupMin
                if interno:
                    esquerda.fihos.extend(filho.children)
                esquerda.chaves.append(self.remove_chave_e_filho(index - 1, index))
                esquerda.chaves.extend(filho.keys)
                return esquerda
            elif direita is not None:  # faz uniao de filho com irmao da direita
                assert len(direita.chaves) == ocupMin
                if interno:
                    filho.filhos.extend(direita.filhos)
                filho.chaves.append(self.remove_chave_e_filho(index, index + 1))
                filho.chaves.extend(direita.chaves)
                return filho
            else:
                raise AssertionError("Condicao inesperada")
