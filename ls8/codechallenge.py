# Given the following array of values, print out all the elements in reverse order, with each element on a new line.
# For example, given the list
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# Your output should be
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process 

new_arr= [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
lines = [i for i in new_arr]
new_arr.reverse()
[print(i) for i in new_arr]
#UPER
#Printing out the Array in reverse
#Look up python reverse in dictionary
# arr [ numbers in array]
#print
#use reverse method
dict = {
  14: "vs code",
  3: "window",
  9: "alloc",
  26: "views",
  4: "bottle",
  15: "inbox",
  79: "widescreen",
  16: "coffee",
  19: "tissue",
}

dict.keys()
sorted(dict.keys())
for key in sorted(dict.keys()) :

    print(key , " :: " , dict[key])

    #can print it in order but need to reverse
  





