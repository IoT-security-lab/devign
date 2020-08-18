#!/bin/bash
echo -------------------------------- `date` >> data/stdout/19.txt
./joern/joern-cli/joern --script src/joern_scripts/scala/19.sc >> data/stdout/19.txt
echo 19.json
echo "Finish successfully at `date`--------------------" >> data/stdout/19.txt
