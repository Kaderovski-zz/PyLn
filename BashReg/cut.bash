#!/bin/bash

cat $1 | awk '/tk_common/,/<\/div>|close/' | sed -e 's/<[^>]*>//g' 
