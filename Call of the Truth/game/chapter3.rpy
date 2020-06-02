# Chapter 3 begins here

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define LINDEN = Character("Linden")

label chapter3_start:
    $ current_chapter = 3

    #CHAPTER 3: Layers of Despair
    #Plot days: 13
    #Free days: 8

    scene room
    centered "{size=+30}CHAPTER 3: Layers of Despair{/size}"

    call new_day("Thursday, 7th September 1922")
    NAR "The effects of casting was certainly more than I ever expected, not sure what I was expecting though considering the coma. With the way everything has been going…"

    NAR "it’s great that it seems like we can actually do something against them. Who knows, maybe we could actually take care of the entire cult in a few months."

    NAR "I stayed home and relaxed for most of the day, it was nice being with Sara for most of it, since she had off on the days I worked anyway. I also called in and was able to take the next few days off, which would hopefully deter things from being as bad as they were the last time I had done this."
    call new_day("Friday, 8th September 1922")

    scene room

    NAR "Absolutely, Dreadfully tired. But conscious still, which is a positive at the very least. The benefit is that I can still move and do things, which is a significant step forward from what happened last time, and if I’m not working like last time…"
    NAR "I might not pass out after today too. My plan was to relax for the entire day as usual but…"

    show sara

    SARA "Hey, since you’re free today, you up for something interesting that I’ve heard is happening today?"
    hide sara
    show jesse

    menu:
        "What is it?":
            hide jesse
            show sara
            SARA "Oh it’s pretty interesting, not sure how much we’ll be able to see of it though."

        "I’m a bit tired.":
            hide jesse
            show sara
            SARA "Don’t worry, it’s just a bit of walking, or do you want to go back to bed already?"

        "Sure.":
            hide jesse
            show sara
            SARA "Awesome."

    SARA "The King’s cup started today. It’s a race between aeroplane pilots, and they go from here, to glasgow, and back. We’ll be able to catch the last part of the race and see them land back here in person."

    hide sara

    NAR "Huh… doesn’t seem too bad, and it’s not like I’m going to do anything else today, if anything it’s an opportunity to spend time with her. Also… isn’t there something relevant with glasgow? No, nevermind that…"

    scene date_transition

    NAR "We spent the majority of the day going out and watching the event. The winner was able to fly there and back in under seven hours…"
    NAR "I don’t know much about the race or how impressive that really is, but it was still incredible to see. I…  had to find a chair after standing for too long in my condition though."

    scene room

    NAR "After we got back home…"

    show sara

    SARA "You know… besides overexerting yourself… are you actually having fun again?"
    hide sara
    show jesse

    menu:
        "Sort of…":
            hide jesse
            show sara
            SARA "I’m glad!"

        "What makes you say that…":
            hide jesse
            show sara
            SARA "Well, you don’t look so sad anymore for one."

        "Not really…":
            hide jesse
            show sara
            SARA "Oh come on, it can’t all be a mask?"

    SARA "Seems like that mentor thing has actually had some benefits hasn’t it? Plus I know you’ve been in contact with your friend again for so long… maybe that’s what you needed all along…"

    SARA "Hey, so on a more serious note… I know your branch of work is a lot easier and just basically busy work… but my position has become a lot more stressful, they’ve been expecting far too much from me, and I’m not sure if I can keep up with it…"
    hide sara
    show jesse

    menu:
        "I’m sure you’re up for it.":
            hide jesse
            show sara
            SARA "I’m glad someone is confident in me…"

        "Do you want to stop?":
            hide jesse
            show sara
            SARA "I’m not sure…"

        "Are you doing okay?":
            hide jesse
            show sara
            SARA "Oh yeah, I’m fine besides that!"

    SARA "But I don’t know… I think if it keeps going on like this I feel like I should just quit… the things they’re wanting me to do is just being a bit too much for what it’s worth, and I’m not sure if I’m okay with that…"

    SARA "Oh it’s not as serious as I’m making it out to be! It’s just like a more managerial position… I’ve had to actually fire some people from the place, when they really didn’t do anything too bad."
    SARA "But I’m sorry for bringing that up, I won’t do anything with that unless I get an alternative, I’m not just gonna room here for free right?"

    SARA "Speaking of that… it’s been almost three months hasn’t it… I…"

    SARA "I may have lied originally about why I wanted to stay here. I Don’t know if I’ve told you, but I originally got to where I am in my job because of my parents, they were both a part of the company too."

    SARA "But four months ago they were let go. They never had the best relationship with each other, and that only got worse… but when I was the only one still with them, they started to point more of their anger towards me… So I just wanted to get out."
    hide sara
    show jesse

    menu:
        "I Don’t know what to say.":
            hide jesse
            show sara
            SARA "No, it’s fine, and I know parents is a touchy subject for you…"

        "I’m sorry.":
            hide jesse
            show sara
            SARA "Thanks… but it’s not like you have been involved right haha."

        "You can keep living here.":
            hide jesse
            show sara
            SARA "Thank you, and that’s why I still want to pay my share."

    SARA "That being said, it’s a part of the reason I’m not sure if I want to quit… but… No I shouldn’t worry you with that too much, I’ll figure it out, thanks for letting me talk at you."

    NAR "SARA RANK 3/7"

    scene date_transition

    NAR "I’m happy she’s being more truthful with me… but… I couldn’t do the same with her, I couldn’t make her worry more than usual… and there’s always that one possibility… no, I don’t want to think of that."

    call new_day("Saturday, 9th September, 1922")
    call half_free_day
    #Walk
    #Study
    #Gardening
    call new_day("Sunday, 10th September 1922")
    NAR "I was actually starting to feel better after relaxing for the past two days. I’ve actually been feeling better in general too, feeling like I’m actually making progress too."

    scene cafe

    NAR "If anything, that’s something I could talk to him about. I met up with him at the Cafe. again."

    show luke

    LUKE "Hey Jesse, how have you been?"
    hide luke
    show jesse

    menu:
        "Better actually.":
            hide jesse
            show luke
            LUKE "Glad you’re feeling better."

        "Doing good.":
            hide jesse
            show luke
            LUKE "That’s good to hear"

        "Could be better.":
            hide jesse
            show luke
            LUKE "It always could, but the ‘now’ is important too."

    LUKE "It’s been a while since we last talked, since you were working the last time. That was also in the hospital too, Haven’t gotten the chance to speak ever since you’ve gotten out. I’m happy to see you out and about again though."

    JESSE "About what you asked me before, about how far I wanted to go through with my friends. I was definitely unsure at the time, but even then, I think I do have an answer now."

    JESSE "You asked me before just to confirm with myself how far I wanted to go, and I think I’m willing to go all the way if they're with me."

    LUKE "Interesting take on that, and I’m happy you were able to find your own conclusion to that. That’s a good view of things, but just to keep you thinking…"

    LUKE "Are you only willing to go along with everything just because of them? There could be a time where you won’t be able to be with them to see things through."

    NAR "LUKE RANK 3/10"

    LUKE "With that however, I’m afraid we won’t be able to meet for about a month. The next time I’ll be free is a bit into October. However, I don’t think you’ll need me for that time."

    LUKE "If you're curious, A friend of mine is setting up a wedding, and he’s invited me to be his best man, it’s hardly an offer I could refuse… even if it did mean disappointing some other friends of mine."
    hide luke
    show jesse

    menu:
        "That’s fine.":
            hide jesse
            show luke
            LUKE "I’m happy you understand."

        "Have fun.":
            hide jesse
            show luke
            LUKE "Yeah, I think it will be a good time."

        "A shame…":
            hide jesse
            show luke
            LUKE "I’m sorry Jesse, but it won’t be for too long really."

    hide luke

    scene date_transition

    NAR "With that, we talked a bit longer, but eventually I parted ways with him and went back home."

    call new_day("Monday, 11th September 1922")
    NAR "The next day marked a turning point for the next couple of weeks for me. Sara would be staying home from work until October 18th, because of some internal changes."

    NAR "It would turn out that it was accommodations made for a promotion she was receiving with the company, but it would take some time."

    NAR "Contacting everybody when I could, it seemed like things in general were becoming more peaceful."

    NAR "I wouldn’t have the book for quite some time either as it was in Evelyn’s possession, which would turn out to be a good thing over the course of the next month or so."

    NAR "Not much occurred in those weeks, nor was I as free as usual from Sara not having anything scheduled. The next time anything of note would happen was…"

    call new_day("Tuesday, 17th October 1922")

    scene room

    NAR "What started off as a usual day changed a little when Sara was looking at the newspaper for the day."

    show sara
    SARA "Hey, something interesting we could go and do, it seems like there’s this hunger march thing coming down from Glasgow that's gonna be in London today. Could be something to get us out of the house, just to do something you know."
    hide sara
    show jesse

    menu:
        "Not against it.":
            hide jesse
            show sara
            SARA "Yeah, it’s something remotely interesting right?"

        "Why not, been boring.":
            hide jesse
            show sara
            SARA "Cool, I’ll figure out the specifics."

        "Why now?":
            hide jesse
            show sara
            SARA "I dunno, seems like it could be historic you know."

    NAR "I mean, it doesn’t really sound that interesting, but it’s something to do. Maybe going to a place filled with people could give us some idea of what's happening with the cult…"

    NAR "Even from the smaller talks with my friends it doesn’t seem like much is going on."

    hide sara

    scene city

    NAR "We arrived, and it’s what you would expect, just a larger gathering, but it was interesting at least. In the middle of things however, I did get separated from Sara for a bit, not sure exactly where exactly she went… "

    NAR "While I was trying to find where she was, I scanned through the crowd, and found… Felix? It seemed like he was spying on people here, I’m kind of interested in what he’s doing…"

    NAR "Behind me, a man grabs my shoulder, turning around it was someone who had traveled here from Scotland."

    show linden

    LINDEN "Hello there, my name is Linden Banks, and you are?"
    hide linden
    show jesse

    menu:
        "Excuse me?":
            hide jesse
            show linden
            LINDEN "You are excused."

        "Hello stranger, do I know you?":
            hide jesse
            show linden
            LINDEN "You do not, no."

        "What if I didn’t?":
            hide jesse
            show linden
            LINDEN "Then our relationship starts off poorly."

    LINDEN "Jesse Stout, I’m afraid I already know who you are. However it would be remiss to ignore formalities."

    NAR "I back away from him."

    JESSE "Okay then, I’d appreciate it if you could give me some reason to trust a random stranger, you know you can’t do anything in this crowd right?"

    LINDEN "You have no reason to trust me. You don’t need to right now either. I wouldn’t think of doing anything here either of course."

    JESSE "Then why are you here? If you want some tea I could show you some good places, it looks like you’re new here right? You can visit the sites, and get away from me."

    LINDEN "Hm, I understand the rudeness, but we both have places to be. I’m afraid I’m not new here either, although it has been a while. I’ll skip the formalities, I’ll meet with you on the 31st, and you will give me the tome."

    NAR "Startled, I approached more aggressively."

    JESSE "What… the hell do you know."

    LINDEN "Careful Jesse, wouldn’t want to try anything in this crowd right? I hope you’ll be ready. Don’t try to bring your friends if you value their lives either. Goodbye."

    hide linden

    NAR "He… who the hell was he… what is he doing… I want to try and stop him, but he’s right I can’t do anything right here, and it’s not like I could fight him right here…"


    NAR "Felix! He’s around here right? I can try and find him. I went through the crowd and caught up with him."

    JESSE "Roark!"

    show felix

    FELIX "Stout? Why are you here, and don’t get in my way."

    JESSE "I just decided to come, but why are you here?"

    FELIX "Doing my job? More so than anything you’ve done… now then stop distracting me."

    JESSE "Okay, listen to me for a second then, Linden Banks, he approached me in the middle of this, and…"

    NAR "His words… he had threatened everybody, is it safe to just talk about it like this openly to everybody? It’s fine, Felix at least would figure it out anyway."

    JESSE "He knows I have the tome, and is threatening me to give it to him. He also threatened all of us if I tried to get anybody involved."

    FELIX "I’m glad you value my life then Stout, trust me I’d do the same for you."
    hide felix
    show jesse

    menu:
        "Your welcome.":
            hide jesse
            show felix
            FELIX "Don’t push it Stout."

        "It’s what friends are for.":
            hide jesse
            show felix
            FELIX "It’s cute that you think we’re friends"

        "Stop messing around.":
            hide jesse
            show felix
            FELIX "Not up for jokes."

    FELIX "Either way, I knew there was going to be some people from the cult coming down from Glasgow. That’s actually a competent lead. Where is he?"

    NAR "I told him I lost him in the crowd then went to look for him since I saw him earlier, but I did explain to him what he looked like."

    FELIX "Maybe being the bait is what suits you best."

    JESSE "I’d rather not be, if you’re gonna keep delving into things, you’ll probably become a bigger target than me."

    FELIX "So i’ll be better at even more things."

    JESSE "Are you going to tail him or not."

    FELIX "Oh not up for it?"

    JESSE "I can’t just ditch my flatmate here…"

    FELIX "Mmhmm."

    hide felix

    NAR "He left, and I caught back up with Sara, I didn’t tell her of anything that happened, but I did mention I ran into a friend, but he had to go…"

    scene date_transition

    NAR "I hope he comes up with something, I need to try and contact that guy before the 31st right? I can’t just give it to him… Sara has work tomorrow, it’s finally a time to meet with everybody again."
    call new_day("Wednesday, 18th October 1922")

    scene bookstore

    NAR "Finally for the first day in quite a while, I was able to meet up with everybody at Wilkinson’s book store again."

    NAR "It was nice to see everybody again, and most of our talk was just catching up, we had kept in touch slightly, but I had never been able to meet up with everybody."

    show carter

    CARTER "My friends, my comrades, my compatriots, I’m sure you all are wondering the greater meaning to us joining together on this fateful day."

    JESSE "Not… particularly?"

    CARTER "Well you see, after ten thousand years-"
    hide carter
    show evelyn

    EVELYN "he means like three weeks."
    hide evelyn
    show carter

    NAR "He clears his throat."

    CARTER "After approximately three long weeks, we have made progress into the mysteries of this dark and foreboding tome of the elder gods, and soon the moves of the cult will be brought to light, as their next move begins…"
    hide carter
    show evelyn

    EVELYN "Translation: we found some way to decipher the book, and we also think the cult is going to start making moves relatively soon again."
    hide evelyn
    show finn

    FINN "Yeah, there hasn’t been much progress since what we did in september."

    JESSE "Is it really that exciting to be acting like that Wilkinson."
    hide finn
    show carter

    CARTER "I will be allowed to act however I wish in my residence."

    NAR "There’s a knock on the door."

    CARTER "Ah, a surprise, a shame though, I’m keeping it closed whenever you guys are around, it’d scare them off completely if they saw you kids."
    hide carter
    show finn

    FINN "You’re one to talk… surprised you don’t scare anybody away already."


    NAR "Before the conversation could continue, we heard a voice muffled behind the door."

    hide finn

    FELIX "I know you’re not actually closed. Come on and open up."

    show carter

    CARTER "I’m sorry but we are, I’m sorry if you cannot read."
    hide carter
    show evelyn

    EVELYN "Wilkinson, don’t. That sounds like someone we know, it’s fine."
    hide evelyn
    show jesse

    menu:
        "Keep it closed.":
            hide jesse
            show carter
            CARTER "Just for you, I’ll open it then."

        "Let him in.":
            hide jesse
            show carter
            CARTER "Fine."

        "Oh great, Felix.":
            hide jesse
            show carter
            CARTER "Oh, that kind of friend huh?"

    NAR "He went over and let Felix in."
    hide carter
    show felix

    FELIX "Hello, nice you meet you. My name is Felix Roark and I hope you’ll allow me to be here."
    hide felix
    show carter

    CARTER "Oh huh he’s got manners. Sure whatever."
    hide carter
    show felix

    FELIX "To start with things, I’d like to request to be a part of these meetings, our goals to aline and it’d be beneficial to all of us if we could work things out with each other like this."

    NAR "No."
    hide felix
    show finn

    FINN "Sure, it’d be great to have you a part of the cause too!"

    NAR "God damn it."

    JESSE "Alright so what’s up, I figure you were able to get some information on what happened yesterday?"
    hide finn
    show evelyn

    EVELYN "Yesterday? Did something happen?"

    JESSE "I assume as long as no one gets physically involved, you’ll be safe so…"
    hide evelyn
    show felix

    FELIX "Stout was approached by a stranger, who knew he had the tome and was threatening him to give it to him at the end of the month."

    FELIX "So, I looked into it since Jesse was preoccupied. Jesse sit down."

    JESSE "I am?"

    FELIX "he’s the man who killed your father."

    NAR "Excuse me?"

    JESSE "What… Do you mean by that."

    FELIX "He’s a part of the cult, and during his stay up in Scotland he was involved in the incident that was related to the original case that was how your father died."

    JESSE "That’s how he knows I have the book… and now that he’s back in London…"

    NAR "There’s this rage building inside me… It was him… he just approached me so normally… who the hell does he think he is? Just… stay calm…"
    hide felix
    show finn

    FINN "Then we’ve got to do something right!"
    hide finn
    show felix

    FELIX "Not exactly, he’s apparently threatened to kill all of us if we get too involved too. Which probably just translates to if we try to mess with their meeting."
    hide felix
    show finn

    FINN "So… what do we do…"

    hide finn

    NAR "Kill him. No… That can’t just be the solution…"

    show felix

    FELIX "We think about this. If he came down, and already knew about Jesse, and presumably us. Why did he go through the effort of confronting Jesse? Why are we all still alive if he could have just alerted everyone about it?"
    hide felix
    show evelyn

    EVELYN "So you’re suggesting that he has some ulterior motive?"
    hide evelyn
    show felix

    FELIX "Yeah, and that’s basically our best way to proceed, we need you to figure out what he wants in that meeting. And to be clear, we’re not giving up the tome to him, that’s the one thing we have against them."
    hide felix
    show carter

    CARTER "Oh my god we’re back on topic."
    hide carter
    show felix

    FELIX "What?"
    hide felix

    show carter

    CARTER "Before you barged in, I never got to finish what I was saying. This conversation is basically over isn’t it?"

    JESSE "Basically yeah, we just wait until he visits me and figure it out from there, and meanwhile everyone sits around and tries to get info on my dad’s killer, sounds great."
    hide carter
    show finn

    FINN "Jesse…"
    hide finn
    show carter

    CARTER "Okay great, back to magic. I’m only gonna say this once, and there’s a quiz at the end, so listen."

    hide Carter

    NAR "There wasn’t a quiz. However Wilkinson explained a whole lot of what they learned about the tome we had. They had found a way to start decoding the glyphs on the tome, due to Wilkinson’s connections and Evelyn’s research."

    NAR "The basics of what they found out is how to use every spell on the scraps of paper that my dad left me. The entire second half of the book is a collection of spells that were already used on the tome."

    NAR "The reason that’s important, is that each page can only be used once, so that entire half of the book is essentially useless."

    NAR "Additionally, after looking into it further, the two torn pages from the front seem even more impossible, as it needs an immense power to be able to damage this, far beyond human capabilities."

    NAR "A few of the notable spells that were on the scraps of paper, were another dispel magic, a rewind spell that turned back time, an explosive fire spell, and an invisibility spell."
    NAR "I would scribe them into the book when I got the time and practice."

    NAR "Otherwise I was a bit distracted by this new information on Linden… but there was not much to do besides wait."

    hide bookstore

    NAR "The rest of the night proceeded normally, with a healthy amount of stifled anger."

    call work_day("Thursday, 19th October 1922")

    call work_day("Friday, 20th October 1922")

    call new_day("Saturday, 21st October 1922")
    call half_free_day
    #Walk
    #Study
    #Gardening

    call work_day("Sunday, 22nd October 1922")

    call new_day("Monday, 23rd October 1922")
    label free_day_10_23:
    call free_day("courage", "Felix", "Evelyn")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Felix"
            call felix_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Evelyn"
            call evelyn_hangout

    if(hangout_failed):
        jump free_day_10_23
    #Felix
    #Evelyn
    #Walk

    call new_day("Tuesday, 24th October 1922")
    label free_day_10_24:
    call free_day("knowledge", "Felix", "Carter")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Felix"
            call felix_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Carter"
            call carter_hangout

    if(hangout_failed):
        jump free_day_10_24
    #Felix
    #Carter
    #Study
    call new_day("Wednesday, 25th October 1922")

    scene museum

    NAR "It had been some time, but today was another time to meet up with Luke… I may actually need it this time. I met with him at the Museum this time."

    show luke

    LUKE "Hello Jesse… It’s been a bit hasn’t it. I’ll start by saying it turned out it wasn’t as great as I thought it’d be."

    LUKE "Not to say it was bad, I still had a good time. It started to remind me of some things I’d forgotten about, but it was nice to be reminded of that, after all I wouldn’t be here without that happening in the first place. Now then, that’s it from me."
    LUKE "How are you?"
    hide luke
    show jesse

    menu:
        "Worried…":
            hide jesse
            show luke
            LUKE "I’m sorry to hear that."

        "Been better…":
            hide jesse
            show luke
            LUKE "Worse than last time?"

        "Okay.":
            hide jesse
            show luke
            LUKE "Hmm."

    LUKE "I take it a lot has been happening since I left? I was under the impression that things were about to be pretty peaceful for you."

    JESSE "Not exactly, well yeah they were. Only recently though, something pretty big came up, and it’s like you were saying, being reminded of stuff after so long… it’s like you almost forget about it."

    LUKE "So it’s come back to haunt you in a sense? Your dad I mean."

    JESSE "Partly… it’s more, I’m conflicted. That’s not the current issue however, there’s been some… complications with my friends and how we’ve been doing."

    JESSE "I’m angry, but I’m not sure if I want to act on it, or if doing anything like that would actually be useful."

    LUKE "If it’s someone you think you can trust… getting angry probably isn’t the answer. You can talk it out. If it’s someone you dislike, you should try and manage that, and try not to vilify yourself just out of hate for them."

    LUKE "There’s too many cases and what ifs, and I’m not about to guess, nor am I going to make you talk about it if you don’t want to. All I’d say, make sure you don’t do anything you’d regret."

    hide luke

    NAR "LUKE RANK 4/10"

    NAR "The conversation eventually reached it’s natural ending point, but that was the last meaningful thing I felt. Something I’d regret… I want to kill him… He’s the reason for all of this?!"

    NAR "I can’t just do that can I… and the consequences of it… But what if I just let him go, and do as he asked, or find that secondary thing that Felix thinks there is…"

    NAR "could I forgive myself for missing an opportunity like this? They returned the tome to me, in case I needed it for surviving a confrontation with Linden, not for fighting him…"

    NAR "But he’s threatened everyone too… I need time to think…"

    scene date_transition

    NAR "Work tomorrow though…"

    call work_day("Thursday, 26th October 1922")

    call work_day("Friday, 27th October 1922")

    call new_day("Saturday, 28th October 1922")
    call half_free_day
    #Walk
    #Study
    #Gardening

    call work_day("Sunday, 29th October 1922")
    call new_day("Monday, 30th October 1922")

    scene park

    NAR "I decided to go to the park today… to clear my head. Tomorrow was the big day, he said he’d meet with me. I’d like to assume he would come to my house, he seemed confident enough for that too."

    NAR "I’m not giving him the tome… but I can’t just let him go free and listen to his reasons for not having us killed already can I? What would Felix berate me for in that thinking…"

    NAR "‘Think about the bigger picture, stop being useless because of your feelings.’"

    NAR "Luke told me not to do anything I’d regret, but I don’t know what I’d regret more… I started to overhear a kid behind me."

    NAR "A little girl, no more than eight years old. They were talking about and showing a drawing they did to their dad. It was probably chicken scratch, they’re a child…"

    NAR "Just seeing that again though… a loving dad… I miss that… except he wasn’t even there that much… all because of this cult, it’s all their fault, and he’d be done with this if it wasn’t for that man…"

    NAR "Oh my god I couldn’t listen to that family behind me anymore, it was too much. That kid will never have to experience what I’ve been through."
    NAR "Even Sara and everybody, I don’t even know all of their relationships with their parents, but at least they have them. I don’t care what Linden is after. I need this."

    NAR "As I was walking away, I saw Finn… was he coming to check up on me? How’d he know I would be here… although I guess it’s not too weird considering he knew how this would get to me…"

    JESSE "You here to convince me not to kill him? I know no one would agree with me. I can’t just look past these feelings, especially not when I have this opportunity."

    show finn

    FINN "I was talking with him. Just before he died. I’d known he was murdered ever since the beginning. I was angry I couldn’t do anything back then, that I couldn’t try and help your dad after everything he did for me… let alone for you."

    FINN "I can’t possibly compare to how it feels to lose him, but being the last person he talked to… when I know if I was more available he could have been saved…"

    JESSE "What are you trying to say?"

    NAR "He pulled out a pistol from under his coat, and held it out to me."

    FINN "I can’t be there or else he’ll do something, but you… you can kill him. I’m with you Jesse, and it doesn’t matter what else he’s up to, he killed him."

    JESSE "Thank… you… But are you sure this is what we need to do?"

    FINN "I’m not… and I don’t want to force this onto you, but it’s what I want… and if it’s what you want."

    NAR "I took the gun from him, and gave him a nod. We parted after that, and I returned home."

    hide finn

    scene date_transition

    NAR "My day continued in premeditation…"

    call new_day("Tuesday, 31st October 1922")

    scene room

    NAR "Today was the day, Linden would come for the book… I sat there… waiting. I hid the tome away so that he wouldn’t be able to see it, worst case scenario I can just go and grab it."

    NAR "Besides, I have the gun from Finn… I’ve shot before… I don’t think what I did when I was younger really counts though… this’ll be easy though, I can picture it. I sat there on the couch waiting and thinking…"

    NAR "There was a knock on the door. I went up, and calmly opened it… it was time."

    NAR "What the hell it was Felix."

    show jesse

    menu:
        "The hell are you doing.":
            hide jesse
            show felix
            FELIX "Talking some sense into you."

        "Why are you here?":
            hide jesse
            show felix
            FELIX "To talk."

        "Did you forget?":
            hide jesse
            show felix
            FELIX "Not in the slightest."

    FELIX "You don’t think I realize what you’re planning right? I questioned everybody about their feelings for this and I know what Finn was thinking."

    JESSE "Then why the hell are you here at the eleventh hour?!"

    FELIX "Because it’s time to make a decision."

    JESSE "And I have you asshole."

    FELIX "What you’re thinking of doing is stupid."

    JESSE "I’m not talking to you at the door, get inside before you start yelling."

    NAR "He came inside and sat down."

    FELIX "I’m not planning on being long"

    JESSE "Yeah you better not be, or else you’ll die when he shows up."

    FELIX "That’s not true, we don’t know what he’s planning."

    JESSE "You want some coffee?"

    FELIX "Yes, but don’t you keep trying to stop talking about this. What you’re planning right now is insane, what do you think will happen out of it?"

    JESSE "I’ll get revenge, and we’ll kill someone important to the cult."

    FELIX "No you idiot, you’ll either get killed or arrested for premeditated murder!"

    JESSE "I know that could happen, but what of the alternative? What if we just let him go and he does decide to do something! We know he hasn’t told anybody about us having the tome, you said so yourself."

    FELIX "Think about the bigger picture, stop being useless because of your feelings."

    JESSE "Knew you’d say that…"

    FELIX "So you can think!? So you’re just ignoring it anyway?"

    FELIX "You’re an angsty kid with daddy issues and because of that tome, you have enough firepower to take out the entire Queen’s Cavalry if you only knew the right words to say."

    JESSE "Without me, none of this would have even started, just shut up and let me complete this one my own, you understand what it takes to commit to this, you’re not going to change my mind."

    FELIX "You’re never going to be the person who’s up for this, you’re not an investigator like me, and you’re not your father."

    JESSE "Yeah because I’m not dead dammit!"

    FELIX "He’d be disappointed in this."

    JESSE "I’ve never cared about your opinion."

    FELIX "I had hope you were better than this, but I guess I knew better than to have hope in someone like you."

    JESSE "So, are you going to leave soon?"

    FELIX "I said I wasn’t leaving until I convinced you not to attack our best lead!"

    JESSE "You’re coffee is done by the way."

    NAR "I walked over with it, and accidentally spilled it next to him, some of it got onto him, and he got up with the pain."

    FELIX "What the hell Stout?!"

    JESSE "Get out of my house."

    FELIX "I’m not going to get myself killed because you can’t keep yourself together. I looked up to him too! More than you could ever know! I wanted this man dead since the moment I learned he was a part of it!"

    FELIX "The difference, Jesse. Is I give a damn about what your dad sacrificed his life for."

    JESSE "Out. of my house. This is my thing to deal with."

    FELIX "Fine Jesse, but if you have any hope in us doing more than inconveniencing the organization that did all this to us you’ll-"

    JESSE "Just leave already."

    FELIX "Goodbye Jesse. This apple fell from the tree… off a canyon."

    hide felix

    NAR "He left. Thank god… I can’t deal with him… not right now not like this… I better clean up this spill. Back to waiting for Linden."

    NAR "It doesn’t matter, if he’s dead then they can’t find anything out, I can use a spell to remove him completely when he’s dead, I’m sure Wilkinson knows how to do that, he’s that kind of evil. God damn it all."

    NAR "A few hours later, another knock on the door. I had cleaned up everything. I welcomed the man of hour, Linden into my home. The man who killed my father in my own home. Felix could never understand what that feels like."

    show linden

    LINDEN "Hello Jesse. Have you made your decision? Will you give up the tome peacefully, or will we have to resort to greater measures."

    JESSE "About that Linden… I can call you that right?"

    LINDEN "I don’t mind at all, in fact I’d prefer it."

    JESSE "Good, don’t want this to be hard on you…"

    LINDEN "Jesse, there’s no reason to carry this on. The tome, will you be giving it to me."

    JESSE "Yeah, I have a lot I want to say to you, but this is the easiest way…"

    NAR "I pulled out the gun and lined it up with his chest, center mass will kill, especially with multiple shots. Linden was shocked, I bet he didn’t think I had it in me! This is for my dad…"

    NAR "Bang!"

    NAR "Bang!"

    NAR "...what… the hell?"

    LINDEN "To think you’d go this far against me. What was that for."

    NAR "It… it didn’t hurt him at all… I was about to fire again."

    LINDEN "Stop this nonsense, or have you thought of a way to explain gunshots to your neighbors!?"

    NAR "How…"

    hide linden

    NAR "There was a knock on the door that Linden quickly went to, and made some bullshit excuse on the loud popping noises…"

    JESSE "How… are you…"

    NAR "I slumped back into the couch… how could I not kill him?"

    show linden

    LINDEN "A similar spell to what you’ve used, the shield one if you recall. It’s much weaker than what you managed, but it’s more than enough to deal with bullets for a single target."

    JESSE "You knew I’d attack you as revenge for my dad… You murderer I know that spell can’t withstand everything!"

    NAR "I stood back up ready to fire… I could do this then grab the spell book… there’s no way it’d survive something from that book… that fire spell…"

    LINDEN "Oh… No, I didn’t think you’d strike me, but I respect it."
    LINDEN "Before you start thinking about the power you have that’s more than a pistol, think about how’d you survive that, there’s people that can come pick it up from your charred corpse."

    NAR "He… He’s right…"

    LINDEN "However I take it that your answer is a no. So you wish to prove that you deserve to wield that tome in the first place do you?"
    LINDEN "So in that case, you wish to rebel against us, even if it’s foolish. It appears I did underestimate you."

    NAR "I just need to wait for the spell to wear off… then I can still shoot him…"

    LINDEN "To finish this conversation before the spell wears off… I trust you’re smart enough to not just leave it here, so killing you has no meaning right now when we don’t know where it is. I’ll let you keep it."

    JESSE "What…"

    LINDEN "Because it appears you need more motivation to hand it over. November 14th. One of your friends in that group of yours will die. I will have them attacked, and they could survive… if you told them about it."
    LINDEN "Which is why if you involve yourself directly with their protection. I will kill them immediately, I have my ways of knowing."

    JESSE "You son of a bitch… the hell do you want"

    LINDEN "I want the tome. I will give you a final opportunity to give it to me during lunch on the 13th. However, if you have the resolve to sacrifice a companion for it, I’ll let you keep it."
    LINDEN "To add to that, I’ll even have you choose which one I’ll have attacked."

    JESSE "Why the hell would I agree to that you bastard?"

    LINDEN "You could call it a test, and besides you need something to live for don’t you?"

    LINDEN "Oh and as a final thing Jesse. I will be transferring into a management position, replacing your boss at work by the weekend, so don’t try anything tricky."

    JESSE "Who the hell are you?"

    LINDEN "Exactly what you think I am. Anyway, it looks like it’s about the time I should get going however."

    hide linden

    NAR "He exited the room, before I could chase after him, I bolted to the door he closed and tried to open it… but it was locked?! Behind the door he speaks again."

    LINDEN "Sorry, I’m not taking chances with you, this will fade after an hour, but until then I’ve magically locked you in. I’ll see you on the 14th."

    scene date_transition

    NAR "I couldn’t help but just scream. I contacted Evelyn and Wilkinson later and told them that I didn’t have to give up the tome, and not to worry about Linden for now."

    NAR "I’d give Finn back his gun the next time I saw him. I needed some time to calm down. I don’t feel like talking to anyone tomorrow…"

    NAR "The rest of the day was filled with as much failure."

    call new_day("Wednesday, 1st November 1922")
    call half_free_day
    #Walk
    #Study
    #Gardening

    call work_day("Thursday, 2nd November 1922")

    call work_day("Friday, 3rd November 1922")

    call new_day("Saturday, 4th November 1922")
    call half_free_day

    call work_day("Sunday, 5th November 1922")

    call new_day("Monday, 6th November 1922")
    label free_day_11_6:
    call free_day("courage", "Carter", "Evelyn")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Carter"
            call carter_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Evelyn"
            call evelyn_hangout

    if(hangout_failed):
        jump free_day_11_6
    #Carter
    #Evelyn
    #Walk
    call new_day("Tuesday, 7th November 1922")
    NAR "It has been a week since Linden contacted me… I can’t just let things end like that with him, besides it’s not over. He was going to kill someone in a week from today too…"

    NAR "What the hell am I supposed to do, and I can’t exactly bring it up to everybody… I was able to play off what happened with him before, but I can’t just leave everybody in the dark about it."

    scene bookstore

    NAR "The group was called together to Wilkinson’s again today… I was too distracted to pay too much attention though. Something about the cult’s next move becoming more and more obvious, trying to install a politician or something…"

    NAR "It’d be great if we could stop that, but it’s not like we can get into politics… Besides, what does it matter when I can’t do anything about Linden."

    NAR "The others did start to notice something wrong with me, but I bet Felix already told them about everything that I was going through, I doubt they think much of me anymore either… Even if they are feigning care for me."

    NAR "Before I could finally leave and get out of there. Felix pulled me aside."

    show felix

    FELIX "Look, things were rough between us last week, and I’m not about to apologize for any of it. Nor do I expect you to."

    FELIX "But Stout… thank you for not killing him, this is the better outcome. We’ll make sure he faces justice in the end."

    FELIX "I’m not going to pretend we don’t know something else is up. It’s clear that you and him are still involved, I need you to take advantage of that. You’re the only one he’ll think about contacting."

    hide felix
    NAR "Yeah, wonderful. The only reason he isn’t dead is because I’m terrible. This has only made the situation worse… I acknowledged what he said, then started to head home."

    hide bookstore

    NAR "..."
    call new_day("Wednesday, 8th November 1922")

    scene room
    NAR "It was a normal day at home alone. I just needed time to think today though…"

    NAR "Making coffee to start my morning. I remind myself of how I was acting when Felix showed up a week ago. He’s not exactly my favorite person. He was worried about me though. Because he didn’t trust me."

    NAR "Still, the way I acted was a bit much wasn’t it… Now everyone probably knows there's more to what's happening, but I’m hiding it from them. Just like how I’m hiding my arm."

    NAR "No, that’s different, I just don’t want to worry them about that, this will actually get them killed."

    NAR "It could have been an empty threat… but if Linden is one of my managers at work… I can’t trust anything around me. If all he wants is the tome… why is he going through all of this? Does he just hate me?"

    NAR "It’s not like I can do anything to stop him at this point… sure I’m the only one that can talk to him, but what good does that do, I guess I can tell him to just kill Felix so I don’t have to deal with him anymore."

    NAR "No, don’t think like that… I’ll just give him the tome on that day, then it’ll be fine right? But what about everything we’ve been doing already…"

    NAR "I can’t even talk to Luke before all of this because of work… I just don’t want to think about this anymore."

    NAR "Maybe things will just work out right?! I haven’t had to work too hard for everything that’s happened so far… because of everyone else’s efforts…"

    scene date_transition

    NAR "I have work tomorrow."

    NAR "..."

    call work_day("Thursday, 9th November 1922")

    call work_day("Friday, 10th November 1922")


    call new_day("Saturday, 11th November 1922")

    scene room

    NAR "It was an average Saturday, wrought with doubt and worry that continued to wrack inside my brain. All of which is interrupted by Sara."

    show sara

    SARA "Hey I was thinking… Want to get a Television set? It’s looking like the BBC is about to start airing stuff soon, so it could be a fun investment."

    SARA "And besides, I’ve got plenty of disposable income since the promotion, mine as well put it towards something we can both use right?"
    hide sara
    show jesse

    menu:
        "Wouldn’t be against it.":
            hide jesse
            show sara
            SARA "I knew you’d be interested."

        "Are you sure?":
            hide jesse
            show sara
            SARA "Yeah, It’s worth it."

        "I could pitch in too.":
            hide jesse
            show sara
            SARA "No, don’t worry about it!"

    SARA "We could go and pick it up later today. But I wanted to ask, are you doing alright? I know I’ve been busier since they actually decided to make work worth my time…"

    SARA "But I guess that’s also distracted me from how you’ve been doing recently. Considering where I am, I could try and get you some time off if you’d want to have more free time…"

    JESSE "No, it’s fine… Just a lot has been on my mind, and I haven’t been able to figure it out so far…"

    SARA "You can talk to me about it if you want, I can keep a secret you know."
    hide sara
    show jesse

    menu:
        "Sorry, I can’t.":
            hide jesse
            show sara
            SARA "Alright then… "

        "It’s something I have to do alone.":
            hide jesse
            show sara
            SARA "Hm… well I know you’ll figure it out."

        "You wouldn’t be able to help.":
            hide jesse
            show sara
            SARA "Oh… okay I’ll stop."

    SARA "Well, if I can’t help, maybe you should just take a break from thinking about it right? Come back to it later, after doing something fun… mine as well go pick up some other stuff when we go and pick up the television right?"

    NAR "There’s no way I can talk to her. It’s become fairly clear that our work is a set up by the guiding comet, especially knowing that Linden is directly involved…"

    hide sara

    NAR "But not everyone could be in on it right? Sara does seem to actually care about me… there’s no way she’d be a part of it right. No matter what, I still think she’s my friend."

    NAR "SARA RANK 4/7"

    scene date_transition

    scene city

    NAR "The two of us ended up going to pick up some other stuff, and additionally pick up a television set. While we were out, we split up to get some various things, and I was startled by a familiar voice."

    show luke

    LUKE "Oh hello there Jesse, didn’t expect to see you for some time"

    JESSE "Oh! Um, hello, didn’t expect this either… Sorry I wasn’t able to make any time yesterday, Didn’t have the opportunity to call off work… I’ve been a bit distracted."

    LUKE "That’s perfectly fine, I’m sorry that I cannot change my schedule around to better account for you…"

    LUKE "I’m not planning on staying here too long, I have a meeting to get to soon, but if there’s something on your mind, I’m here for you now."

    JESSE "Well… I guess it’s felt like for so long I’ve been able to depend on other people, but now it seems like I can’t find any way to go forward without them…"

    JESSE "And they aren’t able to do anything about this either, and even then they are starting to distrust me."

    LUKE "Hmm… I know I couldn’t hope to understand what’s happening in such a short time… But, as for you and your friends getting along, I’d make sure you actually know their feelings?"

    LUKE "You may have reason to suspect they dislike you, but you are your own worst critic, I doubt they truly feel that way…"

    LUKE "And when it comes to not being able to get help for a problem… I would ask yourself if there’s anything that only you could do about the situation to begin with."

    LUKE "Something special that you know none of the other people you know could do anyway. That way you know that no matter what, at least your solution wouldn’t be worse than if one of them tried the same thing."

    LUKE "I’m sorry I can’t try and help you anymore than that today, but I hope you’ll tell me of how things work out for you next time."

    hide luke

    JESSE "Yeah… thanks."

    NAR "LUKE RANK 5/10"

    scene date_transition

    NAR "I met back up with Sara and we headed back home… It isn’t much… but what Luke said does help a little bit, I’ll think about how to win this situation. I have to, but first I have work tomorrow…"

    NAR "The rest of the day proceeded as usual."

    call work_day("Sunday, November 12th 1922")
    call new_day("Monday, 13th November 1922")

    scene room

    NAR "It’s the day before he said he’d attack. The day I get to choose who dies if I do so please…"

    NAR "Something only I can do…"

    NAR "Spellcasting obviously. There’s also what Felix brought up though, with how I’m the only one in contact with Linden."

    NAR "I had given up, but now that it’s about to happen… Way back Luke said not to do anything I would regret. If I can’t figure this out, I know I’d regret it for the rest of my life. I can’t just give up like this."

    JESSE "But it’s already too late… what the hell can I do in one day."

    NAR "What do I have available to me? Spell wise, dispel magic is useless here, the offensive stuff is useless here…"

    NAR "rewind can only take me back in time about a minute or something apparently, which isn’t going to fix the past month, and invisibility… which isn’t applicable right now either."

    NAR "It’s not like I can do anything with that to save anybody… but I still have those options, I can use them for something."

    NAR "That leaves my contact with Linden. Which I also can’t do much with. The only thing of value is that I can tell him who to kill. Wait no, those weren’t his words…"
    JESSE "He said ‘attacked’, he never distinctly said they would die right?"

    NAR "Ulterior motives… That’s the only reason any of us are still alive right now, if it was just to get the tome, there was that spell Wilkinson used to make me more talkative back then. In that case… is Linden going through with this?"

    NAR "Of course he is, he’s a murderer who wants to get in my head. Realistically though… let’s not think of this as choosing someone to die. I need to think of it like I can choose someone who I think will survive."

    JESSE "The person with the most going for them to survive this… would be Finn right? He’s got the talent, and skills needed."

    NAR "I hate to put him up against that though. Wait, guns won’t do anything if he’s being attacked by magical members of the cult…"

    NAR "Wilkinson has other spell tomes though? Maybe he can give Finn enough to combat something like that today, I’m sure he could figure something like that out pretty quickly right?"

    NAR "I contacted Wilkinson."

    JESSE "Hey… I was curious, I have a friend that might be interested in trying to learn magic from you."

    CARTER "You can’t just talk about that you fool! And what do you mean friend? You don’t have friends outside of this group"

    JESSE "I’m hurt, but you’re right."

    CARTER "What? Oh. ooooooh. Alright okay, I understand some other stuff has been going on with you, I’ll be a great cram school for them."

    NAR "I thanked him then hung up. That bit works out apparently, but wait…"

    NAR "How do I even contact Finn?"

    NAR "I sat there in silence for a little bit… there are options but…"
    NAR "Suddenly, a loud noise of the television turning on behind me."
    JESSE "The hell?!"

    show cathee

    CATHEE "I’ve never actually used one of these before… neato"

    JESSE "How the hell?! Why are you? How are you?"

    CATHEE "Oh I’m doing quite well actually. thank-"

    JESSE "Not the question!"

    CATHEE "Well, the door was unlocked, and I was starting to worry about you too… but I think you’ve about figured it out on your own."

    JESSE "How… long have you been here?"

    CATHEE "Like ten minutes."

    CATHEE "But mainly, You should stop talking to yourself, and if you want to contact Finn, I’ll do it."

    JESSE "Um… what?"

    CATHEE "You could certainly find him on your own, either by just wandering aimlessly into places you’d think he’d be, or by calling up your friendly investigator buddy."

    JESSE "Yeah, I’d rather not owe him anything."

    CATHEE "Exactly, imagine owing something to that guy just because your friend doesn’t bother to get a phone."

    JESSE "Uh… thanks, I guess?"

    CATHEE "You are welcome! Oh and also, this isn’t the only thing you can do right? Anyway, gotta go find that guy now, see you eventually."

    hide cathee

    NAR "Just and randomly as she appeared, she left again. What she said… There’s something else I can do? Theoretically I just tell Linden to attack Finn, and then he’ll survive with his own talent plus Wilkinson’s resources…"

    NAR "Wait a moment, the spells. That political thing they were talking about the last time we met. A politician connected to the cult… would have to have some documents on it right?"

    NAR "Linden works within the restricted areas of the company that I can now confirm is a cover for the cult… if I could sneak in and follow him…"
    NAR "It’s risky, but at this point, what do I have to lose that I wasn’t already? I’ll also be able to prove to everybody that I can do something."

    NAR "I could use that invisibility spell, after all the tome heavily empowers everything right? It should be more effective and last longer."

    NAR "Using that… I could tail Linden into those restricted areas at work. He had said during lunch today, so I’ve still got a little bit of time, and he’ll be going back to work. I just need to wait… this’ll work out…"

    NAR "He arrived promptly when I expected and I let him in."

    show linden

    LINDEN "Have you made your decision?"

    JESSE "I have, and I won’t be giving you the tome. Not today, and never in the future."

    LINDEN "Boldly said, but are you willing to face the consequences? If you, would you like to choose?"

    JESSE "I am, and I would. Finn Marsh."

    LINDEN "Understood. Now then, I’m glad that it was much more concise than our previous meeting. You’ve calmed down."

    NAR "This rage, this fear, this hope… anything but calm… But I can’t let him see that."
    hide linden
    show jesse

    menu:
        "We’re done.":
            hide jesse
            show linden
            LINDEN "Indeed we are"

        "Okay, leave.":
            hide jesse
            show linden
            LINDEN "As you wish."

        "Would you like some tea?":
            hide jesse
            show linden
            LINDEN "I’m afraid I must get going."

    LINDEN "Goodbye Jesse, I will speak to you again tomorrow, after all this has passed."

    hide linden

    scene date_transition

    NAR "He left… and I waited only a minute before going outside to give chase. I don’t know how long the spell lasts, the minimum that Wilkinson said would be maybe thirty minutes at most."

    scene city

    NAR "I need to tail him without it until then, which shouldn’t be too hard since I know where he’s going."

    NAR "We got to the company, and I found a place to cast the spell on myself. It was incredibly jarring, to know where I was but completely unable to see or hear what I was doing."

    NAR "I truly felt like a ghost after using it… which was perfect."

    NAR "The rest of that experience was a blur of terror… The lethargy hit me not long after, and half of my trouble was fighting my own tiredness, with the other half keeping an eye on where Linden was going."

    NAR "While also trying to find some other places where there could be information on him. We had gone up a few floors, and into a dozen areas I had never seen before, he went about work as I would normally expect, but now I had access to the building."

    NAR "It occurred to me I didn’t really pay attention to who or what was happening with this politician, besides the fact they were going to be elected and were related to this."

    NAR "I used most of my time just taking any folders or documents I saw that referenced the election or political characters."

    NAR "Felix and Evelyn could sort through all this later, getting them is my job…"

    NAR "I used what was left of the spell's duration, which I’m starting to believe is already a lot longer than thirty minutes."


    NAR "Either that or the panic and lethargy and dissonance of not having a body has completely destroyed my concept of time, but I escaped."

    NAR "Trying not to freak the hell out around an alleyway, I went to a phone booth and contacted Felix. I was able to meet up with him and hand him everything I had stolen."

    NAR "It may be my delusional tired state, but he couldn’t hide the fact he was impressed, was he thinking of forgiving me? Heh."

    NAR "I fumbled my way back home, declining Felix’s offer to drive me home."

    scene date_transition

    NAR "And passed out on my bed."

    call new_day("Tuesday, 14th November 1922")

    scene room

    NAR "I’m woken up in the middle of the afternoon by the phone ringing. It was Finn. He explained to me that he was attacked, but thanks to what I had tried to set up, he was able to deal with it, and his attackers were incapacitated and arrested."

    NAR "He also mentioned that he always believed in me, and reassured me that I could trust him with anything, and if I can’t like this, he’ll still be with me till the end."

    NAR "It certainly was nice to hear that, and amazing to hear that he had survived, and that I was right about it being an attack, not a murder."

    NAR "But… why?"

    NAR "Linden said he’d meet with me after it was all over, I can imagine that means later today then."

    NAR "Sure enough, he showed up and I let him in, but I couldn’t suppress a yawn from how tired I was."

    show linden

    LINDEN "Congratulations Jesse. It turns out your father was right about you."

    JESSE "Don’t you just talk about him like that."

    LINDEN "Yes, that’s actually a big part of why I’m here. You had learned that I was in fact your father’s killer."

    LINDEN "That, is untrue"

    JESSE "And you expect me to believe that?"

    LINDEN "All that I expect from you, is to hear me out.
    Over a year ago, The cover that I was a major proponent in your father’s death was fabricated by the two of us."

    JESSE "You don’t mean…"

    LINDEN "I was actually on good terms with your father. I’ve been working against the cult for a couple of years now."

    LINDEN "The reason I knew you had the tome in your possession is because I was the one who helped your father steal it in the first place."

    JESSE "then why the hell did you not say that in the first place?! Why all these threats and games?"

    LINDEN "Your father had a lot of faith in you. I… did not, I wanted to test if you really had it in you to continue his work, when I learned you thought I killed him, I had hoped that anger would also push you into stopping my plans."

    JESSE "You weren’t really going to kill Finn?"

    LINDEN "No. The cult was already planning to attack one of you as a warning, I had hoped to sway that in your success. Which you did, and you happened to do even more than that..."

    LINDEN "With all of those stolen documents."

    JESSE "How do you know about that?!"

    LINDEN "Well, a couple things have gone missing, and you seem to have recently casted a spell, which I know wasn’t earlier today with Finn. I’m unsure what you did, but it’s clear something happened."

    JESSE "So… what do you want out of this?"

    LINDEN "Because of my involvement with your father, I’ve been shunned by some of the upper echelons of the cult. I wish to continue working against them, and assisting his son and your friends is a viable path to that."

    JESSE "*sigh* I’ll tell them… But I need time to accept what all this means with you."

    LINDEN "I look forward to it. Goodbye-"

    JESSE "One more thing."

    LINDEN "Hmm?"

    JESSE "Do you know who killed my dad?"

    LINDEN "It was referenced to be a group of our acolytes on a ship. However I know for a fact that he made it to Ireland before he died… I’m sorry I don’t know more."

    JESSE "It’s… fine. Goodbye Linden"

    hide linden

    NAR "He left. I wasn’t willing to continue things anyway, because of how tired I was. To think this entire thing was a twisted test of that man."

    NAR "Him helping my dad makes all of his information make a lot more sense, and it’s a reason why he wouldn’t have alerted the entire cult and had us killed…"

    scene date_transition

    NAR "I’ll tell everybody tomorrow…"

    call new_day("Wednesday, 15th November 1922")
    NAR "Sleeping in as usual. I was contacted by Felix, who told me they had successfully apprehended the politician due to the allegations against him with some of the documents I gathered, just before the election too."

    NAR "I was still really tired, so I kept everything incredibly brief, but I did contact and get the group together. I was able to tell them everything that had been happening for me this month, and then I told them about what Linden told me."

    NAR "They were hesitant to accept it at first as I was, but too many things make sense if you look at it as if it was all a test by a questionable ally."

    NAR "Wilkinson for one nearly admits to enjoying that plan, before reminding himself that Linden was a part of the Guiding Comet."

    NAR "Additionally that clarification that my work is a cover for the cult, it’s not like I can stop going at this point, or else suspicions would be raised, but I would try and be more careful with it in general."

    NAR "We gained a new ally, directly involved with the cult, and I was able to thwart another one of their minor plans. This month actually turned out to be pretty successful even with all that headache."

    NAR "The rest of the day proceeded as usual."

    #CHAPTER 3 - END


    jump chapter4_start
