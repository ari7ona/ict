#ex1
def reverselu(a, b):
    keys = []
    for i,j in a.items():
        if j == b:
            keys.append(i)
    return keys
dict = {'Arizona':48, 'Louisiana':18}
print(reverselu(dict, 48))
print(reverselu(dict, 18))

#ex2
import random
def two_dice_roll():
    dice1 = random.randrange(6) + 1
    dice2 = random.randrange(6) + 1
    return dice1 + dice2
result_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
for turn in range(1000):
    result = two_dice_roll()
    result_dict[result] += 1
print("Total".rjust(16), "|", "Simulated".rjust(16), "|", "Expected".rjust(16))
for n in range(2, 13):
    sim_result = str("%.2f" % (result_dict[n] / 1000 * 100))
    if n <= 7:
        exp_result = str("%.2f" % ((n - 1) / 36 * 100))
    else:
        exp_result = str("%.2f" % ((12 - n + 1) / 36 * 100))
    print(str(n).rjust(16), "|", sim_result.rjust(16), "|", exp_result.rjust(16))
    
#ex3
inp = input()
alphabet = {
'1':['.',',','?','!',':'],
'2':['A','B','C'],
'3':['D','E','F'],
'4':['G','H','I'],
'5':['J','K','L'],
'6':['M','N','O'],
'7':['P','Q','R','S'],
'8':['T','U','V'],
'9':['W','X','Y','Z'],
'0':[' ']
}
for n in inp:
    n = n.upper()
    for i, j in alphabet.items():
        for k in j:
            if k == n:
                for t in range(j.index(n)+1):
                    print(i, end="")
          
#ex4
s = input()
alphabet = {'A': '.-', 'J' : '.---', 'S': '...',  '1' : '.---',
         'B': '-...' ,'K': '-.-', 'T' : '-', '2': '..--', 'C': '-.-.',
         'L': '.-..', 'U': '..-', '3': '...-', 'D': '-..', 'M' :'--',
         'V': '...-' ,'4': '....', 'E': '.', 'N': '-.', 'W': '.--',
         '5': '.....', 'F': '..-.', 'O':'---', 'X': '-..-', '6' : '-....',
         'G': '--.', 'P': '.--.', 'Y': '-.--', '7': '--...', 'H': '....', 'Q': '--.-',
         'Z': '--..', '8': '---..', 'I': '..', 'R':'.-.', '0': '-----', '9': '----.'}
for i in s:
    i = i.upper()
    if(i in dict1):
        print(dict1[i.upper()],end=' ')
           
#ex5
def index(s):
    if(len(s)!=6):
        return False
    ind = 1
    for i in s:
        if(ind % 2 == 1 and (i>='A' and i<='Z') == False):
            return False
        elif(ind % 2 == 0 and (i>='0' and i<='9') == False):
            return False
        ind += 1
    return True
province = {'A':'Newfoundland',
         'B':'Nova Scotia',
         'C':'Prince Edward Island',
         'E':'New Brunswick',
         'G':'Quebec',
         'H':'Quebec',
         'J':'Quebec',
         'K':'Ontario',
         'L':'Ontario',
         'M':'Ontario',
         'N':'Ontario',
         'P':'Ontario',
         'R':'Manitoba',
         'S':'Saskatchwan',
         'T':'Albertia',
         'V':'British Columbia',
         'X':'Nunavut',
         'X':'Northwest Territories',
         'Y':'Yukon'}
s = input()
if(index(s) == False):
    print("Wrong postal code")
else:
    if(s[1] == '0'): print("Rural", end=' ')
    else: print("Urban", end=' ')
    print("address in ", end='')
    print(province[s[0]])
        
#ex6
def n2w(s):
    if(len(s) > 3 or len(s) <= 0):
        return False
    for i in s:
        if((i>='0'and i<='9')==False):
            return False
    return True
single = {'0':'zero','1':'one', '2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
decimal = {'0':'','1':'ten','2':'twenty','3':'thirty','4':'forty','5':'fifty','6':'sixty','7':'seventy','8':'eighty','9':'ninety','11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen','17':'seventeen','18':'eighteen','19':'nineten'}
s = input()
con=True
if(n2w(s) == False):
    print("Wrong number")
else:
    i = 0
    n = len(s)
    if(n == 3):
        print(single[s[i]] + ' hundred ', end='')
        i+=1
    if(n >= 2):
        if s[i]+s[i+1] in decimal:
            con=False
            print(decimal[s[i]+s[i+1]])
        else:
            print(decimal[s[i]],end=' ')
        i+=1
    if(n >= 1):
        if(con):
            print(single[s[i]])
            
#ex7
s=input()
s=set(s)
print(len(s))

#ex8
def anagram(s1, s2):   
    if(sorted(s1)== sorted(s2)): 
        print("YES")  
    else: 
        print("NO")          
s1 = input()
s2 = input() 
anagram(s1, s2) 

#ex9
def anagram(s1, s2):
    if(sorted(s1)== sorted(s2)):
        print("YES")
    else:
        print("NO")
s1 = input()
s11 = set()
s2 = input()
s22 = set()
for i in s1:
    if i != ' ' and i != '!' and i != ',' and i != '.' and i != '?':
        s11.add(i)
for i in s1:
    if i  != ' ' and i != '!' and i != ',' and i != '.' and i != '?':
        s22.add(i)
anagram(s11, s22)

#ex10
s = input()
cnt = 0
scores = {1:['A','E','I','L','N','O','R','S','T','U'],
       2:['D','G'],
       3:['B','C','M','P'],
       4:['F','H','V','W','Y'],
       5:['K'],
       8:['J','X'],
       10:['Q','Z']}
for i in s:
    for j,k in scores.items():
        for l in k:
            if l == i:
                cnt += j
print(cnt)

#x11
