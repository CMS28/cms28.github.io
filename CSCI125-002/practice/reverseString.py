def reverseS(mystr):
    #base case
    if len(mystr)==1:
        return mystr
    #general case ---> smaller version
    else:
        #first = mystr[0]
        #return  reverseS(mystr[1:]) + first
        last = mystr[-1]
        return last + reverseS(mystr[:-1])

# test it
print(reverseS("greatjob"))


def reverseWL(wordlist):
    #base case
    if len(wordlist) <=1:
        return wordlist
    #general case
    else:
        first = wordlist[0]
        smallerlist = reverseWL(wordlist[1:])
        smallerlist.append(first)
        return smallerlist



#test function
strgs = "cat is running"
wlist = strg.split(" ")
print(reverseWL(wlist))
