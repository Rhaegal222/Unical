#! /usr/bin/perl

# runnare nella stessa directory di bash_history o cambiare il path

$nomeFile ="../.bash_history";
open($FH, '<', $nomeFile) or die "Impossibile aprire il file: '$nomeFile' !";


if( (scalar @ARGV == 2) && ($ARGV[1] =~ /\d+/) ){

    $NumRighe = $ARGV[1];

    qx(cat $nomeFile | tail -$NumRighe > last_calls.txt);


}
elsif( scalar @ARGV == 0){

    # DA FARE
    while($line = <$FH>){   # Leggi ogni linea da FileHandler
        chomp $line;        # Togli i \n da ogni linea letta
        @splitted = split(' ', $line);  # separa $line per spazi mettendo ogni elemento separato in @splitted
        push @comandi, $splitted[0]; # inserisci in fondo all'array @comandi il primo comando nell'array @splitted
    }

    %contati;   # hashmap

    for(@comandi){  #itera su @comandi ogni variabile va in $_ | equivale a: for $_ in (@comandi)
        $contati{$_}++; # crea automaticamente le voci che non esistono e le aggiunge
                        # una dizionario che conta quante volte è stata inserita una parola
    }



    @nomiComandiOrdinatiDecrescente = sort { $contati{$b} <=> $contati{$a} || $b cmp $a} keys %contati;
    # creiamo un nuovo vettore a cui associamo solo i valori delle chiavi (nomi dei comandi)

    $comandoPiuUsato = $contati{@nomiComandiOrdinatiDecrescente[0]};    # cerca nell'hashmap il valore della chiave fornita
                                                                        # il primo elemento dell'array sarà quello usato più volte
                                                                        # quindi restituirà il numero più grande

    $comandoMenoUsato = $contati{@nomiComandiOrdinatiDecrescente[$#nomiComandiOrdinatiDecrescente]};   # viceversa

    for $comando(@nomiComandiOrdinatiDecrescente) # per ogni comando in questo array
    {
        if($contati{$comando} == $comandoPiuUsato){
            print "$comando - $contati{$comando}\n"; # stampiamo il / i comando/i più usati
        }
    }

    for $comando(@nomiComandiOrdinatiDecrescente) # per ogni comando in questo array
    {
        if($contati{$comando} == $comandoMenoUsato){
            print "$comando - $contati{$comando}\n"; # stampiamo il / i comando/i più usati
        }
    }


}
elsif(scalar @ARGV == 1 && ($ARGV[0] =~ /^-n$/)){
    die "Specifica un value dopo n";
}
else{
    die "Comando formato incorrettamente";
}


print("\n");