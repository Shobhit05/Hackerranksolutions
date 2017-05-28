

class Cryptography:

    def __init__(self,a):
        self._a=a


    def _encode(self,message):
        self.encode=[0]*len(message)
        for i in range(0,len(message)):
            if message[i].isupper():
                self.encode[i]=(chr(int((ord(str(message[i]))-65+self._a)%26+65)))
            else:
                self.encode[i]=message[i]
        encrypt=''.join(self.encode)
        return encrypt

    

    def _decode(self,message1):
        self.decode=[0]*len(message1)
        for i in range(0,len(message1)):
            if message1[i].isupper():
                self.decode[i]=(chr(int(ord(str(message1[i]))-65-self._a)%26+65))
            else:
                self.decode[i]=message1[i]
        decrypt=''.join(self.decode)
        return decrypt


        
    
a=Cryptography(3)
coded=a._encode("THE EAGLE IS IN PLAY;MEET AT JOE'S.")
print coded
d=a._decode(coded)
print d


