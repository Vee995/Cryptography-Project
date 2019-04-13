#student number 214539347
#Project_Main.py

import string
import math
import sys
from pyperclip import copy

#Global use
#List for Caesar cipher use
Assigned_List = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", 
        " ", "!", "?", ":", ";", ",", ".", "-", "(", ")"]

#Vigenere cipher use
Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
shift = 1
matrix = [ Alphabet[(i + shift) % 26] for i in range(len(Alphabet)) ] #["B","C","D","E"......."Z","A"]


#Vigenere Cryptanalysis use
vig_Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

#dictionary with coressponding frequency for each letter in the Alphabet
relative_Frequencies=  { "a": 8.167, "b": 1.492, "c": 2.782, "d": 4.253, "e": 12.702, "f": 2.228, "g": 2.015, "h":6.094,
                         "i": 6.966, "j": 0.153, "k": 0.772, "l": 4.025, "m": 2.406, "n": 6.749, "o":7.507, "p":1.929,
                         "q": 0.095, "r": 5.987, "s": 6.327, "t": 9.056,  "u": 2.758, "v": 0.978, "w": 2.360, "x": 0.150,
                         "y": 1.974, "z": 0.074  }




def Caesar_Encryption(plaintext,key):
    ciphertext=""
    
    for letter in plaintext:
        
        if(letter in Assigned_List):
            char=Assigned_List.index(letter)+1 # get the index of the character
            enc_Formula=((char+int(key))%(len(Assigned_List)))-1 #formula for encryption
            ciphertext+=(Assigned_List[enc_Formula])
            
        else:
            ciphertext+=letter
                
    return ciphertext



def Caesar_Decryption(ciphertext,key):
    plaintext=""
    
    for letter in ciphertext:
        
        if(letter in Assigned_List):
            char=Assigned_List.index(letter)+1 # get the index of the character
            dec_Formula=((char-int(key))%(len(Assigned_List)))-1 #formula for decryption
            plaintext+=(Assigned_List[dec_Formula])
            
        else:
            plaintext+=letter  #Accounts for any characters that are not in the Assigned_List
            
                
    return plaintext
    
    
    
def Vigenere_Encryption(key):
    ciphertext = []
    check = 0     
    
    with open("Encryption.txt") as fileobj: 
        for line in fileobj: 
            print("\nPlainText:" ,line)
            for char in line.upper(): # each character value in the textfile 
                if char not in Alphabet: 
                    ciphertext.append(char)
                    continue
                else:
                    if char not in Alphabet:  #Accounts for any characters which are not in the Vigenere Alphabet
                        ciphertext.append(char)
                        continue
                    else:
                        if (check % len(key) == 0):
                            check = 0 
                        else:
                            check                    
        
                    resulting_Position = (Alphabet.find(char) + matrix.index(key[check])) % 26 #Calculation of the position
                                                                                               #find() will determine if the letter occurs in Alphabet-index returned
                    
                    ciphertext.append(matrix[resulting_Position]) #symbol added to ciphertext
                                                                  #including special symbols and numbers
                    check += 1
        
            return ciphertext      
    
  
    
def Vigenere_Decryption(key):
    plaintext = [] 
    check = 0
    
    with open("Vigenere_decryption.txt") as fileobj: 
        for line in fileobj:  
            print("\nCipherText:" ,line)
            for char in line: #each character value in the textfile  
                
                if char not in Alphabet: 
                    plaintext.append(char)
                    continue
                else:
                    
                    if (check % len(key) == 0):
                        check = 0 
                    else:
                        check
        
                    resulting_Position = (matrix.index(char) - matrix.index(key[check])) % 26 #Calculation of the position 
        
                    plaintext.append(Alphabet[resulting_Position]) #symbol added to plaintext
                    check += 1
            
        
            return plaintext    
        

def Caesar_Cryptanalysis(plaintext):
    Lowercase_text=plaintext.lower()
    match_score=0
    Dictionary=""
    
    text=Lowercase_text.split(" ") #text split by space and added to a list
    
    with open("dictionary.txt") as fileobj: #textfile which contains 100 of the most common words used in the english language 
        for line in fileobj:
            Dictionary+=line
            Lowercase_Dictionary=Dictionary.lower()
            words=Lowercase_Dictionary.split("\n") #Dictionary words added to a list called words
    
    for i in words: # Words in the plaintext will be checked if it's in the dictionary(ie:list which dictionary words were added) 
        if (i in text):
            match_score+=1  #A match_score is given for all matched words
            
    return match_score       
    
    
 
