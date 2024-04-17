#! /usr/bin/perl
if(@ARGV==0){
    die "E' necessario specificare almeno un ingrediente";
}
#NON USATE PER NESSUN MOTIVO AL MONDO PATH ASSOLUTI! Se uno script deve girare su un computer diverso dal vostro, come pensate possa farlo se ci sono path dipendenti dal vostro PC?
@ricette = qx(ls RICETTE);

foreach my $ricetta (@ricette){ 
    #TUTTO quello che viene da input è bene venga chompato! Le vostre regex o uguaglianze falliranno miseramente se non lo fate
    chomp $ricetta;
    $nome = uc $1 if $ricetta =~ "(.*)\.txt"; 
    #RICORDATE di controllare sempre che l'apertura di un file non vada in errore; è il classico esempio che vi fa perdere un casino di tempo per capire come mai lo script non funziona. Muore silenziosamente!
    open(FH,"<RICETTE/$ricetta") || die "Impossibile aprire il file RICETTE/$ricetta";
    while (<FH>){
        if(/Ingredienti/){
            $ingredienti=1;
            next;
        }
        if(/Preparazione/){
            close(FH);
        }
        if($ingredienti){
            foreach $ingrediente (@ARGV){
                chomp $ingrediente;
                if(/$ingrediente/){
                    #salvo la ricetta per poterla ritrovare facilmente se scelta poi dall'utente
                    push @match,$ricetta;
                    #uso la size dell'array (scalar @match) per sapere quante ricette ho già stampato
                    print scalar @match."- $nome: $_";
                    close(FH);
                }
            }
        }
    }
}
if(@match==0){
    print "Spiacente, nessuna ricetta contiene questo ingrediente.\n";
}
#Mi metto in attesa della scelta, sto in loop per gestire eventuali errori
while(<STDIN>){
    if(/END/){
        last;
    }
    if($_<=0 || $_ >@match){
        print "Ricetta non in elenco, scegliere un valore tra 1 e ".scalar @match."\n";
        next;
    }
    #C'è corrispondenza uno a uno tra l'indice stampato e l'indice dell'array in cui è stato inserito il nome della ricetta. Ovviamente, il primo indice dell'array è 0 e non 1.
    open(FH,"<RICETTE/$match[$_-1]");
    while(<FH>){
        if(/Preparazione/){
            $print=1;
            next;
        }
        if($print){
            print $_;
        }
    }
    close(FH);
    print "\n";
    last;
}
