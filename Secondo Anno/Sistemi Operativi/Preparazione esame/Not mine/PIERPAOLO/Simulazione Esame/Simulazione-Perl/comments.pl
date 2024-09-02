#!/usr/bin/perl

if($#ARGV == -1){ # Controlla se l'array di argv è vuoto
    # qx esegue comandi shell
    print qx(ls -1 /usr/include | grep -P "\.h\$");
}
elsif($#ARGV == 0){

    $cont = 0; # numero del commento

    $file = shift @ARGV; # shift toglie il primo elemento dell'array e lo assegna alla variabile

    @file = qx(cat /usr/include/$file);

    for (@file){  # $_=~/regex/
        if(/\/\*(.*)/){ # ogni coppia di parentesi corrisponde ad un gruppo di catura
            if(/\/\*(.*)\*\//){ #commento iniziato e finito su una linea
                # si usa la @ per gli array e il $ se specifichi l'elemento dell'array
                $comments[$cont]=$1;
                $cont++;
                next; # next => continue    last => break
            }
            $comments[$cont]=$1;
            $inComm=1;
        }      
        elsif($inComm==1){
            if(/(.*)\*\//){
                $inComm=0;
                $comments[$cont].=$1;
                $cont++;
            }
            else{
                $comments[$cont].=$_;
            }
        }
    }

    # sort
    
    # se due elementi hanno la stessa lunghezza vanno ordinati in ordine lessicografico
    # quindi se il sort restituisce 0 facciamo un "OR compare" => 
    for(sort({length $a <=> length $b || $a cmp $b } @comments)){
        print $_."\n\n";
    }

}
else{
    die "Troppi parametri";
}




