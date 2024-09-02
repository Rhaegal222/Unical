#! /usr/bin/perl

if( scalar @ARGV == 0){ # nessun options inserito
    # stampare in stdout l'elenco dei file .h
    # contenuti nella cartella /usr/include in ordine lessicografico
    @nomifile = qx(find /usr/include -maxdepth 1 -type f -name *.h -exec basename {} \\; | sort);    # leggere una sequenza
    for(@nomifile){
        print($_);
    }

=pod soluzione alternativa e più semplice con perl 
    @contenuto_cartella = qx(ls /usr/include);
    if(scalar @ARGV==0){
        foreach $fileInCartella (@contenuto_cartella){ 
            chomp $fileInCartella;
            if ($fileInCartella =~ /(.*).h/){
                push @elenco, $fileInCartella
            }
        }
        my @sorted_elenco = sort @elenco;
        print join("\n", @sorted_elenco);
    }
=cut
}
elsif(scalar @ARGV == 1){ # 1 options inserito

    # stampare su stdout i commenti contenuti nel file di testo 
    # testo racchiuso tra /* e */ eventualmente distribuito su più righe
    # ordinando la stampa in base alla lunghezza dei commenti dal più breve al più lungo
    # a parità di lunghezza ordine lessicografico

    $nomeFile = @ARGV[0]; # Elenco dei nomi dei file nella cartella /RICETTE
    print $nomefile;
    open($FH, "</usr/include/$nomeFile") or die "Impossibile aprire il file: '$nomeFile' !";
    $commentoAperto = 0;
    while(<$FH>){
        print $_;
        if( $_ =~ /\/\*(.*)\*\// ){
            print $1;
        }
        elsif($_ =~ /\/\*(.*)/){
            $commentoAperto = 1;
            print $1;
        }
        elsif($_ =~ /(.*)\*\//){
            $commentoAperto = 0;
            print $1;
        }
        elsif($commentoAperto==1){
            print $_;
        }
    }
    close($FH);
}
else{
    die "ATTENZIONE - Sintassi del comando errata!"
}