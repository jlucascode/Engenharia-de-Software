#include<stdio.h>
#include<stdlib.h>


/* 1- Crie uma TAD para representar uma pessoa que ira ser cadastrado em um sistema de academia.
Dados necessarios: nome, matricula, idade, peso, altura*/

//RESPOSTA 1:
typedef struct Pessoa{
    char *nome;
    int matricula;
    int idade;
    float peso;
    float altura;
}pessoa;

struct Pessoa p1;
pessoa p1;

/* 2- Crie uma funcao que recebe os dados de um aluno da academia pelo terminal, salva esses dados 
em uma tad e apresenta no terminal seu nome e IMC */
//RESPOSTA 2:
void cria_tad_aluno(){
    
    aluno p1; 
    char nome[100];
    printf("Digite o nome do aluno: \n"); 
    scanf("%s", nome);
    p1.nome = nome;
    printf("Digite a matricula do aluno: \n");  
    scanf("%d", &p1.matricula);
    printf("Digite a idade do aluno: \n");  
    scanf("%d", &p1.idade);
    printf("Digite a peso do aluno: \n"); 
    scanf("%f", &p1.peso);
    printf("Digite a altura do aluno: \n");
    scanf("%f", &p1.altura);
    
    float imc = p1.peso/(p1.altura*p1.altura);
    printf("O aluno %s tem o imc = %.2f.\n", p1.nome, imc);
}

/* 3 - Crie uma TAD para representar um produto que ira ser cadastrado em um sistema de supermecado.
Dados necessarios: nome do produto, codigo de barra, preco, dia, mes e ano de validade*/



/* 4 - Crie uma funcao que recebe os dados de um produto pelo terminal, salva esses dados 
em uma tad, verifica se ele esta dentro da validade, se sim apresenta no terminal seu nome 
e seu preco com desconto de 20%.
Se o produto esta fora da validade apenas apresenta seu nome e a informacao: fora da validade!*/

//Dica:
void cria_tad_produto(){
    //declare a varivel do tipo produto;
    //coloque o printf e o scanf para carregar cada um dos dados:
    //coloque separado o dia, mes e ano, uma variavel inteira para cada valor.
    //faca um conjunto de ifs para comparar o dia, mes e ano, com o dia atual:
    //use o dia da aula pratica como dia atual.
    //caso o produto esteja dentro da validade faca o calculo do desconto (0.2*preco do produto);
    //coloque um printf com o nome do produto e o valor deste calculo.
    //caso nao esteja dentro da validade basta colocar um printf com o nome do produto e a frase "fora da validade".
}

/*5 - Crie um TAD para representar um aluno da disciplina de ED que ira ser cadastrado em um sistema no sigaa
Dados necessarios: nome, matricula, nota da avaliacao teorica, nota do trabalho de
 ordenacao, nota dos exercicios praticos*/

//agora não temos mais dicas e com vocês! :D 




/*6 - Crie uma funcao que recebe os dados do aluno por terminal, salva esses dados 
em uma tad e aresenta no terminal o nome do aluno e se ele esta aprovado, 
reprovado ou de final na disciplina*/

//agora não temos mais dicas e com vocês! :D 

int main(){

   cria_tad_aluno();
   cria_tad_produto();
   //colocar aqui a chamda da funcao criada na questao 6.
    return 0;
}




