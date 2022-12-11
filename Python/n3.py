#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMaximumRemovals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY order
#  2. STRING source
#  3. STRING target
#

# def subsequenceAvailable(sourceStr, targetStr):
#     sourceCharIdx = 0
#     matchCnt = 0
#     for targetChar in targetStr:
#         for idx in range(sourceCharIdx, len(sourceStr)):
#             if targetChar == sourceStr[idx]:
#                 matchCnt += 1
#                 sourceCharIdx = idx + 1
#                 break
            
#     return True if matchCnt == len(targetStr) else False

def subsequenceAvailable(sourceStr, targetStr, targetStrFoundIdxSet, checkStartIdx):
    sourceCharIdx = checkStartIdx
    matchCnt = 0
    for targetChar in targetStr:
        for idx in range(sourceCharIdx, len(sourceStr)):
            if targetChar == sourceStr[idx]:
                matchCnt += 1
                sourceCharIdx = idx + 1
                targetStrFoundIdxSet.add(idx)
                break
                
    return True if matchCnt == len(targetStr) else False

def getMaximumRemovals(order, source, target):
    # Write your code here
    n = len(order)
    order = [v - 1 for v in order]
    
    answer = 0
    targetStrFoundIdxSet = set([])
    checkStartIdx = 0
    for removalIdx in order:
        source = source[:removalIdx] + '-' + source[removalIdx + 1:]
        if not (removalIdx in targetStrFoundIdxSet) and not (len(targetStrFoundIdxSet) == 0):
            answer += 1
            continue
        # target 찾았던 가장 첫 위치부터 재시작
        checkStartIdx = min(targetStrFoundIdxSet) if len(targetStrFoundIdxSet) != 0 else 0
        targetStrFoundIdxSet = set([])
        if not subsequenceAvailable(source, target, targetStrFoundIdxSet, checkStartIdx):
            break
        answer += 1
    return answer
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    order_count = int(input().strip())

    order = []

    for _ in range(order_count):
        order_item = int(input().strip())
        order.append(order_item)

    source = input()

    target = input()

    result = getMaximumRemovals(order, source, target)

    fptr.write(str(result) + '\n')

    fptr.close()
