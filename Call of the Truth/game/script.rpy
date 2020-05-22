# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

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


    # This ends the game.

    return
