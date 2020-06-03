label side_story:

    $ stat_courage = 100
    $ stat_knowledge = 100
    $ stat_charm = 100
    $ current_chapter = 7

while True:
    scene room
    NAR "Please choose a side story to view."
    hide jesse


    menu:
        "Finn [finn_rank]/6":
            call finn_hangout

        "Evelyn [evelyn_rank]/6":
            call evelyn_hangout

        "Carter [carter_rank]/5":
            call carter_hangout

        "Felix [felix_rank]/5":
            call felix_hangout

        "Linden [linden_rank]/5":
            call linden_hangout

        "I'm done here":
            return

return
