# -*- coding: utf-8 -*-
"""
Expansion: A1 lessons 6-20 and A2 lessons 6-20 \u2013 full content.
Each lesson has: lesson_notes, passage, exercises, use_of_english.
"""
import json
from pathlib import Path

EXP = {
"A1": {
 6: { # My workspace
  "notes":{
   "warmup":"Every IT worker has a workspace. A good workspace is clean, safe, and organised. This matters for productivity and also for security: clean desk policies protect sensitive data.",
   "grammar":{"title":"Prepositions of place + possessive adjectives",
    "rule":"Prepositions say where things are. Possessive adjectives say who owns something: my, your, his, her, our, their.",
    "table":{"head":["Preposition","Meaning","Example"],
     "rows":[["on","surface","The laptop is on the desk."],["in","inside","The files are in the drawer."],
      ["under","below","The cables are under the desk."],["next to","beside","The monitor is next to the lamp."],
      ["in front of","facing","The chair is in front of the desk."],["behind","back of","The server is behind the door."]]},
    "examples":[{"en":"My keyboard is on my desk.","note":"my = 1st person"},
     {"en":"Her laptop is next to the monitor.","note":"her = female owner"},
     {"en":"Their cables are under the floor.","note":"their = plural owner"}]},
   "phrases":[{"phrase":"Where is your \u2026?","use":"ask about location"},{"phrase":"It is next to \u2026","use":"describe location"},
    {"phrase":"On my left / right","use":"point direction"},{"phrase":"In front of me","use":"position"}],
   "mistakes":[{"wrong":"The cables are in the desk.","right":"The cables are under the desk.","why":"IN = inside; UNDER = below."},
    {"wrong":"My cable is on his desk.","right":"My cable is on her desk.","why":"HER for female, HIS for male."}],
   "tip":"Clean Desk Policy: many offices ask you not to leave passwords on sticky notes. Lock your screen every time you stand up."
  },
  "passage":{"title":"Maria's workspace","text":"My name is Maria. I am a junior engineer. This is my workspace. My desk is next to the window. On my desk there is a laptop and a monitor. The laptop is black. The monitor is big. My keyboard is in front of me. My mouse is on my right. Under the desk there are many cables. Behind my desk there is a small shelf. On the shelf I have two books about Python. My workspace is small but clean. I like it.",
   "wc":95,"source":"Original. Inspired by workplace descriptions in VOA Learning English Level 1 (learningenglish.voanews.com, PD)."},
  "exercises":[
   {"type":"mcq","q":"Where is Maria's desk?","options":["next to the door","next to the window","in front of the door","behind the window"],"a":1,"explain":"'My desk is next to the window.'"},
   {"type":"tfng","q":"Maria has three books on the shelf.","a":"F","explain":"'Two books about Python.'"},
   {"type":"gap","q":"The monitor is ___ .","a":"big","alts":["big"],"explain":"Adjective in the text."},
   {"type":"match","pairs":[["laptop","black"],["monitor","big"],["mouse","on the right"],["books","two"]]},
   {"type":"short","q":"Describe your own workspace in 2 sentences.","model":"Model: My desk is in my bedroom. On my desk I have a laptop and a lamp."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"The cables are ___ the desk.","options":["on","in","under","next"],"a":2,"explain":"UNDER = below."},
   {"type":"cloze","sentence":"My laptop is ___ my desk.","a":"on","alts":["on"],"explain":"ON = surface."},
   {"type":"word_form","base":"OWN","sentence":"I like my ___ desk.","a":"own","alts":["own"],"explain":"Emphatic adjective: my own."}
  ]
 },
 7: { # Daily routines in IT
  "notes":{
   "warmup":"Every IT worker has a routine. The routine helps the team: everybody knows what to do and when. In many teams, the day starts with a short meeting called a standup.",
   "grammar":{"title":"Present simple + adverbs of frequency",
    "rule":"Use present simple for habits and routines. Adverbs of frequency go BEFORE the main verb, but AFTER the verb BE.",
    "table":{"head":["Adverb","Frequency","Position"],
     "rows":[["always","100%","before verb"],["usually","80%","before verb"],["often","60%","before verb"],
      ["sometimes","40%","before verb or at start"],["rarely","10%","before verb"],["never","0%","before verb"]]},
    "examples":[{"en":"I always check my email at 9.","note":"before the main verb"},
     {"en":"She is usually late.","note":"after BE"},
     {"en":"Sometimes we work from home.","note":"at the start (less common)"}]},
   "phrases":[{"phrase":"At 9 a.m., I \u2026","use":"say a fixed time"},{"phrase":"Every day I \u2026","use":"habit"},
    {"phrase":"Then, I \u2026","use":"next action"},{"phrase":"On Fridays we \u2026","use":"weekly routine"}],
   "mistakes":[{"wrong":"I check always my email.","right":"I always check my email.","why":"Adverb goes BEFORE the main verb."},
    {"wrong":"Always she is late.","right":"She is always late.","why":"Adverb goes AFTER the verb BE."}],
   "tip":"Shift handovers are critical in IT. When you leave, write 3-5 lines about open issues. The next shift saves 30 minutes of questions."
  },
  "passage":{"title":"A day in the helpdesk","text":"Pedro works on the helpdesk. Every day he arrives at 8.30. First, he reads the tickets from the night shift. Then he has a short meeting with the team at 9. In the morning he answers phone calls from users. He usually helps with passwords, printers, and Wi-Fi problems. At 1 he has lunch for one hour. In the afternoon he writes reports and checks email. Sometimes he helps new employees with their computers. At 6 he goes home. Pedro likes his job. He says: I learn something new every day.",
   "wc":102,"source":"Original. Helpdesk routine adapted from ITIL Foundation public materials (open.edu/openlearn, CC BY-NC-SA)."},
  "exercises":[
   {"type":"mcq","q":"What does Pedro do first?","options":["answers calls","reads night tickets","has lunch","writes reports"],"a":1,"explain":"'First, he reads the tickets from the night shift.'"},
   {"type":"tfng","q":"Pedro has lunch for two hours.","a":"F","explain":"'Lunch for one hour.'"},
   {"type":"gap","q":"Pedro ___ answers phone calls in the morning.","a":"usually","alts":["usually"],"explain":"Adverb of frequency."},
   {"type":"match","pairs":[["8.30","arrive"],["9","team meeting"],["1","lunch"],["6","go home"]]},
   {"type":"short","q":"Describe 3 things you do every morning.","model":"Model: Every morning I drink coffee, I check my phone, and I take the bus to work."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"Pedro ___ helps with passwords.","options":["usual","usually","usual to","is usual"],"a":1,"explain":"'usually' is an adverb."},
   {"type":"cloze","sentence":"At 9 Pedro ___ a meeting with the team.","a":"has","alts":["has"],"explain":"3rd person singular: has."},
   {"type":"word_form","base":"HELP","sentence":"Pedro is a good ___ .","a":"helper","alts":["helper"],"explain":"Agent noun: help \u2192 helper."}
  ]
 },
 8: { # Files and folders
  "notes":{
   "warmup":"On a computer, every document lives in a file. Files live in folders. A good folder structure is like a good filing cabinet: you find things fast. A bad structure wastes hours every month.",
   "grammar":{"title":"HAVE GOT + SOME / ANY",
    "rule":"Use HAVE GOT to say what you own. Use SOME in affirmatives, ANY in negatives and questions.",
    "table":{"head":["Form","Example","Use"],
     "rows":[["have got","I have got two folders.","affirmative"],["has got","She has got a backup.","3rd sing."],
      ["haven't got","We haven't got any files.","negative"],["Have \u2026 got?","Have you got the report?","question"],
      ["some","I have some files.","affirmative"],["any","I don't have any files.","negative/question"]]},
    "examples":[{"en":"I have got some documents in that folder.","note":"affirmative + some"},
     {"en":"Have you got any backups?","note":"question + any"},
     {"en":"She hasn't got the latest version.","note":"negative"}]},
   "phrases":[{"phrase":"Can you send me the file, please?","use":"request"},{"phrase":"It's in the shared folder.","use":"give location"},
    {"phrase":"The file is called \u2026","use":"name a file"},{"phrase":"Save it as PDF.","use":"instruction"}],
   "mistakes":[{"wrong":"I have some money? ","right":"Do I have any money?","why":"Questions use ANY, not SOME."},
    {"wrong":"She have got a file.","right":"She has got a file.","why":"3rd person singular \u2192 HAS."}],
   "tip":"Name your files with dates in ISO format: 2026-04-23-report.pdf. It sorts correctly and everyone in the world understands the order."
  },
  "passage":{"title":"My folders","text":"I work with many files every day. I have got three main folders on my computer. The first folder is for work documents. The second is for personal photos. The third is for software installers. In the work folder there are Word documents, Excel files, and PDFs. I also have some ZIP files for old projects. Every Friday I copy the important files to my backup drive. I have not got any files on my desktop. My manager says: a clean desktop is a clean mind. I think she is right.",
   "wc":100,"source":"Original. File management basics inspired by NIST CSF 'data classification' (nist.gov, PD)."},
  "exercises":[
   {"type":"mcq","q":"How many main folders does the person have?","options":["one","two","three","four"],"a":2,"explain":"'Three main folders'."},
   {"type":"tfng","q":"The person has many files on the desktop.","a":"F","explain":"'Not got any files on my desktop.'"},
   {"type":"gap","q":"Every Friday I ___ the files to my backup drive.","a":"copy","alts":["copy"],"explain":"Routine verb."},
   {"type":"match","pairs":[["folder 1","work"],["folder 2","photos"],["folder 3","installers"],["desktop","empty"]]},
   {"type":"short","q":"Write 3 sentences about your folders.","model":"Model: I have got a 'School' folder, a 'Work' folder and a 'Fun' folder. In 'Fun' I have many videos. In 'School' I have PDFs."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"I ___ got a backup drive.","options":["have","has","am","to have"],"a":0,"explain":"1st person \u2192 HAVE got."},
   {"type":"cloze","sentence":"Have you got ___ old photos?","a":"any","alts":["any"],"explain":"Question \u2192 ANY."},
   {"type":"word_form","base":"BACK","sentence":"Make a ___ before you delete anything.","a":"backup","alts":["backup","back-up"],"explain":"Compound noun."}
  ]
 },
 9: { # Internet basics
  "notes":{
   "warmup":"The internet connects billions of computers. Your computer is talking to servers all over the world right now. Most of the time you do not notice it \u2014 until something breaks.",
   "grammar":{"title":"Present continuous",
    "rule":"Use present continuous for actions happening NOW. Form: subject + am/is/are + verb-ing.",
    "table":{"head":["Subject","Form","Example"],
     "rows":[["I","am + -ing","I am downloading a file."],["He / She / It","is + -ing","The router is rebooting."],
      ["We / You / They","are + -ing","We are streaming a video."],["(neg)","isn't / aren't","It isn't connecting."],
      ["(question)","Is/Are \u2026 -ing?","Are you using Wi-Fi?"]]},
    "examples":[{"en":"The browser is loading the page.","note":"action now"},
     {"en":"My phone is not connecting to the Wi-Fi.","note":"negative"},
     {"en":"Are you using a VPN?","note":"question"}]},
   "phrases":[{"phrase":"I'm on Wi-Fi now.","use":"current state"},{"phrase":"The page isn't loading.","use":"problem"},
    {"phrase":"Let me try again.","use":"retry"},{"phrase":"It's slow today.","use":"network state"}],
   "mistakes":[{"wrong":"I downloading a file.","right":"I am downloading a file.","why":"Need BE + -ing."},
    {"wrong":"The router is reboot.","right":"The router is rebooting.","why":"Continuous needs -ing form."}],
   "tip":"When you report a network problem, always say what you are doing, not just 'it doesn't work'. 'The page isn't loading on Chrome but Firefox works' is 10x more useful."
  },
  "passage":{"title":"Home Wi-Fi","text":"Right now I am at home. I am sitting in the living room with my laptop. I am trying to join a video call for work. The call is at 10. But there is a problem: the page is not loading. I can see my Wi-Fi signal, but the internet is slow. I am restarting the router now. While it is rebooting, I am using my phone as a hotspot. Now I am connecting to the call with the hotspot. Tomorrow I am going to buy a new router. Ten years is too old for a router.",
   "wc":105,"source":"Original. Home networking scenario from VOA Learning English Tech Report (PD)."},
  "exercises":[
   {"type":"mcq","q":"Why is the person restarting the router?","options":["It is old","It is not working well","It is a new router","It is in the living room"],"a":1,"explain":"'The page is not loading... the internet is slow.'"},
   {"type":"tfng","q":"The person is using a hotspot from the phone.","a":"T","explain":"'Using my phone as a hotspot.'"},
   {"type":"gap","q":"The router is ___ now.","a":"rebooting","alts":["rebooting","restarting"],"explain":"Continuous action."},
   {"type":"match","pairs":[["now","at home"],["problem","slow internet"],["solution","phone hotspot"],["tomorrow","new router"]]},
   {"type":"short","q":"Describe what you are doing right now in 2 sentences.","model":"Model: I am studying English in my bedroom. I am sitting at my desk with my laptop."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"The router ___ right now.","options":["rebooting","is rebooting","reboots","reboot"],"a":1,"explain":"'right now' \u2192 present continuous."},
   {"type":"cloze","sentence":"I am ___ a video call.","a":"joining","alts":["joining","attending"],"explain":"-ing form."},
   {"type":"word_form","base":"CONNECT","sentence":"I have a slow Wi-Fi ___ .","a":"connection","alts":["connection"],"explain":"Verb \u2192 noun: -tion."}
  ]
 },
 10: { # Writing safe passwords
  "notes":{
   "warmup":"Your password is the key to your digital life. A weak password is like a key under the doormat. In IT, we say: your password is your identity.",
   "grammar":{"title":"Imperatives + SHOULD / SHOULDN'T",
    "rule":"Use imperatives for direct instructions: 'Use a password manager.' Use SHOULD / SHOULDN'T for advice: 'You should use 2FA.'",
    "table":{"head":["Form","Use","Example"],
     "rows":[["Verb.","direct instruction","Use a passphrase."],["Don't + verb.","stop action","Don't share your password."],
      ["You should + verb","advice","You should enable 2FA."],["You shouldn't + verb","negative advice","You shouldn't reuse passwords."]]},
    "examples":[{"en":"Use at least 12 characters.","note":"imperative"},
     {"en":"Don't write passwords on paper.","note":"negative imperative"},
     {"en":"You should change default passwords.","note":"advice"}]},
   "phrases":[{"phrase":"A strong password has \u2026","use":"describe"},{"phrase":"Never share \u2026","use":"strong prohibition"},
    {"phrase":"Always use \u2026","use":"strong recommendation"},{"phrase":"Enable 2FA.","use":"security step"}],
   "mistakes":[{"wrong":"You should to use 2FA.","right":"You should use 2FA.","why":"SHOULD + base verb, no TO."},
    {"wrong":"Don't to share your password.","right":"Don't share your password.","why":"Negative imperative: DON'T + base verb."}],
   "tip":"Modern advice is no longer 'change your password every 90 days'. NIST SP 800-63B recommends: use long passphrases, enable 2FA, and only change a password if you think it was stolen."
  },
  "passage":{"title":"Safe passwords","text":"A password is your key to the computer. A weak password is a big risk. Don't use '123456'. Don't use your name. Don't use 'password'. These are the most common weak passwords in the world. A good password is long. It has 12 characters or more. It uses letters, numbers, and symbols. Better: use a passphrase. A passphrase is four random words, like 'blue-server-fast-moon'. It is easy to remember and very hard to break. You should also use a password manager. A password manager saves all your passwords. Finally: enable two-factor authentication. Two-factor means two steps to log in. This stops 99% of attacks.",
   "wc":118,"source":"Original. Based on NIST SP 800-63B (nist.gov, PD) and CISA password guidance (cisa.gov, PD)."},
  "exercises":[
   {"type":"mcq","q":"How many characters should a good password have?","options":["6","8","12 or more","50"],"a":2,"explain":"'12 characters or more.'"},
   {"type":"tfng","q":"A passphrase is four random words.","a":"T","explain":"Direct quote."},
   {"type":"gap","q":"Two-factor authentication stops ___% of attacks.","a":"99","alts":["99"],"explain":"Cited figure."},
   {"type":"match","pairs":[["weak password","123456"],["passphrase","blue-server-fast-moon"],["manager","saves passwords"],["2FA","two steps"]]},
   {"type":"short","q":"Write 3 rules for safe passwords.","model":"Model: 1) Use a passphrase of 4 words. 2) Never share your password. 3) Enable 2FA on email and bank."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"You ___ reuse passwords.","options":["should","shouldn't","must to","don't should"],"a":1,"explain":"Negative advice."},
   {"type":"cloze","sentence":"___ share your password with anyone.","a":"Don't","alts":["don't","Don't","Do not"],"explain":"Negative imperative."},
   {"type":"word_form","base":"SECURE","sentence":"We need better ___ for user accounts.","a":"security","alts":["security"],"explain":"Adj \u2192 noun: -ity."}
  ]
 },
 11: { # Mobile devices
  "notes":{
   "warmup":"Your phone is a small computer. You use it for email, maps, banking, and passwords. It needs the same care as your laptop \u2014 maybe more, because you carry it everywhere.",
   "grammar":{"title":"Object pronouns",
    "rule":"Subject pronouns do actions (I, you, he, she, it, we, they). Object pronouns receive actions (me, you, him, her, it, us, them).",
    "table":{"head":["Subject","Object","Example"],
     "rows":[["I","me","She called me."],["you","you","I emailed you yesterday."],
      ["he","him","My boss asked him."],["she","her","I told her the news."],
      ["it","it","I lost it."],["we","us","They helped us."],["they","them","I support them."]]},
    "examples":[{"en":"The phone is mine \u2014 please give it to me.","note":"object pronoun"},
     {"en":"She texted him about the bug.","note":"him = object"},
     {"en":"Can you help us with this update?","note":"us = object"}]},
   "phrases":[{"phrase":"Call me when you arrive.","use":"request"},{"phrase":"Send it to me, please.","use":"request file"},
    {"phrase":"Text her the address.","use":"instruction"},{"phrase":"They trust us.","use":"positive statement"}],
   "mistakes":[{"wrong":"Give it to I.","right":"Give it to me.","why":"After preposition \u2192 object pronoun."},
    {"wrong":"She called I yesterday.","right":"She called me yesterday.","why":"Me = object of called."}],
   "tip":"MDM (Mobile Device Management) lets a company lock or wipe your work phone remotely if you lose it. Accept the policy \u2014 it protects you too."
  },
  "passage":{"title":"My smartphone","text":"I have a smartphone. I bought it two years ago. I use it all day. In the morning, my alarm clock wakes me up. Then I check my email. I read the news. I send messages to my friends. I talk to them on video calls. My phone has a fingerprint sensor. I use it to unlock the screen. My phone also has a password. Only I know it. I never share it. If I lose my phone, my company can erase all the data. This is normal for work phones. It protects the data and it protects me.",
   "wc":112,"source":"Original. Inspired by CISA Mobile Device Security guidance (cisa.gov, PD)."},
  "exercises":[
   {"type":"mcq","q":"How does the person unlock the phone?","options":["with a pattern","with a fingerprint","with the face","with a key"],"a":1,"explain":"'A fingerprint sensor... to unlock.'"},
   {"type":"tfng","q":"The person shares the password with friends.","a":"F","explain":"'Only I know it. I never share it.'"},
   {"type":"gap","q":"In the morning, my alarm clock wakes ___ up.","a":"me","alts":["me"],"explain":"Object pronoun."},
   {"type":"match",
    "pairs":[["fingerprint","unlock"],["password","secret"],["MDM","erase data"],["video call","talk to friends"]]},
   {"type":"short","q":"Write 2 things you use your phone for every day.","model":"Model: I use my phone to read the news and to listen to music on the bus."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"Can you help ___ with the update?","options":["I","me","my","mine"],"a":1,"explain":"Object pronoun."},
   {"type":"cloze","sentence":"If I lose my phone, my company can erase ___ .","a":"it","alts":["it"],"explain":"Refers to the phone."},
   {"type":"word_form","base":"SECURE","sentence":"Your phone needs a good ___ lock.","a":"security","alts":["security"],"explain":"-ity noun as attributive."}
  ]
 },
 12: { # Colors and UI
  "notes":{
   "warmup":"Colour is never random in software. Red means danger or error. Green means safe or success. Understanding colour conventions helps you move faster in any new tool.",
   "grammar":{"title":"Adjective + noun order",
    "rule":"In English, the adjective always comes BEFORE the noun: a red button, not 'a button red'. Multiple adjectives follow a fixed order: opinion \u2192 size \u2192 colour \u2192 purpose.",
    "table":{"head":["Order","Example"],
     "rows":[["opinion","a nice icon"],["size","a big window"],["colour","a red error"],
      ["purpose","a search box"],["combined","a nice big red search icon"]]},
    "examples":[{"en":"Click the small blue button.","note":"size + colour + noun"},
     {"en":"Do not close the large red alert.","note":"size + colour + noun"},
     {"en":"I like the new flat design.","note":"opinion + style"}]},
   "phrases":[{"phrase":"Click the \u2026 button.","use":"instruction"},{"phrase":"The \u2026 icon is for \u2026","use":"explain UI"},
    {"phrase":"In the top right, \u2026","use":"location on screen"},{"phrase":"On the home page, \u2026","use":"page reference"}],
   "mistakes":[{"wrong":"Click the button red.","right":"Click the red button.","why":"Adjective \u2192 before the noun."},
    {"wrong":"A red big alert.","right":"A big red alert.","why":"Order: size before colour."}],
   "tip":"When you design a UI, use red only for destructive or dangerous actions. If every button is red, users stop paying attention."
  },
  "passage":{"title":"A simple interface","text":"A good interface is simple. On my app, the home page has three main buttons. The first button is green. It is for 'Start'. The second button is yellow. It is for 'Pause'. The third button is red. It is for 'Stop'. On the top right, there is a small grey icon. It is the settings menu. On the top left, there is a blue 'Help' link. When there is a problem, the app shows a big red message. When something is ready, the app shows a small green check. These colours are common in all apps. Users understand them quickly.",
   "wc":114,"source":"Original. Inspired by WAI colour conventions, W3C accessibility guidelines (w3.org/WAI, CC BY)."},
  "exercises":[
   {"type":"mcq","q":"What is the colour of the 'Stop' button?","options":["green","yellow","red","blue"],"a":2,"explain":"'The third button is red. It is for Stop.'"},
   {"type":"tfng","q":"The settings icon is in the top left.","a":"F","explain":"'On the top right.'"},
   {"type":"gap","q":"When something is ready, the app shows a small ___ check.","a":"green","alts":["green"],"explain":"Green = success."},
   {"type":"match","pairs":[["green","Start"],["yellow","Pause"],["red","Stop"],["grey","Settings"]]},
   {"type":"short","q":"Describe the colours in an app you use every day.","model":"Model: On WhatsApp the header is green. The 'send' button is also green. New messages have a green dot."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"Click the ___ button to stop.","options":["big red","red big","big of red","red of big"],"a":0,"explain":"Size before colour."},
   {"type":"cloze","sentence":"On the top ___ of the screen there is a help icon.","a":"left","alts":["left","right"],"explain":"Location."},
   {"type":"word_form","base":"ACCESS","sentence":"Colour choices affect ___ for blind users.","a":"accessibility","alts":["accessibility"],"explain":"Noun from 'accessible'."}
  ]
 },
 13: { # Office tools
  "notes":{
   "warmup":"Word, Excel, PowerPoint, Google Docs, LibreOffice \u2014 office tools are part of every IT worker's life. Knowing the keyboard shortcuts can save you hours every week.",
   "grammar":{"title":"HAVE TO / NEED TO (necessity)",
    "rule":"Both express necessity. HAVE TO = external obligation (rule, law). NEED TO = internal necessity. Negative: DON'T HAVE TO = no obligation.",
    "table":{"head":["Form","Meaning","Example"],
     "rows":[["have to","external rule","I have to sign the document."],["need to","internal need","I need to save before closing."],
      ["don't have to","no obligation","You don't have to print it."],["must","strong rule","You must accept the terms."]]},
    "examples":[{"en":"I have to send the report by Friday.","note":"deadline = rule"},
     {"en":"You need to check your formulas.","note":"internal need"},
     {"en":"You don't have to buy Office; LibreOffice is free.","note":"absence of obligation"}]},
   "phrases":[{"phrase":"Save as PDF.","use":"instruction"},{"phrase":"Press Ctrl+S.","use":"shortcut"},
    {"phrase":"Copy and paste.","use":"action"},{"phrase":"Use track changes.","use":"collaboration"}],
   "mistakes":[{"wrong":"I must to save the file.","right":"I must save the file.","why":"MUST + base verb, no TO."},
    {"wrong":"You have not to print it.","right":"You don't have to print it.","why":"Negative: DON'T HAVE TO."}],
   "tip":"Macros in Word and Excel are powerful \u2014 and a classic malware vector. If a document asks you to 'Enable content', stop and check the source before clicking."
  },
  "passage":{"title":"Office day","text":"Today I have a lot of office work. First, I need to finish a Word document. I have to send it to my manager by 3 p.m. I use track changes so my manager can see my edits. After that, I have to update an Excel sheet. The sheet has sales data for the last month. I need to add a new column with the total in dollars. Excel has a formula for that: =SUM. It is very useful. Finally, I need to make a short PowerPoint. My colleague will present it tomorrow. I only have to make 5 slides, with a simple design and no animations.",
   "wc":117,"source":"Original. Typical office task flow inspired by Microsoft 365 training modules (docs.microsoft.com, public docs)."},
  "exercises":[
   {"type":"mcq","q":"When does the person have to send the Word document?","options":["tomorrow","by 3 p.m.","by Friday","at 9 a.m."],"a":1,"explain":"'By 3 p.m.'"},
   {"type":"tfng","q":"The PowerPoint has 10 slides with many animations.","a":"F","explain":"'5 slides, simple design, no animations.'"},
   {"type":"gap","q":"The Excel formula for a total is ___ .","a":"SUM","alts":["SUM","=SUM"],"explain":"Quoted in the text."},
   {"type":"match","pairs":[["Word","document"],["Excel","sales data"],["PowerPoint","5 slides"],["Formula","=SUM"]]},
   {"type":"short","q":"Write 2 keyboard shortcuts you use every day.","model":"Model: I use Ctrl+S to save and Ctrl+Z to undo. I also use Alt+Tab to switch windows."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"I ___ send the report before 3 p.m.","options":["have","have to","must to","should to"],"a":1,"explain":"HAVE TO + base verb."},
   {"type":"cloze","sentence":"You ___ have to print it; digital is fine.","a":"don't","alts":["don't","do not"],"explain":"No obligation."},
   {"type":"word_form","base":"PRESENT","sentence":"My colleague will give the ___ tomorrow.","a":"presentation","alts":["presentation"],"explain":"Verb \u2192 noun: -ation."}
  ]
 },
 14: { # Email etiquette 101
  "notes":{
   "warmup":"Email is still the most common business tool in the world. A clear email saves everyone time. A bad email causes misunderstandings, delays, and sometimes security incidents.",
   "grammar":{"title":"Politeness: COULD YOU / PLEASE / THANK YOU",
    "rule":"Polite requests use COULD YOU + base verb or WOULD YOU + base verb. Add PLEASE and close with THANK YOU. This is basic business English.",
    "table":{"head":["Form","Level","Example"],
     "rows":[["Can you \u2026?","informal","Can you send it?"],["Could you \u2026?","polite","Could you send it, please?"],
      ["Would you \u2026?","very polite","Would you be able to send it?"],
      ["I would appreciate \u2026","formal","I would appreciate a quick reply."]]},
    "examples":[{"en":"Could you send me the file, please?","note":"standard polite request"},
     {"en":"Thank you for your reply.","note":"closing"},
     {"en":"I appreciate your quick support.","note":"formal thanks"}]},
   "phrases":[{"phrase":"Dear \u2026,","use":"formal opening"},{"phrase":"Hi \u2026,","use":"informal opening"},
    {"phrase":"Best regards,","use":"formal close"},{"phrase":"Thanks,","use":"informal close"}],
   "mistakes":[{"wrong":"Send me the file now!","right":"Could you send me the file, please?","why":"Direct orders sound rude in email."},
    {"wrong":"Please you send the file.","right":"Please send the file.","why":"PLEASE + verb, no YOU."}],
   "tip":"Never write 'URGENT' in the subject line unless it truly is. In professional emails, overuse of URGENT is a well-known red flag for phishing too."
  },
  "passage":{"title":"A professional email","text":"Hi Ana,\n\nI hope you are well. I am writing about the new server project. Could you send me the latest diagram, please? I need it for tomorrow's meeting with the client. The meeting is at 10 a.m.\n\nAlso, could we have a short call this afternoon? I have a few questions about the firewall rules. Any time after 2 p.m. is good for me.\n\nThank you for your help.\n\nBest regards,\nCarlos",
   "wc":74,"source":"Original. Email conventions from British Council Learn English (britishcouncil.org, CC BY-NC-SA)."},
  "exercises":[
   {"type":"mcq","q":"What does Carlos want from Ana?","options":["money","the latest diagram and a call","a printer","the office address"],"a":1,"explain":"'Send me the latest diagram' + 'Could we have a short call.'"},
   {"type":"tfng","q":"The meeting is at 2 p.m.","a":"F","explain":"'The meeting is at 10 a.m.'"},
   {"type":"gap","q":"Any time after ___ p.m. is good for Carlos.","a":"2","alts":["2","two"],"explain":"Time given."},
   {"type":"match","pairs":[["Dear","formal open"],["Hi","informal open"],["Best regards","formal close"],["Thanks","informal close"]]},
   {"type":"short","q":"Write a 3-line email to a colleague asking for a file.","model":"Model: Hi Marta, Could you send me the project plan, please? I need it for the call at 3 p.m. Thanks, Juan."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"___ you send me the file, please?","options":["Do","Could","Are","Must"],"a":1,"explain":"Polite request."},
   {"type":"cloze","sentence":"Thank you ___ your help.","a":"for","alts":["for"],"explain":"Collocation: thanks FOR."},
   {"type":"word_form","base":"URGENT","sentence":"Don't use 'urgent' if the request is not ___ .","a":"urgent","alts":["urgent"],"explain":"Adjective unchanged."}
  ]
 },
 15: { # Time, meetings and schedules
  "notes":{
   "warmup":"In IT, meetings fill the calendar. A good meeting has an agenda, a clear time limit, and action points. A bad meeting is a waste of everyone's salary.",
   "grammar":{"title":"Prepositions of time: AT, ON, IN",
    "rule":"AT for exact times and holidays. ON for days and dates. IN for months, years, seasons, and long periods.",
    "table":{"head":["Preposition","Use","Example"],
     "rows":[["at","exact time","The meeting is at 10 a.m."],["at","weekend","I am free at the weekend."],
      ["on","day","On Monday we have a standup."],["on","date","The release is on 15 May."],
      ["in","month","The project starts in June."],["in","year","It started in 2024."]]},
    "examples":[{"en":"We meet at 10 on Tuesday.","note":"exact time + day"},
     {"en":"The deadline is on 30 April.","note":"date"},
     {"en":"I joined the company in 2023.","note":"year"}]},
   "phrases":[{"phrase":"Let's schedule a meeting.","use":"propose"},{"phrase":"Are you free on \u2026?","use":"check availability"},
    {"phrase":"Can we move the meeting to \u2026?","use":"reschedule"},{"phrase":"I'll send a calendar invite.","use":"confirm"}],
   "mistakes":[{"wrong":"The meeting is in 10 a.m.","right":"The meeting is at 10 a.m.","why":"AT for exact times."},
    {"wrong":"I will see you at Monday.","right":"I will see you on Monday.","why":"ON for days."}],
   "tip":"Accept a meeting only if you need to be there. 'Can this be an email?' is a professional question, not a rude one."
  },
  "passage":{"title":"My week","text":"I have many meetings this week. On Monday at 9 a.m. I have our standup with the development team. It is only 15 minutes. On Tuesday I have a one-hour meeting with the client at 11 a.m. On Wednesday I am free in the morning, but I have a training session at 3 p.m. On Thursday there is a long meeting at 2 p.m. \u2014 the sprint review. On Friday we have the retrospective at 10 a.m. I also have calls at random times during the week. In total, I have 8 meetings. That is too many for a busy week!",
   "wc":114,"source":"Original. Scrum meeting cadence from Scrum Guide (scrumguides.org, CC BY-SA)."},
  "exercises":[
   {"type":"mcq","q":"When is the sprint review?","options":["Monday","Wednesday","Thursday","Friday"],"a":2,"explain":"'On Thursday... the sprint review.'"},
   {"type":"tfng","q":"The person is free all day on Wednesday.","a":"F","explain":"'Wednesday I am free in the morning' but has a training at 3 p.m."},
   {"type":"gap","q":"On Monday ___ 9 a.m. I have our standup.","a":"at","alts":["at"],"explain":"Preposition of time with clock time."},
   {"type":"match","pairs":[["standup","Monday"],["client meeting","Tuesday"],["training","Wednesday"],["retrospective","Friday"]]},
   {"type":"short","q":"Describe 3 meetings you have next week.","model":"Model: On Monday I have a class at 9. On Wednesday I have a call with my team at 3. On Friday I have a study group at 6."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"The retrospective is ___ Friday.","options":["at","on","in","for"],"a":1,"explain":"ON + day."},
   {"type":"cloze","sentence":"The project starts ___ June.","a":"in","alts":["in"],"explain":"IN + month."},
   {"type":"word_form","base":"SCHEDULE","sentence":"Our weekly ___ is full.","a":"schedule","alts":["schedule"],"explain":"Noun form (same spelling)."}
  ]
 },
 16: { # Sizes and units
  "notes":{
   "warmup":"In IT, we talk about size all the time. A file is 5 MB. A disk has 1 TB. A photo is 12 MP. Understanding units helps you talk to engineers, sales people, and customers.",
   "grammar":{"title":"Countable vs uncountable + MUCH / MANY",
    "rule":"Countable nouns have singular and plural (file / files). Uncountable nouns have no plural (data, software, advice). Use MANY with countables, MUCH with uncountables.",
    "table":{"head":["Type","Examples","Quantity word"],
     "rows":[["countable","files, disks, laptops","many, few, a few"],
      ["uncountable","data, software, memory","much, little, a little"],
      ["both","How many files?","countable"],["both","How much memory?","uncountable"]]},
    "examples":[{"en":"How many GB does it have?","note":"GB are countable"},
     {"en":"How much memory does it have?","note":"memory is uncountable"},
     {"en":"There isn't much space on this disk.","note":"negative with uncountable"}]},
   "phrases":[{"phrase":"The file is X MB.","use":"size"},{"phrase":"It has X GB of RAM.","use":"memory"},
    {"phrase":"The disk is full.","use":"state"},{"phrase":"How much free space?","use":"question"}],
   "mistakes":[{"wrong":"How much files do you have?","right":"How many files do you have?","why":"Files = countable \u2192 MANY."},
    {"wrong":"I have many free space.","right":"I have much free space.","why":"Space = uncountable \u2192 MUCH."}],
   "tip":"1 KB = 1024 bytes, 1 MB = 1024 KB, 1 GB = 1024 MB. Some tools use 1000 instead of 1024. That is why your 1 TB disk shows 931 GB in Windows."
  },
  "passage":{"title":"My new laptop","text":"Today my new laptop arrived. It is a big change. My old laptop had 4 GB of RAM and a small 256 GB disk. It was very slow. The new one has 32 GB of RAM and a 1 TB SSD. It is eight times more memory and four times more storage. The screen is bigger too: 16 inches. The weight is only 1.7 kilos. I can install many programs without problems. Now I can run Docker, Visual Studio, and three browsers at the same time. No lag. I also like the battery. It lasts 10 hours. My old battery was dying after two hours.",
   "wc":114,"source":"Original. Laptop specifications are typical 2025\u20132026 consumer hardware descriptions."},
  "exercises":[
   {"type":"mcq","q":"How much RAM does the new laptop have?","options":["4 GB","16 GB","32 GB","256 GB"],"a":2,"explain":"'32 GB of RAM.'"},
   {"type":"tfng","q":"The new laptop battery lasts 2 hours.","a":"F","explain":"'It lasts 10 hours.'"},
   {"type":"gap","q":"The new SSD has 1 ___ of storage.","a":"TB","alts":["TB","tb"],"explain":"Unit."},
   {"type":"match","pairs":[["RAM","32 GB"],["Storage","1 TB"],["Screen","16 inches"],["Battery","10 hours"]]},
   {"type":"short","q":"Describe your own laptop in 3 sentences.","model":"Model: My laptop has 8 GB of RAM and 512 GB of storage. The screen is 14 inches. The battery lasts about 6 hours."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"How ___ memory does it have?","options":["much","many","a much","a many"],"a":0,"explain":"Memory = uncountable."},
   {"type":"cloze","sentence":"It has 1 TB of ___ .","a":"storage","alts":["storage","disk"],"explain":"Uncountable noun."},
   {"type":"word_form","base":"STORE","sentence":"The ___ on this disk is full.","a":"storage","alts":["storage"],"explain":"Verb \u2192 noun."}
  ]
 },
 17: { # Simple troubleshooting
  "notes":{
   "warmup":"Troubleshooting is 50% of an IT job. The first rule: describe the problem clearly. The second rule: try the simple steps first. The third rule: document what you did.",
   "grammar":{"title":"WHY / BECAUSE + sequence: FIRST, THEN, FINALLY",
    "rule":"Use WHY to ask a reason and BECAUSE to give one. Use sequence words to describe steps.",
    "table":{"head":["Word","Use","Example"],
     "rows":[["why","ask reason","Why doesn't it work?"],["because","give reason","Because the cable is loose."],
      ["first","start","First, check the power."],["then","next","Then, restart the computer."],
      ["after that","middle","After that, try again."],["finally","end","Finally, if it fails, call support."]]},
    "examples":[{"en":"Why is the laptop slow? Because the disk is full.","note":"Q + A"},
     {"en":"First, restart. Then, update. Finally, reinstall.","note":"sequence"}]},
   "phrases":[{"phrase":"Have you tried \u2026?","use":"suggest"},{"phrase":"Does it work now?","use":"check result"},
    {"phrase":"It still doesn't work.","use":"report failure"},{"phrase":"What was the last change?","use":"investigate"}],
   "mistakes":[{"wrong":"The reason why is because the cable is loose.","right":"The reason is that the cable is loose.","why":"Avoid 'reason why \u2026 because' redundancy."},
    {"wrong":"First, then, you restart.","right":"First, restart. Then, try again.","why":"Each sequence word introduces its own step."}],
   "tip":"'Have you tried turning it off and on again?' is a cliche because it works. Rebooting clears the RAM, closes broken processes, and reapplies settings."
  },
  "passage":{"title":"My computer is slow","text":"Last week, my work laptop was very slow. Every program took five minutes to open. I was angry. First, I restarted the computer. It was a little better, but still slow. Then, I checked the disk space. It was 95% full. That was the problem! I deleted old files. I emptied the Recycle Bin. I uninstalled two programs I never used. After that, the laptop was fast again. Why was it slow? Because the disk was full. A full disk makes everything slow. Now I check my disk space every month. Finally, I also cleared my browser cache. That helped too. Problem solved!",
   "wc":116,"source":"Original. Troubleshooting flow from Microsoft Learn 'Troubleshoot performance' (learn.microsoft.com, public)."},
  "exercises":[
   {"type":"mcq","q":"What was the main problem?","options":["broken keyboard","full disk","bad Wi-Fi","old CPU"],"a":1,"explain":"'It was 95% full. That was the problem.'"},
   {"type":"tfng","q":"The person checked the disk space before restarting.","a":"F","explain":"'First, I restarted... Then, I checked.'"},
   {"type":"gap","q":"Why was the laptop slow? ___ the disk was full.","a":"Because","alts":["Because","because"],"explain":"Reason connector."},
   {"type":"match","pairs":[["first","restart"],["then","check disk"],["after that","delete files"],["finally","clear cache"]]},
   {"type":"short","q":"Write 3 steps to fix a slow computer.","model":"Model: First, restart the computer. Then, check the disk space and delete old files. Finally, uninstall unused programs."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"The disk was full, ___ the laptop was slow.","options":["so","but","because","while"],"a":0,"explain":"Consequence: SO."},
   {"type":"cloze","sentence":"___ , I restarted the computer.","a":"First","alts":["First","first"],"explain":"Start of sequence."},
   {"type":"word_form","base":"SOLVE","sentence":"Problem ___ !","a":"solved","alts":["solved"],"explain":"Past participle as adjective."}
  ]
 },
 18: { # Jobs in IT
  "notes":{
   "warmup":"The IT world has hundreds of job titles. But the big families are clear: development, operations, support, security, data, management. Knowing them helps you map your career.",
   "grammar":{"title":"Comparatives: short adjectives",
    "rule":"Add -er for comparison, -est for superlative. For adjectives ending in -y, change to -ier. For short adjectives ending in consonant+vowel+consonant, double the last consonant.",
    "table":{"head":["Adjective","Comparative","Superlative"],
     "rows":[["fast","faster","the fastest"],["big","bigger","the biggest"],["easy","easier","the easiest"],
      ["good","better","the best"],["bad","worse","the worst"]]},
    "examples":[{"en":"Python is easier than C++.","note":"easier than"},
     {"en":"A senior role is better paid than a junior role.","note":"better paid than"},
     {"en":"The biggest tech companies pay the highest salaries.","note":"superlative"}]},
   "phrases":[{"phrase":"I work as a \u2026","use":"state your role"},{"phrase":"My responsibilities are \u2026","use":"list duties"},
    {"phrase":"I report to \u2026","use":"reporting line"},{"phrase":"I have X years of experience in \u2026","use":"experience"}],
   "mistakes":[{"wrong":"Python is more easy than C++.","right":"Python is easier than C++.","why":"Short adjective + -er, not MORE."},
    {"wrong":"He is gooder than me.","right":"He is better than me.","why":"Good \u2192 better (irregular)."}],
   "tip":"When you apply for a job, match your CV to the job description. Use the same keywords: if they say 'Kubernetes', say 'Kubernetes', not 'container orchestration platform'."
  },
  "passage":{"title":"Different IT jobs","text":"Carmen is a data analyst. She works with numbers and charts. She uses SQL and Excel every day. She says her job is quieter than a developer's job. Diego is a developer. He writes code in Python. He says his job is faster and more stressful than data analysis. Every sprint he has to deliver new features. Laura is a SOC analyst. She watches for cyber attacks at a security team. She says her job is the most stressful of all, because attacks come at any hour. Carmen, Diego, and Laura work at the same company. They are good friends. They often talk about which IT job is the best. For each of them, the answer is: the one I have!",
   "wc":130,"source":"Original. IT role descriptions from ENISA Cybersecurity Skills Framework (enisa.europa.eu)."},
  "exercises":[
   {"type":"mcq","q":"Who says her job is the most stressful?","options":["Carmen","Diego","Laura","all three"],"a":2,"explain":"'Laura... her job is the most stressful.'"},
   {"type":"tfng","q":"Carmen uses Python every day.","a":"F","explain":"She uses SQL and Excel, not Python."},
   {"type":"gap","q":"Diego's job is ___ than data analysis.","a":"faster","alts":["faster","more stressful"],"explain":"Comparative."},
   {"type":"match","pairs":[["Carmen","data analyst"],["Diego","developer"],["Laura","SOC analyst"],["Common","same company"]]},
   {"type":"short","q":"Which IT job would you choose and why?","model":"Model: I would be a developer because I like solving problems with code. It is creative and well paid."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"Python is ___ than C++.","options":["easier","more easy","the easiest","easy"],"a":0,"explain":"Short adj + -er."},
   {"type":"cloze","sentence":"The senior role is ___ paid than the junior role.","a":"better","alts":["better"],"explain":"Irregular comparative."},
   {"type":"word_form","base":"DEVELOP","sentence":"She is a senior software ___ .","a":"developer","alts":["developer"],"explain":"Agent noun."}
  ]
 },
 19: { # My first English CV
  "notes":{
   "warmup":"A good CV opens doors. In English, CVs are short and direct: 1-2 pages, action verbs, numbers when possible. A wall of text kills your chances.",
   "grammar":{"title":"Past simple (regular) + LAST / AGO",
    "rule":"Use LAST + time for the most recent period (last year, last month). Use number + AGO for time from now (two years ago). Both use past simple.",
    "table":{"head":["Word","Example","Use"],
     "rows":[["last week","I finished the project last week.","previous period"],
      ["last year","I joined the company last year.","previous year"],
      ["X ago","I graduated 2 years ago.","distance from now"],
      ["in + year","I started in 2021.","specific year"]]},
    "examples":[{"en":"I completed the CCNA last year.","note":"last year"},
     {"en":"I left my first job 2 years ago.","note":"AGO"},
     {"en":"I joined in 2023.","note":"specific year"}]},
   "phrases":[{"phrase":"I graduated from \u2026","use":"education"},{"phrase":"I worked as \u2026 at \u2026","use":"experience"},
    {"phrase":"I managed a team of \u2026","use":"leadership"},{"phrase":"I delivered \u2026","use":"achievement"}],
   "mistakes":[{"wrong":"I have worked there last year.","right":"I worked there last year.","why":"LAST YEAR = specific past \u2192 past simple."},
    {"wrong":"I graduated since 2 years.","right":"I graduated 2 years ago.","why":"SINCE needs a point in time; AGO = distance."}],
   "tip":"Start every CV bullet with an action verb in past simple: 'Designed', 'Built', 'Deployed', 'Reduced', 'Migrated'. Not 'I was responsible for'."
  },
  "passage":{"title":"Sofia's CV summary","text":"Sofia is looking for a new job. She finished her CV last week. Her CV has three parts. First, her education: she graduated from the university three years ago. Her degree is in computer science. Second, her work experience. She worked as a junior developer at a small startup from 2022 to 2024. She built two mobile apps. Last year she joined a bank as a systems engineer. She designed a new backup process. It reduced recovery time by 40%. Third, her skills and certifications: she knows Python, SQL, and AWS. She passed the AWS Certified Solutions Architect exam six months ago. Now she is ready to apply for senior roles.",
   "wc":124,"source":"Original. CV structure follows common industry guidelines (LinkedIn Learning, public training resources)."},
  "exercises":[
   {"type":"mcq","q":"How long ago did Sofia graduate?","options":["1 year ago","2 years ago","3 years ago","5 years ago"],"a":2,"explain":"'She graduated... three years ago.'"},
   {"type":"tfng","q":"Sofia passed the AWS exam last year.","a":"F","explain":"'Six months ago.'"},
   {"type":"gap","q":"She designed a new backup process. It ___ recovery time by 40%.","a":"reduced","alts":["reduced"],"explain":"Past simple regular."},
   {"type":"match","pairs":[["2021","degree"],["2022\u20132024","startup"],["Last year","bank"],["6 months ago","AWS exam"]]},
   {"type":"short","q":"Write 3 bullets for your own CV (with action verbs).","model":"Model: Built a simple blog in HTML and CSS. Completed an online course on Python. Managed the social media of a small NGO."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"She graduated three years ___ .","options":["before","ago","since","for"],"a":1,"explain":"Distance from now: AGO."},
   {"type":"cloze","sentence":"Last year she ___ a bank.","a":"joined","alts":["joined"],"explain":"Past simple."},
   {"type":"word_form","base":"CERTIFY","sentence":"She has an AWS ___ .","a":"certification","alts":["certification","certificate"],"explain":"Verb \u2192 noun."}
  ]
 },
 20: { # Final project + Mock KET
  "notes":{
   "warmup":"You are ready for the A1 exam. The Cambridge A1 Key Test (KET) has 4 papers: Reading & Writing, Listening, and Speaking. This lesson reviews the main skills.",
   "grammar":{"title":"A1 grammar recap",
    "rule":"This lesson combines everything: BE, have got, present simple, present continuous, past simple, imperatives, modals, prepositions, comparatives.",
    "table":{"head":["Area","Example"],
     "rows":[["BE","I am a systems engineer."],["Present simple","We check logs every day."],
      ["Past simple","I graduated last year."],["Prepositions","The file is on my desk."],
      ["Comparatives","Python is easier than C++."]]},
    "examples":[{"en":"I am a junior engineer and I work at a tech company.","note":"BE + present simple"},
     {"en":"Yesterday I fixed a bug.","note":"past simple"},
     {"en":"Please send me the file, thanks.","note":"imperative + polite"}]},
   "phrases":[{"phrase":"I would like to \u2026","use":"polite intention"},{"phrase":"Let me check.","use":"pause"},
    {"phrase":"Can I ask a question?","use":"interrupt politely"},{"phrase":"I'm not sure.","use":"hedge"}],
   "mistakes":[{"wrong":"I am work here since 2 years.","right":"I have worked here for 2 years.","why":"Duration \u2192 present perfect + FOR."},
    {"wrong":"He don't like it.","right":"He doesn't like it.","why":"3rd person singular: DOESN'T."}],
   "tip":"In the Speaking test, slow and clear beats fast and confused. Repeat the question if you need time: 'So, my typical day at work \u2026'."
  },
  "passage":{"title":"Review: my first year in IT","text":"My first year as a systems engineer is almost over. In September 2025, I started at a small company in Lima. It was my first real job. Every day I checked servers, answered emails, and helped users with passwords. At first, I was nervous. My English was not very good. I made many mistakes. But my team was patient. They helped me every week. In January 2026, I got my first certification. Now I work with more confidence. I speak English in meetings with clients from the United States. I still learn something new every day. I plan to apply for a senior role next year. First, I need to pass the A2 exam.",
   "wc":127,"source":"Original. KET-style personal reflection narrative."},
  "exercises":[
   {"type":"mcq","q":"When did the person start the job?","options":["January 2025","September 2025","January 2026","September 2026"],"a":1,"explain":"'In September 2025.'"},
   {"type":"tfng","q":"The team was not patient at the beginning.","a":"F","explain":"'My team was patient.'"},
   {"type":"gap","q":"I plan ___ apply for a senior role next year.","a":"to","alts":["to"],"explain":"Plan + to + infinitive."},
   {"type":"match","pairs":[["September 2025","first job"],["January 2026","certification"],["Now","meetings in English"],["Next year","senior role"]]},
   {"type":"short","q":"Write a 4-sentence reflection on your own learning year.","model":"Model: This year I studied English every week. I learned many new words. I also passed a Python course online. Next year I want to start working as a junior developer."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"I ___ my first certification in January.","options":["get","getted","got","did get"],"a":2,"explain":"Irregular past: get \u2192 got."},
   {"type":"cloze","sentence":"I plan ___ apply for a senior role.","a":"to","alts":["to"],"explain":"plan + to + inf."},
   {"type":"word_form","base":"CONFIDENT","sentence":"I now work with more ___ .","a":"confidence","alts":["confidence"],"explain":"Adj \u2192 noun: -ence."}
  ]
 },
},
"A2": {
 6: { # Social media safety
  "notes":{
   "warmup":"Social media is a public space that feels private. Every photo, every post, every like is data \u2014 for advertisers, for attackers, and for future employers. Knowing the settings is a skill.",
   "grammar":{"title":"MUST / MUSTN'T / CAN'T",
    "rule":"MUST = strong rule or obligation. MUSTN'T = strong prohibition ('it is forbidden'). CAN'T = impossibility or prohibition (similar to MUSTN'T but slightly softer).",
    "table":{"head":["Modal","Use","Example"],
     "rows":[["must","rule","You must read the privacy policy."],["mustn't","forbidden","You mustn't share your password."],
      ["can't","prohibition","You can't post work photos."],["have to","external rule","I have to accept the GDPR banner."]]},
    "examples":[{"en":"You must not share login codes on WhatsApp.","note":"strong prohibition"},
     {"en":"You can't install random apps on your work phone.","note":"company policy"},
     {"en":"You have to accept the terms to use the service.","note":"external rule"}]},
   "phrases":[{"phrase":"Review your privacy settings.","use":"action"},{"phrase":"Be careful about what you post.","use":"warning"},
    {"phrase":"Block the user.","use":"defensive action"},{"phrase":"Report the post.","use":"defensive action"}],
   "mistakes":[{"wrong":"You must to share your password.","right":"You mustn't share your password.","why":"MUST + base verb; MUSTN'T for prohibition."},
    {"wrong":"I must not to post photos.","right":"I mustn't post photos.","why":"MUSTN'T + base verb, no TO."}],
   "tip":"Before you post on LinkedIn or X, ask: would I be happy if my next employer saw this? The internet has a very long memory."
  },
  "passage":{"title":"Social media and work","text":"Last month, a friend of mine lost his job. Why? Because of a post on social media. He complained about his manager on a public profile. Someone sent a screenshot to HR. The company had a clear policy: employees mustn't post negative comments about their work. He signed this policy when he joined. This story is common. Social media mistakes cost real jobs every week. A few rules are important. First, you mustn't post photos of customers or internal data. Second, you can't share login codes or passwords in messages. Third, check your privacy settings every six months. Platforms change their settings often. And always remember: the internet is not a diary. Everybody can read what you write.",
   "wc":136,"source":"Original. Social-media risk scenarios from ENISA 'Cybersecurity Awareness' campaigns (enisa.europa.eu)."},
  "exercises":[
   {"type":"mcq","q":"Why did the friend lose his job?","options":["he was late","he complained on social media","he stole money","he forgot a meeting"],"a":1,"explain":"'He complained about his manager on a public profile.'"},
   {"type":"tfng","q":"The company had no policy about social media.","a":"F","explain":"'A clear policy: employees mustn't post negative comments.'"},
   {"type":"gap","q":"You ___ share login codes or passwords in messages.","a":"can't","alts":["can't","cannot","mustn't"],"explain":"Prohibition."},
   {"type":"match","pairs":[["rule 1","no customer photos"],["rule 2","no login codes"],["rule 3","check privacy"],["friend","lost his job"]]},
   {"type":"short","q":"Write 3 rules for safe social media at work.","model":"Model: 1) Don't post customer data. 2) Don't write about your manager. 3) Check your privacy settings every 6 months."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"You ___ share passwords in messages.","options":["mustn't","must","can","should to"],"a":0,"explain":"Strong prohibition."},
   {"type":"cloze","sentence":"The company has a ___ against negative posts.","a":"policy","alts":["policy","rule"],"explain":"Formal term."},
   {"type":"word_form","base":"PRIVATE","sentence":"Review your ___ settings.","a":"privacy","alts":["privacy"],"explain":"Adj \u2192 noun: -acy."}
  ]
 },
 7: { # Networks: Wi-Fi and LAN
  "notes":{
   "warmup":"Your home Wi-Fi is a small, real network. Understanding how it works helps you fix problems at home and, later, bigger networks at work.",
   "grammar":{"title":"Adverbs of manner",
    "rule":"Adverbs of manner describe HOW something happens. Most are formed adjective + -ly (quick \u2192 quickly). Irregular: good \u2192 well, fast \u2192 fast, hard \u2192 hard.",
    "table":{"head":["Adjective","Adverb","Example"],
     "rows":[["quick","quickly","The router reboots quickly."],["slow","slowly","The page loads slowly."],
      ["careful","carefully","Check the cable carefully."],["good","well","This router works well."],
      ["fast","fast","Fibre is fast."]]},
    "examples":[{"en":"Configure the firewall carefully.","note":"manner"},
     {"en":"The connection works well in the morning.","note":"irregular"},
     {"en":"Data travels quickly on fibre.","note":"-ly adverb"}]},
   "phrases":[{"phrase":"The signal is weak.","use":"state"},{"phrase":"I lost the connection.","use":"problem"},
    {"phrase":"Move closer to the router.","use":"advice"},{"phrase":"Change the Wi-Fi password.","use":"action"}],
   "mistakes":[{"wrong":"The page loads slow.","right":"The page loads slowly.","why":"Adverb modifies verb \u2192 add -ly."},
    {"wrong":"This router works good.","right":"This router works well.","why":"Irregular: good \u2192 well."}],
   "tip":"Always change the default admin password of your router. Botnets like Mirai scan the internet looking for routers with default credentials."
  },
  "passage":{"title":"My home network","text":"At home we have a small network. It is a LAN \u2014 a Local Area Network. Our router is in the living room. It connects to the internet through fibre. The router shares Wi-Fi with all the devices in the house. We have three laptops, four phones, one printer, one smart TV, and two smart speakers. All of them are connected. The Wi-Fi is fast in the living room but weak in the garage. When my brother plays online games in his room, the connection works well. Sometimes the signal slows down in the evening. Why? Because many neighbours use their networks at the same time. Last month I carefully changed the default admin password. My old neighbour was a hacker \u2014 for jokes, I hope!",
   "wc":142,"source":"Original. Home network basics from Cisco Networking Basics (netacad.com, free educational materials)."},
  "exercises":[
   {"type":"mcq","q":"How many devices are connected to the Wi-Fi?","options":["7","10","11","12"],"a":2,"explain":"3 laptops + 4 phones + 1 printer + 1 TV + 2 speakers = 11."},
   {"type":"tfng","q":"The Wi-Fi is weak in the living room.","a":"F","explain":"'Fast in the living room but weak in the garage.'"},
   {"type":"gap","q":"I ___ changed the default admin password.","a":"carefully","alts":["carefully"],"explain":"Adverb of manner."},
   {"type":"match","pairs":[["LAN","home network"],["router","Wi-Fi source"],["fibre","internet line"],["Mirai","botnet"]]},
   {"type":"short","q":"Describe your own home network in 2-3 sentences.","model":"Model: At home I have one router and I share Wi-Fi with my family. We have 2 laptops, 3 phones and 1 TV connected."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"The page loads ___ this evening.","options":["slow","slowly","more slow","slower of"],"a":1,"explain":"Adverb of manner."},
   {"type":"cloze","sentence":"The connection works ___ in the morning.","a":"well","alts":["well"],"explain":"Irregular adverb."},
   {"type":"word_form","base":"CONNECT","sentence":"My Wi-Fi has a weak ___ .","a":"connection","alts":["connection"],"explain":"-tion noun."}
  ]
 },
 8: { # Mobile devices advanced
  "notes":{
   "warmup":"Modern phones are like mini computers. We use them for work, banking, and security. Configuring them well is part of your digital hygiene.",
   "grammar":{"title":"GOING TO (plans and predictions)",
    "rule":"Use BE + GOING TO + base verb for plans and predictions with evidence. Different from WILL (spontaneous decisions).",
    "table":{"head":["Form","Use","Example"],
     "rows":[["am / is / are going to + base","plan","I'm going to install a VPN."],
      ["am / is / are not going to","plan (negative)","We're not going to allow jailbreak."],
      ["Is/Are \u2026 going to?","question","Are you going to enrol the device?"]]},
    "examples":[{"en":"I'm going to enable MDM on my phone.","note":"plan"},
     {"en":"Our company is going to require 2FA next month.","note":"future policy"},
     {"en":"It's going to rain \u2014 the sky is grey.","note":"prediction with evidence"}]},
   "phrases":[{"phrase":"Enable biometric login.","use":"security action"},{"phrase":"Install the MDM profile.","use":"corporate action"},
    {"phrase":"Update to the latest iOS.","use":"patch"},{"phrase":"Enrol your device.","use":"IT process"}],
   "mistakes":[{"wrong":"I going to call the helpdesk.","right":"I am going to call the helpdesk.","why":"Need BE."},
    {"wrong":"She is going to calls the manager.","right":"She is going to call the manager.","why":"GOING TO + base verb."}],
   "tip":"Never root or jailbreak a work phone. It breaks the chain of trust and most companies have policies that force an immediate wipe."
  },
  "passage":{"title":"My new work phone","text":"Today my new work phone arrives. It is an iPhone 17. I am going to set it up this afternoon. First, I am going to enrol the device with the company MDM. This means my IT department will control some settings. Then I am going to set up a strong passcode and enable Face ID. After that, I am going to install the company apps: Outlook, Teams, and the VPN client. I am not going to install personal apps from the App Store for now. At home I have my old phone for personal use. Finally, I am going to read the acceptable use policy. It has important rules about work data. Next month, my company is going to launch a new security training. Every employee has to take it.",
   "wc":142,"source":"Original. Inspired by NIST SP 800-124 Rev.2 Mobile Device Security Guidelines (nist.gov, PD)."},
  "exercises":[
   {"type":"mcq","q":"What is the person NOT going to do today?","options":["enrol the device","set up Face ID","install Teams","install personal apps"],"a":3,"explain":"'Not going to install personal apps.'"},
   {"type":"tfng","q":"The company will control some settings on the phone.","a":"T","explain":"'My IT department will control some settings.'"},
   {"type":"gap","q":"I am going to set up a strong ___ .","a":"passcode","alts":["passcode","password"],"explain":"From the text."},
   {"type":"match","pairs":[["MDM","corporate control"],["Face ID","biometrics"],["AUP","acceptable use policy"],["next month","security training"]]},
   {"type":"short","q":"Describe 3 things you are going to do next weekend.","model":"Model: I'm going to visit my parents. I'm going to study for an exam. I'm going to clean my room."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"I ___ install the company apps later.","options":["going to","am going to","will going","goes to"],"a":1,"explain":"BE + going to + base."},
   {"type":"cloze","sentence":"We're not going to ___ personal apps on work phones.","a":"install","alts":["install","allow"],"explain":"Base verb."},
   {"type":"word_form","base":"ACCEPT","sentence":"Read the ___ use policy.","a":"acceptable","alts":["acceptable"],"explain":"Verb \u2192 adjective: -able."}
  ]
 },
 9: { # Cloud storage basics
  "notes":{
   "warmup":"Cloud storage is not magic; it is someone else's computer. Understanding what that means helps you choose the right service and avoid embarrassing leaks.",
   "grammar":{"title":"HOW MUCH / HOW MANY + quantifiers",
    "rule":"HOW MUCH + uncountable noun. HOW MANY + countable noun. Use A LOT OF for large amounts of both. Use A LITTLE for small uncountable, A FEW for small countable.",
    "table":{"head":["Quantifier","Use","Example"],
     "rows":[["how much","uncountable","How much storage do I have?"],
      ["how many","countable","How many files can I share?"],
      ["a lot of","both","I have a lot of files."],
      ["a little","uncountable","I have a little space left."],
      ["a few","countable","I have a few backups."]]},
    "examples":[{"en":"How much space do we have left in the bucket?","note":"uncountable"},
     {"en":"How many team members have write access?","note":"countable"},
     {"en":"We have a lot of old backups; we should clean them.","note":"quantifier"}]},
   "phrases":[{"phrase":"Share it with \u2026","use":"permission"},{"phrase":"Make a backup.","use":"safety"},
    {"phrase":"Restore the file.","use":"recovery"},{"phrase":"Check the quota.","use":"capacity"}],
   "mistakes":[{"wrong":"How many space do I have?","right":"How much space do I have?","why":"Space = uncountable."},
    {"wrong":"I have a little files.","right":"I have a few files.","why":"Files = countable \u2192 A FEW."}],
   "tip":"Always enable versioning and access logs on your cloud storage. When a file mysteriously changes, logs are the only way to know who did it."
  },
  "passage":{"title":"Our cloud setup","text":"Our team uses cloud storage every day. We pay for a business plan with 5 TB of storage. How much space do we have left? Not a lot \u2014 only 200 GB. We have too many old files. Last week, the manager asked: how many files are more than two years old? The answer was 28,000. We decided to clean the account. We archived old projects to cheaper cold storage. We also reviewed permissions: how many people have access to sensitive folders? Only the security team now. Finally, we enabled versioning. If someone deletes a file by mistake, we can restore it. A little discipline saves a lot of money in the cloud. Next quarter, we are going to move to a competitor, because the price went up.",
   "wc":140,"source":"Original. Cloud cost-management patterns from AWS Well-Architected Framework (aws.amazon.com/architecture, public)."},
  "exercises":[
   {"type":"mcq","q":"How much free space did they have?","options":["5 TB","2 TB","200 GB","28,000 files"],"a":2,"explain":"'Only 200 GB.'"},
   {"type":"tfng","q":"All employees still have access to sensitive folders.","a":"F","explain":"'Only the security team now.'"},
   {"type":"gap","q":"We enabled ___ so deleted files can be restored.","a":"versioning","alts":["versioning"],"explain":"From the text."},
   {"type":"match","pairs":[["5 TB","total plan"],["200 GB","free space"],["28,000","old files"],["cold storage","archive"]]},
   {"type":"short","q":"Explain why cleaning old files matters in the cloud.","model":"Model: Old files take space and cost money. Cleaning them reduces the cost and makes the account easier to manage."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"___ space do we have left?","options":["How many","How much","How","Much"],"a":1,"explain":"Space = uncountable."},
   {"type":"cloze","sentence":"We have a ___ of old files.","a":"lot","alts":["lot"],"explain":"'A lot of'."},
   {"type":"word_form","base":"STORE","sentence":"We need more ___ .","a":"storage","alts":["storage"],"explain":"Verb \u2192 noun."}
  ]
 },
 10: { # Email etiquette advanced
  "notes":{
   "warmup":"Professional email is a performance: you write, but your reader does not see you. Tone, structure, and timing all affect how the message lands. Bad emails cost relationships.",
   "grammar":{"title":"Polite requests: WOULD YOU MIND \u2026 ?",
    "rule":"WOULD YOU MIND + -ing? = very polite request. Answer 'No, not at all' = I will do it. 'I'd rather not' = I don't want to. Also: COULD YOU POSSIBLY \u2026 ?",
    "table":{"head":["Formula","Register","Example"],
     "rows":[["Can you \u2026?","informal","Can you send it?"],
      ["Could you \u2026?","polite","Could you send it, please?"],
      ["Would you mind \u2026 -ing?","very polite","Would you mind sending it?"],
      ["Could you possibly \u2026?","formal","Could you possibly send it today?"]]},
    "examples":[{"en":"Would you mind reviewing this document?","note":"very polite"},
     {"en":"Could you possibly share the latest version?","note":"formal polite"},
     {"en":"I would really appreciate your feedback.","note":"formal thanks"}]},
   "phrases":[{"phrase":"Please find attached \u2026","use":"attachments"},{"phrase":"With reference to \u2026","use":"open formal"},
    {"phrase":"I'm following up on \u2026","use":"remind"},{"phrase":"As per our discussion, \u2026","use":"refer"}],
   "mistakes":[{"wrong":"Would you mind to send it?","right":"Would you mind sending it?","why":"WOULD YOU MIND + -ing."},
    {"wrong":"Please to find attached the file.","right":"Please find attached the file.","why":"No TO after PLEASE."}],
   "tip":"BCC the sensitive people, CC the informed people, TO only the action owners. Too many TO recipients = nobody takes action."
  },
  "passage":{"title":"A follow-up email","text":"Hi Marta,\n\nI hope you are well. I am following up on my email from last Monday about the firewall upgrade. I haven't heard back yet. Would you mind sending the approval as soon as possible? The maintenance window closes on Friday and I really need your sign-off to proceed.\n\nAlso, could you possibly confirm the budget for the extra licences? As per our last call, we agreed on 15 licences but the final purchase order needs your formal confirmation.\n\nPlease find attached the updated project plan. If you have any questions, I'd be happy to jump on a quick call this afternoon.\n\nThank you very much for your time.\n\nBest regards,\nCarlos",
   "wc":116,"source":"Original. Business-email conventions from the British Council Professional English course (britishcouncil.org, CC BY-NC-SA)."},
  "exercises":[
   {"type":"mcq","q":"What is Carlos chasing?","options":["a new laptop","the firewall approval","a salary raise","a meeting room"],"a":1,"explain":"'The firewall upgrade... the approval.'"},
   {"type":"tfng","q":"The maintenance window closes next Monday.","a":"F","explain":"'Closes on Friday.'"},
   {"type":"gap","q":"We agreed on ___ licences.","a":"15","alts":["15","fifteen"],"explain":"Number given."},
   {"type":"match",
    "pairs":[["Would you mind","very polite"],["Could you possibly","formal"],["Please find attached","file"],["I'd be happy to","offer"]]},
   {"type":"short","q":"Write a 3-line follow-up email.","model":"Model: Hi Ana, I'm following up on the report request from Monday. Would you mind sending the draft today? Thanks, Paolo."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"Would you mind ___ the draft?","options":["send","to send","sending","sent"],"a":2,"explain":"MIND + -ing."},
   {"type":"cloze","sentence":"Please find ___ the project plan.","a":"attached","alts":["attached","enclosed"],"explain":"Email collocation."},
   {"type":"word_form","base":"CONFIRM","sentence":"We need a formal ___ .","a":"confirmation","alts":["confirmation"],"explain":"-ation noun."}
  ]
 },
 11: { # Meetings in IT (USED TO)
  "notes":{
   "warmup":"IT meetings can be useful or painful. The difference is almost always agenda, time limit, and clear roles. Remote meetings especially need structure.",
   "grammar":{"title":"USED TO (past habits)",
    "rule":"USED TO + base verb describes a past habit or state that is no longer true. Negative and question use DIDN'T USE TO / DID YOU USE TO.",
    "table":{"head":["Form","Example"],
     "rows":[["used to + base","I used to work on-site every day."],
      ["didn't use to","We didn't use to have video calls."],
      ["Did \u2026 use to?","Did you use to attend daily standups?"]]},
    "examples":[{"en":"Before 2020, we used to meet in person.","note":"past habit, no longer true"},
     {"en":"I didn't use to like remote meetings, but now I do.","note":"change"},
     {"en":"We used to have a standup every morning.","note":"past routine"}]},
   "phrases":[{"phrase":"Let's get started.","use":"open a meeting"},{"phrase":"Can everyone hear me?","use":"audio check"},
    {"phrase":"Let's take this offline.","use":"move discussion"},{"phrase":"Any blockers?","use":"scrum question"}],
   "mistakes":[{"wrong":"We used to have meetings in person, don't we now.","right":"We used to have meetings in person, but now we don't.","why":"Contrast: BUT + clause."},
    {"wrong":"I didn't used to work from home.","right":"I didn't use to work from home.","why":"After DIDN'T: USE TO (no -d)."}],
   "tip":"If a standup takes more than 15 minutes, it is not a standup anymore. Move detailed discussions to a separate call."
  },
  "passage":{"title":"How meetings changed","text":"Five years ago, my team used to work together in the same office. We used to have a short morning meeting in the conference room. Everybody arrived with a coffee. The meeting lasted about 15 minutes. Then, in 2020, the pandemic changed everything. We started to work from home. We moved all meetings to video calls. At first, it was strange. I didn't use to turn on my camera; now I always do. We didn't use to share screens as much; now we share screens every day. Some things are better. We don't waste time in traffic. Some things are worse. It is harder to read body language on a small screen. Did you use to prefer in-person meetings? I did. Now I prefer hybrid.",
   "wc":139,"source":"Original. Remote-work trends consistent with Microsoft Work Trend Index public reports (microsoft.com/worklab)."},
  "exercises":[
   {"type":"mcq","q":"How long did the morning meetings use to last?","options":["5 minutes","15 minutes","30 minutes","1 hour"],"a":1,"explain":"'Lasted about 15 minutes.'"},
   {"type":"tfng","q":"The author always used to turn on the camera.","a":"F","explain":"'I didn't use to turn on my camera; now I always do.'"},
   {"type":"gap","q":"We didn't use to share ___ as much.","a":"screens","alts":["screens"],"explain":"From the text."},
   {"type":"match","pairs":[["before 2020","in person"],["2020","pandemic"],["now","hybrid"],["15 min","short meeting"]]},
   {"type":"short","q":"Describe one thing you used to do differently 3 years ago.","model":"Model: Three years ago I used to study in a library every afternoon. Now I study at home."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"I ___ work from home.","options":["didn't use to","don't used to","not use to","didn't used to"],"a":0,"explain":"Negative: DIDN'T USE TO."},
   {"type":"cloze","sentence":"We used ___ meet in the office every day.","a":"to","alts":["to"],"explain":"USED + TO + base."},
   {"type":"word_form","base":"MEET","sentence":"Today's ___ was too long.","a":"meeting","alts":["meeting"],"explain":"Verb \u2192 noun: -ing."}
  ]
 },
 12: { # Reporting IT problems (1st conditional)
  "notes":{
   "warmup":"A clear ticket saves everyone time. A vague ticket ('my computer is slow') generates five questions. A good ticket answers them in advance.",
   "grammar":{"title":"First conditional",
    "rule":"Form: IF + present simple, + WILL + base verb. Use for real or very likely future situations. The IF clause never uses WILL.",
    "table":{"head":["IF clause","Result","Example"],
     "rows":[["present simple","will + base","If you restart, the problem will probably disappear."],
      ["","","If I send the ticket now, they will answer tomorrow."],
      ["","","If the disk is full, the system will freeze."]]},
    "examples":[{"en":"If the attack continues, we will block the IP.","note":"action rule"},
     {"en":"If you don't update, your system won't be safe.","note":"negative consequence"},
     {"en":"If support doesn't reply, I will call.","note":"plan B"}]},
   "phrases":[{"phrase":"I'm having a problem with \u2026","use":"open ticket"},{"phrase":"The error message is \u2026","use":"evidence"},
    {"phrase":"I already tried \u2026","use":"what you did"},{"phrase":"The issue started \u2026","use":"timeline"}],
   "mistakes":[{"wrong":"If you will restart, the problem will go away.","right":"If you restart, the problem will go away.","why":"IF clause \u2192 no WILL."},
    {"wrong":"If the disk full, the system will freeze.","right":"If the disk is full, the system will freeze.","why":"Need the verb BE."}],
   "tip":"A good ticket has: (1) what you tried to do, (2) what actually happened, (3) the exact error message, (4) when it started, (5) what you already tried."
  },
  "passage":{"title":"Reporting a problem","text":"Hi helpdesk,\n\nI have a problem with my laptop. It started this morning. When I open Outlook, I get an error: 'Cannot connect to the Exchange server'. The message appears every time I start the computer. I already tried three things. First, I restarted the laptop. Second, I disconnected and reconnected to the Wi-Fi. Third, I opened Outlook on my phone \u2014 it works normally there. So the problem is only on the laptop.\n\nIf you can help me today, I will be very grateful. I have a client meeting at 3 p.m. and I need my email. If the issue continues after 2 p.m., I will use my phone as a backup.\n\nMy laptop ID is LP-4892. Let me know if you need more information.\n\nThanks,\nLaura",
   "wc":138,"source":"Original. Ticket structure from ITIL Foundation public material (itil.com, public docs)."},
  "exercises":[
   {"type":"mcq","q":"What is the error message?","options":["Disk is full","Cannot connect to the Exchange server","Wrong password","VPN disconnected"],"a":1,"explain":"Direct quote."},
   {"type":"tfng","q":"The problem happens on the phone too.","a":"F","explain":"'It works normally there.'"},
   {"type":"gap","q":"If the issue continues after 2 p.m., I ___ use my phone.","a":"will","alts":["will","'ll"],"explain":"First conditional result."},
   {"type":"match","pairs":[["Outlook","application"],["Exchange","email server"],["restart","step 1"],["Wi-Fi","step 2"]]},
   {"type":"short","q":"Write a 3-line ticket describing a real IT problem.","model":"Model: My Wi-Fi disconnects every 10 minutes at home since yesterday. I already restarted the router. I am using my mobile data now."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"If the disk ___ full, the system will freeze.","options":["will be","is","was","be"],"a":1,"explain":"IF + present simple."},
   {"type":"cloze","sentence":"If support doesn't reply, I ___ call.","a":"will","alts":["will","'ll"],"explain":"Result clause."},
   {"type":"word_form","base":"CONNECT","sentence":"Cannot ___ to the server.","a":"connect","alts":["connect"],"explain":"Base verb after 'cannot'."}
  ]
 },
 13: { # Cybersecurity first terms (passive simple)
  "notes":{
   "warmup":"Cybersecurity has its own vocabulary. Start with the CIA triad: Confidentiality, Integrity, Availability. Every control you ever build maps to one of these.",
   "grammar":{"title":"Passive voice (present and past simple)",
    "rule":"Form: object + BE + past participle. Use when the action matters more than the agent, or when the agent is unknown.",
    "table":{"head":["Tense","Active","Passive"],
     "rows":[["Present","Attackers send phishing.","Phishing is sent every day."],
      ["Past","Someone stole the data.","The data was stolen."],
      ["Modal","We must encrypt data.","Data must be encrypted."]]},
    "examples":[{"en":"Passwords are stored as hashes.","note":"present passive"},
     {"en":"The account was locked after 5 attempts.","note":"past passive"},
     {"en":"All logs must be reviewed daily.","note":"modal passive"}]},
   "phrases":[{"phrase":"Sensitive data must be encrypted.","use":"rule"},{"phrase":"Access is granted based on \u2026","use":"explain policy"},
    {"phrase":"The attack was blocked.","use":"report"},{"phrase":"Logs are reviewed daily.","use":"routine"}],
   "mistakes":[{"wrong":"The data is stole.","right":"The data is stolen.","why":"Past participle of STEAL = stolen."},
    {"wrong":"Passwords are store as hashes.","right":"Passwords are stored as hashes.","why":"Past participle: stored."}],
   "tip":"CIA triad: if you can remember only three letters in cybersecurity, these are the ones. Confidentiality, Integrity, Availability."
  },
  "passage":{"title":"The CIA triad","text":"In cybersecurity, three ideas are more important than anything else: Confidentiality, Integrity, and Availability. This is called the CIA triad. Confidentiality means data is only seen by authorised people. For example, passwords are stored as hashes, not as plain text. Integrity means data is not changed in a bad way. If a file is modified by an attacker, integrity is lost. Checksums and digital signatures are used to detect changes. Availability means systems work when we need them. If a service is attacked by a DDoS, availability is lost. The three goals often conflict. Stronger access controls protect confidentiality but can reduce availability for legitimate users. Every control in security is a trade-off. When you design a system, the CIA triad is always in the background.",
   "wc":143,"source":"Adapted from NIST SP 800-12 'An Introduction to Information Security' (nist.gov, PD)."},
  "exercises":[
   {"type":"mcq","q":"What does CIA stand for?","options":["Central Intelligence Agency","Confidentiality, Integrity, Availability","Control, Identity, Access","Cyber, Internet, Access"],"a":1,"explain":"Direct definition."},
   {"type":"tfng","q":"Availability means data is not changed.","a":"F","explain":"That is Integrity. Availability = systems work."},
   {"type":"gap","q":"Passwords are stored as ___ , not plain text.","a":"hashes","alts":["hashes"],"explain":"From the text."},
   {"type":"match",
    "pairs":[["Confidentiality","data visibility"],["Integrity","data accuracy"],["Availability","system uptime"],["DDoS","availability attack"]]},
   {"type":"short","q":"Give one example of each CIA goal.","model":"Model: Confidentiality: password hashing. Integrity: file checksums. Availability: DDoS protection."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"Passwords ___ as hashes.","options":["are stored","are store","stores","is stored"],"a":0,"explain":"Present passive + plural subject."},
   {"type":"cloze","sentence":"The data was ___ by an attacker.","a":"stolen","alts":["stolen"],"explain":"Past participle of STEAL."},
   {"type":"word_form","base":"ENCRYPT","sentence":"All sensitive files need ___ .","a":"encryption","alts":["encryption"],"explain":"Verb \u2192 noun: -tion."}
  ]
 },
 14: { # Phishing awareness
  "notes":{
   "warmup":"Phishing is the #1 cause of real data breaches. Attackers don't break in through complex exploits \u2014 they ask users to open the door. Awareness is the best defence.",
   "grammar":{"title":"Second conditional (basic)",
    "rule":"Form: IF + past simple, + WOULD + base verb. Use for imaginary or unlikely situations in the present/future.",
    "table":{"head":["IF clause","Result","Example"],
     "rows":[["past simple","would + base","If I received this email, I would report it."],
      ["","","If the URL were strange, you'd check it."],
      ["","","If everyone followed this, phishing would fail."]]},
    "examples":[{"en":"If my bank sent an email like this, I would call them first.","note":"imaginary situation"},
     {"en":"If the domain were legitimate, it would end in .bank.com, not .bankk.com.","note":"hypothesis"}]},
   "phrases":[{"phrase":"Don't click on links.","use":"instruction"},{"phrase":"Check the sender.","use":"verification"},
    {"phrase":"Hover over the link.","use":"technique"},{"phrase":"Report the email.","use":"action"}],
   "mistakes":[{"wrong":"If I would receive this, I would report it.","right":"If I received this, I would report it.","why":"IF clause \u2192 past simple, not WOULD."},
    {"wrong":"If he was a hacker, he would succeed.","right":"If he were a hacker, he would succeed.","why":"Formal second conditional uses WERE for all persons (though WAS is accepted informally)."}],
   "tip":"When in doubt, do not click. Open your browser and go to the real site yourself. The 2 minutes you lose are cheaper than a compromised account."
  },
  "passage":{"title":"A phishing email","text":"Yesterday I received a strange email. It said: 'Your bank account will be blocked in 24 hours. Click here to verify your password.' The tone was urgent. The sender was 'security at my-bank-support dot com'. My real bank is called 'Banco Capital' and its domain is 'bancocapital.pe'. So the email was not from my bank. I checked the link without clicking. I hovered over it. The URL was 'my-bank-support.biz/login'. That is not a bank URL. It was a phishing email. If I had clicked, the page would have asked for my password and sent it to the attacker. I reported the email to my IT team. They blocked the sender and warned the company. Always remember: banks never ask for your password by email.",
   "wc":142,"source":"Adapted from FBI 'Common Scams' (fbi.gov, PD) and CISA phishing awareness materials (cisa.gov, PD)."},
  "exercises":[
   {"type":"mcq","q":"How did the author check the link?","options":["clicked it","hovered over it","copied it","asked the bank"],"a":1,"explain":"'I hovered over it.'"},
   {"type":"tfng","q":"The author's real bank domain is 'my-bank-support.biz'.","a":"F","explain":"'Real domain is bancocapital.pe.'"},
   {"type":"gap","q":"If the email were real, it would come from the ___ domain.","a":"real","alts":["real","legitimate"],"explain":"Second conditional."},
   {"type":"match",
    "pairs":[["urgent tone","phishing tactic"],["wrong domain","red flag"],["hover","check technique"],["report","defensive action"]]},
   {"type":"short","q":"Write 3 red flags of phishing emails.","model":"Model: 1) Urgent tone demanding immediate action. 2) A sender that does not match the real company domain. 3) A link that asks for your password or personal data."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"If I ___ this email, I would report it.","options":["receive","would receive","received","am receiving"],"a":2,"explain":"Second conditional IF: past simple."},
   {"type":"cloze","sentence":"If the domain were legitimate, you ___ click safely.","a":"could","alts":["could","would","would be able to"],"explain":"Possibility in 2nd cond."},
   {"type":"word_form","base":"PHISH","sentence":"We received a ___ email today.","a":"phishing","alts":["phishing"],"explain":"Verb \u2192 adj/-ing."}
  ]
 },
 15: { # Backup and recovery
  "notes":{
   "warmup":"Backups are like insurance: boring until you need them. A backup you never tested is not a backup \u2014 it is a hope. Test recovery regularly.",
   "grammar":{"title":"SHOULD HAVE + past participle (regret / criticism)",
    "rule":"SHOULD HAVE + past participle expresses a regret about the past ('I should have backed up') or a criticism ('You should have backed up'). Negative: SHOULDN'T HAVE.",
    "table":{"head":["Form","Use","Example"],
     "rows":[["should have + p.p.","regret","I should have made a backup."],
      ["shouldn't have + p.p.","criticism","We shouldn't have ignored the alert."],
      ["Should I have \u2026?","question","Should I have kept the old server?"]]},
    "examples":[{"en":"We should have tested the restore last month.","note":"regret"},
     {"en":"You shouldn't have deleted the old copy before verifying.","note":"criticism"},
     {"en":"They should have followed the 3-2-1 rule.","note":"regret/criticism"}]},
   "phrases":[{"phrase":"We lost the data.","use":"state a problem"},{"phrase":"The backup is corrupt.","use":"describe failure"},
    {"phrase":"Restore from Friday's backup.","use":"recovery action"},{"phrase":"Verify the checksum.","use":"integrity check"}],
   "mistakes":[{"wrong":"I should made a backup.","right":"I should have made a backup.","why":"SHOULD + HAVE + past participle."},
    {"wrong":"You shouldn't to have deleted it.","right":"You shouldn't have deleted it.","why":"No TO between SHOULDN'T and HAVE."}],
   "tip":"3-2-1 rule: 3 copies of your data, on 2 different media, with 1 copy offsite (or offline). Ransomware eats online backups; an offline one saves you."
  },
  "passage":{"title":"A bad day","text":"Last Friday, our main database server crashed. The disk failed at 11 p.m. Nobody was in the office. On Saturday morning, the team started the recovery. We had a backup from Thursday night. 'Thursday is fine', said the manager. 'We will lose only one day of data.' But when we tried to restore, the backup was corrupt. Nobody had tested a restore for six months. We should have tested it weekly. We should have verified the checksums. We spent the whole weekend trying different backup files. Finally, we used a backup from two weeks before. We lost two weeks of work. On Monday, the CEO was angry. Now, every week, a team member tests one random backup. We also moved to the 3-2-1 rule. We shouldn't have ignored the warnings.",
   "wc":147,"source":"Adapted from CISA 'Data Backup Options' and the Veeam 3-2-1-1-0 rule public materials (veeam.com, public)."},
  "exercises":[
   {"type":"mcq","q":"How old was the backup they finally used?","options":["1 day","1 week","2 weeks","1 month"],"a":2,"explain":"'We used a backup from two weeks before.'"},
   {"type":"tfng","q":"The Thursday backup was perfect.","a":"F","explain":"'The backup was corrupt.'"},
   {"type":"gap","q":"We should have tested the restore ___ .","a":"weekly","alts":["weekly"],"explain":"From the text."},
   {"type":"match",
    "pairs":[["3-2-1","backup rule"],["checksum","verify"],["corrupt","backup failure"],["offline","ransomware defence"]]},
   {"type":"short","q":"Write 2 lessons learned from this story.","model":"Model: 1) Test restores regularly, not just backups. 2) Follow the 3-2-1 rule and keep one backup offline."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"We ___ tested the backup.","options":["should have","should","would","are supposed"],"a":0,"explain":"Past regret: should have."},
   {"type":"cloze","sentence":"You shouldn't ___ deleted the old copy.","a":"have","alts":["have"],"explain":"SHOULDN'T + HAVE."},
   {"type":"word_form","base":"RECOVER","sentence":"The ___ took the whole weekend.","a":"recovery","alts":["recovery"],"explain":"Verb \u2192 noun."}
  ]
 },
 16: { # Data vs information vs knowledge
  "notes":{
   "warmup":"Data, information, knowledge, wisdom \u2014 the DIKW pyramid. At each level, the data becomes more useful. Understanding the hierarchy helps you build good reports and dashboards.",
   "grammar":{"title":"Relative pronouns: THAT / WHICH / WHO",
    "rule":"Use WHO for people, WHICH for things (formal), THAT for both (more common). Defining clauses \u2192 no comma. Non-defining clauses \u2192 use commas.",
    "table":{"head":["Pronoun","Refers to","Example"],
     "rows":[["who","people","The analyst who wrote this report is junior."],
      ["which","things (formal)","The dataset, which was cleaned yesterday, is ready."],
      ["that","both","The tool that we use is Power BI."]]},
    "examples":[{"en":"Data that has no context is useless.","note":"defining"},
     {"en":"The dashboard, which took 3 weeks to build, is now live.","note":"non-defining"},
     {"en":"The manager who requested the report is on leave.","note":"defining, person"}]},
   "phrases":[{"phrase":"The raw data shows \u2026","use":"report"},{"phrase":"If we interpret this, \u2026","use":"go to information"},
    {"phrase":"What this means is \u2026","use":"explain"},{"phrase":"Based on this, we recommend \u2026","use":"call to action"}],
   "mistakes":[{"wrong":"The report what I wrote.","right":"The report that I wrote.","why":"'What' is not a relative pronoun here."},
    {"wrong":"The analyst, who wrote this report, is junior.","right":"The analyst who wrote this report is junior.","why":"Defining clause \u2192 no commas."}],
   "tip":"Data without context is noise. Information without insight is trivia. Dashboards that only show 'what happened' are incomplete \u2014 they should also show 'so what'."
  },
  "passage":{"title":"DIKW in practice","text":"Every day our monitoring tool collects millions of data points. On Monday, one number jumped: CPU usage on server A was 92%. That is raw data. It means nothing by itself. Then an analyst who knows the system added context: 'CPU usage is usually 30% on Monday mornings.' Now we have information. Then a senior engineer who had seen this before added knowledge: 'A pattern like this usually means a runaway backup job'. Now we can act. Finally, wisdom: the team decided to add an alert that triggers when CPU stays above 80% for more than 10 minutes. This is the DIKW pyramid: Data, Information, Knowledge, Wisdom. Each step takes the previous one and adds value. A good observability platform supports every step, not just the raw data collection that most tools offer.",
   "wc":140,"source":"Original. DIKW model widely attributed to Russell Ackoff (1989); monitoring example is typical SRE practice."},
  "exercises":[
   {"type":"mcq","q":"What was the raw data point?","options":["CPU 30%","CPU 92%","disk full","network down"],"a":1,"explain":"'CPU usage on server A was 92%.'"},
   {"type":"tfng","q":"The senior engineer recognised a pattern.","a":"T","explain":"'A pattern like this usually means a runaway backup.'"},
   {"type":"gap","q":"An alert triggers when CPU stays above 80% for more than ___ minutes.","a":"10","alts":["10","ten"],"explain":"From the text."},
   {"type":"match","pairs":[["Data","raw 92%"],["Information","context"],["Knowledge","pattern"],["Wisdom","alert rule"]]},
   {"type":"short","q":"Give an example of DIKW from your own life.","model":"Model: Data: your phone battery is 20%. Information: you usually charge at 30%. Knowledge: you have 2 hours left. Wisdom: always carry a cable."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"The analyst ___ wrote the report is junior.","options":["which","who","what","whose"],"a":1,"explain":"Person \u2192 WHO."},
   {"type":"cloze","sentence":"The dataset, ___ was cleaned yesterday, is ready.","a":"which","alts":["which"],"explain":"Non-defining, thing \u2192 WHICH."},
   {"type":"word_form","base":"OBSERVE","sentence":"A good ___ platform supports every step.","a":"observability","alts":["observability"],"explain":"Verb \u2192 noun: -ability."}
  ]
 },
 17: { # Describing processes
  "notes":{
   "warmup":"Every IT process has a start, a series of steps, and an end. Describing processes clearly is a core skill \u2014 for documentation, for training, and for incident reports.",
   "grammar":{"title":"Sequence connectors + simple passive",
    "rule":"Use sequence words (first, then, next, after that, finally) to show order. Use passive voice when the actor is not important: 'The ticket is assigned to a team.'",
    "table":{"head":["Connector","Use","Example"],
     "rows":[["First,","start","First, the user submits a ticket."],
      ["Then / Next,","continue","Then, the ticket is assigned to a team."],
      ["After that,","middle","After that, the engineer investigates."],
      ["Finally,","end","Finally, the ticket is closed."]]},
    "examples":[{"en":"First, the alert is received by the SIEM.","note":"passive + sequence"},
     {"en":"Then, an analyst opens a case.","note":"active"},
     {"en":"Finally, the incident is documented.","note":"passive"}]},
   "phrases":[{"phrase":"The process starts when \u2026","use":"open"},{"phrase":"This triggers \u2026","use":"cause"},
    {"phrase":"Once X is done, Y \u2026","use":"dependency"},{"phrase":"The process ends with \u2026","use":"close"}],
   "mistakes":[{"wrong":"After that, then, the engineer investigates.","right":"After that, the engineer investigates.","why":"Don't combine two sequence markers."},
    {"wrong":"The ticket is assign to a team.","right":"The ticket is assigned to a team.","why":"Passive needs past participle."}],
   "tip":"When you document a process, draw it first. A diagram shows dependencies that text hides. Even a rough flow on paper helps."
  },
  "passage":{"title":"Our incident process","text":"Our company has a clear incident response process. First, an alert is generated by the monitoring system. For example, a high CPU alarm or a failed login. Then, the alert is sent to the on-call engineer. After that, the engineer checks the logs and decides the severity. If the severity is high, the engineer opens a formal incident. Next, a war room call is started. The communication team is notified. They inform the users. Then, the problem is investigated and a fix is applied. Once the service is restored, the engineer writes an update for the customers. Finally, a post-incident review is scheduled within 48 hours. All incidents are documented in a shared database, so the team can learn from them. Good documentation is the key to improving the process.",
   "wc":140,"source":"Adapted from NIST SP 800-61 Rev 2 (nist.gov, PD) and Google SRE Book public chapters (sre.google, CC BY-NC-ND)."},
  "exercises":[
   {"type":"mcq","q":"When is the post-incident review scheduled?","options":["within 24 hours","within 48 hours","in one week","never"],"a":1,"explain":"'Within 48 hours.'"},
   {"type":"tfng","q":"The communication team informs the users.","a":"T","explain":"Explicit."},
   {"type":"gap","q":"The alert is ___ to the on-call engineer.","a":"sent","alts":["sent"],"explain":"Passive."},
   {"type":"match","pairs":[["1","alert generated"],["2","engineer checks"],["3","war room"],["4","fix applied"],["5","post-incident review"]]},
   {"type":"short","q":"Describe a simple process you do every day in 4 steps.","model":"Model: First, I wake up. Then, I have breakfast. After that, I go to work. Finally, I start my emails."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"The ticket ___ to a team automatically.","options":["is assigned","is assign","assigns","assign"],"a":0,"explain":"Passive present."},
   {"type":"cloze","sentence":"___ , the engineer investigates the problem.","a":"Then","alts":["Then","Next","After that"],"explain":"Sequence."},
   {"type":"word_form","base":"DOCUMENT","sentence":"Good ___ is key to improving the process.","a":"documentation","alts":["documentation"],"explain":"-ation noun."}
  ]
 },
 18: { # Comparing devices (adjective + enough/too)
  "notes":{
   "warmup":"Before you buy a device \u2014 laptop, phone, server \u2014 you compare specs. Good comparison uses the right grammar and the right criteria, not only the price.",
   "grammar":{"title":"ENOUGH and TOO",
    "rule":"TOO + adjective = more than needed (negative). Adjective + ENOUGH = the right amount. ENOUGH + noun = sufficient quantity.",
    "table":{"head":["Structure","Meaning","Example"],
     "rows":[["too + adj","excess","This laptop is too heavy."],
      ["adj + enough","sufficient","The battery is good enough."],
      ["enough + noun","sufficient quantity","We don't have enough storage."],
      ["too + adj + to + V","excess for action","It's too slow to run Docker."]]},
    "examples":[{"en":"This laptop is too expensive for a junior.","note":"excess"},
     {"en":"4 GB of RAM is not enough for modern work.","note":"not sufficient"},
     {"en":"The new model is fast enough for us.","note":"sufficient quality"}]},
   "phrases":[{"phrase":"The main advantage is \u2026","use":"pros"},{"phrase":"On the downside, \u2026","use":"cons"},
    {"phrase":"For our needs, \u2026","use":"match"},{"phrase":"Value for money is \u2026","use":"price judgment"}],
   "mistakes":[{"wrong":"It is too much expensive.","right":"It is too expensive.","why":"TOO + adjective directly, no MUCH."},
    {"wrong":"I have enough much money.","right":"I have enough money.","why":"Don't combine ENOUGH and MUCH."}],
   "tip":"When you compare devices, list the top 3 specs that really matter for your use case. For a dev laptop: RAM, CPU, screen. The rest is secondary."
  },
  "passage":{"title":"Choosing a new laptop","text":"My company gave me a budget to choose a new laptop. I compared three models. Model A was a ThinkPad. It had 16 GB of RAM, a good keyboard, and a solid build. The battery was good enough for a full day. It was not too expensive. Model B was a MacBook Air. It was beautiful and very fast. But it was too expensive for my budget. The storage was also a little small: only 256 GB. Model C was a Dell XPS. It was modern, light, and powerful. The CPU was fast enough for any task. But the battery was too short \u2014 only 5 hours. In the end, I chose the ThinkPad. It was not the prettiest, but it had enough RAM, enough storage, enough battery. For a working engineer, 'enough' is usually the right answer.",
   "wc":152,"source":"Original. Laptop evaluation criteria based on typical enterprise procurement practices."},
  "exercises":[
   {"type":"mcq","q":"Which laptop did the author choose?","options":["MacBook Air","Dell XPS","ThinkPad","None"],"a":2,"explain":"'In the end, I chose the ThinkPad.'"},
   {"type":"tfng","q":"The MacBook was affordable for the author.","a":"F","explain":"'It was too expensive for my budget.'"},
   {"type":"gap","q":"The Dell battery was only ___ hours.","a":"5","alts":["5","five"],"explain":"From the text."},
   {"type":"match","pairs":[["ThinkPad","chosen"],["MacBook","too expensive"],["Dell","short battery"],["Budget","mid-range"]]},
   {"type":"short","q":"Compare 2 phones you know briefly.","model":"Model: iPhone is smooth and well made but too expensive. Samsung Galaxy has enough features at half the price."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"The battery is ___ for a full day.","options":["enough good","good enough","too good","enough of good"],"a":1,"explain":"adj + ENOUGH."},
   {"type":"cloze","sentence":"The laptop is ___ expensive for me.","a":"too","alts":["too"],"explain":"Excess."},
   {"type":"word_form","base":"AFFORD","sentence":"The price is ___ for me.","a":"affordable","alts":["affordable"],"explain":"Verb \u2192 adjective: -able."}
  ]
 },
 19: { # Writing a tech CV (present perfect intro)
  "notes":{
   "warmup":"A CV is a marketing document. It sells you in 30 seconds. Use the present perfect for achievements that matter today. Use numbers: 'reduced latency by 40%' is better than 'improved latency'.",
   "grammar":{"title":"Present perfect (introduction)",
    "rule":"Form: HAVE / HAS + past participle. Use for experiences, achievements, and recent events connected to now. Often with: ever, never, already, just, yet, for, since.",
    "table":{"head":["Structure","Example","Meaning"],
     "rows":[["S + have/has + p.p.","I have worked with AWS.","experience"],
      ["S + have just + p.p.","She has just joined.","very recent"],
      ["S + have never + p.p.","We have never used Oracle.","life experience"],
      ["How long + have \u2026?","How long have you worked here?","duration question"]]},
    "examples":[{"en":"I have built three production apps.","note":"achievement"},
     {"en":"She has led a team of 5 engineers.","note":"experience"},
     {"en":"We have just released v3.","note":"just + p.p."}]},
   "phrases":[{"phrase":"I have X years of experience in \u2026","use":"experience claim"},{"phrase":"I have delivered \u2026","use":"achievement"},
    {"phrase":"I have led \u2026","use":"leadership"},{"phrase":"I have reduced \u2026 by X%","use":"impact with number"}],
   "mistakes":[{"wrong":"I have work at this company since 3 years.","right":"I have worked at this company for 3 years.","why":"FOR + duration; SINCE + point in time."},
    {"wrong":"She has build 3 apps.","right":"She has built 3 apps.","why":"Past participle of BUILD = built."}],
   "tip":"Quantify every achievement possible. 'Migrated 50 services to Kubernetes' beats 'migrated services to Kubernetes'."
  },
  "passage":{"title":"A polished CV summary","text":"My name is Ana Torres. I have worked as a systems engineer for five years. I have designed and maintained production systems on AWS, Azure, and Kubernetes. I have led two successful cloud migrations, moving over 40 services from on-premise to the cloud. I have reduced our monthly cloud bill by 30% through right-sizing and reserved instances. I have also written internal documentation that has been used by 20 new engineers. I have passed three certifications: AWS Solutions Architect Associate, CKA, and Terraform Associate. I have never managed a team formally, but I have mentored four junior engineers in the last two years. I am looking for a senior role where I can grow into formal leadership while staying close to the technology. I have attached my detailed CV below.",
   "wc":138,"source":"Original. CV writing guidance from LinkedIn Learning 'Writing a Great CV' course (linkedin.com/learning, public summaries)."},
  "exercises":[
   {"type":"mcq","q":"How much did Ana reduce the monthly cloud bill?","options":["15%","30%","40%","50%"],"a":1,"explain":"'By 30%.'"},
   {"type":"tfng","q":"Ana has formally managed a team.","a":"F","explain":"'I have never managed a team formally.'"},
   {"type":"gap","q":"She has led two ___ cloud migrations.","a":"successful","alts":["successful"],"explain":"From the text."},
   {"type":"match",
    "pairs":[["5 years","experience"],["40 services","migration"],["30%","cost saving"],["3","certifications"]]},
   {"type":"short","q":"Write 3 sentences about your own achievements using present perfect.","model":"Model: I have studied English for two years. I have completed three online courses. I have built my first website this month."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"I ___ as a systems engineer for 5 years.","options":["have worked","worked","am working","was working"],"a":0,"explain":"Duration up to now \u2192 present perfect."},
   {"type":"cloze","sentence":"I have reduced the bill ___ 30%.","a":"by","alts":["by"],"explain":"'By + percentage'."},
   {"type":"word_form","base":"MIGRATE","sentence":"We completed the cloud ___ last year.","a":"migration","alts":["migration"],"explain":"-tion noun."}
  ]
 },
 20: { # Mock KET / A2 exam
  "notes":{
   "warmup":"You are ready for A2 Key. The exam has three papers: Reading & Writing (60 min), Listening (30 min), and Speaking (10 min per pair). This lesson reviews strategies.",
   "grammar":{"title":"A2 grammar recap",
    "rule":"A2 combines: present simple and continuous, past simple, comparatives, modals (should, must, can, have to), first conditional, basic passive, relative pronouns.",
    "table":{"head":["Area","Example"],
     "rows":[["Present simple","She works at a bank."],["Past simple","They migrated the servers last year."],
      ["Comparatives","Linux is more flexible than Windows."],["1st conditional","If the disk is full, the system will freeze."],
      ["Passive","Passwords are stored as hashes."]]},
    "examples":[{"en":"The meeting was moved to Wednesday at 11.","note":"past passive + prepositions"},
     {"en":"If the email is suspicious, I will report it.","note":"first conditional"},
     {"en":"Python is easier than C++ for beginners.","note":"comparative"}]},
   "phrases":[{"phrase":"I'd like to say that \u2026","use":"polite opinion"},{"phrase":"As far as I know, \u2026","use":"hedge"},
    {"phrase":"It depends on \u2026","use":"conditional answer"},{"phrase":"Could you repeat the question, please?","use":"clarify"}],
   "mistakes":[{"wrong":"I am agree with you.","right":"I agree with you.","why":"AGREE is a verb, no BE."},
    {"wrong":"I am having a laptop.","right":"I have a laptop.","why":"HAVE for possession \u2192 simple, not continuous."}],
   "tip":"In the A2 Speaking test, extend your answers: don't just say 'yes' or 'no'. Add a reason: 'Yes, because I \u2026'. Examiners reward extended answers."
  },
  "passage":{"title":"Ready for A2","text":"This is my last lesson before the A2 exam. My name is Diego. I have studied English for one year. I have learned many things. I know how to introduce myself, describe my job, talk about the past, and write emails. I also know the basics of cybersecurity vocabulary in English. Last month I did a practice test. I got 75% in Reading & Writing, 70% in Listening, and the teacher gave me a good score in Speaking. If I keep practising, I will pass. My plan is: review vocabulary every day for 30 minutes, do one practice test every Saturday, and record myself speaking about IT topics every Sunday. The exam is in three weeks. If I prepare well, I am going to be ready. My next goal is B1 and then B2 by 2028. English is now a key part of my career.",
   "wc":152,"source":"Original. KET exam structure from Cambridge Assessment English public handbooks."},
  "exercises":[
   {"type":"mcq","q":"What is Diego's reading score?","options":["60%","70%","75%","80%"],"a":2,"explain":"'75% in Reading & Writing.'"},
   {"type":"tfng","q":"Diego will take the exam next week.","a":"F","explain":"'The exam is in three weeks.'"},
   {"type":"gap","q":"My next goal is ___ and then B2 by 2028.","a":"B1","alts":["B1"],"explain":"From the text."},
   {"type":"match","pairs":[["Reading","75%"],["Listening","70%"],["Speaking","good score"],["Goal","B1 \u2192 B2"]]},
   {"type":"short","q":"Write a 4-sentence plan for your own A2 preparation.","model":"Model: I will review vocabulary every morning for 20 minutes. I will watch one VOA video every night. I will do a practice test on Saturdays. I will record my Speaking on Sundays."}
  ],
  "uoe":[
   {"type":"mc_cloze","sentence":"I ___ English for one year.","options":["study","have studied","am studying","studied"],"a":1,"explain":"Duration to now."},
   {"type":"cloze","sentence":"If I prepare ___ , I will be ready.","a":"well","alts":["well"],"explain":"Irregular adverb."},
   {"type":"word_form","base":"PREPARE","sentence":"Exam ___ takes time.","a":"preparation","alts":["preparation"],"explain":"Verb \u2192 noun: -ation."}
  ]
 },
},
}

