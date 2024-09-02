#! /usr/bin/perl

@dati = qx{cat /proc/meminfo};

foreach $elem (@dati)
{
	if ($elem =~ / #### /)
	{
		print #####
	}
}