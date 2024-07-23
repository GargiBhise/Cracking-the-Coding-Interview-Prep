str = " abbb"
def isUnique(str):
    for i in range(len(str)):
        for j in range(i+1,len(str)):
            print(i,j, str[i], str[j])
            if str[i] == str[j]:
                return False
    return True
        
print(isUnique(str))