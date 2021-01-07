#!/bin/bash
echo -------------------------------- `date` >> data/stdout/01.txt
./joern-cli/joern --script src/joern_scripts/scala/01.sc >> data/stdout/01.txt
echo 01.json
echo "Finish successfully at `date`--------------------" >> data/stdout/01.txt
rm -r workspace/01* && echo "Trash workspace." >> data/stdout/01.txt
