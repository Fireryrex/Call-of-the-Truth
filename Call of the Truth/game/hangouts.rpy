label finn_hangout:
    #NAR "[finn_rank], [current_chapter]"
    if(finn_rank == 1):
        $ finn_rank = 2

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
        $ finn_rank = 3

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

        $ stat_courage += 1
        NAR "FINN RANK [finn_rank]/6
        \n {b}Courage{/b}: [stat_courage]
        \n {b}Knowledge{/b}: [stat_knowledge]
        \n {b}Charm{/b}: [stat_charm]"

    elif (finn_rank == 3 and current_chapter >= 4):
        $ finn_rank = 4

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

    elif (finn_rank == 4 and current_chapter >= 6 and stat_courage >= 6):
        $ finn_rank = 5

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

    elif (finn_rank == 5 and current_chapter >= 7):
        $ finn_rank = 6

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

    elif(stat_courage < 6):
        NAR "I'm not courageous enough to face Finn right now. Lets do something else"
        $ hangout_failed = True
        return

    else:
        NAR "Finn doesn't seem to be available... Maybe I should try again later."
        $ hangout_failed = True
        return


    return

label evelyn_hangout:
    if(evelyn_rank == 0):
        $evelyn_rank = 1

        scene room

        NAR "I grabbed my phone and rang up Evelyn."

        JESSE "Hey evelyn, its me, Jesse. Are you free today?"

        EVELYN "For a bit at noon, what's up?"

        JESSE "Nothing much, just wanted to hang out."

        scene date_transition

        NAR "Evelyn was was on lunch break when we met up, so we decided to head over to the cafe."

        scene cafe

        NAR "The two of us ordered lunch. Despite the fact that I gave the invitation, I didn't really know what to talk about and was glad when she took the initiative"

        show evelyn

        EVELYN "So, its been a while, huh? The last time that the two of us had a chance to just sit down and talk... Huh, it may have been when you were still in university."

        JESSE "Oh, I think you're right... Wow, a year sure passed quickly. Sorry that I kinda stopped keeping in touch with you after I quit..."

        JESSE "Things... well, things were busy I guess. I had a lot to do not a lot of free time. There was also... you know, that."

        EVELYNN "Yea, about “that”. How are you feeling? It's been a year since your dad died, are you doing any better?"

        hide evelyn
        show jesse

        menu:
            "...":
                hide jesse
                show evelyn
                EVELYN "It's fine. You don't have to think about it if bothers you too much. We can chan-"

            "{i}sigh{/i} I suppose you could say that.":
                JESSE "Lets be honest though, anything is better than the first few days."

                NAR "I tried to crack a smile."

                JESSE "I was a mess. Time has definitely given me a chance to come to terms with it."

                hide jesse
                show evelyn

                EVELYN "I suppose so. It was hard seeing you so upset. Your personality changed so much that I could barely recognize you."

                EVELYN "Oh hey, our food is here."

            "Uh... Oh would you look at that! Our food's here":

                NAR "Evelyn saw right through my feeble attempt at changing the subject."

                hide jesse
                show evelyn

                EVELYN "If you don't want to talk about it that much, you could've just told me."

        NAR "A waiter delivers our order, breaking our conversation."

        NAR "Relieved, I turn my focus to my food and quickly finished"

        NAR "By the time we were both done eating, Evelyn' break was just about finished, so I said my farewells and headed home"

        NAR "EVELYN RANK [evelyn_rank]/5"

    elif(evelyn_rank == 1):
        $ evelyn_rank = 2

        NAR "I called up Evelyn again to see if she wanted to hang out. Much like last time, we headed to the Cafe during her lunch break"

        scene cafe

        NAR "Not wanting things to be as awkward as last time, I attempt to start the conversation first"

        show jesse

        label look_brothers_food:
        menu:
            "So... how's university":

                hide jesse
                show evelyn

                EVELYN "Eh, its not bad, I suppose. The workload is awful though. I swear the professors just want to see us suffer."

                EVELYN "Although I have to admit, things have gotten easier after I got better at scheduling. Otherwise, we probably wouldn't be having this conversation."

                hide evelyn
                show jesse
                jump look_brothers_food


            "I see that you found a different part time job...":

                hide jesse
                show evelyn

                EVELYN "Yea, I had to. My old one is just too far from university. I'd spend too much time travelling there to be able to get any study time for my classes."

                EVELYN "As much as we need the money, my parents want me to prioritize my studeis, so... you know."

                EVELYN "At least my current job has lenient time slots."

                hide evelyn
                show jesse
                jump look_brothers_food

            "... Oh look. Food!"

                EVELYN "Just in time, I'm getting a bit hungry"

        NAR "Not much else happened afterwards. We both finished our food and said our farewells"

        NAR "ALthough, Evelyn was staring at me with a curious expression on her face. I suppose I'll have to get her to explain that to me at our next meeting"

        $ stat_knowledge += 1
        NAR "EVELYN RANK [evelyn_rank]/5
        \n {b}Courage{/b}: [stat_courage]
        \n {b}Knowledge{/b}: [stat_knowledge]
        \n {b}Charm{/b}: [stat_charm]"

    elif(evelyn_rank == 2):
        $ evelyn_rank = 3

        scene cafe
        NAR "We met up at the same place as the last few times, although this time Evelyn brought her own lunch"

        show jesse

        JESSE "Not getting anything today?"

        hide jesse
        show evelyn

        EVELYN "I've been spending too much eating out this month, so I just made myself some food. I'm still down to have a conversation though."

        EVELYN "Speaking of, I've been meaning to ask. Why haven't you come back to univerity?"

        NAR "So thats what she was thinking about last time."

        JESSE "Uh well... I guess I just kind of forgot?"

        JESSE "I don't know... I've been living by myself for the last year just fine. I guess I just don't really think I need college"

        JESSE "Plus, I'm a year behind now and I feel like it'll be a bit weird going back and seeing everyone I know a year up on me."

        EVELYN "Oh, don't give me those excuses. You know university is important for getting jobs that pay better? Sure you could probably continue living the way you are, but do you always want to be a customer service rep for the rest of your life?"

        EVELYN "Plus, the knowledge you can learn from university can be useful."

        JESSE "..."

        EVELYN "Look, if its the being a year behind thing thats keeping you from coming back, I got something for you."

        NAR "She pulled out a stack of papers from one of her bags and plopped it onto the table"

        EVELYN "These are some practice placement tests for the lower division courses. They're pretty easy so you should be able score well on them."

        EVELYN "If you manage to do well, you'll be able to skip a year and rejoin the rest of us as juniors. Boom, problem solved."

        JESSE "Gee, thanks but I-"

        EVELYN "Shh, shh. No butts. Just promise me you'll do them by the time we meet up again alright?"

        JESSE "I mea-"

        EVELYN "Well, I need to get back to work, see you later!"

        NAR "She rushes off without another word, leaving me with a huge stack of papers."

        NAR "I sigh, pay for my meal and awkwardly head back home, clutching the papers to my chest"

        NAR "I suppose doing these wouldn't hurt... I mean, it would be nice seeing my friends from college again..."

        NAR "Although these problems are actually pretty hard. I might need to study more for these..."

        $ stat_knowledge += 1
        NAR "EVELYN RANK [evelyn_rank]/5
        \n {b}Courage{/b}: [stat_courage]
        \n {b}Knowledge{/b}: [stat_knowledge]
        \n {b}Charm{/b}: [stat_charm]"

    elif(stat_knowledge >= 6 and evelyn_rank == 3):
        $ evelyn_rank = 4

        NAR "As I reached for the phone to call Evelyn, I suddenly realized that I haven't finished the practice tests yet."

        NAR "I decided to put off calling her until after I finish, and instead grab out the last practice exam that I need to finish"

        NAR "Taking one look at the paper fills me with dread. Ugh, why did it have to be linear algebra..."

        NAR "I settle in my chair and read the first question."

        show jesse

        label lin_alg_1:
        NAR "Determine if (1, 3) is a solution to the system: \n2x + y = 5 \nx - y = -5"

        menu:
            "It is a solution":
                NAR "Wait... that doesn't seem right"
                $ stat_knowledge -= 1
                $ questions_correct -= 1
                NAR "{b}Knowledge{/b}: [stat_knowledge]"
                jump lin_alg_1

            "It is not a solution":
                NAR "Right because (1) - (3) doesn't equal -5"
                NAR "Huh, I feel a bit smarter after that"
                $ stat_knowledge += 1
                $ questions_correct += 1
                NAR "{b}Knowledge{/b}: [stat_knowledge]"

            "Ugh... why am I doing math":
                NAR "Whatever lets just get to it... seems like the answer is... no? Yea that seems right"

        NAR "After around a while I came across a relatively difficult problem"

        label lin_alg_2:
        NAR "Identify the elementary row operation performed on the follwing matrix: \n1   2   -1          0  -1   -4 \n0  -1   -4    ->    1   2   -1 \n3   3   -11          3   3   -11"

        menu:
            "R1 <-> R2":
                NAR "Seems right..."
                NAR "Huh, I feel a bit smarter after that"
                $ stat_knowledge += 1
                $ questions_correct += 1
                NAR "{b}Knowledge{/b}: [stat_knowledge]"

            "R1 + R2 -> R2":
                NAR "wait a minute,,,"
                $ questions_correct -= 1
                $ stat_knowledge -= 1
                NAR "{b}Knowledge{/b}: [stat_knowledge]"
                jump lin_alg_2:

            "Uh... I'm just going to guess":
                NAR "Hopefully this is right..."

        NAR "With that, the rest of the test was relatively easy, although still very tedious. I managed to finish all the tests, but it was getting dark by the time I did."

        NAR "I decided that I would call Evelyn at a later date to tell her."

    elif(evelyn_rank == 4):
        $ evelyn_rank = 5

        NAR "I finally decided to call Evelyn to tell her about the quiz"

        JESSE "So, I finally finished all of the exams."

        EVELYN "Oh really? They weren't too bad I hope?"

        if(questions_correct == 2):
            JESSE "Easy as pie. The actual exams should be a breeze"

            EVELYN "Yup! The actual exams are much easier. I made sure to make the questions extra difficult to prepare you better"

            JESSE "Thanks for the help, I appreciate it."

            EVELYN "I assume this means that you're coming back to school?"

            JESSE "I'm not 100\% sure about it yet..."

        elif (questions_correct == 1):
            JESSE "Eh, it wasn't too bad. I didn't get every question right but I still did well"

            EVELYN "That's great! I made those practice tests more difficult than the actual ones so you'd do great!"

            EVELYN "So... have you decided to take the exam?"

            JESSE "Eh, I've been going back and forth on it a lot..."

        elif (questions_correct < 1):
            JESSE "It was awful. Why are the questions so difficult?! How did you guys learn all of this?"

            EVELYN "Err... uh... So I wrote those practice exams and made them a bit more difficult-"

            JESSE "You what?."

            EVELYN "Ehehem... well it was so you would be overprepared for the exam and easily pass it."

            EVELYN "even if you didn't do so well, you should still be good for the exam!"

            JESSE "I don't think so..."

        EVELYN "Please consider it. You know, both of us have already spent so much time preparing you for those exams."

        EVELYN "It would be a waste if you were to give up after coming this far."

        EVELYN "So, what do you say?"

        menu:
            "Sure!" if questions_correct >= 1:
                EVELYN "Yay! Can't wait to see you back at school"

                JESSE "Hey, I haven't passed yet"

                EVELYN "Oh don't worry, I have faith in you"

                EVELYN "Anyways, got to go!"

            "Ugh... fine":
                EVELYN "Hey, why are you so hesitant"

                JESSE "I'm not, I'm not..."

                EVELYN "Suuure... Well, either way I'll be happy to see you back at school."

                EVELYN "I'm busy now, so lets get you ready for it later."

            "No."
                EVELYN "Well thats a shame."

                EVELYN "Guess I'll see you later then?"

                JESSE "Yea, I'll call if I want to hang out in the future"

        JESSE "See you."

        NAR "I hung up and went to lie on my bed."

        NAR "The rest of the night proceeded as usual"

    elif(stat_knowledge < 6):
        NAR "I'm not sure I'm smart enough to do the practice tests"
        $ hangout_failed = True
        return

    elif(stat_knowledge < 16):
        NAR "I'm not smart enough to deal with her right now... My mental facilities are exhausted."
        $ hangout_failed = True
        return

    else:
        NAR "Evelyn was busy with work today, so I decided to find something else to do"
        $ hangout_failed = True
        return

    return

