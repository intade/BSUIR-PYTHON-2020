class Vector:

    def __init__(self, *elems):
        self.coordinates = list(elems)
        self.it = 0 #для функции __next__

    def __len__(self):
        return len(self.coordinates)
    
    def __iter__(self):
#        return iter(self.coordinates) 
        self.it = 0
        return self

    def __next__(self):
        t = self.it
        self.it += 1
        if t >= len(self.coordinates):
            raise StopIteration
        return self.coordinates[t] 

    def __getitem__(self, key):
        return self.coordinates[key]
    
    @staticmethod
    def sum(first, second):
        if(len(first) != len(second)):
            raise ValueError("невозможно сложить")
        temp = Vector()
        for i in range(len(first)): 
            temp.coordinates.append(first[i] + second[i])
        return temp

    @staticmethod
    def sub(first, second):
        if(len(first) != len(second)):
            raise ValueError("невозможно вычесть")
        temp = Vector()
        for i in range(len(first)):
            temp.coordinates.append(first[i] - second[i])
        return temp

    @staticmethod
    def mul(vector, c):
        temp = Vector() 
        for i in vector:
           temp.coordinates.append(i * c)  
        return temp

    @staticmethod
    def scalMul(first, second):
        if(len(first) != len(second)):
            raise ValueError("невозможно перемножить")
        result = 0
        for i in range(len(first)):
            result += first[i]*second[i]
        return result 

    @staticmethod
    def comp(first, second):
        if(len(first) != len(second)):
            raise ValueError("невозможно сравнить")
        if Vector.length(Vector.sub(first, second)) == 0:
            return True
        return False
         
    @staticmethod
    def length(vector):
        result = 0
        for i in vector:
            result += i**2
        return result**(1/2) 

    @staticmethod
    def toString(vector):
        return "({0})".format(', '.join(str(num) for num in vector))

    def getItemAt(self, index):
        return self.coordinates[index]
if __name__ == '__main__':
    a = Vector(2,3,4,5,6)        
    b = Vector(2,3,4,5,6)
    c = Vector(2,3,4)
    print(Vector.toString(Vector.sum(a,b)))
    print(Vector.toString(Vector.sub(a,b)))
    print(Vector.length(a))
    print(a.getItemAt(3))
    print(Vector.scalMul(a,b))
    print(Vector.toString(Vector.mul(a, 5)))
    print(Vector.comp(a,b))
    print(Vector.sum(a,c))