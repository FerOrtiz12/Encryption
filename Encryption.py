# Description of Program: Encrypts and decrypts a string
print("Welcome to the program. This program generates a random 26 letter key that allows users \
to encypt text. It decrypts messages encrypted with the generated key, and allows users to see \
the key used to encrypt the text and change to another random or specified key.\n")
import random
LCLETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def isLegalKey( key ):
    # A key is legal if it has length 26 and contains all letters.
    # from LCLETTERS.
    return ( len(key) == 26 and all( [ ch in key for ch in LCLETTERS ] ) )

def makeRandomKey():
    # A legal random key is a permutation of LCLETTERS.
    lst = list( LCLETTERS )  # Turn string into list of letters
    random.shuffle( lst )    # Shuffle the list randomly
    return ''.join( lst )    # Assemble them back into a string
    

class SubstitutionCipher:
    def __init__ (self, key = makeRandomKey() ):
        if (isLegalKey(key)==True):
            self.__key = key
        else:
            return "Key entered is not legal"

    def getKey( self ):
        return self.__key

    def setKey( self, key ):
        if (isLegalKey(key)==True):
            self.__key = key
        else:
            return "Illegal key entered. Try again!"
        
    def encryptText( self, plaintext ):
        self.__plaintext=plaintext
        ciphertext=""
        for letters in self.__plaintext:
            if(letters in LCLETTERS):
                letter_number=LCLETTERS.find(letters)
                ciphertext+=self.__key[letter_number]
            elif(letters==" "):
                ciphertext+=" "
            elif(letters in UPPER):
                lower_letter=letters.lower()
                letter_number=LCLETTERS.find(lower_letter)
                encrypted_letter=self.__key[letter_number]
                ciphertext+=encrypted_letter.upper()
            else:
                ciphertext+=letters
        return ciphertext


    def decryptText( self, ciphertext ):
        self.__ciphertext=ciphertext
        plaintext=""
        for letters in self.__ciphertext:
            if(letters in self.__key):
                letter_number1=self.__key.find(letters)
                plaintext+=LCLETTERS[letter_number1]
            elif(letters==" "):
                plaintext+=" "
            elif(letters in UPPER):
                lower_letter1=letters.lower()
                letter_number1=self.__key.find(lower_letter1)
                desencrypted_letter=LCLETTERS[letter_number1]
                plaintext+=desencrypted_letter.upper()
            else:
                plaintext+=letters
        return plaintext

def main ():
    cipher = SubstitutionCipher()
    while (True):
        n=input("Enter a command (getKey, changeKey, encrypt, decrypt, quit): ")
        if (n.lower()=="quit"):
            print("Thanks for visiting!")
            break
        elif (n.lower()=="getkey"):
            print("  Current cipher key:", cipher.getKey())
        elif (n.lower()=="changekey"):
            m=input("  Enter a valid 26 letter key, 'random' for a random key, or 'quit' to quit: ")
            while (True):
                if(m.lower()=="random"):
                    cipher.setKey(makeRandomKey())
                    print("    New cipher key:", cipher.getKey())
                    break
                elif(isLegalKey(m)==True):
                    cipher.setKey(m)
                    print("    New cipher key:", cipher.getKey())
                    break
                elif (m.lower()=="quit"):
                    break
                else:
                    print("    Illegal key entered. Try again!")
                    m=input("  Enter a valid cipher key, 'random' for a random key, or 'quit' to quit: ")
                    continue
        elif(n.lower()=="encrypt"):
            plaintext=input("  Enter a text to encrypt: ")
            encrypted_text=cipher.encryptText(plaintext)
            print("    The encrypted text is:", encrypted_text)
        elif(n.lower()=="decrypt"):
            ciphertext=input("  Enter a text to decrypt: ")
            decrypted_text=cipher.decryptText(ciphertext)
            print("    The decrypted text is:", decrypted_text)
        else:
            print("  Command not recognized. Try again!")
            continue
    
main()
