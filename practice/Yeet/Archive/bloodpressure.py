def bp(readinglist):
    if str(readinglist) > str(180):
        print("Hypersensitive crisis. Seek Immediate Medical Attention!")
    elif str(readinglist) >= str(140) and str(readinglist) <= str(180):
        print("Hypertension Stage 2, You may want to seek medical attention.")
    elif str(readinglist) >= str(130) and str(readinglist) < str(140):
        print("Hypertension Stage 1, you may want to change your lifestyle")
    else:
        print("You Good Fam")
avg = (132 + 143 + 139 + 146 + 150 + 124)/6
print(avg)
print(bp(avg))
