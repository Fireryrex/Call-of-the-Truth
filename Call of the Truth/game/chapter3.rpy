# Chapter 3 begins here

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c3 = Character("Bob")

label chapter3_start:
    $ current_chapter = 3

    c3 "Welcome to chapter 2, wait no."

    c3 "Its actually chapter 3"

    jump chapter4_start
