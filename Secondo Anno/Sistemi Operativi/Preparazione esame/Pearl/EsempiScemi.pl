#Hello World:

#!/usr/bin/perl
use strict; # dichiara che le variabili devono essere dichiarate prima di essere utilizzate
use warnings; # fornisce avvisi utili per la scrittura di codice sicuro

print "Hello, World!\n";




#Calcolo della somma di numeri da 1 a 10:

#!/usr/bin/perl
use strict;
use warnings;

my $sum = 0; # my dichiara una variabile locale
for my $i (1..10) {
    $sum += $i;
}
print "La somma dei numeri da 1 a 10 è: $sum\n";




#Lettura di input dall'utente:

#!/usr/bin/perl
use strict;
use warnings;

print "Inserisci il tuo nome: ";
my $nome = <STDIN>;
chomp($nome);
print "Ciao, $nome!\n";




#Manipolazione di stringhe:

#!/usr/bin/perl
use strict;
use warnings;

my $stringa = "Perl è un linguaggio potente";
print "Lunghezza: ", length($stringa), "\n";
print "Maiuscolo: ", uc($stringa), "\n"; # uc() converte in maiuscolo
print "Minuscolo: ", lc($stringa), "\n"; # lc() converte in minuscolo
print "Sostituito: ", $stringa =~ s/potente/versatile/r, "\n"; # sostituisce "potente" con "versatile"




#Lavorare con gli array:

#!/usr/bin/perl
use strict;
use warnings;

my @frutti = ("mela", "banana", "arancia");
push @frutti, "pera";
print "Frutti: @frutti\n"; # @frutti restituisce tutti gli elementi dell'array separati da spazi
print "Numero di frutti: ", scalar @frutti, "\n"; # scalar restituisce il numero di elementi nell'array
print "Ultimo frutto: ", pop @frutti, "\n"; # pop rimuove e restituisce l'ultimo elemento dell'array




#Utilizzo di hash (dizionari):

#!/usr/bin/perl
use strict;
use warnings;

my %età = (
    "Alice" => 25,
    "Bob" => 30,
    "Charlie" => 35
);

print "L'età di Bob è: $età{'Bob'}\n";
$età{"David"} = 40; # aggiunge un nuovo elemento all'hash
foreach my $nome (keys %età) {
    print "$nome ha $età{$nome} anni\n";
}




#Lettura di un file:

#!/usr/bin/perl
use strict;
use warnings;

my $filename = "esempio.txt";
open(my $fh, '<', $filename) or die "Non posso aprire '$filename' $!";
while (my $riga = <$fh>) { # <$fh> legge una riga alla volta
    chomp $riga;
    print "$riga\n"; # stampa su schermo
}
close $fh;




#Scrittura su un file:

#!/usr/bin/perl
use strict;
use warnings;

my $filename = "output.txt";
open(my $fh, '>', $filename) or die "Non posso aprire '$filename' $!";
print $fh "Questa è una riga nel file.\n"; # stampa nel file
print $fh "Questa è un'altra riga.\n";
close $fh;
print "File scritto con successo.\n";





#Utilizzo di espressioni regolari:

#!/usr/bin/perl
use strict;
use warnings;

my $testo = "Il mio indirizzo email è esempio@email.com";
if ($testo =~ /(\w+@\w+\.\w+)/) {
    print "Indirizzo email trovato: $1\n"; # $1 contiene il match
} else {
    print "Nessun indirizzo email trovato.\n";
}




#Funzioni personalizzate:

#!/usr/bin/perl
use strict;
use warnings;

sub saluta {
    my ($nome) = @_; # parametri della funzione; si mettono tra parentesi tonde per evitare ambiguità
    my ($altro) = @_; #è come fare my $altro = $_[1];
    return "Ciao, $nome! Ciao $altro!";
}

my $messaggio = saluta("Alice", "Bob");
print "$messaggio\n";