#include <stdlib.h>
#include <stdio.h>

int main(){
	char sexe[5];
	int age;
	char gen1[]="homme";
	char gen2[]="femme";
	printf("le sexe : ");
	scanf("%s" , &sexe);
	printf("l'age : ");
	scanf("%d" , &age);
	if( strcmp(gen1,sexe) && age >= 20 ){
		printf("vous devez payer limpot");
    }
	else if ( strcmp(gen2,sexe) && age >= 18 && age <= 35){
		printf("vous devez payer limpot");
	}
	else{
		printf("ne payee pas limpot");
	}


}
