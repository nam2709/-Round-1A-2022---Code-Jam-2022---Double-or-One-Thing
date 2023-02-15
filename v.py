T = int(input())
for g in range(1,T+1):
	S = input()
	a = str(S)+'0'
	list1=[]
	list1[:0]= a
	x = len(list1)
	list2 = []
	list5 = []
	# for t in list1:
	# 	print (t)
	# cach de lap lai tu dau dung them lenh while vi co dk
	for i in range(0,x-1):
		if list1[i] < list1[i+1]:
			e = 2
		elif list1[i] > list1[i+1]:
			e = 1
		elif list1[i] == list1[i+1]:
			j = 0
			while list1[i] == list1[i+j]:
				j += 1
				if list1[i] < list1[i+j]:
					e = 2
				elif list1[i] > list1[i+j]:
					e = 1

			# if list1[i] < list1[i+2]:
			# 	e = 2
			# elif list1[i] > list1[i+2]:
			# 	e = 1
			# elif list1[i] == list1[i+2]:
			# 	if list1[i] < list1[i+3]:
			# 		e = 2
			# 	elif list1[i] > list1[i+3]:
			# 		e = 1
			# 	elif list1[i] == list1[i+3]:
			# 		if list1[i] < list1[i+4]:
			# 			e = 2
			# 		elif list1[i] > list1[i+4]:
			# 			e = 1
			# 		elif list1[i] == list1[i+4]:
			# 			if list1[i] < list1[i+5]:
			# 				e = 2
			# 			elif list1[i] > list1[i+5]:
			# 				e = 1
			# 			elif list1[i] == list1[i+5]:
			# 				if list1[i] < list1[i+6]:
			# 					e = 2
			# 				elif list1[i] > list1[i+6]:
			# 					e = 1
			# 				elif list1[i] == list1[i+6]:
			# 					if list1[i] < list1[i+7]:
			# 						e = 2
			# 					elif list1[i] > list1[i+7]:
			# 						e = 1
			# 					elif list1[i] == list1[i+7]:
			# 						if list1[i] < list1[i+8]:
			# 							e = 2
			# 						elif list1[i] > list1[i+8]:
			# 							e = 1
			# 						elif list1[i] == list1[i+8]:
			# 							e = 1




		list2.append(list1[i]*e)
		list3= ''.join(list2) 

	print('Case #'+str(g)+': '+str(list3))

