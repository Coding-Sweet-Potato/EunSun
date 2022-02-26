def sherlockAndAnagrams(s):
    # Write your code here
    total = 0
    chunk_dic = {}
    
    for i in range(1, len(s)):
        for j in range(len(s)-i+1):
            chunk = ''.join(sorted(s[j:j+i]))
            total += chunk_dic.setdefault(chunk, 0) #키값이 있으면 value를 반환하고 없으면 0 반환
            chunk_dic[chunk] += 1
            
    return total
