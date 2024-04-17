
# [Sistemi Operativi e Reti](https://sites.google.com/unical.it/inf-sistemioperativi/home-page)

# Materiale del corso

## Introduzione al corso

* Introduzione ai Sistemi Operativi - [Download](https://docs.google.com/presentation/d/1Mjbm7aS5WvZO7ndk7FjtF96lb8q-_JtU)

## Gestione di processi e Thread

### Slide

* Lezione Gestione Processi - [Download](https://docs.google.com/presentation/d/1MjiQOZkOIz8guwp61Q2tsumB1UsoezFT)

### Lock e Condition

* Gioco delle N Sedie
  * [Testo](https://www.mat.unical.it/ianni/SOR-Web/esercitazioni/lock/es1-thread-GiocoSedie.pdf)
  * [Codice](https://www.mat.unical.it/ianni/SOR-Web/codice/lock/sedie/GiocoSedie.py) - **Soluzione** - Contiene un monitor/lock per ciascuna sedia e display semisincronizzato.
* Gatto & Topo
  * [Testo](https://www.mat.unical.it/ianni/SOR-Web/esercitazioni/lock/es2-thread-GattoTopo.pdf)
  * [Codice](https://www.mat.unical.it/ianni/SOR-Web/codice/lock/gatto_topo/basic/gattotopo.py) - **Soluzione basic** - La soluzione basic contiene solo un lock, ma nessuna stampa sincronizzata.
  * [Codice](https://www.mat.unical.it/ianni/SOR-Web/codice/lock/gatto_topo/basic/gattotopo_migliore.py) - **Soluzione advanced** - La soluzione "migliore" introduce una condition per sincronizzare il display.
  * [Codice](https://www.mat.unical.it/ianni/SOR-Web/codice/lock/gatto_topo/basic/gattotopo_inherit.py) - **Soluzione con Ereditarietà** - Questa soluzione integra la basic e la advanced precedenti sfruttando le proprietà dell'ereditarietà.
* Stampa disciplinata
  * [Testo](https://drive.google.com/file/d/1hj3x_p3dGzrCLHx8Faqf2VnBXBaZFtWw/view)
  * [Codice](https://www.mat.unical.it/ianni/SOR-Web/codice/lock/IlMioPrimoThreadGrezzo.py) - **Sorgente di partenza**
  * [Codice](https://www.mat.unical.it/ianni/SOR-Web/codice/lock/IlMioPrimoThread.py) - **Soluzione**

### Blocking Queue

* [Codice](https://www.mat.unical.it/ianni/SOR-Web/codice/blocking_queue/BlockingQueueSimple.py) - Esempio di semplice blocking queue
* [Codice](https://www.mat.unical.it/ianni/SOR-Web/codice/blocking_queue/blocking_queue.py) - Blocking queue implementata con il metodo del buffer circolare
* Pizzeria
  * [Testo](https://www.mat.unical.it/ianni/SOR-Web/esercitazioni/blocking_queue/Pizzeria.pdf)
  * [Codice](https://www.mat.unical.it/ianni/SOR-Web/codice/blocking_queue/pizzeria/Pizzeria.py) - **Soluzione**
* Studio Medico
  * [Testo](https://www.mat.unical.it/ianni/SOR-Web/esercitazioni/blocking_queue/StudioMedico.pdf)
  * [Soluzioni](https://www.mat.unical.it/ianni/SOR-Web/codice/blocking_queue/StudioMedico.zip)

### Deadlock

* Problema dei filosofi
  * [Codice](https://www.mat.unical.it/ianni/SOR-Web/codice/deadlock/filosofi/filosofi_deadlock.py) - Soluzione con deadlock
  * [Codice](https://www.mat.unical.it/ianni/SOR-Web/codice/deadlock/filosofi/filosofi.py) - Soluzione senza deadlock (risolto per ordinamento risorse)
  * [Codice](https://www.mat.unical.it/ianni/SOR-Web/codice/deadlock/filosofi/filosofi_inherit.py) - Entrambe le soluzioni in un unico file con due classi Filosofo una ereditata dall'altra
* Conto Bancario
  * [Testo](https://www.mat.unical.it/ianni/SOR-Web/esercitazioni/deadlock/ContoBancario.pdf)
  * [Codice](https://www.mat.unical.it/ianni/SOR-Web/codice/deadlock/conto_bancario/ContoBancarioTutto.py) - **Soluzione**

### Read/Write Lock

* Problema dei filosofi
  * [Codice](http://www.mat.unical.it/ianni/SOR-Web/codice/readwritelock/readwritelock.py) - Simulazione di un read/write lock con e senza gestione della starvation
* Ponte Mare-Monti
  * [Testo](https://www.mat.unical.it/ianni/SOR-Web/esercitazioni/altro/PonteMareMonti.pdf)
  * [Codice](https://www.mat.unical.it/ianni/SOR-Web/codice/altro/ponte_mare_monti/PonteMareMonti.py) - **Soluzione**
* Reparto Ospedaliero
  * [Testo](https://www.mat.unical.it/ianni/SOR-Web/esercitazioni/altro/Reparto.pdf)
  * [Codice](https://www.mat.unical.it/ianni/SOR-Web/codice/altro/reparto_ospedaliero/con_starvation/Stanza.py) - **Soluzione**

### Barriera

* Esercizio sui numeri primi
  * [Testo](https://www.mat.unical.it/ianni/SOR-Web/esercitazioni/barriera/NumeriPrimi.pdf)
  * [Codice](https://www.mat.unical.it/ianni/SOR-Web/codice/barriera/CyclicBarrier.py) - Soluzione con allocazione statica del carico e Barriera
  * [Codice](https://www.mat.unical.it/ianni/SOR-Web/codice/barriera/CyclicBarrierDinamico.py) - Soluzione con allocazione dinamica del carico
  * [Codice](https://www.mat.unical.it/ianni/SOR-Web/codice/barriera/CyclicBarrierProcess.py) - Soluzione in versione multiprocesso

## Shell programming, scripting, Perl

* Slides su comandi shell di base - [Download](https://www.mat.unical.it/ianni/SOR-Web/slides/lezioneSO-3-Shell.pptx)
* Imparare la shell (in inglese) - [Open](https://www.mat.unical.it/ianni/SOR-Web/slides/lezioneSO-3-Shell.pptx)
* Imparare la shell (in italiano, con spiegazione dei comandi più comuni) - [Open](https://www.mat.unical.it/informatica/SistemiOperativiEReti?action=AttachFile&do=view&target=shell_linux.pdf)
* ABC di bash, from Stanford University - [Open](http://www.compciv.org/bash-guide/)
* Rassegna dei comandi più utili, from Stanford University - [Open](http://www.compciv.org/unix-tools/)
* Esercitazione - [Testo](https://www.mat.unical.it/ianni/SOR-Web/esercitazioni/shell/EsercitazioneShell.docx)
* Perl - [Open](https://docs.google.com/presentation/d/1ZRYqar8vkFxQylDi-x70VMfy571zXYB6u79ly27nlds/edit?usp=sharing)
* Documentazione perl in italiano - [Open](https://pod2it.sourceforge.net/pods/perlfunc.html)
* Esercitarsi sulle regex - [Open](http://regex101.com/)
* Esercitazione Perl-Shell - [Testo](https://www.mat.unical.it/ianni/SOR-Web/esercitazioni/shell/EsercitazionePerlShell.docx)
* Gli array associativi in Perl - [Codice](https://www.mat.unical.it/ianni/SOR-Web/codice/altro/perl/esempiArrayAssociativi.pl)
* Esercitazione Perl-Shell (tipo esame) - [Testo](https://www.mat.unical.it/ianni/SOR-Web/esercitazioni/shell/EsercitazioneDiskUsage.docx) - [Soluzione](https://www.mat.unical.it/ianni/SOR-Web/codice/altro/perl/checkExtensions.zip)

## Gestione memorie di massa

* [Download](https://docs.google.com/presentation/d/1s1bV3jMiZHF1gvOplSdR2A3z6GVVHnQr)

## Gestione memoria RAM

* [Download](https://docs.google.com/presentation/d/1tIphj1INazIdbY49Xk82yVoY9hRFZVwh)

### Other Links

* [queue — A synchronized queue class](https://docs.python.org/3/library/queue.html)
