def my_dfs(numbers, cur_idx, cur_value, target):
    if cur_idx == len(numbers) - 1:
        if cur_value == target:
            return 1
        else:
            return 0
    
    return my_dfs(numbers, cur_idx + 1, cur_value + numbers[cur_idx + 1], target) + my_dfs(numbers, cur_idx + 1, cur_value - numbers[cur_idx + 1], target)
    
    
def solution(numbers, target):
    # x1, x-1
    stack = []
    cur_idx = 0
    total = my_dfs(numbers, cur_idx, numbers[cur_idx], target) + my_dfs(numbers, cur_idx, -numbers[cur_idx], target)
    return total