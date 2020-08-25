#!/bin/bash
echo -------------------------------- `date` >> data/stdout/17.txt
./joern/joern-cli/joern --script src/joern_scripts/scala/17.sc >> data/stdout/17.txt
echo 17.json
echo "Finish successfully at `date`--------------------" >> data/stdout/17.txt
rm -r workspace/17* && echo "Trash workspace." >> data/stdout/17.txt
