a = int(input("Enter total number of bananas: "))
l = int(input("Enter total distance to be travelled: "))
s = 0 #bananas consumed

while (a>l):
	n = (a/l)*2-1
	x = l//n
	s = s+x
	a = a-l

kmsleft = a-s
bananasNeeded = kmsleft
bananasLeft = a-bananasNeeded
print(bananasLeft)
