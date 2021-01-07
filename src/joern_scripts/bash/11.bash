#!/bin/bash
echo -------------------------------- `date` >> data/stdout/11.txt
./joern-cli/joern --script src/joern_scripts/scala/11.sc >> data/stdout/11.txt
echo 11.json
echo "Finish successfully at `date`--------------------" >> data/stdout/11.txt
rm -r workspace/11* && echo "Trash workspace." >> data/stdout/11.txt
