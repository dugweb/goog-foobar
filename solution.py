from textwrap import wrap

def solution(s):
    length = len(s)
    mod = 1
    repeatedlength = length
    while mod <= (length / 2):
        if len(s) % mod == 0:
            theset = set(wrap(s, mod))
            if (len(theset)) == 1 and len(list(theset)[0]) < repeatedlength:
                repeatedlength = len(list(theset)[0])
        mod += 1
    
    return  length / repeatedlength