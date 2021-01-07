#!/bin/bash
echo -------------------------------- `date` >> data/stdout/14.txt
./joern-cli/joern --script src/joern_scripts/scala/14.sc >> data/stdout/14.txt
echo 14.json
echo "Finish successfully at `date`--------------------" >> data/stdout/14.txt
rm -r workspace/14* && echo "Trash workspace." >> data/stdout/14.txt