#Functions related to Vignenere Cryptanalysis below
#Using Kasiski Examination

def sequence_shift(sequence, val): #takes the letters from vig_Alphabet and it's index and apply specific shift 
    val= val % len(sequence)
    return sequence[val:] + sequence[:val] 

#sequence_shift output will look like this when called by Vig_decrypt_Cryptanalysis,sample of some the first few lines:
'''Shift is: ['S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']
   Shift is: ['M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
   Shift is: ['U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
'''

def Word_Distance(ciphertext): # Goes through the ciphertext and returns a list of the distance between matching words(trigrams and higher)
    distanceList = []

    while(len(distanceList)<10):

        for i in range(3,6): #Checks for matches from 3 to 6

            for j in range(len(ciphertext)-i):

                word = ciphertext[j:j+i]
                index = ciphertext.find(word,j+i)

                if(index!=-1):
                    distanceList.append(index-j)  

    return distanceList



def Frequency(ciphertext):
    Frequency_Dict = {key:0  for key in relative_Frequencies.keys()}
    Sum = 0
    shift=0
    lower=0

    for letter in ciphertext:
        Frequency_Dict[letter.lower()] += 1
        Sum += 1
        
    for key in Frequency_Dict.keys():
        Frequency_Dict[key] = Frequency_Dict[key]/Sum


    score = [0 for i in range(26)] #A comparison is done between Frequency_Dict to relative_Frequencies to determine number of shifts
    
    values = [0 for i in range(26)]

    while(shift < 26):
        index = 0
        for key in relative_Frequencies.keys():
            value = Frequency_Dict[vig_Alphabet[(shift+index)%26].lower()]

            values[index] = abs(value-relative_Frequencies[key])
            index += 1

        for counter in range(26):
            score[shift] += values[(counter+1)%26]+values[counter]+values[counter-1]

        if(score[shift] < score[lower]):
            lower = shift
        shift += 1
        
    return lower



#Form strings from the ciphertext of the letters that have been encrypted by the same subkey
#Returns every nth letter for each keyLength set of letters in ciphertext
def nthLetters(factor, substring): 
    result = []
    sub = ""
    for repeat in range (factor):
        index = repeat
        
        while index < len(substring):
            sub += substring[index]
            index += factor
            
        result.append(sub)
    return result



def Sub_Seq(l, s):
    m = s[l:]
    i = -1
    while(m):
        yield m #return a generator
        m = s[l:i]
        i -= 1
          

def resetFrequencies(): #Divides each letter frequency value by the sum of all the frequency values, ie percentage contribution to total 
    freq_total = 0
    
    for k in relative_Frequencies.keys(): #Totals values
        freq_total += relative_Frequencies[k]
        
    for key in relative_Frequencies.keys():
        relative_Frequencies[key] = relative_Frequencies[key]/freq_total # for each key in the list-get the value of it to the value divided by the total value


def Key_Length(ciphertext): # Analysing patterns and distances between patterns in ciphertext
    length = 3 
    distanceList = Word_Distance(ciphertext) 
    factors = {key:0 for key in range(3,27)} #Determine the factors

    for i in distanceList:

        for j in range(26,2,-1):

            if(i % j == 0):
                factors[j] += 1

    for keys in factors.keys(): #Determine key length 

        if(factors[keys] > factors[length]): #if the frequency of the key in the factors list is more than the current length, then length is updated
            length = keys

    GCD = math.gcd(distanceList[0] , math.gcd(distanceList[1],math.gcd(distanceList[2], math.gcd(distanceList[3],distanceList[4])))) #Finds the GCD of the first, and the combination of the next 3, 
                                                                                                                                      #than in turn is calculated the same as the gcd between itself 
                                                                                                                                      #and the next 2

    if(GCD<=26 and GCD>length):
        length = GCD
        
    return length



def Vig_Examination(ciphertext):
    key_value=""
    cipherNpSpace = ciphertext.replace(" ","")
    
    length = Key_Length(cipherNpSpace) #Get the Key length
    
    matrix = [[" " for l in range(length)]for k in range(int(len(ciphertext)/length))]
    
    originalLength = len(cipherNpSpace)
    
    for v in range(int(originalLength/length)): 
        for w in range(length):
                matrix[v][w] = cipherNpSpace[w] #sets this matrix value to the character at the index of w of the ciphertext with no spaces
        cipherNpSpace = cipherNpSpace[length:]
        
    
    for item in range(length):
        s = ""
        for rows in range(int(originalLength/length)):
            s += matrix[rows][item]
        key_value += vig_Alphabet[Frequency(s)]
     
    return key_value

 
 
