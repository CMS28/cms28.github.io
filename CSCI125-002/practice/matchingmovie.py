# input -- read from file
f = open("topmovies.txt","r")
list1 = list(f)
g = open("topmoviesimdb.txt","r")
list2 = list(g)
t = open("movies.txt","w")
# procedure
count = 0
for movies in list1:
    if movies in list2:
        count = count + 1
        print(f"{movies} in both")
        t.write(movies)
print(f"{count} matches")
# close
f.close()
g.close()
t.close()