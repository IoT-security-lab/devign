#!/bin/bash
echo -------------------------------- `date` >> data/stdout/18.txt
./joern/joern-cli/joern --script src/joern_scripts/scala/18.sc >> data/stdout/18.txt
echo 18.json
echo "Finish successfully at `date`--------------------" >> data/stdout/18.txt
