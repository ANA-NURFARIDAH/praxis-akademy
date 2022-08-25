# words = ["anggur", "apel", "jeruk"]
# for i in words:
#     print(i)

users = {'ana' : 'active', 'nur': 'inactive', 'faridah': 'active'}

# Strategy: Interate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy: Create a new collection
active_users = {}
for user, ststus in users.items():
    if status == 'active':
        active_users[user] = status
        
print(users)
print(active_users)

a = {}
a["c"] = "d"
a["e"] = "f"
print(a)