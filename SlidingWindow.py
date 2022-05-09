def sliding_window(arr,win):
    s=sum([arr[i] for i in range(win)])
    print(s)
    max_sum=s
    for i in range(len(arr)-win):
        s=s+arr[i+win]-arr[i]
        max_sum=max(max_sum,s)
    return s
arr=[80,-50,90,100]
k=2
res=sliding_window(arr,k)
print(res)
