#!/bin/bash
echo -------------------------------- `date` >> data/stdout/08.txt
./joern-cli/joern --script src/joern_scripts/scala/08.sc >> data/stdout/08.txt
echo 08.json
echo "Finish successfully at `date`--------------------" >> data/stdout/08.txt
rm -r workspace/08* && echo "Trash workspace." >> data/stdout/08.txt
