# Created a library with 4 methods called Underscore
class Underscore:
    def map(self, iterable, callback):
        for index in range (len(iterable)):
            iterable[index] = callback(iterable[index])
        return iterable

    def find(self, iterable, callback):
        for index in range (len(iterable)):
            if (callback(iterable[index])):
                return iterable[index]
    
    def filter(self, iterable, callback):
        new_list =[]
        for index in range (len(iterable)):
            if (callback(iterable[index])):
                new_list.append(iterable[index])
        return new_list
            
    def reject(self, iterable, callback):
        new_list =[]
        for index in range (len(iterable)):
            if (callback(iterable[index]) != True):
                new_list.append(iterable[index])
        return new_list
# __________________________________________________________________________________________
# Let's create an instance of our class
_ = Underscore() 

print(_.map([1,2,3], lambda x: x*2))             # Should return [2,4,6]
print(_.find([1,2,3,4,5,6], lambda x: x>4))      # Should return the first value that is greater than 4
print(_.filter([1,2,3,4,5,6], lambda x: x%2==0)) # Should return [2,4,6]
print(_.reject([1,2,3,4,5,6], lambda x: x%2==0)) # Should return [1,3,5]


