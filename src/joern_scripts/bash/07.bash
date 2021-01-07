#!/bin/bash
echo -------------------------------- `date` >> data/stdout/07.txt
./joern-cli/joern --script src/joern_scripts/scala/07.sc >> data/stdout/07.txt
echo 07.json
echo "Finish successfully at `date`--------------------" >> data/stdout/07.txt
rm -r workspace/07* && echo "Trash workspace." >> data/stdout/07.txt
