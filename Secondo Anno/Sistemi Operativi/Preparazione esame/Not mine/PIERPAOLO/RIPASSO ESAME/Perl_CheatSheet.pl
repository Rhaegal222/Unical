=pod 
    Shebang è un meccanismo utilizzato dai sistemi operativi 
    basati su Unix (come Linux e macOS) 
    per determinare quale interprete di comandi utilizzare 
    per eseguire uno script
=cut

#! /usr/bin/perl


# variabili scalari (numeri, stringhe, booleani)
$var;    

# array
@array;     # un singolo elemento di un array è uno scalare ( $array[0] )

# dizionari/hashmap
%hashmap;   


################################################### ESEMPI DI SCALARI ###################################################

$var = 2314;

$str='ciao $var';   # '' scrivono esatamente i caratteri al loro interno
                    # "" interpretano il valore delle variabili al loro interno
$str="ciao $var";
$str='ciao'.$var;


################################################### ESEMPI DI VETTORI ###################################################

@numeri = (1, 2, 3, 4, 5);

@frutta = ();  # Array vuoto
push @frutta, "mela", "banana", "arancia";

# array di 10 elementi uguali ad 1
@array=(1)x10;

# array con 1 elemento uguale a 1111111111
@array=1x10; 
# 1111111111

# separa gli elementi dell'array con " "
print join " ", @array; 
# 1 1 1 1 1 1 1 1 1 1


# numero degli elementi di array
print @array."\n";      
# 10


# primo elemento di un array (@ se si tratta di una matrice)
print $array[0];   
# 1


# indice dell'ultimo elemento
print $#array;       
# 9

# lunghezza dell'array
print scalar @array
# 10

#1)
print "Prima \n";
for ($i=0; $i<=$#array; $i++){
    print "$array[$i] ";
}
=pod
Prima 
1 1 1 1 1 1 1 1 1 1 
=cut

#2) Push aggiunge in posizione len-1 dell'array
print "Dopo Push \n";
push @array, 45;
for ($i=0; $i<=$#array; $i++){
    print "$array[$i] ";
}
=pod
Dopo Push 
1 1 1 1 1 1 1 1 1 1 45 
=cut


#3) Unshift aggiunge in posizione 0 dell'array
print "Dopo Unshift\n";
unshift @array, 66;
for ($i=0; $i<=$#array; $i++){
    print "$array[$i] ";
}
=pod
Dopo Unshift
66 1 1 1 1 1 1 1 1 1 1 
=cut

#4) Pop rimuove/restituisce l'ultimo elemento dell'array
print "Dopo Pop\n";
pop  @array;
for ($i=0; $i<=$#array; $i++){
    print "$array[$i] ";
}
=pod
Dopo Pop
1 1 1 1 1 1 1 1 1 
=cut


#5) Shift rimuove/restituisce il primo elemento dell'array
print "Dopo Shift\n";
shift  @array;
for ($i=0; $i<=$#array; $i++){
    print "$array[$i] ";
}
=pod
Dopo Shift
1 1 1 1 1 1 1 1 1 
=cut


#6)
print "Array 2 \n";
@indici=(2,6,7);
@array2 = @array[@indici];
for ($i=0; $i<=$#array2; $i++){
    print "$array2[$i] ";
}
=pod
Array 2 
1 1 1 
=cut


#####################################################################################################################################

#ARGC
$_     

#ARGV  
@_     


#    $#ARGV rappresenta l'indice dell'ultimo elemento dell'array @ARGV. Ecco alcuni esempi:

#  1.  Se lanciato come myscript.pl first_argument:

#    $#ARGV sarà 0 (l'indice dell'unico argomento)
#    @ARGV avrà un elemento


#  2.  Se lanciato con due argomenti myscript.pl arg1 arg2:

#    $#ARGV sarà 1 (l'indice del secondo argomento)
#    @ARGV avrà due elementi


#  3.  Se lanciato senza argomenti myscript.pl:

#    $#ARGV sarà -1 (indicando un array vuoto)
#    @ARGV sarà vuoto

################################################### Stampare - Scorrere un Array ###################################################

for @array{
    #ogni valore di array viene messo in $_ ad ogni iterazione
}

for $var @array{
    #ogni valore di array viene messo in $var ad ogni iterazione
}

#Altri esempi con vettori
@str_a=("ciao","ciccio","pachiderma");


for($i=0; $i< scalar @str_a; $i++){
    print(@str_a[$i]);
    print("\n");
}
=pod

