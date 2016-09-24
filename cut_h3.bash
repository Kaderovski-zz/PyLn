#!/bin/bash

cat $1 | awk '/tk_text/,/<\/h3>|close/' | sed -e 's/<[^>]*>//g'
