#!/bin/bash

if [ $# -eq 1 ]; then
    name=$1
    if [ -f probs/$name.py ]; then
        echo "ERROR: $name.py already exists in probs/ .."
        echo -n 'Overwrite (y/n): '
        read input
    fi
    if [ ! -f probs/$name.py ] || [[ `echo $input | grep -i Y` ]]; then
        commentRows=$((`grep -n 'class Solution' description.txt | cut -d ':' -f1` - 2))
        
        # copy file > comment > add default
        cp description.txt tmp
        sed -i "1,${commentRows}s/^/# /" tmp
        if [[ `grep 'List\[' description.txt` ]]; then
            listRow=$(($commentRows + 2))
            sed -i "${listRow}i from typing import List" tmp
        fi
        echo -ne "\n        pass\n\nif __name__ == '__main__':\n    pass" >> tmp

        mv tmp probs/$name.py
        ./genTest.sh
        if [[ `echo $(which code)` ]]; then
            code probs/$name.py
            code tests/test_$name.py
        fi
    fi
else
    echo "ERROR: Please input name as first argument .."
fi