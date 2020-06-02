# Chapter 2 begins here

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define NURSE = Character("Nurse")
define FELIX = Character("Felix")
define CARTER = Character("Carter")

label chapter2_start:
    $ current_chapter = 2

    scene room
    centered "{size=+30}CHAPTER 2: Entrance to Madness{/size}"

    call work_day("Thursday, 20th July 1922")

    call work_day("Friday, 21st July 1922")
    call new_day("Saturday, 22nd July 1922")

    scene room

    NAR "The previous two days had left me feeling much more tired than usual… It had to have been something with that book the other day… but still I’ve felt so unnaturally tired… it’s taken so much energy just to get through work…"

    NAR "…"

    NAR "In the middle of making breakfast… I lost consciousness entirely, I can only faintly comprehend the startled fear of Sara witnessing it… and the next time I fully understand what’s going on is…"
    call new_day("Tuesday, 8th August 1922")

    scene hospital

    NAR "Waking up in a completely new bed, and sitting up to look around, I don’t feel as tired as before… but if I’m not mistaken... I’m inside of a hospital?! Moments later he sees a nurse walking by. It also looked like it was the morning…"

    NURSE "Ah good, you are awake. I must go inform the doctors that you are awake then I will be back to give you a checkup."

    JESSE "Alright. I also have a quick question before you go, where are we… and umm, what day is it?"

    NURSE "You are in the hospital, try not to worry yourself too much, reserve your strength, and it is August 8th. Now you sit tight and I will be right back okay."

    NAR "Off the nurse went to go inform the doctors. Within a few minutes she was back checking my vitals to see if everything was okay. We discovered that I was too weak to stand up and would have to recuperate in the hospital for a few days."

    call new_day("Thursday, 10th August 1922")

    scene hospital

    NAR "I had been completely unconscious for over two weeks… Compounding my body's health from before, plus the complete lack of activity, the hospital had me doing various tests and checkups to actually make sure I was healthy."

    NAR "Miraculously, it appeared that I was. They had also told me that Finn and Evelyn had come to visit me on occasion, and that Sara was the one who made sure that I was being taken care of throughout the whole ordeal."

    NAR "Perhaps it was because of my current state that I had forgotten what day it was, but an unexpected visitor arrived at the hospital. It was the 10th of the month after all, and Luke had stopped by to check up on me, and for our scheduled meeting."

    show luke

    LUKE "Well, it appeared that we wouldn’t be able to keep on a consistent schedule after all. That’s a joke, how have you been? Besides your obvious condition."
    hide luke
    show jesse

    menu:
        "Been better.":
            hide jesse
            show luke
            LUKE "I can tell."

        "Feeling good.":
            hide jesse
            show luke
            LUKE "That’s good to hear."

        "Mostly confused.":
            hide jesse
            show luke
            LUKE "I would be lying if I said I wasn’t either."

    LUKE "I can understand if you don’t want to talk about it. I’m not going to try and think of the ways you could have ended up here…"

    LUKE "But i’ll just say it’s part of our agreement for me to help you out… Which is partly why I’m here. I figured you hadn’t gotten too many visitors since then."

    NAR "We ended up talking casually, and he was bringing me up to date on all the happenings and things I missed while I was asleep. Eventually we reached the natural conclusion to everything."

    LUKE "Something I wanted to say as a final thing Jesse… Before you were unsure whether or not you wanted to keep continuing with something that your friends had brought up to you, or at least something along those lines."

    LUKE "I’d confirm with yourself how far you want to go with that, assuming it could have been related to this in any way."

    LUKE "Anyway, I’ll let you get some more rest. I’ll see you next time. Although it will be a while, you have work on the 25th I believe. Good luck with however you choose to proceed."

    hide Luke

    NAR "Luke left the room after we said our goodbyes to each other. I looked at the stand to his right and noticed a book. There sat the same dark book with ruby colored writing on the front of it in a language I could not discern."

    NAR "A nurse entered the room to check on me."

    NURSE "How are you doing today? Better than yesterday hopefully."

    JESSE "Yeah, I have a bit more energy, but my legs are still weak."

    NURSE "Well, we will get you a little bit of food and see if you can hold it down. Until then, rest well."

    NAR "The nurse left the room and I looked back to the nightstand. The book seemingly vanished. He wondered if he was imagining the book or not. I thought it best to think I had imagined the book due to the various drugs I had been on in the hospital."

    NAR "The rest of the evening proceeded as usual… for being stuck in the hospital. "

    call new_day("Monday, 14th August 1922")

    scene hospital

    NAR "I had been in the hospital for another few days before I finally regained my strength to stand up. Today I am allowed to be discharged. The nurses told me that Sara would be here to pick me up from the hospital."

    NAR "It had been a long week. Over two weeks have already passed since I had been in a coma, but an entire two weeks felt instantaneous. That week in the hospital felt like I had sat there for those two weeks entirely."

    NAR "Time seemed to pass by so slow and at the back of my mind, I kept picturing that dark book. my mind was riddled with thoughts on the book, but it’s probably best to keep quiet about the book for the time being."

    NAR "Sara did indeed come to pick me up in the afternoon after filling out all of the paperwork. She said hello and we had a small conversation on the way back home."

    scene city

    show sara

    SARA "So how was it being in that place for nearly three weeks?"

    JESSE "Pretty horrible. Those few days I could actually be awake for felt like weeks, and it was like I was afraid for a bit that it would take even longer to be discharged."

    SARA "I can imagine. Must have felt like you were stuck in Purgatory."

    JESSE "Yep."

    SARA "But now, you’re back… but make sure you don’t overexert yourself right? Don’t want that happening again do we."

    JESSE "heh, I’ll try not to."

    scene room

    NAR "We continued our small chat on the way to the apartment. I ate a hearty dinner and then remembered something."

    NAR "The book. I wanted to go check where that dark book was and whether or not I had been hallucinating the book being next to me. When I got the chance, I rushed to the desk where I had left the book before being admitted into the hospital."

    NAR "It was still there, sitting at the edge of the desk in the same position I had imagined it on the nightstand in the hospital. That’s all it was. My imagination."

    call new_day("Tuesday, 15th August 1922")

    scene room

    NAR "I woke up in the morning and was called by Finn since he wanted to know how I was after being discharged."

    FINN "Hey mate, how’s your morning doing, How have you been since being discharged?"

    JESSE "Good good. It was nice to sleep in my own bed once again. Did you want to try and meet up for something today?"

    FINN "Of course. We can go to a cafe down the road around noon. I will invite Evelyn as well."

    JESSE "Sounds good. See you then!"

    scene cafe

    show jesse

    NAR "We all met up in the usual cafe, and sat down, ordering some lunch as well. After basic introductions, and calming their generic worries about him."

    JESSE "Yeah, the entire situation involving that day on the train was confusing for me. It seemed like a set up, and I had seen one of the people set up for the execution that day on the train. But it seemed like that cult was setting up some sort of execution of their own."

    JESSE "My involvement in it… was essentially chance, there’s been this strange woman who has shown up just… given me cryptic assistance and I’m not sure what to make of it."

    hide jesse

    show finn

    FINN "A strange woman? Should we try to look into her at all?"

    JESSE "I want to say yes… but the way they have been seems like she isn’t even real… if a strange woman in blue ever approaches you cryptically, definitely bring it up, but otherwise, probably not something we can actively look into."

    JESSE "She’s definitely related to the cult’s actions, so hopefully we’ll learn more as we continue on?"

    JESSE "I still have no idea what entirely happened on that train though, it all happened so quickly for me… I used the book and read from a page that fell out of it, and then everything happened."
    hide finn
    show evelyn

    EVELYN "I think I know what happened that day on the train. I have had a while to think about it now since you were in the hospital."

    EVELYN "I researched the book with the marking that you showed me and I cannot find anything on the book itself. But… from what I found my best guess is that what you recited was an incantation, something used to conjure a spell."

    NAR "It’s a bit surreal… but it adds up…"

    JESSE "Makes sense after what it did when I recited the incantation. I only thought to do it because I saw other people, presumably acolytes from."
    hide evelyn
    show finn

    FINN "So… you’re saying you’re a wizard?"

    JESSE "I… I mean, no? It wasn’t really intentional… but it was certainly magic…"

    FINN "Either way, it’s incredible mate."
    hide finn
    show evelyn

    EVELYN "From what I gathered, you need to not only transcribe it perfectly, you need to recite the incantation specific to it, and honestly…"

    EVELYN "I’m impressed you were able to do it so easily for what was such a powerful spell, it was the shield one right?"

    JESSE "Huh, yeah it was… I assume that was on one of the scraps I gave you earlier? But no, it was actually all written for me already…"

    JESSE "I assume it had something to do with the blue woman. How’d you figure out so much about this anyway? I’m impressed."
    hide evelyn
    show finn

    FINN "Oh yeah, about that, we’ve actually got someone we want you to meet, we think it’ll help us out a lot afterwards. We can trust him, don’t worry."
    hide finn
    show evelyn

    EVELYN "I will… warn you though, he is a bit interesting… I’m not sure if you’re gonna like it."

    EVELYN "We were gonna try and set up a meeting with him thursday because he’s busy tomorrow. but we’ll schedule it for monday because you’re still going to keep working right"

    JESSE "Yeah, I’m able to now, and besides, trying to stick to a schedule is a good alibi right?"
    hide evelyn
    show finn

    FINN "Yeah, good luck man, we’ll see you on monday!"

    hide finn

    NAR "The three of us finished our meal, and chatted about other unimportant topics, but we eventually all left. I headed back home."

    NAR "The rest of the day proceeded as usual, However…"

    NAR "In a different part of the Cafe, clearly having been watching and eavesdropping on their conversation."

    show felix

    FELIX "Hmm… to think they would be so blatant right after he was released from the hospital. I’ll be keeping an eye on you… don’t disappoint me too much Jesse."

    hide Felix

    hide cafe

    call new_day("Wednesday, 16th August 1922")
    label free_day_8_16:
    call free_day("charm", "Finn", "Evelyn")

    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Finn"
            call finn_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Evelyn"
            call evelyn_hangout

    if(hangout_failed):
        jump free_day_8_16

    #Finn
    #Evelyn
    #Gardening

    call work_day("Thursday, 17th August 1922")

    call work_day("Friday, 18th August 1922")

    call new_day("Saturday, 19th August 1922")
    call half_free_day
    #Walk
    #Study
    #Gardening

    call work_day("Sunday, 20th August 1922")
    call new_day("Monday, 21st August 1922")

    scene bookstore

    NAR "As planned, I got a call from Finn and met up with the two of them and followed them to a bookstore. The two of them have been acting a little strangely… What have they signed me up for?"

    NAR "Inside it was mostly empty. A man stood there behind the counter expectantly. He closed his book and turned to face us."

    show carter

    CARTER "Oh hello everyone. And welcome to my lovely store once again, and you’ve brought… the friend…"

    CARTER "My Name is Carter Wilkinson, and I am the owner of this establishment… now I’m told you’re here to talk."
    hide carter
    show finn

    FINN "Okay Jesse have fun."
    hide finn
    show evelyn

    EVELYN "You’ll do great, we believe in you"

    hide evelyn

    NAR "The two of them walked over to another part of the store immediately, leaving me with Mr. Wilkinson."

    JESSE "Uh, guys?"

    show carter

    CARTER "Oh hello… so they’ve told me some interesting things. So, first question I have for you… They’ve mentioned you’re smart? Any actual accolades? Where’s that talent from?"

    JESSE "I… Well I don’t think I’m actually that impressive at all, but I’ve picked up a lot of things from my dad, who was a renowned investigator, and university was really easy for me until…"

    JESSE "Wait why do you even need to know that? They told me you know something about magic?"

    CARTER "Oh what magic? Like street magic? It’s just a bunch of sleight of hand and fancy tricks you know. It’s not actually real. But you’re modest, and have real talent, anyway…"

    CARTER "Second question, how much would you be willing to do to get to stop the evils in this world?"

    JESSE "What? I mean, already I’ve been a lot more invested in this, but I’m still hesitant, but at this point I think I’m already too deep to back off now, so probably whatever it takes…"

    JESSE "Well no that’s not true I’m still not fully confident in all of this, why am I saying this, what are you doing? You know what I’m talking about, not silly street magic, real occult magic."

    CARTER "I like it, I like it, and yes of course magic exists, it’s what I’m using to you to talk so much, it’s my specialty, it only works on those wanting some information from me…"

    CARTER "But you know Stout, I love your attitude, before I get to my offer, what are you really here for? I’ve heard about a book, yes?"

    JESSE "Yes… that’s why we’re here in the first place… not for whatever you want from me?"

    CARTER "We’ll get to it, don’t worry, just show me"

    NAR "I took out the book, and showed it to him."

    CARTER "OH, Oh nevermind, good day, sorry about that, ignore everything I was talking about, it’s fine, you don’t owe me anything, and once again, I’m sorry for leading you on in the slightest."

    JESSE "Excuse me?"

    CARTER "I’m sorry I didn’t realize. I was going to ask you about joining my cult."

    JESSE "Excuse me!?"

    CARTER "But, don’t worry about that anymore, you’re not allowed in. I don’t want to get anybody in that’s already involved with them."

    JESSE "I don’t think that’s the problem here… do my friends realize? Why are you so casual about this?!"

    CARTER "Of course they knew, and they’re liars, they said that you’d be suitable to join me… that’s the only reason I accepted this little bid anyway. But…"

    CARTER "How about this Stout, I know a lot about this type of stuff, one could say it’s my specialty, come back tomorrow, and I’ll tell you whatever you want to know, just need to make some preparations."

    CARTER "Because I am willing to make a deal with you. I want that cult dealt with, but I don’t want to directly be an aggressor against it. Which is where you come in! I’ll be waiting tomorrow."

    JESSE "It's… a deal… I guess."

    hide carter

    NAR "I took the book back from the counter, and went over and grabbed Finn and Evelyn."

    show jesse

    menu:
        "Why.":
            hide jesse

        "You knew.":
            hide jesse

        "I hate you guys.":
            hide jesse

    show finn

    FINN "haha… I’m sorry mate but it worked out didn’t it. And, I’m sorry we didn’t tell you about any of that… it was part of what he wanted out of this..."
    hide finn
    show evelyn

    EVELYN "Yeah… he’s interesting but he is actually an asset we can use."

    JESSE "I hate that you’re right…"

    hide evelyn

    NAR "The three of us enjoyed some time together after we left, but then we went our separate ways… they knew exactly what I was walking into…"

    scene date_transition

    NAR "The rest of the day proceeded as usual."
    call new_day("Tuesday, 22nd August 1922")

    scene bookstore
    NAR "The following day, Me, Finn, and Evelyn went back to an empty bookstore. It appeared that Carter had closed the store down for the day. I knocked on the door and Carter answered moments later."

    JESSE "Hello again Wilkinson. Are you ready to talk now?"

    show carter

    CARTER "I sure am. It was not easy to find this old book. It has text similar to the pages in your tome. Now let’s get to translating that page."

    JESSE "you… know this book is mostly blank right?"

    CARTER "It’s a spell tome, that’s the point, but the point is to put spells into it, and that’s what this one is all about, what we care about is the page itself, the parchment, the paper."

    CARTER "But usually using these things with an instrument like that takes a toll on the body. As if you’re casting them with a part of your soul. Usually it’s minor, but that one just feels powerful, it’s got that aura."

    JESSE "That doesn’t make much sense, and what do you mean it uses part of my soul?"

    CARTER "Well it uses part of the user’s energy as well it would seem, depending on the strength of the spell, and as a note, your tome in general amplifies spells an incredible amount, but the toll on your body is also increased by the same amount."

    CARTER "Now, there is a little difficulty with all of this however, because of those scraps of writing you actually have. They’re definitely spells, but they’re not special in any way, written how they are."

    CARTER "They could all become immensely powerful if you can use them with that tome, however I regret to tell you that I cannot translate them either."
    hide carter
    show evelyn

    EVELYN "I thought you said you knew how this stuff works?"
    hide evelyn
    show carter

    CARTER "Well I do! But we all do our own techniques a little differently, of course I get the general idea with these, but they’re written specific to those cultists. Now it’s not like all of this is exclusive, you could still cast things that I know through the one you have there."

    JESSE "Is that going to be relevant."

    CARTER "I’ll get to it, that’s partly why I figured we should all meet up again rather than just me and you."

    CARTER "To start with, why don’t you try copying this spell into the book? It's basic dispel magic, but it would probably just negate plenty of effects coming from that thing."

    NAR "I pulled the black tome and the pen out of my coat, and placed them onto the table, opening it up, I noticed something that wasn’t there before… or rather, what should have been."

    CARTER "Wait a moment, there are pages TORN from this thing? That’s absolutely incredible. You need to be empowered magically, or just a greater being in the first place to even have a hope of tearing this thing."

    NAR "There was now a second page torn from the front of the book. I can guarantee there was only one originally… How could that have happened? Well, there’s probably only one way, assuming no one else found the book while I was unconscious."

    CARTER "But either way, I could do it for you, but you should probably get some practice, I heard that pen was actually broken?"

    NAR "I tried my best to copy the spell that Carter had pulled out into the book… but it ended up taking two pages, this does seem like something I’ll have to practice, only because of the faultiness of this pen."

    CARTER "Well… your second try is plenty good, but that first one is essentially worthless. You’ve got plenty of these pages though, it’s fine."
    hide carter
    show finn

    FINN "Now are you going to try and tell us we’ll need this soon?"
    hide finn
    show carter

    CARTER "...possibly… Well look, it’s not actually guaranteed that you’ll need it, but it’s the best guess, and the best idea I have.  Now this is top secret information, that I only feel comfortable telling to fellow cult members…"

    JESSE "No."

    CARTER "We’ve already been over this, I don’t want any of you… you’re not very fun."

    CARTER "I was gonna say that I’m making an exception with you three, because you’ve inspired me with you’re willingness to sign up for suicide, and by that I mean, making moves against the Guiding Comet."
    hide carter
    show finn

    FINN "That’s… certainly a way to phrase it, but… thanks?"
    hide finn
    show carter

    CARTER "Now then, what’s actually happening. I’ve had spies lurking and getting information from all the cults around, and recently there’s been more and more news specifically about the big dogs in the city."

    CARTER "The people we’re all the worst of friends with. It looks like they're on the hunt for some powerful and ancient items, most of them honest myths. To progress with this, part of their plans is some honest explosive terrorism."

    CARTER "From what we gather, they’re targeting two locations, one of them up north in Whitehaven, and one of them down here in London."

    CARTER "Obviously, I have a lot more information on the one here, but it’s not enough to be truly meaningful, because we know where our boundaries are with information gathering. That being said, we can assume their target here is a church."
    hide carter
    show evelyn

    EVELYN "Do you know why they’d be targeting a church? What exactly does just blowing things up do for them exactly…"
    hide evelyn
    show carter

    CARTER "Your guess is as good as ours, you see you’ve got people like me, where our goals are just for some small stuff, like immortality and infinite knowledge you know? These guys are on a different level."

    CARTER "they play both sides of many situations and always pick whatever is the better outcome for them, albeit that better outcome isn’t really parseable by my people. these guys are looking for some sort of control over the world."
    hide carter
    show evelyn

    EVELYN "Anything else?"
    hide evelyn
    show carter

    CARTER "Nope. Look I’ll help how I can, and feel free to come back if you ever want extra help with spellcasting and other parts of this, as long as you’re working against them, I’m working with you."

    CARTER "Oh and by the way, not to worry you guys at all, but the attacks are going to happen in about two weeks, on September 4th."

    JESSE "Well… thanks for that."

    hide carter

    NAR "Nothing else of note was brought up that day, Evelyn and Finn said they would go and start looking into potential churches that would be their targets."

    NAR "One that would be within their sphere of influence, or ones that seem to go against what we know of their motivations, and their locations' viability for secret activities."

    NAR "Besides that…  I was just going to wait and go about things normally, perhaps practicing writing with a broken pen."

    scene date_transition

    NAR "The rest of the day proceeded as usual."

    call new_day("Wednesday, 23rd August 1922")
    label free_day_8_23:
    call free_day("charm", "Carter", "Finn")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Carter"
            call carter_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Finn"
            call finn_hangout

    if(hangout_failed):
        jump free_day_8_23
    #Carter
    #Finn
    #Gardening


    call work_day("Thursday, 24th August 1922")

    call work_day("Friday, 25th August 1922")

    call new_day("Saturday, 26th August 1922")
    call half_free_day
    #Walk
    #Study
    #Gardening

    call work_day("Sunday, 27th August 1922")

    call new_day("Monday, 28th August 1922")
    label free_day_8_28:
    call free_day("courage", "Carter", "Evelyn")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Carter"
            call carter_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Evelyn"
            call evelyn_hangout

    if(hangout_failed):
        jump free_day_8_28
    #Carter
    #Evelyn
    #Walk

    call new_day("Tuesday, 29th August 1922")
    label free_day_8_29:
    call free_day("knowledge", "Carter", "Evelyn")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Carter"
            call carter_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Evelyn"
            call evelyn_hangout

    if(hangout_failed):
        jump free_day_8_29
    #Carter
    #Evelyn
    #Study
    call new_day("Wednesday, 30th August 1922")

    scene cafe

    NAR "It’s been about a week since we learned about the cult’s next potential target, I got a call from Finn asking if I was free to talk about things more in detail today."

    NAR "Finn, Evelyn, and I met at a cafe to have a discussion."

    JESSE "So, have you guys made any progress into finding one that might be more suitable for their attack than the others?"

    show evelyn

    EVELYN "Well, I researched a bit into previous oddities that could probably have been related to them, then checked those with Carter to see if there were any correlations between them."

    EVELYN "Honestly that’s what brought down the number of potential targets down significantly."
    hide evelyn
    show finn

    FINN "Then the targets we had left, I went and investigated the area itself to see if there were any direct entrances or locations around them that would make their activities even possible."

    JESSE "Considering the magic Wilkinson thinks will actually be effective here, it’d have to be some sort of magic ritual that they’re planning"

    FINN "Yeah, that’s what he mentioned, so it was part of what I was looking for when I was scouting out the places. Realistically though, we still have three potential areas it could be… and you can’t get to all three of them."
    hide finn
    show evelyn

    EVELYN "Sadly we couldn’t really find anything specific that would make it easier to pick out which one it would be exactly…"

    EVELYN "I think if we knew their target up in Whitehaven it’d be a lot easier, but that’s too far for us to try and look into, and we’re running out of time…"
    hide evelyn
    show finn

    FINN "It’s the best we got, and the odds are a lot more in our favor than they were before now right? Here, if you want to get a general idea, these are the three churches that we've narrowed down to Jesse."

    NAR "He handed me a list of the three… Not even name wise there was anything important to go off of. St. Magnus, Temple Church, and St Mary Aldermary."

    NAR "Even if I tried to research them, I doubt I’d come up with something that Evelyn hasn’t already looked into… Do they expect me to just guess?"
    hide finn
    show evelyn

    EVELYN "We’ll try our best to find actual detail on it soon, but otherwise, we can still try and find the right one the day of, Maybe we’ll get lucky right?"

    EVELYN "We’ll still try our best to get a better idea, and we’ll talk next time you’re free… which is the 4th…"
    EVELYN "In terms of an actual plan, we should meet up on the 4th, and once we find where they actually are, me and Finn can try and get actual authorities to stop what’s happening after you’re able to dispel the ritual or something."

    EVELYN "Assuming Wilkinson was right about what’s happening. But of course, we’ll work out the specifics on our part over the week."

    hide Evelyn

    NAR "It wasn’t much… and even if it feels like we won’t actually find them, this is a chance to actually combat them. We have to take it. We ate and said our goodbyes."

    scene date_transition

    NAR "The rest of the day proceeded as usual."

    call work_day("Thursday, 31st August 1922")

    call work_day("Friday, 1st September 1922")

    call new_day("Saturday, 2nd September 1922")
    call half_free_day
    #Walk
    #Study
    #gardening

    call work_day("Sunday, 3rd September 1922")
    call new_day("Monday, 4th September 1922")

    scene room

    NAR "It was day, the day that the cult would attack a church here in our city. We had only narrowed it down to three… but that was from nothing."
    NAR "In the end, all we need to do is find it, and I need to cast another spell. We had planned to meet up around noon at the Cafe like usual. As I was getting ready to leave, there was a knock on the door. I opened it up… to someone I had never seen before?"

    show felix

    FELIX "Hello Stout, My name is Felix Roark, I’d like to ask you a few questions this morning."
    hide felix
    show jesse

    menu:
        "I was just about to leave…":
            hide jesse
            show felix
            FELIX "I believe you can wait."

        "Not right now.":
            hide jesse
            show felix
            FELIX "I’m afraid I can’t reschedule."

        "Who are you?":
            hide jesse
            show felix
            FELIX "Tch, you disappoint me already."

    NAR "Before he continued talking, he pulled out a badge from his coat, he was a private investigator?! But he was young… about my age probably."

    FELIX "I’m sorry but you don’t have much of a choice in this, however it will be quick, I believe I already know all the answers in the first place."

    JESSE "Do you now? Do you happen to have anything legal that actually says you can get those answers then?"

    FELIX "For your own sake, no, but if you’d like to remove your accountability from this at all, I can bring my evidence straight to the law, they wouldn’t mind."

    JESSE "What do you want?"

    NAR "I conceded, and let him inside. We both sat down… he sat next to the chair my dad would use."

    FELIX "Answer me truthfully stout, and I might be lenient. What amazes me most is that you're the son of that famous investigator, so why is it that you’re a part of the Cult run by that man at the bookstore?"

    NAR "What?!"
    hide felix
    show jesse

    menu:
        "What?!":
            hide jesse
            show felix
            FELIX "Don’t play dumb with me"

        "No, that’s wrong.":
            hide jesse
            show felix
            FELIX "So you do deny it."

        "And what if I am?":
            hide jesse
            show felix
            FELIX "You treat that so casually?!"

    FELIX "I’ve had an eye on you ever since you left the hospital about a month ago. I know you’re going to the church today under his orders."

    FELIX "And I’m to believe you’re able to do some sort of witchcraft, to think how low you’d go, do you have no respect for your dad?"

    NAR "I stood up."

    JESSE "That’s not what this is about at all. You’ve got all of that wrong, I’m not a part of any of that, and I’m going to save them from an attack not do it myself."

    JESSE "If you think so highly of yourself maybe you could look into what’s happening a bit closer. Maybe die like the man you keep referencing so much."

    NAR "I begin getting my things and start to exit the room anyway, he knows he doesn’t actually have power over me too."

    FELIX "I’ve seemed to have struck a nerve. You wouldn’t get so emotional if I wasn’t right about something. If you want to talk somewhere else, we can talk at the church too."
    hide felix
    show jesse

    menu:
        "What, you going to follow me?":
            hide jesse
            show felix
            FELIX "Why would I do that?"

        "You know where it is?":
            hide jesse
            show felix
            FELIX "Of course I do"

        "Like I'd tell you where it is.":
            hide jesse
            show felix
            FELIX "I already know where it is"

    FELIX "I have already looked into it, enough to know where it’s going to happen. What’s with that shock of confusion? Do you… not know where it is."
    hide felix
    show jesse

    menu:
        "Magnus.":
            hide jesse
            show felix
            FELIX "You disappoint me."

        "Mary.":
            hide jesse
            show felix
            FELIX "Hmph, was that a guess?"

        "Temple.":
            hide jesse
            show felix
            FELIX "You disappoint me."

    FELIX "Even if you were right, that was just a guess. Perhaps I overestimated you. Fine, I believe you."

    FELIX "Now then if you want to actually go to the correct place and not let people die, you’ll let me tag along on your little venture, then maybe I’ll decide to follow through with allegations against you."

    NAR "Who does this guy think he is? I begin to walk to the Cafe, with him trailing me."

    JESSE "So, which was the right one, or were you just messing with me?"

    FELIX "St. Mary Aldermary"

    hide felix

    NAR "..."

    hide room

    scene city

    NAR "Just before we got to the meeting place with Finn and Evelyn…"

    JESSE "So, I take it you haven’t been wrong about a lot of your deductions."

    show felix

    FELIX "Of course not, I actually have a brain for this."

    JESSE "So how are you taking the failure you had earlier."

    FELIX "What do you mean by that."

    JESSE "Oh just the fact that you thought I was a part of Carter’s cult and trying to attack the St. Mary."

    FELIX "You honestly thought I believed that? It was an act to get in your head, you do understand what you’re getting involved with don’t you. I had to make sure you were trustworthy."

    JESSE "Really now?"

    JESSE "What’s the name of the cult that’s really attacking this place."

    FELIX "I don’t need to answer that, we both know after all, no need to say the name aloud."

    JESSE "Sure thing Roark."

    hide felix

    NAR "Yeah right."

    NAR "As we were about to meet with them… I noticed Evelyn starts to get defensive, and stealthfully approaches to probably blindside Roark. I… almost want to let her…"

    NAR "But then Felix noticed her and introduced himself. Dammit."

    show felix

    FELIX "Hello, don’t be alarmed. My name is Felix Roark, I’m a private investigator, and I’m offering to help you on your mission against the cult attacking the St. Mary Aldermary today."
    hide felix
    show evelyn

    EVELYN "Wait… did you figure that out on your own?"
    hide evelyn
    show felix

    FELIX "I’m sorry, but I have been keeping an eye on all of you, so I did start with some of your initial deductions, but yes, since I’ve trained for this, it was obviously easier for me to discover their true target."
    hide felix
    show finn

    FINN "That makes this so much easier, now you can go and be ready to dispel it easily!"

    JESSE "Hey, don’t mention our plans too much, Roark is helping us, but we can’t just trust him completely just yet."
    hide finn
    show felix

    FELIX "Not that you need to, I already know that you plan to use this dispel to stop the magic produced by the sigils that have been set up in that church."

    NAR "Bullshit… he’s just going with it because he actually trusts what Finn said about me being able to dispel something…"

    NAR "the rest of what he said is a good plan though, and he would have had to have checked out the church beforehand…"

    FELIX "Are you all ready?"
    hide felix
    show evelyn

    EVELYN "Well, if we already know where the church is, why don’t we split up and try to figure out how to get authorities to clean up what happens after Jesse casts the spell, since we can’t necessarily just let the cultists leave scot free right?"
    hide evelyn
    show felix

    FELIX "In that case, why don’t you two do that, you can take my card as well for extra backing. I’ve already taken a look into the church and found where it would be attacked from, so I can keep Jesse out of that."
    hide felix
    show evelyn

    EVELYN "That’s… a pretty good idea."
    hide evelyn
    show finn

    FINN "You cool with that Jesse?"

    NAR "Hell no. As much as I hate this guy already, I get the feeling he actually is trustworthy… just full of himself…"

    JESSE "Yeah, that’d work out… and it’d be a way to guarantee we can trust each other Roark. Don’t think we don’t have backups in case this doesn’t work, you do know what we’re up against after all."
    hide finn
    show felix

    FELIX "Of course."

    NAR "Please… just don’t say anything about that being a lie guys."

    FELIX "That is if you can sustain the energy it would take to do multiple things there."

    NAR "Of course, he knew I was in the hospital and visited Wilkinson."

    JESSE "Yeah, Or do you not know how this works? I understand if you didn’t, not many do."

    hide felix

    scene chapel

    NAR "We separated, and Felix and I traveled to the church, and I had never been there, so he had to show me the way… he didn’t make a big deal out of it, but I just have this feeling about how he’s thinking about it…"

    NAR "I got to the position near the top of the church, from the vantage I could see what appeared to be a sigil placed all throughout the room, it was still distorted from this angle, but presumably from underneath it would be a complete spell sigil."

    NAR "I need to wait for it to begin glowing, and then I can use the dispel magic from Wilkinson, at least that’s how I was told to do it."

    NAR "Felix said he’d keep lookout, and throw up a stone up at the glass to alert me. It was actually almost two hours of waiting for something to happen."

    NAR "However I still had a moment of panic when it actually began to happen. Of course I believed all of this was real, I experienced it, but it was all still so surreal to me…"

    NAR "I hesitated for a moment… Wilkinson said this spell was weaker… but that it’ll still drain me incredibly because of the extra power this specific tome imbues it’s magic with… but I’ll just be tired for a bit right?"

    NAR "This has got to be weaker than that shield that I used in July. I opened up the black tome and began to recite the words Wilkinson taught me for Dispel magic, and unleashed the spell."

    NAR "The color in the sigil below began to fade… but it didn’t feel like much else happened, it was mostly silent. Until suddenly, a knock on the glass."

    NAR "That was the signal! I was already feeling incredibly tired from casting it… But it wasn’t impossible to manage… I had to find somewhere else to hide."

    NAR "The glass pinged again. Where? There’s not really anywhere up here… maybe I could just."

    NAR "The glass pinged again."

    NAR "They’ll hear it too at this point I got the first warning! This is just. The glass pinged again."

    NAR "This is just adding to the warning. I heard the fluttering of wings outside the window. It was just a bird…"

    NAR "Bloody thing nearly scared me to death… did it really not have anything better to do?"

    NAR "I did feel really tired however… and my arm was a bit numb… I rolled up my sleeve because of where it felt… and… what… is that?"

    NAR "Part of my forearm, above the elbow was suddenly a pitch charcoal black, I couldn’t feel anything on or around that spot in my arm."

    NAR "It really is draining me, but… it’s not that big, it’s going to heal, I just needed rest like last time. I think… I’ll just rest here until they come and get me."

    NAR "Finn and Evelyn should be back here by now too, I just hope Roark doesn’t come in and see me like this…"

    scene date_transition

    NAR "It was hard to focus for the rest of the day, but Finn was the one who came up and dragged me back home, he stayed as long as he could before Sara would get back."

    NAR "I ended up regaining most of my senses after a bit. We figured we could meet up again when I feel a bit better tomorrow."

    NAR "He also told me that they were successful, and it looks like Roark is taking credit for finding a group of potential terrorists before they were able to act. The son of…"

    NAR "They told me later that it seems like they were able to apprehend four individuals in an area underneath the church itself."

    NAR "Upon the failure of their actions, they were confused and distraught, being caught off guard by the few officers that were convinced to check things out."

    NAR "They burned everything that was there without using magic, and were arrested before causing any more damage…"

    NAR "I went to bed much earlier that day."
    call new_day("Tuesday, 5th September 1922")
    NAR "Waking up, I still felt incredibly tired, awake, but physically tired. I was going to go and meet up with Finn and Evelyn today…"
    NAR "I waited for them to get there, then struggled to walk over. My arm wasn’t entirely numb anymore, but I still couldn’t feel much of anything from that darker spot."

    scene cafe
    NAR "I met up with Finn, and then Evelyn joined us a little later. We greeted her."

    show evelyn

    EVELYN "Morning you two."

    EVELYN "Did you two hear about the explosion?"

    JESSE "You mean the one in Whitehaven?"
    hide evelyn
    show finn

    FINN "Yeah, there was an explosion in the coal mines up there. Nothing cultish it seems, but I saw it in the news before I got here. And that would line up with what we were talking about."

    NAR "I notice Wilkinson entering the Cafe, and he begins to walk straight towards our group."
    hide finn
    show carter

    CARTER "Hey you three. Nice cafe spot you’ve found here, think I’ll visit it more often. Anyway, I have been looking for you all. I have something I need you to hear. Especially you, Jesse."

    JESSE "Well, what is it?"

    CARTER "Rather not say it here. Although I think I’ll stop by here more often. "

    JESSE "Well then just whisper it in my ear and I will tell these two later."

    CARTER "Alright fine, but don’t blame me for this. Huddle in and I’ll just tell you three as quietly as I can."

    CARTER "Some bad people might be coming back around these parts of town soon Jesse. Specifically the lot that killed your father."

    NAR "The… people that killed him… why would they… are they going to kill us too?! No… No, I can’t get worked up about this."

    CARTER "All I’m saying is to be careful and watch where you tread."
    hide carter
    show evelyn

    EVELYN "Thank you Wilkinson. Do you think you can meet us at the school library tomorrow evening after you close shop? I think we may need your help with some research."
    hide evelyn
    show carter

    CARTER "Sure, I can help."

    scene date_transition

    NAR "The rest of the day proceeded as usual."

    call new_day("Wednesday, 6th September 1922")

    scene apartment

    NAR "Another day, another incredibly groggy and tired feeling in my everything, except for the bruise on my arm of course."

    NAR "We were all going to go and meet up with Wilkinson at his store today, I started to get ready to go around our arranged time. After getting down the steps, I noticed her again. Cathee."

    show cathee

    CATHEE "Oh hello there, I’ve noticed you’ve been having some fun."

    JESSE "Not sure I’d call it fun, besides it’s not like we know if what we did actually matters much in the end."

    CATHEE "Oh come now, are you still not invested? You’re a hero whose tales of your honor and victory are at least brought up as an annoyance by those in power you know. Hahaha, I’ll be around, you know how to contact me."

    NAR "She began to skip away… the cat followed her for a bit… Wait a second no I don’t! I yelled out to her, and now noticed how tired even my jaw felt."

    JESSE "Wait! What do you mean by that, you always contact me"

    CATHEE "Exactly!"

    hide Cathee

    NAR "And she… vanished around a corner… Why is she like this, who even is she? Maybe the cat knows. But… she seems happy with what I’m doing, I guess I’m happy about it too… we do something impactful?"

    scene bookstore

    NAR "I met with everyone at Wilkinson’s store in the afternoon."

    show evelyn

    EVELYN "Hi Jesse! With Carter’s help, we found something important."

    NAR "She showed me the book in more detail."

    EVELYN "It appears to be about the language your book is written in."

    EVELYN "I was curious if maybe you could let me borrow the book to decode the meaning of the incantations."

    NAR "It feels wrong to just let go of the book… But I can trust Evelyn and if it’s actually going to be able to decode any actual information on the book, we should definitely take the chance."

    JESSE "Sure thing, just don’t try anything fancy with it."

    EVELYN "Okay good, because we need to discover if any of the other incantations are harmful and if that first spell was just harmful to you."
    hide evelyn
    show finn

    FINN "Yeah. It wouldn’t be great if you passed out every time you used that book."

    JESSE "I agree, but I did what I felt needed to be done to try to understand what is going on lately. Besides, I’m more than capable of it."
    hide finn
    show carter

    CARTER "Oh yeah, plenty of lesser people would have died just from casting that dispel magic. There’s a very important reason that none of those are crafted to be anywhere near as powerful."
    hide carter
    show finn

    FINN "I get he can do it, but you don’t want to kill yourself before you figure things out. Maybe understanding how these spells work will allow you to control them better and not have such a nasty effect on you when you use them."

    hide Finn

    NAR "The group agreed and I handed the book over to Evelyn, we talked a little, but I decided to let them get to work on it, it wasn’t too much text, but it seemed to be a lot of work. We said our goodbyes and I started to head home…"

    scene date_transition

    NAR "Until I noticed someone I wish I hadn’t."

    scene city

    show felix

    FELIX "What are you doing on the streets at this hour, Stout?"

    JESSE "I could ask the same of you, Roark."

    FELIX "hmph, Stout. Something is going on in this town. Something bad and ominous that I cannot quite put my thumb on. That room under the church looked like it had been occupied for quite a while…"

    JESSE "Took you long enough, that’s been obvious for a while now."

    FELIX "Well. I hate to say this, but I can’t do this alone. We aren’t on the best terms, but I think you’d be a great asset to me over the course of my investigation."

    JESSE "What, are you saying that we make a good team?"

    FELIX "Not in the slightest, having to drag you out of that was an incredible liability."

    JESSE "Yeah, and that nose of yours is going to get you killed."

    FELIX "But we can’t deny that we’re at least somewhat useful to each other aren’t we."

    JESSE "We would have been fine without you, the sigil in that church was obvious to me."

    FELIX "Because I led you to it. But I agree, I’ll find somebody more useful than you soon Stout."

    JESSE "Until then though."

    FELIX "Until then."

    NAR "He was just waiting for me here just for this conversation…"

    FELIX "Goodbye Stout."

    JESSE "Bye."

    hide felix

    NAR "We began to start leaving in the same direction."

    scene date_transition

    NAR "The rest of the day proceeded as usual."

    #CHAPTER 2 - END


    jump chapter3_start
