flaga=True
n=int(raw_input())
print('Maksymalizuje:')
for i in range(1,n+1):
    for j in range(1,n+1):
        if flaga:
            flaga=False
        else:
            print '+',
        print 'c'+ str(i)+','+str(j),

print('')
print('Warunki:')
 
for i in range (1,n+1):
    for j in range (1,n+1):
        print ('c' + str(i) + ',' + str(j)+ ' >= 0')
        print ('c' + str(i) + ',' + str(j)+ ' <= 1')

for j in range (1,n+1):
    flaga = True
    for i in range (1,n+1):
        if flaga:
            flaga=False;
        else:
            print '+',
        print 'a'+str(i)+','+str(j),
    print('<=1')


for i in range (1,n+1):
    flaga=True
    for j in range (1,n+1):
        if flaga:
            flaga=False;
        else:
            print '+',
        print 'c'+str(i)+','+str(j),
    print('<= 1')


for roznica in range (-n+2,n-1):
    flaga=True
    for i in range (1, n + 1):
         j=roznica+i
         if j>=1 and j<=n:
             if flaga:
                 flaga= False;
             else:
                 print '+',
             print 'c'+ str(i) + ',' + str(j),
    print('<=1')


for suma in range (3,2*n):
    flaga=True
    for i in range (1,n+1):
        j=suma-i
        if j>=1 and j<=n:
            if flaga:
                flaga=False;
            else:
                print '+',
            print 'c'+str(i)+','+str(j),
    print('<=1')
