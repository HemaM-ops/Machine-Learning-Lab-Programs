# M Hemasri - AIE22028
# ML Lab 1 programs
# Amrita School of Engineering, Bengaluru
#Program to find the count of number of vowels and consonants in the input string

def vowelConsonant_count(str):
    #vowel set
    vowel = set("aeiouAEIOU")

    vowelCount=0
    consonantCount=0

    for alphabet in str:

        if alphabet in vowel:
            vowelCount +=1
        
        else:
            consonantCount +=1

    return vowelCount,consonantCount



instring=input("Enter a string: ")
vowelCount, consonantCount= vowelConsonant_count(instring)
print("The given sting is : ",instring,"\nNumber of vowels: ",vowelCount,"\nNumber of consonants: ",consonantCount)
