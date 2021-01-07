#!/bin/bash
echo -------------------------------- `date` >> data/stdout/3.txt
./joern/joern-cli/joern --script src/joern_scripts/scala/3.sc >> data/stdout/3.txt
echo 3.json
echo "Finish successfully at `date`--------------------" >> data/stdout/3.txt
# rm -r workspace/3out* && echo "Trash workspace." >> data/stdout/3.txt
