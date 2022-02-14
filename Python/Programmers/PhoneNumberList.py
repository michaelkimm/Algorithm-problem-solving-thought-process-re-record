def bisect(start, end, prefix, ary):
    while start <= end:
        mid = (start + end) // 2
        if len(ary[mid]) >= len(prefix) and ary[mid][:len(prefix)] == prefix:
            return True
        elif ary[mid] < prefix:
            start = mid + 1
        else:
            end = mid - 1

    return False

def solution(phone_book):
    answer = True
    phone_book.sort()
    for idx in range(len(phone_book)):
        if bisect(idx + 1, len(phone_book) - 1, phone_book[idx], phone_book):
            answer = False
            break
    return answer