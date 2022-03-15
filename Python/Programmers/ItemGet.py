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