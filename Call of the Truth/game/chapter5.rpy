# Chapter 5 begins here

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c5 = Character("Chap 5 Char")

label chapter5_start:
    $ current_chapter = 5

    c1 "Welcome to chapter 5."

    jump chapter6_start
