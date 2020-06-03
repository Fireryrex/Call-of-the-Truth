# Chapter 5 begins here

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define RAY = Character("Ray", color="#CC0000", what_color="#660000")
define ACOLYTE = Character("Acolyte", color="#990066", what_color="#660066")

label chapter5_start:
    $ current_chapter = 5

    #CHAPTER 5: Birth of Dream
    scene room
    centered "{size=+30}CHAPTER 5: Birth of Dream{/size}"

    call new_day("???, ??? ???")
    #THE EXACT DATE IS NOT REVEALED IMMEDIATELY, IT TRANSITIONS TO THIS STRAIGHT FROM CHAPTER FOUR.

    NAR "It was already almost May. To think it would take seven years for me to make real progress against them…"

    NAR "No matter, I can think about all I’ve missed out on once this is over, I’ve known I couldn’t back out of this since I started."

    show city_night

    NAR "Driving down an empty street in Scotland, in the dead of the night, the only sound that can be heard in the silence is the putter of my motorcycle."

    NAR "The air was nice up here, but I can’t help but miss home, even if it is pretty similar. I had been around these parts before, but the secrecy and importance of this is starting to fire me up."

    NAR "Upon reaching an unlit corner, I had reached where I was supposed to meet him, it was marked with a small sticker of a bird on the corner."

    NAR "I get off the motorcycle and walk down the alley, leading me to a stairway on the side of one of the apartments, going up to see the man leaning against the wall. Perfect. Hopefully this trip won’t be a waste of time."

    show linden

    LINDEN "So, you’ve actually decided to come and go through with this Stout?"
    hide linden
    show ray

    RAY "Please, no need to be formal, you can call me Ray. Besides, we're partners in crime at this point right? You’re an interesting fellow Linden, but I do trust you."

    hide ray
    call new_day("Friday, 29th April 1921")

    show linden

    LINDEN "ha, well, this partnership as you say is of great interest to me as well."
    hide linden
    show ray

    menu:
        "Did you bring what I asked for?":
            hide ray
            show linden
            LINDEN "Yup, it’s all right here."

        "Come on, let’s make this quick.":
            hide ray
            show linden
            LINDEN "Alright don’t worry, I’m sure I wasn’t followed."

        "So…":
            hide ray
            show linden
            LINDEN "Yeah yeah, I’ve got what you need."

    NAR "He pulls out a small envelope from inside his large cloak and hands it over. It seems to be filled with a fairly thick stack of papers."

    LINDEN "I’ve written everything you need to know inside, it would take too long if I were to say it all right now."
    hide linden
    show ray

    RAY "You sure are risking a lot here though. What happens when you’re caught? I can only guess, but I assume you’ve dealt with some traitors yourself in the business."
    hide ray
    show linden

    NAR "His expression changes for a split second, maybe it’s worry, maybe something else, but he soon brings back the grin he’s been holding the whole conversation."

    LINDEN "I wouldn’t be worrying about me in this scenario. I have my own backups for if this guys awry. You’ve got to look after yourself more."
    hide linden
    show ray

    RAY "You should know more than most that I can’t do that."
    hide ray
    show linden

    LINDEN "Your confidence is contagious… but what exactly is your plan with this anyway, you know you won’t be able to use it right? Unless you truly mean to leave things to that boy."
    hide linden
    show ray

    RAY "...If everything so far is true, I won’t drop to that idea so quickly, and either way, it’s not like he’ll be alone."
    hide ray
    show linden

    NAR "He reaches back into his cloak and pulls out the key that was stolen from me. After turning it over a few times, he tosses it to me."

    LINDEN "Then you get this to him yourself."
    hide linden
    show ray

    RAY "Oh, putting in extra work on your own end huh?"

    RAY "Thanks."
    hide ray
    show linden

    LINDEN "I know what you said, but I don’t think I can take your words at face value. You know what I’ve done, and I’m sure you don’t fully trust me. Just think of these actions as a sign of good faith."
    hide linden
    show ray

    menu:
        "Thanks for that.":
            hide ray
            show linden
            LINDEN "Truthfully it’s not much."

        "Well, See you tomorrow.":
            hide ray
            show linden
            LINDEN "I’ll be ready."

        "How many strings did you have to pull?":
            hide ray
            show linden
            LINDEN "Just a couple webs."

    LINDEN "Get some sleep Ray, you’ll need the energy."

    NAR "He gives me a slight nod, and starts to head up to the roof."
    hide linden
    show ray

    RAY "Anywhere you’d recommend, don’t know many places your friends haven’t tainted up here?"
    hide ray
    show linden

    LINDEN "You’ll be fine. But try two blocks up from here."

    hide Linden

    scene date_transition

    NAR "I went back and started off to find a hotel to prepare for the night to come, I had a lot of reading and scouting to do before I was ready to tackle this break in."

    call new_day("Saturday, 30th April 1921")

    show ray

    NAR "The notes and information that Linden had left me was surprisingly more simple than what I expected, then again I guess it is fairly normal work as usual for someone of his caliber."

    NAR "Must have had to master the way of being clear to subordinates that he clearly knew they weren’t the smartest, but it does seem like he has some respect for me, I never worked too well in groups personally, but I get the appeal."

    NAR "What was lined out was theoretically simple:"

    NAR "There are three entranceways accessible and available, but it seems as if the majority of his plans point to me taking the entrance in the bakery either way. "

    NAR "Inside I can follow a map he has displayed here to bring me to the study, Linden is very clear about things here, and this is the most important part of this infiltration anyway."

    NAR "There will be five minutes while there is no one in the study, and that the mystic item they’re preparing will be inside for a short time."

    NAR "It’s been locked away for some time, but with the recent revelation with the pen they’ve been making steps to begin their plans once again. Which is why they’ve been quite antsy ever since I took that from them."

    NAR "Linden mentions that he is not directly a part of the sect that is focusing on dissecting the powers of that book… but we both know it’s incredibly important to the events surrounding six years ago…"

    NAR "Either way he doesn’t say it but I’m sure there’s other important things I need to get from in there."

    NAR "Those five minutes will be incredibly important, and afterwards there will be more coming to check on and take those items from the study. They’ll be on high alert."


    NAR "From there, assuming I have not gotten the attention of the entire base, I can follow Route A, and get out of one of the main exits, specifically the one near the main ritual hall, which will have a much higher density of enemies."

    NAR "However once I take the book I can start a distraction by making notice of it, and collapse one of the exit paths yourself. That exit path will lead out near a cathedral."

    NAR "Since I would be relatively safe from that exit, he will meet you there after another ten minutes."

    NAR "During that time however he will be waiting for me at the end of exit route B, which is if the plan does not go well I can escape from and meet up with me there."

    NAR "Route B has me follow a different secret path that is accessible from the hall outside the treasury. They will collapse it assuming I’m faster than them, but he’s sabotaged it only a little, I will still need to prepare to dig a little bit."

    NAR "During the collapse there will also be a break in the sewer wall that will lead you to a manhole that I can get out of."

    NAR "he said as a foreword, if I do fail in this, but acquire the items, he will find a way to get them out however he can, he mentions he’s almost invested in this almost as much as I am, if I could believe that."

    hide ray

    scene city_night

    show ray

    NAR "Step one was the simplest when you’re given the exact details and landmarks. Well technically that was step two, step one was just wait for nightfall."

    NAR "It was a little scary how accurately he was able to describe so many secret pathways and common areas the cult uses to get to it’s hideouts and to send messages."

    NAR "After arriving at the bakery, it would have been tempting to get something, but I’m here when it’s closed for a reason… I pressed my hands against the wooden wall that he had depicted in the notes and it gave way."
    hide ray
    show ray_tome

    NAR "Finding myself in a pitch black room. I pulled out my smaller spell tome and casted a quick light spell, to hold a globule in my hand."

    NAR "Small enough that I could close my hand to get rid of it for a moment if I needed to hide. Carefully putting the wooden board back in place as well before continuing down the passageway."

    scene cultish

    NAR "Keeping an eye on the time, I finally made it to the entrance to the actual cultist base underneath the city, It had gone into and out of a sewer system, and it’d be amusing if the smell is what messed this up for me."

    NAR "But a quick cleanse spell was a much safer way to remove that issue. Part of the reason why the halls were quieter this evening was because of the importance of this mystic item."

    NAR "Which I believe they have many currently hard at work to progress their goals other places in this city, and in the other parts of the united kingdom, from what I gather the cult is large, large enough to spread to this many locations."


    NAR "But they are still spread relatively thin compared to other malicious groups, that’s partly why their officers travel so much."
    hide ray_tome
    show ray

    NAR "Although it does seem like Linden could have been a bit more accurate on how many people there’d be here…"

    NAR "I’m cutting it really close on time with having to dodge and hide from people just moving around the place, but it was that big of an issue to follow the map."

    NAR "I could have attempted to use invisibility, but it’s only truly effective on the untrained eye at my level, so anyone here would be able to see it plain as day."

    NAR "I got to the door, then waited until the person left, which marked the five or so minutes I would have in Linden’s schedule, I quickly got behind and caught the door before it fully closed from the man exiting."

    NAR "Inside should be magical tools and… a person… Someone was sitting down writing at a desk, thankfully back towards the door. If it’s more active than what Linden had planned for…"

    NAR "I may not have the full five minutes, which means there isn’t a second to waste."

    NAR "I quickly casted a Silence spell to mute everything in the room. It wasn’t long before the man noticed that his writing wasn’t making any noise."
    hide ray
    show ray_gun

    NAR "I pulled out my revolver. He stood up and began to turn around."

    NAR "I pulled the trigger."

    NAR "He hit the desk as he fell down. All was completely silent."

    NAR "His blood had stained multiple papers on the desk, but sitting in the middle, open was a book, that the blood seemed to glide and drift off of, as if it was covered in a barrier of some sort."
    hide ray_gun
    show ray

    NAR "Looking closer, I could feel the aura that radiated from that book… if I was looking for something, it would explain a great deal of the events from six years ago… after all it was incredibly powerful spells…"

    NAR "I couldn’t stand there thinking for too much longer, I was on a severe time limit, and I have to use this opportunity the best I can."

    NAR "The room was cluttered with boxes of scrolls and glyphs, making it incredibly cramp, and my quick checking of everything left my bloody boot prints all over the floor."

    NAR "Checking the desk first it seems like there are mixes of scrolls that encompass many languages, but the most notable, and seemingly the head of their research, was one written in egyptian Hieroglyphics which I grab along with the book."

    NAR "If they cannot find the pen magically, and this book is related to it, then they probably can’t track it either, but if I take anything else specific from them that is magical that’d be a risk."

    NAR "Tt's time consuming but safest if I were to just copy the spells down onto paper. I copied a couple that could be interesting while scanning the rest of the room."

    NAR "I do notice one more scroll hidden away, that seems to be of the similar ancient style as the tome and egyptian notes itself."

    NAR "The way it was positioned seemed to indicate it was important, but perhaps for later in their plan, or perhaps it’s something they don’t want affecting their plans…"

    NAR "I finished the spell I was scribing. Rewind, something that is incredibly potent, and if the history is correct, that book will actually make it more useful than a few moments."

    NAR "I reach out for the scroll, but hear footsteps approaching the door."

    NAR "I can’t let this be a mystery to me… I quickly grab it and begin to scan it… it’s immensely powerful… The power to control an ancient being, the mastery… no even just the ability to cast this is… I need to-"

    NAR "A searing pain, as a spark of fire is shot at my hand, that spills off into the room. It falls from my hand, and the wooden floor begins to ignite. It’s a spell scroll, it’s fine, I have other worries at the moment."

    NAR "Two acolytes of the cult had opened the door and began to attack me, my left hand now quite singed was effectively useless, but it looks like the escape part of the plan was a go, and not the simple one."

    NAR "I dived over behind the desk, and pulled out my spellbook. They’re going to shatter this desk, I need to be quick. Very quick."
    hide ray
    show ray_tome

    NAR "I cast a haste spell on myself, and put away the book."
    hide ray_tome
    show ray_gun

    NAR "opting for my revolver. With the extra speed from the spell, and my reckless abandon taking them by surprise I roll out of cover and shoot one of them in the neck."

    NAR "I miss and only hit the other in the arm, which causes his spell to miss me, but it still detonates and blows all the books and scrolls around and off the shelves, while aggravating the fire."

    NAR "Three bullets. Another shot, which kills the acolyte. Two bullets. The gunshots echoed throughout the halls."

    NAR "I can’t exactly reload with one hand, and besides it’s time to focus on getting out of here right now, before the haste wears off."

    NAR "Now then… which escape route would be best…"
    hide ray_gun
    show ray

    label route_b:
    menu:
    #LOOPING ONE
        "Where I came from.":
            hide ray
            NAR "No, they can collapse that one."
            jump route_b
            #Loop

        "Route A.":
            hide ray
            NAR "It might surprise them to take the approach that would work if I had been unseen, but that’s still a huge risk."
            jump route_b
            #"Loop"

        "Route B.":
            hide ray

    show ray_gun

    NAR "Yeah, that’s probably my only option at this point… I only have two shots available, but I can make those count."

    NAR "I make a dash towards the tunnel, and it seems like I’m being tailed by one other who enchanted himself, they wouldn’t collapse it if they trusted this guy to take me out, and I can’t risk that."

    NAR "I won’t be able to kill him if we’re both moving easily… but he’ll still be able to throw some sort of magic at me. Luckily all the magic quick enough for that is relatively lower in power…"
    hide ray_gun
    show ray_tome

    NAR "I throw the gun down the hall, and pull out the spellbook. I turned around preparing a quick counterspell to stop whatever he was going to send my way at that moment."
    hide ray_tome
    show ray_gun

    NAR "I roll back dropping my spellbook and fire a shot at him, hitting center mass, which should be enough to slow him down."

    NAR "Damn, having one working hand is an incredible hassle right now. I holster my gun and grab my spellbook before continuing my escape."

    NAR "As Linden had planned, there was the exit he had mentioned to my right, which I was able to dash into with the last of my hasted abilities."

    NAR "As I proceeded along swifty, I was able to escape, and within the ten minutes that Linden would wait at this exit, I only had a few minutes before midnight anyway, but it seems like I’m safe for now…"

    hide ray_gun

    hide cultish

    call new_day("Sunday, 1st May 1921")

    scene city_night

    show ray

    NAR "The pain in my hand was starting to numb, but since I finally had the time, I wrapped it up quickly in a handkerchief I had. Climbing a ladder with one hand was also a new experience I wish I had never had to do."

    NAR "I almost felt more scared of falling off than being in a cultist base! Getting up and out, it seemed safe enough, this part of the city was mostly dead like the night before."
    NAR "There’s a sudden tap on my shoulder, and I quickly spin around and find myself face to face with Linden. I breathe a short sigh of relief."

    RAY "You couldn’t have gotten my attention without giving me a heart attack?"
    hide ray
    show linden

    LINDEN "Sorry, but let’s be quiet for now, since you’ve chosen the loud option already. Come along, follow me. Walk and talk."

    LINDEN "So, did you get what you came for?"
    hide linden
    show ray

    menu:
        "Yeah, thanks to your directions.":
            hide ray
            show linden
            LINDEN "Good to hear, I’m glad my work paid off."

        "Possibly…":
            hide ray
            show linden
            LINDEN "As long as you’re satisfied with it"

        "I think so, but you were a bit off.":
            hide ray
            show linden
            LINDEN "I’m sorry I’m not perfect, would you have preferred to use your own discretion?"


    LINDEN "In the end, you’ve now taken both pieces from us, that is sure to greatly discomfort those of us in power, I know for a fact it’s going to make my work significantly harder."
    hide linden
    show ray

    RAY "I’ve got a lot of questions about what I found that I’d like to ask you about but…"
    hide ray
    show linden

    LINDEN "I’m curious, but I’m afraid the time for that may not be for a while, they’re already on their way to try and resolve this, and I should start leading that cause sooner rather than later. We’re not working against forgiving people."

    hide linden
    show ray
    RAY "You’ve got that right… well then, when we meet again, I’ll tell you what I figured out about all of it."

    hide Ray

    NAR "We arrived at my motorcycle, it was high time to get out of this place and not come back for quite some time."

    show linden

    LINDEN "Ray, I’m a firm believer in covering all of the outcomes. I don’t know what you’re planning, but do you truly believe he’s up to it?"

    hide linden
    show ray

    RAY "...We don’t know the full story of how it happened six years ago. I know he can do it."

    RAY "However that’s just the easy way to end all this, we won’t actually need to resort to it. However if that case you're worried about does happen… he’ll be up to it, he has to."
    hide ray
    show linden

    LINDEN "That confidence will get you killed."
    hide linden
    show ray

    RAY "That’d happen regardless."
    hide ray
    show linden

    LINDEN "Goodbye Ray."

    hide Linden

    NAR "I get back on my motorcycle, and give Linden a short nod. I drive off into the night. The journey ahead is going to be pretty tiresome, so I don’t have time to get caught up too long here."

    NAR "Truth be told, I am worried about that. Knowing how much Linden is thinking into it however… is actually pretty reassuring though, I feel like it’s impossible that we’d lose in the end."

    scene date_transition

    hide ray

    NAR "I drove throughout the night, my next stop was actually Dublin, Ireland. My goal was to check with Finn and then make some progress on the cult’s activities over there… then after all of that is finished…"

    NAR "I think I’ll actually be able to go home, but even then, It’s not like I would be able to do much. I’d be in hiding. London is their main base of operations, and their true leader rarely ever leaves."

    NAR "Only that upper brass knows the specifics of the events that happened six years ago, everything me and Linden know is from my investigation."

    NAR "The only reason why their activities from back then would become a focus of them again is that there’s something that’s happening now that they either lost, or didn’t have back then."

    NAR "They are also being a lot more careful since they know the mistakes they made back then, but they couldn’t have planned for my interruptions."

    NAR "They have to plan around them, which makes it much easier to get an idea of their direct goals, at least when related to me. I eventually came upon a rest stop motel sort of place."

    NAR "I had to take a much longer path just to avoid any potential ambush locations, and it was already morning…"

    scene city

    show ray

    NAR "Finally after a whole night of driving, It’s relatively close to the port as well, so I can board a ship early tomorrow after getting some rest, besides a ship I can trust isn’t available until later according to Linden’s information."

    NAR "Even though it’s still really early in the day, I really just want to find a place to get some sleep, all that action and spellcasting is starting to take its toll, but the relaxation of the drive here was quite nice."

    NAR "I set down my motorcycle and purchased a room to stay in. As I walked out and went to the stairway and noticed a woman leaning against the wall near the entrance, smoking a cigarette."
    hide ray
    show cathee
    NAR "Her outfit seems to be pretty shady, and the way she’s eyeing me, almost as if she was waiting for me."

    NAR "I walk past her trying to ignore her and just start to walk up, expecting an interruption, which swiftly comes."

    CATHEE "Well don’t you seem to be in a rush."
    hide cathee
    show ray

    RAY "I’m just an exhausted guy looking for a place to stay, or am I wrong in thinking that’s what this place is for?"
    hide ray
    show cathee

    CATHEE "Hmmm I wonder why a guy like you is driving all through the night, Running from something perhaps?"

    CATHEE "The wife found out about your mistress, or did you just finish a job assassinating the consigliere of a gang…"

    CATHEE "Or perhaps you’re a spy with regrets from the war haunting your every step that you’re trying to outrun."

    CATHEE "Or you’ve messed with some powerful cultists."
    hide cathee
    show ray

    menu:
        "How’d you guess?":
            hide ray
            show cathee
            CATHEE "I feel bad for your wife then."

        "You have quite the imagination.":
            hide ray
            show cathee
            CATHEE "Oh you wouldn’t believe it."

        "Not today for most of those at least.":
            hide ray
            show cathee
            CATHEE "Ohohoho, the scattershot guess always works wonders."

    CATHEE "This little page you had me real confused though, you don’t talk or walk like an egyptian at all!"
    hide cathee
    show ray

    RAY "I’d recommend not sticking your nose into other people’s business like that, it’s not the safest."
    hide ray
    show cathee


    CATHEE "Well, I love doing that, so that sense, everything is my business."
    hide cathee
    show ray

    RAY "Okay… what do you want."
    hide ray
    show cathee

    CATHEE "So I’ve gotten your attention!"

    NAR "This woman… she knows a lot more than what she’s leading on to, and she’s a certified pickpocket at that."

    NAR "I thought this place would be safe, but apparently not. Can’t panic here, It seems like she just wants to talk, and I’d rather make an ally here than anything."

    CATHEE "Oh, no need to be so cautious, I’m just here to talk with you, enlighten you perhaps? The name is Hecate."
    hide cathee
    show ray

    RAY "Like the witch?"
    hide ray
    show cathee

    CATHEE "What does that even mean anymore Mr. Cultist Killer"
    hide cathee
    show ray

    RAY "The name is Ray Stout."
    hide ray
    show cathee

    CATHEE "Okay."

    CATHEE "what does that even mean anymore Mr. Cultist Killer Stout?"
    hide cathee
    show ray

    RAY "Well then, what is it you’re interested in talking about, you’ve already swiped some of the notes I haven’t even investigated too well myself."

    NAR "She looks at the paper with the egyptian writing, and begins to speak."
    hide ray
    show cathee

    CATHEE "They say that one must work for power, only he who is capable of saving themselves, he who denies others, he who is hidden from all…"

    CATHEE "And only he who can break from fate is worthy of the power to change the will of the gods."
    hide cathee
    show ray

    RAY "Seems the person would need to be pretty selfish and contradictory. Is that what it says?"
    hide ray
    show cathee

    CATHEE "Huh? What no, I was just reading this while I said that. Oh! Would you mind if you showed me what spells you got?"
    hide cathee
    show ray

    RAY "Can you just tell me what you’re after?"
    hide ray
    show cathee

    CATHEE "Okay so I don’t know everything you know. My best guess is that you have the Black Tome and also picked up some stuff from there as well, so I’m just wondering how much of it is actually useful."
    hide cathee
    show ray

    RAY "Huh, fine, but you’re also saying that you can translate what that page says too right? I’ll trade for that information"

    NAR "I gave her the scraps of spells I copied after she agreed."
    hide ray
    show cathee

    CATHEE "Ooh, you got like two important ones, nice! That will probably make things go a lot smoother in the future."

    CATHEE "Now then, the paper, it’s nothing really. It’s just talking about the ancient Sphinx that controlled and manipulated most of Egypt, and how that Black Tome was incredibly important for some mortals to gain some freedom of control over it."

    CATHEE "But if you want me to tell you the truth, like 90\% of them were just being controlled by the Sphinx and were used as figureheads to make it’s control even more effective."
    hide cathee
    show ray

    RAY "I’m going to start assuming all of this is relevant somehow, but why are you telling me all this?"
    hide ray
    show cathee

    CATHEE "Well… you see there are some pretty powerful people planning some pretty big things, as you can guess from six years ago."

    CATHEE "They’d much prefer a picture without you or your kid’s involvement, but honestly I think it’s a much prettier picture if that didn’t happen."
    hide cathee
    show ray

    RAY "Would you mind telling me how all this is related? My best guess is something about the Guiding Comet wanting to control this Egyptian Sphinx god, and the first thing you said relates to what they need to do that, but I’m confused at what you meant by ‘I found two important spells.’"
    hide ray
    show cathee

    CATHEE "Well, you see, not all spells are created equal, you know that, and some spells require it so that they are attuned to in a sense, basically you need to be able to cast a certain few spells before being physically able to cast that higher end stuff."
    hide cathee
    show ray

    RAY "So in order to revive their god, they would need to cast these spells from the book first before being able to?"
    hide ray
    show cathee

    CATHEE "You’re on the right track… but no, not really in the slightest. The spell they’d use for that has no importance with that. Unless they wanted to actually try and control the guy."

    CATHEE "But even then that’s not really a possibility unless you have that Tome, and even then… There is a different spell though, one that does require that attunement, one with the power to end everything. One that was used years ago in Egypt."

    NAR "The one spell I saw probably… So it was tucked away because it was dangerous to them?!"
    hide cathee
    show ray

    RAY "I feel like you’re almost being too clear with me. What are you expecting me to do with this information?"
    hide ray
    show cathee

    CATHEE "Your fate has been sealed."

    hide Cathee

    RAY "..."
    hide ray
    show cathee

    CATHEE "Your part of this ends in Ireland."
    hide cathee
    show ray

    RAY "So, you expect to tell me this and for me to still go."
    hide ray
    show cathee

    CATHEE "Yes, because the only way we can win this is for you to go."

    NAR "She hands me back the things she was looking at."

    CATHEE "You know what you have to do, I’m sorry it has to end this way, it’s partially my fault…"
    hide cathee
    show ray

    RAY "Who’s to say the fate you speak of is true? Didn’t you say we had to break free of determinism for this?"
    hide ray
    show cathee

    CATHEE "haha, I'd be really happy if you surprised me. I’ll provide the steps we need to set this all up. I’d rather not bore you with the details."
    hide cathee
    show ray

    RAY "Because I won’t be a part of them right."
    hide ray
    show cathee

    CATHEE "I’ll tell you if you get out of this, besides you’re allowed to know. If you want to know, the plan is pretty flawless if I do say so myself. Goodbye Ray."
    hide cathee
    show ray

    RAY "I’ll see you in London Hecate."

    NAR "She was lying. She’s worried about this plan. It’s clear to me now though, Jesse… He’s able to use the pen, it reacted too strangely with him…"

    NAR "Which means he’s probably the only one who could effectively use this… I need to hope he can do this, and for that, I need to get this to him."

    NAR "Even still, the more I do in Ireland before her warning comes to pass, the better. I can contact Finn and have him continue with the plan, he’ll be able to help Jesse."

    hide Ray

    NAR "Realistically I have no reason to trust her. However it seems like she’s been involved with all of this for quite some time, to physically get involved after knowing so much…"

    NAR "it has to be genuinely important to her, that carefree personality hides what she really is."

    NAR "Either way, it’s not like I can run from this, they’ll find us eventually, and in the long term Linden’s cover won’t last more than a year or two."

    scene date_transition

    NAR "That was certainly one Bizarre woman. Nothing else unusual happened that day, and I got some much needed rest. Tomorrow I sail to Ireland."

    call new_day("Monday, 2nd May 1921")
    NAR "I woke up far too early, and would have to wait to catch the ship, but I spent that time going over what I had actually taken."


    show ray

    NAR "The translation of the Egyptian text also helped some, at this point I’m making claims under the assumption that Linden and Hecate are truthful, which I like to think I’m good at reading people…"

    NAR "But should never discredit the possibility. I can probably assume the other papers and other languages that were scattered across near the book were all different accounts of their deity in different countries."

    NAR "Six years ago, they were probably attempting that attunement process so they could control their god when they would choose to summon it. Ideally we could just disrupt their goals entirely…"

    NAR "Perhaps completing this attunement in a sense will give us the upper hand against them… Checking the book itself, there is a torn page near the front, and a dozen or so dulled out spell notes in the back…"

    NAR "Presumably the spells that were casted six years ago, comparing them to the ones I had copied down, they were mostly different…"

    NAR "although they did share some similarities, but all the symbols used in this book are completely different from what I’m used to normally, it’s on a different level from anything else I’ve seen used."

    NAR "What matters is that I’ve taken it from them in the end. My hand is also now at least usable, if not a bit bloody painful."

    NAR "After a bit, I got some breakfast then headed to the port. It was easy enough to purchase a ticket, I had prepared everything for this a long while ago."

    scene boat

    NAR "Shame I feel so refreshed and energized, just to spend most of the day on a ship. I settled in, and went to the room I got on it."
    NAR "While it did have a great window to see the ocean, it was incredibly boring, and I decided to go about and see what else is happening on the ship, need to check if everything is going smoothly of course."

    NAR "Not going to take that threat too lightly, Hecate…"

    NAR "Although technically I’m safe on the boat, it’s not Ireland yet right."

    NAR "Checking on the other travellers on the ship, I’d like to thank my paranoia as I wouldn’t have been able to find the cultists without it."

    NAR "I don’t know how, but I saw a group of at least four, could be others blending in better, chatting."

    NAR "I gaze off, giving them some opportunity to ignore me, it could just be a generic group of suspicious people, could be unrelated to me, but also it’s not like this is the first time Linden’s information is wrong."

    NAR "It also seems like some of them are talking and interacting with the actual crew of the ship… Bloody hell they’re all in on it aren’t they…"

    NAR "While they’re preoccupied I’ll get back to my room and formulate some sort of plan… Which shouldn’t take too long, it seems like they’re about to spread out along the ship."

    NAR "An opportunity arises as the main group I notice is offered meal assistance for the journey, which I take…"

    NAR "However it’s very easy to tell if you’re being tailed when you know who wants to tail you. The lead I have is enough, and whenever I’m not in sight I jogged just enough to make a lead."

    NAR "I got to my room, I have maybe a minute to figure something out. Part of, if not the entire crew is in on it, This boat is no longer an option."

    NAR "My gun is loaded, but fighting a group like that without cover is suicide. I can just get off of it… but then I can’t take the book, or I could, but the scraps would get wet, and they’re not going to let up on targeting me…"

    hide Ray

    NAR "Okay, I’ve decided how I want to play this."

    NAR "I gathered together the book and some of the items, grabbed the guidebook off a shelf, which luckily was also slightly black… Running out of time… I may not get the chance to contact Jesse…"

    NAR "I… don’t know what to say… I wrote a quick letter to him, but knocking on the door made me have to end too quickly. I hid them away in this room, and held the fake in my burned hand as best as I could. They broke in."

    ACOLYTE "Mr. Stout, I’m afraid your journey on this boat is at an end."

    show ray

    RAY "Yeah, I guess you’re right…"
    hide ray
    show ray_gun

    NAR "I pulled out my revolver, and they all began preparing defensive spells, and I shot twice at the window behind me to make it easier… to jump through!"

    hide ray_gun

    scene date_transition

    NAR "Crashing into the waves below, and diving to stay out of range of them… If they really have the crew on board, they might take the time to scout the area for me."

    show ray_tome

    NAR "I put away my gun, and dropped the decoy book, pulling out my own spellbook to find the water breathing spell… As I began to swim further down."

    hide Ray_tome

    NAR "Ditching my coat entirely, to go faster. They know how long the spell lasts… So I need to find a way to lose them before that runs out…"

    NAR "I quickly swim back to the boat itself and grab on to follow with it… the thought of letting go and falling into the blades is not a happy thought and I’m not sure why I need to be thinking about that right now…"

    NAR "Eventually I was correct, they started to turn the boat around to more precisely where I dropped, they had thrown furniture to mark where I was originally, but I was able to let go of the boat and let them run back there at their leisure."

    NAR "As the spell wore off, I went back to the surface, but had to start swimming away from where the boat's path could see… the last thing I want is them coming back and running into me."

    NAR "I’m… glad… I… had so much… energy today… because…"

    NAR "I NEED… TO SWIM… THIS… ENTIRE DISTANCE."

    NAR "ohmygod…"

    call new_day("Tuesday, 3rd May 1921")
    NAR "It took… an entire day… but that’s a beach ahead… please for the love of everything… let this end…"

    show ray_end

    NAR "I swam to shore and laid there for… for not long enough… I got up and started to try and get some water out of my clothes… my boots… my socks… I liked that coat, but it dragged me down so much. Ah… and now I’m all sandy."

    NAR "Okay, the first step in all of this, I need to contact Finn and get him to find the book I hid on the ship, then he can eventually get that to Jesse."

    NAR "I guess she was right huh, I don’t see any way that they aren’t going to be able to find me in a few hours, that boat would have gotten there yesterday."

    NAR "I’ve finally pissed them off enough for them to want to kill me huh, but I guess I still have won huh, as long as I make that call to Finn."

    show city

    NAR "It took a bit of walking but I made it to a city, and found a phone booth. Going inside I called up the military base I knew Finn was at and was able to get him on the phone."

    RAY "Hey Finn… it’s been a while huh."
    hide ray_end

    FINN "Mr. Stout!? I, I’ve been good, how about you, it’s been a while hasn’t it."

    show ray_end

    RAY "Hey, I hate to ask a favor after not talking to you for so long but… A boat should have come into the port in Dublin yesterday, in room 108 I left a package."

    RAY "I need you to get it, and I need you to get it to Jesse. You have to be careful, and secretive too, it’s a very sensitive subject."

    hide ray_end

    FINN "Sir, are you alright? This sounds too serious, what’s going on."

    show ray_end

    RAY "It is quite serious, but don’t worry about me, just do this for me, but just be safe too… Yeah, it’s the cult."

    NAR "A fancy black and silver car drives up, and parks next to me in the phone booth."

    hide ray_end

    FINN "Mr. Stout is-"

    show ray_end

    RAY "I’ve got to go Finn. Tell Jesse… I’m sorry."

    NAR "I hung up, and a man exited the vehicle, he looked like a butler, and motioned for me to get in."

    NAR "I got out of the phone booth and leaned against it… I’m way too tired for a fight."

    RAY "Do you really think I’m about to make the cover up that easy for you?"

    NAR "The butler is motioned to get back into the car, and then a man gets out. He was… elegant… calm…"

    Mysterious "If that is what you wish. I can at least show you thanks with a quick death."

    NAR "He pulls out a thin pistol, I try to react, but I’m too slow."

    hide ray_end
    scene date_transition

    NAR "Bang."

    #CHAPTER 5 - END


    jump chapter6_start
