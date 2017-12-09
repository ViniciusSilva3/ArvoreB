#ifndef funcoes_h
#define funcoes_h 1
#include "coisa.h"



void mostrar(coisa *lista,uint32_t tam){
  uint32_t a;
  for(a=0;a<tam;a++){
    printf("-->%s<--\n",lista[a].chave);
  }
}

coisa *criar_indice_ordenado(FILE *fp,uint32_t *tam_indice){
  //Declaracao das variaveis a serem utilizadas
  coisa *indice=NULL;
  *tam_indice=0;
  while(!feof(fp)){
    //esse monte de whiles abaixo servem para tirar lixo do inicio e do fim do arquivo
    while(!feof(fp)&&fgetc(fp)<'0');
    if(feof(fp))break;
    fseek(fp,-1,SEEK_CUR);
    while(!feof(fp)&&fgetc(fp)>'9');
    if(feof(fp))break;
    fseek(fp,-1,SEEK_CUR);
    //ordem: matricula nome op curso turma

    //aqui pega a posicao no arquivo para colocar no indice
    uint32_t pos=ftell(fp);

    //aqui aumenta o indicador do tamanho do indice
    ++*tam_indice;

    //aqui ve se ja tem alguma coisa no indice para saber se é para usar malloc ou realloc
    if(indice==NULL)indice=(coisa*)malloc(sizeof(coisa));
    else indice=realloc(indice,sizeof(coisa)*(*tam_indice));

    //aqui pega o indice
    fread(indice[*tam_indice-1].matricula,6,1,fp);fgetc(fp);
    fread(indice[*tam_indice-1].nome,40,1,fp);fgetc(fp);
    fread(indice[*tam_indice-1].op,5,1,fp);fgetc(fp);
    fread(indice[*tam_indice-1].curso,9,1,fp);fgetc(fp);
    fread(indice[*tam_indice-1].turma,2,1,fp);

    /*Esse while esta tratando das diferentes quebras de linha que existem no arquivo, apagando qualquer espaço que esteja entre o ultimo byte lido e a quebra de linha */
    while(fgetc(fp)!=10&&!feof(fp));


    //aqui gera a chave
    uint32_t a;
    for(a=0;a<6;a++){
      indice[*tam_indice-1].chave[a]=indice[*tam_indice-1].matricula[a];
    }
    for(a=0;a<24;a++){
      indice[*tam_indice-1].chave[a+6]=indice[*tam_indice-1].nome[a];
    }
    //aqui garante que vai terminar todas as "strings"
    indice[*tam_indice-1].turma[2]='\0';
    indice[*tam_indice-1].op[5]='\0';
    indice[*tam_indice-1].chave[30]='\0';
    indice[*tam_indice-1].matricula[6]='\0';
    indice[*tam_indice-1].nome[40]='\0';
    indice[*tam_indice-1].pos=pos;
    indice[*tam_indice-1].curso[9]='\0';


  }
  /* Aqui o heapsort ordena a lista de indices */
  //mostrar(indice,*tam_indice);
  heapsort(indice, *tam_indice);
//printf("\n---\n");  mostrar(indice,*tam_indice);printf("___\n");
  fclose(fp);
  return indice;

}

void deixa_oco(coisa **lista,uint32_t *tam,char *chave){
  uint32_t a;
  for(a=0;a<*tam;a++){
    if(strcmp((*lista)[a].chave,chave)==0){
      --*tam;
      uint32_t b;
      for(b=a;b<(*tam)-1;b++){
        (*lista)[b]=(*lista)[b+1];
      }
      *lista=realloc(*lista,*tam*sizeof(coisa));
      return;
    }
  }
  printf("Não encontrei");
}
void atualiza_registro(coisa *lista,uint32_t tam,char *chave){
  getchar();
  uint32_t a;
  for(a=0;a<tam;a++){
    if(strcmp(lista[a].chave,chave)==0){
      uint32_t b;

      printf("Nome: ");scanf("%40[^\n]",lista[a].nome);getchar();
      printf("Turma: ");scanf("%2s",lista[a].turma);getchar();
      printf("Op: ");scanf("%5s",lista[a].op);getchar();
      uint32_t matricula;
      printf("Matricula: ");scanf("%d",&matricula);
      sprintf(lista[a].matricula,"%06d",matricula);
      printf("Curso: ");scanf("%9s",lista[a].curso);getchar();
      for(b=strlen(lista[a].nome);b<40;b++)lista[a].nome[b]=' ';
      for(b=strlen(lista[a].turma);b<2;b++)lista[a].turma[b]=' ';
      for(b=strlen(lista[a].matricula);b<6;b++)lista[a].matricula[b]='0';
      for(b=strlen(lista[a].op);b<5;b++)lista[a].op[b]=' ';
      for(b=strlen(lista[a].curso);b<9;b++)lista[a].curso[b]=' ';

      for(b=0;b<6;b++){
        lista[a].chave[b]=lista[a].matricula[b];
      }
      for(b=0;b<24;b++){
        lista[a].chave[b+6]=lista[a].nome[b];
      }
      lista[a].turma[2]='\0';
      lista[a].op[5]='\0';
      lista[a].chave[30]='\0';
      lista[a].matricula[6]='\0';
      lista[a].nome[40]='\0';
      lista[a].curso[9]='\0';
      return;
    }
  }
  printf("Não encontrei");
}
void atualiza_lista(coisa *lista,uint32_t tam,char *arq){
  FILE *a=fopen(arq,"w");
  uint32_t b;
  for(b=0;b<tam;b++){
    printf("<%s %s %s %s %s>\n",lista[b].matricula,lista[b].nome,lista[b].op,lista[b].curso,lista[b].turma);
    fprintf(a,"%s %s %s %s %s\n",lista[b].matricula,lista[b].nome,lista[b].op,lista[b].curso,lista[b].turma);
  }
  fclose(a);
}










































