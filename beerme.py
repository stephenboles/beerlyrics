for x in range (99,0,-1):
	print ""
	if x > 1:
		print "%x bottles of beer on the wall" %(x)
	if x == 1:
		print "%x bottle of beer on the wall" %(x)
	if x<1:
		break
print ""
print "No more bottles of beer on the wall"
