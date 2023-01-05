n = 5
lst = [13,46,24,52,20,9]

print(lst)

for i in range(n):
    print(lst)
    for j in range(i+1, n+1):
        
        if lst[i]>lst[j]:
            lst[i], lst[j]= lst[j], lst[i]         

print(lst)
