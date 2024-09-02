# Esercizio 1

## 2023-04-28

### 0) Costruire il seguente albero di cartelle

```shell
pierpaolo@Patricio:~$ mkdir -p a/c a/b/e a/b/f
```

### 1) Scegliere 'a' come cartella corrente

```shell
pierpaolo@Patricio:~$ cd a
```

### 2) Creare nella cartella 'a' i file: (utilizzare il comando 'touch' dopo averne letto la documentazione)

1) file1.txt
2) file2.txt
3) file3.tmt
4) xfile.txt
5) doc1.doc
6) doc2.doc
7) doc3.doc
8) xdoc.doc

```shell
pierpaolo@Patricio:~/a$ touch ./a/file1.txt ./a/file2.txt ./a/file3.tmt ./a/xfile.txt ./a/doc1.doc ./a/doc2.doc ./a/doc3.doc ./a/xdoc.doc

```

### 3) Creare una copia di 'file1.txt' con nome 'copiafile1.txt' aoll'interno della cartella 'a'

```shell
pierpaolo@Patricio:~/a$ cp file1.txt copiafile1.txt
```

### 4) Copiare 'file1.txt' e 'copiafile1.txt' nella cartella 'b/e' utilizzando il path assoluto di 'e'

```shell
pierpaolo@Patricio:~/a$ cp file1.txt copiafile1.txt "/home/pierpaolo/a/b/e"
```

### 5) Rinominare la copia di file1.txt presente in 'e' usando il path relativo di 'file1.txt' partendo da 'a'. Il nuovo file dovrà chiamarsi 'rinominato.txt'

```shell
pierpaolo@Patricio:~/a$ mv b/e/file1.txt b/e/rinominato.txt
```

### 6) Spostare tutti i file in 'a' con estensione 'txt' in 'b'

```shell
pierpaolo@Patricio:~/a$ mv *.txt b
```

### 7) copiare tutti i file nella cartella 'a' che contengono la sottostringa 'doc' a partire dal secondo carattere, nella cartella 'c'. ad esempio devono essere copiati file con nome pdocumento.gif, xdocumento.txt, _doc, ecc

```shell
pierpaolo@Patricio:~/a$ cp ?doc*.* c
```

### 8) Spostare tutti i file nella cartella 'e' che iniziano per 'd' nella cartella 'f'

```shell
pierpaolo@Patricio:~/a$ mv b/e/d*.* b/f
```

### 9) Scaricare nella cartella 'a' la home page di 'google': (utilizzare il comando wget dopo averne letto la documentazione)

```shell
pierpaolo@Patricio:~/a$ wget www.google.com
```

---

## Modificare i diritti di accesso alle cartelle in modo che

### 10) Chiunque possa leggere e scrivere nella cartella 'a'

```shell
pierpaolo@Patricio:~/a$ chmod +rw .
```

### 11) Others non possa vedere il contenuto di 'c'

```shell
pierpaolo@Patricio:~/a$ chmod o-rwx c
```

### 12) Others possa entrare in 'f' ma non in 'e'

```shell
pierpaolo@Patricio:~/a$ chmod o+x b/f && chmod o-x b/e
```

### 13) Others abbia il diritto di lettura su b, mentre group abbia tutti i diritti

```shell
pierpaolo@Patricio:~/a$ chmod o+r b && chmod g+rwx b
```

### 14) Rimuovere la cartella 'f' con tutto il suo contenuto

```shell
pierpaolo@Patricio:~/a$ rm -r b/f
```
