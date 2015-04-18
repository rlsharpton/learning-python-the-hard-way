while True:
	response = raw_input()
	if int(response) % 7 == 0:
		break
	else:
		print "not divisable by 7 try again."

print "all done"