#!/usr/bin/python 
 
  def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.")
    if answer == "LEFT" or answer == "Left" or answer == "left":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "RIGHT" or answer == "Right" or answer == "right":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

#clinic()