def linear_search(list, element):
        searched_block=enumerate(list)
        for position, item in searched_block:
                if item == element:
                        print position
                        return
        print "%s not in list." % element 
        a=type(element)

linear_search([0,1,4,'a',-4],7)
