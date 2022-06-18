# Python3 code to demonstrate median_grouped()

# importing median_grouped from
# the statistics module
freq = [7, 18, 25, 30, 20]
central_size= [2.5, 7.5, 12.5, 17.5, 22.5]
s = 0
for i in range(5):
    s+=freq[i]
    print("CF at "+str(central_size[i])+" = ", s)

s /= 2

med =  15 + ((s-s)/25) * 5
print("Since it lies in 15-20 class therefore l=15\n h=5 because its the size of class \n n = sum of CF/2 and that "
      "would be 50 \n now the closest greater value or equal value to is 50 that means c is 50 as well\n"
      "putting it all in formula")
print("Median is equal to = ",  med)