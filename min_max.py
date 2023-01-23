# Author: Aubrey Floyd
# GitHub username: aubreyfloyd2
# Date: 1/23/2023
# Description: Asks user for a number of integers and then collects that many integers from
#              the user and outputs the minimum and maximum of the integers
input_int = 0
print("How many integers would you like to enter?")
total_int = int(input())
if total_int == 1:
    print("Please enter", total_int, "integer.")
    min_num = int(input())
    max_num = min_num
    input_int += 1
else:
    print("Please enter", total_int, "integers.")
while input_int == 0:
    min_num = int(input())
    max_num = min_num
    input_int += 1
while input_int != total_int:
    num_2 = int(input())
    if num_2 <= min_num:
        min_num = num_2
    if num_2 >= max_num:
        max_num = num_2
    input_int += 1
if input_int == total_int:
    print("min:", min_num)
    print("max:", max_num)