ciao

ciccio

pachiderma

=cut


for(@str_a){
    print "\n";
    print split "c";
    print "\n";
}
=pod

iao

iio

pahiderma

=cut


@s = split("_","c_i_a_o_");

print join ' ', @s;

=pod
c i a o
=cut

=pod
Per confrontare gli scalari numerici
Possiamo utilizzare i classici operatori di confronto

<, >, =, <=, >=, <=>


Per confrontare le stringhe invece dobbiamo utilizzare altri operatori
=cut

eq  #   equal
gt  #   greater than    
lt  #   lower than
ge  #   greater or equal
le  #   less or equal


################################################### OPERATORI BOOLEANI ###################################################

&&      #   (più efficiente di and)
||      #   (più efficiente di or)
!
and     #   valuta ugualmente entrambe le condizioni anche se la prima è falsa
or      #   valuta ugualmente entrambe le condizioni anche se la prima è vera


################################################### ESEMPI DI CONFRONTO ###################################################

$str1="aabb";
$str2="aaaa";

if($str1 ge $str2 ){ # se aabb è più grande di aaaa stampa "aabb"
    print $str1;
}

=pod
aabb
=cut



################################################### ESPRESSIONI REGOLARI - REGEX ###################################################

=~ # restituisce un valore booleano


# cerca la stringa "ia" in $str1 e restituisce un valore booleano se il match è soddisfatto
$str1 =~ /ia/;           

# controlla se la stringa comincia per a
$str1 =~ /^a/;              

# controlla se la stringa finisce per a
$str1 =~ /a$/;              

# controlla se la stringa contiene una lettera maiuscola o minuscola seguita da zero o più caratteri
$str1 =~ /^[a-zA-Z](.*)/;   

# controlla se la stringa contiene una lettera minuscola, una maiuscola seguite da 1 o più caratteri
$str1 =~ /[a-z][A-Z](.+)/;  

# I GRUPPI DI MATCH SONO SOLTANTO QUELLI RACCHIUSI TRA ()
# il resto viene usato solo a scopo di ricerca, ma successivamente ignorato

#------------------------------Esempi------------------------------
    # $1...$9 conterranno i gruppi di match
    $str = "Chiama 123-456-7890 o 987-654-3210";
    while ($str =~ /(\d{3})-(\d{3})-(\d{4})/g) {
        print "Numero trovato: $1-$2-$3\n";
    }

    # w = [a-zA-Z0-9_] quindi qualunque carattere alfanumerico o underscore
    $text = "Contattaci a info@example.com o support@company.org";
    while ($text =~ /(\w+@\w+\.\w+)/g) {
        print "Email trovata: $1\n";
    }

    #uso di + come quantificatore
    $str = "abbbbccccddddeeee";
    if ($str =~ /a(b+)(c+)(d+)(e+)/) {
        print "b ripetuto $1 volte\n";
        print "c ripetuto $2 volte\n";
        print "d ripetuto $3 volte\n";
        print "e ripetuto $4 volte\n";
    }

    #Uso di (?:) per non catturare; la parte centrale non viene catturata
    $str = "123-45-6789";
    if ($str =~ /(\d{3})-(?:\d{2})-(\d{4})/) {
    print "Prima parte: $1, Ultima parte: $2\n";
    }

    #uso di \s che matcha con uno spazio (anche tabulazione). \s+ matcha con uno o più spazi. Con la s davanti la regex si sostiutisce in modo globale
    $str = "Questa è una  frase  con  spazi  multipli";
    $str =~ s/\s+/ /g; #sostituisce uno o più spazi con uno spazio
    print "$str\n";  # Stampa: "Questa è una frase con spazi multipli"

#   Cerca la stringa "ia" in $str1 e restituisce un valore booleano se il match è soddisfatto
$str1 =~ /$str2/;           

# ES 1)
$str1 = "baab";
$str2 = "aa";
if ($str1 =~ /$str2/) {
print "Corrispondenza trovata\n";
} else {
print "Nessuna corrispondenza trovata\n";
}

=pod
Corrispondenza trovata
=cut



#   Controlla se la stringa comincia per a
$str1 =~ /^a/;              

# ES 2)
$str1 = "baab";
if ($str1 =~ /^a/) {
print "Corrispondenza trovata\n";
} else {
print "Nessuna corrispondenza trovata\n";
}

=pod
Nessuna corrispondenza trovata
=cut



#   Controlla se la stringa finisce per b
$str1 =~ /a$/;   

