#!/bin/bash

INIT_TOKEN="333bd06ae23c4063eba835cd69585109"
BASE_URL="https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod"

MATCH_SKILL=10000
WAIT_WEIGHT=2

python3 solve.py --problem 1 --init-token $INIT_TOKEN --base-url $BASE_URL --match-skill 20000 --wait-weight 3
# python3 solve.py --problem 2 --init-token $INIT_TOKEN --base-url $BASE_URL --match-skill 10000 --wait-weight 4