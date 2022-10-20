#Statement assesment, a program to find out the words starting with "S or "s

st = input("Enter a string : ")
lst = []
for i in st.split(" "):
    if i[0] == "s" or i[0] == "S":
        lst.append(i)

print("Please find the below list of words starting with character 'S' or 's' " "\n", lst)

