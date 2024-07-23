# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other. 

str1 = "tab"
str2 = "bat"

# Approach 1
def permutation(str1, str2):
    if (len(str1) != len(str2)):
        print('Lengths are not same')
        return False

    str1 = sorted(str1)
    str2 = sorted(str2)

    for i in range(0, len(str1)):
        if(str1[i] != str2[i]):
            print("Not Equal")
            return False

    print("Permutation successful")    
    return True

print(permutation(str1,str2))


# Approach 2

No_Of_Characters = 256

def permutation1(str1, str2):
    if (len(str1) != len(str2)):
        print('Lengths are not same')
        return False
    
    count1 = [0] * No_Of_Characters

    for i in range(len(str1)):
        count1[ord(str1[i])] += 1

    for i in range(len(str2)):
        count1[ord(str2[i])] -= 1
        if count1[ord(str2[i])]<0:
            return False
        
    return True
print(permutation1(str1,str2))