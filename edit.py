import sys
fhand = open("text.txt", "r")
sys.stdout=open('edited.txt','w')
for line in fhand:
        word = line.split()
        per_line=5
        for i in range(0,len(word),per_line):
            print(" ".join(word[i:i+per_line]))
sys.stdout.close()