def Vig_decrypt_Cryptanalysis (ciphertext, key): #Decipher the Ciphertext and return the message
    key = key.upper() #Key must be in all CAPS
    plaintext = ""
    count = 0
    
    for index in range(len(ciphertext)):
        
        if (ciphertext[index] == ' '): #need to check if ciphertext index is a space and increment count
            plaintext += ' '
            count += 1
            
        else:          
            col = ciphertext[index] #column is the index letter of the ciphertext
            row = key[(index-count)%len(key)]  #row is the index of the col letter % key length (character is part of the key)
            
            queueL = sequence_shift(vig_Alphabet, vig_Alphabet.index(row))
            
            plaintext += vig_Alphabet[queueL.index(col)] # gets the character from the vig_Alphabet at that index
    print("\nKey : ", key)
    
    file1 = open("[214539347_[Vigenere_break].txt","w") #Plaintext is written to a textfile along with the key
    file1.write("Key : ")
    file1.write(key)
    file1.write("\n")
    file1.write(plaintext)
    file1.close()          
    
    return plaintext


def testKeys(possibleKeysList, ciphertext):
    keyTest = ""
    for key in possibleKeysList:
        keyTest += (Vig_decrypt_Cryptanalysis(ciphertext, key))
        
    return keyTest 


#Kasiski used to break Vigenere Ciphertext 
def Vigenere_Cryptanalysis (ciphertext): 
    plaintext = ""  
    Possible_Keys = []
    
    for i in ciphertext:
        if (ciphertext == ""):
            cipherNoSpace = ciphertext.replace(" ", "") #replace ciphertext character with a space now with no space
            
            substring = longestRepetitiveSubstring(cipherNoSpace) #get the longest substring found
            
            nthLetterList = nthLetters(substring[1], substring[0])
            
            return (nthLetterList)
             
        resetFrequencies()
        
        
        Possible_Keys.append(Vig_Examination(ciphertext))
        
        keyVal = testKeys(Possible_Keys, ciphertext) #get the Key used
        
        plaintext += keyVal #key is added to the plaintext and returned 
        
        return (plaintext)    
    


