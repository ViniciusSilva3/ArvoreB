//Funcao que vai descobrir a ordem a ser utilizada para construir a ARVORE B
//A profundidade provavelmente sempre vai ser 3, pois é um numero aceitavel de seeks
/*Para descobrir a quantidade de chaves é necessario ler o arquivo uma primeira vez e utilizar
um contador para ir armazenando esse numero*/
#include <math.h>

int AchaOrdem(int quantChaves, int profundidade){
	int ordem;
	ordem = 2 * sqrt(quantChaves/2);
	return ordem;
}
