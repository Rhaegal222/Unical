# Esercitazione 2

## 2023-05-08

### 1) Scrivere una linea di comando che esamini il contenuto del file /proc/cpuinfo e restituisca il numero di CPU presenti nel calcolatore

```shell
pierpaolo@Patricio:~$ cat /proc/cpuinfo | grep "processor" | wc -l
```

### 2) Scrivere una linea di comando che mostri i primi 5 processi che utilizzano più memoria RAM

```shell
pierpaolo@Patricio:~$ ps -eo pid,cmd,%mem --sort -%mem| head -6 
```

oppure

```shell
pierpaolo@Patricio:~$ ps -eo pid,%mem | sort -k2 -r | head -6
```

### 3) Scrivere una linea di comando che elenchi i soli file di una certa cartella la cui dimensione è nell’ordine dei Gigabyte (consultare la documentazione di ls oppure usare il comando find)

```shell
pierpaolo@Patricio:~$ find -size +1G
```

### 4) Scrivere una linea di comando che elenchi le risorse presenti in una certa cartella mostrandone esclusivamente il n­ome e la dimensione (usare perl oppure cut + column)

```shell
pierpaolo@Patricio:~$ ls -lh | grep -v "$(ls -l | head -n 1 | cut -f 1)" | perl -ne '@a = split(/\s+/); print ($a[4]." - ".$a[8]."\n");'
```

### 5) Scrivere una linea di comando che calcoli la somma delle dimensioni di tutti i file di una certa cartella

```shell
pierpaolo@Patricio:~$ ls -l | grep -v "$(ls -l | head -n 1 | cut -f 1)" | perl -ne '@a = split(/\s+/); $sum += $a[4]; END {print $sum."\n"}'
```

### 6)  Scrivere una linea di comando che elenchi tutti i file con estensione ".log" più vecchi di 30 giorni in una certa cartella (si può usare /var/log per le prove)

```shell
pierpaolo@Patricio:~$ find /var/log -name "*.log" -mtime +30 | grep ".*" | less
```

### 7)  Scrivere una linea di comando che visualizzi il contenuto del file /proc/meminfo e converte i valori da kB in mB

```shell
pierpaolo@Patricio:~$ cat /proc/meminfo | awk '{print $1 ": " $2/1024 " MB" };'
```

### 8) Scrivere una linea di comando che trovi tutti i file con estensione ".txt" in una cartella e nelle sue sottocartelle e li copi in una cartella chiamata "backup"

```shell
pierpaolo@Patricio:~$ find -type f -name "*.txt" -exec cp {} ./backup/ \;
```

oppure

```shell
pierpaolo@Patricio:~$ find -type f -name "*.txt" | perl -ne 'chomp($_); qx{cp $_ ./backup/}'
```

### 9) Scrivere una linea di comando che visualizzi il contenuto del file /proc/uptime e converta i secondi di uptime in minuti e secondi

```shell
pierpaolo@Patricio:~$ cat /proc/uptime | awk '{print $1/60 " " $2/60};
```

### 10) Scrivi una linea di comando, o uno script, che esamini l’output del comando ‘ifconfig’ e stampi tutte le stringhe espresse nel tipico formato di un MAC address. MAC Address di esempio: FF:00:15:5D:02:EC (sei byte espressi in esadecimale separati dai due punti). In assenza del comando ‘ifconfig’, usare ‘ip link’

```shell
pierpaolo@Patricio:~$ ip link | perl -ne ' $_ =~ /(([a-fA-F]|\d){2}:){5}([a-fA-F]|\d){2}/; print "$&\n" '
```

### 11) Scrivi una linea di comando che utilizzi l’output del comando ‘file’ per determinare il tipo di file più frequente nella cartella /usr/bin (ingredienti: file; perl; sort; uniq; tail)

```shell
pierpaolo@Patricio:~$ find /usr/bin -type f -exec file {} \; | perl -ne '@a = split(/:/); print  $a[1]; '| sort | uniq -c | sort -n | tail -n 1
```

### 12) Elencare i comandi presenti nell’output del comando ‘history’ ma non presenti nel file $HOME/.bash_history e salvarli in un file

```shell
pierpaolo@Patricio:~$ history | perl -ne '@a = split(/\s+/); print $a[2]."\n";' && cat $HOME/.bash_history | sort | uniq -d > file.txt
```
