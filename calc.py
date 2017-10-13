print "please input the first number"
fnum = raw_input()
print "please input the second number"
snum = raw_input()
print "please input the operator"
opt = raw_input()
if opt=="+":
	result = int(fnum) + int(snum)
elif opt == "-":
	result = int (fnum) -int(snum)
elif opt == "*":
	result =int(fnum)*int(snum)
elif opt =="/":
	result = int(fnum)/int(snum)
else:
	result ="error"
print"the result is",result
