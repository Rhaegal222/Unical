#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

void* hello(void* arg){
    sleep(1);
    printf("Ciao %d\n", *(int *)arg);
    delete (int *)arg;
    return NULL;
}

int main1() {
    pthread_t tid;
    pthread_create(&tid, NULL, &hello, NULL);
    pthread_join(tid, NULL);
    return 0;
}

int main() {
    pthread_t tid[10];
    for (int i=0; i<10; i++){
        int *p = new int;
        *p=i;
        pthread_create(&tid[i], NULL, &hello, p);
    }
    for (int i=0; i<10; i++){
        pthread_join(tid[i], NULL);
    }
    return 0;
}
