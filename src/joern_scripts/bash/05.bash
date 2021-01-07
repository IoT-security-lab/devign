#!/bin/bash
echo -------------------------------- `date` >> data/stdout/05.txt
./joern-cli/joern --script src/joern_scripts/scala/05.sc >> data/stdout/05.txt
echo 05.json
echo "Finish successfully at `date`--------------------" >> data/stdout/05.txt
rm -r workspace/05* && echo "Trash workspace." >> data/stdout/05.txt
