def solution(s):
    # TODO: implement find_vowels_positions
    vowels = "aeiouAEIOU"
    positions=[]
    
    for i in range(len(s)):
        if s[i] in vowels:
            positions.append(i)
    return(positions)
    
print(solution("Hello WORLD"))