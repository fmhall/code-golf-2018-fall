g=(x for x in range(1,999999)if(str(x)[-1]==str(x)[0]and(x%3==0 or x%5==0 or x%7==0)))
for i in g:print(i)