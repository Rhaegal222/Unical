@est = qx(cat estensioni.txt);
chomp @est;
while(<>){
    for $est(@est){
        if(/(\d+).*$est$/){
            $somma{$est}+=$1;
        }
    }
}
for(sort({$somma{$b}<=>$somma{$a}} keys %somma)){
    print "$_ $somma{$_}KB\n";
}