#!/bin/bash
echo -------------------------------- `date` >> data/stdout/09.txt
./joern-cli/joern --script src/joern_scripts/scala/09.sc >> data/stdout/09.txt
echo 09.json 
echo "Finish successfully at `date`--------------------" >> data/stdout/09.txt
rm -r workspace/09* && echo "Trash workspace." >> data/stdout/09.txt
