#!/bin/bash
echo -------------------------------- `date` >> data/stdout/2.txt
./joern/joern-cli/joern --script src/joern_scripts/scala/2.sc >> data/stdout/2.txt
echo 2.json
echo "Finish successfully at `date`--------------------" >> data/stdout/2.txt
rm -r workspace/2out* && echo "Trash workspace." >> data/stdout/2.txt
