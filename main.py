import bcrypt

text = input('Text: ')



class Hash_Encryption():
    def __init__(self, salt):
        self.salt = salt
        self.abc = ['n', 'Z', 'c', ')', 'o', 'f', 'A', '*', '{', 'D', 'B', 'w', 'u', 'K', 'W', 'q', 'T', ']', 'd', 'e', '(', 'V', '/', '[', 'a', 'N', 'J', '^', 'E', 'm', 'y', 'F', 'S', ';', 'r', 'U', 'i', 'j', 'g', '0', '.', 'P', 'H', 'z', '<', '9', '`', 'x', '3', '5', 'C', '|', 'R', '+', '6', 'v', '@', '}', '&', '-', '~', 'b', 't', '4', '1', ':', 'k', 'L', '$', '>', '8', '7', '%', 'M', 'Y', 'X', 'I', 'O', '2', 'Q', 'h', 's', '?', 'l', 'p', 'G', "'"]
        self.charLength = int(len(self.abc) - 1)

    def check_letter(self, iL):
        for i, letter in enumerate(self.abc):
            if letter == iL:
                return i

    def encode(self, user_i):  
        user_i = user_i[::-1]        
        encoded = '' 
        for char in user_i:
            if char != ' ':
                index = self.check_letter(char)
                if int(index + 5) > self.charLength:
                    letter = self.abc[(int(index + 5) - self.charLength) - 1]
                else: 
                    letter = self.abc[int(index + 5)]
            else:
                letter = '_'
            encoded += str(letter)
        return encoded
            
            
    def decode(self, user_i):
        user_i = user_i[::-1]        
        decoded = '' 
        for char in user_i:
            if char != '_':
                index = self.check_letter(char)
                if int(index - 5) < 0:
                    letter = self.abc[(int(index - 5) + self.charLength) + 1]
                else: 
                    letter = self.abc[int(index - 5)]
            else:
                letter = ' '
            decoded += str(letter)
        return decoded
    
    
    
    def hashText(self, text):
        bcryptText = bytes(text, 'utf-8')
        hashed = bcrypt.hashpw(bcryptText, bcrypt.gensalt())
        
        return hashed

    def confirmHasedText(self,hash, text):
        bcryptText = bytes(text, 'utf-8')
        if bcrypt.checkpw(bcryptText, hash):
            return True
        return False

    def hack_and_encrypt(self,input):   
        hash = self.hashText(input)
        encoded = self.encode(hash.decode())
        
        return hash, encoded


    def crack(self, guess, encoded, hash):
        hash = self.decode(encoded)
        bcryptHash = bytes(hash, 'utf-8')
        check = self.confirmHasedText(bcryptHash, guess)
        return check


lockText = Hash_Encryption(19)
hash, encoded = lockText.hack_and_encrypt(text)


guess = 'hello'
output = lockText.crack(guess, encoded, hash)
print(output)


    
    
