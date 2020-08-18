#!/bin/bash
echo -------------------------------- `date` >> data/stdout/14.txt
./joern/joern-cli/joern --script src/joern_scripts/scala/14.sc >> data/stdout/14.txt
echo 14.json
echo "Finish successfully at `date`--------------------" >> data/stdout/14.txt
