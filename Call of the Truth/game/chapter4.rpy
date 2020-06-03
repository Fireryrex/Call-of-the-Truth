# Chapter 4 begins here

# Declare characters used by this game. The color argument colorizes the
# name of the character.

label chapter4_start:
    $ current_chapter = 4

    #CHAPTER 4: Put to Rest
    scene room
    centered "{size=+30}CHAPTER 4: Put to Rest{/size}"

    call work_day("Thursday, 16th November 1922")


    call work_day("Friday, 17th November 1922")

    call new_day("Saturday, 18th November 1922")
    call half_free_day
    #Walk
    #Study
    #Gardening

    call work_day("Sunday, 19th November 1922")

    call new_day("Monday, November 20th, 1922")

    scene room

    NAR "My peaceful slumber was interrupted by the sharp ringing of the phone, Wonder who that could be at this ungodly hour of...noon? Must have been more exhausted than I thought."

    NAR "I reach for the phone and place it up to my ear, only to be ‘delighted’ with the voice of Linden coming through on the other line. I answer with a heavy sigh"

    show jesse

    menu:
        "What is it now?":
            hide Jesse
            LINDEN "Well hello to you too."

        "Linden Hello! Just who I wanted to hear from today right now!":
            hide Jesse
            LINDEN "While I appreciate the enthusiasm, the sarcasm is unnecessary."

        "{i}Hangs up immediately{/i}":
            hide Jesse
            NAR "The phone rings again and you are compelled to pick up."
            LINDEN "Nice try Jesse."


    LINDEN "Now, I’ve called you here today for a bit of an update. A bit of good news actually, if you could call it that. Your previous actions caused a bit of a stir, my boy. Suspicions are raised, but luckily, not too high."

    LINDEN "I believe if you lay low for a while and avoid being on their radar, then there is no need for harm."

    NAR "I stay silent for a moment thinking about this information and whether that makes me feel better or not. Something in Linden’s voice tells me there’s more."

    JESSE "I’ll keep that in mind. Now tell me the real reason you called."

    LINDEN "Ever so impatient. The cult is actually in a bit of a rough spot themselves as of late."

    LINDEN "Your actions against them with stopping their actions against the church, you’re on their radar, and they’re having to account for you, it’s been impactful even if minorly to say the least. The existence of you and that tome has made them think twice about taking some actions."

    NAR "After informing me of all this, the phone goes quiet with a heavy click. This all doesn’t surprise me, I figured there was something going on here with my work."

    NAR "The cult is watching me, waiting to make a move. They’re watching me...In more ways than I know. Does that mean that Sara is involved with…?"

    NAR "No...that couldn’t be...it makes no sense, but it would explain some of the stranger things…"

    scene date_transition

    NAR "Apparently I had slept through most of the day, but the rest of it proceeded as usual."

    call new_day("Tuesday, 21st November 1922")
    label free_day_11_21:
    call free_day("knowledge", "Finn", "Linden")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Finn"
            call finn_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Linden"
            call linden_hangout

    if(hangout_failed):
        jump free_day_11_21
    #Finn
    #Linden
    #Study

    call new_day("Wednesday, 22nd November 1922")
    label free_day_11_22:
    call free_day("charm", "Evelyn", "Carter")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Evelyn"
            call evelyn_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Carter"
            call carter_hangout

    if(hangout_failed):
        jump free_day_11_22
    #Evelyn
    #Carter
    #Gardening

    call work_day("Thursday, 23rd November 1922")

    call work_day("Friday 24th November 1922")

    call new_day("Saturday, 25th November 1922")
    NAR "Today was another meeting with Luke, my life has been relatively quieter recently, which has been nice but… I’m still interested in talking to him again."

    scene museum

    NAR "I met up with him in the afternoon at the museum again. After all the complications with Linden, it’s hard to not distrust a lot of the people outside my main group of friends…"

    NAR "But so far there’s been nothing with Luke to suggest anything, and it’s not like my talks with him are ever related to what I’ve been doing, just how I’ve been doing. We met up, and chatted for a bit, before he started to pose a question."

    show luke

    LUKE "You seem like you’re more confident in yourself recently. I take it some things are actually started to work out for you?"
    hide luke
    show jesse

    menu:
        "You could say that…":
            hide jesse
            show luke
            LUKE "You’re not that hard to read."

        "Yeah actually.":
            hide jesse
            show luke
            LUKE "Good to hear."

        "I guess yeah.":
            hide jesse
            show luke
            LUKE "Are you unsure?"

    LUKE "Overall though, it’s been interesting to see your growth over the past couple of months."

    LUKE "I can tell you’ve been starting to feel a lot better about yourself, and your life ever since June. I must say, I was incredibly worried about you back in the hospital in July, but it seems like it’s worked out for you in the end."

    LUKE "Part of where I want to go on this is while you are growing or improving your life in general, I want to make sure of something. That you aren’t just finding new things to replace and avoid your thoughts about your father."

    LUKE "What started all of this stemmed from that grief, and while avoiding it will make things seem better, when you’re alone again you won’t have actually moved on from that."

    NAR "I… didn’t really think about it like that. Everything I’ve been doing has been because of what he left me, and I’ve always been angered by everything I’ve had to go through since…"

    NAR "But I’ve been enjoying my time with everyone. It’s not like I’ve forgotten about him, but he’s right that I haven’t tried to come to terms with it yet…"

    NAR "LUKE RANK 5/10"

    LUKE "Either way, just something I wanted to bring up to you that you may not have ever thought about… I don’t want you to say anything about it now, but it’s something to think about when you have time."

    hide luke

    scene date_transition

    NAR "We chatted for a little before parting ways. The rest of the evening proceeded as usual."

    call work_day("26th November 1922")
    call new_day("Monday, 27th November 1922")

    scene bookstore

    NAR "What would have been an average day, was interrupted by a call from Wilkinson, apparently he was getting the group together to talk about something somewhat important."

    NAR "Finn and I are the last to show up for this little impromptu meeting that Wilkinson has planned for us. He says it’s important, but I almost didn’t want to come. I feel worse for wear today and would rather take a three day long nap instead."

    NAR "We greeted each other, then opened the floor for Wilkinson to talk."

    show carter

    CARTER "Now I’m sure you’re all wondering why I needed you here. Well first off a question, what do you all know about Egypt?"
    hide carter
    show jesse

    menu:
        "Where’s that again.":
            hide jesse
            show carter
            CARTER "What are the odds, a stupid wizard."

        "Not a whole lot.":
            hide jesse
            show carter
            CARTER "It’s alright, let me tell you what I discovered"

        "{i}Stare blankly at Carter.{/i}":
            hide jesse
            show carter
            CARTER "...."


    CARTER "Okay, well I was looking into the power of the tombs. Apparently, there’s a lot of ancient powers that lie there, deep in the heart of the Egyptian Pyramids. It could be related to what the cult is doing now."
    hide carter
    show evelyn

    EVELYN "Hmm...We’ll have to keep an eye out to see if it comes up anywhere in our search. Meanwhile, I’m more worried about Jesse"

    JESSE "Me?"

    EVELYN "Yes you. No offense but you look terrible. Are you feeling alright?"
    hide evelyn
    show jesse

    label tell_evelyn_truth:
    menu:
    #LOOPING ONE
        "{i}Lie and say it’s all good.{/i}":
            hide jesse
            NAR "No, they’ll see through that"
            jump tell_evelyn_truth
            #Loop

        "{i}Play dumb.{/i}":
            hide jesse
            show evelyn
            EVELYN "Stop hiding it. We both know something isn't right with you do just tell me what's up."
            hide evelyn
            jump tell_evelyn_truth
            #Loop

        "{i}Tell them the truth.{/i}":
            hide jesse

    JESSE "Alright to tell you the truth, I’ve been uneasy and have had trouble sleeping. Not only that, I recently had a conversation with Linden about the cult."

    JESSE "They’re more weaved into my life than I originally thought. I don’t know how much exactly, but it’s not exactly a comfortable thought."

    show evelyn

    EVELYN "Jesse…"

    JESSE "Just promise me you guys will be on the lookout and be more careful from now on. We don’t know what could happen next"
    hide evelyn
    show felix

    FELIX "I’d prefer if you didn’t get yourself killed Jesse, but you better not disappoint me with that anytime soon."

    JESSE "Almost makes me want to do it just to spite you."
    hide felix
    show finn

    FINN "While we’re on the topic, some interesting developments have been happening in terms of our relation with Ireland."

    FINN "It seems like things are starting to quiet down a lot more, the main thing being that they had an election and it seems like we’re going to stay united once again."

    FINN "Basically it just seems whatever this cult’s involvement with the division between people there seems to have ended."
    hide finn
    show carter

    CARTER "Which could be a reason they’d want to focus on things in Egypt right now right? Maybe they’re progressing to a new step of their plan? It’s Egypt, that stuff is ancient!"
    hide carter
    show felix

    FELIX "That’s all interesting, but I don’t see us getting any information on their goals in Egypt from any of us right now. It’s an interesting topic, but it’s not exactly relevant to what we can do right now."
    hide felix
    show carter

    CARTER "Oh Mr. Detective, why don’t you do some research then."
    hide carter
    show felix

    FELIX "Ugh…"

    NAR "It was interesting, perhaps we’re not giving Wilkinson’s worries enough credit, but Felix is right we don’t have any real way to investigate."

    NAR "Either way, I can probably trust Evelyn and him to start looking into at least a little."

    scene date_transition

    NAR "We said our goodbyes and the rest of the day proceeded normally for me."

    call new_day("Tuesday, 28th November 1922")
    label free_day_11_28:
    call free_day("knowledge", "Felix", "Evelyn")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Felix"
            call felix_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Evelyn"
            call evelyn_hangout

    if(hangout_failed):
        jump free_day_11_28
    #Felix
    #Evelyn
    #Study

    call new_day("Wednesday, 29th November 1922")
    label free_day_11_29:
    call free_day("charm", "Linden", "Felix")
    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Linden"
            call linden_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Felix"
            call felix_hangout

    if(hangout_failed):
        jump free_day_11_29
    #Linden
    #Felix
    #Gardening

    call work_day("Thursday, 30th November 1922")

    call work_day("Friday, 1st December 1922")

    call new_day("Saturday, 2nd December 1922")
    call half_free_day
    #Walk
    #Study
    #Gardening

    call work_day("Sunday, 3rd December 1922")

    call new_day("Monday, 4th December 1922")

    scene room

    NAR "It has been surprisingly quiet as of late. Almost too quiet. Gives me way too much time to myself and my thoughts, which is scary in it’s own right, but honestly…"

    NAR "thinking about it I feel like maybe it’s been a lot better for me to have a goal like this now, compared to how I was before."

    NAR "The lack of feeling in my right arm has no longer bothered me as much as I think it really should, but that’s not something I can do anything about right now."

    NAR "But something has been on my mind lately. When I think back to the cult, some things just don’t make much sense. What doesn’t make sense"

    show jesse

    label cult_actions_make_no_sense:
    menu:
        #LOOPING ONE
        "The cult’s fashion sense.":
            hide jesse
            NAR "No...Well yes, but No."
            jump cult_actions_make_no_sense
            #LOOP

        "Where the cult is located.":
            hide jesse
            NAR "They are everywhere Duh."
            jump cult_actions_make_no_sense
            #LOOP

        "What the cult is doing.":
            hide jesse

    NAR "Yes exactly, their interests don’t add up. If the cult is interested in all these ancient and political powers, then why are they working in sects involved with Ireland and Scotland?"

    NAR "Linden did come down from Glasgow after all…  It is almost like they want control over the entire United Kingdom. Is there not a spell in the book that can control large populations?"

    NAR "The more I think about it, they didn’t have the pen for quite some time, but it could also be the case that they need both the spell and the political control. I’m so confused. I should ask Isaac for help in this."

    NAR "It could entirely be the case that the cult knows about everything I’ve done and have, but cares little for my involvement due to being low on their list of threats."

    NAR "Even then, Linden has been saying they have taken an interest in me, maybe they haven’t acted because they don’t know that it is me exactly."

    NAR "I’ll look more into this later, for now I should call Isaac, he’s more involved directly with authorities, maybe he knows something about their actions, or at least maybe something then the rest of the group hasn’t thought of."

    NAR "The phone rings for three seconds before it is picked up. Isaac answers in a rushed tone."

    ISAAC "Jesse? What is it, I am a bit busy at the moment."

    NAR "I go on to explain everything that I have been thinking in a paraphrased way, trying to get my thoughts together enough to make sense."

    ISAAC "I see. I have some information that may be useful for you to hear. I’ll call you back tomorrow morning."

    scene date_transition

    NAR "The phone hangs up abruptly. Wonder what that was about. Either way, I guess I’ll just have to wait. I kept thinking about the situation for the rest of the day."

    call new_day("Tuesday, 5th December 1922")

    scene room

    NAR "The thoughts I had yesterday won’t seem to leave my mind. What exactly do I make of all this? The phone breaks me out of my deep thinking. Must be Issac. Picking it up, I was not disappointed."

    ISAAC "Sorry about yesterday, got caught up in something myself. Anyways, you had questions, right? Well, let me fill you in on what’s been happening."

    NAR "I sit up and make sure that I can hear every word that comes through."

    ISAAC "Have you heard of the new constitution being drafted today? It’s said to end the war soon in Ireland. Great, right? A vote is set to see if they will remain in the UK, hopefully uniting the country."

    ISAAC "Other than that, not much has been happening. A few minor crimes, and, oh right there’s that murder trial as well. Nothing we can’t handle on our end."

    JESSE "Oh I see…"

    ISAAC "Something on your mind?"

    JESSE"....I’m fine, just been overthinking I guess"

    ISAAC "Well, keep me posted if you need anything, and one last thing. It would appear that some of the cult’s higher ups have stepped down"

    NAR "This catches me by surprise and I almost spill a cup of water on myself"

    ISAAC "I’m not too sure what this means for us, but stay alert."

    NAR "With that final message, he hangs up the phone. Things are calming down, the exact opposite of what I thought would happen. Didn’t the cult want chaos?"

    NAR "Did they mess up somewhere? I need to take my mind off things for now"

    show jesse
    menu:
        "Take a nap.":
            hide Jesse
            NAR "A nap does sound nice right now."

        "Go for a walk.":
            hide Jesse
            NAR "It looks like it’s about to rain. I should take an
            Umbrella."

        "Read a book.":
            hide Jesse
            NAR "Reading always did calm me down."

    NAR "Something felt wrong, I need to talk to somebody about all this, things seem too quiet, and they couldn’t have been from just my actions right?"

    NAR "Maybe Cathee will show up any one of these days and bring up what’s actually happened… in a completely unparseable way of course."

    scene date_transition

    NAR "The rest of the day proceeded as usual… usual?"

    call new_day("Wednesday, 6th December 1922")

    scene bookstore

    NAR "It has been raining hard today. That’s all I am focused on when the phone rings yet again. Aren’t I popular these days. I answer the phone without hesitation and the sound of Felix, wonderful."

    FELIX "Hello Jesse. I’ll make this call brief. Just wanted to give you some updates on the cult."

    FELIX "I’m sure you haven’t made much progress that I haven’t, They’ve been suspiciously calm as of late. In fact, there’s talk of some disagreements. Might not be as stable as we thought."

    NAR "That doesn’t sit well with me. Something is up."

    JESSE "ISSAC told me something similar yesterday. What’s going on?"

    FELIX "Oh so you have done some of your own research huh? I’m not too sure, but I’ll let you know when I know. Trust me, you have the same doubts I do right."

    JESSE "It just seems like things are working out better than they should."

    FELIX "And additionally they are certainly being affected by us, and you’re suspiciously still alive."

    JESSE "That’d be because they haven’t found us, otherwise they’d have no reason to."

    FELIX "I agree with you there… but something about that doesn’t sit well with me, but I don’t have any other reasonable explanation."

    JESSE "It’s entirely possible that they’re also just not as focused on us because they’ve been spread to having to deal with the reunification of everyone again."

    FELIX "We don’t know how big they are, but if we take the idea that we’ve done to that has been more minor to them, that’d explain why they have been taking a break from us."

    FELIX "Even then Jesse, things just don’t add up. We don’t have enough information."

    JESSE "I agree with you there, but so far our only real way to combat them has been reactive. The only other way to do something more would be to directly try and start working against them, but we need information for that and…"

    FELIX "It’s a big risk. If they get a hold of one of us, they’d get to you. You really are a liability even when you aren’t tired from your spellcasting."

    JESSE "I am the liability that is the only reason we’ve made any progress."

    FELIX "You can be useful and a liability at the same time. Jesse, I know we can’t trust Linden very much at all, but maybe that’s a direction we can take this to find a way to attack them directly."

    FELIX "I know you’re worried, but we won’t make the same mistakes as your dad."

    JESSE "Who’s to say he made any mistakes…"

    FELIX "Talking about this only makes me more frustrated, I said this would be quick, goodbye Jesse."

    JESSE "Bye Felix."

    NAR "He… had already hung up."

    NAR "Next time I’m free, we need to contact everybody and figure out what we can do. We’ve been reactive for far too long. We have the tome, we can take the initiative."

    call work_day("Thursday, 7th December 1922")

    call work_day("Friday, 8th December 1922")


    call new_day("Saturday, 9th December 1922")

    NAR "The days seem to blend together nowadays. Today we can finally try and make progress again, even if it’s just trying to change our ideas on things."

    NAR "I thought I wouldn’t be able to make it, but it seemed like Sara was called in for something extra today, so I tried to get them all together today rather than Monday."

    scene bookstore

    NAR "I hurry my stride as I enter the Wilkinson’s bookstore. He had called us and arranged another get together. Hopefully with new information on what exactly is going on."

    NAR "I glance up and meet the gaze of Evelyn as she turns towards the door. I should greet her, but the mood overall seems pretty tense, we enter the store to see everyone already there."

    show felix

    FELIX "Last as always Stout."

    JESSE "Thought that’s what you saved the best for?"

    NAR "Carter clears his throat and begins the so-called meeting."
    hide felix
    show carter

    CARTER "Shut…"

    CARTER "Anyway, glad we could all make it. I just wanted to say that I’ve noticed something rather interesting behavior with the Guiding Comet. They’re backing down, it seems."

    NAR "This is all old news for me. I’m a tad disappointed. I can tell Felix is also already disappointed."
    hide carter
    show finn

    FINN "Are you sure?"
    hide finn
    show carter

    CARTER "It would appear so, but who knows. Maybe they’re plotting"

    NAR "He said that with a small chuckle. Is this funny to him?"

    CARTER "Whatever, for now, I’m happy. This is good news for my cult. One less thing for us to worry about. Maybe we can finally start taking action against the grand rulers of this land"
    hide carter
    show evelyn

    EVELYN "Or, you could not do anything too terrible."
    hide evelyn
    show carter

    CARTER "I would never, I thought you all knew me?"
    hide carter
    show felix

    FELIX "I do know you, and exactly how to arrest you and your cult."
    hide felix
    show carter

    CARTER "That’s such a low blow."
    hide carter
    show evelyn

    EVELYN "Come on, as long as we’re working together, we’re all friends here."
    hide evelyn
    show finn

    FINN "Yeah guys, we’ve already been able to do so much to stand up against what we all thought was an impossible enemy at first."

    hide finn

    NAR "After a moment…"

    JESSE "Is that all."

    show carter

    CARTER "Pretty much. Anyone got anything else to add?"

    NAR "The others look around at each other to see if anyone had something to say. Felix begins to start but…"

    hide carter
    show felix

    FELIX "Well…"
    hide felix
    show finn

    FINN "OH! It’s Jesse’s birthday soon. We HAVE to do something."

    JESSE "Ehh...I don’t know about that"
    hide finn
    show evelyn

    EVELYN "We must! Plus it will be a good distraction from all this crazy stuff happening"
    hide evelyn
    show finn

    FINN "Yeah we could do something at your place Monday or something right?"

    JESSE "I mean, would that be safe?"
    hide finn
    show carter

    CARTER "If there was an occasion to celebrate, this would probably be it you know. If you’re really worried, if something comes up tomorrow I’ll let you know."
    hide carter
    show felix

    FELIX "No, actually I like this idea."

    JESSE "Well.. I guess it wouldn’t hurt."


    hide Felix

    NAR "The group decides to call it for the day. I almost forgot about my birthday until now… it really is in just two days."

    NAR "Do we really have to do something? What if something happens… We were all on our way leaving, Felix taking me aside alone."

    show felix

    FELIX "If what we’re good at is being reactive, wouldn’t this be a possibility."

    JESSE "Are you expecting something to happen?"

    FELIX "Not exactly, but if something does, the two of us can at least prepare for something. Of course I’d rather not."

    JESSE "Are you even coming?"

    FELIX "If the idea is to bait them… I guess I’d have to."
    JESSE "I don’t like this… at all. You don’t actually think something is going to happen right?"

    FELIX "Not really, I hate to admit that I do trust Wilkinson’s opinion on this stuff… I’m just grasping for something that we can do with them."

    JESSE "Stop trying to go with things that may be a risk to us."

    FELIX "At the very least, let’s spend the next few days having fun, we’ll bring up our idea to start taking the initiative against the cult on tuesday, after your birthday."

    JESSE "Yeah, it would be good for our morale at the very least. Goodbye Felix."

    hide felix

    NAR "We can start thinking about what we can do to stop them tuesday… the calm before the storm, celebrated with my birthday of all things."

    scene date_transition

    NAR "Later that night I actually got called by Linden, and he said I didn’t have to come in for work tomorrow, some sort of Holiday, which left it open to meet with Luke, which was nice."

    NAR "Sara wasn’t in a good mood when she got back, but she didn’t talk about it too much. The rest of the day proceeded as usual."


    call new_day("Sunday, December 10th, 1922")
    NAR "One more day until we were going to have that party for me… but before then, another opportunity to meet with Luke. I met up with him at the Cafe again this time."

    NAR "As usual we started with more minor small talk before he transitioned into the point of the conversation, and as usual, reading my mood."

    show luke

    LUKE "You seem more worried today than before. Are you willing to talk about it?"

    JESSE "Well… I’m not sure, it’s just more like I don’t know where anything is going. Everything is going good with all my friends and what we’re doing, but it just seems like something is wrong even though nothing really is."

    LUKE "You’re not a fan of how simple things have gotten in a sense. After your life has been so hard to get through for so long in your mind, now that it’s become more calm you feel like things are wrong don’t you."

    LUKE "I’d say my only tip is that if you do really enjoy what you have now, even if it feels like it could break or something is wrong, you should try and protect it."

    LUKE "You’ll be able to realize how important stuff like this is when it’s over, so even if you don’t think it’s important now, you should try and keep it for as long as you can."

    LUKE "Either way, I know it’s your birthday tomorrow right? I hope you plan to spend in some way fun, take it as an off day or something. You deserve it."

    NAR "Eventually the conversation ended naturally, and he ended up having a meeting for some other things later that day."

    hide luke

    NAR "LUKE RANK 6/10"

    NAR "The rest of the evening proceeded as usual."
    call new_day("Monday, 11th December 1922")

    show room

    NAR "Today… it felt like any other day, but it was my birthday wasn’t it. It seemed like Sara had remembered as well, and prepared me food already."

    show sara

    SARA "Happy birthday! Sorry I haven’t been able to do too much, work has been getting… a bit complicated you know. Were you planning to do anything today?"

    JESSE "Actually yeah… a few of my friends were going to be coming over… Sorry I didn’t tell you about any of it happening until now."

    SARA "Oh, no that’s fine… I’m glad you’ve been getting along with more people recently, I could tell you’ve been happier. But I take it they’re gonna be coming here right…"

    JESSE "Yeah, is that a problem? I’m sure they’ll get along with you, they’re alright people… and the problem person thankfully isn’t going to be here…"

    SARA "Oh… no it’s fine, I’ll… I’ll get ready, yeah…"

    JESSE "Is something wrong?"

    SARA "No, it’s fine… I’m happy for you… it’s good, I’m excited, All of you are probably better together right?"

    JESSE "Yeah I guess you could say that."

    hide sara

    NAR "Everyone began to arrive, and they all seemed to get along with Sara, her and Evelyn began to hit it off. But she seemed surprisingly… different than normal… Then it almost seemed like Felix was trying to one up me even now somehow."

    NAR "It was fun, but… too many things were on my mind, Sara’s attitude, the Cult’s true motives, the idea of fighting the cult directly…"

    NAR "We ended up watching a play on the television set, it originally was performed a few months ago, called “Secrets” but I couldn’t focus on that too much either."

    NAR "I start to notice that Sara is looking a little anxious, it could be all the people she hasn’t met until today. Suddenly, a loud crash!"

    NAR "The windows of the room shater, the glass lodging themselves into Evelyn’s shoulder. What is happening?!?"

    NAR "I look to my left with a sharp turn and see Finn on the ground. Is he breathing? A massive shockwave occured, and then three people in the cult’s acolyte robes rushed in…"

    NAR "I can’t think straight right now. The blood is pounding in my head. We’re being attacked, the thought finally occurring to me. I need to act fast. It was far too fast."

    NAR "Felix yelled out at me to figure something out. What is there to figure out?! What can I even do!? They begin casting another variant of that shockwave spell."

    NAR "It blasts all of us away, I was further away from where they casted it, but it still was incredibly painful. I’m… not sure if they’re okay… I don’t know what… I tried to get into my room, as I was blasted into it, and closed the door."

    NAR "I can hear Sara screaming at them, and everyone trying to do something, but it’s all cut short. In not even a moment they start to pound on my door and are demanding the tome from me, They’re going to blow down the door."

    NAR "How. How do I. I can’t."

    NAR "Magic, something, anything… Rewind… that spell… No it’s far too strong, it could… kill me right?! I can’t… No no it’s the only way to stop this I need to. I lift up the tome, as the door splinters into the room."

    scene date_transition

    NAR "I recited the incantation that I had out into the spell many weeks ago… As soon as I finished, the wave of lethargy hit more than anything I had ever experienced…"

    NAR "but luckily I was already sitting down on the couch… I… it’s three minutes before that all happened… I have… to… I’m too tired… But I can’t…"

    scene room

    JESSE "I’ll be right back guys… forgot to do something the other day… It’ll take just a second"

    NAR "Okay Jesse, I know we’re tired, but right now, we can’t mess this up for them… there’s no way we could stop that… I need to just… how do I stop them…"

    NAR "I have to give them the tome and pen, there’s no way…"

    NAR "I tried my best to hide how tired I was, and I can’t tell if it’s because I can’t think straight, but I think I was pretty convincing."

    scene date_transition

    NAR "I went inside my room and got the tome and pen, and left the room. And found them making their ways."

    JESSE "Take it!"

    NAR "I shove the book and pen into their hands."

    JESSE "Will you leave them alone now? Promise me they won’t be harmed!"

    NAR "The cultist smiled at me and confirmed that they were safe...for now. I begrudgingly headed back into the apartment, my energy drained from the spell."

    NAR "I open the door to concerned faces. I tried to tell them that ‘I had just forgotten to give mail to the neighbor, they weren’t home the other day so they knocked on my door and asked me too…"

    NAR "like I said, nothing much.’ I’m not sure if they bought it though, I know Felix won’t buy it… but at least he’ll keep it to himself right…"

    NAR "After the confusion, the group proceeds to finish watching the play. I can barely keep conscious…"

    NAR "After a few hours, everyone leaves, and I am left in the darkness once again. I lay down on my bed."

    NAR "Only going to take a brief nap I think as the world around me goes black."

    NAR "I’m… going to… survive right…"

    #CHAPTER 4 - END

    jump chapter5_start
