from bisect import bisect_left, bisect_right

def my_bisect_word_cnt(ary, left, right):
  # 물음표 앞 매치되는 문자 인덱스 시작 & 끝 구하기
  tmpStartIdx = bisect_left(ary, left)
  tmpEndIdx = bisect_right(ary, right)

  return tmpEndIdx - tmpStartIdx

def check_question_on_tail(target):
  if target[len(target) - 1] == '?':
    return True
  else:
    return False

sortedWordsInCntOrder = [[] for _ in range(10001)]
sortedReverseWordInCntOrder = [[] for _ in range(10001)]


def solution(words, queries):
  answer = []

  # 데이터 초기화 & 정제
  for word in words:
    sortedWordsInCntOrder[len(word)].append(word)
    sortedReverseWordInCntOrder[len(word)].append(word[::-1])

  for i in range(10001):
    sortedWordsInCntOrder[i].sort()
    sortedReverseWordInCntOrder[i].sort()

  # 물음표 앞 매치되는 문자 인덱스 시작 & 끝 구하기
  for i in range(len(queries)):
    if (check_question_on_tail(queries[i])):
      cnt = my_bisect_word_cnt(sortedWordsInCntOrder[len(queries[i])], queries[i].replace("?", "a"), queries[i].replace("?", "z"))

    else:
      cnt = my_bisect_word_cnt(sortedReverseWordInCntOrder[len(queries[i])], queries[i][::-1].replace("?", "a"), queries[i][::-1].replace("?", "z"))
    # startIdx, endIdx 사이에 query 갯수와 갯수가 같은 애들 몇개 있나?
    answer.append(cnt)

  return answer

aryy = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queir = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(sorted(aryy))

print(solution(aryy, queir))