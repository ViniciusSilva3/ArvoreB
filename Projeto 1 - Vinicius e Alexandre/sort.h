#ifndef sort_h
#define sort_h 1
#include "coisa.h"

unsigned char maior(coisa a,coisa b){
	uint32_t c;
	for(c=0;c<30;c++){
		if(a.chave[c]>b.chave[c])return 1;
		if(a.chave[c]<b.chave[c])return 2;
	}
	return 0;
}
void bubblesort(coisa *a,uint32_t tam){
	uint32_t c,b;
	for(c=0;c<tam;c++){
		for(b=0;b<tam-1;b++){
			coisa aux;
			if(maior(a[b],a[b+1])==1){
				aux=a[b];
				a[b]=a[b+1];
				a[b+1]=aux;
			}
		}
	}
}
/* PARA A FUNCAO HEAPSORT CONSIDERAR:

   *Filho da direita = 2*i + 2
   *Filho da esquerda = 2*i + 1
*/
uint32_t pai(uint32_t i){
  uint32_t retorno;
  retorno = (i-1)/2;
  return retorno;
}

void swap(coisa *a, uint32_t x, uint32_t y){
  coisa aux;
  aux = a[x];
  a[x] = a[y];
  a[y] = aux;
}

void siftDown(coisa *a, uint32_t start, uint32_t end){
  uint32_t raiz, troca, filho;
  raiz = start;
  while((2*raiz+1) <= end){ /* enquanto a raiz ainda possuir um filho */
      filho = 2*raiz + 1;
      troca = raiz;
      if(maior(a[troca], a[filho]) == 2)
        troca = filho;
      if(filho+1 <= end && maior(a[troca], a[filho+1]) == 2)
        troca = filho + 1;
      if(troca == raiz)
        return;
      else{
          swap(a, raiz, troca);
          raiz = troca;
      }
  }
}

void heapify(coisa *a, uint32_t tam){
  int inicio;
  inicio = pai(tam-1);
  while( inicio >= 0){
      siftDown(a, inicio, tam-1);
      inicio --;
  }
  
}

void heapsort(coisa *a, uint32_t tam){
  uint32_t fim;
  coisa aux;
  heapify(a, tam);
  /*aqui vamos dar inicio ao loop que vai ordenar o array */
  fim = tam - 1;
  while(fim > 0 ){
      swap(a, fim, 0);
      fim --;
      siftDown(a, 0, fim);
  }
}

#endif
