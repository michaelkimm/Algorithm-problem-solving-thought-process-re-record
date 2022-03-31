def solution(numbers):
    answer = []
    for number in numbers:
        number = int(number)
        bOrgNum = list(str(format(number, 'b')))
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            bOrgNum.insert(0, '0')
            zeroIdx = ''.join(bOrgNum).rfind('0')
            bOrgNum[zeroIdx] = '1'
            oneIdx = ''.join(bOrgNum[zeroIdx + 1:]).find('1')
            bOrgNum[zeroIdx + 1 + oneIdx] = '0'
            answer.append(int(''.join(bOrgNum), 2))
                
    return answer