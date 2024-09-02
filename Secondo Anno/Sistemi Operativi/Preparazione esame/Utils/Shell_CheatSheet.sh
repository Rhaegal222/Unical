

#Aprire BASH

Ctrl+Alt+F1

Ctrl+Alt+F7

#Uscire da BASH

Ctrl-D

# Interrompere l'esecuzione di un comando

Ctrl-C

#Ripulisci il terminale

Ctrl-L


#Ricevere aiuto

man # man <comando> per la visualizzazione del manuale di quel comando

history # Permette di visualizzare l'elenco completo dei comandi che abbiamo digitato in precedenza

info

opzione --help


#nella shell si usano '/' per navigare nelle directories



################################################## COMANDI DI NAVIGAZIONE ##################################################

mkdir <nomedir>   # Crea la cartella <nomedir>
    # Opzioni
    -p  # Crea anche la directori padre se non esistono 
    -m  <mode> #  Imposta le autorizzazioni della directory appena creata secondo il valore specificato
    -v  # Mostra un output dettagliato delle operazioni eseguite da mkdir

rmdir <nomedir> # Rimuove la cartella <nomedir> SOLO se è vuota
    # Opzioni
    -p  # Rimuove anche le directories padre se sono vuote
    -v  # Mostra un output dettagliato delle operazioni eseguite da rmdir

rm <nomefile>   # Rimuove il file <nomefile>
    # Opzioni
    -r  # Ricorsivo - rimuove i contenuti delle directories uno dopo l'altro
    -i  # Interattivo - avvisa prima di cancellare ciascun file
    -f  # Forza - forza rm a cancellare i files ignorando errori o avvertimenti
    -v  # Mostra un output dettagliato delle operazioni eseguite da rm

cd <nomedir>    # Cambia la cartella corrente a </nomedir>
    # Opzioni
    ..  # Sposta la working directory corrente alla directory padre
    -   # Sposta la working directory alla precedente su cui si trovava
    ~   # Sposta la working directory alla directory home

pwd     # Stampa la cartella corrente


ls <nomedir>  # Elenca tutto il contenuto di <nomedir> o della cartella corrente se non specificato
    # Opzioni
    -a  # Tutti i files, compresi quelli nascosti
    -F  # Aggiunge / per le directories, * per gli eseguibili, @ per i link simbolici
    -l  # Formato completo - dettagli per i files
    -m  # Elenca i files come se fossero un testo scritto, separandoli con la virgola
    -r  # Inverte l'ordine alfabetico
    -R  # Ricorsivo; comprende le sottodirectories
    -s  # Dimensione dei files in blocchi
    -t  # Elenca secondo la data dell'ultima modifica
    -u  # Elenca secondo la data dell'ultimo accesso
    -i  # Inode di ciascun file
    -1  # Elenca un file per riga
    -lh # Elenca i files con le dimensioni in formato leggibile
    

################################################## COMANDI DI GESTIONE DEI FILE ##################################################

cp <nomefile1> <nomefile2> [<nomedir>]  # Crea una copia di <nomefile> in file2
cp <nomefile1> ... <nomefileX> [<nomedir>] #Crea una copia di tutti i file specificati nella directory
    # Opzioni
    -i  # Chiede conferma prima di sovrascrivere un file di destinazione esistente
    -r  # Ricorsivo - copia i files e lesottodirectories uno dopo l'altro
    -u  # Sposta solo i file di origine che sono più recenti rispetto ai file di destinazione
    -v  # Mostra un output al dettaglio delle operazioni eseguite
    -n  # Impedisce di sovrascrivere un file di destinazione esistente
    -p  # Conserva i permessi di origine
    -b  # Crea un backup del file di destinazione se esiste già
    -S  # Crea un backup del file di destinazione se esiste già, aggiungendo un suffisso
    -v  # Mostra un output dettagliato delle operazioni eseguite da cp