# ---- MERGE ----
path = Path(r"E:\CLAUDE\PAOLO BACA MANRIQUE\course-app\course_data.json")
course = json.loads(path.read_text(encoding="utf-8"))

merged_lessons = 0
for level in course["levels"]:
    code = level["code"]
    for lesson in level["lessons"]:
        entry = EXP.get(code, {}).get(lesson["n"])
        if not entry:
            continue
        # Only fill lessons that don't have pilot content yet
        if lesson.get("has_content"):
            continue
        # lesson_notes
        if entry.get("notes"):
            lesson["lesson_notes"] = entry["notes"]
        # passage
        if entry.get("passage"):
            p = entry["passage"]
            lesson["passage"] = {
                "title": p.get("title", lesson["topic"]),
                "text": p["text"],
                "word_count": p.get("wc", len(p["text"].split())),
                "source": p["source"],
            }
        # exercises
        if entry.get("exercises"):
            lesson["exercises"] = entry["exercises"]
        # use_of_english
        if entry.get("uoe"):
            lesson["use_of_english"] = entry["uoe"]
        lesson["has_content"] = True
        merged_lessons += 1

path.write_text(json.dumps(course, ensure_ascii=False, indent=1), encoding="utf-8")

# stats
print(f"OK: Added full content to {merged_lessons} lessons")
for lv in course["levels"]:
    filled = sum(1 for le in lv["lessons"] if le.get("has_content"))
    notes = sum(1 for le in lv["lessons"] if le.get("lesson_notes"))
    uoe = sum(len(le.get("use_of_english",[])) for le in lv["lessons"])
    print(f"  {lv['code']}: {filled}/20 lessons with content, {notes} with teaching notes, {uoe} UoE exercises")
