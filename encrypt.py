from random import randint

class Encrypt:
    def __init__(self, data, pin):
        self.data = list(data)
        self.pin = pin
        self.ceaser = []
        
    def build(self):
        len_pre = (int(self.pin[0]) + int(self.pin[2])) \
        if (int(self.pin[0]) + int(self.pin[2])) else 4
        len_app = (int(self.pin[1]) + int(self.pin[2])) \
        if (int(self.pin[1]) + int(self.pin[2])) else 4
        
        swap = self.data[::2] + self.data[1::2]
        swap.reverse()    
        shift = int(self.pin[3]) if int(self.pin[3]) else 5
        for pos, char in enumerate(swap):
            origin = ord(char)
            if pos%2 == 0:
                new = chr((((origin-33+shift)%93)+33))
            else:
                new = chr((((origin-33-shift)%93)+33))
            self.ceaser.append(new)
        for _prepend in range(len_pre):
            insert_chr = chr(randint(33, 126))
            self.ceaser.insert(0, insert_chr)            
        for _append in range(len_app):
            insert_chr = chr(randint(33, 126))
            self.ceaser.append(insert_chr)
        return ''.join(self.ceaser)

    def __str__(self):
        printable = ''.join(self.ceaser)
        return printable
        
class Decrypt:
    def __init__(self, data, pin):
        self.data = data
        self.pin = pin
        self.ceaser = []
        
    def restore(self):
        len_pre = (int(self.pin[0]) + int(self.pin[2])) \
        if (int(self.pin[0]) + int(self.pin[2])) else 4
        len_app = (int(self.pin[1]) + int(self.pin[2])) \
        if (int(self.pin[1]) + int(self.pin[2])) else 4
                
        
        shift = int(self.pin[3]) if int(self.pin[3]) else 5
        stripped = self.data[len_pre:len_app*-1]
        for pos, char in enumerate(stripped):
            origin = ord(char)
            if pos%2 == 0:
                new = chr((((origin-33-shift)%93)+33))
            else:
                new = chr((((origin-33+shift)%93)+33))
            self.ceaser.append(new)
        self.ceaser.reverse()
        password = ['' for _ in self.ceaser]
        first_half = (len(password)/2)+(len(password)%2)
        for char_pos in range(first_half):
            password[char_pos*2] = self.ceaser[char_pos]
        for char_pos in range(len(password)-first_half):
            password[(char_pos*2)+1] = self.ceaser[first_half+char_pos]
        return password

def test():
    for _ in range(100000):        
        password = ''
        for l in range(randint(5,15)):
            password += chr(randint(34,125))
        pin = str(randint(1000, 9999))
        print _, password, pin, 
        e = Encrypt(password, pin)
        x = e.build()
        d = Decrypt(x, pin)
        a = d.restore()
        if ''.join(a) == password: 
            print True
        else:
            print False
            print a
            break

def manual_test():
    pin = '2757'
    e = Encrypt('Mygirls', pin)
    x = e.build()
    print x
    d = Decrypt(x, pin)
    a = d.restore()
    print a
    

manual_test()