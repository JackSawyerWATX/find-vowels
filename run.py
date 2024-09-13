def solution(s):
    # TODO: implement find_vowels_positions
    vowels = "aeiouAEIOU" #defines what vowels are. 
    positions=[] #creates and empty list to store the positions of the vowels in from the string to be provided.
    
    for i in range(len(s)): # Creates a for loop to iterate the string, using range, passing in the length of the string, and the string, being s.
        if s[i] in vowels: # checks if the current character in the string is a vowel, by using the in operator and the vowels string defined earlier.
            print(s[i])
            positions.append(i) # if the character is a vowel, it appends the position of the vowel to the positions list.
    print(positions)
    return(positions)
    
print(solution("Write a function that takes a string s, iterates through it, and collects all 0-based positions of vowels in it to a list. Note that you should not use any Python built-in string methods to solve this task. For example, print(solution(\"Hello WORLD\")) should output [1, 4, 7]. Here, 'e' is a vowel, and its position in the string \"Hello\" is 1. 'o' is also a vowel, and its position is 4. The last vowel is O at position 7."))

print(solution("Hello WORLD"))