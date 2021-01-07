#!/bin/bash
echo -------------------------------- `date` >> data/stdout/10.txt
./joern-cli/joern --script src/joern_scripts/scala/10.sc >> data/stdout/10.txt
echo 10.json
echo "Finish successfully at `date`--------------------" >> data/stdout/10.txt
rm -r workspace/10* && echo "Trash workspace." >> data/stdout/10.txt
