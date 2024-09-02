#!/usr/bin/perl

$ARGV[0]

$linee1 = qx(sort $HOME/Desktop/$ARGV[0] | uniq |wc -l );
$caratteri1 = qx (sort $HOME/Desktop/$ARGV[0] | uniq |wc -m );
$linee2 = qx(sort $HOME/Desktop/$ARGV[1] | uniq |wc -l );
$caratteri2 = qx (sort $HOME/Desktop/$ARGV[1] | uniq |wc -m );


$comune = qx(cat $HOME/Desktop/$ARGV[0] $HOME/Desktop/$ARGV[1] | sort | uniq -d| wc -l);

print "$ARGV[0] \nlinee: $linee1\ncaratteri: $caratteri1 \n$ARGV[1] \nlinee: $linee2 \ncaratteri: $caratteri2 \ncomuni: $comune\n";

