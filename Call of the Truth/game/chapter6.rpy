# Chapter 6 begins here

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define BUTLER = Character("Butler", color="#990066", what_color="#660066")

label chapter6_start:
    $ current_chapter = 6

    #CHAPTER 6: Descent
    scene room
    centered "{size=+30}CHAPTER 6: Descent{/size}"

    call new_day("???, ??? ???")
    NAR "The first time I was able to realize what was happening, was the sound of raindrops outside the window."

    NAR "I couldn’t tell where I was, but I know I’ve been here before… I can open my eyes, but they still feel very heavy. I was somewhat conscious now… but even then it seems like time is passing too far with every blink."

    NAR "I was in the hospital again, and who knows how long it’s been… Nurses and doctors would come in from time to time and check up on me…"
    call new_day("???, ??? ???")
    NAR "As the days progressed… I have been feeling ever so slightly better, but I still don’t fully comprehend how long it’s been, I don’t know if it’s something the doctors are doing, or if it’s something else that’s wrong…"

    NAR "Today Luke came to see me, I honestly don’t remember what we talked about, or why he came at all. I remember it was nice though, and I didn’t say too much at all I believe. The nurses told me he had visited me two times before too… which would mean…"
    call new_day("Thursday, 2nd February 1923")

    scene hospital

    NAR "Today I finally felt like myself again, to an extent of course. I still felt incredibly tired, but in the end I can actually comprehend everything that’s going on again, unlike the days before…"

    NAR "It’s today I learned that it was already february. The last thing I remember in detail was my birthday in december… Well, I did survive in the end… but…"

    NAR "I’ll think about that later, when I can talk to everybody. Apparently I hadn’t gotten too many visitors over the months."

    NAR "Sara had brought me in again, and besides her and Luke, Felix had visited once early on, but I did speak to him apparently?"

    NAR "Either way, I just need to go through their evaluations until they’re comfortable with me getting out of here, assuming it’s like last time I should be physically pretty fine once I recover from the lethargy. Except…"

    NAR "Majority of my right arm, from my wrist to my shoulder is all a pitch black bruise, that I can barely feel. That patch that spawned from my casting has spread exponentially."
    call new_day("9th February 1923")
    NAR "About a week after, the doctors were incredibly worried, but they were content with my physical state. Sara had come in to pick me up, and signed very similar paperwork compared to when this happened back in August."

    NAR "She seemed… really worried about me, and we started on our way back home. We were pretty quiet the whole journey back…"

    scene room

    NAR "We got back home, and she started to heat up some food, which is when it occurred to me how hungry I was… We ate in silence, and then…"

    show sara

    SARA "I… was hoping you’d want to talk about it"
    hide sara
    show jesse

    menu:
        "Oh…":
            hide jesse
            show sara
            SARA "Jesse?"

        "What do you mean?":
            hide jesse
            show sara
            SARA "..."

        "It’s fine.":
            hide jesse
            show sara
            SARA "Is it?"

    SARA "What do you mean… the first time I was incredibly worried, it’s not normal, the way the doctors explained it to me didn’t make any sense at all."

    SARA "And this time it was so much worse, I wasn’t sure if you’d even wake up this time. Even when you did, you weren’t okay for weeks."

    JESSE "I… don’t know what to say."

    SARA "Can you at least tell me what's happening? At least give me an excuse to explain you just passing out. You seem completely healthy outside of these two events… You can’t hide how tired you’ve been sometimes either."

    NAR "I can’t possibly make an excuse for this that doesn’t include magic."

    SARA "I thought you’ve been getting better… You’re friends are good people too, and it’s clear they care about you, but all of this? It’s related to them isn’t it… You can’t continue like this."

    JESSE "It’s not like that."

    SARA "Is it something here? What if you just leave, escape whatever is happening here? We could just leave."

    JESSE "what?"

    SARA "I know you don’t want to talk about it… but if it’s something that you can’t talk about, but something that is actively hurting you, and it’s happening because of people here… What if we just left. Cut ties from here?"

    JESSE "I don’t know what to think about that… but I don’t think we can do that."

    SARA "What’s stopping us?"

    JESSE "I’m sorry, I don’t feel comfortable talking about everything with you… But this isn’t something we could run away from, and even then, I do care about those people, I can’t abandon them."

    SARA "Okay… it’s okay, It’s fine Jesse. I wish you could trust me… can you just… promise me you’ll be okay?"
    hide sara
    show jesse

    menu:
        "I will.":
            hide jesse

        "I can’t do that.":
            hide jesse

        "...":
            hide jesse

    show sara

    SARA "..."

    SARA "Oh, also you don’t have to work tomorrow, but they did call, and want you to go back on Sunday, so just relax some more."

    hide sara

    NAR "SARA RANK 5/7"

    NAR "The rest of the day proceeded in silence…"
    call new_day("Friday, 10th February 1923")

    NAR "With my free time from not having to go to work, I was able to meet up with Luke again. Sara was still being somewhat distant from me…"

    scene cafe

    NAR "We met at that Cafe again, which I guess is a small positive considering we know it’s safe from the Cult, just in case of course. Even then I only say that because I trust Finn, at the very least it’s not directly connected to them I believe."

    NAR "Our talk started as it usually does, but it was clear something was… bugging him this time?"

    show luke

    LUKE "Jesse… are you doing all right? I was concerned the first time you were in the hospital, and then it was significantly worse this time."
    hide luke
    show jesse

    menu:
        "I’m fine.":
            hide jesse
            show luke
            LUKE "I understand but…"

        "Don’t worry about it.":
            hide jesse
            show luke
            LUKE "I understand how you feel but…"

        "I’m better now though.":
            hide jesse
            show luke
            LUKE "That’s good to hear but…"

    LUKE "I just want to make sure… well no actually… I care for your wellbeing of course, but if you are happy with how things are turning out, then perhaps this is best for you anyway…"

    LUKE "I don’t want you to answer me on this, but I want you to start thinking about it. I can’t begin to imagine what you’re doing of course, but if you’re okay with what's been going on, even if it’s putting yourself in danger…"

    LUKE "Do you still dislike why your father risked his life?"

    hide Luke

    NAR "I… I never hated him, but I wouldn’t just forgive him for risking his life when he still had me to protect…"

    NAR "But isn’t that what I’ve been doing? To an extent kind of, but no it’s like I’m actually putting myself in huge risk right… Well no I knew the risk back in december…"

    NAR "LUKE RANK 7/10"

    show luke

    LUKE "Also, I’m sorry, but I won’t be able to meet with you on the 25th this month, and if I recall correctly you have work on the coming 10th. However I do think this is something important to take your time and think on… good luck with everything Jesse"

    scene date_transition

    NAR "We didn’t talk too much after that, but we said our goodbyes and I went back home."

    NAR "Later, I also called Wilkinson and told him I wanted to get everybody together. After being slightly annoyed that I was asking him to do so much work, he agreed, and we’d meet up on monday once I’m free, and when Sara is working."

    call new_day("Saturday, 11th February 1923")
    call half_free_day
    #Walk
    #Study
    #Gardening

    call work_day("Sunday, 12th February 1923")
    call new_day("Monday, 13th February 1923")

    scene bookstore

    NAR "It’s been a couple of days since I’ve gotten out of the hospital, but I still feel incredibly tired compared to usually…"

    NAR "I’ve gotten used to using my arm though, even if it’s almost entirely numb, luckily my hand still works. The journey to the bookstore felt longer than usual…"

    NAR "As usual I was the last one to arrive."

    show finn

    FINN "Jesse! So good to see you up again."

    NAR "He was already up and eager, I can tell everyone was worried about me, except maybe Felix… or he was but in his own way."

    NAR "Before I could start talking more than greeting everybody, there was a knock on the door. Opening it up, was Linden."
    hide finn
    show linden

    LINDEN "Good evening everyone. I figured since it was the first conversation after your health improved, there’d be some important information I’d want to know."

    NAR "Before I could explain anything too much…"
    hide linden
    show carter

    CARTER "Oh gods no, get out of my shop right this instant."
    hide carter
    show linden

    LINDEN "Of course, if you’d like a reason to let me stay you can take these."

    NAR "He places an envelope on the counter and slides it to Wilkinson… who carefully opens it, and looks at some of the papers inside…"
    hide linden
    show carter

    CARTER "hmm… okay nevermind you get to stay. For now…"

    CARTER "If you all must know… you’re not allowed, but it’s some things me and my boys have been interested in for months hehe, Okay carry on."

    hide carter

    NAR "Felix and I explained who Linden was in detail to the others, and they came around to trusting him. Eventually, the floor was opened up once again, to the question all of them were worried about. What happened to me that day."

    JESSE "I… I had to give up the tome, it was the only way to save all of us. I used that rewind spell we had after we were attacked and stopped them… but now we don’t have the tome anymore"

    NAR "It was a mix of surprise and worry."

    show finn

    FINN "Jesse, that’s fine. If you couldn’t find any other way, that was the best move… It worked out in the end right?"

    JESSE "It did, but what can we even do without it? We know they would have wanted that back desperately, and now they have it…"
    hide finn
    show evelyn

    EVELYN "Even then, we still are in this right? Sure they might have that advantage, but think about all we’ve learned about things so far?"

    EVELYN "Apparently they’ve been angered enough to actively attack us right? What Carter and Linden can get us access to is enough power to get through things even without the book."
    hide evelyn
    show carter

    CARTER "You have been putting a lot of faith into what was essentially single use powerhouse spells, when you could just like, split that up in smaller spells… Also guns exist."
    hide carter
    show felix

    FELIX "Yes, but our enemy is fairly far above that. Our one out that we truly had against them was this tome."

    hide felix
    show linden

    LINDEN "This is true, and it took a lot of effort to get it out of our hands in the first place. Where we proceed from here will be very important."
    hide linden
    show felix

    FELIX "You’re directly from inside the organization aren’t you? Would you like to give us some insight on how to progress this from here?"
    hide felix
    show linden

    LINDEN "Sadly I cannot. I had not learned that we even had the book in our possession until now. However since late December we have been having a shift in our planning structure. I had hoped it was from something you all had succeeded in, rather than failed."
    hide linden
    show finn

    FINN "It wasn’t a failure, failure would have been all of us dying then. It’s a setback, but we can still get it back."
    hide finn
    show linden

    LINDEN "I’ll see what I can get happening in the cult to progress towards one, getting the information of our theft and plans to me naturally, and two an opportunity to acquire it for us. I can’t promise any of that will happen quickly."
    hide linden
    show evelyn

    EVELYN "In that case… we all need to work on actively trying to get information directly from the cult… it’s a bit scary though, that kind of investigation is what got your dad killed in the first place, and they’ve already made an attempt on our lives…"
    hide evelyn
    show carter

    CARTER "Then just take it slow. You’ve got the time right?"
    hide carter
    show felix

    FELIX "If only it was that simple… they’ve had the tome for what, nearly two months at this point? We may be up against their endgame."
    hide felix
    show finn

    FINN "There’s not much else to do though, it’s the best we have, and it’s not like they’re going to target us so directly now that they know we don’t have it right? It got stolen by Jesse’s dad before, I’m sure all of us can think of something."
    hide finn
    show evelyn

    EVELYN "Then it’s settled, we’ll all try to make progress into getting information on them, and what they’re plans are from here on out, once any of us gets some sort of lead, we can meet up and actually formulate a plan."
    hide evelyn
    show linden

    LINDEN "Worst case scenario, we wait until they actually require my expertise to make the final plans work, then we’ll get definitive answers on what to do."

    hide linden

    NAR "It seems like we actually have some idea of how to progress, even after losing it… I guess we didn’t really need it until the end anyway right?"

    NAR "And if the operation is just to try and steal it back, it was done before without the tome, it can be done again. Hopefully we’ll get some information soon though."

    NAR "We all said our goodbyes, and I headed home… I don’t think I want to tell them about my arm, it’ll only cause unnecessary worry, it’s not like I’ll be able to use that tome at all until we get it right? We can worry about that then."

    scene date_transition

    NAR "The rest of the day proceeded in silence…"

    call new_day("Tuesday, 14th February 1923")
    label free_day_2_14:
    call free_day("knowledge", "Finn", "Evelyn")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Finn"
            call finn_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Evelyn"
            call evelyn_hangout

    if(hangout_failed):
        jump free_day_2_14
    #Finn
    #Evelyn
    #Study
    call new_day("Wednesday, 15th February 1923")

    scene bookstore

    NAR "In what started as a normal day, quickly changed by the alert of news from Wilkinson, he mentioned he contacted everybody for some important news. I rushed down to his store when I got the chance."

    NAR "After greeting everyone and getting settled, everyone was here except Linden. Which Wilkinson mentioned he hadn’t called because he would already know about it, and additionally he doesn’t have a way to contact him, nor does he want one."

    show carter

    CARTER "So. Do you all remember Egypt?"
    hide carter
    show jesse

    menu:
        "Yes.":
            hide jesse
            show carter
            CARTER "Fantastic."

        "Why?":
            hide jesse
            show carter
            CARTER "Because it’s Egypt related!"

        "Again?":
            hide jesse
            show carter
            CARTER "So you’ve forgotten again?"

    CARTER "Like I said back when I first found out about it, I knew this would be relevant later, and none of you believed me."
    hide carter
    show felix

    FELIX "It didn’t matter if we believed you or not, you made a deal out of something that didn’t become relevant for what, four months?"
    hide felix
    show carter

    CARTER "Shut. Your superior is explaining things."

    NAR "Felix lets out a long sigh as Wilkinson continues his thoughts."

    CARTER "So, there’s finally been some bigger prospects down there, Uncovering ancient tombs, as you do of course."

    CARTER "Which honestly is what I was planning on doing in my free time once this all finished, but meh, there’s plenty of tombs in the sea as the saying goes."
    hide carter
    show evelyn

    EVELYN "I’m pretty sure it’s fish?"
    hide evelyn
    show carter

    CARTER "Yes but there are no fish in the desert, anyway."

    CARTER "It seems like they’ve entered and excavated an ancient tomb heavily related to a certain sphinx they tend to idolize, and it’s partly from the papers Linden gave me."

    CARTER "But that was all really just confirming what we thought was there. There’s powerful arcane tools that are important to something akin to summoning a creature."

    CARTER "I guess more specifically resurrecting in this case? I’m inclined to believe it’s resurrection."
    hide carter
    show finn

    FINN "how do you figure that?"
    hide finn
    show carter

    CARTER "Well, I mentioned we just want the simple things, immortality etcetera, so we were looking into the more resurrect-y type of alternatives, which included the ancient gods of egyptian mythos, among other locations."
    hide carter
    show felix

    FELIX "So you’re saying their end goal is going to be using the power of the tome to enact a great resurrection type of scenario?"
    hide felix
    show carter

    CARTER "That’s currently my guess, although that doesn’t particularly get us any closer to actually getting the tome back."
    hide carter
    show evelyn

    EVELYN "Even if we know their end goal, we still don’t know anything useful… I haven’t made much progress myself."
    hide evelyn
    show felix

    FELIX "That’s not true. Now any information we get can be pieced together under the assumption of this resurrection, which is important when what we’re trying to figure out tends to be so vague. Realistically we need more information on the inside."
    hide felix
    show evelyn

    EVELYN "Can’t we get more of that from Linden?"
    hide evelyn
    show carter

    CARTER "Nope."
    hide carter
    show felix

    FELIX "*sigh* No, but that’s just because we can’t just trust everything he says to us, not necessarily because he’s untrustworthy, but because if the cult is expecting anything about him."

    FELIX "They could be giving him information to fish for us in a sense. Especially since he apparently didn’t know about the book in the first place."

    hide felix

    NAR "The rest of the conversation wasn’t too important. I was almost wondering why I was even a part of this anymore, sure I did stuff without the tome that was important..."

    NAR "now I just feel like I can’t do anything too exceptional compared to the four of them, there’s got to be something I can bring to the table that no one else could…"

    hide bookstore

    NAR "The rest of the day proceeded in silence…"

    call work_day("Thursday, 16th February 1923")

    call work_day("Friday, 17th February 1923")

    call new_day("Saturday 18th February 1923")
    call half_free_day
    #Walk
    #Study
    #Gardening
    call new_day("Sunday, February 19th, 1923")
    NAR "It was a normal day at work, exhausting as ever, but a thought occurred to me. Sara has been acting so strange lately… Thinking back on it, she knew about what was going to happen that day in December… it’s always been in the back of my mind."

    NAR "That she’s been a part of the cult all along… Not everything makes sense with that though, I’ve always felt she’s been a great friend to me…"

    NAR "That could all be an act though. We need someone on our side, we need more people involved. I see it working out in three ways."

    NAR "One, she’s not a part of the cult, but she’s still in some sort of management position in the company we work for, which is clearly a front by the cult because of Linden’s involvement."

    NAR "Two, she’s part of the cult, and an enemy, and at this point, she has to already know, that was pretty evident from when she picked me up from the hospital…"

    NAR "Or three, she’s an ally and a part of the cult, which is exactly what we need right now."

    call new_day("Monday, 20th February 1923")

    scene room

    NAR "Today is my opportunity to talk to her, directly about all of this. If this doesn't work out, I can call Felix and he’ll be able to get me out of things probably…"

    NAR "which is why I can’t let things come to that, the last thing I want is for him to ‘save’ me."

    NAR "I waited for her to come home. When she got back, I told her I wanted to talk to her about something, but gave her time to get settled back home."

    show sara

    SARA "So what did you want to talk about?"

    NAR "How… do I even start this… I guess I should just be direct? I still don’t believe that she’s not my friend, but it could all be a facade that she’s been playing since the start… the start… even when we met years back in high school?"

    SARA "...Are you okay? Did I do something wrong?"

    JESSE "How long?"

    SARA "How long… for what?"

    JESSE "Don’t try to play it off anymore. I’ve known Linden for some time now, I know what your position is in that company now. What does that mean to you."

    SARA "..."

    JESSE "This entire time, you’ve just been watching me haven’t you? Spying on me to see if I’ve ever come close to uncovering the truth about what’s really been going on. That’s why you’ve been busier lately, because of my actions surrounding them."

    SARA "..."
    JESSE "Did you not realize? That’s been your purpose with me right? While you’ve been off planning how best to trap us. You were in on the attack they weren’t you?! How long have you been lying to me."

    SARA "It’s not… I knew it was you, I couldn’t ignore how you were when you suddenly became so tired… when your arm started to bruise…"

    SARA "Of course I knew you had the tome and were working against us… They were the ones that assigned me to have a reason to try and move in with you, they’ve been worried ever since your friend came back last year."

    SARA "And… of course I knew about the attack, they told me about it a few days before it was planned… but…"

    JESSE "So this entire time, you’ve just been working for them against me."

    SARA "No! No… I couldn’t… It wasn’t all lies Jesse, Everything about my parents, about how I got involved with this, that’s all true, I just omitted that part…"

    SARA "Yes, we met originally because they wanted to try and start having more ways to keep track of you and your dad… and they figured I would be a good choice to try and get close to you… But I’m not just their puppet."

    SARA "I do… see you as a close friend."

    JESSE "Then why were you willing to let them kill all of us."

    SARA "I wasn’t! I told you they only informed me about that a few days before it happened, and I was so confused when nothing happened…"

    SARA "But when you stepped out, I was so worried. I hate to say it like this, but why do you think you’ve been able to get by so freely all this time?"

    SARA "You staying quiet about everything really made it easier for me… but I tried to tell them enough to keep them satisfied, but I’d still try to spin it…"
    JESSE "What do you mean?"

    SARA "This started out all because of what they wanted, but I’m not just their puppet. I wanted… to protect you, It’s not simple to just be free of them…"

    SARA "That’s why my home life became so dangerous, because I was endangering my parents, and they hated me for staying with them, but if I didn’t…"

    SARA "I ran out of ways to hide from the fact that you were the spellcaster that was targeting us, but I was able to convince them to not do anything too rash against you…"

    SARA "Even the attack you’re talking about is a blessing compared to some of the ways they were thinking about dealing with everyone…"

    JESSE "Why didn’t you tell me?"

    SARA "I… was scared… scared that you wouldn’t trust me, or would try and make me leave… I can’t try and say that I haven’t betrayed you, I’m part of the reason that your dad died…"

    SARA "I could never atone for that, especially not with trying to be your friend in spite of all of that. And I’m scared, scared of what they would do if they realize I’ve betrayed them…"

    JESSE "...Are you serious about trying to help us."

    SARA "Yes… but I know you can barely trust me…"

    JESSE "So you know they have the book and the pen. We’ve essentially lost. They let us live since I gave up those items. Which means they don’t particularly care about us right? Are they going to have to stay spying on me?"

    SARA "Yes… they’re moderately concerned about you staying against them, but… another part of my job was to see if there was ever a chance you would join them, but that idea was scrapped the moment they fully realized it was you who was working against them."

    JESSE "that’s interesting… but the point is, we’ve lost, and this is the perfect opportunity for us to let it go, and give up. And you can make sure that’s the message they get."

    JESSE "We’ve known Linden has been shunned and removed from some discussion by certain groups within your cult. You can confirm and possibly double-check that information."

    SARA "What are you asking of me?"

    JESSE "We have next to no leads, and you’re close to winning this. We’re desperate, and you changing teams would be an incredible boon to us."

    JESSE "I do believe that you’re actually my friend, but I’m not going to be able to trust you again… until you prove it to me."

    JESSE "If our only chance of victory without a double-agent like you is slim, I’m willing to risk this."

    SARA "Honestly… part of me was hoping you would talk to me about this… Thank you for putting your trust in me…"

    SARA "I know I don’t deserve it, but from here on, I’ll put you first. I’ve witnessed firsthand what these people do… and I’m not free of that either, but if we can stop them, I want that. I feel I can put my faith in you for this."

    JESSE "Tomorrow when you get back. You’re going to tell this to everybody."

    SARA "I… understand. I won’t betray you anymore!"

    hide sara

    NAR "I’m not sure how much faith I can put into any of those words, or anything she’s said for the past few years I’ve known her, but desperate times call for desperate measures…"

    NAR "And I refuse to believe that everything we’ve shared together has been a lie. One way or another, I’ll learn soon enough."

    NAR "SARA RANK 6/7"

    hide room

    NAR "The rest of the day proceeded as usual."

    call new_day("Tuesday, 21st February 1923")

    scene bookstore

    NAR "I got in contact with everybody telling them I’ve got us a lead, and we need to meet up. They were a bit confused why I was calling it for so late in the day, but they went with it and we all got to Wilkinson’s. Me and Sara, arriving last."

    NAR "Immediately embraced with confusion all around, except from Linden and Felix."

    show sara

    SARA "Hi everyone… I know we met back then, but to properly introduce myself again. I’m Sara Harper, and… I’d like to apologize to everyone."

    SARA "I’ve been working for the guiding comet for a long time now, and part of my job was to spy on Jesse and his friends for a while now… and…"

    NAR "The mood in the room quickly soured, but it looked like they were going to give her a chance to explain herself."
    hide sara
    show carter

    CARTER "Oh come on now?! TWO of them! How-"

    JESSE "Carter."

    CARTER "...hmm."
    hide carter
    show sara

    SARA "And… I tried my best to keep Jesse safe, but until now I had always been worried about trying to do whatever I could to keep myself going first. I can’t try and make that an excuse."

    SARA "I’ve always had my worries and doubts about what I was doing, but I never made up my mind until now, and I’m sorry."
    hide sara
    show evelyn

    EVELYN "It’s okay… Thank you for telling us, what matters the most to us is stopping them, and if you can help us with that, that’d be a great help. What matters is what happens from now on, not who you were before."
    hide evelyn
    show linden

    LINDEN "The simplest thing this gives us the opportunity for is double checking what the two of us know, because since you’ve been co-operative they probably do trust you, at least enough to have you still important to watching Jesse."
    hide linden
    show sara

    SARA "I don’t know how much I can really do, but I’ll try and get whatever I can, Jesse was telling me that you’re all in a bit of a rough spot now after what happened in december though…"
    hide sara
    show felix

    FELIX "That’s a bit of an overstatement, he’s been feeling that way certainly. But either way, now that you’re actually able to get us some information on the inside, even the minor issues will soon work themselves out."

    hide felix
    show sara

    SARA "I’ll start trying to see what all the moving parts and assignments they’ll be changing now that they are moving towards a plan with the tome. I can’t promise much…"

    SARA "But I can confirm with you guys given the current pace of things it seems like they still have quite a bit of work to do. And it’d also be easier to get the fire off of everyone if you all keep quiet for a little bit anyway."

    hide sara
    show linden

    LINDEN "I can confirm most of what she’s saying."

    hide linden
    show finn

    FINN "Thanks for all that. It’s a start to making up for what you’ve done…"

    FINN "Hey actually, now that you’re in on it, we can finally meet up at reasonable hours! And we can do stuff on saturdays."

    hide finn
    show sara

    SARA "I’m not too sure of that, it’s been really easy to make excuses of where he’s been when he just stays around the house during the weekends…"

    hide sara
    show felix

    FELIX "Just say the two of you started going out or something."

    hide felix
    show sara

    SARA "Haha, that could work actually."

    JESSE "huh?"

    hide Sara

    NAR "Linden left soon after we were done talking about important news. We talked a bit more, and Sara began to open up to a few of them."

    hide bookstore

    NAR "It started to get late, so we  all said our goodbyes and left. Felix started to walk with us."

    scene city

    show felix

    FELIX "So, out of curiosity, who finally broke the ice?"

    JESSE "Interesting way to phrase it…"

    FELIX "My assumption would be Sara, after all it was pretty clear she was with them, but also not fully on board with them, I had my suspicions but your birthday bash decided that fully."
    hide felix
    show sara

    SARA "I’m not that obvious am I?"
    hide sara
    show felix

    FELIX "Not particularly, but I figured there had to be someone that was watching and keeping track of Jesse, and there really were only two options out of our group, and it seemed like you were more… secretive."

    JESSE "Wait who’s the other one?"

    FELIX "Oh, your mentor, I doubt he’s in on this at all though."

    FELIX "Anyway, goodbye you two."

    hide Felix

    NAR "We walked home together, finally knowing our true selves…"

    hide city

    NAR "The rest of the night proceeded as usual."

    call new_day("Wednesday, 22nd February 1923")
    label free_day_2_22:
    call free_day("charm", "Carter", "Linden")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Carter"
            call carter_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Linden"
            call linden_hangout

    if(hangout_failed):
        jump free_day_2_22
    #Carter
    #Linden
    #Gardening

    call work_day("Wednesday, 23rd February 1923")

    call work_day("Thursday, 24th February 1923")

    call new_day("Saturday, 25th February 1923")
    label free_day_2_25:
    call free_day("all", "Finn", "Linden")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Finn"
            call finn_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Linden"
            call linden_hangout

    if(hangout_failed):
        jump free_day_2_25
    #Finn
    #Linden
    #Self Improvement

    call work_day("Sunday, 26th February 1923")

    call new_day("Monday, 27th February 1923")

    scene cafe

    NAR "I got a call in the afternoon, requesting to meet with Linden at the cafe, he also asked that I bring Sara. I waited, and eventually told her and we set off."

    NAR "It was strange to meet with these two at this place, when the only other time was with Finn and Evelyn… two members of the cult…"

    JESSE "Hello, was curious why you picked this place?"

    show linden

    LINDEN "It’s nearby, and not in direct connection to our work so it’s ideally a safe place."

    JESSE "heh, we used to use this place to talk too before we met with Wilkinson."

    LINDEN "Well, it was a good pick then, but I digress, the reason I wanted to talk to you two is about some items that we will be receiving soon."
    hide linden
    show sara

    SARA "Are you talking about the things from the dig coming to them?"
    hide sara
    show linden

    LINDEN "precisely, and partly why I wanted you here was to see if you could confirm or cross-reference what I know with what you’ve learned."


    JESSE "I’ve actually already heard about this too… from Carter."

    LINDEN "Hm, well the reason why I bring it up now is because there’s been some advancement with that."

    LINDEN "The basics of things is that once we get the artifact from Egypt in our hands then we’ll be able to proceed with a much grander spell than normal."

    LINDEN "The goal as well is to use the tome to complete that to empower it beyond comprehension, but it’s not exactly required."
    hide linden
    show sara

    SARA "This would explain a lot for me actually… They’ve been working towards moving and removing a lot of people to more specific jobs."
    SARA "They’ve transferred a lot of the more magical focused acolytes to locations here in london, while moving assassins and the like back to Ireland and Scotland."
    hide sara
    show linden

    LINDEN "Either way these preparations will still take some time. The attitude of the public is an important part of our plans since our conception."

    LINDEN "The idea that minds need to be in a malleable state to progress things is deathly important to the overall goals. Which will come to a head with our endgame with the Egyptian Artifact and the Black Tome."
    hide linden
    show sara

    SARA "So they haven’t told you any specifics about it either?"

    hide sara
    show linden

    LINDEN "It’s certainly on a need to know basis, which is relegated to only the upper echelon of our members."

    JESSE "Do you at least have any idea of the timeframe we’re running on here?"

    LINDEN "I’m afraid not, we cannot start without the artifact in our hands, that much I know. From then, it would take approximately a month to complete preparations, so at minimum we have until near the beginning of April."

    hide linden
    show sara

    SARA "I’ll definitely be able to figure out when big moves are about to happen, but we’ll still need to wait on that."

    JESSE "Hmm, well thanks for letting us know. If it’s more relevant I’ll inform everybody else when I get the chance. Part of me feels like we’re not doing enough."
    hide sara
    show linden

    LINDEN "Things of this scale take time Jesse, enjoy your freedom while it lasts."

    hide Linden

    NAR "Linden left us soon after, and we ordered some food before heading home."

    hide cafe

    NAR "The rest of the day proceeded as usual."

    call new_day("Tuesday, 28th February 1923")

    scene room

    NAR "Whatever plans I had today were thwarted by the knock on the door. Finn and Evelyn had come over. It was still early so Sara was at work."

    show evelyn

    EVELYN "Hi, we figured we could give you a quick update on what we’ve found, plus I have something to give you. We were working with Wilkinson to try and find out more about this artifact that they’ve been wanting to get their hands on."
    hide evelyn
    show finn

    FINN "tracked it to some black market dealing actually, which we started to assume were related to the cult in some way. They’re going to be in the city in early March."
    hide finn
    show evelyn

    EVELYN "From there we were thinking about some way we could use that to potentially infiltrate what they’re doing right?"

    JESSE "It’s not a bad idea… It’s actually relevant to some other information we’ve found out."
    hide evelyn
    show finn

    FINN "Why don’t we meet up tomorrow and see if we can actually get any serious plan out of this?"

    hide Finn

    NAR "We ended up making arrangements to get together with the other four, but Linden wouldn’t be able to make it."

    hide room

    NAR "The rest of the day proceeded as usual."
    call new_day("Wednesday, 1st March 1923")

    scene bookstore

    NAR "We all met up at the bookstore once again, and in the afternoon at that. After getting settled, I told them about what Linden had told us the other day."

    show evelyn

    EVELYN "So... our minimum deadline on this is April… I don’t think we can keep our current pace if that’s when their plans will finish…"
    hide evelyn
    show sara

    SARA "Yeah… on that line of thinking actually, after spending this time looking into trying to find what and where the tome is, I can safely say I won’t be able to make any progress on that sadly."

    JESSE "So we don’t have any ways to move forward without trying to get this artifact from  them?"
    hide sara
    show finn

    FINN "Even then, I don’t think that’s necessarily safe, the moment we take something else from them, there’s no reason they don’t attack us again."
    hide finn
    show sara

    SARA "I do actually have an idea… The original idea they had was actually to try and recruit you into it… but they gave up on that since they realized you were the one causing them problems."

    SARA "It’s possible they might still be interested in that?"
    hide sara
    show evelyn

    EVELYN "Then from there, they might be able to talk to you about the tome, since you have used it!"

    JESSE "That seems… like a strange plan."
    hide evelyn
    show sara

    SARA "But I bet it could work, we could try and see if Linden knows anyway to get you in. After all, what we really need is information on the inside, right?"
    hide sara
    show finn

    FINN "It’s not like you investigating outside of it is going to be safe either… It will probably take some time to actually get you into it too?"

    JESSE "Are we serious about this?"

    FINN "Only if you’re up for it… but it would probably make sense to wait on it until after they’ve gotten the artifact, so it doesn’t look too obvious."
    hide finn
    show sara

    SARA "Let’s wait on things, then we’ll get in contact with Linden and see what we can do."
    hide sara
    show carter

    CARTER "You guys. Are just messing with me at this point. When did it become okay to have not just one, not just TWO, BUT THREE full fledged members of the guiding comet in MY establishment… I do too much for you all"
    hide carter
    show finn

    FINN "Oh come on, they’re all traitors isn’t that a good thing?"
    hide finn
    show carter

    CARTER "It’s just so hard to explain to the regulars you know? But don’t get me wrong, I’m still on board with helping however I can. Good luck joining a cult, want any tips?"

    JESSE "I think I’m good, but thanks."

    hide Carter

    NAR "If you can’t beat em, join em, to beat them."

    hide bookstore

    NAR "The rest of the day proceeded as usual."

    call work_day("Thursday, 2nd March 1923")

    call work_day("Friday, 3rd March 1923")

    call new_day("Saturday, 4th March 1923")
    label free_day_3_4:
    call free_day("all", "Felix", "Finn")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Felix"
            call felix_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Finn"
            call finn_hangout

    if(hangout_failed):
        jump free_day_3_4
    #Felix
    #Finn
    #Self Improvement

    call work_day("Sunday, 5th March 1923")

    call new_day("Monday, 6th March 1923")

    NAR "The next week, we got confirmation from Evelyn that the black market trade for the artifact did occur over the weekend, which could be backed up by some of Sara’s work that day too."

    scene cafe

    NAR "In the afternoon we got in contact with Linden, and the two of us met with him at the Cafe like last time."

    show sara

    SARA "So… well first of all we figure that we have until at best April 5th to actually retrieve the tome back from them. We both know the two of us can’t just progress too well in efforts directly towards it without overstepping our boundaries."
    hide sara
    show linden

    LINDEN "This is true, that time limit may be outside of our reach, I can start trying to take more risks if that is what it will take us."

    JESSE "Well, that’s why we were thinking they might be interested in someone who had already used it, and just had to go through a fairly impactful decision and minor coma."

    LINDEN "...You expect to be able to join, and be able to get to it?"
    hide linden
    show sara

    SARA "It’s a bit of a longshot… but it could at least get us some insight into more things going on, and they’ve always been interested in recruiting Jesse in the first place."
    hide sara
    show linden

    LINDEN "Hmm… it is possible they would work with you actually, the fact that you’ve survived casting with that tome for so long, it’d be of great interest to them."

    LINDEN "I’m not sure where that would get us, but you do realize what you’re trying to sign up for right?"

    JESSE "If the plan is to resurrect their god and destroy so much, then I’d prefer if there was something I could actually do about that."

    LINDEN "It still won’t exactly be easy, I can try and find a way for them to get in contact with you… but they would need something from you to prove that you’ve actually had a change of heart."
    hide linden
    show carter

    CARTER "And that is a sacrifice I am willing to make."
    hide carter
    show sara

    SARA "Wilkinson?!"
    hide sara
    show carter

    CARTER "Yes hello, I called earlier but no one picked up, so I decided to come over. They’re going to want you to prove you’ve betrayed whoever you’ve been working with."

    CARTER "Hopefully they don’t actually know who exactly everyone is, but they’d certainly have my organization, and probably the detective as key persons that have worked against them with you."

    CARTER "They wouldn’t directly attack me, but… they’d love to be able to do some irreparable damage or my people."

    JESSE "I thought you hated this idea?"

    CARTER "Oh I do, but this is currently my best way to deal with it in the long run. It’s worth the trade. I’m basically just sacrificing some contacts, and some of my better underground routes around the city."
    hide carter
    show linden

    LINDEN "Hmm, that makes things easier, but It still may take me about a week to get anything to you all. With the artifact coming into our possession and everything else going on… I’ll do what I can."

    hide Linden

    NAR "This entire plan seems too far fetched… but it’s something I can work on while the other three actually make some decent headway elsewhere."

    scene date_transition

    NAR "The rest of the day proceeded as usual."

    call new_day("Tuesday, 7th March 1923")
    label free_day_3_7:
    call free_day("knowledge", "Linden", "Evelyn")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Linden"
            call linden_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Evelyn"
            call evelyn_hangout

    if(hangout_failed):
        jump free_day_3_7
    #Linden
    #Evelyn
    #Study

    call free_day("Wednesday, 8th March 1923")
    label free_day_3_8:
    call free_day("charm", "Evelyn", "Carter")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Evelyn"
            call evelyn_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Carter"
            call carter_hangout

    if(hangout_failed):
        jump free_day_3_8
    #Evelyn
    #Carter
    #Gardening

    call work_day("Thursday, 9th March 1923")

    call work_day("Friday, 10th March 1923")

    call new_day("Saturday, 11th March 1923")
    label free_day_3_11:
    call free_day("all", "Finn", "Evelyn")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Finn"
            call finn_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Evelyn"
            call evelyn_hangout

    if(hangout_failed):
        jump free_day_3_11
    #Finn
    #Evelyn
    #Self Improvement

    call work_day("Sunday, 12th March 1923")

    call new_day("Monday, 13th March 1923")
    NAR "At work the previous day, Linden had told me how to get in contact with someone that would question me and try to recruit me, apparently it wasn’t going to be anyone too big, but he had informed someone he could trick into helping us better than most."

    NAR "I told Wilkinson about us trying to enact this plan today, and asked him to get the message separately to everybody."

    NAR "Assuming this works out, I’d try to not visit them for any anti-cult related activities, but meeting with them one on one wouldn’t pose too big of an issue."

    scene city

    NAR "I was told to go to a phone booth and call a directory related to my work in the evening. I got there, and the phone rang, but didn’t get anywhere."

    NAR "I waited for a few minutes, but nothing seemed to be happening… I got a bit anxious and left the phone booth, when I saw a car driving up."

    NAR "A fancy black and silver car drives up, and parks next to me in the phone booth."

    NAR "I could see the silhouette of an imposing man behind the window of the car, but then a man got out of the driver's seat. He seemed almost like a butler."

    NAR "Whoever this was, they weren’t just powerful within the organization it seemed. The butler began to speak."

    BUTLER "These are my master’s words, but he does not wish to speak to you directly. While we are enticed to hear that you wish to join us, no doubt because you had finally learned of Harper’s true intentions…"

    BUTLER "To let you truly join us we would request that you give us something that would prove your betrayal from your previous associates."

    NAR "I pulled out the resources that Wilkinson gave me, of course I had re-transcribed and made it look like he hadn’t just given them to me freely, he had warned me about that later."

    BUTLER "hm, it would seem you are smart enough to have thought of that. Your mind is truly made it would seem."

    BUTLER "We’ve been very interested in you for quite some time now, but we will disclose more of that information once you’ve proven you’re up for some of the tasks we have for you."

    BUTLER "You will be able to show this to your division’s lead and he’ll start you on some more important tasks we’ll plan for you."

    BUTLER "Your schedule will remain the same, but expect to be doing much more than what could have been boiled down to simple busywork, we’ll find a replacement for your original position quickly."

    NAR "I nodded in agreement, but did not say much. The window of the car was rolled down a little, and the man motioned to the butler, but I couldn’t get a good look at him."

    NAR "He leaned over and was being informed of something… the windows rolled up, as he turned back to me."

    BUTLER "He also wishes to inform you of something important. We saw no real way to tell you this while you would be antagonistic towards us, but now that your mind is more open."

    BUTLER "We did not kill your father. He had committed suicide and attempted to frame us to try and dissuade you from ever considering us an ally."

    BUTLER "We’ll be expecting great things from you Stout."

    NAR "What… No, that’s a lie right? They want to just try and manipulate me into thinking this is actually a good decision…"


    NAR "Whatever, it doesn’t matter, it’s just to mess with me, my dad spent far too long, and risked too much to try and stop them…"

    NAR "The butler left, and they began to drive off. That wasn’t just some random random recruiter that Linden had tried to get…"

    NAR "that man seemed far too important, the car, the butler, the information on my dad? One way or another… It seems like I’m in this now, just going to have to see where work takes me now… "

    NAR "I called and informed Linden and Carter that it was successful, and asked Linden more about who was supposed to meet with me, but he wasn’t exactly sure who it would have been either."
    NAR "The scene I described to him didn’t give me any information, but he did say he’s never heard of something like that happening with someone. They’re treating me as an exception, I need to be careful."

    scene date_transition

    NAR "I’d have to wait until Thursday to get any progress."

    NAR "The rest of the day proceeded as usual."

    call new_day("Tuesday, March 14th 1923")
    label free_day_3_14:
    call free_day("knowledge", "Felix", "Finn")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Felix"
            call felix_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Finn"
            call finn_hangout

    if(hangout_failed):
        jump free_day_3_14
    #Felix
    #Finn
    #Study
    call new_day("Wednesday, March 15th 1923")
    label free_day_3_15:
    call free_day("charm", "Felix", "Linden")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Felix"
            call felix_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Linden"
            call linden_hangout

    if(hangout_failed):
        jump free_day_3_15
    #Felix
    #Linden
    #Gardening
    call new_day("Thursday, 16th March 1923")
    NAR "Today not much happened… I showed my lead and they started to do more work, but told me to just continue as usual for the day… Apparently something was going to happen tomorrow though."
    call new_day("Friday, 17th March 1923")

    scene cultish

    NAR "The next day was completely different from usual. They had taken me down under the workplace and had informed me they were going to test my magical capabilities."

    NAR "They handed me a basic spellbook, similar to the ones Wilkinson had shown me, and had me cast some spells. It felt incredibly strange to do so many, but they didn’t tire me out in the slightest."

    NAR "Well they did but it wasn’t anything I wasn’t already used to. While my arm did feel strange with every cast, it wasn’t growing at all compared to when I used my tome."

    NAR "They were doing this to see my aptitude in this department, no doubt because they already knew what I was capable with, but to see if I was actually talented at the basics."

    NAR "They seemed… pleased with my results? I was told that they would have me already start on more important work with them on sunday."

    hide cultish

    NAR "I told Sara of everything that happened, and she would tell the others."

    call new_day("Saturday, 18th March 1923")
    label free_day_3_18:
    call free_day("all", "Evelyn", "Linden")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Evelyn"
            call evelyn_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Linden"
            call linden_hangout

    if(hangout_failed):
        jump free_day_3_18
    #Evelyn
    #Linden
    #Self Improvement
    call new_day("Sunday, 19th March 1923")
    NAR "Today was fairly fast for me… but it wasn’t the most comfortable thing I had to agree to. They began to study my right arm, and even took a small sample to look into…"

    NAR "They did actually inform me that they rarely have seen anyone survive to this extent of using the tome."

    NAR "They had it for a few decades before it was stolen, and they’d end up sacrificing some to cast a single spell or two from it, but they had stopped using it as frequently around ten years ago…"

    call new_day("Monday, 20th March 1923")
    label free_day_3_20:
    call free_day("courage", "Finn", "Carter")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Finn"
            call finn_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Carter"
            call carter_hangout

    if(hangout_failed):
        jump free_day_3_20
    #Finn
    #Carter
    #Walk

    call new_day("Tuesday, 21st March 1923")
    label free_day_3_21:
    call free_day("knowledge", "Carter", "Felix")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Carter"
            call carter_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Felix"
            call felix_hangout

    if(hangout_failed):
        jump free_day_3_21
    #Carter
    #Felix
    #Study

    call new_day("Wednesday, 22nd March 1923")
    label free_day_3_22:
    call free_day("charm", "Linden", "Evelyn")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Linden"
            call linden_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Evelyn"
            call evelyn_hangout

    if(hangout_failed):
        jump free_day_3_22
    #Linden
    #Evelyn
    #Gardening
    call new_day("Thursday, 23rd March 1923")

    scene cultish

    NAR "Today was another day of somewhat meaningless tasks… but it seemed like they were continuing to just judge my aptitude and commitment to them, which I tried to seem genuine for."

    NAR "Near the end of the day they told me about a new plan they had for me to help them. They had informed me that the pen used to write in the tome couldn’t actually be used by everyone."

    NAR "They mentioned my assistance with writing with it would be incredibly helpful. My first thought was I didn’t want to directly help them advance their plans too fast."

    NAR "My second thought was that they’re actually going to let me see the tome itself?! Before I could wonder too much about how they would have even progressed if I hadn’t joined them…"

    NAR "They told me there were other ways around using that pen to inscribe spells into the tome. Human blood and sacrifices… that blood could be fused and manipulated to be able to ink the pages."

    hide cultish
    call new_day("Friday, 24th March 1923")

    scene Cultish

    NAR "Today they had me transcribing dozens of spells into the book. I had tried to get them some way for me to practice, and had to show them the state of the pen, and how it being broken would affect the process."

    NAR "They agreed when they realized the importance of the number of spells they had me doing and the number of pages left in the book."

    NAR "I had kept track of every spell I transcribed to tell everyone else in the group, if these are ones they potentially plan to use…"

    NAR "It’s something we want to be wary of I figured, although it seemed like a great number of them weren’t too important."

    hide cultish
    call new_day("Saturday, 25th March 1923")
    NAR "As a break from all of my now completely cultish work, and the task of memorizing and relaying all that information to my friends."

    scene museum

    NAR "I have another opportunity to meet with Luke, after he could make it last time. I met up with Luke at the Museum again."

    NAR "We chatted for a bit, but it was clear something was on both our minds… I broke the silence."

    JESSE "About what we talked about last time… I haven’t really had the chance to think about it because of everything that’s been going on. We’ve all been kind of stuck, but we’re figuring out things as we go."

    show luke

    LUKE "It’s not something you need to do immediately, but it’s something that you would benefit from, part of getting past everything and moving on. However if there are more pressing matters at hand, you can’t divide yourself too much."

    LUKE "I understand you’ve been going through a lot lately, your life has been changing quite a bit ever since we started meeting up again back in July, and you’ve grown quite a lot since then too."

    LUKE "I feel like you’ve also gotten better at making decisions for yourself, rather than being as indecisive about what you wanted to be doing."

    LUKE "I’d say… if you're still in a rough patch with your friends, don’t miss out on an opportunity to fix things."

    LUKE "Even if you’re not entirely sure that it will be successful in helping things, you never know if you’re going to get any better opportunities."

    LUKE "Should take the initiative, and do what you can to help things, rather than waiting for what others expect of you all of the time."

    NAR "I know it’s been a long series of events with everything happening around me… but, I do think after learning what my dad was trying to do…"

    NAR "I can’t be mad at him… He went out and did what he could to stop them, and ran into probably similar hardships to myself, he had to steal the tome back too right?"

    NAR "Luke is right though, I can’t just keep working for them and waiting… I think we already have enough information to start forming some kind of plan… Tomorrow is the last honest day I’ll work. I swear it."

    NAR "LUKE RANK 8/10"

    hide museum

    NAR "The rest of the evening proceeded as usual."
    call new_day("Sunday, 26th March 1923")

    scene cultish

    NAR "After meeting with Luke, I knew I had to do something soon, it was already almost April. They had watched over my transcribing procedure for a while, but complications arose, that I was able to overhear outside."

    NAR "They had taken the people watching me off to go complete other tasks, they apparently had other times to prepare… even if the spells were completed and ready, they still had to find a location and a time to set everything up…"

    NAR "They couldn’t trust many others with being involved with my tome and its power, so they had left me alone in this room filled with potential spells I could find and cast…"

    NAR "There’s got to be something about this resurrection thing right?"

    NAR "I checked out everything when I felt I had the spare time after quickly completing some work, I should be able to finish all they need from me the next day I work…"

    NAR "I find a lockbox, but quickly discover it’s not physically locked. I tried to use a unlock spell from the basic spellbook they had given me, but it didn’t work… something about it not working depending on the strength of the magic…"

    NAR "I copied that spell into the black tome, and casted it once again through that. It was a weaker spell, it shouldn’t cause me much trouble at all, I’ve felt what it was like without the tome."

    NAR "I was very wrong… it immediately hit me just how much more it takes to use this rather than anything ‘normal’ but… it unlocked the box."

    NAR "Inside was a much older looking spell, and much more complicated looking one at that… I copied it down onto a normal piece of paper, to hopefully show to everyone soon."

    NAR "It was locked away, and honestly… it has some similarities to that dispel magic I used a while ago, but with much more…"

    NAR "This combined with me knowing where the tome was, and their trust in me to leave me alone with it? I think that’s all the pieces we would need to try and take it back from them."

    NAR "I took a breath… then tried to copy the dozens of complex lines into the tome in a single go… and…"

    NAR "It looks like it should work? At least from what I can tell about it…"

    NAR "I don’t think I’ll get a chance to see it one for one any time besides now, and it should be easy enough to hide next time I do anything on thursday, besides it was locked up, I doubt anyone has actually seen it."

    NAR "Hmm… but how do I re-lock it? If I had to dispel it with the tome, I doubt I could lock it with the basic book…"

    NAR "It wasn’t that bad using it… but I could already tell that the curse on my arm spread a smidge over my wrist…"

    NAR "I took the risk and locked it with the basic spellbook, I don’t think I could get away with being tired from using another spell like that, without being caught in some regard…"

    hide cultish

    NAR "When I got home I contacted everybody and told them about the spells I transcribed and also that I think we can actually formulate a plan at this point."
    call new_day("Monday, 27th March 1923")
    NAR "The whole group met together at Wilkinson’s store. We hadn’t met up like this for quite some time, but now we finally had some ideas on how to go about stealing back the tome from them."

    scene bookstore

    NAR "We met up in the evening and me and Sara arrived last as usual. I told them a bit of what I was thinking yesterday."

    show felix

    FELIX "So, all the information that we have has pointed to them starting their endgame and beginning this plan to resurrect their god around the first week of April."

    FELIX "However, I think we’re forgetting some key details with that."
    hide felix
    show sara

    SARA "Even with Jesse’s work scribing and speeding up the tome’s completion you would think that they could have sped things up outside of that but it still seems like things are going slowly."

    SARA "Especially not if they’re going to go through with things in only a week or two."
    hide sara
    show evelyn

    EVELYN "If everything they’ve been doing up until now has been with this end goal in place, they must have been wanting to divide the people of the country or just the idea that this kind of political change was necessary."
    hide evelyn
    show felix

    FELIX "Let’s assume that we do have more time for this, they’re going to need bigger events in the future. We can think about that after we succeed in getting the tome back, we don’t have much hope of combating them outside of using that tome."
    hide felix
    show carter

    CARTER "And that spell you found seems like it was locked away, because it has the ability to counter what they're doing here, and if we were able to cast it with that power, it could have an after effect that would affect everyone attuned to the cult’s magic at the time. Again, we need the tome for that first."
    hide carter
    show linden

    LINDEN "Then we need a plan to retake the book, shall we begin?"

    hide Linden

    NAR "It took us quite a bit, but we thought we had figured out an actually possible strategy to get it out of there from the information and accessibility I had, to Sara’s knowledge of the workers, and the extra information Felix and Finn got on the extraneous and underground workers for the cult."

    NAR "It would be happening Thursday, at night."

    NAR "First I would use my new relative freedom inside to plant ways for us to bypass any locks that would be present when we return in the night."

    NAR "Evelyn also asked to tell her about all the other specifics of what I would do to the tome, such as the other spells I’d transcribe that day before we stole it back."

    NAR "Similarly Linden would allow us to get access to the lower levels from a separate entrance."

    NAR "Once all of that is set up, we come back at night and infiltrate the place using the things we already set up inside, avoiding everyone."

    NAR "The other idea is me being more of a decoy… Linden and Sara gave me a good idea of the upper floors, which I would be using to escape. I would take the book and drop out a window down to Evelyn, and then…"

    NAR "Sara would find a path up from a stairway that I would meet her at, and he would set a rope I could get down quickly from."

    NAR "Finn and Felix would use disguises they’ve procured from Linden and the other avenues they were looking into, mainly just to cause a distraction. It’s Finn though, so I’m sure they’ll be fine especially with Felix’s strategies."

    NAR "Afterwards we meet with Evelyn and grab the book, all meet up in one location then split up and try to spend the night quietly. The next morning we’d meet back at the bookstore."

    NAR "When we were essentially done with the planning process most of us left, but Evelyn, Finn, and Felix stayed for a bit at the bookstore, probably clarifying their part in this. Thursday is when we’re going to do this…"

    scene date_transition

    NAR "The rest of the night proceeded as usual."

    call new_day("Tuesday, 28th March 1923")
    label free_day_3_28:
    call free_day("knowledge", "Linden", "Finn")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Linden"
            call linden_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Finn"
            call finn_hangout

    if(hangout_failed):
        jump free_day_3_28
    #Linden
    #Finn
    #Study

    call new_day("Wednesday, 29th March 1923")
    label free_day_3_29:
    call free_day("charm", "Linden", "Felix")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Linden"
            call linden_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Felix"
            call felix_hangout

    if(hangout_failed):
        jump free_day_3_29
    #Linden
    #Felix
    #Gardening
    call new_day("Thursday, 30th March 1923")
    NAR "The workday went how I expected, they gave me a certain amount of freedom that I needed, I went and set ways to unlock a path from the entrance to the room they keep the tome over the night."

    scene city_night

    NAR "I got back home and just had to wait until the night… We got a call that Sara picked up. She mentioned it was just something about work, that I didn’t need to worry about, everything was still going to work out as planned."
    NAR "Everyone got into their positions, and while it was a bit interesting, it did seem like most of our route was actually fairly silent… It felt easy, almost too easy."

    scene cultish

    NAR "I was able to get down to where they kept the tome fairly easily, and pick it up once again. Now to leave with it. There was activity in the building, we knew they wouldn’t just be empty waiting for us to take it…"

    NAR "Part of the plan for them to notice me though, they’re going to attack us regardless once they know that the tome is stolen from them, so that’s part of the idea of trying to split up immediately afterwards."

    NAR "But… realistically, if I could do this without getting caught at all… then we could actually just be stealthy and quietly stay hidden from them in the slightest."

    NAR "I thought to myself, as I exited the room with the tome."

    NAR "Directly in sight of someone."

    NAR "Less thinking, more stealthing, or in this case, running."

    NAR "Two people had seen me, and immediately started being aggressive, one of them began to cast that similar form of flame magic that I had seen before but his partner seemed a bit slower on the draw."

    NAR "I definitely felt too slow to dodge around the corner to avoid anything they were doing, but their attack did miss me entirely."

    NAR "Part of the plan was to completely avoid the main entrance we came from, because that’d be the only real exit for me, and now that they knew about it, they’d put people there."

    NAR "While presumably leaving the already empty upper floors safer. A big part of this was me taking quicker and smaller pathways up… and while the stairs were incredibly tiring, especially since I still hadn’t fully recovered in general."

    NAR "It wasn’t that impactful of an issue. When I had gotten away to the fourth floor, I found the side of the building overlooking the street, where I dropped the book out the window. It was sturdy, apparently can’t even be torn, it’s sure to survive a drop without much damage."

    NAR "Could tell that whatever distraction Finn and Felix were doing was working, and took the opportunity to move towards the stairway that Sara was supposed to meet me at, Which took a fair amount of time after I dropped the tome."

    NAR "She met up with me, and we escaped down out of the building entirely. From there took our time to get to our meeting place outside, to make sure none of us were seen or followed out of the building…"

    hide cultish
    call new_day("Friday, March 31st, 1923")

    scene city_night

    NAR "We were able to meet up at around an area that was still populated for the time. A random bar that had already been confirmed to not be directly related to anything occult at the moment…"

    NAR "Evelyn handed me back the tome, which looked no worse for wear. Then she told me she made sure that the cult seemingly saw that I didn’t have it."

    NAR "They may know that we’re all against them, but we can use that to spread them thin if they don’t know too much. Of course they’re going to be interested in me to begin with…"

    NAR "Which is why everyone was adamant that I still keep the tome, for protection, and it’s not like anyone else to use it in any way."

    NAR "We all split up from there, me and Sara were going to stay at a hotel for the night, because the first place they’d check would be my home if they wanted to try and get it back…"

    NAR "Realistically as long as we have it the cult isn’t going to let us go back to normal lives."

    NAR "It seemed safe enough when we got there, and then got a room, Sara got us food and we ate, it was late but we had done a lot and certainly weren’t tired enough to sleep… well I was always tired, but that’s only physically."

    NAR "There was something about all this, it worked out really well. Sure it seemed like we actually had the upper hand but…"

    NAR "If somethings wrong with all this I still need to just focus on what we have, I have the tome again, and if I can keep that than no matter what we have the upper hand don’t we?"

    NAR "All of the sudden though… I felt far too tired…"

    NAR "Was everything finally hitting me? No… no that’d be impossible it would have… I realized I could move my body very much at all…"

    NAR "Things started to get hazy… The last thing I saw before passing out was Sara opening the door to… acolytes of the cult…"

    NAR "why?..."

    #CHAPTER 6 - END

    jump chapter7_start
