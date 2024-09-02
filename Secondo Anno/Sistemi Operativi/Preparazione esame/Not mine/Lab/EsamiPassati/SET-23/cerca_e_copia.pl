#!/usr/bin/perl


$matricola = "123456";
qx(mkdir $matricola);
if($#ARGV==0){ # #ARGV è l'indice dell'ultimo elemento dell'array @ARGV 
    qx(cp $ARGV[0]/*.pl $matricola); # se $#ARGV==0 allora c'è un solo argomento passato (il path della cartella)
    $riga = qx(find $ARGV[0] -name "*.pl" | wc -l); # conta il numero di file .pl nella cartella
}else{
    qx(cp ../*/*.pl $matricola); #non è stato passato alcun path nella riga di comando
    $riga = qx(find ../* -name "*.pl" | wc -l); # conta il numero di file .pl nella cartella
}
print "Numero di file copiati: $riga\n";