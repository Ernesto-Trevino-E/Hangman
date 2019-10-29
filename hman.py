#My attempt at hang man
def wordVerify():
    checker=[]
    word=input('What word shall be guessed: ')
    
    while (word.isnumeric()):
        word=input('Please only write one word: ')
        
    checker+=word
    
    while ' ' in checker:
        checker=[]
        word=input('Only one word please: ')
        checker+=word
    if ' ' not in checker:
        return word

def BlankCopier(size):
    vector=[]
    count='_'
    for ir in range (size):
        vector.append(count)
    return vector

def shotfilter():
    shot=input('Guess one letter: ')
    while shot.isnumeric():
        shot=input('Only put one letter, no numbers: ')
    while len(shot)>1:
        shot=input('Please only slect one letter: ')
    return shot
    

def endgame(hman,saver):
    saver=[]
    print('ONE SHOT BB, EMINEM STYLE')
    print('G U E S S')
    gues=input('Guess: ')
    saver+=gues
    if saver==hman:
        print('You have saved us my boi.... all part of the plan :)')
        input('Enter to continue')
        main()
    elif saver!=hman:
        print('you like J A Z Z')
        input('Enter to continue.... and watch bee movie')
        main()
    

def game(hman,saver):
    lose=int(input('How many tries do you want?: '))
    print(saver)
    points=0
    while hman!=saver and lose!=0:
        cycle=1
        
        while cycle==1:
            endgamer=input('Do you wish to guess the entire word?<yes><no>: ')
            if endgamer=='no':
                cycle=0
            elif endgamer=='yes':
                endgame(hman,saver)
        
        tiro= shotfilter()
        
        if tiro in hman:
            points+=1
            for ir in range (len(saver)):
                if tiro == hman[ir]:
                    saver[ir]=tiro
            print('Goode guess')
            print(saver)
            
        elif tiro not in hman:
            lose=lose-1
            print(f'You have {lose} tries left')
            print(saver)
            
    if hman==saver:
        print('You did it, you beautiful bastard')
        input('<Enter to continue>')
        main()
    elif lose==0:
        print('Big Loss')
        input('<Enter to continue>')
        main()


def menu():
    return int(input('''
1.- Start Hangman
2.- What to do?
0.- Quit
Select option: '''))

def main():
    hman=[]
    saver=[]
    print('''Welcome to hangman, ya man... I need your help :(
It's very simple you see....

save me :)''')
    opcion=menu()
    
    while (opcion != 0):
        if (opcion == 1):
            word = wordVerify()
            hman+=word
            saver = BlankCopier(len(hman))
            game(hman,saver)
            
        if (opcion == 2):
            print('''It's very simple you see:
1.- When you click start, you will be promted to select a word
2.- A person who is not the guesser(s), types out a word(no spaces)
3.- When you input the word, the game begins,
you will be asked to guess the word
4.- You will input a single character and click enter to see if
its part of the word
5.- If the letter is in the word the postions will be revealed
6.- If it isn't I'll be one step closer to my demise
7.- Proceed until you save me or be the reason of my end.
8.- Before taking a guess, you will be asked if you wish to guess the
full word, this is a one shot opportunity
9.- Guessing the word will immediately win the game
10.- Failure to guess will mean BOTH of us being forced to watch
the bee movie until a trilogy is made.

GOOD LUCK
HAVE FUN ;)
''')
            input('<Enter to continue>')
            
        opcion=menu()
main()