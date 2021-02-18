print("Hello, pleace input what you want to do: R for Read or W for Write")
word = input("Input here: ")

if word == "R":
    large = open("D:\Computing stuff\Challenges\BigBoi212.txt", "r")
    print(large.read())
    large.close()

elif word == "W":
    newWords = input("Input the new text: ")
    small = open("D:\Computing stuff\Challenges\BigBoi212.txt", "wt")
    small.write(newWords)
    small.close()

