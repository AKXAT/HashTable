class HashTable:
    def __init__(self):
        self.max = 100 #for initiating 100 sized list 
        self.arr =[None for i in range(self.max)]
    def hash_key(self,key): # funtion for finding the hash key using ASCII 
        h = 0 # this is varialbe for saving the sum
        for char in key:
            h += ord(char) #ord - will convert each character in the key to the ASCII value 
        #print(h%self.max)
        return h % self.max # assuming that 100 will the size of the list so we are calculating mod using 100
    def add(self,key,value):
        h = self.hash_key(key)
        self.arr[h]= value
    def get(self,key):
        h = self.hash_key(key)
        #print(self.arr[h])
        return self.arr[h]
        
if __name__ == '__main__':
    t = HashTable() 
    t.hash_key('march 6')
    t.add('march 6',310)
    t.get('march 6')
