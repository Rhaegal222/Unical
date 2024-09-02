#! /usr/bin/perl

#Cotrollo che ci siano TUTTI e SOLI i parametri previsti
$op = shift @ARGV || die "manca parametro obbligatorio";
if(!($op =~ /^(-n|-o)$/)){
    die "Opzioni consentite -n | -o";
}

$comm = shift @ARGV || die "manca parametro obbligatorio"; 

if($ARGV >0 ){
    die "Troppe opzioni";
}
#Potrei usare --help ma con man è più semplice gestire le descrizioni: sono tutte su un'unica riga, non ci sono \n di mezzo
@doc = qx(man $comm);

#Non mi chiedo se devo iniziare a contare le opzioni o meno: so che le opzioni seguono questo pattern:
#            [-opz_breve1,]*--opzione lunga (descrizione sulla stessa riga o alla riga successiva)
for(@doc){
    if($op eq "-o" && $opzione ne ""){#Ho già incontrato un'opzione ma non ancora la sua descrizione
        if(/^\s+([^\s-].*)/){#Regex che fa match con una riga che contiene una descrizione
            $descr{$opzione}=$1;
            $opzione="";
        }
    }elsif(/^\s+((-[^-,]+),\s)*(--[^,\s\n]+)(.*)/){#Regex per match con riga che inizia con un'opzione lunga (eventualmente preceduta da opzioni brevi)
        if($op eq "-n"){
            $n+=1;
        }else{
            $opzione=$3;#memorizzo l'opzione la cui descrizione, potenzialmente, si trova sulla riga successiva
            if($4 =~ /^\s([^\n]+)/){#$4 può essere uno \n e quindi la descrizione è sulla riga successiva, oppure qualcosa che non sia \n e quindi la descrizione è sulla stessa riga
                $descr{$opzione}=$1;
                $opzione="";
            }
        }
    }
}

if($op eq "-n"){
    print "$n opzioni lunghe\n";
}else{
    open(FH,">opzioni_lunghe.log") || die "impossibile aprire il file";
    for(sort{$a cmp $b} keys %descr){
        print FH "$_ : $descr{$_}\n";
    }
}
