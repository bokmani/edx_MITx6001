def f(i):
    return i + 2

def g(i):
    return i > 5
    
def applyF_filterG(L, f, g):
    #L에서 아닌건 지워야 하니 임시 list에 L을 추출해서 넣어줌
    #temp = L --> temp랑 L이 같게 됨 -> L을 지우면 temp도 따라서 지워짐
    #temp = L[:] --> L 처음부터 끝까지 temp에 넣어준다는 의미
    temp = L[:]

    # temp를 기준으로 for loop
    for i in temp:
        # false가 나오면 L에서 remove
        if g(f(i)) == False:
            L.remove(i)

    #L에 들어있는 숫자가 있으면 max로 가장 큰값을 return
    #값이 하나도 없으면 -1 return
    if len(L) > 0:
        return max(L)
    else:
        return -1
            

L = [0, -10, 5, 6, -4]

print(applyF_filterG(L,f,g))
print(L)
 