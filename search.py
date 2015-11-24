def search(list1, sum):
    d=dict()
    for i in list1:
        if sum-i in d:
                     print "The sum"+str(sum)+"is contained and the numbers"\
                           " are " + str(i) + " and " + str(sum-i)
                     return
        else:
                d[i]=1
    print "Required numbers do not exist"
list1= []
length=5
while len(list1)<length:
    num=raw_input("Enter number:")
    num1=int(num)
    list1.append(num1)
sum=raw_input("Enter sum to be searched:")
sum1=int(sum)
search(list1,sum1)
