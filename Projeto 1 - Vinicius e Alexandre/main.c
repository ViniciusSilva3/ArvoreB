#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>
#include <string.h>
#include "coisa.h"
#include "sort.h"
#include "funcoes.h"









void main()
{
  FILE *fp, *ind1;
  fp = fopen("lista1.txt", "r");
  uint32_t *tam;
  tam = malloc(2*sizeof(uint32_t));
  coisa **indice=malloc(2*sizeof(coisa*));
  uint32_t a;
  indice[0] = criar_indice_ordenado(fp, &(tam[0]));
  ind1 = fopen("indicelista1.ind", "w");
  for(a=0;a<tam[0];a++){
    fprintf(ind1, "%s %06d\t\n",indice[0][a].chave,indice[0][a].pos);
  }
  fclose(ind1);

  FILE *fp2, *ind2;
  fp2 = fopen("lista2.txt", "r");
  indice[1] = criar_indice_ordenado(fp2, &(tam[1]));
  /* Aqui vale o mesmo comentario feito na abertura de ind1 */
  ind2 = fopen("indicelista2.ind", "w");
  for(a=0;a<tam[1];a++){
    fprintf(ind2, "%s %d\t\n",indice[1][a].chave,indice[1][a].pos);
  }
  fclose(ind2);
  
  CriaIndSec(indice[0],tam[0],"indiceseclista1.ind");
  CriaIndSec(indice[1],tam[1],"indiceseclista2.ind");

  //################################ MENU #########################
  FILE *temp, *temp2;
  uint32_t entrada = 0, entrada1 = 0;
  char *listinha;
  char *listinha1=malloc(20);
  char *remover=malloc(35);
  sprintf(listinha1,"indiceseclista%d.ind",entrada1-1);
  listinha = malloc(13);
  do{
    printf("\n"); printf("MENU:\n");
    printf("Digite qual lista deseja manipular:\n\n"); printf("[1] : Lista 1;\n"); printf("[2] : Lista 2; \n");
    scanf("%d", &entrada1);
    while(entrada1!=1 && entrada1!= 2)
      scanf("%d", &entrada1);
    sprintf(listinha,"lista%d.txt",entrada1-1);
    if(entrada1 == 1){
      strcpy(listinha,"lista1.txt");
      temp = fopen("lista1.txt", "r");
      temp2 = fopen("indicelista1.ind", "r");
    }
    else{
      strcpy(listinha,"lista2.txt");
      temp = fopen("lista2.txt", "r");
      temp2 = fopen("indicelista2.ind", "r");
    }

    printf("\n");
    printf("Qual operacao deseja realizar na Lista : \n\n");
    printf("[1] : Verificar o arquivo armazenado na memoria :\n");
    printf("[2] : Verificar lista de Indices primarios :\n");
    printf("[3] : Verificar lista de Indices Secundarios :\n");
    printf("[4] : Adicionar um novo elemento na lista :\n");
    printf("[5] : Remover um elemento da lista :\n");
    printf("[6] : Atualizar um Registro :\n");
    printf("[7] : Trocar a lista que deseja manipular :\n");
    printf("[0] : Sair do programa.\n");
    while(entrada < 0 && entrada > 7);
      scanf("%d", &entrada);
    
    switch(entrada){
        /*estou ajustando aqui ainda, estava só testando se o menu funcionaria */
        case 1:
            printf("MATRIC NOME\t\t\t\t\tOP\tCURSO\t TURMA\n");
            for(a=0;a<tam[entrada1-1];a++){
                printf("%s %s %s\t%s\t %s\n", (indice[entrada1-1][a]).matricula, (indice[entrada1-1][a]).nome, (indice[entrada1-1][a]).op, (indice[entrada1-1][a]).curso, (indice[entrada1-1][a]).turma);

            }
  
            break;
        case 2:
            for(a=0;a<tam[entrada1-1];a++){
              printf("%s %d\t\n",indice[entrada1-1][a].chave,indice[entrada1-1][a].pos);
            }
            fclose(temp2);
            break;
        case 3:
            CriaIndSec(indice[entrada1-1],tam[entrada1-1],listinha1);
            //AINDA FALTA ESSE
            
                
            break;
        case 4:
            //o arquivo deve ser mostrado antes da inserção
            printf("Arquivo de indices antes da inserçao:\n");
            for(a=0;a<tam[entrada1-1];a++){
              printf("%s %d\t\n",indice[entrada1-1][a].chave,indice[entrada1-1][a].pos);
            }

            insere_registro2(&(indice[entrada1-1]), &(tam[entrada1-1]));
            atualiza_lista(indice[entrada1-1], tam[entrada1-1], listinha); free(indice[entrada1-1]);
            indice[entrada1-1] = criar_indice_ordenado(temp, &(tam[entrada1-1]));
            printf("Arquivo de indices depois da inserçao:\n");
            for(a=0;a<tam[1];a++){
                fprintf(temp2, "%s %d\t\n",indice[entrada1-1][a].chave,indice[entrada1-1][a].pos);
            }
            fclose(temp2);
            break;
        case 5:
            printf("Digite a chave primaria do registro que deseja remover:\n");getchar();
            //POSSIVELMENTE O ERRO É ESSE REMOVER, ELE TEM TAMANHO 35, E MUITAS VEZES AS CHAVES NAO VAO TER ESSE TAMANHO
            scanf("%30[^\n]", remover);
            for(a=strlen(remover);a<30;a++)remover[a]=' ';
            remover[30]='\0';
            printf("Arquivo de indices antes da remocao:\n");
            for(a=0;a<tam[entrada1-1];a++){
              printf("%s %d\t\n",indice[entrada1-1][a].chave,indice[entrada1-1][a].pos);
            }
            deixa_oco(&(indice[entrada1-1]), &(tam[entrada1-1]), remover);
            atualiza_lista(indice[entrada1-1], tam[entrada1-1], listinha); free(indice[entrada1-1]);
            indice[entrada1-1] = criar_indice_ordenado(temp, &(tam[entrada1-1]));

            printf("Arquivo de indices depois da remocao:\n");
            for(a=0;a<tam[1];a++){
                fprintf(temp2, "%s %d\t\n",indice[entrada1-1][a].chave,indice[entrada1-1][a].pos);
            }
            fclose(temp2); free(remover);
            break;
        case 6:
            atualiza_lista(indice[entrada1-1], tam[entrada1-1], listinha);
            break;
        case 7:break;
        case 0:
            free(tam); free(indice[0]);free(indice[1]); free(indice);free(listinha);free(listinha1);
            return;
            break;
    }
  }while(1);
  
  return ;
}
