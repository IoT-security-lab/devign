#!/bin/bash
echo -------------------------------- `date` >> data/stdout/16.txt
./joern/joern-cli/joern --script src/joern_scripts/scala/16.sc >> data/stdout/16.txt
echo 16.json
echo "Finish successfully at `date`--------------------" >> data/stdout/16.txt