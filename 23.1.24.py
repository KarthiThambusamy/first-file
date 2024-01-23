##def oddoreven(number):
##    result=[]
##    for i in number:
##        if i%2==0:
##            result.append('even')
##        else:
##            result.append('odd')
##    return result
##
##numberarray=[5,7,9,11]
##q=oddoreven(numberarray)
##print(q)


def even_filter(number):
    even_number=[num for num in number if num % 2==0]
    return even_number

    def odd_filter(number):
        odd_number=[num for num in number if num%2!=0]
        return odd_filter
    
    num1=[1,3,7,8,9,4,5]
    result1=odd_filter(num1)
    print(result1)

num=[1,2,3,8,9,12,18]
result=even_filter(num)
print(result)
print(result1)
