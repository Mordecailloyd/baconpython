def cls(): print "\n"* 75
def numsuffix(x):
    if x==1:
        return "1st"
    if x==2:
        return "2nd"
    if x==3:
        return "3rd"
    if x>3:
        return str(x)+"th"
def printmistake (x):
    suffix= " mistakes"
    if x==1:
        suffix= " mistake"
    print "You have made "+str(x)+ str(suffix) + "."

def printhangman(strikes):
    if strikes == 0:
        print """
_______
|     | 
|     
|    
|     
|   
|
|___________
        """
    if strikes == 1:
        print """
_______
|     | 
|     0
|    
|     
|    
|
|___________
        """
    if strikes == 2:
        print """
_______
|     | 
|     0
|     |
|     |
|     
|
|___________
"""
    if strikes == 3:
        print """
_______
|     | 
|     0
|    \|
|     |
|     
|
|___________
"""
    if strikes == 4:
        print """
_______
|     | 
|     0
|    \|/
|     |
|     
|
|___________

"""

    if strikes == 5:
       print """
_______
|     | 
|     0
|    \|/
|     |
|    / 
|
|___________
"""
    if strikes == 6:
       print """
_______
|     | 
|     0
|    \|/
|     |
|    / \\
|
|___________
"""

     
    

w=raw_input("What is your word?\n")
cls()
wordresp= ["_"for i in range(len(w)) ] 
numberlist=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth","eleventh",]
mistake=0
resp=0
correctresp=0
done=False
while not done:
    print wordresp
    Letter=raw_input("What is your " + numsuffix(resp+1) + " guess?\n")
    cls()
   
    resp=resp+1
    if len(Letter)==1:
        if Letter in w:
            print "success"
            printmistake (mistake)
            for i in range(len(w)):
                if w[i] == Letter:
                    wordresp[i]=Letter
                    correctresp +=1 
            if len(w)== correctresp:
                print "You have succesfully guessed \""  +w+ "\" in " + str(resp)+ " guesses."
                done=True
            
        else:
            mistake=mistake + 1
            print "FAILURE!"
            printmistake (mistake) 
            if mistake > 5:
                print "You have run out of guesses! Nice try!"
                print "The correct answer was " +str(w)+ "."
                done=True
            

            
    else:
        len(Letter)>1
        print "Guess only one letter at a time."

    printhangman(mistake) 


