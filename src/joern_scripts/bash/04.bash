#!/bin/bash
echo -------------------------------- `date` >> data/stdout/04.txt
./joern-cli/joern --script src/joern_scripts/scala/04.sc >> data/stdout/04.txt
echo 04.json
echo "Finish successfully at `date`--------------------" >> data/stdout/04.txt
rm -r workspace/04* && echo "Trash workspace." >> data/stdout/04.txt
