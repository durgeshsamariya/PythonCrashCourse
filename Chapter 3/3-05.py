# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite. • Start with your program from Exercise 3-4. Add a print statement at the end of your program stating the name of the guest who can’t make it. • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting. • Print a second set of invitation messages, one for each person who is still in your list.


guest_list = ['Durgesh', 'John', 'Sarah', 'James']

print("Due to busy schedule " + guest_list[0] + " is unable to come for dinner.")

guest_list[0] = "Peter"

print(guest_list[0] + " is invited for dinner.")
print(guest_list[1] + " is invited for dinner.")
print(guest_list[2] + " is invited for dinner.")
print(guest_list[3] + " is invited for dinner.")