void CriaIndSec(coisa *indice,uint32_t tam,char *saida){
  typedef struct tipo{
    char turma[3];
    char op[6];
    coisa *indice;
    uint32_t tam;
    struct tipo *prox;
  } tipo;
  FILE *indsec1 = fopen(saida, "w");

  tipo *a=NULL;
  tipo *novo(){
    tipo *_a=malloc(sizeof(tipo));
    _a->prox=NULL;
    _a->tam=1;
    _a->indice=(coisa*)malloc(sizeof(coisa));
    return _a;
  };

  uint32_t b;
  for(b=0;b<tam;b++){
    if(a==NULL){
      a=novo();
      a->indice[0]=indice[b];
      strcpy(a->turma,indice[b].turma);
      strcpy(a->op,indice[b].op);
    }
    else{
      tipo *_a=a;
      while(_a!=NULL){
        if(strcmp(_a->op,indice[b].op)==0&&strcmp(_a->turma,indice[b].turma)==0){
          _a->tam++;
          _a->indice=(coisa*)realloc(_a->indice,_a->tam*sizeof(coisa));
          _a->indice[_a->tam-1]=indice[b];
        }
        else if(_a->prox==NULL){
          _a->prox=novo();
          _a->prox->indice[0]=indice[b];
          strcpy(_a->prox->turma,indice[b].turma);
          strcpy(_a->prox->op,indice[b].op);
          break;
        }
        _a=_a->prox;
      }
    }
  }
  tipo *_a=a;
  while(_a!=NULL){
    fprintf(indsec1,"%s %s: ",_a->op,_a->turma);
    for(b=0;b<_a->tam;b++){
      fprintf(indsec1,"%s",_a->indice[b].chave);
      if(b<_a->tam-1){fprintf(indsec1," ");}
    }
    tipo *prox=_a->prox;
    if(prox!=NULL)fprintf(indsec1,"\n");
    free(_a->indice);
    free(_a);
    _a=_a->prox;
  }
  fclose(indsec1);
}





//Inicio da funcao de inserção de um novo elemento na lista
void insere_registro2(coisa **lista,uint32_t *tam){
  getchar();
  uint32_t a=*tam;
  ++*tam;
  printf("<%d %d>",a,*tam);
  *lista=realloc(*lista,sizeof(coisa)*(*tam));
  uint32_t b;
  printf("Nome: ");scanf("%40[^\n]",(*lista)[a].nome);getchar();
  printf("Turma: ");scanf("%2s",(*lista)[a].turma);getchar();
  printf("Op: ");scanf("%5s",(*lista)[a].op);getchar();
  uint32_t matricula;
  printf("Matricula: ");scanf("%d",&matricula);
  sprintf((*lista)[a].matricula,"%06d",matricula);
  printf("Curso: ");scanf("%9s",(*lista)[a].curso);getchar();
  for(b=strlen((*lista)[a].nome);b<40;b++)(*lista)[a].nome[b]=' ';
  for(b=strlen((*lista)[a].turma);b<2;b++)(*lista)[a].turma[b]=' ';
  for(b=strlen((*lista)[a].matricula);b<6;b++)(*lista)[a].matricula[b]='0';
  for(b=strlen((*lista)[a].op);b<5;b++)(*lista)[a].op[b]=' ';
  for(b=strlen((*lista)[a].curso);b<9;b++)(*lista)[a].curso[b]=' ';
  for(b=0;b<6;b++){
    (*lista)[a].chave[b]=(*lista)[a].matricula[b];
  }
  for(b=0;b<24;b++){
    (*lista)[a].chave[b+6]=(*lista)[a].nome[b];
  }
  (*lista)[a].turma[2]='\0';
  (*lista)[a].op[5]='\0';
  (*lista)[a].chave[30]='\0';
  (*lista)[a].matricula[6]='\0';
  (*lista)[a].nome[40]='\0';
  (*lista)[a].curso[9]='\0';
  return;
}



void InsereRegistro (void){
  char *matricula, *op;
  char *nome, *turma, *curso;
  matricula = malloc(7);
  op = malloc(6);
  nome = malloc(41);
  turma = malloc(3);
  curso = malloc(10);
  printf("Digite a Matricula: \n");
  scanf("%6s", matricula);
  getchar();
  printf("Digite o nome: \n");
  scanf("%40[^\n]", nome);
  getchar();
  printf("Digite o OP: \n");
  scanf("%5s", op);
  getchar();
  printf("Digite o curso: \n");
  scanf("%9s", curso);
  getchar();
  printf("Digite a turma: \n");
  scanf("%2s", turma);

  FILE *fp;
  uint32_t counter = 0;

  fp = fopen("lista1.txt", "r+");
  fseek(fp, 0, SEEK_END);
  fprintf(fp, "%s ", matricula);
  fprintf(fp, "%s", nome);
  fseek(fp, -48, SEEK_CUR);
  do{
    fgetc(fp);
  }while(fgetc(fp)!=10 && !feof(fp));
  
  while(!feof(fp)){
      fgetc(fp);
      counter++;
  }
  fclose(fp);
  fp = fopen("lista1.txt", "r+");
  fseek(fp, 0, SEEK_END);
  counter = 49 - counter;
  for(counter; counter>0; counter--)
      fprintf(fp, " ");
  fprintf(fp, "%s    ", op);
  fprintf(fp, "%s         %s\n", curso, turma);
  fclose(fp);

  free(matricula);
  free(op); free(nome); free(turma); free(curso);

 
}

#endif
