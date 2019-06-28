import random
letters = ['O', 'r', 'a', 'n', 'g', 'e', ' ', 'M', 'e', 't', 'h', 'o', 'd']
def create_string():
    str = ""
    for i in letters:
        str += i
    return str
print(create_string())

def fill_ticket():
    li = []
    for x in range(0,5):
        num = int(input("Enter a number: "))
        li.append(num)
    return li

def matches(ticket, winners):
    total = 0
    for x in range(min(len(ticket), len(winners))):
        if(ticket[x]==winners[x]):
            total+=1
    return total

guesses = fill_ticket()
winners = [1,2,3,4,5]

print(matches(guesses,winners))

def caesar_cipher(st):
    newstr = ''
    cipher_key = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w',
                  'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g',
                  'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm'}
    for x in range(0,len(st)):
        if cipher_key.get(st[x]) != None:
            newstr += str(cipher_key.get(st[x]))
        else:
            newstr += st[x]
    return newstr

print(caesar_cipher("pnrfne pvcure? v zhpu cersre pnrfne fnynq!"))

def guess():
    boolean = True
    num = random.randint(1,20)
    while(boolean):
        user = int(input("What is your guess? "))

        if num == user:
            print("That's right!")
            boolean = False
        else:
            print("Nope")

guess()

def creditlimit():
    balance = int(input("Enter Account Balance: "))
    while(balance > 0):
        spent = int(input("Enter Amount spent: "))
        balance -= spent
        print("Amount Left: " + str(balance))
    print("All out of money!")
creditlimit()

def pig_latin(pig):










