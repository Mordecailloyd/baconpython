def linear_search(list, element):
        searched_block=enumerate(list)
        for position, item in searched_block:
                if item == element:
                        print position
                        return
        print "%s not in list." % element 
        a=type(element)

linear_search([0,1,4,'a',-4,[7,'a',-4,5,90]],7)


def bin_search(find, items, low=0, high=None):
	if high is None:
		high= len(items)
	else:
		high = high
	position = low + (high - low) / len(items)
#    position = (high - low) // 2 + low
	if position =len(items):
		return False
    if low == high:
        return False
    if find == items[position]:
        return position
    elif find > items[position]:
    	position+=1
        return bin_search(items, find, low=(position), high)
    elif find < items[position]:
        return bin_search(items, find, low=low, high=position)

