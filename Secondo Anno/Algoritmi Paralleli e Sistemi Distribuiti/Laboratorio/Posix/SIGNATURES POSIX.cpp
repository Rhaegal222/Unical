// Creazione di un thread POSIX
int pthread_create(pthread_t * thread,
                   const pthread_attr_t * attr,
                   void * (*start_routine)(void *),
                   void *arg);

// Join per un thread POSIX
int pthread_join(pthread_t thread, void **value_ptr);

// Inizializzazione di un mutex POSIX
int pthread_mutex_init(pthread_mutex_t *mutex,
                       const pthread_mutexattr_t *attr);

// Blocco di un mutex POSIX
int pthread_mutex_lock(pthread_mutex_t *mutex);

// Sblocco di un mutex POSIX
int pthread_mutex_unlock(pthread_mutex_t *mutex);

// Distruzione di un mutex POSIX
int pthread_mutex_destroy(pthread_mutex_t *mutex);

// Inizializzazione di una variabile di condizione POSIX
int pthread_cond_init(pthread_cond_t *cond,
                      const pthread_condattr_t *cond_attr);

// Distruzione di una variabile di condizione POSIX
int pthread_cond_destroy(pthread_cond_t *cond);

// Attendi su una variabile di condizione POSIX
int pthread_cond_wait(pthread_cond_t *cond, pthread_mutex_t *mutex);

// Segnala una variabile di condizione POSIX
int pthread_cond_signal(pthread_cond_t *cond);

// Segnala tutti i thread in attesa su una variabile di condizione POSIX
int pthread_cond_broadcast(pthread_cond_t *cond);