def processInput(screen, inputLine):
    
    if screen == 0:
        if inputLine == 1:
            print("\nCaesar Cipher Options: " + "\n----------------------")
            print("\n1.Encrytion" + "\n2.Decryption" + "\n3.Cryptanalysis")
            return 1
        elif inputLine == 2:
            print("\nVigenere Cipher Options: " + "\n------------------------")
            print("\n1.Encrytion" + "\n2.Decryption" + "\n3.Cryptanalysis")
            return 2
        elif inputLine == 3:
            exitProgram()
    elif screen == 1:
        if inputLine == 1:
            plaintext=""
            print("\nKey being used : 17")
            key=17 #10 + 7 (214539347)
            
            with open("Encryption.txt") as fileobj: #Opening the textfile with the plaintext
        
                for line in fileobj:  
                    for char in line: #each character value in the textfile
                        plaintext+=char 
                        
                    print("\nPlaintext : ",plaintext,end="")
                    print("\n")            
                    result=Caesar_Encryption(plaintext,key)
            print("Ciphertext :",result,end="") 
            print("\n")
            
            file1 = open("[214539347]_[Caesar_encrypt].txt","w")
            file1.write(result)
            file1.close()     
            
            copy(result) #copy to clipboard
            
            print("\nCaesar Cipher Options: " + "\n----------------------")
            print("\n1.Encrytion" + "\n2.Decryption" + "\n3.Cryptanalysis" + "\n4.Back")
            return 1            
        elif inputLine == 2:
            ciphertext=""
            print("\nKey being used: 14")
            key=14
            
            with open("Caear_decryption.txt") as fileobj: #Opening the textfile with the ciphertext
        
                for line in fileobj:  
                    for char in line: #each character value in the textfile
                        ciphertext+=char 
                    print("\nCiphertext : ",ciphertext,end="")
                    print("\n")    
                    result=Caesar_Decryption(ciphertext,key)
                print("Plaintext :",result,end="")  
                print("\n")
        
            #plaintext is written to a new file
            file1 = open("[214539347]_[Caesar_decrypt].txt","w")
            file1.write(result)
            file1.close()  
            
            copy(result) #copy to clipboard
            print("\nCaesar Cipher Options: " + "\n----------------------")
            print("\n1.Encrytion" + "\n2.Decryption" + "\n3.Cryptanalysis" + "\n4.Back")
            return 1
        elif inputLine == 3:
            ciphertext=""
            score_List=[]
            with open("Caesar_break.txt") as fileobj: #Opening the textfile with the ciphertext
                    
                            for line in fileobj:  
                                for char in line: #each character value in the textfile
                                    ciphertext+=char 
                                print("\nCiphertext : ",ciphertext,end="")
                                print("\n") 
                                for key in range(1,len(Assigned_List)):
                                    result=Caesar_Decryption(ciphertext,key) #Brute force,going through every key 
                                    word_match=Caesar_Cryptanalysis(result) #and return a match score from the Caesar_Cryptanalysis()
                                    
                                    score_List.append(word_match) #scores are added to a list
                                max_Score=max(score_List) #the highest score ie: score which had the most matches
                                if(max_Score>=10):
                                    decoded=score_List.index(max_Score)+1 #index value of that score
                                    print("Key : ", decoded)
                                    message=Caesar_Decryption(ciphertext,decoded) #decrypt the message with the key found
                                    print("\nPlaintext :",message,end="")  
                                    print("\n")
                                    
                                
                                    #plaintext and key are written to a new file
                                    file1 = open("[214539347_[Caesar_break].txt","w")
                                    file1.write(message)
                                    file1.write("\nKey:")
                                    file1.write(str(decoded))
                                    
                                    file1.close()              
                        
                                    copy(message) #copy to clipboard  
                                    print("\nCaesar Cipher Options: " + "\n----------------------")
            print("\n1.Encrytion" + "\n2.Decryption" + "\n3.Cryptanalysis" + "\n4.Back")
            return 1
        elif inputLine == 4:
            return(displayMenu())
    elif screen == 2:
        if inputLine == 1:
            print("\nKey being used: Verosha")
            key="Verosha"          #Key=Verosha
            key=key.upper()
            result=Vigenere_Encryption(key)
            r=''.join(result)
            print("\nCiphertext: {0}".format(''.join(result)))  #Letters from the List are merged
            print("\n")
            
            f=''.join(result)
            file1 = open("[214539347]_[Vigenere_encrypt].txt","w")
            file1.write(f)
            file1.close()    
            
            copy(r) #copy to clipboard
            print("\nVigenere Cipher Options: " + "\n------------------------")
            print("\n1.Encrytion" + "\n2.Decryption" + "\n3.Cryptanalysis" + "\n4.Back")
            return 2
        elif inputLine == 2:
            print("\nKey being used: Neuschwanstein")
            key="Neuschwanstein"
            key=key.upper()
            result=Vigenere_Decryption(key)
            r=''.join(result)
            print("\nPlaintext: {0}".format(''.join(result)))   
            
            f=''.join(result)
            file1 = open("[214539347]_[Vigenere_decrypt].txt","w")
            file1.write(f)
            file1.close()  
            
            copy(r) #copy to clipboard
            print("\nVigenere Cipher Options: " + "\n------------------------")
            print("\n1.Encrytion" + "\n2.Decryption" + "\n3.Cryptanalysis" + "\n4.Back")
            return 2
        elif inputLine == 3:
            ciphertext=""
            with open("Vigenere_break.txt") as fileobj: #Opening the textfile with the ciphertext
        
                for line in fileobj:  
                    for char in line: #each character value in the textfile
                        ciphertext+=char             
            print("\nciphertext :",ciphertext)
            result=(Vigenere_Cryptanalysis (ciphertext))
            
            print("\nplaintext :" , result)   
            print("\n")
            
            copy(result) #copy to clipboard
            print("\nVigenere Cipher Options: " + "\n------------------------")
            print("\n1.Encrytion" + "\n2.Decryption" + "\n3.Cryptanalysis" + "\n4.Back")
            return 2
        elif inputLine == 4:
            
            return(displayMenu())        
       
           

def displayMenu():
    print("\nMenu Options " + "\n-------------")
    print("\n1.Caesar Cipher" + "\n2.Vigenere Cipher " + "\n3.Exit")
    return 0

def exitProgram():
    sys.exit()
    
    
def main():
    
    menuInput = -1
    screen = 0  #0: Menu, 1:Caesar, 2:Vigenere
   
    
    displayMenu()
    while (True):
 
        menuInput = int(input("\nPlease make a selection : "))
        print("_____________________________________________________________________________________________________________________________")
        
        screen = processInput(screen, menuInput)     
    
    
main()