#!/bin/bash
echo -------------------------------- `date` >> data/stdout/9.txt
./joern/joern-cli/joern --script src/joern_scripts/scala/9.sc >> data/stdout/9.txt
echo 9.json 
echo "Finish successfully at `date`--------------------" >> data/stdout/9.txt
# rm -r workspace/9out* && echo "Trash workspace." >> data/stdout/9.txt
