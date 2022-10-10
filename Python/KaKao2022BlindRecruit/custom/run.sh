#!/bin/bash

INIT_TOKEN="333bd06ae23c4063eba835cd69585109"
BASE_URL="https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod"
WEIGHT=4

python3 solve.py --problem 1 --init-token $INIT_TOKEN --base-url $BASE_URL --weight $WEIGHT