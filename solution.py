from textwrap import wrap

def solution(pattern):
    
    print(set(wrap(pattern, int(len(pattern) / 2))))
    


    return  3

solution("abcabcabcabc")