label carter_hangout:
    #NAR "[carter_rank]"
    if(carter_rank == 0):
        $ carter_rank = 1

        scene bookstore

        NAR "Even though I’ve been having a lot of things going on these days, there have been some pockets of free time, and there’s not a lot to do."

        NAR "Getting a book to read is sort of the only thing I could come up with to fill that time. Plus it would get my mind off everything else..."

        NAR "And so I found myself back here, given the lack of options. As much as I hate to admit it, Wilkinson would probably be able to get me a good book to read, and it was a convenient place to get to…"

        show carter

        NAR "A small bell rang as I opened the door, and Carter, who seemed to be spinning a pen on his table, looked up as I came in, and gave me a puzzled look."

        CARTER "I wasn’t aware we were meeting up today. Did something urgent happen?"

        CARTER "You seem to be alone though. Maybe you came to get my advice on something? Or...dare I say, you’re here to buy a book?"

        JESSE "Well no, I mean nothing bad happened. I just wanted to have a little chat...or something like that."

        NAR "Man, I’m not even a minute into this conversation and Ialready feel like this was a terrible idea. I mean it’s already too late to back out so I might as well try to keep this going."

        hide carter

        show jesse

        menu:
            "So uh...nice weather isn’t it?":
                hide jesse
                show carter
                CARTER "If you really have nothing interesting to talk about, you can just get straight to the point."

            "Good to see business is booming.":
                    hide jesse
                    show carter
                    CARTER "Haha, glad to see you’ve been working on your sweet talking."

            "I just thought you might be feeling pretty lonely, so I decided to come give you a visit.":
                    hide jesse
                    show carter
                    CARTER "Ha! Or maybe you were feeling lonely and have no one else to talk to?"

        CARTER "Well I am pleased that you came to pay a visit. How about I show you a bit of what I’ve been working on lately."

        NAR "He sat there smiling at me and kept giving short glances toward a potted plant on his desk."

        JESSE "Plants? You’ve been uh...gardening?"

        CARTER "I mean, I don’t know if you can quite call this gardening, but yes, I’ve been messing around with plants. Adds a nice touch to the store doesn’t it?"

        JESSE "Sure. I mean it’s great that you’re decorating this place, it really could use the help."

        CARTER "Oh please, I’m sure you’re just jealous your room could look this clean all the time."

        NAR "he’s joking right?"

        NAR "I try to retaliate to his comment, but he immediately cuts me off and points to the pot on his desk."

        CARTER "You see this little guy? Give it a year or so and I could wrap him all the way around my desk! Wouldn’t that be exquisite."

        JESSE "Uh…"

        CARTER "And this guy…"

        NAR "He gets out of his desk and walks to another plant at one of the aisles."

        CARTER "If you break its leaves, it starts dripping this gooey thing, and I’ve heard it helps cure skin problems. Or something like that."

        JESSE "Yeah, I’m sure that will come in handy…"

        CARTER "Oh, and then there’s this other guy…"

        NAR "This was starting to get out of hand, and I wasn’t really following this conversation, so I had to try and cut him off."

        JESSE "Okay so actually, I came because I was looking for a book recommendation, and well I figured maybe you would have an idea of something I could read?"

        CARTER "So you did come to buy a book! Why didn’t you say so earlier?"

        JESSE "Well, I wasn’t really sure how to bring it up. I mean you also seemed like you were having fun talking about your uh… projects."

        CARTER "Ahem, I mean this is a bookstore after all, so every now and then I suppose I should help someone take these off the shelves. Anyways, what kinda books are you looking for?"

        JESSE "Uh, I haven’t exactly thought about it. I was just hoping maybe you had something interesting to recommend."

        CARTER "Mmm let’s see here, The Interpretation of Dreams, interesting read for sure, dunno if it’s quite your speed though. Ah, Tarzan Of The Apes, popular book, I assume you’ve already read it though?"

        JESSE "Well, actually no. I’ve heard some of my friends reading it in classes, but my teachers never had me read it."

        CARTER "Oh, is that so? Well I’m sure you’ll have a great time with this book. You can have it until you’re finished, if you would like to keep it afterwards, you can pay me the cost."

        JESSE "Huh really? Thanks I guess, I’ll try to keep it in good condition."

        CARTER "Don’t worry about it. I’m just trying to build a good relationship with my customer."

        hide carter

        show jesse

        menu:

            "Well maybe if this one’s good I’ll consider buying some others from you.":
                hide jesse
                show carter
                CARTER "Perfect, pleasure doing business with you."

            "If you keep saying stuff like that, I might actually believe that you’re doing your job.":
                hide jesse
                show carter
                CARTER "I treat you so well, and this is the treatment I get?"

            "Okay, just letting you know you threw away your only shot of getting me to buy a book from here.":
                hide jesse
                show carter
                CARTER "I trust that you’ll be so blown away, you’ll just come running back for more."

        NAR "I’ve already spent way more time here that I was planning to, so I thanked him for the book and quickly left before he could bring up his plants again."

        scene date_transition

        $ stat_charm += 1
        NAR "CARTER RANK [carter_rank]/5
        \n {b}Courage{/b}: [stat_courage]
        \n {b}Knowledge{/b}: [stat_knowledge]
        \n {b}Charm{/b}: [stat_charm]"


        NAR "Just skimming through the pages as I’m walking back, I catch bits of some fairly interesting parts. Hopefully this will all be worth the effort."

    elif(stat_charm >= 6 and carter_rank == 1):
        $ carter_rank = 2

        #Charm rank 2 required
        scene bookstore

        NAR "I had been reading the book Carter gave me during my free time, and although I hadn’t gotten that far into it, I reached a page that appeared to have been torn out."

        NAR "I tried asking Sara and Evelyn if they had an extra copy, but neither of them did, and I really didn’t want to just skip over that section."

        NAR "Hopefully Carter will let me just grab a different copy and leave. I don’t want to get stuck in another lecture detailing the attributes of each plant."

        NAR "I walk back into the store and for once, I see Carter helping a customer look through his collection of books."

        show carter

        CARTER "Jesse, back already? Let me finish helping this young lady and I’ll be right with you."

        NAR "I just wait in the middle of the room, browsing the shelves for any potentially interesting titles. Soon enough he’s finished and the girl leaves with two books in her hands."

        CARTER "Alright, hope I didn’t keep you waiting too long."

        JESSE "I get the feeling you’re just rubbing in the fact that you finally have a customer."

        CARTER "Oh please, I have plenty of customers. You just never decide to visit during the rush hours."

        JESSE "Mind telling me when that is?"

        CARTER "Anyways, I’m assuming you came here to talk about something? Did you already finish the book I gave you? Are you looking for another recommendation?"

        NAR "He was pretty blatantly switching the topic on purpose, but at this point, I could care less. I don’t think I can really get anywhere arguing with this guy."

        JESSE "No, I’m still only a few chapters in. I couldn’t help but notice however, that there’s a page missing, and I couldn’t find another copy."

        JESSE "So maybe, if you have an extra, could I switch it out for this one or something?"

        CARTER "A missing page? That certainly isn’t good for my credibility. Thank goodness it ended up in your hands and not another customer."

        NAR "I couldn’t tell if he meant that as an insult, or if maybe he was just saying he trusted me more. To be honest, I’m not even sure which one I would prefer."

        CARTER "Hmm I believe that copy was actually given to me by one of my old customers. Perhaps I need to be a little more cautious when getting donations. Anyways, how have you been enjoying it so far?"

        hide carter

        show jesse

        menu:

            "To be honest, it’s been really interesting. It was a good recommendation.":
                hide jesse
                show carter
                CARTER "Well I’m glad to hear you like it. That’s what you should expect when working with a professional."

            "It’s been pretty good. I guess even you can get lucky sometimes.":
                hide jesse
                show carter
                CARTER "That’s very flattering. I try my best to be humble at what I do."

            "I mean it’s okay I guess…":
                hide jesse
                show carter
                CARTER "Oh no need to be shy, you can show your appreciation once in a while."

        CARTER "Anyways, I have another copy right here. It’s brand new, so you shouldn’t have any more problems. I’ll see what I can do about that missing page."

        NAR "I take the new book and return the copy I had. I glance it over, and it seems to be in good condition."

        JESSE "Thanks, maybe I’ll stop by again to give you some company to show my appreciation."

        CARTER "I’ll be awaiting your return. Maybe you’ll have something a little more substantial to say next time."

        CARTER "Oh I almost forgot. I just got this new plant a few days ago. Care to take a look at it? If I let it…"

        NAR "Oh no, I wasn’t about to let this happen again. I’d gotten what I wanted and I had no reason to stay anymore."

        JESSE "Oh would you look at the time. I’ve got to go, thanks for the book!"

        NAR "I could’ve sworn I saw him chuckling to himself as I left the store. He better not be doing this just to get on my nerves."

        hide carter

        NAR "It might not even be that bad of an idea to visit every now and then. Things don’t really get dull when I’m around at least. Who knows, maybe he’ll even give me another free book."

        scene date_transition

        $ stat_charm += 1
        NAR "CARTER RANK [carter_rank]/5
        \n {b}Courage{/b}: [stat_courage]
        \n {b}Knowledge{/b}: [stat_knowledge]
        \n {b}Charm{/b}: [stat_charm]"

    elif(carter_rank == 2):
        $ carter_rank = 3

        scene bookstore

        NAR "I’m back at Carter’s place after taking a short walk for some fresh air. Upon walking inside, I’m surprised to see that he’s helping yet another customer."

        show carter

        JESSE "Wow, two customers in two visits, you must be getting really lucky."

        CARTER "Give me a sec, I’ll be right with you."

        NAR "He didn’t seem to notice that it was me that walked in. I just watched as he helped a middle aged man navigate his store before walking away with a book in hand. He finally realizes it’s me."

        CARTER "Oh it’s you! Why didn’t you say anything?"

        JESSE "Well you just seemed so engrossed in your work I didn’t want to disturb you."

        CARTER "I appreciate the consideration, but I don’t mind holding multiple conversations. I’m quite good at it in fact."

        JESSE "I’ll be sure to test your limits next time."

        CARTER "Don’t go too overboard. I am still human after all. Hmm...unless you went on a reading spree, I’m assuming you’re still not done with Tarzan?"

        JESSE "Yeah I’m still working on it. It’s been enjoyable though."

        CARTER "Which means you’re here because you missed me! Glad I could help comfort you in these trying times."

        JESSE "Ha ha very funny. Just thought your shop could use a few more visitors."

        CARTER "Well you came at the perfect time. I just got a new stock of books. You can help me shelf them."
        hide carter

        show jesse

        menu:

            "Oh sure I can help with that!":
                hide jesse
                show carter
                CARTER "Why thank you for being cooperative."

            "I come all the way here just to do your job for you?":
                hide jesse
                show carter
                CARTER "This is hard work. I feel like I deserve a break every now and then."

            "More like I’ll just be doing all the work?":
                hide jesse
                show carter
                CARTER "Oh don’t worry, I’ll do my fair share of the work."

        NAR "He pulls out a box filled with books and just hands it to me."

        CARTER "These are all the books that need shelving. Each shelf corresponds to a genre and they are in alphabetical order. If you have any questions about the genres just let me know."

        JESSE "So...what will you be doing while I’m busy with this?"

        CARTER "Oh I’ll be watching you. And if you need any help I’ll give you some assistance."

        JESSE "Uhuh."

        NAR "Whatever. Might as well do something productive every now and then."

        NAR "I spend the next ten or so minutes going down each aisle, putting books where I assumed they belonged. The whole time Carter was just reading a book. So much for watching me."

        NAR "Finally done. I hand the empty box back to Carter."

        CARTER "Great job. Maybe in the future if you beg me hard enough, I’ll let you work here sometimes."

        JESSE "I’m not sure if you can afford that with the business you’re getting."

        CARTER "Do you have any more time? There’s something else I would love to have some assistance with."

        JESSE "Oh I gotta bounce. I’m uh, meeting up with someone soon."

        CARTER "Suit yourself. I’ll let you have a discount on the next book you buy for helping me out today."

        JESSE "Gee thanks. We’ll see if I end up using that."

        NAR "I wave goodbye and get on my way before he drags me into anything else."

        scene date_transition
        NAR "CARTER RANK [carter_rank]/5
        \n {b}Courage{/b}: [stat_courage]
        \n {b}Knowledge{/b}: [stat_knowledge]
        \n {b}Charm{/b}: [stat_charm]"

    elif(stat_charm >= 16 and carter_rank == 3):
        $ carter_rank = 4

        #Charm rank 3 required
        scene bookstore

        NAR "I enter the bookstore to find Carter kneeling on the ground, preoccupied with one of his plants. He turns around when he hears me come in, scissor in hand."

        show carter

        CARTER "Jesse! Perfect timing! I just started trimming my plants. You can give me a hand taking care of them."

        NAR "Oh whatever. How long could it possibly take?"

        JESSE "Sure thing. What do you need me to do?"

        CARTER "Grab that water pail over there, it should be filled with water. Just go around and water each plant a little."

        NAR "Okay, simple enough. I walk over and pick up the water pail, it’s a lot heavier than I expected. I walk over to the nearest plant and start watering it."

        hide carter

        show jesse

        menu:

            "Is this a good amount?":
                hide jesse
                show carter
                CARTER "Yeah just give that much to each one."

            "Just tell me when to stop.":
                hide jesse
                show carter
                CARTER "Stop stop stop! That’s way too much. Give the others like half that much."



            "That’s it?":
                hide jesse
                show carter
                CARTER "Yes, just like that. Now move on to the next one."

        NAR "I slowly go from one plant to another, sprinkling them for a bit before moving on. Carter isn’t saying anything, so I decide to ask him something that’s been on my mind for a while."

        JESSE "So uh, this cult that you’re a part of. How exactly did you end up in it?"

        CARTER "Ah, asking the deep questions. Well you have been quite helpful lately so I suppose I could tell you a bit about my past."

        NAR "He stops trimming the plant and gets up to think a little."

        CARTER "Hmm I believe it started when I was still in college. Much like yourself, I didn’t have too many friends at that time. There was this group of three people that I tended to hang around."

        JESSE "No need to lump us together. I prefer to think I’m quite different from you."

        NAR "He just chuckles at this comment and continues."

        CARTER "Anyways, these three guys were close friends, I sort of just tagged along with them sometimes. Even now I’m not really sure how they stumbled upon it, but they found out about magic and started to mess around with it."

        CARTER "Since I hung out with them often, they decided to let me in on their discoveries and it started to become more organized than a bunch of kids just playing with magic."

        CARTER "From there, we started recruiting other people we believed would be helpful with what we were researching, and we’ve been growing ever since."

        CARTER "Watch it with that pail, you’re going to drip water all over my floor!"

        hide carter

        show jesse

        menu:

            "Ha, don’t worry I’m not that clumsy.":
                hide jesse
                show carter
                CARTER "I don’t think I have that much trust in you yet."

            "It’s fine, keep going.":
                hide jesse
                show carter
                CARTER "Well that’s about all I was gonna tell you."

            "{i}Pour some on the floor{/i}":
                hide jesse
                show carter
                CARTER "Hey hey hey! Don’t make me regret answering your question!"

        CARTER "Whatever, that should be the last one. Any other questions? Or do you want to help out with some other stuff?"

        JESSE "No I’m good, I’ve spent plenty of time here already. Thanks for telling me more about your uh...organization."

        CARTER "No problem. You’re gonna have to do a lot better if you think I’m gonna just let you in right now though."

        JESSE "Oh you don’t have to worry about that."

        hide carter

        NAR "CARTER RANK [carter_rank]/5
        \n {b}Courage{/b}: [stat_courage]
        \n {b}Knowledge{/b}: [stat_knowledge]
        \n {b}Charm{/b}: [stat_charm]"

        scene date_transition

        NAR "With that I get on my way. Today was somewhat productive I guess…at least more than the other days."

    elif(current_chapter >= 7 and carter_rank == 4):
        $ carter_rank = 5

        #Chapter 7 required
        scene bookstore

        NAR "I finally finished Tarzan Of The Apes. It was a pretty good read, definitely something I would have rather read over some of the other books I was forced to read in school. I had to return the book to Carter though, since he was only letting me borrow it in the first place."

        NAR "I walk through the door and I see Carter fiddling with the plant on his desk."

        show carter

        CARTER "Ah Jesse! Are you here to help out with the plants again? You must be getting pretty attached."

        JESSE "Pshh, you wish. I finished the book you gave me. I’m just here to return it."

        CARTER "Hmm you don’t want to keep it?"

        hide carter

        show jesse

        menu:

            "I mean I’d love to, but I’m too cheap to buy it.":
                hide jesse
                show carter
                CARTER "What a shame, you seemed like such a promising customer."

            "It was good, don’t get me wrong. It just wasn’t that good.":
                hide jesse
                show carter
                CARTER "Hmm, it seems I’ve failed to give you the best recommendation."

            "No way, I’m not about to buy something I’ve already read.":
                hide jesse
                show carter
                CARTER "Oh, that’s quite disappointing."

        CARTER "Well if that’s that, would you like to browse my shop for any of these other quality selections? Remember you still have that discount from earlier. I’m willing to give you one for half the price!"

        JESSE "No I’m good. If I ever have the urge to read another book I’ll be sure to ask you for recommendations."

        CARTER "Are you sure? I have plenty of good books here. You can try a different genre, it’ll freshen up your mind. How about this one here, it’s a story about…"

        JESSE "No really. I’m good. Don’t worry about it."

        CARTER "Or how about this one? It’s a personal favorite of mine. It talks about how…"

        JESSE "Uh I really gotta go. I appreciate the thought, but I don’t have the time right now."

        NAR "I quickly make for the door."

        CARTER "Oh well. Be sure to come back soon. I’ll have a perfect pool of books for you to choose from."

        CARTER "Jesse."

        CARTER "I’ll drop it for now."

        NAR "His tone had shifted."

        CARTER "To tell you the truth, I wanted to finish telling you that tale from the other day."

        hide carter
        show jesse

        menu:

            "About Egypt again?":
                hide jesse
                show carter
                CARTER "There is more to say about that! But no."

            "Your cult?":
                hide jesse
                show carter
                CARTER "So you do remember some of the things I say."

            "About plants?":
                hide jesse
                show carter
                CARTER "Planty left to say about that, but no."
                NAR "..."

        CARTER "It’s about the origins of my cult again."

        CARTER "I mentioned I just felt like a tag along until things sort of blew up. I still was for the longest time. I didn’t want to be a part of it’s leadership at all."

        CARTER "Originally of course, It’s been a great job, but anyways."

        CARTER "I only got promoted because those old friends of mine were… well lets just say they poked the bear that is the Guiding Comet with too short of a stick."

        CARTER "If there’s anything I can say to you. It’s to keep your friends. It’s a miracle you haven’t lost any so far. I hope you can keep it that way."

        CARTER "And remember, if you want any specifics on casting anything, I’m your guy."

        JESSE "Thanks… You’re a bit too much most of the time, we wouldn’t be here without you really. I do actually have to go though, this was supposed to be a quick trip."

        CARTER "Then get out of here already, or else I may think of charging late fees."

        JESSE "What?!"

        hide carter
        hide bookstore

        NAR "CARTER RANK MAX
        \n {b}Courage{/b}: [stat_courage]
        \n {b}Knowledge{/b}: [stat_knowledge]
        \n {b}Charm{/b}: [stat_charm]"

    elif(stat_charm < 16):
        NAR "I'm not smooth enough of a talker to face Carter right now. Lets do something else"
        $ hangout_failed = True
        return

    else:
        NAR "Carter doesn't seem to be available... Maybe I should try again later."
        $ hangout_failed = True
        return

    return

