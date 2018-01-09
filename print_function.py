if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(1,n+1):
      arr.append(i)
    
    print(*arr,sep='')