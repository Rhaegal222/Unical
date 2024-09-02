#! /usr/bin/perl


if(scalar @ARGV == 1){

    $nomeCartella = $ARGV[0]; 


    @nomiSottocartelle = qx(find $nomeCartella -maxdepth 1 -type d -exec basename {} \\; | grep -P '^[\da-zA-Z]');



    # ALTERNATIVA
    # nomiSottocartelle = qx(ls -l Sistemi-Operativi/ | grep -P '^d' | cut -d ' ' -f 13-) 
                                                                    # taglia usando ' ' come delimitatore
                                                                    # e prende dal campo 13 in poi
                                                                    # (il - serve per indicare dal 13 in poi)

    print scalar @nomiSottocartelle ;
    print "\n";
    for($i=0;$i<scalar @nomiSottocartelle; $i++){
        print($nomiSottocartelle[$i]);
    }

    @nomiFile = qx(ls -l $nomeCartella | grep -p '^-');

    $max=0;
    $maxIndex = 0;
    $count = 0;
    for(@nomiFile){
        @temp = split(' ', $_);
        if($maxIndex<$temp[4]){
            $max = $temp[4];
            $maxIndex = $count;
        }
        $count+=1;
    }
    print "output: ".$max;


=pod

    $path = "Sistemi-Operativi/";

    @content = qx(ls -l $path);
    $maxDimension=0;
    for (@content){
        @splitted = split " ";
        if(/^d/){
            push @folders, $splitted[8];
        }else{
            if($maxDimension<$splitted[4]){
                $maxDimension=$splitted[4];
                $lastAccess = $splitted[5]." ".$splitted[6]." ".$splitted[7];

                for($i=0;$i<8;$i++){
                    shift @splitted;
                }

                $file=join (' ',@splitted);
            }
        }
    }

    print $maxDimension;

    print "\n";

    print $file;

    print "\n";


=cut




    $input = <STDIN>;
    if($input =~/^bin$/){
        @contBin = qx(find $nomefile/bin -maxdepth 1 -exec basename {} \\;);
        for(@contBin){
            print $_;
        }
    }
    elsif($input =~/output/){
        @contFile = qx(cat $nomefile/output);
        for(@contFile){
            print $_;
        }
    }
    close STDIN;

    print "\n";
    


    print "\n";

}
else{
    if(scalar @ARGV > 1){
        die "Questo comando DEVE ricevere UNA SOLA cartella come parametro";
    }
    else{
        die "Questo comando DEVE ricevere ALMENO UNA cartella come parametro";
    }
}