def formatter(string1) :
    a = string1.split('\n')
    print(a)
    for i in range(1,int(a[0])) :
        list1 = a[i].split(" ")
        s = sorted(list(set(list1)),reverse=True)
        k = int(a[2+i])
        print(s[k-1])


formatter("""2
3.14159 -1000 999999999 3.14
3
0 0 0 0 0 0 1 -1 0 0 0 0 0 0
2""")