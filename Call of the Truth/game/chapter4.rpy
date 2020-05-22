# Chapter 4 begins here

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c4 = Character("Another Another Random Character")

label chapter4_start:

    c4 "Welcome to chapter 4."

    call free_day("Bob", "Another Another Random Character")

    if spend_free_day_socializing:

        if(with_friend1):
            e "I decided to spend the day with Bob."
            #Add the jump to socializing section
        elif(with_friend2):
            e "I decided to spend the day with Another Another Random Character."
            #Add jump here as well

    jump chapter5_start
