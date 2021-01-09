# https://adventofcode.com/2020/day/1

# Specifically, they need you to find the two entries that sum to 2020 and 
# then multiply those two numbers together.
# For example, suppose your expense report contained the following:
# 1721
# 979
# 366
# 299
# 675
# 1456
# In this list, the two entries that sum to 2020 are 1721 and 299. 
# Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579

myData = [ 1721,  979, 366, 299, 675, 1456]

for i in myData:
    print("Curr val:", i);
    currValue = (2020 - i);
    if currValue in myData :
        print("Value ", currValue, " + ", i, " = ", i + currValue, "and the answer is:", i * currValue);
