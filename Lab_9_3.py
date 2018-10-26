from math import*
def function(x):
    """

    >>> function(4)
    512
    >>> function(10)
    1058576
    >>> function(15)
    1073792449
    
    """
    y=pow(x,4)+pow(4,x)
    print(y)

print('Введіть число')
result=int(input())
function(result)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
