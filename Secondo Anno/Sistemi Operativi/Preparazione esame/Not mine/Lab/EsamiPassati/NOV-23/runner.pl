#!/usr/bin/perl

$to_print=qx(wc ../*.pl -l | head -n -1 | sort -n | head -n 1);
@splitted = split " ",$to_print; #$splitted[0] conterrà il numero di righe e $splitted[1] conterrà il nome del file
qx(chmod a-x $splitted[1]);