#!/bin/bash

cat $1 | awk '/tk_common/,/<\/div>|close/' | sed '/<div class="tk_common">/d' | sed '/<\/div>/d'
