# define ordem 3

typedef struct no{

	int n; //Numero de chaves que a pagina possui
	int chaves[ordem - 1]; // Um vetor que pode armazenar todas as chaves
  int prrchaves[ordem - 1];//um vetor que armazena as PRR das chaves no arquivo data.txt 
	struct no *p[ordem]; // Numero de ponteiro que o nó possui

}BTPAGE;

/* Os vetores chaves e prrchaves estao relacionados da seguinte maneira, chave[x] = y,
 prrchaves[x]= PRR(y). */

