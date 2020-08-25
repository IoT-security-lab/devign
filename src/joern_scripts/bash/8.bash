#!/bin/bash
echo -------------------------------- `date` >> data/stdout/8.txt
./joern/joern-cli/joern --script src/joern_scripts/scala/8.sc >> data/stdout/8.txt
echo 8.json
echo "Finish successfully at `date`--------------------" >> data/stdout/8.txt
rm -r workspace/8* && echo "Trash workspace." >> data/stdout/8.txt
