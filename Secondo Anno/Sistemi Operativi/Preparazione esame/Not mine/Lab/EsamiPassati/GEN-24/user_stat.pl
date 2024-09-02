#!/usr/bin/perl


$utente = qx( whoami );
$utente = chomp($utente); # remove newline
print "Nome utente: $utente\n";
$processi = qx(ps -u $utente |awk '{ print $1}'| tail -n +2);
print "PID dei processi in esecuzione:\n$processi\n";

$spazio = qx(du -sh $HOME);

print "Spazio occupato nella home: $spazio /home/$utente\n"; 