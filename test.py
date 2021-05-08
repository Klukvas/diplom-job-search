import re

# print(re.match(r"^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$", 'asd@asd.ad'))
match = re.fullmatch(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$' ,'asd@asd.aasdd') 
print('YES' if match else 'NO') 