# ES 2)
$str1 = "baab";
if ($str1 =~ /b$/) {
print "Corrispondenza trovata\n";
} else {
print "Nessuna corrispondenza trovata\n";
}

=pod
Corrispondenza trovata
=cut


# ES 3)
# Controlla se la stringa contiene una lettera maiuscola o minuscola seguita da zero o più caratteri
$str1 =~ /^[a-zA-Z](.*)/;   


# Controlla se la stringa contiene una lettera minuscola, una maiuscola seguite da 1 o più caratteri
$str1 =~ /[a-z][A-Z](.+)/;  

# ES 4)
$str1 ="127.0.0.1";
$str1 =~ /^(\d+)\.(\d+)\.(\d+)\.(\d+)$/;#$1...$9 conterranno i gruppi di match
print ("$1-$2-$3-$4\n");

=pod
127-0-0-1
=cut



# ES 5)
# Itera su ogni elemento dell’array @- che contiene le posizioni iniziali di ogni gruppo di cattura
for ($i=0; $i<=$#-; $i++){ # $#- restituisce l'indice dell'ultimo gruppo di cattura.
    print($-[$i]."\n");
}
=pod
0
0
4
6
=cut
=pod
$-[$0] = 0   # Posizione iniziale dell'intero match
$-[$1] = 0   # Posizione iniziale del primo gruppo di cattura (127)
$-[$2] = 4   # Posizione iniziale del secondo gruppo di cattura (0)
$-[$3] = 6   # Posizione iniziale del terzo gruppo di cattura (0)
$-[$4] = 8   # Posizione iniziale del quarto gruppo di cattura (1)
=cut

 #$& contiene l’intera stringa che corrisponde all’ultima espressione regolare di successo.
 #In altre parole, se hai un’espressione regolare che fa match con una parte di una stringa,
 #$& conterrà la parte della stringa che corrisponde all’espressione regolare

################################################### USO DI PERL TRAMITE SHELL ###################################################

# per usare Perl all'interno di un comando shell è sufficiente digitare

perl -ne 'comando'

=pod
L'argomento -n crea un ciclo che legge l'input riga per riga. 
Legge automaticamente ogni riga di input e vi applica il codice specificato.

L'argomento -e consente di fornire il codice Perl direttamente sulla riga di comando. 
Il codice specificato dopo il flag -e viene applicato a ogni riga di input.
=cut


#ESEMPIO 1)
#   Scrivere una linea di comando che elenchi le risorse presenti in una certa cartella
#   mostrandone esclusivamente il nome e la dimensione (usare perl oppure cut + column)

pierpaolo@Mauricio:~$ ls -lh | grep -v "$(ls -l | head -n 1 | cut -f 1)" | perl -ne '@a
= split(/\s+/); print ($a[4]." - ".$a[8]."\n");'

# il comando all’interno delle parentesi $(...) viene eseguito prima e il suo output
# viene utilizzato come parte del comando esterno.

#ESEMPIO 2)
#   Scrivere una linea di comando che calcoli la somma delle dimensioni di 
#   tutti i file di una certa cartella

pierpaolo@Mauricio:~$ ls -l | grep -v "$(ls -l | head -n 1 | cut -f 1)" | perl -ne '@a
= split(/\s+/); $sum += $a[4]; END {print $sum."\n"}'


#ESEMPIO 3)
#    Scrivi una linea di comando, o uno script, che esamini l’output del comando ‘ifconfig’ e
#   stampi tutte le stringhe espresse nel tipico formato di un MAC address. MAC Address di
#   esempio: FF:00:15:5D:02:EC (sei byte espressi in esadecimale separati dai due punti). In
#   assenza del comando ‘ifconfig’, usare ‘ip link

pierpaolo@Mauricio:~$ ip link | perl -ne ' $_ =~ /(([a-fA-F]|\d){2}:){5}([a-fA-F]|\d)
{2}/; print "$&\n" '


#ESEMPIO 4)
#   Scrivi una linea di comando che utilizzi l’output del comando ‘file’ per determinare il tipo
#   di file più frequente nella cartella /usr/bin (ingredienti: file; perl; sort; uniq; tail);

pierpaolo@Mauricio:~$ find /usr/bin -type f -exec file {} \; | perl -ne '@a =
split(/:/); print $a[1]; '| sort | uniq -c | sort -n | tail -n 1 

#ESEMPIO 5)
#   Elencare i comandi presenti nell’output del comando ‘history’ ma non presenti nel file
#   $HOME/.bash_history e salvarli in un file.


