'''15.	For the following text:
I completely agree with you
write a program that calculates and displays the number of letters in each word. 
Use the map() and an anonymous functions to calculate the number of letters. 
Tip: to split text into words, use the split() function.
'''


x="I completely agree with you"

y=list(map(lambda w:len(w), x.split()))
print(y)