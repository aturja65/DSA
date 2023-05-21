def findPowerOfElement(num, pow):
    if pow == 0:
        return 1
    elif pow == 1:
        return num
    else:
        mid = pow // 2
        ans = findPowerOfElement(num, mid)
        return (ans * ans) if (pow % 2 == 0) else (ans * ans * num)


## Driver Code
num = 2
pow = 14
result = findPowerOfElement(num, pow)
print(f"Power of element is: {result}")
