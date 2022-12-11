#!/bin/bash

INIT_TOKEN="7476c2a8cb88ff9f033d80d70268dce5"
BASE_URL="https://68ecj67379.execute-api.ap-northeast-2.amazonaws.com/api"
WEIGHT=1

python3 solve.py --problem 1 --init-token $INIT_TOKEN --base-url $BASE_URL --weight $WEIGHT
python3 solve.py --problem 2 --init-token $INIT_TOKEN --base-url $BASE_URL --weight $WEIGHT