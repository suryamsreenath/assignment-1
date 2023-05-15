#palindrome program 
a='sun'
b='dad'
c='mom'

if a==a[::-1]:
    print(a+ ' is a palindrome')
else:
    print(a+ ' is not a palindrome')

    if b==b[::-1]:
        print(b+ ' is a palindrome')
    else:
        print(b+ 'is not a palindrome')
    if c==c[::-1]:
        print(c+ ' is a palindrome')
    else:
        print(c+ ' is not a palindrome')
