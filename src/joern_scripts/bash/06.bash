#!/bin/bash
echo -------------------------------- `date` >> data/stdout/06.txt
./joern-cli/joern --script src/joern_scripts/scala/06.sc >> data/stdout/06.txt
echo 06.json
echo "Finish successfully at `date`--------------------" >> data/stdout/06.txt
rm -r workspace/06* && echo "Trash workspace." >> data/stdout/06.txt
