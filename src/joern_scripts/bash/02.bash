#!/bin/bash
echo -------------------------------- `date` >> data/stdout/02.txt
./joern-cli/joern --script src/joern_scripts/scala/02.sc >> data/stdout/02.txt
echo 02.json
echo "Finish successfully at `date`--------------------" >> data/stdout/02.txt
rm -r workspace/02* && echo "Trash workspace." >> data/stdout/02.txt
