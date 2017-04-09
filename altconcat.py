def linear_search(list, element):
        searched_block=enumerate(list)
        for position, item in searched_block:
                if item == element:
                        print position
                        return
        print "%s not in list." % element 
        a=type(element)

#linear_search([0,1,4,'a',-4,[7,'a',-4,5,90]],7)


#def bin_search(find, items )



def bin_search(find, items, low=0, high=None):
	if high is None:
		high= len(items)
	else:
		high = high
	position = low + (high - low) / len(items)
#    position = (high - low) // 2 + low
	if position ==len(items):
		return -1
	if low == high:
		return -1
	if find == items[position]:
		return position
	elif find > items[position]:
		position+=1
		return bin_search(find, items, position, high)
	elif find < items[position]:
		return bin_search(find, items, low, position)


def create_sum(dig_list,find,found_list=[]):
	#print "function called"
	#print dig_list
	#print found_list

	if len(dig_list)==0:
		if sum(found_list)==find:
			print sum(found_list)
			print found_list 
			print "Answer!"
		return
	undecided_value=dig_list.pop(0)
	neg_undecided_value=undecided_value*(-1)
	list_copy1=dig_list
	list_copy2=dig_list[:]
	found_list_copy1=found_list+[undecided_value]
	found_list_copy2=found_list+[neg_undecided_value]
	if len(dig_list)>0:
		concat_value=int(str(undecided_value)+str(dig_list[0]))
		list_copy3=[concat_value]+dig_list[1:]
		found_list_copy3=found_list[:]
		create_sum(list_copy3,find,found_list_copy3)
	create_sum(list_copy1,find,found_list_copy1)
	create_sum(list_copy2,find,found_list_copy2)



#create_sum([1,2,3,4,5,6,7,8,9],100)





def Binary_search(list,find,low=0,high=None):
	length=len(list)
	value = False
	if high is None:
		high=length
	half=((high - low)/2) + low 
	if list[half] == find:
		return half
	if (high-low) < 2:
		return "Value not found in list."
	if low == high:
		return "Value not found in list."
	if half == length:
		return "Value not found in list."		
	if list[half] > find:
		return Binary_search(list,find,low,half)
	if list[half] < find:
		return Binary_search(list,find,half,high)







list1=[1,2,3,4]
print Binary_search(list1,5)