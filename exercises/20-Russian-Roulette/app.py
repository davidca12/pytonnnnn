import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

#  DON'T CHANGE THE CODE ABOVE
def fire_gun(num):
	# YOUR CODE HERE
    if bullet_position==num:
        return "You are dead! "+str(num)
    else:
        return "Keep playing! "+str(num)
    



num=spin_chamber()
print(fire_gun(num))