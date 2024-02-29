#!/bin/bash
# Now we curling methpds only

curl -sI "$1" | grep -i Allow | sed 's/^.*: //'
