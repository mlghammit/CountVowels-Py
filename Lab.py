def countVowels(word): #Spacing
    numVowels = 0 #change numvowels = 0
    for letter in word: ###intention, change string to word
        if letter in "AUIOEaeiou": #Needs comma,
            numVowels+=1 
    return numVowels
print(countVowels("AEIOu"))#It is correct counts only lower case vowels

def factorial(n):
    result = n
    for i in range(n-1, 0, -1):
        result *= i
    return result

print(factorial(5))