mv <nomefile1> <nomefile2> [<nomedir>] # Rinomina <nomefile1> in file2
mv <nomefile1> ... <nomefileX> [<nomedir>] # muove tutti i file nella directory
    # Opzioni
    -i  # Chiede conferma prima di sovrascrivere un file di destinazione esistente
    -f  # Sposta o rinomina i file senza richiedere conferma
    -v  # Mostra un output al dettaglio delle operazioni eseguite
    -n  # Impedisce di sovrascrivere un file di destinazione esistente
    -u  # Sposta solo i file di origine che sono più recenti rispetto ai file di destinazione
    -t  # Specifica la directory di destinazione per i file o directory che si vuole spostare


cat <nomefile>   # Stampa su terminale il contenuto di <nomefile>
cat <nomefile1> <nomefile2>  # Concatena i file <nomefile1> e <nomefile2> e stampa il risultato
    # Opzioni
    -n  # Precede ogni linea con un numero, le righe vengono numerate
    -b  # Mostra i numeri di riga solo per le righe non vuote, le righe vuote non vengono numerate
    -s  # Comprime le righe vuote consecutive in una singola riga vuota
    -v  # Visualizza i caratteri non stampabili
    -e  # Visualizza $ alla fine di ogni riga
    -t  # Visualizza i caratteri di tabulazione
    -a  # Combina le precedenti 3 opzioni
    -E  # Visualizza $ alla fine di ogni riga 
    -T  # Visualizza i caratteri di tabulazione

nano <nomefile>   # Modifica il <nomefile> da terminale (alias: pico)


file <nomefile>   # Analizza il tipo di file di <nomefile>
    # Opzioni
    -b  # Restituisce una descrizione breve del tipo di file senza includere il nome
    -e  # Esclude determinati tipi di file dalla determinazine del tipo

touch <nomefile>   # Crea un nuovo file vuoto dal nome <nomefile>
    # Opzioni
    -a  # Aggiorna il timestamp di accesso del file senza modificarne il contenuto
    -c  # Non crea il file se non esiste
    -d  # Imposta il timestamp del file al timestamp specificato

head <nomefile>    # Fornisce la parte iniziale del file in ingresso
    # Opzioni
    -n  # Mostra le prime n linee (10 se n non viene specificato)
    -c  # Specifica il numero di byte da visualizzare anzichè il numero di righe 
    -q  # Disabilità l'output dei nomi dei file prima di ogni riga di output
    #Esempio
    head -5 file.txt #mostra le prime 5 righe del file file.txt (oppure head -n 5 file.txt)
    head -n -1 #stampa tutte le righe di un file o di un flusso di input tranne l’ultima.

tail <nomefile>    # Fornisce la parte finale del file in ingresso
    # Opzioni
    -n  # Mostra le ultime n linee (10 se n non viene specificato)
    -c  # Specifica il numero di byte da visualizzare anzichè il numero di righe 
    -q  # Disabilità l'output dei nomi dei file prima di ogni riga di output
    -f  # Mostra i dati aggiunti al file mentre il file cresce
    #Esempio
    tail -5 file.txt #mostra le ULTIME 5 righe del file file.txt (oppure tail -n 5 file.txt)
    tail -n +2 file.txt #mostra tutte le righe di un file a partire dalla seconda riga.

less <nomefile>  # Legge il contenuto del <nomefile> (stessa modalità del man)
    # Opzioni
    -o  # Copia l'output sul file specificato nel caso in cui l'input provenga da una pipe
    -p  # mostra il file a partire dalla prima occorrenza di <pattern>

    # Comandi
    <space> # Mostra la schermata successiva
    <invio> # Visualizza la riga di testo successiva
    frecce_direzionali  # Per spostarsi su e giù di una linea per volta
    q   # Per uscire dal comando 
    /pattern    # Cerca il pattern indicato all'interno del testo
    :n  # Salta al file successivo (quando visualizziamo più file)
    :p  # Salta al file precedente

