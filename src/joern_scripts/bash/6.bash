#!/bin/bash
echo -------------------------------- `date` >> data/stdout/6.txt
./joern/joern-cli/joern --script src/joern_scripts/scala/6.sc >> data/stdout/6.txt
echo 6.json
echo "Finish successfully at `date`--------------------" >> data/stdout/6.txt
