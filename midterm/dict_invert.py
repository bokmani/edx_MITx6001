def dict_invert(d):
    inverse = {}
    #dictionary의 key값들로 for loop 돌리면서
    # inverse dictionary에 해당 키가 없으면 key / [value] 
    # 있으면 해당 key에 append --> 이렇게 하기 위해서 [value] list로 처음 값을 기록
    for keys in d.keys():
        if d[keys] in inverse:
            inverse[d[keys]].append(keys)
        else:
            inverse[d[keys]] = [keys]
    
    #value 가 list이므로 value를 for loop로 돌리면서, list를 sort처리 해준다 ([4,3] --> [3,4])
    for values in inverse.values():
        values.sort()

    return inverse



d = {1:10, 2:20, 4:30, 3:30} 
print(dict_invert(d))