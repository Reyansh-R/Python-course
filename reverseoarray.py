def revers(a, a_size, n):
    temp = 0
    while (temp<a_size):
         start = temp
         end = min(temp + n-1, a_size - 1)
         while(start < end):
              a[start], a[end] = a[end], a[start]
              start+= 1
              end-= 1
         temp+= n
         
         
         

a = [1, 2, 3, 4, 56, 78, 99, 1000]

n = 2
a_size = len(a)
revers(a, a_size, n)

for i in range(0, a_size):
     print(a[i], end="")

        
        
         
              
              
