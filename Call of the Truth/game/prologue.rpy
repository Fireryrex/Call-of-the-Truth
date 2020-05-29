# Prologue begins here

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define CATHEE = Character("Cathee")
define JESSE = Character("Jesse Stout")
define FINN = Character("Finn Marsh")
define SARA = Character("Sara Harper")
define EVELYN = Character("Evelyn Baker")
define ISAAC = Character("Isaac Goodwin")
define LUKE = Character("Luke Macthorn")
define Mysterious = Character("???")

label prologue_start:

    #PROLOGUE: Birth of a Nightmare
    #DATE - Thursday, 22nd June 1922
    call new_day("Thursday, 22nd June 1922")
    scene room

    NAR "My alarm blared, but what woke me up was the sunlight coming through the windows hours later. I regretfully got out of bed to start the day, at what appears to be 1pm from looking at the clock."

    NAR "I got dressed and walked out to the empty living room, which is still cleaned from the last time she came over, solely due to its lack of use."

    NAR "I check the mirror…"

    show Jesse

    NAR "Same old me… gonna lose track of myself one of these days, anyway."

    hide Jesse

    NAR "Checking the refrigerator, it was filled with a couple of items that friends had brought over since they didn’t have one themselves, but to the point, there wasn’t any milk. Digressing to turn the stove on to cook some eggs for a decent meal."


    JESSE "I swore there was something I’m forgetting about today, besides grocery shopping…"

    NAR "Pushing some of my old university books off to the side of the table, it seemed like she was searching through some of my stuff on the shelves again… or she’s just interested in whatever I was studying before, not that it matters now."

    JESSE "Was it the interview? No… that’s next thursday."

    NAR "I Finished my meal, and started cleaning up… might as well put those textbooks back in the study, not like I’m gonna need them for a long time anyway."

    NAR "Opening up into the study, the mess of papers and books stacked or open remains in the same position it was since that time last year…"

    NAR "Right… it’s been over a year since dad died, and I made this mess in the first place…"

    NAR "Placing the books and closing the door. As the door clicks into place, a loud ringing sound begins, from the home’s telephone. At least he left me with the annoying technology too…"

    JESSE "Who could it be this time? Wait, was I expecting a call? *yawn*"

    NAR "Walking over and picking up the phone he heard an incredibly familiar voice."

    show Finn

    FINN "Hey man, been a while huh. This is the right number right? Haven’t used one of these here yet haha"

    hide Finn

    NAR "Oh. Oh god how could I forget this? This was FINN Marsh, an old friend I’ve known for most of my life. He's about 4 years older than me and even fought in the great war not long ago."

    NAR "Last time we saw each other was for a little bit after the war, but then he got another job not long after. We met through a case my dad was investigating involving his mother, and it turned out he was a great guy."

    NAR "He was finally able to leave his latest assignment not a few days ago, and was coming home, and he thought it’d be fun to catch up."

    show Jesse

    #[CHARACTER CHOICE]
    menu:
        "How’ve you been?":
            show Finn
            FINN "Doing quite well myself, happy to be back."

        "I’m sorry, I forgot about today.":
            show Finn
            FINN "Oh, it’s all good, don’t worry about it."

        "Sorry, wrong number":
            show Finn
            FINN "Good to see you haven’t lost your humor!"

    FINN "I figured you might have overslept so I wanted to give you some time to wake up, but I’ve gotten back and settled in."

    FINN "Want to meet me at the park? I haven’t been there in ages. I’ll be waiting, don’t know how much time I’m allowed on this thing."

    scene apartment

    NAR "Leaving the apartment, locking the door, and heading down the steps passing the floor filled with flowers, and the complex’s cat. It’s an average spring day in London."

    show Cathee

    NAR "At the bottom of the stairs rests a woman I had never seen before. Leaning against the wall in a long dark blue coat and hat, smoking a cigarette. It’s certainly unusual to see someone loitering around that I don’t recognize, and the outfit is…"

    NAR "interesting to be sure… but it’s nothing to be worried about."

    Mysterious "Late for your first venture with destiny are you?"

    NAR "Was she talking to me?"

    Mysterious"There are many different parties interested in what’s going to happen. Just know I’m rooting for you in particular"

    show Jesse

    #[CHARACTER CHOICE]
    menu:
        "Do I know you?":
            show Cathee
            Mysterious "Of course, we’ve just met haven’t we?"

        "Are you talking to me?":
            show Cathee
            Mysterious "Either that or the cat which followed you a bit"

        "{i}Ignore her{/i}":
            show Cathee
            Mysterious "Isn’t that right kitty… you like him too don’t you"

    Mysterious "Start enjoying your life again… and one last thing, what’s this one’s name *pointing at the cat*"

    NAR "It didn’t have a name… at least not until my dad named it…"

    JESSE "His name is Jimmy, and you don’t happen to have one too?"

    CATHEE "A great name, and… call me Cathee."

    NAR "Quite possibly the least trustworthy stranger I’ve ever met, but… friendly enough… Doesn’t matter much."

    NAR "Anyway the fastest way to Hyde park would be the tube, I wouldn't want to keep Finn waiting too long anyway."

    scene park

    NAR "Arriving at Hyde Park. Its familiar beautiful greenery is a sight that always made me feel better, but it’s still been a while since I’ve come here by yourself, even if it’s still to meet with someone."

    NAR "It appears some construction is being done, appears they’re trying to make an underground railway nearby?"

    NAR "After a little wandering around the park, I heard a whistle that the two of us had made to get each other's attention years ago. Even after not seeing him for 2 or so years, it’s easy to recognize him."
    NAR "He waves at me and I walk over to the bench he’s been sitting at. He’s friendly as ever…  but it’s impossible to hide the side effects of war… or just any battle for that matter, but I doubt any sees it besides me."

    show Jesse

    #[CHARACTER CHOICE]
    menu:
        "You back for good?":
            show Finn
            FINN "Hopefully."

        "When is the next time you leave?":
            show Finn
            FINN "Hey man, don’t worry on the end of this just yet."

        "Happy to rest for a bit?":
            show Finn
            FINN "Should be longer than that."


    FINN "This time should be for a while… at least for me, I can see some others getting dragged back into things if they escalate anymore, but I think they realize I need a longer break than normal."

    FINN "I’m only out because of some agreement the higher ups made, shame too was kind of enjoying Ireland if it wasn’t for the whole focusing on my job thing."

    FINN "Much happier to be back here though… it’s been far too long since we could just hang out together like normal… not that I think it could ever go back to how it was."

    show Jesse

    #[CHARACTER CHOICE]

    ##>Ireland?
    #[Yeah, been some drama between this one group and us… but it’s not a big deal]

    ##>Normal huh…
    #[Well, you know. The two of us at least, besides we can drink again.]

    ##>I can’t even call you though.
    #[I’ll work on getting a phone too then, but it works out for me]

    show Finn

    FINN "Anyway, you can guess what I’ve been through, but what about you? How’s uni been? Learn anything interesting?"

    NAR "About that… I haven’t been in university for about a year now either… I couldn’t keep up with my studies or have the willpower for any of it since dad passed away."
    NAR "Since then I’ve still kept up with a few friends, but it’s mainly just been Sara who’s kept me focusing on things after I dropped out. I figured he’d be curious about it… but I’m not sure I even want to talk about it too much with him."

    FINN "Ah… no I don't worry about it. I can only imagine what it's like for you… I haven’t really had the time for it to fully sink in myself… about… your dad…"

    NAR "Another strange thing that struck me today… partly during this conversation it seems like he’s been distracted? As if looking for someone. Or… watching out to make sure someone isn’t here."

    show Jesse

    #[CHARACTER CHOICE]

    ##>Are you okay?
    #[Huh? Yeah, of course. It’s a different kind of pain, but I’ve dealt with worse.]

    ##>No one really understands…
    #[yeah, i get that… It is different between us too.]

    ###>(Try to spot something yourself)
    #THIS ONE IS NARRATION NOT A REPLY #[It seems like normal crowds… but th-]

    show Finn

    FINN "There was something else I wanted to talk to you about, but I’ve just remembered something I need to do to actually have a place to stay tonight haha."

    FINN "Gotta say, readjusting to being back from across the lake has taken some getting used to, having to relearn all the new all the secrets of the city."

    FINN "Especially it feels like how both our lives have been uprooted recently. Besides we both need something to distract us from the world. I’ll call you sometime later, we have stuff that just the two of us can talk about right, catch you later"

    show Jesse

    #[CHARACTER CHOICE]

    ##>See ya
    #[Yeah, I’ll try and talk to you soon.]

    ##>Just don’t call on saturdays!
    #[What? Do you actually do stuff on them now? leaves]

    ##>What are you…?
    #[Oh I completely forgot about the time before calling you, sorry about that, they’re gonna kill me if I don’t get there on time haha]

    hide Finn

    NAR "What was up with him…"

    NAR "that was the most obvious message I’ve ever heard… but why say it now? Did he actually see the thing he was worried about? Was he worried about something or was he just waiting for a signal?"

    NAR "Did I mess this up by being late? What's going on, either way it’s clear he was trying to say…"

    show Jesse

    #[CHARACTER CHOICE]

    ##>He hid something at the park
    #[continue]
    ##>He hid something in ireland
    #[No, that can’t be it…]  #[loop]
    ##>He’s taken something that was hidden here
    #[No, that’s not right.] #[loop]

    hide Jesse

    NAR "So he hid something, and he wants me to take it? But couldn’t just show it to me because there was someone…"

    show Jesse

    #[CHARACTER CHOICE]

    ##>Watching him
    #[No, loop]

    ##>Watching Me
    #[Yes]

    ##>I’m the distraction
    #[No, loop]

    hide Jesse

    NAR "And if I’m being watched, he’s taking the bait to give me some freedom from whatever it was by being a distraction? But why am I even being followed?"
    NAR "It doesn’t make much sense… but… there was that weird woman earlier… is she watching me? No that would have been too noticeable."
    NAR "It’s safe to say I don’t have enough information as to who, or why I’m being followed, should just accept that I am, and that Finn knows that. But what do I do when I get whatever is hidden there?"

    show Jesse

    #[CHARACTER CHOICE]

    ##>Keep it secret between us
    #[Yes]

    ##>Get the police involved
    #[No, loop]

    ##>Keep it secret between those I trust
    #[No, loop]

    hide Jesse

    NAR "He seemed pretty clear to just keep it between the two of us… but the possibility that it’s something I can do on my own means I could trust others with whatever it is unless…"
    NAR "I don’t know what's happening because I shouldn’t trust those around me… Well first of all let's dig up whatever this was. Now where would it be?"

    show Jesse

    #[CHARACTER CHOICE]

    ##>Check the tree’s limbs
    #[No, loop]

    ##>Check inside the tree
    #[No, loop]

    #>Dig near tree
    #[Yes]

    hide Jesse

    NAR "Digging up near the roots it’s easy to find the patch he would have hidden something in. Pushing off and dusting off an object wrapped in parchment, and sealed with a wax stamp…"

    NAR "with my name written on it… If the idea is that I’m being watched constantly, it’d be best to open this now, while I can hope that Finn is distracting them."

    NAR "Opening it up is a worn black furlike book, with an illegible title, with distinct red accents along the letters, and a brass key with a cracked ruby jewel in the hilt. And a letter written by… dad…"

    NAR "‘Hi Jesse, I can’t imagine what you’ve been going through if you’re reading this… I don’t have much time, and I’m sorry.’"

    NAR "‘My failures are soon to become your burdens, I only know that you’ll be able to make it through without me. It pains me that you will be dragged into what I alone have discovered. My only regret is that I failed, and that I couldn’t spend time with you…’"

    NAR "‘and I’m sorry that I don’t know what or how to say what you need to hear right now… It’s hard when you only have a few minutes to try and say everything for the last time right? Make your own decisions, only you can finish this.’"

    NAR "‘I love you. Yours respectfully, Dad’"

    NAR "Why… why is it so… what does Finn know, he had to have gotten this from him right? And what are these? There was a locked box in the hidden compartment of my dad’s study… maybe that my next best bet to see if he has anything more to say for himself?"

    NAR "Your death has already caused me enough problems… But it seems you don’t care about those troubles… only about the ones you devoted yourself to."
    NAR "It doesn’t matter though, this was probably an accident… he died in an accident… What do I have to do with anything? If it's just to satisfy his worry I’ll open up that box back home."

    NAR "And now this strange book. Opening it up and flipping through the pages… the front half is all blank, with the cover page torn out, but then in the latter dozens of pages are incredibly dull and worn pictures and symbols that mean nothing."

    NAR "Wow. Thanks dad. Placing the items into a coat pocket, and cleaning the mess of digging it up, I got up and started to leave the park."

    NAR "...I should get out of here before Finn runs out of time in doing… whatever he planned."

    NAR "Deciding to take the train back… the shifting faces of the crowd, but no one looks like they could be suspicious… Besides why would anyone be interested in me after what happened."

    NAR "I was a tag along at best and a hamper to the investigations at worst when I was doing anything important with dad. Was never interested in trying to pick up his work, why would anyone be looking in to me in something he was involved with."

    NAR "It’s not like they could use me against him, he’s dead. Either way, the worry from this should all be figured out if I can just talk to Finn again and get him to clarify some things.. Right.

    scene apartment"

    NAR "Returning to the apartments, the strange woman wasn’t waiting by the stairway this time… she’s got to be involved with what's been happening in some way?"

    NAR "What she said was too cryptic to not be related to this mess I’ve apparently been in. Either way, the same boring and calm building lied ahead, going back up to the top floor to get into my room, when outside the door I noticed her."

    NAR "I wasn’t expecting her to show up today, just another strange occurrence to add to the pile apparently. And she’s holding… grocery bags? I knew I needed to go out and get food eventually but did she just grab me some stuff without asking?"

    show Sara
    SARA "Oh I was wondering where you’ve been, don’t worry I haven’t been waiting long, figured maybe you were just still sleeping into the wee hours of 4pm again."

    NAR "...I don’t even know what to think, this certainly isn’t too out of the usual for her. I’ve known her since senior year of high school, she ended up joining the theatre club I was in at the time and we got along from there."

    NAR "She didn’t end up going to uni, and just got an easy enough job through her family’s connections."

    NAR "so she hasn’t been stressed with much work since and has been hanging out with me more often since I dropped out… It’s probably some form of pity but it helps. But at this point… I’m not ev-"

    SARA "Sorry for the confusion, I didn’t say I’d be coming at all today… but some things have come up, and I was wondering if I could just steal the couch here for a little bit? And sooo…"

    SARA "if I’m gonna be here for a little bit I figured I’d get the food and stuff to not worry you any… and besides I know how low you were on stuff last time I was here…"

    SARA "and I know you wouldn’t have gone out and gotten anything."

    NAR "She is a good friend… it couldn’t hurt, and it’s not like it’s the first time she’s stayed over at my place."

    NAR "Besides, maybe I could ask for tips to get rid of any nerves the day before I go to that final interview, she was the one who introduced me to the job anyway, plus she works there."

    JESSE "Sure, you can stay, but what’s up?"

    NAR "The least I need to do is act as I usually would… I still don’t have any information."

    NAR "Everything is related to my dad’s death… and it’s apparently enough for Finn to go out of his way to hide this, I should treat things as if I’m constantly being watched by someone looking to know I found these things."

    SARA "I’m glad you’re okay with it! Honestly I’m not sure what I would have done if you had declined, but it’s nothing too important, wouldn’t want to worry you with it"

    show Jesse

    #[CHARACTER CHOICE]

    #>You can tell me.
    #[Yeah…]

    #>Household rule, no secrets
    #[Oh is it now?]

    #>I’m more worried if I don’t know
    #[Ah.. um..]

    show Sara

    SARA "Well… it would probably be a lot easier for us both if I just told you now huh. My parents are not exactly happy with each other in the slightest and it’s been getting significantly worse everyday…"

    SARA "I really just wanted a place to escape from that for a while, so I’m not sure how long I’ll actually end up wanting to stay here."

    SARA "If I become too much I can try and find another place to stay at for a while… But I figured you need the company anyway."

    show Jesse

    #[CHARACTER CHOICE]

    #>I’m sorry about that
    #[thanks, but it really isn’t a big deal]

    #>Feel free to stay until it dies down
    #[Thanks, that’s a lot less to worry about for me]

    #>Have you tried stopping it?
    #[It’s not that simple…]

    show Sara

    SARA "I know it’s not really for me to say that I dislike my family to you… considering… no I’ll just stop there."

    SARA "Enough about that, I’m assuming you haven’t eaten have you? Genuinely I’m happy I can rely on you for times like this, and don’t forget I can help you out too."
    hide Sara

    NAR "SARA RANK 1/7"

    NAR "I let her inside, and she put away the groceries she bought, I wouldn’t be lying if I said I was excited to have her cook instead… my meals haven’t turned out too great recently."
    scene room

    NAR "After getting settled back home, it might be a good idea to clean up… if someone was watching from a distance they wouldn’t notice the subtle things, like the dirt on my shoes back when I dug up the package."

    NAR "But now if I go out and it’s someone within the apartment complex, it would be something they could connect back to Finn’s message. But why was he encoding that message anyway?"

    NAR "It’s not like anyone was close enough to hear it, he could have just said it directly… unless he’s just doing it to be extra cautious… unnecessary but I’d see why he would do it… unless even the birds are against me in this crazy world?"

    NAR "No, too crazy. The possibility that Sara is in on it? No she would have been buying the groceries and deciding to come over during the time I was at the park."

    NAR "And even if she was somehow she wouldn’t have noticed the dirt if she didn’t know about the park in the first place which should be impossible."

    NAR "Again assuming a sane world where the birds are not against me."

    show Sara

    SARA "By the way, what were you up to earlier today? Not usual to see you out and about on your own… unless you meet someone cool?"

    NAR "Wait. No that’s just a normal question, of course she’d be curious, it’s not like I showed I was bringing anything back with me…"

    show Jesse

    #[CHARACTER CHOICE]

    #>I was at the park.

    #>I was with an old friend.

    #>I was just walking around.

    show Sara

    SARA "Oh yeah! I remember you mentioned something about a friend coming back from deployment or something today? That’s cool, it’s always nice to catch up with someone after a while."
    SARA "Did he bring anything back for you from wherever he was? Oh wait no he was military… I doubt it’s ever really a vacation for them… Well I won’t pry too much between you two, haven’t met him myself even."

    NAR "It was just a normal enough day past that. But if she’s gonna be staying here… Unless I completely trust her I can’t really try and look into that key my dad’s given me"

    NAR "The rest of the day was normal enough, with Sara around."

    hide room
    #DATE - Friday, 23rd June, 1922

    scene room

    NAR "The day progresses as usual, without any of the complications of anything that happened yesterday. I can’t seem to make much progress into the book or key…"

    NAR "but nothing’s happened with them for the past year, I can think about that when the opportunity arises, besides, if there is something bad happening, nothing has happened yet, if I just keep things normal, they’ll stay normal."

    NAR "You can’t force me into your work dad."

    NAR "The phone begins to ring in the afternoon. Not used to it being a daily occurance. Sara picks up the phone."

    show Sara

    SARA "Hello, Stout residence, who is this.     Hmm…  mhmm, okay one second"


    SARA "Yeah it’s someone asking to speak with you, might be an old professor or something? Sound professional."

    hide Sara

    NAR "Walking over and picking up the phone, it’s an unfamiliar voice…"
    NAR "Wait, no. Just one that i’ve heard, but not someone I ever really talked to before. It’s the person who has replaced my dad after he died."

    ISAAC "Hello, this is Isaac Goodwin, I’m not sure if you remember me"

    NAR "I assured him that I did."

    ISAAC "Well… I know you don’t really want to hear much from me, but I just thought you might want to know some final things that have come up about your old man’s case…"
    ISAAC "yeah it’s supposed to have been closed a long time ago, but I couldn’t just let it sit. Would you be able to meet me near the station on Sunday?"
    ISAAC "It’s not exactly things I can explain over the telly, and besides I think you’d want to see it for yourself."

    NAR "Sunday… that’s the 25th… I have a mentorship program that Sara introduced me to on those days, that’s been really helpful to have."

    NAR "And at this point I feel like I need to get some things off my chest about this… if I can figure out the right way to allude to it."
    NAR "I informed him that I already have plans on that day, not because it’s sunday, but because of the mentor thing twice a month."

    ISAAC "Ah, I see. Well I’ll try and call you next time my schedule is free. I really want to talk to you specifically about all this."

    NAR "My dad died in an accident last year, on a boat and it wasn’t too long until authorities stopped looking into it and just judged it as a fatal accident of the crew…"

    NAR "It took me a while to believe that, but there’s no other feasible reason for any of that to have happened, so I’ve just accepted it at this point."

    NAR "My dad was a well renowned private investigator, he would travel occasionally and I would go with him sometimes. The only case he didn’t solve was the one he was on when he died…"

    hide room

    NAR "The rest of the day proceeded as usual…"

    #DATE - Saturday, 24th June 1922

    scene room

    NAR "If I want to actually look into this thing with my dad I need situations where I’ll be completely alone, which has only now become a complication, even if unintentionally by Sara."

    NAR "I can just wait and do my own things on the days where she works, which are Monday, Tuesday, and Wednesday."

    NAR "The weekends are almost assuredly a no go to do anything, whoever is watching me has even more excuses to not be at a job of some kind… assuming their job isn’t just to watch me."

    NAR "Besides today I have that interview, apparently I’ll be completely fine too, especially since Sara has recommended me, and the other introduction and interview I had went incredibly well."

    NAR "I don’t exactly need the extra money, but I know if I don’t do something on my own eventually dad’s money will run out…"

    NAR "I’ve already wasted too much doing nothing with my life since his death, so whatever will be happening can hopefully work itself around my work schedule too."

    NAR "The interview went exceptionally well for that place and I’m going to end up working on Thursdays, Fridays, and Sundays."

    NAR "I doubt I’ll be able to get much done on those days either due to work, it seems like it’ll actually take a decent amount of effort, but if Sara can get through it I should be fine too."

    NAR "My tasks are mostly working with customers and other stock and various busywork, while she’s in a different division entirely. The building itself is pretty large, with a dozen or so floors."


    hide room

    NAR "I was pretty tired after all that though, and the rest of the day proceeded in this new normal."

    #DATE - Sunday, 25th June 1922

    scene room

    NAR "Today was going to be my first meeting with Luke Macthorn in quite some time. He had been unavailable for about a month and a half, and we only ever meet twice a month anyway."

    NAR "But I never felt it was helping me too much… well that’s not entirely true. Luke is a mentor who I met from a suggestion from Sara."

    NAR "Someone who I could talk to and try to put into a figure I could actually share things with ever since my dad died."

    NAR "It only started up around March this year… but I’ve never been too sure if I wanted to keep talking with him…"

    hide room

    scene cafe

    NAR "I met up with him and we went to a local Cafe near the building today, we would tend to go wherever he felt, but he has offered to meet anywhere I’d suggest if I had ideas about it, which… I have not."

    NAR "He was calm and friendly, how I remembered, but I don’t remember too much from when we used to talk before, it was only a handful of times."

    show Luke

    LUKE "Good afternoon Jesse, it’s been a while hasn’t it. How have you been?"

    show Jesse

    #[CHARACTER CHOICE]

    #>Fine.
    #[Similar to the fine weather outside.]

    #>Good.
    #[I’m happy to hear that.]

    #>Not the best.
    #[Of course, trying times for us all.]

    show Luke

    LUKE "I’m glad that you’re willing to come back to this after our break and talk to me."

    LUKE "However something that I want you to know, is that whether you’re honest with me or not doesn’t matter too much, It’s about being honest to yourself."

    LUKE "I’m sorry I couldn’t make any time over here, but I was out of town for some time. An old friend of mine who lives in Glasgow recently lost his son."

    LUKE "I was with him and his family up until the funeral was held… But I don’t want to bore you too much about that, it’s all been settled now."

    LUKE "‘It did make me think about you though, the mirror of my friends' situation I mean. However I won’t bring that up dauntless you do."
    LUKE "In other news, I had heard that recently some soldiers were finally recalled from Ireland, and if I remember correctly, wasn’t a good friend of yours in that group, have you been able to meet up with him?"

    show Jesse

    #[CHARACTER CHOICE]

    #>Yeah.
    #[That’s good.]

    #>No.
    #[You should get around to that.]

    #>Not for too long.
    #[It’s good you could see him though.]

    show Luke

    LUKE "It’s not often you make friends like that if what you’ve said about him is true. I wouldn’t let yourself keep growing distant now that he’s finally back."

    LUKE "You never know when he might be pulled away with that job."

    LUKE "I don’t mean to say he’ll ever be gone forever. I know you already probably can’t stop thinking about your dad with him, considering how the two of you met originally."

    LUKE "I guess what I’m trying to get at is that this is an opportunity for you to finally talk to someone you know you can trust completely, and to possibly start over with him."

    LUKE "I’m sure he still cares about you as a friend after all this time."

    NAR "What he’s saying isn’t wrong… but the way the situation has evolved… The first thing he came back to see me about involved my father, but I do trust him."
    NAR "If there are bad things really happening around me, I’m glad he’s looking out for me…"

    NAR "We chatted for a bit longer, but maybe it’s because I’m more open or thinking about what's happening in my life again, but I feel like I’ve grown closer to Luke."

    NAR "LUKE RANK 1/10"

    hide cafe

    NAR "We said our goodbyes, what was left of the day proceeded how it normally would."

    #    [CEVELYN-WIP] DATE - Monday, 26th June 1922
    #        Today could be a day to try and look into that key… *brng Brrrng*
    #        As the phone begins to ring for another complication, could it be Mr. Goodwin again? Doubtful, it’s a Monday, probably just got slammed with all the weekend’s worth of news.  Picking up the phone…
    #        #>Wrong number.
    #        #>Who’s this?
    #        #>Can I help you?
    #    Enter Evelyn Baker
    #        "Hi, it’s Evelyn, I wanted to ask if you’d be interested in…
    #    (Actual Description and activity for the two of them, nothing big, just to introduce the character as a book guy, and set her up as a potentially important character when it comes to deciphering things.) Bond 1/7
    #    (I think an interesting plot line to take with him as well is to have him concerned about JESSE’s studies, and try to get him to essentially test out of classes because he knows how smart he can be.)

    #    Fades Out
    #Day Changes to
    #DATE - Tuesday, 27th June 1922

    scene room

    NAR "Another average morning, where the thoughts of all the mysteries go on… The morning is the same as ever with the new flatmate, but she gets ready and goes to work in the morning as usual."

    NAR "Leaving me free to do anything in the security of my own place… But I’ll have time to confront all that later, it’s waited for so long, I can relax and let it keep waiting."

    NAR "No. No, I've already pushed it off too much… but my life has been fine already without getting involved in all this, I doubt much would change if I just continue to live without acknowledging it… but…"

    NAR "My thoughts were cut short by the ringing of the telephone. It was Finn"

    FINN "Hey, been a while, and yeah I’m okay. Was wondering if you’d be up to hang out again after last time!"

    FINN "I found a cool cafe somewhat nearby to your place, I’ll be waiting for you in an hour or so"

    show Jesse

    #[CHARACTER CHOICE]

    #>Not right now

    #>Wait is that safe?

    #>Wait there multiple cafes aren’t there?!

    hide Jesse

    NAR "Oh… he had already hung up… and it wouldn’t be very good of me to just let him sit there by himself. I wonder if he knows more about all of this than I do, I guess I can assume it would be safe."

    NAR "Maybe I can talk to him and figure out if I should do anything specific with the book and key, it’s not like he knew what was in the package right?"
    NAR "And he shouldn’t expect me to just get into all this immediately either…"

    NAR "But he didn’t even specify which cafe… there can’t actually be one that would be that obvious around would there?"

    NAR "He better not expect me to lose someone tailing me either when I don’t know anything. I guess I can spend the next hour finding the place."

    NAR "After looking at some maps, it turns out there really is only one notable cafe he’d like within walking distance of my place… which was actually quite surprising, then again, I do know his tastes."

    NAR "I meet up with him there, and he’s sitting at a table already, we order some food, and begin to chat."

    hide room

    scene cafe

    FINN "Sorry for calling you out of nowhere, but It’s probably gonna be awhile before you can contact me instead of the other way around haha."
    FINN "But in all seriousness I figured there was stuff we should have talked about after what happened that night, you got the thing right?"

    show Jesse

    #[CHARACTER CHOICE]

    #>The package?

    #>I don’t know what you’re talking about.

    #>Are we not being secretive?

    FINN "Oh yeah, don’t worry, part of the reason it took me so long to get back to you was I was trying to find a place that was safe from their influence, And I’m like 90% sure this place is pretty safe."

    FINN "Even if someone were to be watching from outside, there’s no way they could hear what we’re sayin. So yeah, I don’t know, er.. what was in that anyway?"

    NAR "I explained to him that it was some sort of cultish book and key, along with a message from my dad."

    FINN "Hmm. I’m not sure what I was expecting considering what I found. All I got was a message from your old man worried that he was running out of time, and to look in some secret compartment of a ship that would hopefully still be docked at Dublin."

    FINN "I hate to say… But I think I’m more in the dark about all of this than you are in truth… I only started looking into things after realizing the message I got from him was one of the final messages he ever sent…"

    FINN "Which is when I realized there are people watching over you. Well, not over you in a good way you know. Do you know if we can get any leads out of the things in that package?"

    FINN "I’m ready to help you however you need, it’s the least I can do"

    NAR "He seems pretty interested in this… I don’t think I should bring up how uneasy this is making me, I wouldn't want to burden him with that, he’ll still try and help no matter what."

    NAR "I told him that I have an idea, but haven’t had the chance to do it… Well that’s not entirely true… But there’s also the investigator who’s taken my dad’s place, who has been trying to contact me."

    FINN "Huh, yeah if this is as serious as it could be, you probably just want to live a normal life, make it so anybody who’s trying to make sure you don’t figure it out thinks you haven’t."
    FINN "I’d definitely try to follow up with him, he’s not your dad, but he’s probably the most involved person in this mess than anyone we’d know."
    FINN "I guess as a last thing to say… I don’t know what we’re really getting into with all of this, but I feel like I need to do something you know?"
    FINN "It hasn’t sat well with me knowing I didn’t have the freedom to do anything for a year."

    NAR "FINN RANK 1/7"

    hide cafe

    scene room

    NAR "After I got back from the cafe, it was a normal day… I could go and check out the room and see if this key works… but there’s a chance that could take a bit, and I’d rather not have Sara walk in during it."

    NAR "Should just continue to live a normal life… under these circumstances."

    NAR "The phone begins to ring again. Who could it be this time?"

    NAR "It was ISAAC."

    ISAAC "Hello, I’ll make this brief just because I’m about to leave for a bit. I’ll be free tomorrow afternoon, around 1:30pm, I understand if you’re not able to make it."

    ISAAC "If you have the time just call in the morning tomorrow and confirm with me that you’ll be coming. Have a nice day. -click"

    NAR "How opportunity presents itself… It would probably be an idea to talk to him and learn more about the overall situation before I look into whatever Dad directly gave to me."

    NAR "Well that at least sets up a plan for tomorrow, and it will probably be easy to go while Sara is at work."

    NAR "Later that night, Sara gets home, and looks exceedingly tired."

    show Sara

    SARA "Work has been… far too much recently. They better be thinking about giving me some sort of promotion with all this extra nonsense they’re throwing at me."

    SARA "Gah… The past few months have been rough with my branch of the company, and since a few of the upper roles are out of the country they’re sending most of their work to me of all people."

    SARA "That being said, I am taking off tomorrow, because I am not into continuing with all that right now. I’m sick of looking up and researching people for hours on end."

    SARA "Luckily it should clear up soonish, or at least I don’t think much else will be put onto this pile… hmmm…"

    SARA "Anyway, that being said, I was wondering if you’d be up to go to the theatre or something tomorrow afternoon? Was thinking like 1pm or something, the actual one I got tickets for doesn’t start until 1:25 though."

    show Jesse

    #[CHARACTER CHOICE]

    #>You already got a ticket?
    #[It was on the way back.]

    #>That sounds fun.
    #[Yeah, I hope it will be.]

    #>Wait, you want me to come?
    #[Figured you’d be up for it, not forcing you though.]

    hide Sara

    NAR "...Thinking about it, this is totally something I’d do if I wasn’t trying to look into the cult… which is exactly what they’d be looking for if they wanted to see if I wasn’t still oblivious right?!"

    NAR "So I should do this. Besides, the other things can wait, it’s like I was thinking about earlier, if something bad was going to happen, there’s no reason it would have waited a year just to do something now."

    NAR "Also, this’ll be fun, saw this in the paper, was a little interested anyway… "

    hide room

    NAR "And with that, the evening continued as usual, and I got to sleep."
    #DATE - Wednesday, 28th June 1922

    scene room

    NAR "Another normal, nice day. Another opportunity to look into these doubts crawling up from all around me. I’m sure Sara wouldn’t mind if I called off her thing, it’s normal to make plans?"

    NAR "Well, for anyone normal it would be… Yeah, it might not be the best idea right? I’d want to wait until it’s always going to be safe. Besides, if they’re following her too, wouldn’t it be safer for me to go with her."

    NAR "And, it’ll be fun… yeah, I can wait on all of this, or it can wait for me, that’s what it has been doing all this time anyway right?"

    hide room

    NAR "I ended up going to see the play that she had talked about the day before. We traveled to the St. Martins theatre and got inside to watch the play called ‘Loyalties’."
    NAR "I felt distracted in my thoughts watching the play, but the basic plot was about a man who was robbed, but instead of being helped, was defamed by those who could have helped him…"
    NAR "When the guilt man was found, they commited suicide, and the blame was shifted onto the man he robbed. It was enjoyable enough, but I can’t seem to stop worrying about everything going on…"

    NAR "The two of us went back home."

    scene room

    show Sara

    SARA "That was a well needed break for me… How long has it been since you went out and did something fun anyway? Hey… are you doing alright?"

    show Jesse

    #[CHARACTER CHOICE]

    #>Huh?
    #[I don’t know… you just seem less focused recently…]

    #>Yeah, I’m fine.
    #[If you say so…]

    #>Been thinking about things more…
    #[Oh, well don’t get too caught up on it.]

    show Sara

    SARA "Oh! It must be because of your mentor thing right? I can imagine he’s been getting you to start trying to think more about how everything has been for you right? Well, I won’t pry into that too much."

    SARA "And… hey, I know you probably didn’t want me to just show up and start living with you, but I’ve been doing a lot better being here than anywhere else…"

    SARA "So thanks for letting me stay. But if you ever need anything, don’t be afraid to ask, I’m willing to help you with whatever i can. Don’t be afraid to just worry about yourself first sometimes."

    JESSE "...Thanks"

    NAR "SARA RANK 2/7"

    hide Sara

    hide room

    NAR "The rest of the day proceeded as usual. I wouldn’t be able to do very much because of work the next few days, but I do have Saturdays off at least."

    #WORK - Thursday, 29th June 1922
    #WORK - Friday, 30th June 1922
    #DATE - Saturday, July 1st, 1922

    scene apartment

    NAR "While I don’t expect to make any progress on the weekends because of how easy it’d be to find out. Today is a little special, it’s the day to pay the rent."

    NAR "Walking down the stairway to the first floor, passing the flowers of the 3rd floor, and the complex cat and turning to drop off the envelope of this month's rent to the owner."

    NAR "I’ve been given reduced rates for the foreseeable future it seemed my dad and the landlord were good friends… just like seemingly everybody… treating me better just because of him."

    NAR "On the way back up, on the floor with the flower, the strange woman was there and inspecting them. And… she’s also in the middle of the stairway… completely and intentionally blocking the stairway."

    show Cathee

    CATHEE "Oh come now, don’t give me that look, take the excuse to stay and look at the flowers. Do you even know who takes care of them?"

    NAR "I did. It was an old man who lived in the room two doors to the left of the stairs. He was a nice man, but I’ve only given him a simple wave or greeting the past times I’ve seen him for the past couple of months."

    CATHEE "You know, I’m sure you recognize it too but being stuck up in your room all the time has got to be bad, a dull tool is never going to be able to crack the coconut, and when was the last time you had to think about something hard."

    show Jesse

    #[CHARACTER CHOICE]

    #>Is this a lecture?
    #[So you can still use your brain! I thought you didn’t go to those anymore.]

    #>What do you want?
    #[Well right now, to look at flowers and find that cat again.]

    #>Who exactly are you?
    #[Cathee, nothing more, and nothing less.]

    show  Cathee

    CATHEE "All I’m saying is that you may want to improve yourself too, can’t just expect your friends to drag you up from the ashes all by themselves?"

    CATHEE "And besides, maybe if you figured out how to take care of another living thing, say a plant, you’d be able to nurture other relationships too!"

    CATHEE "Just food for thought. Besides it’s not like you can get through this alone. That’s why your father failed. Anyway Bye, I’ll always be that 3rd pair of eyes on your spotlight!"

    NAR "Before I could say anything… She went up a flight of stairs and seemingly disappeared. What did she mean by… any of that… who even is she?"
    NAR "Who’s side is she on here? She ended up leaving tools to take off the plants… did she really just want to tell me to do that…"

    hide apartment

    NAR "The rest of the day continued as normal with what now seemed like a permanent flatmate."
    #DATE - Monday, 3rd July 1922

    scene room

    NAR "If there was a day to check out my dad’s study it’d be today… Although if I’m really going to commit to doing this I guess I should see when ISAAC is free considering his schedule is a lot less flexible."

    NAR "I doubt i’d get anything since it’s monday. Mine as well just wait on trying to start anything until I’m able to meet with him right?"

    NAR "It’ll probably be important in some regard to have both events happen around the same time, which means I won’t need to worry about things until I can actually get a meeting with him."

    NAR "I called and got redirected to Isaac."

    ISAAC "Oh Jesse, thank you for contacting me, are you able to make time to come meet with me? I know it must be hard on you, but I really think you need to hear this. Are you free in an hour? I’d be able to set up time for us then."

    NAR "I… did not expect that to be so easy… I can just go basically right now. Is he not focusing on his job? Am I somehow more important than his job."
    NAR "Either way it doesn’t make sense but… I guess this is where I commit to this…"

    show Jesse

    #[CHARACTER CHOICE]

    #>Yeah, I’ll be there
    #[Thank you for this]

    #>Don’t expect much
    #[I’m sure you’ll find it interesting]

    #>Better be interesting
    #[I’m sure it will be for you]

    hide Jesse

    NAR "I guess I should get a second key for Sara if I start leaving the room too much. Then again I guess it’s bad if she catches me not in the building alone again, for whatever that could mean… It really feels like an unnecessary worry."

    NAR "Taking the train to the station, I started to watch the people around me quite a bit more. Is it really a good idea in trying to get involved in this?"

    NAR "Best case scenario it’s just a new lead into the case dad was working on before he died, which already drained him of so much."

    hide room

    NAR "I met up with Isaac, and he brought me to his room. Which was originally my dad’s office in the actual station, for when he had the opportunity to use it, but he quit working directly with the police some time before his death."

    NAR "It was painful to see Isaac’s rendition of that room I remembered, but it didn’t matter. He went over and pulled out files on the original case. I remembered a few of them."

    NAR "The file on his death… was much thinner than I remembered it. Which was clarified when Isaac began to explain the bigger picture."

    NAR "He said he didn’t care what I did with this information, but he felt I should know the truth he has been investigating… or trying to investigate."

    NAR "It seems like anything involving what my dad was investigating is being hidden and covered up, and even Isaac is unable to be given permission to look into it."

    NAR "He told me my dad was investigating a cult before he died, called the Guiding Comet. He never discovered their true goals, but he thinks that my dad was really close, which is why…"

    NAR "He wanted me to know that there was still more to be done, and that the death was not an accident, but a murder."

    NAR "I knew that, but I had tried to forget, since there was nothing that could be done about it, I just accepted the fake story anyway."

    NAR "He tried to lecture me on how my Dad was thinking of the greater good when he died, but I’ve heard all of that before, and it’s never made me feel better about it."

    NAR "That was basically it though, my Dad was invested into a cult. A cult whose main location is in London, which branches spread far and wide in the country, which is why he traveled so much."

    NAR "Isaac finished the conversation by just re-affirming that he couldn’t do much of anything about it because of the shift in priorities at the workplace…"

    NAR "But he wanted me to know the truth before he had to quit looking into it, even if it’s nothing to go off of."

    NAR "Of course I want to do something… but it’s not like there’s any point to it? He died in vain, not being able to learn anything… Except he got me that book and key…"

    NAR "I bid farewell to Isaac, and left back for home. I guess it was helpful to break my misconceptions once and for all…"

    NAR "The rest of the night was normal, but I couldn’t get those thoughts out of my mind. I knew they were true… back when this happened all those months ago, I knew there was more to it."

    NAR "It just wasn’t worth it, there wasn’t anywhere to even start… it was too distracting and too hopeless… and it still is… unless…"
    NAR "Tomorrow… I’ll open it."

    #DATE - Tuesday, 4th July 1922

    scene room

    NAR "Another good morning… and another perfect opportunity to check things out without the potential of anybody peeking and spying on me, besides our age old enemy, the birds."

    NAR "Are they possibly the magic treading between improbable and impossible? Bird spies? No."

    NAR "Breakfast first. Get cleaned up, check if we need any groceries."

    NAR "We don’t."

    NAR "Sara got some 4 days ago, but really looking for any distraction before…"

    NAR "Creaking the door open to the study, after digging up the key and notebook from a place under my bed, and confirming they’ve been untouched, if Sara was with the cult she would have looked for this right?"

    NAR "But… I know exactly where this key goes. Hidden compartment in the bookshelf, that was installed directly into the apartment. No idea why they let him do this, but apparently it was paying off a favor to the old man."

    NAR "Unlocked the vault was a very simple code, my birthday, and then again reversed, 12-11-02-02-20-11-21. Unlocking the door, and seeing the small metal box stuck inside."

    NAR "The small dent I made in it was still prominent, from when I was trying to open it back around when he died…"

    NAR "The key was a perfect fit in the otherwise flat box, and a quick twist opened up and revealed the incredibl...y disappointing contents."

    NAR "It was a reddish brown pen, scraps of torn paper, all with quickly done nearly illegible sketches of symbols and a foreign language."

    NAR "It also appeared that the pen was broken… it looked like it was dripping ink, but none of it was landing on the pages below it. Reaching down and touching the pen, it opened its eyes."

    NAR "…"

    NAR "Quickly throwing the box down, the papers and the pen bounced and flew around the room before settling on the floor."

    NAR "That didn’t happen. I’m just going crazy, you know, from staying in the house too long, well no, from suddenly being more active and leaving the house right?"

    NAR "That was just impossible. Hahaha… walking up. And reaching down and gently holding the pen."

    NAR "See noth- Its eyes open again. And it’s staring up at me. I dropped it instantly, and the eyes closed as well."

    NAR "Hahahaha… what kind of… they can’t even fit in the size of… why would dad  put a magic prop in a… sealed box… only openable… by a key he had… and died with… investigating a cult…"

    NAR "Well great dad, now I have five things."

    NAR "A dented box that can only be opened by your key, that said key, A book, whose first page is torn out, with half of it blank, and half of it illegible, and pen that can’t write, and a bunch of scribbles on scraps of paper."

    NAR "Well… there’s got to be something related between them. Picking up the pen, and choosing to completely ignore that those eyes are real."

    NAR "They aren’t real. It’s a prop."

    NAR "Stop looking at me."

    NAR "Now… what can I do with this?"

    show Jesse

    #[CHARACTER CHOICE]

    ##>Stab the ruby on the key with the pen
    #[Bounces off the key, but does chip it] #[loop]

    ##>Place the scraps into the book itself
    #[Nothing happens] #[loop]

    ##>Scribble in the book with the pen
    #[Continue]

    hide Jesse

    NAR "I began trying to write in the book I got from Finn, theoretically it shouldn’t do anything since it wasn’t dripping on any of those other scraps of paper either."

    NAR "I was very wrong, and the pen was very broken, attempting to write in the book not only worked, it printed in a dark red across the pages of the tome, but it did not seem to bleed through to other pages despite how much ink there was."

    NAR "The pen wasn’t able to stop writing, and would drip ink onto the page unless you throw it in the middle of writing, but even then it’d start leaking onto it as soon as it got within a few inches of the page."

    NAR "Needed to be quick, and keep things connected to have anything remotely legible. But… that’s a lead. A book my dad got when he died, and a leaky pen he hid before he went on that trip."

    NAR "A pen that’s been right under my nose for around a year now… And now I’ve freed it if it’s creepy eyes were ever in that box for a real reason."

    NAR "But the bigger question was what did any of this mean? I’d have to look through dozens of notes, and presumably a lot of stuff that’s been taken or disposed of to get any leads past this."

    NAR "All I have are these scraps, a disgusting pen, and a book that can write it. I should be free to do some things on my own again tomorrow, but it’s safe to say that whoever has been watching me… would not be happy with what I’ve just unlocked."

    hide room

    NAR "After cleaning up the mess, and hiding things appropriately inside that box, Sare came home, and the evening proceeded as normal."

#    PROLOGUE - END


    jump chapter1_start
