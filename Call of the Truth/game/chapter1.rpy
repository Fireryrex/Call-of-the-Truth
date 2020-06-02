# Chapter 1 begins here

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define NICK = Character("Nick")

label chapter1_start:
    $ current_chapter = 1

    scene room
    centered "{size=+30}CHAPTER 1: When Does the Night Sleep?{/size}"

    call new_day("Wednesday, 5th July 1922")

    scene room

    NAR "Another day, another bit of time free to myself… except I’m not sure if there much I can even do at this point. Sure I now have some sort of tools that are guaranteed related to whatever is happening, but where do I even start with them. Hmmm…"

    NAR "No matter how I look at this, I’m going to need more people that I can actually trust and get information from, there’s no way I could do this alone with being monitored on the daily."

    NAR "Even if we think that these hours where I’m completely alone are free that’s not enough time. The second I go and check out a book of the history of cults or something that’d be an obvious trail someone could follow."

    NAR "I can’t exactly ask the investigator to do much either, if his department is already trying to hinder things. The best I can do is just act like I’m getting out and hanging out with friends more, which would make sense since Finn just came back."

    NAR "He’s not going to be able to do much alone either… not that he exactly specializes in this field of work anyway… But he could be incredibly useful actually, I think he said he was gonna call me today? I can talk to him about my idea then."

    NAR "Waiting a little bit, and just continuing into the afternoon, the phone rings, to the expected person."

    FINN "Hey! Finally got the time to call you today, was wondering if you’d made any progress into the thing?"

    NAR "I explained to him that I had done the past two days."

    FINN "Oh wow, that’s pretty crazy stuff, glad we finally have some idea of what’s going on"

    JESSE "Well, about that… We really don’t have any information on this stuff, and going out and looking at it is not the best idea for me and…"

    FINN "I’d have no real idea of where to even start yeah… if you got any ideas, I’ll be willing to help out however I can"

    JESSE "That’s a big part of it actually, I was hoping you could try and confirm if certain people are safe to share this stuff with, if we’re actually thinking about doing anything about this we’re gonna need more people on our side… I was thinking of a uni friend of mine? Evelyn Baker, she’s still taking classes now I believe, and she’s probably the most booksmart person we could trust."

    FINN "Oh yeah, I can definitely do that, if she’s just at the university I can probably find her and bring you up. Just leave it to me, I’ll catch back up with you when I can, probably by the weekend, see ya"

    JESSE "Yeah that should be fine, see you then. -Click"

    NAR "Wait a second, no that’s not fine, we only want to get people in this one at a time, and I’d rather not get Sara involved if we don’t have too."

    NAR "there’d be no reason for me to just go alone… besides if we assume the worst about everyone I don’t have Finn check out first…"

    NAR "No, that’s not something that I need to worry about right now, I’ll just make sure to catch the phone and play it off on Saturday."

    NAR "...But do I really want to keep going with all of this? This is clearly important stuff… enough to kill someone over, but why would they go through such a process of monitoring me…"

    NAR "Even if they believed I had some clue as to where this thing was, assuming they want it in the first place… agh, one step at a time, we don’t even know what it is right now… "

    scene date_transition

    NAR "Guess I can relax until I hear back from Finn."

    call work_day("Thursday, 6th July 1922")

    call work_day("Friday, 7th July 1922")

    call new_day("Saturday, 8th July 1922")

    scene room

    NAR "It was your normal saturday morning, and I was prepared to cancel whatever with Finn just to keep my cover, at the very least the cult is certainly watching Sara’s activities as well now that I’m not living here alone…"
    NAR "Maybe that’s actually better since they’ll have to spread their resources when she’s out and about too… Either way, that *was* the plan but…"

    NAR "The phone began to ring, and I was able to nonchalantly pick it up, but it wasn’t Finn. It was a lead at the place Sara and I worked at. And he asked for Sara."

    NAR "They talked for a little bit, but not much. Immediately after she started to look a little frustrated, and then started to go and get dressed for work."

    show sara

    SARA "So, it turns out, they desperately need someone to come in, and of course they need me, as if this week couldn’t get any more awful with these guys."

    SARA "Haaa… I guess that’s what I get for taking off a day, either way it sounded like this won’t be a full day at least."

    SARA "You’re so lucky you don’t have to deal with the leadership in my branch, they’re actually the worst when it comes to this…"
    hide sara
    show jesse

    menu:
        "Sorry to hear that.":
            hide jesse
            show sara
            "Eh, it’s whatever, I can deal with it."

        "I believe in you.":
            hide jesse
            show sara
            "Thanks… at least."

        "The luckiest.":
            hide jesse
            show sara
            "Just don’t get promoted…"

    hide sara

    NAR "She got ready and left, and I wished her good luck on whatever they needed her for…"

    NAR "After not even five minutes, there was a knock on the door. Did she leave her key here? Either way, I opened it up, and was greeted by Evelyn!"

    show evelyn

    EVELYN "Hi! Sorry that we didn’t call you earlier, figured you’d be alone and free so I was just coming to get you. Finn is already at the Cafe, he said you would know where it was?"
    hide evelyn
    show jesse

    #menu:
    menu:

        "Call next time!":
            hide jesse

        "That was too close…":
            hide jesse

        "I really need a way to contact him first huh…":
            hide jesse

    show evelyn

    EVELYN "Oh, was something going on? He said this was a part of the plan you guys made before?"

    JESSE "No.. it’s fine somehow but… wait did you see, er rather did a woman with orange hair, and freckles?"

    EVELYN "Yeah actually, I ran into her at the bottom of the stairs, why do you know her?"

    JESSE "Wait… I haven’t told you guys about that yet have I… it doesn’t matter, looks like my day has freed up, let’s head to that cafe."

    hide evelyn

    scene cafe

    NAR "Joining Finn at the cafe, the three of us sit down at the same spot as last time."

    JESSE "Okay, first thing I’d like to say to you guys is that I’m probably not going to be free on saturdays, and this was an incredibly lucky situation where it just happened to work out."
    JESSE "Basically, I have a flatmate now, an old friend of mine so I’m sure she’s fine… but she’s probably being watched by the cult too."

    show finn

    FINN "Wait, when she’d start rooming with you?"

    JESSE "A week or so ago, she was already technically without a home for a few days, but it was on the day I met up with you actually…"

    JESSE "No, no I don’t think she has anything to do with this, she was out getting groceries during the time we were together, so she’s not a spy of any kind…"

    FINN "Well, alright, if you trust her, I’ll leave that up to your discretion. But anyway, the reason we’re here today, I didn’t go into much detail about what we’ve been looking into, but then again we don’t really know much now do we."
    hide finn
    show evelyn

    EVELYN "I know you guys are looking into some sort of occult book right? Like a magical tome! Maybe not that, even assuming they're real…"

    EVELYN "But I can use the library and do some of my own research into this stuff, and I’m sure I’d be more free from whatever is keeping an eye on you Jesse."

    EVELYN "Oh yeah, and don’t worry about me, I know a thing or two about staying away from what could actually get me in trouble. Was there anything specific I should start with?"

    JESSE "Yeah actually, first of all the book, but also there were scraps of paper with some strange drawings on them in the same vault that the pen was in for the book, but it doesn’t seem like the scraps can do much on their own."

    JESSE "I’m not carrying the stuff with me, but if you can just look into the mysteries surrounding London and the other places involved with my dad or anything that’d be a place to start."

    EVELYN "If anything, I could probably come by and drop off some things in your mail or something that you could look into with your free time."

    JESSE "By the way Finn… what’d you do to actually figure out if she was okay or not?"
    hide evelyn
    show finn

    FINN "Oh uh… well that actually went completely different than I’d expect"
    hide finn
    show evelyn

    EVELYN "Um… when I saw him I kinda just started questioning him about it on my own, and then we realized we were both on the same side… I’m sorry Jesse, but I had secondary reasons for getting in touch with you the other day…"
    EVELYN "I didn’t feel confident enough to ask you about it then, I didn’t want to bring up the old wounds again with you, but now that I know you two are already trying to get involved, I may actually have an Idea of where we could start…"
    EVELYN "although I’m not sure if there’s much we could do with it in the first place."

    EVELYN "A friend I know has been struggling with his family life, and his dad is actually a politician. From what I’ve gathered it seems like his dad is being threatened by a group, who I believe is actually the same cult that is interested in you!"

    EVELYN "I haven’t asked him too much directly about this, But I could try and get us a meeting with him specifically so that we could talk about it."
    hide evelyn
    show finn

    FINN "I’m not sure where it will get us, but at the very least it could be some insight about the actual goals of these people right!"
    hide finn
    show jesse

    menu:
        "Is it safe?":
            hide jesse

        "Will he be up to it?":
            hide jesse

        "You seem confident in it.":
            hide jesse

    show evelyn

    EVELYN "Yeah, It’s been something I’ve been thinking about doing for a while now, and I know he’ll be a lot more interested in talking to you than he would be for me or anyone from the government. I know you’re busy tomorrow, but would Monday work out?"

    JESSE "No, I meet up with my mentor twice a month, on the 10th and 25th, so those days are also gonna be out for me doing stuff, unless it’s worth it enough that’d it be better to skip and raise some suspicions."

    JESSE "That being said, I’m free for tuesday, the apartment will be free, but if this guy is also connected to the cult, that’s probably a terrible idea."

    JESSE "Would it be possible to meet him at the university, I have some college books I’ve been meaning to give back for a while now, which would be a great excuse to head over."

    EVELYN "Works for me!"
    hide evelyn
    show finn

    FINN "I’m sure you guys got this, besides me going there too would definitely be strange, and besides I think I’m actually going to need to go to work soon."

    FINN "Don’t worry though, it’s nothing serious just some report stuff since we were only recalled kind of recently, I’ll tell you about it later if anything comes up."

    scene date_transition

    NAR "And with that, we finished up and headed home, and tomorrow’s work was more of the same."

    call work_day("Sunday, 9th July 1992")
    call new_day("Monday, 10th July 1922")
    NAR "Today was another of the scheduled meetings with Luke. this would certainly be a thing that if I skipped it’d tip off whoever that I was acting more strangely… besides I actually do think I want to talk to him anyway."

    scene museum

    NAR "I met up with him and we went to the museum, a more favorite spot of his, just to admire people’s creations, and it was a more quiet public spot that was free. There was other small talk, as the conversation continued…"

    show luke

    LUKE "Jesse, I was wondering… you seem a bit conflicted? Did you follow up with your friend and something came up?"
    hide luke
    show jesse

    menu:
        "Sort of…":
            hide jesse
            show luke
            "If you don’t want to talk about it, that’s fine"

        "Not exactly.":
            hide jesse
            show luke
            "Hm, well either way."

        "Essentially.":
            hide jesse
            show luke
            "Oh, I’m sorry to hear that."

    LUKE "In the end, I don’t think you need to tell me too much about it. It would be strange if I tried to tell you exactly how to live your life in the first place."

    LUKE "I should ask however, I know you may not want to get too invested in things that aren’t just for yourself, which I understand and is important sometimes."

    LUKE "If what you need to do doesn’t directly help you, as long as it doesn’t harm you too much you should be open to trying it."

    JESSE "That’s… not entirely it. It just seems like people are expecting something out of me. When in reality I can’t do too much."

    LUKE "I can imagine that it’s impossible for you to avoid comparing yourself to him. Don’t just assume that’s why everybody is looking at you though…"

    LUKE "They’re probably still just interested in you and what you can do. You aren’t your dad, and there’s a reason they were your friends in the first place."

    JESSE "It’s just, I’ve never been too interested in what he was doing… but it’s not like it wasn’t interesting… It’s just I know I never would have been able to be on par with him, and I could just do something other than follow in his footsteps."

    LUKE "You don’t have to be better than anyone Jesse, you can still do things, or have people rely on you without having to be the best."
    LUKE "Overall, I’d say that it’s okay to be yourself, and if people are trying to rely on you, don’t feel like you need to be someone better just because of that."

    NAR "I don’t want to go in detail about any of this… especially with all the occult things happening… But I’m thankful I can talk to him about this sort of stuff."

    $ luke_rank = 2
    NAR "LUKE RANK [luke_rank]/10"

    scene date_transition

    NAR "We talked for a bit longer, but eventually we said our goodbyes, the rest of the evening proceeded as usual."
    call new_day("Tuesday, 11th July 1922")

    scene room

    NAR "Tuesday, today is when I’m supposed to meet up with Evelyn to talk to her friend. Time to go find those textbooks too, I’m sure it won’t actually matter how overdue they are right?"

    NAR "But… What am I even doing? I’m not an investigator like my dad, and I feel like that’s what both these people are expecting out of me. Even if I was, it’s not like this is anything to go off of, what we’re trying to do is just insane…"
    NAR "But that’s why it’s just the start, right? Anyway, I should head over once I get the call."

    hide room

    scene university

    NAR "At the university, I found the library where we said we were going to meet up, and it's mostly empty as usual, and eventually I find Evelyn and their friend, Nick."

    show evelyn

    EVELYN "I guess we should get straight into this right? Nick, this was the friend I was talking about, I can’t promise anything specific, but you can trust him to help out in some way"
    hide evelyn
    show jesse

    menu:

        "Don’t expect much.":
            hide jesse
            NICK "It’s okay, I’m not… really…"

        "thanks for meeting with us.":
            hide jesse
            NICK "I figured it was better than doing nothing"

        "So, what do you know?":
            hide jesse
            NICK "Well, it’s not that much honestly…"

    NICK "Well, it’s all been going on for a few months now, my father became indebted to some that support the more radical ideas circulating in Ireland and has been threatened about some of his opinions about it."

    NICK "He’s essentially being blackmailed into it. He’s been trying to back down, but he’s being required by this strange group to continue to spread the message, and rally people for it."
    NICK "I can’t say he hasn’t been protected by these people either. But that’s basically it."

    NAR "Hmm… I know there’s some political drama happening with that, maybe that’s what Finn is involved with currently, definitely want to follow up with him on that… But where can I go with this?"

    show jesse

    label blackmail:
    menu:

    #--Loop all three, unless blackmail is chosen

        "Blackmail?":
            hide Jesse
            NAR "I know he’s been getting sent things or been approached by this group, and they’re definitely not direct supporters of the movement itself"

    #Continue

        "Tell me about these threats.":
            hide Jesse
            NAR "They’re more minor, but there are loud voices on both sides"
            jump blackmail

    #Loop

        "He doesn’t believe what he’s advertising?":
            hide Jesse
            "Yes, it would be easy to unite more people if he was able to get out of this easily."
            jump blackmail
    #Loop


    NAR "we can work with that…"

    JESSE "If you could get us those messages or anything from this group that’d at least be some way we could start figuring out who they are, which would make this a more comprehensible enemy…"

    NICK "Yeah, I’m sure I could get some of those from him, er, I wouldn’t let him know of course, but if that can help you guys with the investigation then I’ll try my best."

    show evelyn

    EVELYN "You can get in touch with me as soon as you find anything, Jesse here is a bit busy, so if you need to contact him, you can do it through me. Thank you for your time."

    hide evelyn

    NAR "Nick got his things and left."

    show jesse

    menu:

        "What does he know about me…":
            hide jesse
            show evelyn
            EVELYN "He was only willing to do this because I may have made you sound more impressive than you’d want… but it’s fine right?"

        "We can trust him right?":
            hide jesse
            show evelyn
            EVELYN "If there’s one thing I know, it’s that he does care about his dad"

        "Still not sure about this.":
            hide jesse
            show evelyn
            EVELYN "Don’t worry, I don’t think it could be connected to us if he messes up anyway"

    EVELYN "Either way, now that he’s actually invested in trying to do something, I’ll keep an eye on him, and get back to you when he’s actually found something. But the goals of this group are still so strange to me."

    show jesse

    menu:

        "They’re not simple.":
            hide jesse

        "Bigger than we know right now.":
            hide jesse

        "Part of it is to divide people at least…":
            hide jesse

    show evelyn

    EVELYN "Yeah, I guess we just have to take this one step at a time huh, we don’t even know what we’re up against really… Anyway, thanks for coming."
    EVELYN "I know he wouldn’t have been up to talk about something personal like usually. Who knows, maybe you are fit to be an investigator, you’ve got the rep already!"

    EVELYN "I’m just joking… I know it’s not what you want to do… Anyway, the next important meetup will be after we get something physical from him."

    hide university

    scene room

    NAR "I returned to the apartment, and proceeded as usual, but is it really a good idea to get involved with all of this? Apparently they’re trying to mess with the political side of things too…"

    NAR "or who knows, it’s not like we’ve confirmed that it’s the same group, it could be completely unrelated, could just be multiple cults."

    NAR "I’m not sure if I want it to be multiple cults."

    NAR "The phone rang once more, and it was Finn!"

    FINN "Hey, sorry to call you so abruptly, but I wanted to let you know that the work thing is turning out to be more complex than I’d hoped. Don’t worry about too much, I’ll talk to you about it in detail once I actually get more involved…"

    FINN "But I’ve got a feeling it’s actually related to what we’re trying to get involved with too. Anyway, see you soon man, good luck."

    NAR "Hmm… well… no use thinking about a lot of this stuff on my own, we just need more information, but it looks like we actually have two leads from them."

    hide room

    NAR "Then there’s the mess of me and my dad’s involvement with them. I try to come up with something for hours… it’s not worth it, let's just wait for now."

    #FREE - Wednesday, 12th July 1922")

    call new_day("Wednesday, 12th July 1922")
    label free_day_7_12:
    call free_day("charm", "Finn", "Evelyn")

    if(spend_free_day_socializing):
        if(with_friend1):
            NAR "I decided to spend the day with Finn"
            call finn_hangout
        elif(with_friend2):
            NAR "I decided to spend the day with Evelyn"
            call evelyn_hangout

    if(hangout_failed):
        jump free_day_7_12

    #Finn
    #Evelyn
    #Gardening

    call work_day("Thursday, 13th July 1922")

    call work_day("Friday, 14th July 1922")

    #HREE - Saturday, 15th July 1922")
    call new_day("Saturday, 15th July, 1922")
    call half_free_day

    #Walk
    #Study
    #Gardening

    call work_day("Sunday, 16th July 1922")
    call new_day("Monday, 17th July 1922")

    scene room

    NAR "It’s been some time since anything has come up, then again I haven’t been too free. It’s only been a week since those two split to gather some information, but what can we really do… I guess I can only hope to get a call from them… Soon…"

    NAR "After some time, I did get a call; it was from Finn."

    FINN "Hey, you're free for a second, I can probably stop by and talk with you right?"

    show jesse

    menu:

        "Yeah.":
            hide jesse
            FINN "Alright cool"

        "I’ll clean up.":
            hide jesse
            FINN "haha, you don’t have to"

        "No cafe this time?":
            hide jesse
            FINN "not today, can’t go there every time we meet up right?"

    NAR "After a bit, Finn shows up, and he gets settled in."

    show finn

    FINN "So hey, it’s been a while. Sorry I haven’t been able to get back to you on what’s been going on, but it’s been an interesting venture for my corps."

    FINN "I am a part of a group that has been involved with the more political happening between us and the groups in ireland…"

    FINN "Overall, it seems like some actions from a rebellious group have been theorized to happen."

    FINN "It seems like they’ve been delayed overall from external forces that are being investigated which, it’s probably a bit to go and say that’s also a part of the cult but…"

    JESSE "Well, it might not be too far off actually, It’s not entirely confirmed yet but it seems like this cult might actually be involved with trying to divide people, politically like this"

    FINN "Oh, that’s pretty interesting then, so yeah, it seems like some things have been delayed. Either way, There was an assination a while ago, but apparently it was originally planned to be about a month ago."

    FINN "I was on call for it at the time, but nothing came up, that’s the gist of what’s happening with it now, that call was rung you know."

    FINN "And the important thing to say… is that the assassination did happen, and the culprits for it have been caught. They’re a part of the Irish republican party."

    FINN "Which definitely adds up for it to be at least somewhat related to the cult. They’re going to be executed in two days, so I’m not sure if there might be any more action from any groups around about that."

    FINN "They have other targets too that we’re looking into, was wondering if that might correlate with that friend of Evelyn’s, but maybe we can meet up and see what’s going on with her tomorrow or something, she’s bound to have something right?"

    hide finn

    NAR "I wished him well, and then contacted Evelyn at the university and asked her if she was free to meet up at the Cafe or something the following day, and she was."

    scene date_transition

    NAR "The rest of the day proceeded as usual."
    call new_day("Tuesday, 18th July 1922")

    scene cafe

    NAR "As planned yesterday, I headed over to the Cafe at the time I arranged with Evelyn and Finn and met up with them."
    NAR "I was also going to actually bring the scraps of paper that I had to directly show evelyn this time. Finn repeated what he had told me to Evelyn, albeit much simpler."

    show evelyn

    EVELYN "If all that is true… why would the cult be trying to simultaneously help out the Irish republican party and also look to stop it’s support over here."
    hide evelyn
    show jesse

    menu:

        "They don’t actually care about either side.":
            hide jesse

        "It’s just to incite division.":
            hide jesse

        "They do seem confused.":
            hide jesse

    show evelyn

    EVELYN "Oh, and yeah, I was able to get a piece of the mail they sent to Nick’s father, and the letter inside is actually quite worrying."

    NAR "she pulls out the letter and shows it to us"

    EVELYN "It’s not directly a threat, but it’s fairly clear this has become expected between both parties. It’s almost as if the situation with his dad is not much of a focus for them."

    EVELYN "Something about the letter seemed familiar… part of the design under the signature was the exact style of symbols on the book and paper scraps, I pulled out some as an example for them."
    hide evelyn
    show finn

    FINN "Well that confirms it right? This cult is playing both sides just to incite more violence, and probably have excuses to get rid of certain people in politics!"
    hide finn
    show evelyn

    EVELYN "Well… that’s what they’re doing, but it’s not why they’re doing it, which is pretty hard to think they’re just doing this for the sake of chaos right?"

    JESSE "And if we don’t know why they’re doing it, there’s not really any way to figure out what they’ll do outside of this, and trying to get further into this is a bit hard if we have to try and get into politics…"

    EVELYN "Yeah… it’s almost like we need a different angle on this entirely, we already knew how deep into the system they are with the investigator right?"

    EVELYN "Oh, and sorry I haven’t been able to look into those other things you mentioned about from your dad, I’ve been focused a little on just this."
    hide evelyn
    show jesse

    menu:

        "Any other leads in the letter?":
            hide jesse

        "What about the postage?":
            hide jesse

        "Where was the letter sent from?":
            hide jesse

    show evelyn

    EVELYN "You would think it would just be secretly delivered or something, but if they are actually more ingrained in society than we think…"

    EVELYN "maybe it’s something we could check out. I was looking into where this was sent from, but I wasn’t sure if it’d be worth it to check it out."
    hide evelyn
    show finn

    FINN "At this point, it’s a lead to something right? Maybe we’ll find something, there’s no point in not checking right?"

    hide finn

    NAR "Well… even if it’s fruitless it’s not like it would hurt to check it out, besides Finn will know that we won’t be tracked by whoever anyway."

    scene city

    NAR "We headed to the post office where Evelyn had discovered it was from, and took the train there."

    NAR "Inside we looked around at some of the stuff around, while other customers were doing things, and looking at the possible stamps you could get."

    NAR "I noticed one of them had the same symbol we’ve seen on other items for this cult. So I got the other two and showed them."

    show finn

    FINN "So that’s confirmed that this place is related to them in some way right?"
    hide finn
    show evelyn

    EVELYN "You two are already on their radar right? Why don’t you two hang out outside of here, and I’ll ask around here. We probably shouldn’t loiter here anymore anyway right?"

    hide evelyn

    NAR "After exiting the building, and finding a place nearby to relax for a moment."

    show finn

    FINN "Man, did not expect her to be so enthusiastic about joining the Starseekers!"
    hide finn
    show jesse

    menu:

        "Excuse me.":
            hide jesse

        "The what?":
            hide jesse

        "Is that… what you’re calling us.":
            hide jesse

    show finn

    FINN "Well, we’re trying to find and figure out the guiding comet right? I thought it was a cool name."

    JESSE "..."

    FINN "Either way, I’m glad she’s with us, because you getting all interested in this stuff alone would be far too suspicious."

    NAR "That and I wouldn’t have gotten involved in all of this alone to begin with… Finn begins to look around and finds a newspaper on a stand and starts flipping through it."

    FINN "Oh huh, they’re announcing the executions publically in this issue, saying they’re going to happen tomorrow morning."

    NAR "He turns it around, and I can clearly see the faces of the perpetrators."

    FINN "You don’t think the cult would be up to doing anything to stop that right? Don’t see them risking themselves to save people they’re technically not involved with."

    NAR "Still though, for something like that to be announced publicly, it’s not like there would be any way to get out of it unless there were already people on the inside, and in that case, what could we even do?"

    NAR "We’re just three people without anything special. It was around then that Evelyn was catching up with us from inside."
    hide finn
    show evelyn

    EVELYN "Hey… wasn’t able to get anything out of them, seems like they’re not involved, or I’m not as insightful as I thought I was…"

    EVELYN "But this got me thinking, how many people in the city might actually be able to get us information about this stuff, I’m sure I could look around as ask around, while you guys focus on staying more on the stealthier side of things."
    hide evelyn
    show jesse

    menu:

        "You can’t just trust everybody.":
            hide jesse
            show evelyn
            EVELYN "That’s not what I’m doing."

        "Sure you’ll be safe?":
            hide jesse
            show evelyn
            EVELYN "It’ll be fine."

        "that’s a great idea.":
            hide jesse
            show evelyn
            EVELYN "Thanks."

    EVELYN "Don’t worry about me, I’ll make sure to not get into any trouble. But I guess that’s everything for today right… it sucks we weren’t really to get anywhere."

    JESSE "It’s fine, it doesn’t seem like much has been happening either, One step at a time is the best we can do… it’s not like anyone else has actually tried to do this besides…"

    EVELYN "Yeah… but don’t worry, I’ll definitely have something about those paper scraps you got by tomorrow, I’ll call you."
    hide evelyn
    scene date_transition

    NAR "I decided to give her a few of the scraps, so she could have them physically with her while researching, then we said our goodbyes and decided to all head back separately."

    NAR "The rest of the day proceeded as normal."

    NAR "SOME TIME AFTER MIDNIGHT"

    scene apartment

    show cathee

    NAR "Cathee appears outside in the apartment complex, and she’s in front of the door to Jesse’s apartment."

    NAR "Cha-clink"

    CATHEE "Oh it’s been far too long since I’ve had to resort to that, but lockpicking is still so easy!"

    hide Cathee

    call new_day("Wednesday, 19th July 1922")


    scene room

    NAR "The morning was like any other, except with the hope of finding out what Evelyn could figure out about the paper scraps. Hopefully she didn’t ask around anywhere too dangerous."

    NAR "The expected call arrived a bit earlier in the afternoon than I had thought, and Evelyn’s voice was not what I heard… A mysterious deeper feminine voice commandingly spoke to me."

    Mysterious "You have 20 minutes to come to the university, if you ever wish to see Evelyn again you’ll bring the book with you as well. -click"

    NAR "Wh… how did this happen? I can’t go can I? I have to go, they clearly already know I have the book, there’s no reason… wait they only want the book, as in they don’t know about the pen or key?"

    NAR "Are they unimportant? I thought they were keeping an eye on me because of the pen? I don’t have time to think about that right now, all that means is that we would still have something against them even without the book, and I can’t just let her…"

    NAR "No, it’ll be fine, 20 minutes is plenty of time to get to her using the train, it’ll be fine, think about it on the move."

    NAR "I began to get dressed, and grabbed the book, Maybe I could contact Finn! Wait, how would I do that? He still doesn’t have a phone or anything… damn it…"

    NAR "Getting dressed, and leaving the building, passing the plants and the complex cat, I was able to catch the train only a few moments before it was about to leave, and he took a seat."

    scene train

    NAR "Okay… Can’t do much else now except try and figure out what’s going on… Why do they want the book, is there something about it that… wait a second…"

    NAR "There’s a bookmark in the book, that was never there before, who could have put this in here? Did Sara do it, no that’d be impossible she doesn’t know about it right? maybe it’s some sort of message or signal… "

    NAR "Before opening it to check, I checked my surroundings to guarantee it was safe to open it in the public of the train."

    NAR "From the looks of it, no one seemed too suspicious, not that I could really know any tell of who would be out for me, besides if they’re expecting me to go to the library why would the-"
    NAR "Why is he here?"

    NAR "Moving through the train, going to cars further ahead, was a man whose face I had only seen once before, the previous day in the newspaper. He was moving quickly along the train cars."

    NAR "This is our only possible lead. How is he free? I need to follow him now, there won’t be a chance for this ever again."

    NAR "After going up a few cars, he stops and peeks through the window. It appears that the car is incredibly empty. Only two others are in there besides the man in question, dressed in strange robes."

    NAR "The two of them pull out basic leather books, each of them… with the symbol of The Guiding Comet! The man begins to panic and takes a step back."

    NAR "Suddenly, an explosive fire begins to emanate from the two books they’re holding, and they begin to make strange motions. They’re trying… to blow up the train?! But what about!? Wait then…"

    NAR "Quickly, how do I survive"

    show jesse
    #LOOPING ONE
    label book:
    menu:

        "Use the book":
            hide jesse

        "Pull the emergency break":
            hide jesse
            "It’ll still explode!"
            jump book

        "Run away":
            hide jesse
            "But to where?!"
            jump book

    NAR "It’s from the cult too isn’t it? That’s right, if they’re going to try and explode the train with theirs… maybe I can do something with this?"

    NAR "I whip out the book and open it to the bookmark. It appears that a large sigil, similar to those on the scraps of paper, is drawn into the book… it would have had to have been with that pen, but… there’s no time to analyze!"

    NAR "A random scrap of paper falls out of the book. Quickly scrambling to get it, and pick it up. Which reads"

    NAR "‘Hi! Read the English phrase on the back aloud, or, I guess it’s not really English, really the closest th-’"

    NAR "I quickly turned it around, and read what was essentially gibberish on the back of it in a panic. The light from the train car ahead of me glows brighter, and a few of the other passengers freak out over having noticed it too."

    NAR "What happened next was too surreal."

    NAR "A glowing silver mist began to form in front of me, and behind in the small cone shape that formed around most of the traincar."

    NAR "And then everything was engulfed in fire."

    NAR "Which caused rocks to collapse over the subway, and the train was torn apart in an explosion."

    scene date_transition

    NAR "..."

    NAR "I woke up, in the rubble of a collapse of the train, but other than being incredibly tired…"

    NAR "it appears that I was physically incredibly fine, and many passengers from the cars behind me were also in much better shape than what you would expect, but none of them completely unscathed like myself."
    NAR "After a moment, and collecting myself, I sat up and grabbed the book that was lying near me and tucked it away. Then I noticed a woman walking towards me. In an unforgettable blue, Cathee."

    show jesse

    menu:

        "Oh… you made the call didn’t you?!":
            hide jesse
            show cathee
            CATHEE "Guilty as charged."

        "Did you set this up?!":
            hide jesse
            show cathee
            CATHEE "technically, no."

        "Why are you here?!":
            hide jesse
            show cathee
            CATHEE "Wanted to make sure you were okay of course!"

    CATHEE "What you’ve just experienced first-hand is the cover-up for what else happened today, but now a lot less didn’t needlessly die. Good job on that front."

    CATHEE "But anyway, you should start thinking of a cover for why you were here, and by the way, Evelyn’s fine, I was at the university around the same time you got that call, so I checked on her."

    CATHEE "I’m sure you’re pretty tired, so I’ll let you be. But congratulations, and good luck!"

    hide cathee


    NAR "I wanted to try and stop her, but she just ran off down into the rubble of the train… I was tired and unfocused."

    NAR "The rest of that day was a blur. And I was able to get off from being approached by the police or medics by pretending to be a bystander and answering enough to get out, because in the end I was relatively fine… despite how tired I am now…"

    NAR "I found a payphone and called the university library to check on Evelyn, and she was fine."

    NAR "I struggled to walk back home, which wasn’t too far luckily because of how fast this all happened… I don’t know what time I fell asleep… but it was early… And I have… work… tomorrow…"

    NAR "The rest of the day proceeded as usual… but I was very tired."

    #CHAPTER 1 - END


    jump chapter2_start
