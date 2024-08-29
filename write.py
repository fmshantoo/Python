f = open("Thursday.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("Thursday.txt", "r")
print(f.read())
