import sys
input = sys.stdin.readline

N = int(input().strip())
tops = list(map(int, input().split()))

def recursive(tops, record, sourceIdx, cmpIdx):
    if cmpIdx < 0:
        return -1
    if tops[sourceIdx] < tops[cmpIdx]:
        record[sourceIdx] = cmpIdx
        return cmpIdx
    else:
        return recursive(tops, record, sourceIdx, record[cmpIdx])
    
record = [-1 for _ in range(N)]

for idx in range(N):
    record[idx] = recursive(tops, record, idx, idx - 1)

print(' '.join([str(v + 1) for v in record]))
