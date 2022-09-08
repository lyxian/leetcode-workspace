#!/bin/bash

if [ $# -eq 1 ]; then
    filename=$1
    if [ ! -f probs/$filename ]; then
        echo "ERROR: $filename cannot be found in probs/ .."
    else
        # Find in script
        probs="probs."`echo $filename | cut -d . -f1`
        ARGUMENTS=`grep "^    def" probs/$filename | sed 's/.*(\(.*\)).*/\1/' | tr , '\n' | grep ':' | cut -d ':' -f 1 | xargs | sed 's/ /, /'`
        FUNCTION=`grep "^    def" probs/$filename | sed 's/.*def \(.*\)(.*/\1/'`

        # Replace script
        sed "s/probs/$probs/" tests/template.py > tmp
        sed "s/ARGUMENTS/$ARGUMENTS/" tmp > tmp1
        sed "s/FUNCTION/$FUNCTION/" tmp1 > tests/test_$filename
        rm tmp tmp1
    fi
elif [ $# -eq 0 ]; then
    if [[ `git status | grep "probs/.*\.py"` ]]; then
        echo "Creating test files for all modified python scripts in probs/ .."
        git status | grep "probs/.*\.py" | cut -d / -f2 | xargs -I % ./genTest.sh %
    else
        echo "ERROR: No modified python scripts found in probs/ .."
    fi
else
    echo "ERROR: Please input filename as first argument .."
fi