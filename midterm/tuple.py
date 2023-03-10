def max_val(t):
    #숫자만 뽑아내는 함수를 하나 추가로 정의
    def find_number(term):
        num_list = []
        #term으로 넘어오는게 숫자 / tuple / list 일 수 있으므로 for loop로 하나씩 체크
        for item in term:
            #type으로 int이면, num_list에 append
           if type(item) is int:
              num_list.append(item)
            #int가 아니면 tuple이나 list이므로 find_number를 다시 실행 
            #return 받는게 num_list list이므로 num_list에 +로 이어 붙임
           else:
              num_list += find_number(item)

        #최종적으로 재귀함수 실행까지 해서 num_list로 숫자 리스트만 retur됨
        return num_list
    
    #숫자리스트만 뽑아내도록 실행
    numbers = find_number(t)

    #max를 이용해서 list에서 가장 큰수 찾음
    print(max(numbers))







max_val((5, (1,2),[[1],[9]]))