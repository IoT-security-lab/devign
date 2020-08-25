#!/bin/bash
echo -------------------------------- `date` >> data/stdout/0.txt
./joern/joern-cli/joern --script src/joern_scripts/scala/0.sc >> data/stdout/0.txt
echo 0.json
echo "Finish successfully at `date`--------------------" >> data/stdout/0.txt
rm -r workspace/0out* && echo "Trash workspace." >> data/stdout/0.txt
