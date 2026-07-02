# --------------------------------------------------
# Brute Force Approach
# TC : (n^2)
# SC : O(n)
# --------------------------------------------------
class solution :
    def z_function(self,s):
        n = len(s)
        z= [0]*n
        for i in range(1,n):
            j = 0 
            while i+j <n and s[j]==s[i+j]:
                j+=1 
            z[i]=j 
        return z 

a = solution()

s1 = "ababa"
print("String :", s1)
print("Z Array:", a.z_function(s1))

# --------------------------------------------------
# Optimal Approach
# TC : (n)
# SC : O(n)
# --------------------------------------------------
class solution :
    def z_function(self,s):
        n = len(s)
        z=[0]*n
        L= 0 
        R= 0 
        for i in range(1,n):
            if i >R:
                L= R=i 
                while R<n and s[R-L]==s[R]:
                    R+=1
                z[i]= R-L
                R-=1
            else:
                k = i-L 
                if z[k] < R-i+1:
                    z[i]= z[k]
                else:
                    L=i 
                    while R<n and s[R-L]==s[R]:
                        R+=1
                    z[i]= R-L
                    R-=1
        return z

print("-"*30)
a = solution()
s1 = "ababa"
print("String :", s1)
print("Z Array:", a.z_function(s1))
