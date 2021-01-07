#!/bin/bash
echo -------------------------------- `date` >> data/stdout/00.txt
./joern-cli/joern --script src/joern_scripts/scala/00.sc >> data/stdout/00.txt
echo 00.json
echo "Finish successfully at `date`--------------------" >> data/stdout/00.txt
rm -r workspace/00* && echo "Trash workspace." >> data/stdout/00.txt
