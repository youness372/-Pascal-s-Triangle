# *The Problem*  🤔 

- Given an integer `numRows`, return the first numRows of Pascal's triangle.

- In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

    ![PascalTriangleAnimated2.gif](https://assets.leetcode.com/users/images/d9f54ddd-a9bc-4206-966b-0d91c6a18ad7_1754041357.765602.gif)

# ⛓️‍💥 *Approach* 

---


- To Solve This Probleme we have a 3 Important Points : 

    - in any step the number of rows graeter than the previos one 
    - always ` Rows[i][0] = Rows[i][-1] =  1 `
    - inside any Rows we have `Rows[i][j] =Rows[i-1][j-1] +Rows[i-1][j] ` 

# 🧪 *Sumulation* : 
```py
    t =  [0] * numRows    
        |
        |
    t =  [0,0,0,0,0,0,0,...........(numRows Time)]   
```
-  we Know the lengh of any Row inside our Array   :   

    - `t[i] = [0] * (i+1)`

- Exmple 1 :  
```py
        numRows = 5 
        t = [0] * numRows   
        t = [0 ,0 ,0, 0, 0]   

           [[0], 
           [0,0],
      t = [0,0,0],  
         [0,0,0,0], 
        [0,0,0,0,0]]
``` 
- Always we have 1 in ` Rows[i][0] = Rows[i][-1] =  1 `   

```py
           [[1], 
           [1,1],
      t = [1,0,1],  
         [1,0,0,1], 
        [1,0,0,0,1]]
```
- if` i != i` and `j != 0` so : 

    
![image.png](https://assets.leetcode.com/users/images/901bf7ba-a84b-40f1-a682-70276609e340_1754045199.1705456.png)

# *⌛ Complexity*

- *Time complexity :* $$O(n^2)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- *Space complexity:* $$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# *✅ Solution :*
```python3 []
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        t =  [0] * numRows  
        for i in range(numRows) : 
            t[i]  = [0]*(i+1) 
            for j in range (i+1) : 
                if  i ==  j or j == 0  : 
                    t[i][j] =1  
                else : 
                    t[i][j] = t[i-1][j-1] + t[i-1][j]  
        return t 
```

![monkey-d-luffy-leetcode.jpg](https://assets.leetcode.com/users/images/fb9de30f-bfca-4232-8c28-a6ee09520c0d_1754045425.2866802.jpeg)












