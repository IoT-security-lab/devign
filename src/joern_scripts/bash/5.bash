#!/bin/bash
echo -------------------------------- `date` >> data/stdout/5.txt
./joern/joern-cli/joern --script src/joern_scripts/scala/5.sc >> data/stdout/5.txt
echo 5.json
echo "Finish successfully at `date`--------------------" >> data/stdout/5.txt
rm -r workspace/5* && echo "Trash workspace." >> data/stdout/5.txt
