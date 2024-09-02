# Esercitazione 0

## 2023-04-24

### 1) Determinare il numero di files nella directory /bin la cui prima lettera è "c"

```shell
pierpaolo@Patricio:~$ find /bin -name "c*" | wc -l
```

### 2) creare un file contenente i nomi dei primi 7 files della directory /etc

```shell
pierpaolo@Patricio:~$ ls /etc | head -7 > file.txt
```

### 3) Determinare il numero di files della current directory nel cui nome compare la stringa "string"

```shell
pierpaolo@Patricio:~$ ls | grep "string" | wc -l
```

### 4) creare un file contenente una lista col nome di 10 comandi di /bin ordinati secondo il momento dell'ultimo accesso

```shell
pierpaolo@Patricio:~$ ls -l -u /bin/ | head -10 > file.txt
```

### 5) Creare un file contenente i nomi dei primi 7 files e gli ultimi 6 files (in ordine alfabetico) della directory /etc

```shell
pierpaolo@Patricio:~$ ls /etc/ | head -7 > file.txt && ls /etc/ | tail -6 >> file.txt
```

### 6) Creare un file contenente una lista coi nomi di 8 files in /usr/sbin ordinati secondo il momento dell'ultima modifica

```shell
pierpaolo@Patricio:~$ ls -l -t /usr/sbin | head -8 > file.txt
```
