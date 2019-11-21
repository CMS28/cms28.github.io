# open file
f = open("die4.txt","rb") #b binary mode
t = open("mycopy.png","wb") #binary mode

# read file
content = "this is to write"
t.write(f.read())  # binary mode byte

# close file
f.close()
t.close()