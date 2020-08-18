#!/bin/bash
echo -------------------------------- `date` >> data/stdout/1.txt
./joern/joern-cli/joern --script src/joern_scripts/scala/1.sc >> data/stdout/1.txt
echo 1.json
echo "Finish successfully at `date`--------------------" >> data/stdout/1.txt
