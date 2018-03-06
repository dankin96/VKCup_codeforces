def is_similar(one, two):
    one = one.lower()
    two = two.lower()
    one = one.replace('o', '0')
    one = one.replace('i', '1')
    one = one.replace('l', '1')
    two = two.replace('o', '0')
    two = two.replace('i', '1')
    two = two.replace('l', '1')
    return one == two


have_similar = False
newlogin = input()
counter = int(input())
for i in range(0, counter):
    login = input()
    if is_similar(newlogin, login):
        have_similar = True
        break
if have_similar:
    print("No")
else:
    print("Yes")
