#!/usr/bin/perl

#print("Hello world\n");

$var=2314;  # scalare
$str='ciao $var';
$str="ciao $var";
$str='ciao'.$var;  # . operatore di concatenazione

@array=(1,2,3,4);
@array1=(1) x 10;
@array2=1 x 10;

#print $str . "\n";
#print @array . "\n";
#print @array1 . "\n";
#print join " ", @array1;
#print "\n";
#print join " ", @array1;
#print @array . "\n";
#print $#array;
#print $array[0];
#print "\n";
#print $str . "\n";

for($i=0; $i<=$#array; $i++){
    print("$array[$i] ");
}
print "\n";

push @array, 5;

for($i=0; $i<=$#array; $i++){
    print("$array[$i] ");
}
print "\n";

unshift @array, 0;

for($i=0; $i<=$#array; $i++){
    print("$array[$i] ");
}
print "\n";

pop @array;
print "Rimosso l'ultimo\n$array[$#array] \n";

shift @array;
print "Rimosso il primo\n$array[0] \n";

for(@array){
    print "$_\n" # _ serve per indicare variabili temporanee che non vengono salvate ne associate da nessuna parte
}

@str_a=("ciao", "ciccio", "chfkh");
@s = split('_',"c_i_a_o");

for(@s){
    print "$_\n" # _ serve per indicare variabili temporanee che non vengono salvate ne associate da nessuna parte
}

for(@str_a){
    print "\n";
    print split "c";
    print "\n";
}

print join ' ', @s;

print "\n";
print $str."\n";

@array;  # array
%array_a;  # array associativi
%hash;  # hashmap

$str1="ciao";
$str2="giykuyg";