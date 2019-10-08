keycode=input("What is your keycode?")
keylist=("dog4","cat5","horse10","1234","4321")

if keycode in keylist:
    message="Login Successful"
else:
    message="Login Failed"
print(f"{message}")
