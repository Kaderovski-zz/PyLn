#!/bin/bash


curl --silent http://www.lemonde.fr/rss/une.xml |grep "title" | head -3 | tail -1 | sed -e "s/<title>//g" | sed -e "s/<\/title>//g"
