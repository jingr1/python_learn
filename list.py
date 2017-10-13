numbers = [1,2,3,4,5,6]
even =[i for i in numbers if i%2==0]
double = [i*2 for i in numbers]
print double
print even

for i in numbers:
	if 6<i<7:
		break
	print i
else:
	print "false"