pierpaolo@Mauricio:~$ history | perl -ne '@a = split(/\s+/); print $a[2]."\n";' && cat
$HOME/.bash_history | sort | uniq -d > file.tx


#!/bin/bash

# File di output
output_file="$HOME/unique_history_commands.txt"

# Estrai l'output del comando history in un file temporaneo
history | cut -d ' ' -f 4- > /tmp/current_history.txt

# Rimuovi duplicati e ordina i comandi del file history
sort /tmp/current_history.txt | uniq > /tmp/sorted_current_history.txt

# Rimuovi duplicati e ordina i comandi del file .bash_history
sort "$HOME/.bash_history" | uniq > /tmp/sorted_bash_history.txt

# Trova i comandi presenti in sorted_current_history.txt ma non in sorted_bash_history.txt
grep -Fxv -f /tmp/sorted_bash_history.txt /tmp/sorted_current_history.txt > "$output_file"

# Rimuovi i file temporanei
rm /tmp/current_history.txt /tmp/sorted_current_history.txt /tmp/sorted_bash_history.txt

echo "I comandi unici sono stati salvati in $output_file"

################################################### Ordinare con la funzione sort ###################################################


# sort consente di specificare una routine esplicita di ordinamento: 

sort {$a cmp $b} 	#  ordinamento lessicografico
sort {$b cmp $a} 	#  come prima ma in ordine inverso
sort {$a <=> $b} 	#  ordinamento numerico ascendente
sort {$b <=> $a} 	#  ordinamento numerico discendente


#Stampa un vettore in modo ordinato
for(sort{$a cmp $b}@nomeVettore){

}


################################################### Array Associativi - 1 - Hashmap ###################################################

%nomicompleti = (                                  
    "Camus"      => "Albert",
    "Einstein"   => "Albert",
    "Smith"      => "Renee",
    "Baudelaire" => "Charles",
    "Pierre"     => "Robes",      
    "Sartre"     => "Jean-Paul"
);      


print "\n*** Stampa ***\n";
for $cognome (keys %nomicompleti)            
{                                                 
    print "$nomicompleti{$cognome} $cognome\n";
}

=pod

*** Stampa ***
Albert Camus
Albert Einstein
Jean-Paul Sartre
Charles Baudelaire
Robes Pierre

=cut


print "\n*** Stampa ordinata per chiave (cognome) ***\n";
foreach $cognome  (sort keys %nomicompleti)             
{                                                       
    print "$nomicompleti{$cognome} $cognome\n";
}

=pod

*** Stampa ordinata per chiave (cognome) ***
Charles Baudelaire
Albert Camus
Albert Einstein
Robes Pierre
Jean-Paul Sartre

=cut






print "\n*** Stampa ordinata per chiave (cognome) ascendente ***\n";
foreach $cognome (sort { $a cmp $b } keys %nomicompleti)             
{                                                                    
    print "$nomicompleti{$cognome} $cognome\n";
}

=pod

*** Stampa ordinata per chiave (cognome) ascendente ***
Charles Baudelaire
Albert Camus
Albert Einstein
Robes Pierre
Jean-Paul Sartre


=cut


 print "\n*** Stampa ordinata per chiave (cognome) discendente ***\n";
 foreach $cognome (sort { $b cmp $a } keys %nomicompleti)             
 {                                                                    
   print "$nomicompleti{$cognome} $cognome\n";
 }

=pod

*** Stampa ordinata per chiave (cognome) discendente ***
Jean-Paul Sartre
Robes Pierre
Albert Einstein
Albert Camus
Charles Baudelaire

=cut


print "\n*** Stampa ordinata in base al valore (nome) in corrispondenza della chiave ***\n";
foreach $cognome (sort { $nomicompleti{$a} cmp $nomicompleti{$b} } keys %nomicompleti)
{
    print "$nomicompleti{$cognome} $cognome\n";
}

=pod

*** Stampa ordinata in base al valore (nome) in corrispondenza della chiave ***
Albert Camus
Albert Einstein
Charles Baudelaire
Jean-Paul Sartre
Robes Pierre


=cut



print "\n*** Stampa ordinata in base al valore (nome) e a parità di valore in base alla chiave (cognome) ***\n";
foreach $cognome (sort { $nomicompleti{$a} cmp $nomicompleti{$b} || $a cmp $b} keys %nomicompleti)
{
    print "$nomicompleti{$cognome} $cognome\n";
}