more <nomefile>
    # Opzioni
    -c  # Mostra le schermate successive dall'alto della pagina
    -s  # Sostituisce le linee vuote consecutive con un unica linea vuota
    +/pattern  # mostra il file a partire dalla prima occorrenza di <pattern>

    # Comandi
    <space> # Mostra la schermata successiva
    <invio> # Visualizza la riga di testo successiva
    h   # Informazioni aggiuntive
    q   # Esce dal programma
    v   # Apre il file con l'editor vi
    /pattern    # Cerca il pattern indicato all'interno del testo
    :n  # Salta al file successivo (quando visualizziamo più file)
    :p  # Salta al file precedente

zcat <nomefile> # Visualizza il contenuto di un file compresso
    # Opzioni
    -f  # Forza la decompressione anche se il file non è compresso
    -d  # Decomprime il file

unzip <nomefile>    # Estrae il contenuto di un file compresso
    # Opzioni
    -l  # Mostra l'elenco dei file contenuti nel file compresso
    -t  # Testa l'integrità del file compresso
    -v  # Mostra l'elenco dei file estratti
    -f  # Forza la decompressione anche se il file non è compresso
    -d  # Specifica la directory di destinazione per i file estratti

echo <stringa>  # Stampa la <stringa> su terminale
    # Opzioni
    -n  # Non inserisce un carattere di nuova linea alla fine della stringa
    -e  # Interpreta i caratteri di escape
    -E  # Non interpreta i caratteri di escape


################################################## RICERCA TRA DIRECTORY E FILE ##################################################

find <nomedir> -name <nomefile>  # Cerca il file di nome <nomefile> a partire da /<nomedir>
    # Opzioni
    -atime n    # Files visitati n giorni fa
    -mtime n    # Files modificati n giorni fa
    -size n[bckw]   # Files di dimensione esattamente, maggiore o minore n - Es: Trovare file di dimensione tra 1 e 2 kilobyte: find /path/to/directory -size +1k -size -2k
                    #   n può essere data in blocchi da 512 byte -> b
                    #                        caratteri da 1 byte -> c
                    #                        due parole da due byte -> w  
    -type c # tipo di file (f -> file, d -> directory, l -> link)
    -name <name>    # Trova tutti i files di nome <name>
    -newer <name>   # Trova tutti i file più recenti del file <nome>
    -user <name>    # Trova tutti i file che hanno l'utente <name> come owner
    -group <name>   # Filtra in base al gruppo del proprietario
    -maxdepth n     # Trova tutti i file che si trovano ad una "profondità" massima (innestati nelle cartelle) di n
    -exec <command> [options] {}\;  # esegue il comando <command> usando come input il file trovato
                                    # {} rappresenta il percorso del file trovato
                                    # \; termina la linea di comando                                
    -ok <command> [options] {}\;    # come exec, ma richiede conferma
    -print  # mostra i file trovati sullo schermo
    # Esempio
    find /home -type f -name "*.txt" -exec basename {} \; -exec echo \; #trova tutti i file con estensione .txt nella directory /home e stampa solo il nome del file
    #basename è un comando che rimuove il percorso completo da un file, lasciando solo il nome del file
    #exec echo stampa una riga vuota tra i nomi dei file trovati

