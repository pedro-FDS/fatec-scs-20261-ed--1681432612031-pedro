'''*---------------------------------------------------------*
* Fatec São Caetano do Sul                                   *
* Atividade B2-3                                             *
* Autor: 1681432612031 - Pedro Henrique Ferreira da Silva    *
* Objetivo: Árvore binária                                   *
* data: 19/05/2026                                           *
*------------------------------------------------------------*
'''

def inserir(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

def _inserir_recursivo(self, no, valor):
        if valor < no.valor:
            if no.esq == None:
                no.esq = No(valor)
            else:
                self._inserir_recursivo(no.esq, valor)
        else:
            if no.dir == None:
                no.dir = No(valor)
            else:
                self._inserir_recursivo(no.dir, valor)

def imprimir_nos_internos(self):
        lista_internos = []
        self._pegar_internos(self.raiz, lista_internos)
        print("Nos Internos:", lista_internos)

def _pegar_internos(self, no, lista):
        if no == None:
            return
        if no.esq != None or no.dir != None:
            lista.append(no.valor)
        self._pegar_internos(no.esq, lista)
        self._pegar_internos(no.dir, lista)

def imprimir_folhas(self):
        lista_folhas = []
        self._pegar_folhas(self.raiz, lista_folhas)
        print("Nos Folhas (externos):", lista_folhas)

def _pegar_folhas(self, no, lista):
        if no == None:
            return
        if no.esq == None and no.dir == None:
            lista.append(no.valor)
        self._pegar_folhas(no.esq, lista)
        self._pegar_folhas(no.dir, lista)

def imprimir_niveis(self):
        if self.raiz == None:
            print("arvore vazia")
            return

        fila = []
        fila.append((self.raiz, 0))

        nivel_atual = 0
        nos_do_nivel = []

        while len(fila) > 0:
            no, nivel = fila.pop(0)

            if nivel != nivel_atual:
                print("Nivel", nivel_atual, ":", nos_do_nivel)
                nivel_atual = nivel
                nos_do_nivel = []

            nos_do_nivel.append(no.valor)

            if no.esq != None:
                fila.append((no.esq, nivel + 1))
            if no.dir != None:
                fila.append((no.dir, nivel + 1))

        print("Nivel", nivel_atual, ":", nos_do_nivel)

def calcular_altura(self, no):
        if no == None:
            return -1
        altura_esq = self.calcular_altura(no.esq)
        altura_dir = self.calcular_altura(no.dir)
        if altura_esq > altura_dir:
            return 1 + altura_esq
        else:
            return 1 + altura_dir

def calcular_profundidade(self, valor):
        return self._profundidade_recursiva(self.raiz, valor, 0)

def _profundidade_recursiva(self, no, valor, contador):
        if no == None:
            return -1
        if no.valor == valor:
            return contador
        if valor < no.valor:
            return self._profundidade_recursiva(no.esq, valor, contador + 1)
        else:
            return self._profundidade_recursiva(no.dir, valor, contador + 1)

def imprimir_ancestrais(self, valor):
        lista_anc = []
        self._achar_ancestrais(self.raiz, valor, lista_anc)
        print("Ancestrais de", valor, ":", lista_anc)

def _achar_ancestrais(self, no, valor, lista):
        if no == None:
            return False
        if no.valor == valor:
            return True
        achou_esq = self._achar_ancestrais(no.esq, valor, lista)
        achou_dir = self._achar_ancestrais(no.dir, valor, lista)
        if achou_esq or achou_dir:
            lista.append(no.valor)
            return True
        return False

def imprimir_descendentes(self, valor):
        no_encontrado = self._buscar_no(self.raiz, valor)
        if no_encontrado == None:
            print("valor nao encontrado")
            return
        lista_desc = []
        self._pegar_todos(no_encontrado.esq, lista_desc)
        self._pegar_todos(no_encontrado.dir, lista_desc)
        print("Descendentes de", valor, ":", lista_desc)

def _buscar_no(self, no, valor):
        if no == None:
            return None
        if no.valor == valor:
            return no
        if valor < no.valor:
            return self._buscar_no(no.esq, valor)
        else:
            return self._buscar_no(no.dir, valor)

def _pegar_todos(self, no, lista):
        if no == None:
            return
        lista.append(no.valor)
        self._pegar_todos(no.esq, lista)
        self._pegar_todos(no.dir, lista)

def analisar_arvore(self, valor_busca):
        print("=" * 50)
        print("   DIAGNOSTICO GERAL DA ARVORE")
        print("=" * 50)

        if self.raiz != None:
            print("\nRaiz:", self.raiz.valor)
            print("Endereco da raiz:", hex(id(self.raiz)))
        else:
            print("arvore esta vazia!")
            return

        print()
        self.imprimir_nos_internos()
        self.imprimir_folhas()

        print("\nOrganizacao por niveis:")
        self.imprimir_niveis()

        print("\n" + "=" * 50)
        print("   DIAGNOSTICO ESPECIFICO - No:", valor_busca)
        print("=" * 50)

        no_busca = self._buscar_no(self.raiz, valor_busca)

        if no_busca == None:
            print("Valor", valor_busca, "nao esta na arvore")
            return

        grau = 0
        if no_busca.esq != None:
            grau = grau + 1
        if no_busca.dir != None:
            grau = grau + 1

        print("\nGrau do no", valor_busca, ":", grau)

        self.imprimir_ancestrais(valor_busca)
        self.imprimir_descendentes(valor_busca)

        altura = self.calcular_altura(no_busca)
        profundidade = self.calcular_profundidade(valor_busca)

        print("Altura do no", valor_busca, ":", altura)
        print("Profundidade do no", valor_busca, ":", profundidade)
        print("Endereco de memoria do no", valor_busca, ":", hex(id(no_busca)))
        print("=" * 50)