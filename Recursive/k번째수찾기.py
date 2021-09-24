def findK(n, k):
    result = []
    data = []
    for element in n:
        data.append(element)
        data.sort()
        if len(data) < k:
            result.append(-1)
        else:
            result.append(data[k-1])
    return result

def main():
    t = [int(v) for v in input().split()]
    arr = [int(i) for i in input().split()]
    print(*findK(arr,t[1]))
    
    
if __name__ == "__main__":
    main()