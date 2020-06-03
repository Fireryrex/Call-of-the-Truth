# Chapter 2 begins here

# Declare characters used by this game. The color argument colorizes the
# name of the character.

label chapter7_start:
    $ current_chapter = 7

    #CHAPTER 7: To Dream of a Nightmare
    scene room
    centered "{size=+30}CHAPTER 7: To Dream of a Nightmare{/size}"

    call new_day("Saturday, 1st April 1923")

    NAR "The ultimate joke. The next thing I could understand about my situation was that I was locked up in a cell, presumably by the guiding comet after the entire incident last night."

    NAR "Tired and locked away in the dark… awaiting something… somewhere… I know there wasn’t real betrayal… but even if this is going to work out for us it’s still not the most comfortable thing to go through…"

    NAR "We’re so close to stopping their plans once and for all… we just need this one final push, and we’ll all be free from this… but they got the tome back too didn’t they? We didn’t let this happen did we…"

    NAR "My dread grew as each day passed…"

    call new_day("Monday, 9th April 1923")

    NAR "The darkness of the cell only shifted by people outside running by with light…"

    NAR "Until the jangling of keys and the distinct opening of the door to where Jesse was being held. Opening the door, and rushing inside was Finn. He grabs Jesse and starts to move him out of the room."

    show finn

    FINN "Hey, sorry it took us all a bit, but we can catch up once we’re out of here yeah"

    hide finn

    NAR "Following their lead in a tired state, it had seemed they were able to blend in and then distract the group guarding this area; they got him outside, then they all carefully and quickly got to Carter’s Bookstore."

    scene bookstore

    NAR "It was the dead of night. Me and Finn were the only ones inside, and eventually Carter arrived, followed shortly by Evelyn."

    NAR "I leaned back in my chair, exhausted and confused…"

    JESSE "Thank you… everyone… How did you guys even find me and pull that off? I know we had an idea if this had happened but still, you guys pulled it all off in a week…"

    show finn

    FINN "Yeah! Of course we didn’t have too much to go on, and it was even hidden from Linden and Sara, but we actually got help from a friend of yours, and then Felix started trying to put together the entire plan."

    FINN "Oh yeah, those two are still out and about finishing up with the cover."

    JESSE "But… we lost the tome… I’m sorry we trusted her… but there’s still parts of this we aren’t fully clear on right, and if they have the tome, they’re going to be able to continue to the end and we won’t be able to do anything…"

    JESSE "We won’t get another chance to take it back…"
    NAR "At that moment Sara walks into the store, and is greeted by everyone."
    hide finn
    show evelyn

    EVELYN "Oh yeah about that Jesse… well, we may have made some plans for this all without you. You’re right that they now have the tome, the fake tome that we prepared for you!"

    NAR "Carter opens up a drawer behind the counter, and holds up the real tome before placing it down."
    hide evelyn
    show carter

    CARTER "It has been an honor to hold onto the artifact that will cause them so much trouble… the greatest shame is that I cannot keep it…"
    hide carter
    show sara

    SARA "And… yeah with that, sorry for having to try and trick you again, but we had to make sure they would be confident they caught the group off guard. Which means that as long as they don’t try to keep track of you anymore, we have the upper hand."
    hide sara
    show finn

    FINN "Which is one of the things that Felix is taking care of, he seemed really keen on being a part of the killing the ‘fake’ you part of the plan"

    JESSE "So… everything worked out… But you mentioned one of my friends was the one who gave you something that actually started this entire plan? Who was that?"
    hide finn
    show sara

    SARA "Oh, he’s gonna get in contact with you tomorrow, but he never actually said his name to us, he seemed trustworthy before… I swear I’ve seen him around before too…"

    SARA "Of course it was really our best lead at the time, and it worked out so, it seems like he’s been a part of this for a while now."

    NAR "Hmmm… that’s concerning in it’s own right, but I guess I’ll talk to you tomorrow."
    hide sara
    show carter

    CARTER "So, we’re starting the plan to get rid of these guys for good right?"
    hide carter
    show finn

    FINN "Yeah! We just need to figure out exactly when and where they’re doing the resurrection and then we can use the tome to disrupt things for good right?"

    JESSE "Theoretically yeah… if their idea is to resurrect this ancient being and use it’s power to subjugate the masses… it’d be on a day that many people would be excited or interested in, so that their minds would already be open to a ‘change’ of sorts…"

    JESSE "What’s notable that’s happening in the next few weeks? We can assume it’s going to be this month…"
    hide finn
    show evelyn

    EVELYN "Well, let’s see, Carter you have the most recent news don’t you?"

    hide evelyn

    NAR "We began to talk about the possibilities of big events that would match up with the scale of ritual they’re planning on doing…"

    NAR "But I couldn’t get my mind off something, it was as if things were actually working out for us… Like they’ve always been working out for… me… Why wouldn’t they just-"

    show sara

    SARA "Oh what about the Shakespeare play, it’s going to be their first show, it’s bound to be a big event! And it’s on a tragedy of one of Britain's kings, it’s thematic enough for their theatrics."
    hide sara
    show evelyn

    EVELYN "That’s not a bad event, and it would have people tuned in from all over assuming it’s broadcasted too… But I think there’s something a lot bigger that we haven’t thought about this month."

    EVELYN "The Royal Wedding. It’s set to happen on the 26th in Westminster Abbey."
    hide evelyn
    show carter

    CARTER "Even if it’s not to try and win over and subjugate the entire city, if they could just control the rulers that’d be an easy way for them to expand everything…"

    JESSE "So it’s clear. They’re going to enact their plans in about two weeks. And we are going to go and stop their plans once and for all, with that spell, and turn them all against themselves."
    hide carter
    show finn

    FINN "From there, once we break their influence the actual government enforcement can hold power against them again. But it’s getting late, we have an idea, and we can work on the specifics another day, we have plenty of time."

    FINN "Jesse you need to get some real rest. Besides, your friend is waiting to meet with you tomorrow, can’t be too tired for that right?"

    NAR "We all begin to start leaving."
    hide finn
    show sara

    SARA "Thanks for letting us use this bookstore all the time Carter, But maybe we can hope to not need it in a few weeks."
    hide sara
    show carter

    CARTER "Yeah that’d be great, besides I need to clean it from all this atrocious cultish energy every time you come over, it’d save me so much hassle…"

    CARTER "Goodnight everyone."

    hide carter

    scene date_transition

    NAR "We all went our separate ways, and me and Sara headed home, and I got some much needed rest on a worthwhile bed."
    call new_day("Tuesday, 10th April 1923")
    NAR "Waking up, and feeling much more refreshed than the past few days… We finally have a goal, and an ending."

    NAR "The confusions and terror of this past year were finally about to end… in just 16 more days. Oh right they said my friend who helped them was going to meet with me today…"

    NAR "Wait today is the 10th that would mean I would…"

    NAR "Oh… that would mean that ‘friend’ is actually Luke"

    scene museum

    NAR "I got a call from him, and would be meeting him at the museum today, I got dressed and headed over. With thoughts running through my head."

    NAR "Of Course I’ve been suspicious of him, I’ve been suspicious of everybody at some point… but to think he got directly involved with everybody to help me… I need to know why."

    NAR "I met up with him, and we began to walk, touring the museum. In silence. Until he broke it."

    show luke

    LUKE "I’m sorry. For delving too much into your affairs I mean."
    hide luke
    show jesse

    menu:
        "Don’t be…":
            hide jesse
            show luke
            LUKE "It’s still too personal for me to have done all this behind your back"

        "You helped save me…":
            hide jesse
            show luke
            LUKE "I wasn’t going to let you suffer more"

        "Expecting something from me?":
            hide jesse
            show luke
            LUKE "Yes, that is my purpose in all this, but what I expect is your own growth."

    LUKE "I take it you want answers… and that’s a big part of what I want to talk about today, is your actions involving this group for the past couple of months."

    JESSE "I’ll listen."

    LUKE "Well, I first started worrying about your involvement with the Guiding Comet since around November last year, the things happening around them, and you were too linked."

    LUKE "As well as what happened to you in December, it became impossible for me to ignore that."

    LUKE "But… to tell you the truth I’ve been linked to this cult for much longer than that on my own."

    LUKE "You see, my little sister was in a similar situation to your own, it’s obvious when someone has casted spells from that tome. It was about 7 years ago when she died."

    LUKE "She was actually a member of the cult, for how long I’m not sure, but I only learned that when I started to notice how she was feeling afterwards."

    LUKE "Part of my point is that I’m equally invested in all of this ending as much as you are, but I didn’t see any way to approach you about it until now."

    LUKE "I can only assume how dire things are… All I can say, casting those spells is what killed her, she wasn’t strong enough to complete what they wanted to its fullest, but the spell still activated."

    LUKE "I can assume you’ve already thought of every way to get through this. If there is one way to stop them, it’s that tome. I hate to say any of this to you, and I admit I must have failed long ago… when I couldn’t save her… But…"

    LUKE "I have something to give you that might help honestly, it’s something my sister gave to me the last time I ever saw her. But before I give it to you I want to confirm that you’re going to go through with this."

    LUKE "And I believe you would be able to cast without needing the tome, if you had it’s magic… at least that's what she could do."

    LUKE "You understand now, why your dad would risk so much for this don’t you?"

    NAR "LUKE RANK 9/10"

    NAR "…"

    hide luke

    NAR "We ended our conversation there. I understood what he meant. It’s a thought that I've been worried about since that day in July. I haven’t told anybody, but I’ve never felt the same since December, if I haven’t recovered from that, there’s no telling what this means for me."

    NAR "But to think his sister was also in my situation… I have a lot I want to talk to him about, but I am not today, I need to collect myself."

    scene date_transition

    NAR "I… know what needs to be done… I’ve accepted that for a while now, and if I could do something that important for everyone… The next time I meet with him is the 25th, the day before this all ends."

    NAR "I don’t think it’s a good idea to tell everyone about this, they’ll panic and try to find a different way, when we can assuredly win if I just take this sacrifice, besides it’s not like death is guaranteed, just likely."

    NAR "I told Sara about parts of the meetings, and that we should get the group together tomorrow to figure out things more indepthly."
    call new_day("Wednesday, 11th April 1923")

    scene bookstore

    NAR "We got everyone together at the bookstore for another meeting, now that we were all rested, and Felix wasn’t busy with finishing the plan."

    NAR "I explained to them in detail about what Luke had told me, and told them about my relationship with him over the past few months. I left out the part where he said the spellcasting is what killed her… and what will kill me."

    show finn

    FINN "I don’t know… it seems like he’s been involved with this a lot longer than any of us thought, but he did help us out… I dunno it just seems a little untrustworthy"
    hide finn
    show sara

    SARA "I’m fairly sure I would know if he was involved with the cult in any way, anything with the tome seems to be above me… but when I recommended him to Jesse is wasn’t involved with the cult at all."
    hide sara
    show carter

    CARTER "I for one, can not confirm nor deny any of his dealings in the mystical… because I haven’t seen him in any form either."
    hide carter
    show finn

    FINN "Well, if you guys are confident that he’s not directly involved like that… and he did help us out, and he’s been helping out Jesse this entire time even knowing right? He’s probably okay."
    hide finn
    show felix

    FELIX "It’s not like he matters much in the scheme of this at the moment, besides your meeting with him on the 25th. Did he really not say anything about what he was going to give you then?"

    JESSE "No, not at all… He did say it was just from his sister, who apparently also used this tome, so it could be something related to that magical nature…"

    FELIX "It’s suspicious he would choose to keep secrets now of all times, he does know that our operation is going to be the 26th doesn’t he? Or are you fine with completing the plan with his information in 24 hours."

    JESSE "Not exactly, but it’s a stretch to even say that he knows anything will happen on the 26th."

    FELIX "hmm…"
    hide felix
    show evelyn

    EVELYN "Maybe it’s things that won’t make you feel so bad after using it?"

    JESSE "Probably not, and besides I’ve been feeling fine, the worst it could be is another hospital visit right?"

    hide evelyn

    NAR "It’s clear they’re worried about me, but they trust me… It feels wrong but it’ll only make things more complicated if I were to say anything."

    show felix

    FELIX "Anyway, should we focus on what’s actually happening rather than the hypothetical?"

    FELIX "I’m going to spend the next few weeks planting the seeds for actual officials to retake control from the occult once we break them at the Abbey, but we need someone to actually scout out that area and find where they’ll be setting this up."

    FELIX "Additionally we’ll need a way to actually get to that location, because I’m sorry to say but we’re not just going to be let near the royal wedding that easily."
    hide felix
    show finn

    FINN "I can start checking out the area and figure out where they’ll be coming and going"
    hide finn
    show sara

    SARA "With my position with them still not being completely compromised, I can help out with that as well, we can’t trust Linden to be able to leak everything for us."
    hide sara
    show evelyn

    EVELYN "And I can figure out a way to get us through easily, and quietly."
    hide evelyn
    show carter

    CARTER "A topic, I can assist with, manipulation is our forte, not that you would know right?"

    JESSE "Anything specific I can focus on, I actually have the time to be out and about now."
    hide carter
    show felix

    FELIX "Of course I have something planned for you, but you’re going to need to wait a little bit, I’ll contact you personally, expect something on Monday."

    hide felix

    scene date_transition

    NAR "After hanging out for a little bit, and discussing more specifics of when and where a few of them should meet to get things on their way, at least until… Carter decided to close shop early and kick us all out."

    NAR "I’ll have some more free time now though, since I’m not going back to work ever again."

    NAR "We said our goodbyes, and each headed home."

    call new_day("Thursday, 12th April 1923")
    label free_day_4_12:
    call free_day("all", "Carter", "Evelyn")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Carter"
            call carter_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Evelyn"
            call evelyn_hangout

    if(hangout_failed):
        jump free_day_4_12
    #Carter
    #Evelyn
    #Self Improvement

    call new_day("Friday, 13th April 1923")
    label free_day_4_13:
    call free_day("all", "Finn", "Linden")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Finn"
            call finn_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Linden"
            call linden_hangout

    if(hangout_failed):
        jump free_day_4_13
    #Finn
    #Linden
    #Self Improvement

    call new_day("Saturday, 14th April 1923")
    label free_day_4_14:
    call free_day("all", "Carter", "Evelyn")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Carter"
            call carter_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Evelyn"
            call evelyn_hangout

    if(hangout_failed):
        jump free_day_4_14
    #Carter
    #Evelyn
    #Self Improvement

    call new_day("Sunday, 15th April 1923")
    label free_day_4_15:
    call free_day("all", "Finn", "Linden")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Finn"
            call finn_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Linden"
            call linden_hangout

    if(hangout_failed):
        jump free_day_4_15
    #Finn
    #Linden
    #Self Improvement
    call new_day("Monday, 16th April 1923")

    scene room

    NAR "Another fair day outside, and Sara gets ready to head to work. I waited somewhat impatiently for Felix to contact me."

    NAR "I understand that everyone else is more suited to each of the tasks, and splitting this up is still a good idea, but even still I could be helping more directly than just being the final play against the cult."

    NAR "The phone does not go off for a while, but the doorbell is rung, and opening it up, is Felix in person."

    show felix

    FELIX "Afternoon, hope you don’t mind me just coming here to talk, no point in going about this anywhere else"
    hide felix
    show jesse

    menu:
        "Yeah it’s fine":
            hide jesse
            show felix
            FELIX "Good, now on to why I’m here."

        "Want something to eat?":
            hide jesse
            show felix
            FELIX "Not from you, no."

        "Don’t get comfortable.":
            hide jesse
            show felix
            FELIX "Not that I could here."

    FELIX "I’ll get straight to the point. I know you’re smart enough to come to some of the same conclusions I have, and at this point I don’t think your dumb enough to try and blind yourself. What the hell are you doing?"
    hide felix
    show jesse

    menu:
        "Excuse me?":
            hide jesse
            show felix
            FELIX "For what? Playing this off?"

        "I don’t understand.":
            hide jesse
            show felix
            FELIX "*Sigh* yes, you do."

        "Ah, being rude in my own home. Expected.":
            hide jesse
            show felix
            FELIX "Stop messing around."

    FELIX "We both know there’s more to this than what’s happening right now. What we’re doing and how we’re doing it isn’t right. And I don’t mean that there’s another way or it’s exactly bad."

    FELIX "You realize it though, why is this working out so well for us? And more importantly, why is this working out so well for you."

    JESSE "..."

    NAR "But it isn’t, for all of this to work, there’s no way I can survive casting that spell…"

    FELIX "And don’t even try to play like you dying from this is the issue we’re trying to realize."

    FELIX "The question that I think we’ve both asked since we first learned about all of this, that still hasn’t been answered in any real form."

    FELIX "Why are you still alive?"

    FELIX "It seems like killing you would have been much more effective for this cult the moment you found the book wouldn’t it?"

    FELIX "And now we both know you flatmate was in on it for even a few years before any of this even started!"

    NAR "He’s right. I’ve always tried to ignore that question, because things were just easier to make sense of if it wasn’t at the forefront of things."

    NAR "My dad died trying to reach the truth of all of this, and here I am, now in his shoes, but still alive until I’m able to essentially kill myself."

    NAR "They wouldn’t just wait for me to die when it would also disrupt their plans, it’s clear they have the potential for it. They’ve always had the potential for it."

    FELIX "It looks like you have thought about it before. You realize what this means right, if we’re going into the final hour of all of this, and we don’t know if we’re actually one step ahead of them or not…"

    JESSE "We have to go about this… as if me surviving to this point is a part of their plans."

    FELIX "And now we know that it turns out you are ever so slightly special because of your use of the tome."

    JESSE "What do you mean by that, unless you mean… Luke’s Sister?"

    FELIX "There being two of you who have used the book makes this much more interesting, because even during that time where they stole the book from us, was it that they couldn’t progress their plans until now because they weren’t ready?"

    FELIX "Or because they know they can’t use it. If this sister also used it, and also was harmed by it to the similar extent to you…"

    FELIX "something that would result in her death, maybe there’s something about you that makes them need you specifically to cast it."

    JESSE "If anyone could do it, they would have easily been able to complete all of this much earlier, especially if they were already testing it 7 years ago. But that still doesn’t explain why I can."

    FELIX "Probably nothing we can figure out with the time, but that’s probably something your father knew, which would explain why he got so invested in all of this, even compared to his other work."

    FELIX "In the end, let’s assume we’d be able to succeed in this if we tried, but the only things we have going for us is that they may not realize their tome is a fake."

    FELIX "We can go about this under the assumption that this is actually a part of their plan. I hate that I’m entrusting this to you, but it’s something only you can figure out, magic is just that step beyond me."

    FELIX "And on top of all of that, you’re not allowed to die to this, not gonna let you go out in a blaze of glory thinking you’re better than me since you finished this."

    NAR "He gets up and starts getting ready to leave."

    FELIX "I don’t trust anything that’s happening in the slightest. But if surprise is our best option, you better find a card to pull without us. Good Luck."

    hide felix

    NAR "I sat there, thinking about what he said. I hated how much I agreed with him. We have definitely created more problems for them than they would like in most cases, Linden and Sara are proof of that…"
    NAR "But the reason they wouldn’t attack us or at least kill me is because they somehow need me, they want us to ‘succeed’ it’s part of their plan."

    NAR "That could also explain why they haven’t figured out that it’s a fake… because they can’t even use it right now. But he’s right, there’s not much else they can do, but I don’t know where to begin on my end…"

    NAR "It sounds stupid, but our answer out of this may come from whatever Luke will give me on that day… our final meeting…"

    NAR "Until then, let's make sure I’m content with everything, even still I don’t see myself getting out of this without casting a spell… and if it’s anything important that would stop that…"

    scene date_transition

    NAR "The rest of the day proceeded as usual…"

    call new_day("Tuesday, 17th April 1923")
    label free_day_4_17:
    call free_day("knowledge", "Linden", "Felix")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Linden"
            call linden_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Felix"
            call felix_hangout

    if(hangout_failed):
        jump free_day_4_17
    #Linden
    #Felix
    #study

    call new_day("Wednesday, 18th April 1923")
    label free_day_4_18:
    call free_day("charm", "Felix", "Carter")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Felix"
            call felix_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Carter"
            call carter_hangout

    if(hangout_failed):
        jump free_day_4_18
    #Felix
    #Carter
    #gardening

    call new_day("Thursday, 19th April 1923")
    label free_day_4_19:
    call free_day("all", "Linden", "Carter")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Linden"
            call linden_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Carter"
            call carter_hangout

    if(hangout_failed):
        jump free_day_4_19
    #Linden
    #Carter
    #Self Improvement

    call new_day("Friday, 20th April 1923")

    scene room

    NAR "The day went along as any other, until there was a knock at the door, where Finn and Evelyn were standing."

    show evelyn

    EVELYN "Are you guys ready?"
    hide evelyn
    show sara

    SARA "Oh yeah, give me a second and we’ll be ready to head out."

    hide sara

    NAR "…we?"

    show finn

    FINN "Hey Jesse why do you look so confused?"
    hide finn
    show jesse

    menu:
        "What’s going on?":
            hide jesse

        "Why are you here?":
            hide jesse

        "Did I forget something?":
            hide jesse

    show sara

    SARA "Oh yeah, I forget to tell you! We were planning on going out shopping for some nicer clothes to wear for the theatre and the wedding!"
    hide sara
    show finn

    FINN "Yeah come on, we have the time, most of us are just waiting until next week to look into the specifics, since it’s closer to the final date, so we were thinking about actually having some fun for a change."
    hide finn
    show evelyn

    EVELYN "Unless you’re not up for it today on such short notice, we’ll pick you out something."

    hide evelyn

    NAR "This… was not what I had expected for today… and none of them realize the severity of what’s happening. Perhaps this will actually be fun, there’s not much else to do besides wait at this point either…"
    NAR "And besides I can’t let them pick out clothes for me."

    scene apartment

    NAR "We got ready and headed down the stairs, and waiting for us parked, was Felix, who appeared to be in the same mindset as me it appears…"

    scene city

    NAR "We went to the mall, and spent far too much money shopping… and far too much time throwing me between outfits to find something that worked… But, it was fun."

    NAR "I don’t think I’ve been this happy in quite some time, even knowing what awaited us in 6 days. It was fun, and after they talked about the theatre some more, it does seem like some much needed time to remove the more depressing thoughts from my head."
    call new_day("Saturday, 21st 1923")
    NAR "We all met up once again, and headed on our way to the Theatre, the Shakespearean play Cymbeline. Which was enjoyable enough, even with me projecting my own crazy life into the story."

    NAR "A story sought with betrayal and trickery, but in the end… a great feast, a happy ending. That’d be nice wouldn’t it."

    NAR "The rest of the day proceeded as usual… I feel like tomorrow may be my last chance to do something of my own with my time… The day of the wedding approaches ever so slowly…"

    call new_day("Sunday, 22nd April 1923")
    label free_day_4_22:
    call free_day("all", "Felix", "Finn")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Felix"
            call felix_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Finn"
            call finn_hangout

    if(hangout_failed):
        jump free_day_4_22
    #Felix
    #Finn
    #Self Improvement

    call new_day("Monday, 23rd April 1923")

    scene bookstore

    NAR "With only three days before the big event, and with Jesse being unavailable for a time on the 25th, the group arranged to meet up at the bookstore to confirm their plans for the 26th."

    NAR "I can barely keep focus, thinking about the flaws and the idea that all of this could be the wrong way to end all of this."

    show finn

    FINN "I’ve confirmed where they’re gonna be, and how we can get there, we found a secondary entrance that’ll let us be above the ritual area under a secret crypt they’ve constructed underneath the Abbey."
    hide finn
    show evelyn

    EVELYN "And we’ve confirmed the people we can talk to that will let us in without any trouble, which means step one to our plan is complete."

    NAR "Linden opens up and walks into the room, giving everyone a polite greeting."
    hide evelyn
    show felix

    FELIX "Good that you could make it too."
    hide felix
    show linden

    LINDEN "I will attempt to keep this brief, I have a train to catch soon. The operation to instill the resurrection glyph with alterations to let it empower our disruption spell is assured."

    LINDEN "However, the resurrection, or rather the more correct term would be the summoning spell can still be cast through it."

    LINDEN "While it’s more powerful if used through your tome, this spell is not exclusive to it, so time is still of the essence when you arrive."
    hide linden
    show sara

    SARA "Thanks for your assistance sir, and… we can still confirm that they don’t realize the tome they have is a fake"
    hide sara
    show carter

    CARTER "Of course not! Just because my people aren’t as impressive as you all doesn’t mean we can’t pull the rug under you sometimes."
    hide carter
    show linden

    LINDEN "As he says… I can confirm they have not looked into trying to identify if the tome is a forgery, but the preparations are set for it to be used, it took them some time to perfect that spell with the faulty pen. But I’m afraid this will be goodbye."

    LINDEN "Once you succeed, the time before the group fully collapses will be enough for them to at least learn of my betrayal, So I plan to leave the country entirely. Good luck to you all."
    hide linden
    show felix

    FELIX "Feel free to come back soon, I’ve basically set up all the arrangements to oust everybody from the cult the second we get through this."
    hide felix
    show linden

    LINDEN "I appreciate the offer, but personally there’s a lot of bad blood here with everything going on, so I’m using this as an extra excuse to travel more."

    JESSE "Linden. Thank you for the help. This wouldn’t have been possible without you."

    LINDEN "Don’t worry. I know. Goodluck to you all, and goodbye."

    hide linden

    NAR "Linden exits the room, suitcase in hand."

    show felix

    FELIX "And yeah, as I mentioned there, I’m all prepared on my end, which means it all rests on you Jesse. Your meeting with Luke and then the disruption of the ritual is all on you."

    NAR "His eyes are piercing."
    hide felix
    show evelyn

    EVELYN "Well… it seems like everything is set for the day, How about we meet up here in the morning, then head out together."
    hide evelyn

    NAR "Everyone gets up to leave, and Felix stops me for a second in this room."
    hide evelyn
    show felix

    FELIX "I understand we still don’t have anything extra that can work with this. Especially without the pen. But just this once, actually live up to being the son of the legendary detective."

    JESSE "Now you’re worrying about this too much."

    FELIX "The hell do you mean by that?"

    JESSE "I’ve never really realized what I have here. I’m not going to lose that now."

    FELIX "Heh, I’d say that blind faith is stupid, but it’s worked out for you so far huh. See you soon."

    hide Felix

    NAR "We all said our goodbyes, and we left."

    hide bookstore

    NAR "Sara has been acting strangely distant…"

    NAR "The rest of the day proceeded as usual."
    call new_day("Tuesday, 24th April 1923")

    scene room

    NAR "The day before my meeting with Luke… Who knows what he’s planning on giving me, and who knows if this is also a part of the grand plan they all have."

    NAR "The day proceeded as usual. Until…"

    NAR "Sara confronted me. She was struggling to say everything clearly to me…"

    show sara

    SARA "How long are you going to play it off?! I was just waiting for you to say something about it, but do you really not realize what's going to happen if you go through with this?"
    hide sara
    show jesse

    menu:
        "I know…":
            hide jesse
            show sara
            SARA "Then why… are you being so calm about it."

        "Don’t worry.":
            hide jesse
            show sara
            SARA "What’s that supposed to mean?!"

        "What do you mean?":
            hide jesse
            show sara
            SARA "That you’ll die!"

    SARA "I know better than any of them how you actually are physically… you’re not ready to cast something this high level again, and after learning that it will actually kill you…"

    SARA "There’s no way you don’t realize what you’re getting into, and yet you’re still going to do it, I’m sure if you brought it up we’d be able to find a way around it right?"

    JESSE "I’m… sorry, but that’s exactly why I didn’t do it. Things are too important to value my one life over saving so many others…"
    JESSE "I hadn’t mentioned but Luke was actually the one who brought that up, and when I realized that as much as I may have hated it, what my Dad did was right"

    SARA "That doesn’t matter right now! It doesn’t matter what Luke told you, maybe he wants you dead, so he isn’t ashamed he couldn’t do anything for his sister… or just…"

    SARA "If this is somehow a part of Luke’s plan, and not ours, I don’t want you to go through with it. Even if things turn out worse without our intervention, I’m sure we can all figure out a way around it if we’re all alive and safe."

    JESSE "I understand where you’re coming from… And of course, I don’t want to die, it’s never going to be a part of the plan. But we can’t stop doing this, it’s far too important to not take the chance we have here."

    SARA "If you’re confident in it… I’ll trust you… But i’ll never forgive you if you don’t do something incredible to get out of this… Not like I’ll be able to pay for this place if our job goes under right?"

    SARA "Ever since all this started… I’m sorry that I lied to you for so long, but in the end, if this all works out, maybe it was better that it worked out this way?"

    SARA "Sure it could have been better if none of it ever happened, but the people we’ve met, the struggles we’ve gotten through."

    SARA "That would have never happened if we didn’t all get caught up in this. I’ll be with you, until the end, and past that too if you need me."

    NAR "I can sense a new confidence in her…"

    NAR "SARA RANK MAX"

    scene date_transition

    NAR "The only hope I have, which may even be playing into their hands even more, is to see what Luke was promising to give me, but he’s intended to give those to me when I’ve accepted that I’m willing to die for this…"

    NAR "Which, I was, until recently… I’ll figure something out, I have to, besides… there’s still one mystery that only I know about…"

    NAR "The rest of the day proceeded as usual."
    call new_day("Wednesday, 25th April 1923")
    NAR "The eve of the wedding. The end of the game that we’ve been pieces of for so long, I will find out the truth behind Luke’s goals."

    NAR "I will find the one subversion that we need, that third path that leads us all to a better time."

    NAR "The key things with all of this,"

    NAR "My dad investigated this for the final years of his life, he was able to steal and keep the pen hidden, and was able to take the book directly from them, his goal to give it to me."

    NAR "The cult knew of this to some unknown extent, and our actions did cause them some more hardships than they expected. They have yet to kill me outright however."
    NAR "When they stole the book from us, they were content with letting us all live in exchange, It would be easy to assume we’d still work against them, even without those items, when they could have easily dealt with us."

    NAR "Similarly with when they stole the fake tome."

    NAR "Luke’s sister also used the tome, and was working directly with the cult, however she suffered similarly to me, and died from using the tome, meaning if the ultimate goal is to use the tome, Something has been preventing them for a long time."

    NAR "They have worked to incite violence and divide the country and its people, to in theory open peoples minds to the idea of change, under the presumption that there is magic that can bend and subjugate the will of the people."

    NAR "After gathering relics from an archeological dig in Egypt, and using resources they’ve gathered over the years, they are planning to resurrect, or how Linden put it, summon their god to possibly enact that subjugation. They have only begun this now that they have my tome."

    NAR "Linden had said that the summoning ritual does not need my tome, but that it would be more powerful if summoned from it."

    NAR "The people in the cult do not know that I still have the real tome, with the Disruption spell already copied and ready to be cast."

    NAR "They have copied the summoning spell onto the fake tome, and are planning to cast it, but will be unable with the fake tome at least due to its fraudulent nature."

    NAR "Luke has been helpful and supporting of me since all of this began, without him I don’t think I could have made it to where I am today… Sara and Linden have confirmed they haven’t seen him involved with their cult directly."

    NAR "Linden has been on the outskirts of some major developments, and is shunned by some of his peers, but still has enough power to contribute and manipulate some parts of this summoning ritual."

    NAR "Sara has been specifically assigned to follow and watch me to make sure that I wasn’t doing anything the cult deemed as wrong, but the actions accounted for by her updates are probably unknown to her."

    NAR "Felix and I have come to the conclusion that our intervention at the abbey in the future almost seems ‘too good’ for us considering what we’re up against."

    NAR "The answer may lie in treating everything as if the cult had planned where I would be right now from the start."

    NAR "Whew…"

    scene park

    NAR "For the final meeting with Luke, we met at Hyde park. The construction had made incredible progress, and I met him at the bench that I spoke with Finn on all those months ago."

    NAR "However the subtle chill of spring was nothing compared to how cold I was to myself that summer… A lot has happened, and part of that is thanks to Luke…"

    show luke

    LUKE "Have you made your decision?"

    JESSE "I have, I’m willing to find the way to save everyone I care about, no matter the cost."

    LUKE "I’ll say a little more about my sister first… She was a part of the cult, but near the end she started to realize what she was doing wasn’t right in her eyes."

    LUKE "That’s why she knew she was going to die… and why she gave me, what she said was the answer to the problems that would eventually surface from their evils."

    NAR "He takes out a piece of paper, one I would recognize from anything, it was clearly a piece from my tome, one of the two pages that was torn from it."

    NAR "Taking it from Luke, a very similar spell was scrawled out on it, it’s the exact spell for the disruption spell we plan on using, except it’s drawn much neater than anything with the current broken pen."

    LUKE "With that, you should be able to stop their final plan, at least that all I could gather, and judging from you, that’s awfully soon isn’t it"
    hide luke
    show jesse

    menu:
        "Awfully soon indeed.":
            hide jesse
            show luke
            LUKE "It’s a shame there isn’t more time."

        "Tomorrow actually.":
            hide jesse
            show luke
            LUKE "Oh… I’m sorry about having to wait then."

        "...":
            hide jesse
            show luke
            LUKE "It’s okay, I understand it must be daunting."

    LUKE "As your… as your friend, I am truly sorry it has to come to this. When I realized what you had gotten into, I had tried to look for any number of ways for you to be able to survive, but now that it’s near the end…"

    LUKE "The best I can do is guarantee your victory over them. It’s what my sister wanted, and it’s what I want."

    JESSE "I want to save everybody too."

    LUKE "What you do will decide the future of everything, I know I asked for you to make up your mind by now, but I know that when you get to that deciding moment, you may falter, the choice becomes so much harder when you finally have to make it."

    LUKE "I Know you’ll do what’s best Jesse"

    LUKE "Now… did you want to ask me anything?"

    JESSE "Nothing really… It’s funny, this is the place I first found the book, when Finn made the most obvious coded message I’ve ever heard to get me to check where he buried it."

    JESSE "So no one would notice I had it. It’s just funny that it turns out you’ve had one of the two ripped pages this entire time…"

    LUKE "Yes, it’s interesting how fate works out doesn’t it, I would have never guessed this would happen between us."

    JESSE "I was hoping that you’d have both of the torn pages honestly, but I guess maybe my dad tried to use it back then or something… there are like 7 years unnaccounted for…"
    JESSE "I guess I’m just worried this page could cause more trouble… then again the cult does have the entire book, so what’s one more page to them."

    LUKE "I wouldn’t worry about that too much, but I’m sorry that I can’t tell you where that second page is. Sadly, there’s not many other options at this point… But you now have the tool to finish this once and for all."

    NAR "LUKE RANK MAX"

    JESSE "yeah, and now we don’t have to worry about trying to get the tome back from them in the middle of it, which means that there’s nearly no risk in this for any of my friends…"

    JESSE "Thank you Luke… for everything, your help means more to me than you could ever know… which I’m not sure what that’s like to hear from someone you know is going to die soon."

    JESSE "I think… i’m going to stay here for a little while longer, truly make peace with it you know. Like you said, I need to make sure I’m ready when the decision is actually in my face."

    LUKE "I’m sorry I couldn’t do more Jesse, but I’ve never been
    more proud. I’m sure your friends won’t forget what you’ve done, I know I won’t. Be proud of yourself too, everyone’s story has an end."

    LUKE "Goodbye Jesse."

    hide luke

    NAR "Sitting there, in silence, and after some time…"

    JESSE "I think I got rid of his fears for all of this more than my own… now he thinks that I don’t know when that second page was torn… the rat bastard… this entire time huh…"

    JESSE "The only way he would react like that, is if he was worried I might have a second option, and that he knew there were two tears, except there’s no way anyone would know about the second tear."

    JESSE "Unless they were a part of the cult. Hahahahaha… hahaha…"

    NAR "This spell. This disruption spell… this isn’t the answer at all. I didn’t even need this, I already have it in the tome. Luke… it turns out they’ve needed me since the beginning. I have to be the one to cast this spell…"

    NAR "Suddenly, sitting down next to me, in the usual blue, Cathee."

    show cathee

    CATHEE "Lookin a little down aren’t you now. But you’re right there, you just need one little thing to push you to victory! You’ve gotten so far, but there’s only one mystery left!"

    JESSE "Is there now. Do tell, did you already know all of this would happen!?"

    CATHEE "Hey now, no need to be rude. See they had hundreds of plans to get you to complete all this for them, meanwhile I’m just here happy this happened to work out in favor."

    CATHEE "Good job out there kid. Your pops was right about you after all. Gonna be honest, I had my doubts here and there."

    JESSE "Ha… their real goal this entire time, has just been to get me to cast their final super spell by any means necessary… well that is not it."

    JESSE "they had plenty to keep themselves busy in between trying to manipulate me… my flatmate, my mentor, my work… the people at my dad’s job."

    JESSE "Everyone who’s sole purpose was to trick me into doing something for them, while the rest of the organization did some set up around the country."

    CATHEE "Bingo! And with that last little stunt, they’re probably more confident than they were thinking you had that other random page."


    CATHEE "They gotta restrict your options here, you really think with all the magical power in the world only one spell would do the trick?"

    JESSE "Well… kind of, but when Linden said he was able to alter the glyph to make it work."

    JESSE "There’s no way the upper echelons of those people would overlook that if they didn’t plan for it, and I don’t give Linden enough credit to do it even under those circumstances."
    CATHEE "Let’s be real too, Sara? There’s no way they wouldn’t have realized she would start to develop a thing for you and have a heel turn."

    JESSE "I’m sorry wh-"

    CATHEE "Soooo, did you figure out how you’re gonna stop them."

    JESSE "I… nevermind, I do have one idea."

    JESSE "I know I can’t cast this spell, and if this entire thing has really just been a ploy to get me to cast this magic, then it’s doubtful they really intended to summon their god in the first place…"

    JESSE "Although if I don’t show up, they’ll be uncontested, could actually just summon it anyway without the tome and wreak havoc, which could be a smaller win for them."

    JESSE "Then afterwards they finally just come and kill me and take the book back when they realize it’s a fake. I think the most amusing thing about this is that in the end, the tome is useless to both sides."

    CATHEE "Oh that’s not entirely true, are you saying the legendary magical tome couldn’t possibly hold value just because you’re not gonna use it directly to cast your spell?"

    CATHEE "It’s a grand ancient relic planned to be passed down to the son of a great detective… by said great detective, but the point is you having it right now, is incredibly important to our win condition anyway."

    JESSE "So. When are you going to give it to me?"

    CATHEE "What could you be talking about?"

    JESSE "The page you tore out back in July. What’d you do with it"

    CATHEE "Well, I’m offended you think I would plan to endanger your life AND steal from you on the same day… But I do like playing to win, So I figured I would do it at the same time."

    JESSE "And why didn’t you just tell me all this from the start? We could have avoided a lot of this… assuming that the spell you’re giving me is actually going to help."

    CATHEE "If it was that easy, I would have. But this stuff is complicated, and I don’t think you fully comprehend what you’ve had to learn to get here."

    CATHEE "Let me ask you this. Are you angry that your life for quite some time has all been dragged along and manipulated by those people, and it turns so many of your trusted friends would betray you?"

    JESSE "Of course… all of this started because of what they did to me and my dad… Almost everything bad… if I could take revenge on them and actually win, that’d be incredible…"

    CATHEE "But…"

    JESSE "...without any of what’s happened, I wouldn’t have met these people, and grown to care for so many things because of them…"

    JESSE "I can’t forgive the cult for everything they’ve done, no one could, But I can move on from it, once they pay. I don’t wish anything would change about the past anymore, I just want to keep on going into whatever the future holds."

    CATHEE "Fantastic, that kind of resolve may be enough honestly, and you wouldn’t have any of that if you hadn’t done this on your own, well without my help at least."

    JESSE "I don’t see how that matters when it comes to this though, as if my own willpower would be needed to cast a spell… Oh do you know why they need me specifically?"

    CATHEE "Oh, just some ancient ritual that me and my sisters thought up a long long time ago, it’s really completely by random chance that you can do anything of this!"

    CATHEE "But to answer your previous question, more than you could ever know. Becauseee…"

    NAR "She reaches into her coat and pulls out a piece of paper, specifically the 2nd torn page."

    CATHEE "Now wait, Guess what spell this is."
    hide cathee
    show jesse

    label the_summoning_spell:
    menu:
        "Time Manipulation.":
            hide jesse
            show cathee
            CATHEE "No you can’t control the world with this, but it’s pretty good."
            jump the_summoning_spell

        "The power of Friendship.":
            hide jesse
            show cathee
            CATHEE "Ooh, that’s another amazing one, but sadly no"
            jump the_summoning_spell

        "The Summoning spell.":
            hide jesse
            show cathee
            CATHEE "Bingo"

    CATHEE "i---t's the summoning spell! Here you go! I got to tell you dude, drawing that with the broken pen was actually the scariest part of my life."

    CATHEE "Oh, and don’t worry this one is special, you won’t instantly die if you do right of course. Anyway, I’ll be cheering you on, have fun and good luck out there."

    hide cathee

    NAR "Well, it appears option four does exist."

    scene date_transition

    NAR "The rest of the day proceeded as usual."

    NAR "I’m ready."

    call new_day("Thursday, 26th April 1923")
    NAR "The fateful day. Of course I’m afraid that none of this may work, that I may have given away too much with the second ripped page, with the insanity that the plan has become."

    NAR "It was so simple, just disrupt the spell so they couldn’t subjugate the world, when in reality, me casting the spell most likely would have done that…"

    NAR "Me and Sara got dressed up in our nice outfits that we purchased last week, and headed over to the Carter’s bookstore for one final meeting before all this was over."

    scene bookstore

    NAR "We were the last to arrive, Everyone else already inside, Finn, Evelyn, Felix, and Carter too."
    NAR "While in the end, everything we accomplished may have been for naught if today proceeded as they had intended, if I’m to believe what Cathee was saying, that was all incredibly important to the challenges ahead."

    show finn

    FINN "Everything is set for us to proceed, anything to say."
    hide finn
    show evelyn

    EVELYN "We’ve always been lagging behind what they’ve truly been after, but today we’ll show them what we can do, and that they shouldn’t underestimate us"
    hide evelyn
    show sara

    SARA "From everything they’ve done, to the hardships we’ve been through, it ends today."
    hide sara
    show carter

    CARTER "I finally don’t need to keep letting you guys into the shop… what a wonderful day…"
    hide carter
    show felix

    FELIX "And perhaps it’s the day you actually are able to earn my respect Jesse."
    hide felix
    show jesse

    menu:
        "This case will finally close!":
            hide jesse

        "I won’t let it end here.":
            hide jesse

        "They’ll never see it coming.":
            hide jesse

    NAR "Everyone began to start getting ready and being on their way."

    JESSE "You guys go on without me, I’ll catch up in a second, I want to talk to carter about something real quick"

    NAR "They all left the building, leaving me and Carter alone."

    show carter

    CARTER "No, even after you’ve dealt with them, I’m not recruiting for mine any time soon, especially if we’re gonna have to deal with the fallout."

    JESSE "That’s not it at all-"

    CARTER "And. No, I will not be stopping any of my cult’s activities, we’ve got families to kill, I mean feed. Look I’m not going to have them do anything too much, you know that."

    JESSE "I do… but also not something I really care about right now. What I wanted to ask, do you know any specifics to casting the summon spell."

    NAR "He’s silent for a moment. He clears his throat, he pauses once more, and looks me dead in the eyes."

    hide carter

    scene date_transition

    CARTER "EXCUSE ME. WHAT THE HELL ARE YOU PLAN-"

    scene chapel

    NAR "In front of Westminster Abbey, we all arrive, ready for what’s to come. The wedding set up is extravagant, and despite our age, we don’t stand out too much."

    NAR "We are able to get in easily by following Evelyn’s lead, apparently one of the guards was bribed or convinced somehow by her and Carter… It worked amazingly."

    NAR "From there, Sara was on the lookout for any spies from the cult, while we took the time to blend and mingle before it was time to head down."

    scene cultish

    NAR "Finn led us directly to the hidden tunnel down into the crypts, which did dirty out nice suits, but that’s not even close to a priority at this point in time."

    NAR "We were able to get down to the entrance to the raised area, what Finn described as a ‘Crypt Catwalk.’"

    NAR "We all understood that we were all together just so they could carry me out after casting the spell, But it feels right for all of us to do this together…"

    NAR "Besides, it's an extra reason for me to do this right, because otherwise I’ll get them all killed too, and I will not let that happen."

    NAR "Standing there, the doors to the ritual chamber ahead of us, everyone is ready. And I go to thrust open the doors. Felix grabs my hand."

    show felix

    FELIX "You seem awfully confident for a man without a plan."

    hide felix

    JESSE "..."

    JESSE "Just watch me."

    NAR "I  can sense their trust in me. It’s time to end this, end all of this."

    NAR "Throwing open the doors, we’re greeted by the ritual area. Finn’s description was not entirely inaccurate, this was the top floor of a much larger chamber, the large sigil for the spell on the bottom of the floor beneath the raised area we’ve stepped onto."

    NAR "The alterations to make it capable of also casting Disruption were blatant now that I know what I’m looking for…"

    NAR "Small bridges on the side of the room, and one in the center, all overlooking the ritual ground below, with a dozen or so cult members around chanting."

    NAR "A hooded man stood across from all of us, in much more interesting attire than the normal members, In his hand, he held our replica tome. It’s almost like a play, all the pieces and stage set for this grand display."

    NAR "Fine then… let’s give them a show, my life has been some screenplay they’ve been writing, now it’s time to make their big moment my stage."

    ACOLYTE "It far too late for you to stop us now, we’d discovered your escape, but you do not worry us at all, nothing you can do could stop us, especially when you do not have the tome, that you’ve inconvenienced us with for so long."

    NAR "Oh it’s so blatant. Walking forward, away from the group and out onto the bridge above the giant sigil."

    JESSE "You may be right, but luckily I know some people who have been planning this a lot longer than I have!"

    NAR "I pull out the spell scroll that Luke gave me."

    show jesse

    JESSE "Even without the book, a page from it holds the same power, and I can cast from that just fine. You know this spell don’t you, with this I can end this all right here. Do you have any final things to say"

    NAR "As I say this, I accidentally drop the piece of paper. After audibly expressing my failure, I drop down to grab it before it flies down to the bottom of the room, far… far from reach."

    NAR "Finn, Evelyn, and Sara are shaken, and you can hear Felix stifling a laugh."

    NAR "The Hooded Acolyte, keeps his cool."

    hide jesse

    ACOLYTE "You fail yourself with your own hubris, do you not realize what you’re up against?"

    ACOLYTE "Or do you lack the resolve to break your legs to save what you apparently care for."

    NAR "I stood back up"

    show jesse

    JESSE "Yeah, but why would I do that. When I have the real deal."

    NAR "Pulling out his tome from his coat, and showing it to him"

    JESSE "I’ve gotta commend you on your acting with that prop, thinking that was the real one for all this, I truly do, But I’ve had it this entire time, I’ve also already had this spell in there for weeks if you give me a second to flip through the pages…"

    JESSE "You never stood a chance from the start."

    hide jesse

    ACOLYTE "I-Impossible, how did you make this one…"

    ACOLYTE "this is a trick, the only way you stop us is casting that, and I’m calling your bluff right here, witness the power of our god!"

    NAR "I began to get into a pose to cast the spell, and the Hooded Acolyte pauses for a moment."

    NAR "Suddenly, I slammed the book shut again in his hand. Everyone is shocked."

    show felix

    FELIX "*softly* Oh now this is starting to be fun"

    hide felix

    show jesse

    NAR "I snatched out a separate piece of paper from my coat, the spell scroll given to me by Cathee."

    JESSE "This book is all well and good, but that spell seems boring. Now then I’m calling your bluff on this charade!"

    JESSE "Witness my resolve!"

    JESSE "I call upon you from the darkest of shadows, in the lies and minds, from the hearts of the wicked and the voice of the wind, Avatar of Nyarlathotep, the Black Demon, I summon you to my command!"

    hide jesse

    NAR "A surge of energy explodes first from the scroll and  the black tome, that is then amplified by the great sigil below. The room fills with a dark smoke that swirls with the wind coalescing in the center."

    NAR "Everyone is blown back except me, The Hooded Acolyte’s hood is blown off and is revealed to be none other than Luke Macthorn himself."

    NAR "Everyone in the room is in Awe of what is happening, with some of the acolytes freaking out and trying to stop what’s happening on the lower floor."

    NAR "The shadows finish and take a large humanoid form… A black beast, furry with a long snout, muscular but slim, with tentacle-like strands of fur and muscle coming from it’s joints."

    NAR "It’s eyes are blazing red. It stands imposingly in front of Jesse, the entire room becomes darker from its presence."

    show finn

    FINN "What… the hell…"
    hide finn
    show evelyn

    EVELYN "Wait, we’re doing it ourselves?!"
    hide evelyn
    show sara

    SARA "He’s actually insane… this is his way out isn’t it…"
    hide sara
    show felix

    FELIX "tch, He actually had a plan."

    hide felix

    NAR "The room calms. But I fell to one knee… my entire left arm a pitch black from casting the spell, similar to the darkness that resides in the Black Demon."

    show jesse

    JESSE "First… you will take this plague from me…"

    hide jesse

    NAR "The great beast hews back, and screeches loudly, one arm fighting itself, and the other reaching out towards Jesse, and a vein of darkness travels from him to the beast."

    NAR "Jesse, cured of this all, clutching onto the book, stands back up, and walks in front of the Demon. Staring directly at Luke Macthorn."

    show luke

    LUKE "What… have you done… who… are you…"
    hide luke
    show jesse

    JESSE "You had everything calculated to manipulate and deal with any man or woman who stood in your way. But now you are faced with something far different"

    NAR "The Black Demon’s eyes focus intently on the book in Jesse’s hands… as if crying out to destroy it… to break it free."
    hide jesse
    show luke

    LUKE "You don’t truly expect to be able to control that… banish it before it breaks free entirely! What you’re doing now could destroy everything this world has built!"

    hide luke
    show jesse

    JESSE "Nyarlathotep, I command you to…"

    hide jesse

    menu:
        "Kill them all.":
            show jesse

        "Kill them all.":
            show jesse

        "Kill them all.":
            show jesse


    NAR "No… No you will follow… my orders…"
    hide jesse
    show luke

    LUKE "What we want is to free the people from the shackles of doubt and fear. The great war is proof of man’s inability to govern itself, only more harm will happen in this world if it’s allowed to run free!"

    LUKE "That’s our plan, that’s our goal in the end! That thing will destroy us all"
    hide luke
    show jesse

    JESSE "No… your manipulation is meant for your own abuse, the lives of hundreds… to die without knowing, to live without knowing, you want to control and rule, you can’t even pretend to be righteous in a time like this."

    hide jesse

    NAR "Luke pulls out a thin pistol, and takes aim at me. I attempt to get the Black Demon to protect me, but I can’t tell if I’m fast enough…"

    NAR "I hear a gunshot from behind me, and the gun flies out of his hand."

    NAR "Finn was faster."

    show jesse

    JESSE "In a moment before the god you praise. Nyarlathotep… your servants wish to do the unthinkable… to use your power for their own gain…"

    JESSE "They would have wished to control you with this tome… But the people of this world… would never accept that… I would never accept that… we would never accept that… Aren’t we all Hypocrites?"

    NAR "Nyarlathotep, I command you to…"

    hide jesse

    menu:
        "MURDER  ALL":
            show jesse

        "PILLAGE ALL":
            show jesse

        "DESTROY ALL":
            show jesse

    NAR "No… I won’t falter… when we’re so close… I will not… be constrained… to anyone’s choices… I will choose MY life… and for that…"

    JESSE "Nyarlathotep… I command you…"

    hide jesse

    menu:
        "{i}-End the Game-{/i}":
            show jesse

    JESSE "The twisted sin of your followers… drain them… The corrupt minds of them, Dilute them… Their guilt, account them… Their crimes reveal them… Give them what they’ve run from, give them what they’ve feared for…"

    JESSE "Reave them, Nyarlathotep!"

    hide jesse

    NAR "A horrifying cry arises from the Black Demon. As it’s body forcefully begins to carry out Jesse’s wishes."

    NAR "Black tendrils sprout from the demon, and fly out in ethereal smoke outside of the room, and to all the acolytes in the room. From that day on, all true members of the Guiding Comet changed for the betterment of humanity."

    NAR "The rest of that day was a Blur for me, after that had finished, the black demon had disappeared, and I fell unconscious."

    scene date_transition

    NAR "Finn ran over and picked me up, and the rest began to flee the area, Felix was first to make the calls and contact the people to be on the watch for the great change that I had forced."

    NAR "In the coming days, peace would return, the hidden secrets of the occult would remain a mystery from all but a select few, but that is for the better… They had truly won."
    call new_day("Saturday, April 28th, 1923")

    centered "{color=#ffffff}{size=+30}Epilogue{/size}{/color}"

    NAR "Two days later…"


    NAR "Me, Finn, Evelyn, and Sara all went to the empire Stadium in Wembley, which opened to the public that day. Finn had thought it would be fun to go and watch the game, and to celebrate everything with some bigger event."

    NAR "The crowds of people there were incredible, everyone excited for the final match of that season, the grounds had to be cleared by the police, one stood out amongst them riding a white horse…"

    NAR "The past year had been a journey for all of us, but we made it through the end. There wasn’t any normal to return to, but we could carry on together through whatever we would encounter from there."

    NAR "And it wouldn’t be anywhere near as life threatening, hopefully. No one would ever know what we did, or what was going on beneath them all this time, but they don’t need to."

    NAR "Being able to enjoy the moment, and look forward to events like this, that’s what I’m looking forward to now. I know I haven’t really meant this in a long time… But thanks dad, even if it was hard, it was worth it."

    NAR "The next few weeks, Felix’s goals of revealing and accounting the higher ups in the cult worked out, and it seemed most of them have been purged from society."

    NAR "Many of which were willing to reveal themselves and step down, due to the manipulation by the Demon."

    NAR "Isaac worked towards that too, and was able to bring light back to old cases because of that, I was given extra support from all of it due to the truth about my dad’s death being revealed."

    NAR "Of course none of this ever revealed the cult, or it’s true nature, spun for the general public to accept."

    NAR "Finn was able to actually be on leave for some time, but in the future he would commit himself to our country once again. Evelyn Graduated, and I was working my way back into university while finding other jobs with Felix’s… ‘support.’"
    NAR "Carter continued his own business… and would occasionally inform us of things to watch out for, but he never crossed the line with his activities, especially after all of this."

    NAR "We had received a letter from Linden much later, expressing his gratitude for the way we were able to end their plans, he had pictured things going much differently if the solution was a simple ‘disruption.’"

    NAR "Sara cut her ties to the members of her family that were more involved with the cult, and was also able to avoid any repercussions from their actions, and would try and use her abilities to get a job with the government as well."

    NAR "I would never get the chance to talk to Luke ever again. I had gone over many different ways and many different things I would want to say to him if I met him again…"

    NAR "In the end, I know I’ll never get that chance. What he did for me… in the end, I am thankful for it, he did help me figure everything out after all."

    NAR "I would finally clean up my dad’s study, and start to use it myself. The tome was our way into and out of everything that’s happened, his final gift to me."

    NAR "As much as I enjoyed this ancient and occult tome, it was time to close this chapter for one final time."

    scene apartment

    NAR "I met Cathee one final time, messing with the cat."

    show cathee

    CATHEE "I figured you’d want this in the end too"

    NAR "She pulled out the pen, and gave it to me. Looking at it a little closer…"
    hide cathee
    show jesse

    JESSE "Thanks…"

    JESSE "Although, I think it’s finally out of ink."

    scene date_transition

    NAR "The rest of my life proceeded as “usual”."
    hide jesse
    #FIN


# Return ends the game
return
