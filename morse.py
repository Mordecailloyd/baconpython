from hastable import *

table=HashTable(100)


morse_dictionary={'a':'.- ','b':'-... ','c':'-.-. ','d':'-.. ','e':'. ','f':'..-. ','g':'--. ','h':'.... ','i':'.. ','j':'.--- ','k':'-.- ','l':'.-.. ','m':'-- ','n':'-. ','o':'--- ','p':'.--. ','q':'--.- ','r':'.-. ','s':'... ','t':'- ','u':'..- ','v':'...- ','w':'.-- ','x':'-..- ','y':'-.-- ','z':'--.. ','0':'----- ','1':'.---- ','2':'..--- ','3':'...-- ','4':'....- ','5':'..... ','6':'-.... ','7':'--... ','8':'---.. ','9':'----. ',' ':'.-.- ','.':'.-.-.- '}
#morse_dictionary2={'.-.- ': ' ', '..--- ': '2', '--. ': 'g', '----- ': '0', '.- ': 'a', '.--. ': 'p', '-.. ': 'd', '-- ': 'm', '-.-. ': 'c', '...-- ': '3', '...- ': 'v', '-.- ':'k', '---.. ': '8', '. ': 'e', '.... ': 'h', '--.- ': 'q', '.-. ': 'r', '-. ': 'n', '.--- ': 'j', '... ': 's', '.-.-.- ': '.', '.. ': 'i', '----. ': '9', '-...': 'b', '.-.. ': 'l', '....- ': '4', '--- ': 'o', '.---- ': '1', '..-. ': 'f', '..... ': '5', '- ': 't', '-.-- ': 'y', '..- ': 'u', '.-- ': 'w', '-.... ': '6','-..- ': 'x', '--... ': '7', '--.. ': 'z'}
morse_dictionary2 = {}

for key in morse_dictionary:
	morse_dictionary2[morse_dictionary[key]] = key

for key in morse_dictionary:
	table.insert(key,morse_dictionary[key])

for key in morse_dictionary2:
	table.insert(key,morse_dictionary2[key])



def morsify(text):
	morse_text = ''
	pointer=0
	text=text.lower()
	while pointer < len(text):
		morse_value=table.get(text[pointer])
		morse_text += str(morse_value)
		pointer+=1
	return morse_text


def englishify(morse):
	english_text = ''
	key_text = ''
	pointer=0
	while pointer < len(morse):
		key_text += morse[pointer]
		if morse[pointer] == ' ':
			english_value=table.get(key_text)
			english_text += english_value
			key_text = ''
		pointer +=1
	return english_text


a = morsify("Take me to your leader.")
#print a
print a
print englishify(a)


# def morsify(text):
# 	morse_text = ''
# 	pointer=0
# 	text=text.lower()
# 	while pointer < len(text):
# 		morse_value=morse_dictionary[text[pointer]]
# 		morse_text += morse_value
# 		pointer+=1
# 	return morse_text


# def englishify(morse):
# 	english_text = ''
# 	key_text = ''
# 	pointer=0
# 	while pointer < len(morse):
# 		key_text += morse[pointer]
# 		if morse[pointer] == ' ':
# 			morse_value=morse_dictionary2[key_text]
# 			english_text += morse_value
# 			key_text = ''
# 		pointer +=1
# 	return english_text
