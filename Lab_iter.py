class Converse:
    def __init__(self, data):
        self._data = data          
        self._len = len(data)
        self._start = self._len + 1 if self._len % 2 else self._len
        
    def __iter__(self): 
        return self
    
    def __str__(self):
        return '{}'.format(self._data)

    def __next__(self): 
        if self._start <= 0:       
            raise StopIteration
        self._start -= 2
        return self._data[self._start]
data = Converse([1,5,8,9,7,6,10])
print(data)
for x in data:
    print(x)
