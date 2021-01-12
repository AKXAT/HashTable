class HashTable:
    def __init__(self):
        self.max = 100 #for initiating 100 sized list 
        self.arr =[ [] for i in range(self.max)]
    def hash_key(self,key): # funtion for finding the hash key using ASCII 
        h = 0 # this is varialbe for saving the sum
        for char in key:
            h += ord(char) #ord - will convert each character in the key to the ASCII value 
        #print(h%self.max)
        return h % self.max # assuming that 100 will the size of the list so we are calculating mod using 100
    def add(self,key,value):
        h = self.hash_key(key)
        found = False
        for idx,element in enumerate(self.arr[h]):
            if element[0]== key and len(element) == 2:
                self.arr[h][idx] = (key,value)
                found = True 
                break
        if not found:
            self.arr[h].append((key,value))
    def get(self,key):
        h = self.hash_key(key)
        for each in self.arr[h]:
            if each[0] == key:
                #print(each[1]) 
                return each[1]
        
if __name__ == '__main__':
    t = HashTable() 
    t.add('march 6',310)
    t.add('march 17',400)
    t.add('march 6',489)
    t.get('march 6')
