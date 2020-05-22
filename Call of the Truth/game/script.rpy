# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Main character")



define narrator = Character(what_italic=True)


# The game starts here.

label start:
    $ character_stat1 = 0
    $ character_stat2 = 0
    $ character_stat3 = 0
    $ spend_free_day_socializing = False
    $ with_friend1 = False
    $ with_friend2 = False

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "This is the chapter selection screen."

    e "Please choose a chapter to jump to, or play the game as intended."

    menu:

        "Lets start from the top!":
            jump chapter1_start

        "Chapter 2":
            jump chapter2_start

        "Chapter 3":
            jump chapter3_start

        "Chapter 4":
            jump chapter4_start

        "Chapter 5":
            jump chapter5_start

        "Chapter 6":
            jump chapter6_start

        "Chapter 7":
            jump chapter7_start

# This is essentially the function for a half free day. When you have a half free day in your chapter, just type:
# call half_free_day
# and everything should work out
label half_free_day:

    narrator "Today is a half free day, please choose an activity to do:"

    menu:

        "activity for stat 1":
            e "My stat 1 is [character_stat1]."
            $ character_stat1 += 1
            e "Now it is [character_stat1]."

        "activity for stat 2":
            e "My stat 2 is [character_stat2]."
            $ character_stat2 += 1
            e "Now it is [character_stat2]."

        "activity for stat 3":
            e "My stat 3 is [character_stat3]."
            $ character_stat2 += 1
            e "Now it is [character_stat3]."
    return

# This is essentially the function for a free day. When you have a free day in your chapter, just type:
# call free_day
# and everything should work out
# optionally, add in up to 2 strings after call free_day if you have some people the mc can socialize with. I.E.
# call free_day("Bob", "Joe")
# Afterwards, you'll want something like this:
#    if spend_free_day_socializing:
#        if(with_friend1):
#            e "I decided to spend the day with Bob."
#            Add the jump to socializing section
#        elif(with_friend2):
#            e "I decided to spend the day with Another Another Random Character."
#            Add jump here as well
label free_day(friend1="", friend2=""):

    narrator "Today is a free day, please choose an activity to do:"

    menu:
        "activity for stat 1":
            $ spend_free_day_socializing = False
            e "My stat 1 is [character_stat1]."
            $ character_stat1 += 1
            e "Now it is [character_stat1]."

        "activity for stat 2":
            $ spend_free_day_socializing = False
            e "My stat 2 is [character_stat2]."
            $ character_stat2 += 1
            e "Now it is [character_stat2]."

        "activity for stat 3":
            $ spend_free_day_socializing = False
            e "My stat 3 is [character_stat3]."
            $ character_stat2 += 1
            e "Now it is [character_stat3]."

        "Spend some time with [friend1]" if friend1 != "":
            $ spend_free_day_socializing = True
            $ with_friend1 = True
            $ with_friend2 = False

        "Spend some time with [friend2]" if friend2 != "":
            $ spend_free_day_socializing = True
            $ with_friend2 = True
            $ with_friend1 = False


    return
