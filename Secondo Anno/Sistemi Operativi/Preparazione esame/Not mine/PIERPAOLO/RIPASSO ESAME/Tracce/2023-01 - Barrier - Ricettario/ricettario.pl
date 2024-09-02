#! /usr/bin/perl



if( scalar @ARGV == 0){
    die "Inserisci almeno un ingrediente da cercare";
}
else{
    @ricette = qx(ls ./RICETTE); # Elenco dei nomi dei file nella cartella /RICETTE

    foreach $ricetta (@ricette){
        chomp $ricetta; # Per ogni ricetta togli il \n

        $nome = uc $1 if $ricetta =~ /(.*).txt/; # prendi il nome della ricetta corrente tramite un gruppo di match e falla UpperCase

        open($FH, "<RICETTE/$nome.txt") or die "Impossibile aprire il file: '$nome' !";

        while(<$FH>){
            if(/Ingredienti/){  #compara con $_
                $ingredienti = 1;   # quando $ingredienti = 1 significa che nella lettura del file abbiamo superato quel rigo
                next;
            }
            if(/Preparazione/){ #compara con $_
                close($FH);
            }
            if($ingredienti){
                foreach $ingrediente(@ARGV){  # per ogni ingrediente ricevuto in input
                    chomp $ingrediente;
                    if(/$ingrediente/){ #cerca con una regex se l'ingrediente è presente
                        push @match, $ricetta; #salva in un vettore il nome della ricetta se c'è l'ingrediente che cercavamo
                        print(scalar @match." - $ricetta: $_");
                    }
                }
            }
        }
    }
    if(scalar @match == 0){
        print "Spiacente - Nessuna ricetta contiene questo ingrediente";
    }

    #mettersi in attesa della scelta

    while(<STDIN>){
        if(/END/){
            last; # Termina il while
        }
        if($_ < 0 || $_ > scalar @match){ # controlla se in range
            print ("Ricetta non in elenco, scegliere un valore tra 1 e ".scalar @match."\n");
            next; # Prossima iterazione del while
        }
        # Se è stato scelto un numero appropriato allora stampa
        # la ricetta associata a quel numero

        $nomeFile ="./RICETTE/$match[$_-1]";
        open($FH,"<$nomeFile");
        while(<$FH>){
            if(/Preparazione/){ # cerca preparazione e imposta un flag a 1
                $print =1;
                next;
            }
            if($print){ # stampa solo se il flag è stato impostato a 1, cioè se nella lettura si è superato il rigo "Preparazione"
                print $_;
            }
        }
        close($FH);
        print "\n";
        last;
    }
}