# -*- coding: utf-8 -*-
"""
Lesson notes (teaching content) for the 30 pilot lessons.
Each lesson has: warmup, grammar (rule + table + examples), key phrases,
common mistakes, and a pedagogical tip \u2013 calibrated to CEFR level.
"""
import json
from pathlib import Path

NOTES = {
# =========================================================================
"A1": {
 1: {
  "warmup":"In IT companies, people introduce themselves many times every week: to new users, to new colleagues, in meetings. Good self-introductions are short, clear and contain only the basics: name, role, team, city.",
  "grammar":{
   "title":"Verb BE (present) + the article A / AN",
   "rule":"Use the verb BE to describe identity, job, age and nationality. Use 'a' before consonant sounds and 'an' before vowel sounds.",
   "table":{
    "head":["Subject","Form","Example"],
    "rows":[
     ["I","am","I am Juan."],
     ["You","are","You are on my team."],
     ["He / She / It","is","She is my manager."],
     ["We / They","are","We are engineers."],
    ]
   },
   "examples":[
    {"en":"I am a systems engineer.","note":"A \u2192 before /s/ consonant sound"},
    {"en":"She is an analyst.","note":"AN \u2192 before /\u00e6/ vowel sound"},
    {"en":"They are on my team.","note":"plural subject \u2192 ARE"},
   ]
  },
  "phrases":[
   {"phrase":"My name is \u2026","use":"to give your name"},
   {"phrase":"I am from \u2026","use":"to say your country or city"},
   {"phrase":"I work at \u2026","use":"to say the company"},
   {"phrase":"Nice to meet you.","use":"first-time greeting"},
  ],
  "mistakes":[
   {"wrong":"I am engineer.","right":"I am an engineer.","why":"Use A or AN with a job."},
   {"wrong":"She are my manager.","right":"She is my manager.","why":"He/She/It \u2192 IS, not ARE."},
  ],
  "tip":"In IT introductions, say your role first: 'I am a junior systems engineer.' It is more useful than just your name."
 },
 2: {
  "warmup":"IT workers spell things many times a day: URLs, emails, passwords, product names. On the phone, bad spelling causes real problems. This is why engineers use the NATO alphabet and clear names for symbols.",
  "grammar":{
   "title":"Basic plurals + the NATO alphabet",
   "rule":"To say letters clearly, we replace them with a known word: B \u2192 Bravo, S \u2192 Sierra. For symbols in URLs and emails, we use short names: @ = at, . = dot, / = slash.",
   "table":{
    "head":["Symbol","Say it","Example"],
    "rows":[
     ["@","at","paolo@gmail.com \u2192 paolo at gmail dot com"],
     [".","dot","nist.gov \u2192 nist dot gov"],
     ["/","slash","/home/user \u2192 slash home slash user"],
     ["-","dash / hyphen","en-US \u2192 en dash U S"],
     ["_","underscore","log_file \u2192 log underscore file"],
    ]
   },
   "examples":[
    {"en":"My email is paolo at gmail dot com.","note":"standard email spelling"},
    {"en":"That is Bravo, one, two, Charlie.","note":"spelling a code over the phone"},
   ]
  },
  "phrases":[
   {"phrase":"Can you spell that, please?","use":"to ask for spelling"},
   {"phrase":"It is spelled \u2026","use":"before giving letters"},
   {"phrase":"One more time, slowly.","use":"ask to repeat"},
   {"phrase":"In lower case.","use":"not capital letters"},
  ],
  "mistakes":[
   {"wrong":"My email is at paolo gmail punto com.","right":"My email is paolo at gmail dot com.","why":"In English: 'at' comes between user and domain; '.' = dot."},
   {"wrong":"B like boy.","right":"B like Bravo.","why":"Use the NATO word, not a random one."},
  ],
  "tip":"For 0 (zero) and O (letter O), say 'zero' and 'O as in Oscar'. They look the same but sound different."
 },
 3: {
  "warmup":"Software versions look like numbers, but they tell a story. Big number = big change (maybe not compatible). Small number = only a small fix. Knowing this helps you decide when to update.",
  "grammar":{
   "title":"Cardinals, ordinals and semantic versioning",
   "rule":"Cardinals count things (one, two, three). Ordinals put things in order (first, second, third). Versions use cardinals: MAJOR.MINOR.PATCH. The second Tuesday of the month is an ordinal use.",
   "table":{
    "head":["Cardinal","Ordinal","Use"],
    "rows":[
     ["one","first (1st)","the first release"],
     ["two","second (2nd)","the second Tuesday"],
     ["three","third (3rd)","the third update"],
     ["four \u2026 twelve","fourth \u2026 twelfth","the twelfth minor version"],
    ]
   },
   "examples":[
    {"en":"Python 3.12.4 \u2192 'three twelve four'.","note":"read dots out loud"},
    {"en":"Patch Tuesday is the second Tuesday.","note":"second = ordinal"},
   ]
  },
  "phrases":[
   {"phrase":"We are on version \u2026","use":"to say the current version"},
   {"phrase":"The latest update is \u2026","use":"newest release"},
   {"phrase":"Please update to \u2026","use":"request"},
  ],
  "mistakes":[
   {"wrong":"Version three point twelve point four.","right":"Version three twelve four.","why":"'Point' is for decimals; in versions we just say the numbers."},
   {"wrong":"On second of Tuesday.","right":"On the second Tuesday.","why":"Ordinal + noun, not 'of'."},
  ],
  "tip":"Write 'v1.2.3' when you write, say 'version one two three' when you speak. Never say 'v dot'."
 },
 4: {
  "warmup":"The words inside a computer are the same in every country. CPU, RAM, SSD, monitor \u2014 all come from English. Knowing their functions helps you explain problems to a helpdesk anywhere in the world.",
  "grammar":{
   "title":"There is / there are",
   "rule":"Use 'there is' + singular noun, 'there are' + plural noun. Use this structure to describe what exists in a place. Negative: 'there isn't / there aren't'.",
   "table":{
    "head":["Form","Use","Example"],
    "rows":[
     ["there is (there's)","+ singular","There is a fan inside the tower."],
     ["there are","+ plural","There are two USB ports."],
     ["there isn't","negative singular","There isn't a webcam."],
     ["there aren't","negative plural","There aren't any HDMI cables."],
     ["Is there \u2026 ? / Are there \u2026 ?","questions","Is there a power button on the front?"],
    ]
   },
   "examples":[
    {"en":"There is a CPU and a GPU inside.","note":"singular \u2192 there IS"},
    {"en":"There are many cables behind the tower.","note":"plural \u2192 there ARE"},
   ]
  },
  "phrases":[
   {"phrase":"How many \u2026 are there?","use":"count something"},
   {"phrase":"There are no \u2026","use":"describe absence"},
   {"phrase":"The CPU is the brain.","use":"explain function"},
  ],
  "mistakes":[
   {"wrong":"It has two CPU.","right":"There are two CPUs.","why":"Plural = add -s; use 'there are' for existence."},
   {"wrong":"There is two fans.","right":"There are two fans.","why":"Plural noun \u2192 ARE."},
  ],
  "tip":"Learn the function, not just the name. CPU = brain, RAM = short memory, SSD = long memory. This helps you explain problems."
 },
 5: {
  "warmup":"Every IT worker installs software. Clicking 'Next, Next, Next' is fast but dangerous: many installers add extra programs you do not want. Reading each screen takes 30 seconds and can prevent hours of problems.",
  "grammar":{
   "title":"Imperatives + basic modal CAN",
   "rule":"Use the imperative for instructions: 'Click Next.' 'Do not click on strange links.' Use CAN to say what is possible: 'You can download it from the official website.'",
   "table":{
    "head":["Form","Use","Example"],
    "rows":[
     ["Base verb","instruction","Download the file."],
     ["Do + not + verb","negative instruction","Do not use strange sites."],
     ["Can + verb","possibility","You can install it now."],
     ["Can't + verb","impossibility","You can't run it without admin rights."],
    ]
   },
   "examples":[
    {"en":"Click 'Next' to continue.","note":"instruction"},
    {"en":"Don't download cracked software.","note":"negative imperative"},
    {"en":"You can find it in Settings.","note":"possibility with CAN"},
   ]
  },
  "phrases":[
   {"phrase":"Read each screen carefully.","use":"install advice"},
   {"phrase":"Uncheck that option.","use":"remove extra software"},
   {"phrase":"It is free to use.","use":"describe a free program"},
  ],
  "mistakes":[
   {"wrong":"Don't to click that.","right":"Don't click that.","why":"Imperative: no 'to' after 'don't'."},
   {"wrong":"You can to download.","right":"You can download.","why":"CAN + base verb, no 'to'."},
  ],
  "tip":"Always verify the SHA-256 hash of an installer before running it. If you do not know what that means, ask \u2014 it will save you one day."
 },
},
# =========================================================================
"A2": {
 1: {
  "warmup":"In a modern IT team, people play very different roles: developers write code, systems engineers keep servers running, SOC analysts watch for attacks. Each one has a typical day and a typical vocabulary.",
  "grammar":{
   "title":"Present simple vs present continuous",
   "rule":"Present simple = routines, habits, truths (with adverbs like 'usually', 'every day'). Present continuous = what is happening right now (with 'now', 'at the moment', 'look!').",
   "table":{
    "head":["Tense","Form","Signal words"],
    "rows":[
     ["Present simple","I write / She writes","always, usually, every day"],
     ["Present continuous","I am writing / She is writing","now, at the moment, look!"],
    ]
   },
   "examples":[
    {"en":"A developer writes code every day.","note":"routine \u2192 simple"},
    {"en":"The SOC analyst is investigating an alert right now.","note":"now \u2192 continuous"},
    {"en":"I work at a bank, but I am attending a training this week.","note":"mixed"},
   ]
  },
  "phrases":[
   {"phrase":"I am responsible for \u2026","use":"describe duties"},
   {"phrase":"She is in charge of \u2026","use":"responsibility"},
   {"phrase":"I report to \u2026","use":"name your manager"},
   {"phrase":"My team handles \u2026","use":"describe scope"},
  ],
  "mistakes":[
   {"wrong":"I am working every day at the bank.","right":"I work every day at the bank.","why":"'Every day' = habit \u2192 simple."},
   {"wrong":"He write code for mobile.","right":"He writes code for mobile.","why":"He/She/It \u2192 add -s."},
  ],
  "tip":"Verbs like 'know, understand, want, need, believe' are rarely used in continuous. Say 'I know' not 'I am knowing'."
 },
 2: {
  "warmup":"When we describe a career, we move through past events in order: started, worked, moved, changed. The past simple is the natural tense for this. English has many irregular verbs, so memorisation matters.",
  "grammar":{
   "title":"Past simple (regular + irregular) + DID for questions/negatives",
   "rule":"Regular verbs add -ed (work \u2192 worked). Irregular verbs change (go \u2192 went, begin \u2192 began). Negatives and questions use DID + base verb.",
   "table":{
    "head":["Type","Affirmative","Negative","Question"],
    "rows":[
     ["Regular","She worked.","She didn't work.","Did she work?"],
     ["Irregular","He went.","He didn't go.","Did he go?"],
     ["To be","We were there.","We weren't there.","Were we there?"],
    ]
   },
   "examples":[
    {"en":"I started my career in 2019.","note":"regular past: started"},
    {"en":"She moved to a cloud company last year.","note":"regular past + time marker"},
    {"en":"He didn't have AWS experience before 2022.","note":"negative with DID"},
   ]
  },
  "phrases":[
   {"phrase":"I graduated from \u2026","use":"say your university"},
   {"phrase":"I have worked at \u2026 for X years.","use":"ongoing job"},
   {"phrase":"Last year, I \u2026","use":"past achievements"},
   {"phrase":"I changed jobs because \u2026","use":"explain move"},
  ],
  "mistakes":[
   {"wrong":"I didn't went to the meeting.","right":"I didn't go to the meeting.","why":"After DID/DIDN'T, use the base form (go, not went)."},
   {"wrong":"Last year I work in Lima.","right":"Last year I worked in Lima.","why":"'Last year' \u2192 past simple, add -ed."},
  ],
  "tip":"Keep a personal list of irregular verbs you use at work: build/built, break/broke, find/found, lose/lost, run/ran. 20 verbs cover 80% of cases."
 },
 3: {
  "warmup":"We constantly compare tools: Windows vs Linux, Chrome vs Firefox, Python vs Go. Comparatives and superlatives are the grammar of tech opinions. Getting them right makes your argument sound professional.",
  "grammar":{
   "title":"Comparatives and superlatives",
   "rule":"Short adjectives: add -er / -est (fast \u2192 faster \u2192 the fastest). Long adjectives: more / the most (popular \u2192 more popular \u2192 the most popular). Irregular: good/better/best, bad/worse/worst.",
   "table":{
    "head":["Adjective","Comparative","Superlative"],
    "rows":[
     ["fast","faster","the fastest"],
     ["popular","more popular","the most popular"],
     ["good","better","the best"],
     ["bad","worse","the worst"],
     ["flexible","more flexible","the most flexible"],
    ]
   },
   "examples":[
    {"en":"Linux is more flexible than Windows.","note":"long adj + THAN"},
    {"en":"macOS has the best design.","note":"irregular superlative"},
    {"en":"Firefox is safer than Chrome for privacy.","note":"short adj + -er + than"},
   ]
  },
  "phrases":[
   {"phrase":"X is better than Y.","use":"basic comparison"},
   {"phrase":"The main advantage of X is \u2026","use":"highlight pros"},
   {"phrase":"Compared to X, Y is \u2026","use":"introduce comparison"},
   {"phrase":"The most popular \u2026 is X.","use":"superlative claim"},
  ],
  "mistakes":[
   {"wrong":"Linux is more better than Windows.","right":"Linux is better than Windows.","why":"Don't use 'more' with irregular comparatives."},
   {"wrong":"macOS is the most good.","right":"macOS is the best.","why":"Good \u2192 best (irregular)."},
  ],
  "tip":"Support your comparisons with a reason: 'Linux is more flexible because you can customise the kernel.' Comparisons without reasons are weak in professional discussions."
 },
 4: {
  "warmup":"Installing software looks simple, but doing it safely is a small skill. Every week, someone in every company gets malware because they clicked the wrong download link or ignored a permission prompt.",
  "grammar":{
   "title":"Sequence markers + modals of necessity",
   "rule":"Use sequence markers to order steps: first, then, next, after that, finally. Use HAVE TO / NEED TO for necessity, DON'T HAVE TO for no obligation, MUST for strong rules.",
   "table":{
    "head":["Sequence","Modal","Example"],
    "rows":[
     ["First","have to","First, you have to go to the official site."],
     ["Then","need to","Then, you need to verify the hash."],
     ["Next","must","Next, you must accept admin rights."],
     ["Finally","don't have to","Finally, you don't have to restart on Linux."],
    ]
   },
   "examples":[
    {"en":"You have to verify the SHA-256 hash.","note":"necessity"},
    {"en":"You don't have to restart after every install.","note":"no obligation"},
    {"en":"You must never download from pirate sites.","note":"strong prohibition"},
   ]
  },
  "phrases":[
   {"phrase":"First of all, \u2026","use":"start instructions"},
   {"phrase":"Make sure that \u2026","use":"verify a step"},
   {"phrase":"In case of error, \u2026","use":"backup plan"},
   {"phrase":"Before running it, \u2026","use":"preparation"},
  ],
  "mistakes":[
   {"wrong":"You have to not download cracked software.","right":"You must not download cracked software.","why":"Prohibition \u2192 MUST NOT, not 'have to not'."},
   {"wrong":"After that, you downloading.","right":"After that, you download.","why":"After sequence markers, use the base form."},
  ],
  "tip":"Always uncheck 'Install extra toolbars' and 'Make X my default browser'. 9 times out of 10, these are not what you want."
 },
 5: {
  "warmup":"Your browser knows more about you than most of your friends. Every website, every search, every click can be stored. Configuring the browser for privacy is a basic skill for any IT professional.",
  "grammar":{
   "title":"Modal verbs of advice and obligation: SHOULD, OUGHT TO, HAD BETTER",
   "rule":"SHOULD = general advice (mild). OUGHT TO = more formal, same idea. HAD BETTER = strong warning, consequence implied. Negative: shouldn't / had better not.",
   "table":{
    "head":["Modal","Strength","Example"],
    "rows":[
     ["should","advice","You should update weekly."],
     ["ought to","formal advice","You ought to review extensions."],
     ["had better","strong warning","You'd better not ignore that warning."],
     ["must","strong rule","You must not install from unknown sites."],
    ]
   },
   "examples":[
    {"en":"You should use a VPN on public Wi-Fi.","note":"advice"},
    {"en":"You had better clear your cookies before logging in.","note":"strong advice"},
    {"en":"You shouldn't install extensions from email links.","note":"negative advice"},
   ]
  },
  "phrases":[
   {"phrase":"It's a good idea to \u2026","use":"soft advice"},
   {"phrase":"I would recommend \u2026","use":"formal recommendation"},
   {"phrase":"Avoid \u2026","use":"list bad practice"},
   {"phrase":"Stick to \u2026","use":"recommend one option"},
  ],
  "mistakes":[
   {"wrong":"You should to install Firefox.","right":"You should install Firefox.","why":"After modal \u2192 base form, no 'to'."},
   {"wrong":"You had better to update.","right":"You had better update.","why":"HAD BETTER + base verb, no 'to'."},
  ],
  "tip":"Use SHOULD for advice, MUST for rules, HAVE TO for external obligation (policy, law). Choosing the right modal shows professional register."
 },
},
# =========================================================================
"B1": {
 1: {
  "warmup":"The Software Development Lifecycle is the skeleton of every project. Whether you are in a three-week startup sprint or a five-year government procurement, the stages are the same: gather requirements, design, build, test, deploy, maintain.",
  "grammar":{
   "title":"Passive voice (present and past) + present perfect vs past simple",
   "rule":"Passive = object + BE + past participle (+ BY agent). Use the passive when the action matters more than the actor. Use present perfect for experiences or recent events; past simple for finished events at a specific time.",
   "table":{
    "head":["Tense","Active","Passive"],
    "rows":[
     ["Present","Developers write code.","Code is written by developers."],
     ["Past","The team deployed the app.","The app was deployed by the team."],
     ["Pres. perfect","We have replaced waterfall.","Waterfall has been replaced."],
    ]
   },
   "examples":[
    {"en":"Code is deployed to production thousands of times a day at Amazon.","note":"passive, general truth"},
    {"en":"Waterfall has been largely replaced by agile in the last two decades.","note":"present perfect passive"},
   ]
  },
  "phrases":[
   {"phrase":"From my point of view, \u2026","use":"opinion"},
   {"phrase":"In my experience, \u2026","use":"personal evidence"},
   {"phrase":"As far as I know, \u2026","use":"hedge your knowledge"},
   {"phrase":"This approach helps us \u2026","use":"describe benefit"},
  ],
  "mistakes":[
   {"wrong":"Code is deploy many times a day.","right":"Code is deployed many times a day.","why":"Passive needs the past participle: deploy \u2192 deployed."},
   {"wrong":"Since two decades, waterfall has been replaced.","right":"Over the last two decades, waterfall has been replaced.","why":"Use 'over/in the last X years', not 'since X'."},
  ],
  "tip":"When you write a process description, the passive voice is often more professional: 'The requirements are gathered' sounds more neutral than 'The team gathers the requirements'."
 },
 2: {
  "warmup":"Programming languages are like tools in a workshop. A hammer is not better than a screwdriver \u2014 they solve different problems. Choosing the right language depends on the task, the team, and the long-term maintenance.",
  "grammar":{
   "title":"Gerunds vs infinitives + prepositions + gerunds",
   "rule":"After some verbs (enjoy, avoid, recommend) we use the -ing form. After others (want, decide, plan) we use the to-infinitive. After all prepositions (of, for, on, about, by) we always use -ing.",
   "table":{
    "head":["Pattern","Example","Verbs / prepositions"],
    "rows":[
     ["verb + -ing","I enjoy coding.","enjoy, avoid, recommend, suggest, mind"],
     ["verb + to + infinitive","I decided to learn Rust.","want, decide, plan, hope, need"],
     ["preposition + -ing","Rust is famous for being safe.","of, for, on, about, by, without"],
    ]
   },
   "examples":[
    {"en":"Python is popular for being readable.","note":"preposition + -ing"},
    {"en":"Google decided to create Go to solve backend problems.","note":"verb + to + infinitive"},
    {"en":"I recommend learning Python first.","note":"verb + -ing"},
   ]
  },
  "phrases":[
   {"phrase":"The main advantage of \u2026 is \u2026","use":"highlight a pro"},
   {"phrase":"The downside is \u2026","use":"acknowledge a con"},
   {"phrase":"It is especially suitable for \u2026","use":"recommend a use case"},
   {"phrase":"Unlike X, Y \u2026","use":"contrast"},
  ],
  "mistakes":[
   {"wrong":"I recommend to learn Python.","right":"I recommend learning Python.","why":"RECOMMEND + -ing, not + to-infinitive."},
   {"wrong":"Rust is famous for be safe.","right":"Rust is famous for being safe.","why":"After a preposition \u2192 -ing, not the base form."},
  ],
  "tip":"Keep a personal 'pattern notebook': each time you meet 'X + preposition + Y', write it down. Patterns are memorised faster than rules."
 },
 3: {
  "warmup":"A database is not just storage; it is a promise. The bank promises that transactions are consistent. The social network promises that your post will appear. The right database for the right promise is half of a good system.",
  "grammar":{
   "title":"Defining relative clauses: THAT / WHICH / WHO",
   "rule":"Defining clauses give essential information. Use WHO for people, WHICH for things (formal), THAT for either (informal). No commas. If the relative pronoun is the object, you can drop it.",
   "table":{
    "head":["Pronoun","Refers to","Example"],
    "rows":[
     ["who","people","The engineer who wrote this code is Maria."],
     ["which","things (formal)","The database which we use is PostgreSQL."],
     ["that","both (informal)","The queries that she writes are efficient."],
     ["\u2014 (omitted)","object","The database (that) we chose is NoSQL."],
    ]
   },
   "examples":[
    {"en":"NoSQL is an umbrella term that contains several models.","note":"defining clause about 'term'"},
    {"en":"Companies which handle millions of users often need NoSQL.","note":"defining clause about 'companies'"},
   ]
  },
  "phrases":[
   {"phrase":"This is the case for \u2026","use":"typical example"},
   {"phrase":"The root cause is \u2026","use":"explain origin"},
   {"phrase":"In practice, \u2026","use":"real-world note"},
   {"phrase":"From a security point of view, \u2026","use":"security framing"},
  ],
  "mistakes":[
   {"wrong":"MongoDB is a database what stores JSON.","right":"MongoDB is a database that stores JSON.","why":"'What' is not a relative pronoun for things."},
   {"wrong":"The engineer, who wrote this code, is Maria.","right":"The engineer who wrote this code is Maria.","why":"Defining clause \u2192 no commas."},
  ],
  "tip":"If you can remove the relative clause without losing the meaning, it is non-defining and needs commas. If not, it is defining and does not."
 },
 4: {
  "warmup":"Cloud is a rental business. You rent servers, storage and entire applications. The big question is: who is responsible when something breaks? The shared responsibility model answers that question.",
  "grammar":{
   "title":"Modals of deduction (present) + conditionals (type 1)",
   "rule":"MUST = almost certain, CAN'T = almost impossible, MIGHT / MAY = possible, COULD = possible. For real future plans use the first conditional: If + present simple, will + base form.",
   "table":{
    "head":["Modal","Probability","Example"],
    "rows":[
     ["must","very likely","It must be a misconfiguration."],
     ["might / may","possible","It might be a quota issue."],
     ["could","possible","It could also be a billing problem."],
     ["can't","impossible","It can't be the provider's fault; SLA is intact."],
    ]
   },
   "examples":[
    {"en":"If your data changes often, NoSQL is usually better.","note":"real conditional"},
    {"en":"It must be a customer misconfiguration, not an AWS problem.","note":"deduction"},
   ]
  },
  "phrases":[
   {"phrase":"The customer is responsible for \u2026","use":"ownership"},
   {"phrase":"The provider handles \u2026","use":"other side"},
   {"phrase":"This falls under \u2026","use":"categorise"},
   {"phrase":"It is up to us to \u2026","use":"responsibility claim"},
  ],
  "mistakes":[
   {"wrong":"If you will use NoSQL, your data can scale.","right":"If you use NoSQL, your data can scale.","why":"In first conditional IF clause \u2192 present simple, not 'will'."},
   {"wrong":"It must to be a misconfiguration.","right":"It must be a misconfiguration.","why":"After modal \u2192 bare infinitive."},
  ],
  "tip":"When a system fails, start with the most likely cause: misconfiguration. 'Blame the cloud' is almost always wrong."
 },
 5: {
  "warmup":"TCP/IP is the invisible layer that makes the internet possible. Every time you open a webpage, dozens of small things happen in less than a second. Understanding the stack even at a high level helps you debug faster.",
  "grammar":{
   "title":"Time clauses (before, after, while, as soon as) + sequence of tenses",
   "rule":"In time clauses about the future, use the present simple (never 'will'). Use 'before / after + -ing' for simpler sentences.",
   "table":{
    "head":["Connector","Use","Example"],
    "rows":[
     ["before","earlier event","Before data flows, TCP performs a handshake."],
     ["after","later event","After the handshake, data is transferred."],
     ["while","simultaneous","While the connection is open, the state machine keeps track."],
     ["as soon as","immediate","As soon as the SYN arrives, the server responds."],
    ]
   },
   "examples":[
    {"en":"TCP performs a handshake before any data is sent.","note":"time clause"},
    {"en":"UDP just sends the packet without waiting for a reply.","note":"preposition + -ing"},
   ]
  },
  "phrases":[
   {"phrase":"At the \u2026 layer, \u2026","use":"locate a protocol"},
   {"phrase":"This sits on top of \u2026","use":"describe a stack"},
   {"phrase":"The trade-off is \u2026","use":"describe pros/cons"},
   {"phrase":"In practice, \u2026","use":"real-world clarification"},
  ],
  "mistakes":[
   {"wrong":"As soon as the SYN will arrive, the server responds.","right":"As soon as the SYN arrives, the server responds.","why":"Time clause about the future \u2192 present simple."},
   {"wrong":"Before to send data, TCP does a handshake.","right":"Before sending data, TCP does a handshake.","why":"Preposition BEFORE + -ing."},
  ],
  "tip":"When you debug, trace the packet by layer: link \u2192 internet \u2192 transport \u2192 application. Most problems live at one specific layer."
 },
},
# =========================================================================
"B2": {
 1: {
  "warmup":"The difference between a minor incident and a catastrophic breach is almost never the technology. It is the preparation. A team that has rehearsed its playbooks and knows its escalation paths responds in minutes, not hours.",
  "grammar":{
   "title":"Mixed conditionals + third conditional",
   "rule":"Third conditional: If + past perfect, would have + past participle. Describes imaginary past situations. Mixed conditional combines past condition with present result.",
   "table":{
    "head":["Type","Structure","Use"],
    "rows":[
     ["Third","If + past perfect, would have + p.p.","If we had segmented the network, the breach wouldn't have spread."],
     ["Mixed (past \u2192 now)","If + past perfect, would + base","If we had hired a CISO earlier, we wouldn't be in this situation."],
     ["Mixed (now \u2192 past)","If + past simple, would have + p.p.","If the team were better trained, they would have contained it quickly."],
    ]
   },
   "examples":[
    {"en":"If SolarWinds had applied stronger SDLC controls, the compromise would have been harder.","note":"3rd conditional"},
    {"en":"If we weren't so dependent on a single vendor, we wouldn't have been paralysed.","note":"mixed"},
   ]
  },
  "phrases":[
   {"phrase":"In retrospect, \u2026","use":"post-incident reflection"},
   {"phrase":"Lessons learned include \u2026","use":"formal recap"},
   {"phrase":"A root cause analysis revealed \u2026","use":"formal investigation result"},
   {"phrase":"This could have been avoided by \u2026","use":"preventable suggestion"},
  ],
  "mistakes":[
   {"wrong":"If we would have segmented, the breach wouldn't happen.","right":"If we had segmented, the breach wouldn't have spread.","why":"In the IF clause of 3rd conditional \u2192 past perfect, not 'would have'."},
   {"wrong":"If the team trained, they had contained it.","right":"If the team had been trained, they would have contained it.","why":"3rd conditional needs past perfect + would have."},
  ],
  "tip":"In post-incident reports, use conditionals with care. They imply blame. A neutral phrase like 'A stronger control would have prevented this' is safer than 'If you had configured X correctly'."
 },
 2: {
  "warmup":"Modern enterprise networks are not flat. Segmentation, identity, continuous verification \u2014 these are baseline. Calling your network 'Zero Trust' does not make it so; building it that way takes three to five years of disciplined work.",
  "grammar":{
   "title":"Cleft sentences (It is \u2026 that / What \u2026 is)",
   "rule":"Cleft sentences emphasise a specific element. 'It is X that \u2026' emphasises X. 'What \u2026 is X' gives end-focus and sounds more reflective.",
   "table":{
    "head":["Pattern","Example"],
    "rows":[
     ["It is X that \u2026","It is the identity layer that makes Zero Trust real."],
     ["What \u2026 is X","What really matters is continuous verification."],
     ["All \u2026 is X","All we need is better telemetry."],
     ["The reason why \u2026 is that \u2026","The reason why flat networks fail is that trust is static."],
    ]
   },
   "examples":[
    {"en":"It is continuous verification, not strong authentication alone, that defines Zero Trust.","note":"emphasis on the subject"},
    {"en":"What most teams underestimate is the cost of migration.","note":"end-focus"},
   ]
  },
  "phrases":[
   {"phrase":"Contrary to popular belief, \u2026","use":"refute a myth"},
   {"phrase":"The crux of the matter is \u2026","use":"core point"},
   {"phrase":"At its heart, \u2026","use":"essential idea"},
   {"phrase":"The real question is \u2026","use":"reframe"},
  ],
  "mistakes":[
   {"wrong":"What matters is that continuous verification.","right":"What matters is continuous verification.","why":"No 'that' after the clefted element."},
   {"wrong":"It's the identity layer which makes Zero Trust.","right":"It's the identity layer that makes Zero Trust.","why":"In cleft sentences, use 'that', not 'which'."},
  ],
  "tip":"Use cleft sentences sparingly. Overusing them makes writing sound theatrical. Save them for the one or two points you really want to highlight."
 },
 3: {
  "warmup":"Ransomware used to be a technical problem. Now it is a business problem, a legal problem and a public-relations problem all at once. The CISO who only knows cryptography cannot protect the organisation anymore.",
  "grammar":{
   "title":"Concessive clauses (although, though, even though, despite, in spite of)",
   "rule":"Use 'although / even though' + clause (S + V). Use 'despite / in spite of' + noun or -ing. These express contrast or concession.",
   "table":{
    "head":["Connector","+ ?","Example"],
    "rows":[
     ["although","clause","Although insurers were generous, premiums are now higher."],
     ["even though","clause","Even though we paid, the data was still leaked."],
     ["despite","noun / -ing","Despite paying the ransom, we lost the data."],
     ["in spite of","noun / -ing","In spite of the risk, many victims still pay."],
    ]
   },
   "examples":[
    {"en":"Despite having tested backups, the company paid the ransom.","note":"despite + -ing"},
    {"en":"Although the FBI later recovered most of the money, the reputational damage was permanent.","note":"although + clause"},
   ]
  },
  "phrases":[
   {"phrase":"Pay or not pay \u2014 that is the question.","use":"dilemma framing"},
   {"phrase":"There is no one-size-fits-all answer.","use":"complexity"},
   {"phrase":"This is a business decision, not a technical one.","use":"reframe"},
   {"phrase":"Legal exposure includes \u2026","use":"listing risks"},
  ],
  "mistakes":[
   {"wrong":"Despite we paid, we lost the data.","right":"Despite paying, we lost the data.","why":"DESPITE + -ing or noun, not a clause."},
   {"wrong":"Although of the risk, they paid.","right":"Despite the risk, they paid.","why":"'Although' + clause; 'despite' + noun."},
  ],
  "tip":"When executives ask 'should we pay?', your answer must cover three dimensions: operational (can we recover?), legal (is it permitted?), ethical (does it fund future attacks?)."
 },
 4: {
  "warmup":"The day a zero-day breaks the news is not the day to start asking questions. Mature organisations know their inventory, their exposure and their patch windows before the news breaks. The rest scramble.",
  "grammar":{
   "title":"Inversion after negative / restrictive adverbs",
   "rule":"After adverbs like 'never, rarely, not only, hardly, no sooner, under no circumstances', the subject and auxiliary are inverted for emphasis.",
   "table":{
    "head":["Adverb","Normal","Inverted"],
    "rows":[
     ["Not only","Not only do we patch, (but) we also segment.","Not only + do + S + V"],
     ["Under no circumstances","Under no circumstances will we delay.","+ modal + S + V"],
     ["No sooner","No sooner had we patched than a new CVE appeared.","+ had + S + p.p."],
     ["Rarely","Rarely have we seen such a chain.","+ aux + S + V"],
    ]
   },
   "examples":[
    {"en":"Not only do zero-days affect unpatched systems, they also stress incident response.","note":"inversion after 'not only'"},
    {"en":"Under no circumstances should public-facing systems run without an EDR.","note":"formal policy register"},
   ]
  },
  "phrases":[
   {"phrase":"Given the severity, \u2026","use":"justify action"},
   {"phrase":"At the time of writing, \u2026","use":"hedge currency"},
   {"phrase":"It is worth noting that \u2026","use":"raise a point"},
   {"phrase":"This raises a broader question: \u2026","use":"escalate"},
  ],
  "mistakes":[
   {"wrong":"Not only we patch but also segment.","right":"Not only do we patch, we also segment.","why":"Inversion needed after 'not only'."},
   {"wrong":"No sooner we patched than \u2026","right":"No sooner had we patched than \u2026","why":"Inversion + past perfect after 'no sooner'."},
  ],
  "tip":"Inversion raises the register. Use it sparingly in reports and in executive briefings. Overusing it sounds pompous."
 },
 5: {
  "warmup":"The OWASP Top 10 is not a standard; it is a mirror. It shows us which mistakes keep happening, year after year, across thousands of real incidents. Reading it every release is professional hygiene.",
  "grammar":{
   "title":"Participle clauses (reduced relative clauses)",
   "rule":"Replace 'which is / who are' + V-ing with the -ing form. Replace 'which is + past participle' with just the past participle. This makes writing more concise.",
   "table":{
    "head":["Full","Reduced"],
    "rows":[
     ["Applications which use parameterised APIs are safer.","Applications using parameterised APIs are safer."],
     ["Categories which are new in 2021 include Insecure Design.","Categories new in 2021 include Insecure Design."],
     ["Secrets which are committed to Git are a common failure.","Secrets committed to Git are a common failure."],
    ]
   },
   "examples":[
    {"en":"Categories introduced in 2021 reflect modern threat models.","note":"past participle as adjective"},
    {"en":"Applications concatenating untrusted input are vulnerable to injection.","note":"present participle"},
   ]
  },
  "phrases":[
   {"phrase":"A common root cause is \u2026","use":"recurrent issue"},
   {"phrase":"This is preventable by \u2026","use":"suggest fix"},
   {"phrase":"The attack surface includes \u2026","use":"scope definition"},
   {"phrase":"This aligns with \u2026","use":"relate to standards"},
  ],
  "mistakes":[
   {"wrong":"Categories introducing in 2021 are \u2026","right":"Categories introduced in 2021 are \u2026","why":"Passive meaning \u2192 past participle."},
   {"wrong":"Applications using of parameterised APIs \u2026","right":"Applications using parameterised APIs \u2026","why":"No 'of' after -ing form in this pattern."},
  ],
  "tip":"Each year, compare the OWASP Top 10 to your own findings. If a category rises in OWASP but not in you, either your coverage is better \u2014 or your detection is missing it."
 },
},
# =========================================================================
"C1": {
 1: {
  "warmup":"Cyber Threat Intelligence is a discipline that collapses on contact with vague demands. Executives who ask for 'intel' without specifying the question usually get feeds. Teams that ask the right questions get answers.",
  "grammar":{
   "title":"Cleft + pseudo-cleft + fronting for emphasis",
   "rule":"Pseudo-cleft structures with 'What \u2026 is' and 'The reason why \u2026 is' allow elegant emphasis. Fronting places a non-subject element at the start for focus.",
   "table":{
    "head":["Structure","Example"],
    "rows":[
     ["What + clause + is \u2026","What distinguishes strategic CTI is its time horizon."],
     ["The thing \u2026 is \u2026","The thing board members want is implications."],
     ["Fronting","Atomic indicators we have in abundance; analytical tradecraft, not so much."],
    ]
   },
   "examples":[
    {"en":"What most young programmes conflate is the four layers of intelligence.","note":"pseudo-cleft"},
    {"en":"The real bottleneck is rarely tooling; it is analytical tradecraft.","note":"cleft"},
   ]
  },
  "phrases":[
   {"phrase":"In essence, \u2026","use":"core summary"},
   {"phrase":"To put it differently, \u2026","use":"reformulate"},
   {"phrase":"The underlying assumption is \u2026","use":"expose premise"},
   {"phrase":"This is where \u2026 becomes relevant.","use":"connect to topic"},
  ],
  "mistakes":[
   {"wrong":"What distinguish strategic CTI is \u2026","right":"What distinguishes strategic CTI is \u2026","why":"The clause functions as singular \u2192 '-s'."},
   {"wrong":"What most teams conflate is are the layers.","right":"What most teams conflate are the layers.","why":"Plural complement \u2192 'are'."},
  ],
  "tip":"Before you write an intel product, identify the consumer. Board, engineer, analyst: different consumers need different products. A report that tries to serve everyone serves no one."
 },
 2: {
  "warmup":"APTs used to mean state intelligence services. Today, contractors, mercenary spyware vendors and well-funded criminals operate at the same level of tradecraft. The old taxonomy no longer reflects the landscape.",
  "grammar":{
   "title":"Nominalisation + participle clauses (advanced)",
   "rule":"Academic and professional register converts verbs into nouns: 'attribute \u2192 attribution', 'fail \u2192 failure'. Participle clauses compress dense information: 'Operators who live off the land \u2192 Operators living off the land'.",
   "table":{
    "head":["Verb","Noun","Example"],
    "rows":[
     ["attribute","attribution","Attribution is treated with confidence levels."],
     ["evade","evasion","Signature-based tools enable evasion."],
     ["persist","persistence","Kernel rootkits are a classic persistence mechanism."],
     ["exfiltrate","exfiltration","Data exfiltration often precedes encryption."],
    ]
   },
   "examples":[
    {"en":"The blurring between espionage and destructive preparation is one of the defining trends.","note":"nominalisation + participle"},
    {"en":"Operators bringing their own vulnerable drivers bypass endpoint protection.","note":"participle clause"},
   ]
  },
  "phrases":[
   {"phrase":"By extension, \u2026","use":"derived point"},
   {"phrase":"This is compounded by \u2026","use":"additional problem"},
   {"phrase":"A quietly defining trend is \u2026","use":"understated emphasis"},
   {"phrase":"We should be wary of \u2026","use":"cautious advice"},
  ],
  "mistakes":[
   {"wrong":"Operators which bring their own vulnerable drivers \u2026","right":"Operators bringing their own vulnerable drivers \u2026","why":"Reduce the relative clause for conciseness."},
   {"wrong":"Attribution is treat with confidence levels.","right":"Attribution is treated with confidence levels.","why":"Passive \u2192 past participle."},
  ],
  "tip":"Use confidence levels (ICD 203: low / moderate / high) when you attribute. 'Likely' does not mean 'certain'. Clarity about uncertainty is itself a professional signal."
 },
 3: {
  "warmup":"Zero Trust is frequently misunderstood as a product. It is not. It is a principle applied through three pillars: identity, endpoint trust, and continuous verification. Implementing any of them without the others is theatre.",
  "grammar":{
   "title":"Subjunctive for recommendations + formal inversion",
   "rule":"After verbs of recommendation (recommend, suggest, demand, require, advise, propose) the base form is used: 'We recommend that the policy be updated.' In formal writing, inversion after restrictive adverbs raises register.",
   "table":{
    "head":["Verb","Subjunctive","Example"],
    "rows":[
     ["recommend","that + S + base","We recommend that access be revoked."],
     ["suggest","that + S + base","The report suggests that the root be offline."],
     ["demand","that + S + base","Regulators demand that MFA be enforced."],
     ["require","that + S + base","The standard requires that logs be retained."],
    ]
   },
   "examples":[
    {"en":"We recommend that every service account be rotated quarterly.","note":"subjunctive"},
    {"en":"Not only is Zero Trust a three-year journey, it is also a cultural shift.","note":"inversion"},
   ]
  },
  "phrases":[
   {"phrase":"A realistic roadmap spans \u2026","use":"timeframe"},
   {"phrase":"The central tension is \u2026","use":"expose dilemma"},
   {"phrase":"This has non-trivial implications for \u2026","use":"formal caution"},
   {"phrase":"Legacy systems complicate \u2026","use":"real-world limit"},
  ],
  "mistakes":[
   {"wrong":"We recommend that the policy is updated.","right":"We recommend that the policy be updated.","why":"Subjunctive uses the base form."},
   {"wrong":"Not only Zero Trust is a journey, it is a cultural shift.","right":"Not only is Zero Trust a journey, it is also a cultural shift.","why":"Inversion required after 'not only'."},
  ],
  "tip":"In policy documents, prefer the subjunctive: it is formal, precise and \u2014 crucially \u2014 unambiguous. 'Is' can be descriptive; 'be' is prescriptive."
 },
 4: {
  "warmup":"A modern SOC is, at its best, a detection-engineering lab that happens to also triage alerts. The bottleneck is rarely tooling. It is analyst cognitive load, quality of detections and integration with response.",
  "grammar":{
   "title":"Advanced passive forms + complex subordination",
   "rule":"Register moves higher through passive reporting verbs ('It is said that \u2026', 'X has been argued to \u2026') and through longer, well-balanced subordinate structures.",
   "table":{
    "head":["Form","Example"],
    "rows":[
     ["It is argued that \u2026","It is argued that signature-based approaches alone are inadequate."],
     ["X is said to \u2026","Leading teams are said to supplement MTTR with coverage metrics."],
     ["X is widely regarded as \u2026","FIRST is widely regarded as the canonical CSIRT body."],
     ["It should be noted that \u2026","It should be noted that burnout is endemic."],
    ]
   },
   "examples":[
    {"en":"It has been observed that SOCs gaming metrics accumulate invisible breaches.","note":"passive reporting"},
    {"en":"Leading teams are known to supplement MTTR with coverage mapped to ATT&CK.","note":"formal hedge"},
   ]
  },
  "phrases":[
   {"phrase":"Against this backdrop, \u2026","use":"contextual pivot"},
   {"phrase":"Given these constraints, \u2026","use":"formal consequence"},
   {"phrase":"This is borne out by \u2026","use":"evidence"},
   {"phrase":"Crucially, \u2026","use":"emphasise"},
  ],
  "mistakes":[
   {"wrong":"It is said that SOCs gaming metrics leads to breaches.","right":"It is said that SOCs that game metrics accumulate breaches.","why":"Agreement: 'SOCs' is plural."},
   {"wrong":"It has been observe that \u2026","right":"It has been observed that \u2026","why":"Present perfect passive \u2192 past participle."},
  ],
  "tip":"In board-level reports, replace 'we think' with 'it is argued that', replace 'we see' with 'evidence suggests'. Same content, much higher register."
 },
 5: {
  "warmup":"Threat hunting is not detection. Detection fires when something known happens. Hunting searches for what no detection has caught. A mature programme accepts that a hunt can find nothing and still be valuable.",
  "grammar":{
   "title":"Hedging language + cause-effect connectors",
   "rule":"In professional reports, claims are hedged to signal uncertainty: 'appears to', 'is consistent with', 'likely / probably'. Cause-effect connectors build arguments: 'consequently, hence, as a result, thereby'.",
   "table":{
    "head":["Function","Phrase","Example"],
    "rows":[
     ["hedge","appears to","The traffic appears to match a C2 beacon pattern."],
     ["hedge","is consistent with","The activity is consistent with ransomware staging."],
     ["cause","as a result","The logs were rotated too fast; as a result, the evidence is lost."],
     ["result","thereby","The hunt revealed a gap, thereby informing detection engineering."],
    ]
   },
   "examples":[
    {"en":"The behaviour is consistent with early-stage reconnaissance.","note":"hedged claim"},
    {"en":"The programme treats null hunts as information, thereby avoiding theatre.","note":"result connector"},
   ]
  },
  "phrases":[
   {"phrase":"With moderate confidence, \u2026","use":"ICD 203 hedge"},
   {"phrase":"Absent further data, \u2026","use":"formal caveat"},
   {"phrase":"On the balance of evidence, \u2026","use":"weigh evidence"},
   {"phrase":"It is worth flagging that \u2026","use":"raise concern"},
  ],
  "mistakes":[
   {"wrong":"The hunt was fail because it found nothing.","right":"The hunt did not fail because it found nothing.","why":"Use the correct verb phrase: 'did not fail' and the full pattern."},
   {"wrong":"The behaviour is consistent to reconnaissance.","right":"The behaviour is consistent with reconnaissance.","why":"Collocation: consistent WITH."},
  ],
  "tip":"A hunt report without a confidence level is incomplete. Even 'with low confidence' is more useful than silence. It tells the reader how much to rely on your claim."
 },
},
# =========================================================================
"C2": {
 1: {
  "warmup":"The grey zone sits between peace and war, between espionage and attack, between ambiguity and escalation. Mapping existing international law onto it is a task that has occupied the world's best lawyers for twenty years \u2014 and remains incomplete.",
  "grammar":{
   "title":"Academic register: nominalisation + hedging + complex coordination",
   "rule":"Academic writing in IR and legal studies prefers dense noun phrases and careful hedging. Cause-effect is signalled through connectors, not through simple sentences.",
   "table":{
    "head":["Move","Phrase","Function"],
    "rows":[
     ["Formal hedge","arguably / putatively / ostensibly","distance from claim"],
     ["Nominalise","the blurring of X and Y","compress information"],
     ["Formal contrast","by contrast / conversely","balance argument"],
     ["Escalate claim","what is more / indeed","extend point"],
    ]
   },
   "examples":[
    {"en":"States, for entirely rational strategic reasons, prefer ambiguity.","note":"embedded clause"},
    {"en":"What is more, the collapse of the observation/attack distinction complicates deterrence.","note":"escalation"},
   ]
  },
  "phrases":[
   {"phrase":"A further layer of complexity arises from \u2026","use":"add dimension"},
   {"phrase":"This diffusion of authority raises \u2026","use":"flag issue"},
   {"phrase":"The cumulative effect is \u2026","use":"sum up"},
   {"phrase":"An underappreciated dynamic is \u2026","use":"highlight overlooked point"},
  ],
  "mistakes":[
   {"wrong":"The Tallinn Manual solved the thresholds.","right":"The Tallinn Manual has not settled the thresholds.","why":"C2 demands precise hedging; 'solved' is too strong."},
   {"wrong":"By contrast of traditional doctrine, \u2026","right":"By contrast with traditional doctrine, \u2026","why":"Preposition: 'by contrast WITH', not 'of'."},
  ],
  "tip":"In C2 writing, absolute claims are rare and suspicious. Readers look for the hedge. Absence of hedging is itself a signal that the writer has not thought carefully."
 },
 2: {
  "warmup":"The old mental model of 'one state, one group, one campaign' has been superseded by something messier: contractors who move between employers, infrastructure shared across principals, and commercial vendors who sell to both sides.",
  "grammar":{
   "title":"Formal subordination + inversion in academic prose",
   "rule":"Long sentences in formal writing rely on relative clauses, adverbial clauses and balanced coordination. Inversion after 'only if / seldom / nowhere' maintains register.",
   "table":{
    "head":["Pattern","Example"],
    "rows":[
     ["Only by \u2026 can \u2026","Only by accepting this commercialisation can attribution remain credible."],
     ["Seldom \u2026","Seldom has the analytic community faced such a shift."],
     ["Nowhere is \u2026","Nowhere is this more visible than in the i-Soon disclosures."],
    ]
   },
   "examples":[
    {"en":"Seldom has the attribution community had to incorporate commercial supply-chain analysis to the extent now required.","note":"inversion"},
    {"en":"Only by treating the ecosystem as a labour market can policy responses be designed appropriately.","note":"inversion + passive"},
   ]
  },
  "phrases":[
   {"phrase":"The analytical consequence is \u2026","use":"reasoned implication"},
   {"phrase":"This complicates, without invalidating, \u2026","use":"qualified claim"},
   {"phrase":"One reading is \u2026; another is \u2026","use":"present alternatives"},
   {"phrase":"Normatively, \u2026","use":"shift to policy"},
  ],
  "mistakes":[
   {"wrong":"Only by accepting this, attribution can remain credible.","right":"Only by accepting this can attribution remain credible.","why":"Inversion is required after 'only by \u2026'."},
   {"wrong":"Seldom the community has faced \u2026","right":"Seldom has the community faced \u2026","why":"Inversion after 'seldom'."},
  ],
  "tip":"In policy writing, acknowledge competing readings before giving your own. A paragraph that presents only one view signals bias even when the analysis is sound."
 },
 3: {
  "warmup":"International data transfers live in the space between judgments. Schrems II invalidated a framework, the replacement Data Privacy Framework arrived, and Schrems III is already before the courts. Compliance is a moving target.",
  "grammar":{
   "title":"Legal-English modals + conditional perfects",
   "rule":"Legal texts use precise modals: SHALL = obligation, MAY = permission, MUST NOT = prohibition. Conditional perfects express counterfactual legal reasoning.",
   "table":{
    "head":["Modal","Legal meaning","Example"],
    "rows":[
     ["shall","obligation","The controller shall notify within 72 hours."],
     ["may","permission","Processors may sub-contract subject to written consent."],
     ["must not","prohibition","Personal data must not leave the EEA without adequacy."],
     ["is entitled to","right","Data subjects are entitled to erasure."],
    ]
   },
   "examples":[
    {"en":"Had Schrems II left SCCs untouched, half a decade of turbulence would have been avoided.","note":"conditional perfect"},
    {"en":"The controller shall conduct a transfer impact assessment.","note":"legal obligation"},
   ]
  },
  "phrases":[
   {"phrase":"Without prejudice to \u2026","use":"legal caveat"},
   {"phrase":"Subject to \u2026","use":"condition"},
   {"phrase":"For the purposes of \u2026","use":"scope definition"},
   {"phrase":"Notwithstanding \u2026","use":"override clause"},
  ],
  "mistakes":[
   {"wrong":"The controller should notify within 72 hours.","right":"The controller shall notify within 72 hours.","why":"Legal obligation \u2192 SHALL, not SHOULD."},
   {"wrong":"If Schrems II would have left SCCs, \u2026","right":"Had Schrems II left SCCs untouched, \u2026","why":"Inversion in 3rd conditional instead of 'if \u2026 would have'."},
  ],
  "tip":"When drafting anything legal-adjacent, know which verbs translate to which modal. 'Will' is often ambiguous; 'shall' is unambiguous in legal English."
 },
 4: {
  "warmup":"The ethics of offensive security are not a secondary concern. They shape the entire research ecosystem: what is published, what is embargoed, who can be prosecuted, who is protected. No serious researcher can ignore them.",
  "grammar":{
   "title":"Subjunctive in formal prose + balanced concession",
   "rule":"The formal register uses the subjunctive in recommendations and in hypotheticals ('were it the case that \u2026'). Concession is often structured with 'while / whilst + clause, clause' for balance.",
   "table":{
    "head":["Structure","Example"],
    "rows":[
     ["Were it the case that \u2026","Were it the case that statutes were uniform, the regime would be simpler."],
     ["Whilst X, Y","Whilst the US has narrowed CFAA prosecution, the UK CMA remains a chilling instrument."],
     ["Be that as it may, \u2026","Be that as it may, the market adapts faster than regulation."],
     ["Lest \u2026","Lest the point be missed: restraint is part of tradecraft."],
    ]
   },
   "examples":[
    {"en":"Whilst the DoJ policy change is welcome, its impact depends on prosecutorial discretion.","note":"formal concession"},
    {"en":"Lest disclosure become weaponised, researchers must calibrate their claims.","note":"lest + subjunctive"},
   ]
  },
  "phrases":[
   {"phrase":"This tension is not readily resolved.","use":"acknowledge difficulty"},
   {"phrase":"On a charitable reading, \u2026","use":"fair interpretation"},
   {"phrase":"There is an empirical case that \u2026","use":"evidence-based claim"},
   {"phrase":"Whether X is politically feasible remains \u2026","use":"policy hedge"},
  ],
  "mistakes":[
   {"wrong":"Lest disclosure becomes weaponised, \u2026","right":"Lest disclosure become weaponised, \u2026","why":"LEST + subjunctive base form."},
   {"wrong":"Whilst the DoJ has narrow CFAA, \u2026","right":"Whilst the DoJ has narrowed CFAA, \u2026","why":"Past participle after 'has'."},
  ],
  "tip":"In ethics writing, avoid binary framing. 'Publish or not' is a false binary. 'Publish with what level of detail, to what audience, after what coordination' is the real question."
 },
 5: {
  "warmup":"Post-quantum cryptography is the first large-scale migration the internet has faced in a generation. It is also the first where the timeline is set not by user preference but by adversary capability. Planning accordingly is not optional.",
  "grammar":{
   "title":"Academic hedging + inversion + formal conditionals",
   "rule":"At C2, hedging becomes an entire system: probabilistic modals, confidence markers, and calibrated claims. Conditional perfects express likely but non-certain consequences.",
   "table":{
    "head":["Marker","Function","Example"],
    "rows":[
     ["is dismissible","dismiss a claim","The risk is not dismissible."],
     ["appropriate analytical humility","hedge","Estimates should be treated with appropriate analytical humility."],
     ["is at least a credible possibility","measured","A CRQC is at least a credible long-term possibility."],
     ["the relevant deadline is not \u2026 but \u2026","reframe","The relevant deadline is not the quantum computer but today's traffic."],
    ]
   },
   "examples":[
    {"en":"The probability is not dismissible, though it should be treated with appropriate analytical humility.","note":"layered hedging"},
    {"en":"Were ML-KEM to suffer an unexpected cryptanalytic break, hybrid deployments would preserve classical protection.","note":"formal conditional"},
   ]
  },
  "phrases":[
   {"phrase":"For a system with a meaningful design lifespan, \u2026","use":"qualify scope"},
   {"phrase":"The practical message is unusually simple: \u2026","use":"lead into thesis"},
   {"phrase":"This is prudent rather than paranoid.","use":"reject accusation"},
   {"phrase":"The central consequence for practitioners is \u2026","use":"translate to action"},
  ],
  "mistakes":[
   {"wrong":"Were ML-KEM to break, hybrid deployments preserved classical protection.","right":"Were ML-KEM to break, hybrid deployments would preserve classical protection.","why":"Conditional: WOULD + base form in result."},
   {"wrong":"The risk is not dismiss.","right":"The risk is not dismissible.","why":"-ible suffix for adjective."},
  ],
  "tip":"In research-grade writing, calibrate every quantitative claim. 'Aggressive by any realistic measure' is more credible than '10 years' because it signals the writer knows the uncertainty."
 },
},
}

# ---- merge into course_data.json ----
path = Path(r"E:\CLAUDE\PAOLO BACA MANRIQUE\course-app\course_data.json")
course = json.loads(path.read_text(encoding="utf-8"))

merged = 0
for level in course["levels"]:
    code = level["code"]
    for lesson in level["lessons"]:
        notes = NOTES.get(code, {}).get(lesson["n"])
        if notes:
            lesson["lesson_notes"] = notes
            merged += 1
        else:
            lesson.setdefault("lesson_notes", None)

path.write_text(json.dumps(course, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"OK: Merged lesson notes into {merged} pilot lessons")
for code in ["A1","A2","B1","B2","C1","C2"]:
    lv = next(l for l in course["levels"] if l["code"]==code)
    n = sum(1 for le in lv["lessons"] if le.get("lesson_notes"))
    print(f"  {code}: {n}/20 lessons with teaching notes")
