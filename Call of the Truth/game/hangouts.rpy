label finn_hangout:

    if (finn_rank == 1):
        $ finn_rank += 1

        NAR "Finn had contacted me again, and I headed out to the park to hopefully run into him. I can see him a bit off away from the path."

        JESSE "Finn!"

        show finn

        FINN "Hey Jesse, how you been. We haven’t had much time to just talk lately have we? You busy?"

        FINN "Great! We have a lot to catch up on, cultists and magic aside"

        NAR "We spend a good hour talking about all sorts of mundane things going on in our lives. It feels nice to just have a chat and not have to worry about much."

        FINN "I’m glad I caught you on some free time of yours. This has been great"

        JESSE "It really has. I wish I could relax like this more often"

        FINN "Listen mate, if you ever need to talk about things, just know I’m here for you. Things might get...complicated in the future. Who knows what might happen soon…"

        NAR "He trails off and the look on his face worries me for a second. Before I can question him again, he’s back to his cheery self."

        FINN "Anywho, I should get home before it gets too late. Don’t wanna get mugged, though who would wanna mess with someone like me, am I right"

        NAR "He laughs at his own remark. God I missed having him around."
        hide finn
        show jesse

        menu:

            "{i}Go along with it{/i}":
                hide jesse
                show finn
                FINN "Oh, definitely. Who would want a piece of a strong soldier like yourself? They'd be on their knees begging for their lives."
                NAR "He laughed and agreed"

            "{i}Roll your eyes{/i}":
                hide jesse
                show finn
                FINN "Hey! You know it’s true"
                NAR "Maybe it is, but I’d never admit that. It would fuel his ego too much"

            "{i}Show concern{/i}":
                hide jesse
                show finn
                FINN "Don’t worry, I was only kidding. Kind of…"

        FINN "Alright, I’ll catch ya later!"

        $ stat_courage += 1
        NAR "FINN RANK [finn_rank]/6
        \n {b}Courage{/b}: [stat_courage]
        \n {b}Knowledge{/b}: [stat_knowledge]
        \n {b}Charm{/b}: [stat_charm]"


        NAR "I wave to him, and we part ways."

    elif (finn_rank == 2):
        $ finn_rank += 1

        scene room

        NAR "I’m relaxing in my bed for a change. It’s nice to have a break for once. The phone ringing breaks me out of my trance."

        NAR "I ignored it for a little bit, but it seemed pretty adamant on getting my attention."

        FINN "Oh good! You answered."

        JESSE "Finn? What are you doing so early?"

        FINN "Early? It’s already past noon!"

        JESSE "Oh right….time is but a construct"

        FINN "Uhuh...listen you got a sec? I wanted to check up on you. I know things have been kind of crazy lately and well, I want to know if you’re doing good? Mental health is important you know. Trust me, the more you damage that, the worse off you’ll be."

        NAR "He sounds somber."

        JESSE "Finn? Are YOU alright?"

        FINN "Huh? Oh, yea I’m good. Just tired is all. Been having some not so fun dreams lately about everything… and the war. Not so pretty to think about."

        NAR "This is the first time he’s talked to me about this stuff. I wonder if he’s comfortable talking about that…"

        JESSE "Hey Finn, if you’re not busy, why not come stay over for a bit. It’ll help get your mind off things."

        FINN "Really man? I appreciate it! I’ll head over in a bit okay? I don’t have much on actual progress, but we can worry about that later right?"

        NAR "He sounds way too happy about doing that, but if it helps him temporarily forget the trauma, then by all means. It feels like he’s always putting himself from one thing to another…"

        NAR "He ended up coming over, and we hung out for a bit."

        NAR "Nothing too serious was brought up… but I’m not sure if I’m really the one he would want to open up to about it… am I?"

        NAR "Either way, it was nice to catch up with him again."

        courage += 1
        NAR "FINN RANK [finn_rank]/6
        \n {b}Courage{/b}: [stat_courage]
        \n {b}Knowledge{/b}: [stat_knowledge]
        \n {b}Charm{/b}: [stat_charm]"

    elif (current_chapter >= 4 && finn_rank == 3):
        $ finn_rank += 1

        #Locked until chapter 4

        scene park

        NAR "I got a call from Finn again, and decided to meet up with him again. We opted for the park again this time."

        NAR "I could tell something was on his mind… But I waited until he brought it up naturally in a conversation."

        show finn

        FINN "This may sound weird, but thanks for trusting me back then."

        JESSE "What do you mean?"

        FINN "Back during everything that was happening back when Linden was pretending to be against us."

        hide finn
        show jesse
        menu:

        "I nearly got you killed?!":
            hide jesse
            show finn
            FINN "Well, it was a risk yeah, but I survived."

        "You’re… welcome?":
            hide jesse
            show finn
            FINN "Yeah, I guess that’s a weird thing to be thankful for."

        "What do you mean?":
            hide jesse
            show finn
            FINN "When you added me to your plan for Linden’s test."

        FINN "I guess… let me rephrase that."

        FINN "I’m happy I was able to help you out during all of that, by being someone you knew could get out of that."

        JESSE "I honestly just expected it to be alright once I thought of it…"

        FINN "Dwelling on that thought would have probably made you rethink it. It’s not something you should get used to, but it’s a decision that’s needed."

        FINN "Some things need to be done, and when you're in a team, you sometimes have to split up responsibility. I’ve been sent off to harder missions anyway. You fight your battles, and I’ll fight mine, except I’m not always going to know where that is."

        FINN "Dividing and conquering right?"

        FINN "Anyway, I’m not sure if I can forgive Linden, but he’ll be useful to us actually stopping them. I also… Wanted to apologize for when I wanted you to kill him."

        FINN "In the end, I'm glad you didn’t. You were always a bit more level-headed than me."

        hide finn

        scene date_transition

        $ finn_rank += 1
        NAR "FINN RANK [finn_rank]/6
        \n {b}Courage{/b}: [stat_courage]
        \n {b}Knowledge{/b}: [stat_knowledge]
        \n {b}Charm{/b}: [stat_charm]"

        NAR "Except… that’s not true at all."

        NAR "I didn’t expect to hear something like that from him… I’m certainly not a leader, but… I think I can forgive myself for throwing that at him."

    elif (current_chapter >= 6 && stat_courage >= 2 && finn_rank == 4):
        $ finn_rank += 1

        #Locked until chapter 6
        #Locked to rank 2 courage

        scene park

        NAR "I decided to take a breather for today and head to the park for some quiet time, the fresh air already making my head feel better. As I get closer, I see Finn sitting on a bench with his hands crossed leaning on his knees."

        NAR "He looks like he’s thinking about something, and I’m gonna go and bother him."

        show finn

        FINN "Hey, Jesse. What are you doing here?"

        JESSE "Same as you probably, just clearing my thoughts."

        NAR "His eyes looked back down. It was a few moments before he spoke again."

        FINN "Do you remember when we first met? Things were so much more simple back then."

        JESSE "Yeah, I think our only worries were not getting caught swiping from your dad’s alcohol stash."

        FINN "Hahahah I remember that! He used to get so mad at us that he’d make up the strangest punishments. I mean, who makes their kid stand out in the rain doing chores for hours on end? The man was crazy!"

        JESSE "Oh, remember when you had a thing for that lass, what was her name? Riley Jankins? She was quite the character"

        FINN "But she was kind of cute! Had a strong gambling habit though. Maybe too much for being only 15."

        NAR "We shared a few more good laughs, mostly at Finn’s awful experience with females. He seemed to be cheering up from whatever was getting him down earlier."

        FINN "There has just been so much on my mind as of late. The cult is acting shady like always, and I keep having nightmares from all the fighting."

        FINN "It’s strange, I never had any issues during the actual war, just after it. I don’t want to think I’m just crazy, but it’s hard to forget about that stuff."

        NAR "I take in this information before slowing speaking again."

        JESSE "That sounds...difficult, but if anyone can pull through this, I know you can. You’re the toughest guy I know, remember."

        FINN "Haha...yeah man. Listen, I appreciate you listening to me. I feel like I should have more regrets about things… but I guess that’s just a part of life too."

        FINN "Like with your dad. There was no way I could have done anything. But it’s so easy to think about all the things I could have done… if I had known of course."

        JESSE "Meanwhile, I didn’t even know anything. And you had kept that to yourself for the better part of a year…"

        FINN "It wasn’t hard… stuff like that you just forget when more and more things are thrown at you… but it’s always there in the back of the mind."

        FINN "Just, ignore me. It’s not even about revenge or vengeance or whatever anymore."

        JESSE "We’re involved in everything, almost as much as he was… and probably soon to be more."

        FINN "Exactly, if anything. I know he’d be happy with us carrying on what he started."

        JESSE "Of course, he’d be a little sad that we’ve had to get involved at all."

        FINN "Yeah, but we all know nothing is gonna go perfectly. At least for us right?"

        FINN "I’m in this, and I’ll do what I can. Even if fighting isn’t the best option we really have, I’ll make sure none of you have to do it."

        NAR "We say our goodbyes and part ways. Suddenly, I feel better about my own problems having heard Finn. I just hope this whole cult business doesn’t hurt him more than his own mind already has."

        hide finn
        scene date_transition

        $finn_rank += 1
        NAR "FINN RANK [finn_rank]/6
        \n {b}Courage{/b}: [stat_courage]
        \n {b}Knowledge{/b}: [stat_knowledge]
        \n {b}Charm{/b}: [stat_charm]"

        NAR "He’s never gotten a break really… and I didn’t tell him about what really happened back in november, I feel like he needs to hear that."

    elif current_chapter >= 7 && finn_rank == 5):
        $ finn_rank += 1

        #locked until chapter 7

        scene cafe

        NAR "I got a call from Finn again, and it seemed like he was free for a bit tonight"

        show finn

        FINN "Hey mate, wanted to check up on you again, spend some quality time together. Besides… you don’t look too good."

        JESSE "Is it that obvious?"

        FINN "For me at least. I know you better than anyone. I just came to tell you that if you ever need to talk, I’m here for you."

        JESSE "Thanks man, I think I’ll be okay though. What’s a little cult activity and magic anyways right? Easy stuff"

        NAR "Finn frowns at that."

        FINN "We know something big is gonna go down…  I just want you to be ready for whatever that may be. There are still a lot of unknown variables here."
        hide finn
        show jesse
        menu:
            "{i}Play it off coolly{/i}":
                JESSE "It’ll be fine. You know, probably."
                NAR "He didn’t resonate with that too well… he can tell something is up."
                hide jesse
                show finn

            "{i}Express concern{/i}":
                JESSE "To be honest… I am worried about what’s going to happen."
                NAR "He puts a hand on my shoulder to reassure me."
                hide jesse
                show finn


            "{i}Be confident{/i}":
                "I’ve got this, and I know everybody will do their part."
                NAR "Finn looks a little uneasy…"
                hide jesse
                show finn

        FINN "I just want you to be safe. You’re already putting a strain on your body and mind. If you aren’t careful, something irreversible could happen."

        JESSE "The sentiment is appreciated, but I’ll be okay, I promise. I have a good team behind me after all"

        NAR "He smiles at the thought"

        FINN "You’re right about that."

        NAR "I need to tell him…"

        JESSE "And… I need to tell you. Back in november, I didn’t decide not to kill him. I just… failed to."

        FINN "I…"

        FINN "I think I knew that."

        JESSE "What do you mean?"

        FINN "It’s hard to make up your mind to do something like that… but I knew I wasn’t dealing with it well… and I could only imagine for you. It’s fine Jesse."

        FINN "We all make mistakes, or have moments of weakness, but it’s about where to go with that. You’ve had some rough spots over the past couple of months."

        FINN "But I think now… It’s been something, but I think it was good for us."

        JESSE "It feels weird to phrase it like that, but I think I agree."

        FINN "Anyway… hey Jesse, does this place seem off to you?"

        JESSE "What do you mean? The Cafe, well a little I guess but…"

        FINN "No, It’s just this is the first place I thought was safe from them all… but now…"

        FINN "No, it wouldn’t make sense, we’ve said way too much here. Ignore me, I guess I’m just a little paranoid."

        JESSE "You think you’ll take a break from this when we end this?"

        FINN "What do you mean by that?"

        JESSE "Just feel like you’ve always been caught into things. War, cults, who knows what’s next."

        FINN "Ha. It’s certainly a lot when you mention it… I don’t know. It certainly isn’t boring. Which is enough for me I guess."

        FINN "But yeah, I think I’d like to relax for a bit."

        hide finn

        scene date_transition

        NAR "FINN RANK MAX
        \n {b}Courage{/b}: [stat_courage]
        \n {b}Knowledge{/b}: [stat_knowledge]
        \n {b}Charm{/b}: [stat_charm]"

        JESSE "By the way, are you ever going to get a phone?"

        FINN "Eventually you know, but then you’d get me involved in more stuff wouldn’t you?"

        NAR "He’s right on that front."

    elif(stat_courage < 2):
        NAR "I'm not courageous enough to face Finn right now. Lets do something else"
        $ hangout_failed = True
        return

    else:
        NAR "Finn doesn't seem to be available... Maybe I should try again later."
        $ hangout_failed = True
        return


    return

label evelyn_hangout:
    NAR "HAHA I still need to write this :P"
    return
