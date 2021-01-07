#!/bin/bash
echo -------------------------------- `date` >> data/stdout/03.txt
./joern-cli/joern --script src/joern_scripts/scala/03.sc >> data/stdout/03.txt
echo 03.json
echo "Finish successfully at `date`--------------------" >> data/stdout/03.txt
rm -r workspace/03* && echo "Trash workspace." >> data/stdout/03.txt
