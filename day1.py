#SUM OF DIGITS
n=int(input())
sum=0
while n>0:
    rem=n%10
    sum+=rem
    n=n//10
print(sum)
#o/p=1234
     #10

#PRODUCT OF DIGITS
n=int(input())
pro=1
while n>0:
    rem=n%10
    pro=pro*rem
    n=n//10
print(pro)
#o/p=1234
     #24
    

#sum the digit from the string s='a1b2c3'
s=intput()
sum=0
for i in range(0,len(s)):
    if s[i].isdigit():
        sum+=int(s[i])
print(sum)
#o/p='a1b2c3'
      #6

#count no of digits from the string
s=input()
count=0
for i in range(0,len(s)):
    if s[i].isdigit():
        count+=1
print(count)
#o/p='a1b2c3'
      #3

#check the string is palindrom or not
s=input()
rev=s[::-1]
if (rev==s):
    print("palindrom")
else:
    print("not palindrom")
        
        #OR

s=input()
s1=''
for i in range(len(s)-1,-1,-1):
    s1+=s[i]
    if s1==s:
        print("palindrom")
    else:
        print("not palindrom")
#o/p=Malayalam
    # palidrom


#COUNT NO OF VOWLES IN A STRING
s=input()
vowles=['a','e','i','o','u','A','E','I','O','U',]
count=0
for c in s:
    if c in vowles:
        count+=1
print(count)

#o/p=Nishitha
     #3
#bitwise operation
print(2&1|5)

#o/p=5

#MEMBERSHIP
s='123ABC$'
count=0
for i in s:
    if(not(i.isdigit())):
        count+=1
print(count)

#o/p=4
#print fruits from the given data
data=[1,8,'appele','carrot','mango']
fruits=['apple','mango','orange','watermelon']
for i in data:
    if i in fruits:
        print(i)

#o/p=apple
    # mango objects of data in vegies and not in fruits 
data=[1,8,'appele','carrot','mango']
fruits=['apple','mango','orange','watermelon']
vegies=['tamato','beans','carrot','onion']
for i in data:
    if i in vegies and not fruits:
        print(i)

#o/p=carrot
        #identites
s='hello'
s1='hello sri devi'
print(s is s1)

'''o/p=true
     false
false'''
#countthe no of words
s='he is playing football but he is not playing cricket'
s=s.split()
print(s.count('playing'))
print(s.count('he'))
print(len(s))

'''o/p=2 
     2 
     10
'''
#sample functions
def greetings(branch):
    return 'hello good morning',branch
print(greetings('cse'))
print(greetings('ece'))
print(greetings('it'))

'''o/p=('hello good morning', 'cse')
     ('hello good morning', 'ece')
     ('hello good morning', 'it')

'''
def greetings(branch):
    print ('hello good morning',branch)
greetings('cse')
greetings('ece') 
greetings('it')
'''o/p=hello good morning cse
     hello good morning ece
     hello good morning it
'''

# using functions return even or odd
def evenOdd(n):
    if n%2==0:
        return"even"
    else:
        return"odd"
print(evenOdd(10))
#o/p=even
#17=odd
#array divisible by 4 and 6
def divisible(arr):
    count=0
    for i in arr:
        if i%4==0 and i%6==0:
            print(i,end=' ')
            count+=1
        return count
arr=[1,36,9,24,4,2,12]
print(divisible(arr))
#
def divisible(arr):
    count=0
    for i in arr:
        if i%4==0 and i%6==0:
            print(i,end=' ')
            count+=1
        return count
arr=list(map(int,input().split()))
print(divisible(arr))
#o/p=36 24 12 3
#reverse the words
def reverseword(s):
    rev=''
    for i in s:
        rev=i+rev
    print(type(rev))
    return rev
s='sri devi is engineering college'
'''
o/p=   egelloc gnireenigne si ived irs

'''       
#
def reverseword(s):
   s=s.split()
   s=list(reversed(s))#s becomes reverse list
   print(s)
   for i in s:
       rev=i[::-1]#characters of reverse list
       print(rev,end=' ')
s='sri devi is engineering college'
reverseword(s)
'''
o/p=['college', 'engineering', 'is', 'devi', 'sri']
    egelloc gnireenigne si ived irs
'''
#fibonacci series
def fibonacci(n):
    first=0
    second=1
    print(first,second,end=' ')
    count=2
    while count<n:
        third=first+second
        print(third,end=' ')
        first=second
        second=third
        count+=1
fibonacci(10)
#o/p=0 1 1 2 3 5 8 13 21 34 
#sum of single digit number
def single_Digit(n):
    sum=0
    while (n>0):
        rem=n%10
        sum=sum+rem
        n=n//10
    return sum
n=int(input())
while (n>=10):
    n=single_Digit(n)
print(n)
'''
o/p->1234
n=678432
s=678 ,f=432
o/p=234678
'''
#functon calling another function
def check(ele):
    return ele%2==0
def increment(arr):
    count=0
    for i in arr:
        if check(i):
            print(i)
            count+=1
    return count
arr=[5,9,12,6,17,3]
print(increment(arr))
'''o/p=12
    6
    2
'''
#palindrom
def check(ele):
    ele=str(ele)
    return ele==ele[::-1]
def increment(arr):
    count=0
    for i in arr:
        if check(i):
            print(i)
            count+=1
    return count
arr=[21,78,212,782,1001]
print(increment(arr))
'''o/p=212
    1001
    2
'''
def check(n):
    n=str(n)
    return len(n)>1 and n==n[::-1] 
def increment(N):
    count=0
    for i in range(1,N+1):
        if check(i):
            print(i)
            count+=1
    return count
N=50
print(increment(N))

'''o/p=11
    22
    33
    44
    4
'''

         
