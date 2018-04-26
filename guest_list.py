import math

guest_list = ["steve jobs", "gahndi", "dahlai lama"]

def print_invite(guests):
    print("NEW GUEST LIST:")
    for guest in guests:
        print("Dear {}, you are invited to my party".format(guest.title()))


print_invite(guest_list)

not_attending = ["steve jobs"]

new_guestlist = guest_list

for guest in not_attending:
    new_guestlist.remove(guest)
    print(">>>> Oh No! {} cant make it!".format(guest))
    print("   > {} removed from guest list".format(guest))



new_guestlist.append("elvis presley")

print_invite(new_guestlist)

print("We found a bigger table!")

new_guestlist.insert(0, "fortet") # beginning
new_guestlist.insert(math.ceil(len(new_guestlist) / 2), "jesus") # middle
new_guestlist.append("marilyn monroe")

print_invite(new_guestlist)

print("Sorry I can only invite 2 people for dinner now.")

while len(new_guestlist) > 2:
    sorry = new_guestlist.pop()
    print("sorry {}, your not invited anymore".format(sorry))
    print(new_guestlist)

while len(new_guestlist) > 0:
    del new_guestlist[0]

print(new_guestlist)
