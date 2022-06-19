# Every time a month number is passed, we check if it's less than or
# equal to 12 and if it's not, we add 3 to the month and decrease the
# counter by 1. The final value of the counter will be the quadrant
# in which the month is located.
#
# This is backed by the idea that, whatever month number is passed,
# when we add 3 to it, we will, eventually, reach 12. Since the
# year can be divided into 4 quadrants, each with 3 months, we need
# 4 iterations to reach a number greater than or equal to 12 for the
# first quadrant (count will be 5-4=1), 3 iterations for the second 
# quadrant (5-3=2), 2 to the third one (5-2=3) and 1 to the fourth
# (5-1=4)
count=5
month = int(input("> "))
while month <= 12:
    month+=3
    count-=1
print(f'Quadrant: {count}')

# This is "kind of" cheating, but it does the trick in O(1) time,
# considering we don't need to iterate through all of the Dictionary
# indices to find in which quadrand the month is.
#maq={1:1, 2:1, 3:1, 4:2, 5:2, 6:2, 7:3, 8:3, 9:3, 10:4, 11:4, 12:4}
#month = int(input("> "))
#print(f'Quadrant: {maq[month]}')
