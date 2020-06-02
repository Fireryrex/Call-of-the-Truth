# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Main character")


define NAR = Character(what_italic=True)

# The game starts here.

label start:
    $ stat_courage = 0
    $ stat_knowledge = 0
    $ stat_charm = 0
    $ spend_free_day_socializing = False
    $ with_friend1 = False
    $ with_friend2 = False
    $ hangout_failed = False

    $ current_chapter = 0

    $ finn_rank = 1
    $ evelyn_rank = 1
    $ carter_rank = 0
    $ felix_rank = 0
    $ linden_rank = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show jesse

    # These display lines of dialogue.

    NAR "This is the chapter selection screen."

    NAR "Please choose a chapter to jump to, or play the game as intended."


    menu:

        "Lets start from the top!":
            jump prologue_start

        "Chapter 1":
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
    scene map
    show jesse

    NAR "Today was a busy day, but suddenly I found myself having some free time. Maybe I should work on improving myself. What to do...
    \n {b}Courage{/b}: [stat_courage]
    \n {b}Knowledge{/b}: [stat_knowledge]
    \n {b}Charm{/b}: [stat_charm]"

    menu:

        "Take a walk around to build up courage":
            $ stat_courage += 2
            NAR "I strolled around the neighborhood. Nothing notable happened, but I feel braver now."

        "I've been neglecting my studies, I should catch up and increase my knowledge":
            $ stat_knowledge += 2
            NAR "I spent my free time reviewing my notes and felt myself grow smarter"

        "Maybe I should do some gardening, work on my charm a bit.":
            $ stat_charm += 2
            NAR "I spent my time working on my garden, speaking to passersby. From these social interactions, I felt my charm increasing."

    NAR "{b}Courage{/b}: [stat_courage]
    \n {b}Knowledge{/b}: [stat_knowledge]
    \n {b}Charm{/b}: [stat_charm]"

    hide jesse

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
label free_day(stat_to_train="", friend1="", friend2=""):

    $ hangout_failed = False
    $ spend_free_day_socializing = False
    $ with_friend1 = False
    $ with_friend2 = False

    scene map
    show jesse

    NAR "I don't really have anything to do today. Maybe I could work on my [stat_to_train]. I could also hang out with [friend1] or [friend2].
    \n {b}Courage{/b}: [stat_courage]
    \n {b}Knowledge{/b}: [stat_knowledge]
    \n {b}Charm{/b}: [stat_charm]"

    menu:
        "Take a walk to work on courage." if stat_to_train == "courage":
            $ stat_courage += 2
            NAR "I strolled around the neighborhood. Nothing notable happened, but I feel braver now."

        "Spend some time study to improve my knowledge." if stat_to_train == "knowledge":
            $ stat_knowledge += 2
            NAR "I spent my free time reviewing my notes and felt myself grow smarter"

        "Work on my garden to train my charm." if stat_to_train == "charm":
            $ stat_charm += 2
            NAR "I spent my time working on my garden, speaking to passersby. From these social interactions, I felt my charm increasing."

        "Spend time working on improving myself" if stat_to_train == "all":
            $ stat_courage += 2
            $ stat_knowledge += 2
            $ stat_charm += 2
            NAR "As I started on my excersises, I felt a sense of futility. The rate at which I was working wouldn't be enough. With a sudden burst of determination, I started working faster than ever before. At the end of the day, I sat down exhausted, feeling satisfaction from my improvement."

        "Spend some time with [friend1]" if friend1 != "":
            $ spend_free_day_socializing = True
            $ with_friend1 = True
            $ with_friend2 = False

        "Spend some time with [friend2]" if friend2 != "":
            $ spend_free_day_socializing = True
            $ with_friend2 = True
            $ with_friend1 = False

    NAR "{b}Courage{/b}: [stat_courage]
    \n {b}Knowledge{/b}: [stat_knowledge]
    \n {b}Charm{/b}: [stat_charm]"

    hide jesse

    return

label new_day(date=""):

    scene date_transition
    centered "{size=+10}{color=#ffffff}[date]{/color}{/size}"

    return

label work_day(date=""):

    scene date_transition
    centered "{size=+10}{color=#ffffff}[date]{/color}{/size}"

    NAR "Today's a work day, so after finishing my morning routine, I set off for work"

    return
