#!/bin/bash
echo -------------------------------- `date` >> data/stdout/15.txt
./joern/joern-cli/joern --script src/joern_scripts/scala/15.sc >> data/stdout/15.txt
echo 15.json
echo "Finish successfully at `date`--------------------" >> data/stdout/15.txt
