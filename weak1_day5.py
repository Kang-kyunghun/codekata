def get_prefix(string):
    
    if not string:
        return ''

    start_str = string[0]

    for compare_str in string:
        result_str =''
        
        for start, compare in tuple(zip(start_str, compare_str)):
           
            if start == compare:
                result_str += start
            else:
                start_str = result_str
                break
    
    return result_str

string =['saart', 'sbair', 'sce', 'sdep']
#string = ['start', 'wework', 'today']


print(get_prefix(string))
