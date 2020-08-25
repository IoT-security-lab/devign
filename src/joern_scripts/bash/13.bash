#!/bin/bash
echo -------------------------------- `date` >> data/stdout/13.txt
./joern/joern-cli/joern --script src/joern_scripts/scala/13.sc >> data/stdout/13.txt
echo 13.json 
echo "Finish successfully at `date`--------------------" >> data/stdout/13.txt
rm -r workspace/13* && echo "Trash workspace." >> data/stdout/13.txt
