#!/bin/bash

rm ./subseq.pyc

for i in /usr/local/p3ws/subseq/subseq*.pyc
do
    test=`basename $i | sed 's/subseq//' | sed 's/.pyc//'`
    if [ "$test"  == "c" ]
    then
	echo "**Testing correct implementation **"
    else
	echo "**Testing broken implementation ${test} **"
    fi
    echo "-------------------------------------"
    echo ""

    cat $i > subseq.pyc
    python3 test-subseq.py
    if [ "$?" != 0 ]
    then
	if [ "$test" == "c" ]
	then
	    echo "Your test program falsely failed the correct implementation!" > /dev/stderr
	    exit 1
	fi
    else
	if [ "$test" != "c" ]
	then
	    echo "Your test program did not identify $i as broken!" > /dev/stderr
	    exit 1
	fi
    fi
    echo ""
done