grep <regex> <nomedir> # Cerca in tutti i file collocati nella directory <nomedir> o nel file la regex <regex>
    # Opzioni
    -v  # Restituisce righe che NON corrispondono alla stringa di ricerca
    -n  # Visualizza anche il numero di riga
    -c  # Mostra il numero di linee in cui la sequenza viene trovata, ma non le linee stesse
    -i  # Non distingue tra maiuscole e minuscole
    -w  # Trova solo parole intere
    -q  # dà 0, se il testo è stato trovato, 1 altrimenti
    -l  # Visualizza solo i nomi dei file che contengono le righe corrispondenti all'espressione regolare
    -P  # Usa la sintassi Perl per eseguire le regex
    -r # Cerca ricorsivamente in tutte le sottodirectory
    #Esempio
    grep "hello" nomeCartella/* #se non sono nella giusta directory
    grep "hello" * #se sono nella giusta directory in cui cercare
    grep "hello" nomefile.txt #mostra solo le righe che contengono la parola 'hello' nel file 'nomefile.txt'

cut <nomefile>  # Estrae parti di una linea di testo
    # Opzioni
    -c  # Estrae i caratteri specificati
    -d  # Usa il carattere specificato come delimitatore
    -f  # Estrae i campi specificati
    -s  # Non visualizza le linee che non contengono il delimitatore
    # Esempio
    cut -d ' ' -f 5- # estrae tutto dalla quinta colonna in poi
    cut -d ' ' -f 2,4,6 # estrae la sseconda, quarta e sesta colonna
    cut -d ' ' -f 1-7 # estrae dalla prima alla settima colonna
    --complement -f 2 # estrae tutto tranne la seconda colonna

awk 'pattern { action }' <nomefile> # manipola il testo leggendolo riga per riga
    # Opzioni
    -F  # Imposta il delimitatore di campo
    -f  # Legge il programma awk da un file
    -v  # Imposta una variabile

    # Esempio
    awk '{ print $1, $3 }' file.txt # Questo comando stampa il primo e il terzo campo di ogni riga del file "file.txt".
    awk '/ciao/ { print $1 }' file.txt # Questo comando stampa il primo campo di tutte le righe del file "file.txt" che contengono la parola "ciao".
    awk -F'\t' '{sum += $2} END {print sum}' file.txt # Questo comando somma tutti i numeri della seconda colonna del file "file.txt" e stampa il risultato.
    awk '$3 > 10' file.txt # Questo comando stampa tutte le righe del file "file.txt" in cui il terzo campo è maggiore di 10.
    awk -F',' '{sum += $4} END {print sum/NR}' file.csv # Questo comando calcola la media del quarto campo del file "file.csv" e stampa il risultato.
    awk '{gsub(/vecchio/, "nuovo"); print}' file.txt awk # Questo comando sostituisce la prima occorrenza della parola "vecchio" con la parola "nuovo" in ogni riga del file "file.txt" e stampa il risultato.
    awk 'END {print NR}' file.txt # Questo comando stampa il numero di righe del file "file.txt".

sort <nomefile> # Ordina un flusso di testo, o un file, in base ai criteri di ordinamento forniti
    # Opzioni
    -c  # Verifica se il file è già ordinato
    -u  # Elimina dal risultato le linee duplicate
    -f  # Non distingue tra caratteri maiuscoli e minuscoli
    -r  # Inverte il senso di ordinamento
    -n  # Ordina numericamente
    -k <chiave_di_ordinamento> # Indica una porzione della linea da usare come chiave per l'ordinamento
    # Esempio
    sort -k 2,2 -k 1,1 file.txt # Ordina il file "file.txt" in base al secondo campo, e poi in base al primo campo

uniq <nomefile> # Elimina le righe duplicate di un file che è stato ordinato (spesso in coppia con sort)
    # Opzioni
    -c  # Precede ogni linea con un conteggio del numero di volte consecutive in cui è ripetuta 
    -d  # Mostra solo le linee duplicate
    -i  # Non distingue tra maiuscole e minuscole
    -u  # Elimina dal risultato le linee duplicate

wc <nomefile>   # Fornisce il Word Count presenti in un file o in un flusso di testo
    # Opzioni
    -w  # Fornisce solo il numero delle parole
    -l  # Fornisce solo il numero delle righe
    -c  # Fornisce solo il numero dei byte
    -m  # Fornisce solo il numero dei caratteri
    -L  # Fornisce solo la dimensione della riga più lunga

du <nomedir>    # Mostra la dimensione di <nomedir>
    # Opzioni
    -h  # Mostra la dimensione in un formato leggibile
    -s  # Mostra solo la dimensione totale della directory
    -a  # Mostra la dimensione di tutti i file, non solo delle directories
    -c  # Mostra la dimensione totale alla fine dell'output
    -d  # Specifica la profondità massima della ricerca
    -x  # Mostra solo i file nello stesso filesystem
    -k  # Mostra la dimensione in kilobyte
    -m  # Mostra la dimensione in megabyte
    -B  # Specifica la dimensione del blocco

################################################## PIPING ##################################################

|   # La pipe viene usata per collegare i comandi in modo sequenziale (immagina una tubatura - pipe)

    # Esempio
    comando1 | comando2 | comando3  # L'output di comando1 verrà dato a comando2 e a sua volta l'output di comando2 verrà dato a comando3   

    pierpaolo@Mauricio:~$ ls | grep "file" | wc -l
                            #   Conta il numero di file presenti nella directory corrente 

# Ogni programma eseguito dalla shell apre tre files:
    # Standard input <- 0    -  Fornisce un modo per inviare dati ad un processo, lo standard input viene letto dalla tastiera del terminale   
    # Standard output <- 1   -  Fornisce al programma un mezzo per rendere disponibili i dati. Di default lo standard output viene usato dallo schermo del terminale
    # Standard error <- 2    -  È dove il programma registra ogni eventuale errore incontrato durante l'esecuzione. Di default, anche lo standard error viene indirizzato sullo schermo del terminale 

    # Esempi

    pierpaolo@Mauricio:~$ ls 1> pippo
    #oppure
    pierpaolo@Mauricio:~$ ls > pippo
                                #   Scrive l'output di ls nel file "pippo"
    pierpaolo@Mauricio:~$ ls 2> pippo
                                #   Scrive l'errore "-bash: list: command not found" nel file "pippo"

<comando> < <nomefile>  # Leggere l'input da un file
    #Esempio:
    cat < file.txt
<nomefile> > <comando>  # Memorizzare l'output su un file (sovrascrivendo il file)
    #Esempio:
    ls > file.txt
<nomefile> >> <comando> # Appendere l'output al file

<comando> >& <nomefile>   # Impone alla shell di inserire lo standard error e lo standard output del comando in un file detto <nomefile>

################################################## CARATTERI JOLLY ##################################################

*   # 0 o più caratteri
+   # 1 o più caratteri
?   # Un qualsiasi singolo carattere

#BONUS
[]  # Un singolo carattere tra quelli specificati
[^] # Un singolo carattere che non è tra quelli specificati
{}  # Un numero specifico di ripetizioni di un carattere o di un gruppo di caratteri
^   # Inizia con
$   # Finisce con

#Esempi
ls -l /etc/*.conf  # Mostra tutti i file con estensione .conf nella directory /etc
ls -l /etc/*.[ch]  # Mostra tutti i file con estensione .c o .h nella directory /etc
ls -l /etc/*.{conf,backup}  # Mostra tutti i file con estensione .conf o .backup nella directory /etc
ls -l /etc/[^a]*  # Mostra tutti i file nella directory /etc che non iniziano con la lettera 'a'


################################################## VARIABILI D'AMBIENTE ##################################################

env # Mostra tutte le variabili d'ambiente

export  # cambia il valore su una di esse
    # Esempio
    export PATH=$PATH:/nuova/directory

# Variabili speciali
#   $SHELL - $PATH - $HOME
# $HOME - La directory home dell'utente corrente


################################################## GESTIONE PROCESSI E JOB ############################################################

ps  # Mostra la lista dei processi attivi e i loro id
    # Opzioni
    -e  # Mostra informazioni su tutti i processi di tutti gli utenti
    -x  # Mostra i processi che non sono associati ad una tty (tty=teletype cioè il terminale)
    -u  # Mostra solo i processi di un utente specificato
    -f  # Mostra output dettagliato
    -p  # Mostra le informazioni sul processo specificato dal PID
    -a  # Mostra tutti i processi, inclusi quelli di altri utenti non associati ad una tty
    -eo pid,tty,time,cmd,%cpu,%mem  # Mostra solo le colonne PID, TTY, TIME, CMD, %CPU e %MEM

    #Esempio Output:
        PID TTY          TIME CMD
        1234 pts/1    00:00:00 bash
        5678 pts/1    00:00:01 ps
        #PID: Process ID
        #TTY: Terminale associato al processo
        #TIME: Tempo di CPU utilizzato
        #CMD: Comando che ha avviato il processo

top  # Mostra la lista dei processi attivi in tempo reale e le attività gestite dal kernel ordinati per utilizzo della CPU.
    # Opzioni
    -e  # Mostra informazioni su tutti i processi di tutti gli utenti
    -x  # Mostra i processi che non sono associati ad una tty
    -u  # Mostra solo i processi di un utente specificato
    -f  # Mostra output dettagliato
    -p  # Mostra le informazioni sul processo specificato dal PID
    -a  # Mostra tutti i processi, inclusi quelli di altri utenti non associati ad una tty

    #Esempio Output:
        top - 10:02:35 up  1:35,  2 users,  load average: 0.05, 0.10, 0.09
        Tasks: 192 total,   1 running, 191 sleeping,   0 stopped,   0 zombie
        %Cpu(s):  0.3 us,  0.1 sy,  0.0 ni, 99.6 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
        KiB Mem :  8180308 total,  1144200 free,  3982128 used,  3053980 buff/cache
        KiB Swap:  2097148 total,  2097148 free,        0 used.  3800040 avail Mem 

        PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
        1675 user      20   0  157284  12456   4716 S   0.3  1.2   0:01.36 bash
        892 root      20   0  22592   1128    924 S   0.0  0.1   0:00.03 init
        2437 user      20   0  47184   3624   2972 R   0.0  0.3   0:00.01 top
            #Tasks: Numero totale di processi e il loro stato (running, sleeping, stopped, zombie).
            #%Cpu(s): Percentuali di utilizzo della CPU suddivise per tipo di attività.
            #KiB Mem: Informazioni sulla memoria fisica totale, libera, usata e disponibile.
            #KiB Swap: Informazioni sulla memoria di swap totale, libera e usata.
            #PID: Process ID
            #USER: Utente che ha avviato il processo
            #PR: Priorità del processo
            #NI: Nice value del processo
            #VIRT: Dimensione virtuale del processo
            #RES: Dimensione residente del processo
            #SHR: Dimensione condivisa del processo
            #S: Stato del processo
            #%CPU: Utilizzo della CPU
            #%MEM: Utilizzo della memoria
            #TIME+: Tempo di CPU utilizzato
            #COMMAND: Comando che ha avviato il processo

htop   # Come top ma semplificato e con la possibilità di interagire 
    # Opzioni
    -e  # Mostra informazioni su tutti i processi di tutti gli utenti
    -x  # Mostra i processi che non sono associati ad una tty
    -u  # Mostra solo i processi di un utente specificato
    -f  # Mostra output dettagliato
    -p  # Mostra le informazioni sul processo specificato dal PID
    -a  # Mostra tutti i processi, inclusi quelli di altri utenti non associati ad una tty

kill <pid>  # Termina il processo con process id <pid>

jobs    # Mostra i task eseguiti in background dall'utente

fg  # Sposta un task da background a foreground

bg  # Riprende l'esecuzione di un task lasciato sospeso in background

wget  # Utility gratuita per il download non interattivo di file da Internet

whoami  # Mostra il nome dell'utente corrente

############################################################ PERMESSI ############################################################

chmod
    # Opzioni
    [+-=]r  # Aggiungere, togliere o assegnare il permesso di lettura  
    [+-=]x  # Aggiungere, togliere o assegnare il permesso di esecuzione
    [+-=]w  # Aggiungere, togliere o assegnare il permesso di scrittura
    u   # Modificare i permessi del proprietario
    g   # Modificare i permessi del gruppo
    o   # Modificare i permessi degli altri

    # Esempi
    chmod u+x <nomefile>   # Aggiunge il permesso di esecuzione al file solo per il proprietario
    chmod g+w <nomefile>   # Aggiunge il permesso di scrittura al file solo per il gruppo
    chmod a+x <nomefile>   #  Aggiunge il permesso di scrittura al file per tutti

    chmod u+x,g+x,o+x <nomefile>   # Aggiunge il permesso di esecuzione al file per il proprietario, il gruppo e gli altri.
    chmod u+x, u+w, u+r <nomefile>   # Aggiunge i permessi di esecuzione, scrittura e lettura al file solo per il proprietario

    chmod u=rw <nomefile>   # Imposta i permessi di lettura e scrittura per il file solo per il proprietario
    chmod u=rw,g=r file <nomefile>   # Imposta i permessi di lettura e scrittura per il proprietario e il gruppo, e il permesso di sola lettura per il gruppo
    
    chmod u-r <nomefile>   # Rimuove il permesso di lettura dal file solo per il proprietario
    chmod o-r <nomefile>   # Rimuove il permesso di lettura dal file solo per gli altri (non proprietario né gruppo)
    
    chmod 750 file <nomefile>   # Imposta i permessi di lettura, scrittura ed esecuzione per il proprietario, il permesso di lettura ed esecuzione per il gruppo, e nessun permesso per gli altri.
    



############################################################ SCRIPTING ############################################################


# Creare tre file chiamati file-1.txt, file-2.txt, file-3.txt usando il seguente comando shell (da impartire tutto su un rigo):

for F in {1..3}; do for N in {1..100}; do od -An -N1 -i /dev/urandom | tr -d " \t" >> file-$F.txt; done; done

#   -   for F in {1..3}; do ... done: Questo è un ciclo for che itera su tre valori (1, 2, 3). Ad ogni iterazione, il valore corrente viene assegnato alla variabile F.
#   -   for N in {1..100}; do ... done: Questo è un altro ciclo for annidato all’interno del primo ciclo.
#       Itera su 100 valori (da 1 a 100). Ad ogni iterazione, il valore corrente viene assegnato alla variabile N.
#   -   od -An -N1 -i /dev/urandom: Questo comando genera un numero intero casuale. od è un comando che legge i dati grezzi (in questo caso, da /dev/urandom) e li visualizza in un formato leggibile.
#           L’opzione -An dice a od di non visualizzare gli indirizzi di offset. L’opzione -N1 dice a od di leggere solo un byte di dati. L’opzione -i dice a od di visualizzare i dati come numeri interi.
#   -   /dev/urandom: È un dispositivo speciale in sistemi Unix-like che genera dati casuali.
#   -   tr -d " \t": Questo comando elimina tutti gli spazi e i tabulazioni dal suo input. tr è un comando che traduce o elimina caratteri. L’opzione -d dice a tr di eliminare i caratteri specificati.
#   -   >> file-$F.txt: Questo comando reindirizza l’output del comando precedente (il numero casuale generato) al file file-$F.txt.
#       Il doppio maggiore >> dice alla shell di appendere l’output al file invece di sovrascriverlo.
#       La variabile $F viene sostituita con il valore corrente del ciclo for esterno, quindi i nomi dei file saranno file-1.txt, file-2.txt, file-3.txt.


#------------File .sh---------------
    #!/bin/bash

    # Questo è un semplice script shell
    echo "Hello, World!"

#per eseguire lo script, sul terminale:
chmod +x hello.sh
./hello.sh