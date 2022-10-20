#Program to find only negative numbers from a given list:

lst = [10,20,-8,-9,23,56,-80,89,-70]
#
# for i in lst:
#     if (i>0):
#         pass
#     else:
#         print(i)

negative_list = []

for i in lst:
    if (i>0):
        pass
    else:
        negative_list.append(i)

print(negative_list)