=pod

*** Stampa ordinata in base al valore (nome) e a parità di valore in base alla chiave (cognome) ***
Albert Camus
Albert Einstein
Charles Baudelaire
Jean-Paul Sartre
Robes Pierre


=cut



#Array Associativi - 2 - Hashmap


%studenti = (
    "ale"  => 10567,
    "cla"  => 1789,
    "adri" => 6443,
    "mary" => 9890
);

=pod
Sebbene meno leggibile, gli array associativi
possono essere definiti anche come segue:

%studenti = ("ale", 10567, "cla", 1789, "adri", 6443, "mary",9890);
=cut


 print "\n*** Stampa ***\n";
 foreach $nome  (keys %studenti)
 {
   print "$nome - $studenti{$nome}.\n";
 }

=pod

*** Stampa ***
adri - 6443.
cla - 1789.
ale - 10567.
mary - 9890.

=cut



 print "\n*** Stampa ordinata in base alla chiave (nome) ***\n";
 foreach $nome  (sort keys %studenti)
 {
   print "$nome - $studenti{$nome}.\n";
 }

=pod

*** Stampa ordinata in base alla chiave (nome) ***
adri - 6443.
ale - 10567.
cla - 1789.
mary - 9890.

=cut
print "\n*** Stampa ordinata in base al valore (matricola), ascendente ***\n";
 foreach $nome  (sort { $studenti{$a} <=> $studenti{$b} } keys %studenti)
 {
   print "$nome - $studenti{$nome}.\n";
 }

=pod

*** Stampa ordinata in base al valore (matricola), ascendente ***
cla - 1789.
adri - 6443.
mary - 9890.
ale - 10567.

=cut



 print "\n*** Stampa ordinata in base al valore (matricola), discendente ***\n";
 foreach $nome  (sort { $studenti{$b} <=> $studenti{$a} } keys %studenti)
 {
   print "$nome - $studenti{$nome}.\n";
 }

=pod

*** Stampa ordinata in base al valore (matricola), discendente ***
ale - 10567.
mary - 9890.
adri - 6443.
cla - 1789.

=cut




################################################### APRIRE FILE PERL ###################################################
open($FH, '<', 'c:\temp\test.txt');
open($FH, '<', 'c:\temp\test.txt') or die $!; # se non riesce ad aprire il file, stampa l'errore

# < lettura
# > scrittura
# >> append

# CHIUDERE FILE PERL
close($FH);






################################################### BONUS - PRETEST ###################################################

# Leggere il contenuto della cartella ./francesco
@lista_file = qx(find ./francesco);


# Scorre e stampa la lista ordinata lessicograficamente
for(sort @lista_file){
    print($_);
}

@var = ("francesco", "giovambattista", "denise");
# Stampare il valore dell'oggetto var su file
 # Apri il file in scrittura

open($fh, ">", "nomefile.txt");

# Scorri l'array
for $valore(@var){
    # Stampa sul file precedente ogni elemento di @var
    print $fh "$valore";
} # Chiudi il file

close($fh);



#Stampare qualcosa su file
$a = "valore";

qx(echo $a > file.txt); # aggiunge - >> per appendere


# Leggere una variabile da input - Esempio
my $input = <STDIN>;

chomp($input); # Rimuove il carattere di nuova linea

print "Hai inserito: $input\n";

#è possibile accedere a “pezzi” di array: @array[1,3], @array[1..5], @array[@indici]




# Next passa alla successiva iterazione del ciclo
# Last esce dal ciclo

# Esempio
for (1..10){
    if($_ == 5){ # Se $_ è uguale a 5
        next; # Passa alla successiva iterazione
    }
    print "$_\n"; # stampa tutti i numeri da 1 a 10 tranne 5
}

# Esempio
for (1..10){
    if($_ == 5){ # Se $_ è uguale a 5
        last; # Esce dal ciclo
    }
    print "$_\n"; # stampa tutti i numeri da 1 a 4
}

#------------File .pl------------
# Esempio
    #!/usr/bin/perl

    # Questo è un semplice script Perl
    print "Hello, World!\n";

# Eseguire lo script da terminale:
chmod +x hello.pl
./hello.pl

#se voglio fare uno script perl che però esegue comandi shell usando qx
#------------File .pl------------
    #!/usr/bin/perl

    # Questo è un semplice script Perl
    print qx(ls -l);

    #oppure

    $output = qx(
        echo "Hello, World!"
        echo "This is a Perl script"
    );

    print $output;
    