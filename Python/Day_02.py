st1 = "krishna"
print(len(st1)) 
print(st1.upper())


st2 = "krishNa balAram"
print(st2.lower()) # lowers all letters of the string
print(st2.title()) # capitalises first letter of all words in the string
print(st2.capitalize()) # capitalises only first letter of first word
print(st2.swapcase()) # swaps current size of letters
print(st2.count('a')) # this is case sensitive as it will not include 'A'
print(st2.endswith('ram')) # returns TRUE if the last letters of last word end with given string 
print(st2.startswith('kris')) # returns TRUE if the first letters of initial word starts with given string 


st3 = "upflairs pvt ltd jaipur rajasthan"
print(st3.center(10,"*")) # justifies the string in center
print(st3.ljust(8 + 1, "*")) # justifies the string to the left
print(st3.rjust(8 + 1, "*")) #justifies the string to the right
print(st3.index("p",2,25)) # returns the index of first occurence of the substring in the given string and raises value-error if substring is not found in the string
print(st3.find("r")) # returns the index of first occurence of the substring in the given string and returns -1 if substring is not found in the string


st5 = "       upflairs pvt ltd          "
print(st5.strip()) # removes white spaces from left and right side of the string
print(st5)
print(st5.lstrip()) # removes white spaces from left
print(st5.rstrip()) # removes white spaces from right





















