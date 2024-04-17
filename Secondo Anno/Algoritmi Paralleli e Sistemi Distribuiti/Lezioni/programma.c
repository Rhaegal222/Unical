#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <unistd.h>

int n = 100000, num = 0;

// creazione e distruzione di un mutex, serve a lockare la risorsa ed evitare le race condition
int pthread_mutex_init(pthread_mutex_t * mutex);
int pthread_mutex_destroy(pthread_mutex_t * mutex);

void * run(void * args){
    //pthread_mutex_lock();
    for(int i = 0; i < n; i++) num++;
    return NULL;
}

int main(){
    pthread_t id0, id1;
    pthread_create(&id0, NULL, &run, NULL);
    pthread_create(&id1, NULL, &run, NULL);

    pthread_join(id0, NULL);
    pthread_join(id1, NULL);
    printf("num = %d \n",num);
}