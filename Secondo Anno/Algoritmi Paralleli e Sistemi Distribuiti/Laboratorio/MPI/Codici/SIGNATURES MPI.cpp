// Inizializzazione di MPI
int MPI_Init(int *argc, char ***argv);

// Ottieni il numero di processi nel comunicatore
int MPI_Comm_size(MPI_Comm comm, int *size);

// Ottieni il rango di un processo nel comunicatore
int MPI_Comm_rank(MPI_Comm comm, int *rank);

// Termina MPI
int MPI_Finalize(void);

// Invia dati tramite MPI
int MPI_Send(void *buf, int count, MPI_Datatype datatype, int dest, int tag, MPI_Comm comm);

// Ricevi dati tramite MPI
int MPI_Recv(void *buf, int count, MPI_Datatype datatype, int source, int tag, MPI_Comm comm, MPI_Status *status);

// Ottieni il conteggio di elementi ricevuti
int MPI_Get_count(MPI_Status *status, MPI_Datatype datatype, int *count);

// Invia dati in modo non bloccante tramite MPI
int MPI_Isend(void *buf, int count, MPI_Datatype datatype, int dest, int tag, MPI_Comm comm, MPI_Request *request);

// Attendi la completa esecuzione di un'operazione MPI non bloccante
int MPI_Wait(MPI_Request *request, MPI_Status *status);

// Verifica lo stato di completamento di un'operazione MPI non bloccante
int MPI_Test(MPI_Request *request, int *flag, MPI_Status *status);

// Definisci un nuovo tipo di dato vettoriale MPI
int MPI_Type_vector(int block_count, int block_length, int stride, MPI_Datatype old_datatype, MPI_Datatype *new_datatype);

// Conferma il nuovo tipo di dato MPI
int MPI_Type_commit(MPI_Datatype *datatype);

// Rilascia il tipo di dato MPI
int MPI_Type_free(MPI_Datatype *datatype);
