username=""
display_name=username if username else "Guest"
print("Welcome,", display_name) #Welcome, Guest
'''
if username: display_name=username
else: display_name=Guest
as username is empty string, it returns False, username=Guest
'''