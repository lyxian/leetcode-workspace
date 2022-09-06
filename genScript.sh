#!/bin/bash

if [ $# -eq 1 ]; then
    name=$1
    if [ -f probs/$name.py ]; then
        echo "ERROR: $name.py already exists in probs/ .."
        echo -n 'Overwrite (y/n): '
        read input
    fi
    if [[ `echo $input | grep -i Y` ]]; then
        commentRows=$((`grep -n 'class Solution' description | cut -d ':' -f1` - 2))
        
        # copy file > comment > add default
        cp description tmp
        sed -i "1,${commentRows}s/^/# /" tmp
        echo -ne "\n        pass\n\nif __name__ == '__main__':\n    pass" >> tmp

        mv tmp probs/$name.py
        if [[ `echo $(which code)` ]]; then
            code probs/$name.py
        fi
    fi
else
    echo "ERROR: Please input name as first argument .."
fi