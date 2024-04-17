#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

void* run(void * arg){
	printf("ciao\n");
	return NULL;
}

int main(int arg, char* argv[])
{
	pthread_t thid;
	int ris = pthread_create(&thid, NULL, &run, NULL);
	if (ris){
		printf("errore creazione thread\n");
		exit(-1);
	}
	pthread_join(thid, NULL);
}
