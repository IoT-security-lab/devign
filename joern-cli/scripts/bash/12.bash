#!/bin/bash
echo -------------------------------- `date` >> data/stdout/12.txt
./joern/joern-cli/joern --script src/joern_scripts/scala/12.sc >> data/stdout/12.txt
echo 12.json
echo "Finish successfully at `date`--------------------" >> data/stdout/12.txt
# rm -r workspace/12out* && echo "Trash workspace." >> data/stdout/12.txt
