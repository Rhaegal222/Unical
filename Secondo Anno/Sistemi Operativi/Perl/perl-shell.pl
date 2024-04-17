cat /proc/cpuinfo | grep 'processor' | wc -l
ps -A -o pid --sort=%mem | tail -n 5
find . -size +1G