label felix_hangout:
    NAR "WIP"
    return

label linden_hangout:
    if(linden_rank == 0):
        $ linden_rank = 1

        scene city
        NAR "I see Linden walking away from the office looking deep in thought. I feel like I don’t really want to talk with him… but I am interested in who he really is…"

        show linden

        LINDEN "Ah Jesse. What brings you to me on this fine afternoon. Could it be that you missed me?"
        hide linden
        show jesse

        menu:
            "{i}Respond sarcastically{/i}":
                hide jesse
                JESSE "Oh most definitely! What would I do without you."
                NAR "He frowns at that last bit"
                show linden

            "{i}Respond truthfully{/i}":
                hide jesse
                JESSE "I came here to talk to you, if that is alright."
                NAR "He smirks at that"
                show linden

            "{i}Stay silent{/i}":
                hide Jesse
                show linden
                LINDEN "Ah the silent treatment. No matter."

        NAR "Linden turns away for a second before looking back at me."

        LINDEN "I know you’re still confused about certain things, but be patient. All will be clear soon."

        JESSE "As cryptic as ever"

        LINDEN "Ah, now it wouldn’t be fun if I wasn’t, now would it. Come talk to me on another day."

        LINDEN "I’m sure we have a lot to discuss. Unfortunately I have matters to attend to at the moment. Until then"

        NAR "I watch as he walks farther and farther away. Something is not right about that man."

        NAR "Didn’t really get much out of that, but it seems like he’s still willing to actually try to talk… maybe make up for that meeting of ours."
        hide city
        $ stat_courage += 1
        NAR "LINDEN RANK [linden_rank]/5
        \n {b}Courage{/b}: [stat_courage]
        \n {b}Knowledge{/b}: [stat_knowledge]
        \n {b}Charm{/b}: [stat_charm]"

    elif(linden_rank == 1):
        $ linden_rank = 2

        scene city

        NAR "On my way to see if I can meet up with Linden"

        NAR "I bump into a body as I walk down the path I am on. I hit the ground with a *thud*. Looking up, I see the familiar face of Linden, as mysterious as ever. Why can’t we have normal meetings."

        show linden

        LINDEN "My boy, do you not look where you are going?"

        NAR "He offers me a hand."
        hide linden
        show jesse

        menu:
            "{i}Take it{/i}":
                hide jesse
                NAR "I grab it and pull myself up."

            "{i}Ignore it and get up myself{/i}":
                NAR "I push his hand to the side and get up myself."
                NAR "He gives me a weird look"

            "{i}Stay on the floor{/i}":
                NAR "People are starting to stare at me as I just lay on the ground. Maybe I should get up…I think as I slowly start to stand."

        NAR "As I dust myself off, I look cautiously at the man in front of me. He didn’t mean to meet me out here did he?"

        LINDEN "There is no need for that look, my boy. Believe it or not, I am not your enemy."

        JESSE "Hard to make friends with someone who could have been my dad’s killer"

        LINDEN "But I’m not remember. I have no ill will against you or Ray"

        NAR "That throws me off guard. It’s been so long since someone has said his name to me…"

        JESSE "Ray…? How did yo-"

        LINDEN "I really must be going now. You know me, always so busy. Until we meet again Jesse"

        NAR "I tried to call up to him to get him to wait up. I thought it’d be a decent time to see him, but apparently not…"

        NAR "He kept walking, just how much work needs to be done when you’re trying to subvert your own workplaces goals?"

        NAR "If I could just actually get a conversation with him…"
        scene date_transition

        $ stat_courage += 1
        NAR "LINDEN RANK [linden_rank]/5
        \n {b}Courage{/b}: [stat_courage]
        \n {b}Knowledge{/b}: [stat_knowledge]
        \n {b}Charm{/b}: [stat_charm]"

    elif(linden_rank == 2):
        $linden_rank = 3

        scene city

        NAR "I went during his break, to see if I could actually get a conversation with him this time…"

        NAR "I see him reading some kind of book. Now would be perfect to talk to him. The last time I bumped into him left me questioning a lot about him."

        show jesse
        menu:
            "{i}Greet him{/i}":
                hide jesse
                show linden
                LINDEN "Jesse, greetings. It’s always a pleasure."

            "{i}shout to get his attention{/i}":
                hide jesse
                NAR "Linden winces at the sound."
                show linden
                LINDEN "Why so worked up boy?"

            "{i}Walk up and wait until he notices you{/i}":
                hide jesse
                show linden
                LINDEN "Ah, Jesse. To what do I owe the pleasure?"


        NAR "I study him for a moment before deciding on what to say."

        JESSE "How did you know him?"

        NAR "He knows exactly what I am talking about, and based on the look on his face, he is hesitant to say anything."

        LINDEN "Ray was an interesting man for sure. We worked together for a bit before...well before he was killed."

        LINDEN "I felt I didn’t have any way to truly prove I was on his side."

        LINDEN "He still seemed to believe in me anyway."

        LINDEN "I only hope that belief didn’t sour when things took a turn… I really hadn’t thought something like that could happen…"

        NAR "We fell silent for a moment. For once, the composed man before me looked almost distraught, before his facade quickly replaced it."

        LINDEN "Well enough of that for today. It’s getting late, and I should go."

        NAR "I wanted to talk to him more, and press him on more about that relationship, but he had to get going, plus this wasn’t exactly the environment for this…"

        scene date_transition

        $ stat_courage += 1
        NAR "LINDEN RANK [linden_rank]/5
        \n {b}Courage{/b}: [stat_courage]
        \n {b}Knowledge{/b}: [stat_knowledge]
        \n {b}Charm{/b}: [stat_charm]"


    elif (current_chapter >= 7 and linden_rank == 3):
        $ linden_rank = 4

        #Chapter 7 lock:

        scene apartment

        NAR "On my way out of the apartment, he actually ran into me this time."

        show linden

        LINDEN "I thought I might find you here"

        JESSE "Linden, why are you here?"

        LINDEN "I came to find you actually. I’ve felt there’s some things I need to say to you alone. Would you like to move the conversation to that Cafe?"

        show cafe

        NAR "We sat down and got something small to eat, as usual…"

        show linden
        LINDEN "You haven’t been well, have you?"

        NAR "I can’t lie to him… he’d see through it pretty easily. He knows too much about the tome…"

        JESSE "All this cult stuff is going to my head. What’s going to happen to all of us? I’m not sure if I’m even capable of doing this in the end…"

        LINDEN "I know it’s tough, but it will get better. You have my word. They will be stopped one way or another, you’re our best option, but even if it’s hard it shouldn’t be impossible to stop them in the future."

        JESSE "Linden… what exactly is your relationship to them?"

        LINDEN "My involvement with the Guiding Comet is a very complicated one. I once found myself devoted to their teachings, believing that I could be more than I ever was."
        LINDEN "...Time has not been kind to me. I know now that I am only human, nothing more. The cultists are delusional in their quest for power. That is why they must be taken down."

        LINDEN "I know you’re unsure of yourself, but I have faith… Even if that’s mainly just because of the faith your father had in you."

        NAR "Took a bit to solidify that faith though…"

        JESSE "I was curious before about that… but who exactly was he to you."

        LINDEN "Your father was an interesting man as I have said before. He was devoted to his investigations more so than his own family."

        LINDEN "And while that isn’t the best of outcomes, it came from a good thought, of trying to protect you."

        LINDEN "The passion he had for his work drew me to him, and I eventually found myself wanting to help him. You remind me a lot of him now."

        LINDEN "Ray was a good man. His death… was something I knew could have happened… And I can’t forgive myself for not trying to make a better plan back then."

        LINDEN "Every way I think about it. Looking back, there was no way for us to succeed without that outcome. However I still wish there was a better way than to entrust you with so much."

        NAR "I had never realized what everything meant to him… I wanted to ask more about what him and my dad did… but I don’t think I need that…"

        LINDEN "You are strong, Jesse. They will not win, I will not make any more mistakes."

        NAR "I give him a nod as we part ways."

        scene date_transition

        NAR "LINDEN RANK [linden_rank]/5
        \n {b}Courage{/b}: [stat_courage]
        \n {b}Knowledge{/b}: [stat_knowledge]
        \n {b}Charm{/b}: [stat_charm]"

    elif(linden_rank == 4):
        $ linden_rank = 5
        scene cafe

        NAR "Linden had called and asked to meet up at the cafe again, alone. He was running really late though, and I was getting a bit bored."

        show linden

        LINDEN "Jesse."

        NAR "Surprised, I turn to find Linden walking over, and he sits down. He looks tired."

        LINDEN "I wanted to check up on you once again. You look worse than before."

        JESSE "You could say that…"

        LINDEN "I’m sorry for contacting you then being late."

        LINDEN "Would you be interested in hearing a story?"

        JESSE "Sure?"

        LINDEN "It’s a story of a young man who didn’t know what to do with his life. You see, he was in a rut very early on in life. He had no money, no family to go back to, and hardly a will to go on."

        LINDEN "The stress became too much so he went to go take care of it in the only way he knew how: by jumping off a large bridge."

        LINDEN "Drastic, I know, but when you are that deep in, your thoughts become clouded. At the last moment, right as he was going to jump, a beacon of hope came."

        LINDEN "For me, that beacon was the guiding comet finding me and offering me a purpose in life."

        JESSE "Why are you telling me this?"

        LINDEN "I’m telling you this for two reasons. One: To show that I am human, and I make mistakes. But I am here to correct those mistakes by helping you do what’s right."
        LINDEN "And Two: I want you to know that life gets hard, but it is worth living if you find your purpose, I know that you have."

        NAR "I look at him in confusion."

        JESSE "Have I?"

        LINDEN "Yes, you have. You live for your friends, for your dad. Finish what he has started, no matter the cost."

        LINDEN "The pain is hard, believe me, I know, but the outcome will be well worth it. I know what you’re being put up to is a lot to ask, but what you will be able to give everyone will be worth it."

        LINDEN "Then… it will be over, and from there you shouldn’t have to worry about anything like this from then on."

        NAR "Maybe he’s right… I really can do this, and I really can survive. However that’s just a bonus isn’t it? Even if I don’t… it’s not just about me."

        JESSE "Thank… you for that Linden."

        JESSE "I will do whatever it takes to stop them, I promise"

        NAR "Linden smiles as he stands up. He looks to me with his hand extended"

        LINDEN "I look forward to it Jesse"

        NAR "I shake his hand."

        scene date_transition

        NAR "LINDEN RANK MAX
        \n {b}Courage{/b}: [stat_courage]
        \n {b}Knowledge{/b}: [stat_knowledge]
        \n {b}Charm{/b}: [stat_charm]"

    else:
        NAR "It seems like he’s been a bit busy from work, I doubt I’ll be able to get time with him"
        $ hangout_failed = True
        return
    return
