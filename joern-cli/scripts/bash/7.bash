#!/bin/bash
echo -------------------------------- `date` >> data/stdout/7.txt
./joern/joern-cli/joern --script src/joern_scripts/scala/7.sc >> data/stdout/7.txt
echo 7.json
echo "Finish successfully at `date`--------------------" >> data/stdout/7.txt
# rm -r workspace/7out* && echo "Trash workspace." >> data/stdout/7.txt
