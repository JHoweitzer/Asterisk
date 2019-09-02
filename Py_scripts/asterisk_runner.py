import os
import os.path

welcomeString = "Hello user! Welcome to a text adventure game!"

if os.path.exists("../Save_Files"):
    print("Welcome back!")
else:
    try:
        os.mkdir("../Save_Files")
    except OSError:
        print("File initialization failed")
    else:
        print(welcomeString)