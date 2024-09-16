#Strings are immutable
a = "Harshit!!!!" 
print(len(a))
print(a.upper()) # Creats a new string and print it in UPPERCASE
print(a.lower()) #Creats a new string and prints it in lowercase
print(a.rstrip()) #Creats a new string and strips the trailing characters
print(a.replace("Harry", "John")) #Creats a new string and replaces the occurence of the string with another string
print(a.split("  ")) #Creats a new string and splits the given string at the specified instance
print(a.count("Harshit")) #Tells the no of times the given string is occuring

blogHeading = "introduction tO Chess"
print(blogHeading.capitalize()) #Creats a new string and capitalizes the first letter and lowercases all the other letters
str1 = "!!!!Welcome to the console!!!!"
print(str1.center(50)) #It will create a new string and add spaces to center the string
print(str1.endswith("!!!!"))#Answers in true or false if the variable ends with a given string
print(str1.startswith("!!!!"))#Answers in true only if the variable starts with a given string

str2 = "He's name is Dan. He is an honest man."
print(str2.find("is")) # prints the index of the occurence of the given string
#print(str2.index("ishh")) #prints an error if the given string is not present
print(str2.isalnum()) #It returns true only if the entire string consistsof A-Z,a-z and 0-9.Otherwise it will return false
print(str2.isalpha()) #It returns true only if the entire string consistsof A-Z,a-z.Otherwise it will return false
print(str2.islower()) #It returns true only if the entire string is in lowercase
print(str2.isupper()) #It returns true only if the entire string is in UPPERCASE
print(str2.isprintable()) #It returns true only if the entire string is printable
print(str2.isspace()) #It returns true only if the entire string is in white space using spaces ot tabs
print(str2.istitle()) #It returns true only if the first letter of each word in string is capitalized
print(str2.istitle()) #It returns true only if the first letter of each word in string is capitalized
print(str2.swapcase()) #It comverts uppercase to lowercase and lowercase to uppercase.
print(str2.title()) #It converts the whole string into title.
