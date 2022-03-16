def check_pt_in_rectangle(rectangle, x, y):
    p = (x, y)
    bl = (rectangle[0], rectangle[1])
    tr = (rectangle[2], rectangle[3])
    return p[0] >= bl[0] and p[0] <= tr[0] and p[1] >= bl[1] and p[1] <= tr[1]

def check_pt_in_line(p1, p2, x, y):
    if p1[0] == p2[0] == x:
        if p1[1] > p2[1]:
            return True if p1[1] >= y > p2[1] else False
        else:
            return True if p2[1] > y >= p1[1] else False
    elif p2[1] == p2[1] == y:
        if p1[0] > p2[0]: 
            return True if p1[0] >= x > p2[0] else False
        else:
            return True if p2[0] > x >= p1[0] else False
    else:
      return False

def get_cur_rect_info(rectangles, x, y, before_rect = [0,0,0,0]):
    # x, y좌표, 새롭게 속한 사각형 정보
    cur_info = [x, y, before_rect]
    for rectangle in rectangles:
        if check_pt_in_rectangle(rectangle, x, y):
            if rectangle == before_rect:
                continue
            cur_info[2] = rectangle
            break
    return cur_info, before_rect

def moveCWInRectangle(rectangle, x, y):
    pt = (x, y)
    bl = (rectangle[0], rectangle[1])
    br = (rectangle[2], rectangle[1])
    tr = (rectangle[2], rectangle[3])
    tl = (rectangle[0], rectangle[3])
    #print(bl,br,tr,tl)
    # 상
    if check_pt_in_line(tr, tl, pt[0], pt[1]):
        return x - 1, y
    # 좌
    elif check_pt_in_line(tl, bl, pt[0], pt[1]):
        return x, y - 1
    # 하
    elif check_pt_in_line(bl, br, pt[0], pt[1]):
        return x + 1, y
    # 우
    elif check_pt_in_line(br, tr, pt[0], pt[1]):
        return x, y + 1
    #print("haha")
    return x, y

def get_path_length(rectangles, srcX, srcY, targetX, targetY):
    length = 0
    #print(srcX, srcY)
    cur_info, _ = get_cur_rect_info(rectangles, srcX, srcY)
    #print(cur_info)
    time_passed = 0
    while cur_info[0] != targetX or cur_info[1] != targetY:
    #for _ in range(14):
        cx, cy = moveCWInRectangle(cur_info[2], cur_info[0], cur_info[1])
        cur_info[0], cur_info[1] = cx, cy
        cur_info, before_rect = get_cur_rect_info(rectangles, cur_info[0], cur_info[1], cur_info[2])
        time_passed += 1
        #print(cur_info)
      
    length = time_passed
    return length

def solution(rectangle, characterX, characterY, itemX, itemY):
    src2item = get_path_length(rectangle, characterX, characterY, itemX, itemY)
    #print("--")
    item2src = get_path_length(rectangle, itemX, itemY, characterX, characterY)
    answer = min(src2item, item2src)
    return answer

# 82.1%


# =================================================================================== #

def check_movable_pt(rectangles, x, y):
    for rect in rectangles:
        if check_pt_in_rectangle(rect, x, y):
            return False
    for rect in rectangles:
        if check_pt_on_rect_border(rect, x ,y):
            return True
    return False

def check_pt_on_rect_border(rectangle, x, y):
    # 모든 직사각형의 내부에 있으면 안됨 and 1개 이상의 직사각형의 border에 있어야함.
    p = (x, y)
    bl = (rectangle[0], rectangle[1])
    tr = (rectangle[2], rectangle[3])
    is_in_on_rect = p[0] >= bl[0] and p[0] <= tr[0] and p[1] >= bl[1] and p[1] <= tr[1]
    is_in_rect = check_pt_in_rectangle(rectangle, x, y)
    return is_in_rect == False and is_in_on_rect

def check_pt_in_rectangle(rectangle, x, y):
    p = (x, y)
    bl = (rectangle[0], rectangle[1])
    tr = (rectangle[2], rectangle[3])
    return p[0] > bl[0] and p[0] < tr[0] and p[1] > bl[1] and p[1] < tr[1]

from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0 ,0]
    visited = [[False] * 101 for _ in range(101)]
    
    answer = 0
    rects = []
    for r in rectangle:
        rect = [p * 2 for p in r]
        rects.append(rect)
        
    cx = characterX * 2
    cy = characterY * 2
    ix = itemX * 2
    iy = itemY * 2
    q = deque([(cx, cy, 0)])    # x, y, cost
    
    while q:
        cx, cy, cost = q.popleft()
        #print(cx, cy, cost)
        if cx == ix and cy == iy:
            answer = cost // 2
            break
        for idx in range(4):
            nx = cx + dx[idx]
            ny = cy + dy[idx]
            is_on_rectangle = check_movable_pt(rects, nx, ny)
            if 2 <= nx <= 100 and 2 <= ny <= 100 and not visited[ny][nx] and is_on_rectangle:
                q.append((nx, ny, cost + 1))
                visited[ny][nx] = True
    return answer


# ======================================================== #

from collections import deque

def check_movable_pt(rectangles, x, y):
    on_any_rectangle = any((x in (x1, x2) and y1 <= y <= y2) or (y in (y1, y2) and x1 <= x <= x2) for x1, y1, x2, y2 in rectangles)
    in_any_rectangle = any(x > x1 and x < x2 and y > y1 and y < y2 for x1, y1, x2, y2 in rectangles)
    return (not in_any_rectangle) and on_any_rectangle

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0 ,0]
    visited = [[False] * 101 for _ in range(101)]
    
    answer = 0
    rects = []
    for r in rectangle:
        rect = [p * 2 for p in r]
        rects.append(rect)
        
    cx = characterX * 2
    cy = characterY * 2
    ix = itemX * 2
    iy = itemY * 2
    q = deque([(cx, cy, 0)])    # x, y, cost
    
    while q:
        cx, cy, cost = q.popleft()
        #print(cx, cy, cost)
        if cx == ix and cy == iy:
            answer = cost // 2
            break
        for idx in range(4):
            nx = cx + dx[idx]
            ny = cy + dy[idx]
            is_on_rectangle = check_movable_pt(rects, nx, ny)
            if 2 <= nx <= 100 and 2 <= ny <= 100 and not visited[ny][nx] and is_on_rectangle:
                q.append((nx, ny, cost + 1))
                visited[ny][nx] = True
    return answer