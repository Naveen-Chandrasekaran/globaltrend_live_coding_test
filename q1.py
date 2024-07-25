def  lcs(str1 , str2,m,n):
    if m==0 or n==0:
        return 0
    elif str1[m-1] == str2[n-1]:
        return 1+lcs(str1,str2,m-1,n-1)
    else:
        return max(lcs(str1,str2,m,n-1),lcs(str1,str2,m-1,n))


str1="abcde"
str2="ace"
print(lcs(str1,str2,len(str1),len(str2)))
