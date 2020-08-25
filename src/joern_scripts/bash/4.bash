#!/bin/bash
echo -------------------------------- `date` >> data/stdout/4.txt
./joern/joern-cli/joern --script src/joern_scripts/scala/4.sc >> data/stdout/4.txt
echo 4.json
echo "Finish successfully at `date`--------------------" >> data/stdout/4.txt
rm -r workspace/4* && echo "Trash workspace." >> data/stdout/4.txt
