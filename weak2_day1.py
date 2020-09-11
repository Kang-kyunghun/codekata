def roman_to_num(string):
    # 로마자가 key, 아라비아가 velue 인 dictionary
    num_dict = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
   
    num = 0 # 변환한 값이 될 변수 
    temp = string[0] # 비교할 문자의 변수 
    
    for roman in string:  roman = 
        if roman == 'V' or roman == 'X': # V, X 앞에 I가 오는 경우
            if temp == 'I':
                num = num - 2*num_dict['I'] num = 1 -2*1 = -1
            # 2*을 하는 이유: 이미 앞에서 I가 1인줄 알고 +1을 하기 때문에 2번 빼줘야 한다.
        if roman == 'L' or roman == 'C': # L, C 앞에 X가 오는 경우
            if temp == 'X':
                num = num - 2*num_dict['X']
        
        if roman == 'D' or roman == 'M': # D, M 앞에 C가 오는 경우
            if temp == 'C':
                num = num - 2*num_dict['C'] 100 -(2*100) =100 -200 = -100
        
        num = num + num_dict[roman]  #num에 해당 로마자에 대응 대는 아라비아 숫자를 num에 더 한다. 
        temp = roman # 비교할 값을 교체한다. 
    return num

print(roman_to_num("CDL"))
	