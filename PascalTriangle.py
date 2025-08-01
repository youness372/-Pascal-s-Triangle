class Solution:
    def generate(numRows) :
        t =  [0] * numRows  
        for i in range(numRows) : 
            t[i]  = [0]*(i+1) 
            for j in range (i+1) : 
                if  i ==  j or j == 0  : 
                    t[i][j] =1  
                else : 
                    t[i][j] = t[i-1][j-1] + t[i-1][j]  
        return t 

    