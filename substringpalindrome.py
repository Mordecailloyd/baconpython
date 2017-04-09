
with open("C:\Users\Nicholas Bacon\Desktop\Simmons, Dan - Ilium - 01 - Ilium.txt",'r') as myfile:
    data=myfile.read().replace('\n', '')


#complete 
# def substring_palindrome(string):
# 	length=len(string)
# 	pointer = 0 
# 	long_substring=''
# #	index=length-pointer2
# 	while pointer <= length:
# 		pointer2=pointer + 2
# 		while pointer2 <= length:
# 			substring=string[pointer:pointer2]
# 			if ''.join(reversed(substring)) == substring:
# 				long_substring=substring
# 				print long_substring
# 			pointer2+=1
# 		pointer +=1
# 	print long_substring

# #substring_palindrome(data[:20000])
# substring_palindrome("racecar")


#longest/faster
def substring_palindrome(string):
	length=len(string)
	pointer=3
	long_substring=''
#	index=length-pointer2
	while pointer <= length:
		index=0
		if len(long_substring) < (pointer-3):
			break
		while (pointer+index) <= length:
			if is_palindrom(string,index,(pointer+index-1)):
				substring = string[(index):(pointer+index)]
				long_substring = substring
				print long_substring
			index+=1
		pointer +=1 
	print long_substring


def is_palindrom(string,index1,index2):
	length=((index2-index1+1)/2)
	pointer=0
	while pointer < length:
		if string[index1+pointer] != string[index2-pointer]:
			# print pointer
			# print string[index1+pointer]
			# print string[index2-pointer]
			return False
		pointer+=1
	return True

substring_palindrome(data)
#substring_palindrome("racecar")
#print is_palindrom("seques",0,5)