#! /usr/bin/perl

$path = shift || die "Folder path required.";
die "Too many arguments" if @ARGV>0;

@content = qx(ls -l $path);
$maxDimension=0;
for (@content){
    @splitted = split " ";
    if(/^d/){
        push @folders, $splitted[8];
    }else{
        if($maxDimension<$splitted[4]){
            $maxDimension=$splitted[4];
            $file=$splitted[8];
            $lastAccess = $splitted[5]." ".$splitted[6]." ".$splitted[7];
        }
    }
}
print scalar(@folders)."\n";
print join("\n",@folders)."\n";
print "$file: $maxDimension\n";
while(<STDIN>){
    chomp;
    if($file eq $_){
        print "$lastAccess\n";
        $done=1;
    }else{
        for $f (@folders){
            if($f eq $_){
                print qx(ls $f);
                $done=1;
                last;
            }
        }
    }
    if($done==1){
        last;
    }
    print "Choose an item from the list above.";
}

