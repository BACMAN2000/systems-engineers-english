// ============================================================
// COHASSET BUSINESS ENGLISH - CURRICULUM EXTENSION (Units 16-20)
// Adds 30 new units (5 per level) to bring total to 120 units
// matching General English / Systems Engineers depth
// ============================================================

window.BE_CURRICULUM_EXTENSION = {

// ========== A1 EXTENSION ==========
a1: [
    // ---------- A1-16 ----------
    {id:"be-a1-16",title:"Unit 16: Office Hours & Daily Schedules",subtitle:"Tell the time and talk about your work schedule",exercises:[
        {type:"vc",tl:"Vocabulary",cb:"BEC Preliminary",title:"Time & Schedule Words",ins:"Learn these words for talking about time at work.",content:{words:[
            {w:"o'clock",ipa:"/əˈklɑk/",d:"Used for exact hours, e.g. nine o'clock"},
            {w:"half past",ipa:"/hæf pæst/",d:"30 minutes after the hour"},
            {w:"quarter to / quarter past",ipa:"/kˈwɔrtər tɪ  kˈwɔrtər pæst/",d:"15 minutes before / after the hour"},
            {w:"morning shift",ipa:"/ˈmɔrnɪŋ ʃɪft/",d:"Work that happens early in the day"},
            {w:"lunch break",ipa:"/lənʧ breɪk/",d:"A short rest in the middle of the day"},
            {w:"working hours",ipa:"/ˈwərkɪŋ aʊərz/",d:"The hours you are at work"},
            {w:"day off",ipa:"/deɪ ɔf/",d:"A day when you do not work"},
            {w:"deadline",ipa:"/ˈdɛˌdlaɪn/",d:"The last day or time to finish a task"}
        ]}},
        {type:"ls",tl:"Listening",cb:"BEC Preliminary",title:"Audio: A New Employee Asks About the Schedule",ins:"Listen to a manager explaining office hours. Then answer the questions.",content:{tts:"Manager: Welcome to Globex, Carla. Let me explain your schedule. We open at nine o'clock in the morning and close at six in the evening. You start work at nine. Carla: OK. And what about lunch? Manager: Lunch break is from one to two. You can eat in the cafeteria on the second floor. Carla: That's good. Do we have meetings every day? Manager: We have a short team meeting every Monday at half past nine. On Friday at four o'clock we have a weekly review. Carla: And weekends? Manager: Saturday and Sunday are days off. Welcome to the team!",qs:[
            {q:"What time does work start?",o:["8:00","8:30","9:00","9:30"],a:2},
            {q:"When is the lunch break?",o:["12 to 1","1 to 2","2 to 3","12 to 2"],a:1},
            {q:"What day is the weekly review?",o:["Monday","Wednesday","Friday","Saturday"],a:2}
        ]}},
        {type:"fl",tl:"Open Cloze",title:"Telling the Time",ins:"Type the missing time word.",content:{ss:[
            {t:"It's nine ___, time to start work.",a:"o'clock"},
            {t:"The meeting is at half ___ ten.",a:"past"},
            {t:"My lunch ___ is from 1 to 2.",a:"break"},
            {t:"Saturday is my day ___.",a:"off"},
            {t:"The ___ for the report is Friday.",a:"deadline"}
        ]}},
        {type:"mt",tl:"Matching",title:"Match the Time to the Activity",ins:"Match each time with the typical activity.",content:{l:["9:00 AM","12:30 PM","3:00 PM","5:30 PM","6:00 PM"],r:["End of the working day","Coffee meeting with a client","Start of work","Leave the office","Lunch break"],ans:{0:2,1:4,2:1,3:3,4:0}}},
        {type:"wr",tl:"Writing",title:"Describe Your Daily Schedule",ins:"Write about your daily work schedule. Use simple sentences. (50-70 words)",content:{prompt:"Write 5-7 sentences about your day at work. Start at the morning and finish at the evening.",tips:"Use: I start work at..., I have lunch at..., I finish at..., On Mondays we have...",minWords:50}}
    ]},
    // ---------- A1-17 ----------
    {id:"be-a1-17",title:"Unit 17: Asking for Directions in the Office",subtitle:"Find rooms, floors and people in a building",exercises:[
        {type:"vc",tl:"Vocabulary",title:"Office Places & Directions",ins:"Learn these words to find your way in an office.",content:{words:[
            {w:"reception",ipa:"/rɪˈsɛpʃən/",d:"The first place you arrive in a building"},
            {w:"meeting room",ipa:"/ˈmitɪŋ rum/",d:"A room for meetings"},
            {w:"lift / elevator",ipa:"/lɪft  ˈɛləˌveɪtər/",d:"A machine to go up and down floors"},
            {w:"stairs",ipa:"/stɛrz/",d:"Steps to go between floors"},
            {w:"floor",ipa:"/flɔr/",d:"A level of the building (1st, 2nd, 3rd...)"},
            {w:"next to",ipa:"/nɛkst tɪ/",d:"Beside, very near"},
            {w:"opposite",ipa:"/ˈɑpəzɪt/",d:"On the other side"},
            {w:"on the left / right",ipa:"/ɔn ðə lɛft  raɪt/",d:"Direction when you walk"}
        ]}},
        {type:"ls",tl:"Listening",cb:"BEC Preliminary",title:"Audio: Where Is the Meeting Room?",ins:"Listen and find the right room.",content:{tts:"Visitor: Excuse me, I have a meeting with Mr. Park at ten o'clock. Receptionist: OK, his office is on the third floor. Take the lift, it's behind you on the right. Visitor: Thank you. And the meeting room? Receptionist: When you go out of the lift, turn left. The meeting room is opposite the kitchen. It's room 305. Visitor: Room 305, third floor. And the bathroom? Receptionist: It's next to the lift on every floor. Visitor: Perfect, thank you very much. Receptionist: You're welcome.",qs:[
            {q:"Which floor is Mr. Park's office on?",o:["First","Second","Third","Fourth"],a:2},
            {q:"What is the meeting room number?",o:["305","350","503","530"],a:0},
            {q:"Where is the bathroom?",o:["Opposite the kitchen","Next to the lift","On the first floor","Inside the meeting room"],a:1}
        ]}},
        {type:"dd",tl:"Drag & Drop",title:"Complete the Directions",ins:"Drag the correct phrase into each gap.",content:{ws:["take the lift","on the left","next to","opposite","third floor"],ss:[
            {t:"The CEO's office is on the ___.",b:"third floor"},
            {t:"To go up, please ___.",b:"take the lift"},
            {t:"The kitchen is ___ the meeting room.",b:"opposite"},
            {t:"The printer is ___ my desk.",b:"next to"},
            {t:"When you exit the lift, turn ___.",b:"on the left"}
        ]}},
        {type:"mt",tl:"Matching",title:"Match Question and Answer",ins:"Match each question with the correct response.",content:{l:["Where is the meeting room?","Excuse me, where is reception?","Is the bathroom on this floor?","Where can I find Mr. Lee?","Is there a coffee machine?"],r:["Yes, on every floor.","On the second floor, room 210.","Yes, next to the kitchen.","His office is opposite mine.","On the ground floor."],ans:{0:1,1:4,2:0,3:3,4:2}}}
    ]},
    // ---------- A1-18 ----------
    {id:"be-a1-18",title:"Unit 18: Basic Email - Greetings & Sign-offs",subtitle:"Start and finish a simple business email",exercises:[
        {type:"vc",tl:"Vocabulary",cb:"BEC Preliminary",title:"Email Phrases",ins:"Learn how to start and finish an email.",content:{words:[
            {w:"Dear Mr. / Ms. Smith,",ipa:"/dɪr ˈmɪstər.  mɪz. smɪθ,/",d:"Formal greeting when you know the name"},
            {w:"Hi John,",ipa:"/haɪ ʤɑn,/",d:"Informal greeting for colleagues"},
            {w:"Dear Sir or Madam,",ipa:"/dɪr sər ər ˈmædəm,/",d:"Formal, when you don't know the name"},
            {w:"Best regards,",ipa:"/bɛst rɪˈgɑrdz,/",d:"Polite, neutral sign-off"},
            {w:"Kind regards,",ipa:"/kaɪnd rɪˈgɑrdz,/",d:"Friendly but professional sign-off"},
            {w:"Thanks,",ipa:"/θæŋks,/",d:"Informal sign-off"},
            {w:"Yours sincerely,",ipa:"/jʊrz sɪnˈsɪrli,/",d:"Very formal, after Dear + name"},
            {w:"Yours faithfully,",ipa:"/jʊrz ˈfeɪθfəli,/",d:"Very formal, after Dear Sir or Madam"}
        ]}},
        {type:"mt",tl:"Matching",title:"Greeting Goes With Sign-off",ins:"Match the email opening with the correct closing.",content:{l:["Dear Mr. Cohasset,","Dear Sir or Madam,","Hi Anna,","Dear Team,","Hello Mr. Park,"],r:["Yours faithfully,","Hope to see you soon, Marco","Yours sincerely,","Best regards,","Thanks, Marco"],ans:{0:2,1:0,2:4,3:3,4:1}}},
        {type:"dd",tl:"Drag & Drop",title:"Build a Simple Email",ins:"Drag the right phrase to each part of the email.",content:{ws:["Dear Ms. Vargas,","I am writing to","Could you please","Best regards,","Marco Rossi"],ss:[
            {t:"___ (greeting)",b:"Dear Ms. Vargas,"},
            {t:"___ confirm our meeting on Tuesday.",b:"I am writing to"},
            {t:"___ send me the agenda?",b:"Could you please"},
            {t:"___ (sign-off)",b:"Best regards,"},
            {t:"___ (your name)",b:"Marco Rossi"}
        ]}},
        {type:"fl",tl:"Open Cloze",title:"Email Sentences",ins:"Type the missing word.",content:{ss:[
            {t:"___ Mr. Park, I am writing to confirm the meeting.",a:"Dear"},
            {t:"Best ___, Marco.",a:"regards"},
            {t:"Yours ___, when you start with Dear Sir or Madam.",a:"faithfully"},
            {t:"Hi Anna, ___ for your help yesterday.",a:"Thanks"},
            {t:"I look ___ to hearing from you.",a:"forward"}
        ]}},
        {type:"wr",tl:"Writing",title:"Write a Short Email",ins:"Write a short email to a colleague to ask for the meeting agenda. (50-70 words)",content:{prompt:"To: maria.vargas@globex.com\nSubject: Meeting on Tuesday\n\n",tips:"Structure: 1) Greeting 2) Reason for writing 3) Clear request 4) Polite closing 5) Your name",minWords:50}}
    ]},
    // ---------- A1-19 ----------
    {id:"be-a1-19",title:"Unit 19: Numbers, Dates & Prices",subtitle:"Use numbers, dates and money in business",exercises:[
        {type:"vc",tl:"Vocabulary",title:"Numbers and Money",ins:"Learn these basic number and money words.",content:{words:[
            {w:"hundred / thousand / million",ipa:"/ˈhənərd  ˈθaʊzənd  ˈmɪljən/",d:"100 / 1,000 / 1,000,000"},
            {w:"dollar ($) / euro (€) / pound (£)",ipa:"/ˈdɔlər   ˈjʊrə €  paʊnd £/",d:"Common currencies"},
            {w:"price",ipa:"/praɪs/",d:"How much something costs"},
            {w:"discount",ipa:"/ˈdɪskaʊnt/",d:"A lower price"},
            {w:"total",ipa:"/ˈtoʊtəl/",d:"The full amount"},
            {w:"VAT / tax",ipa:"/væt  tæks/",d:"Money added by the government"},
            {w:"invoice",ipa:"/ˈɪnvɔɪs/",d:"A bill that shows what to pay"},
            {w:"due date",ipa:"/du deɪt/",d:"The day a payment must arrive"}
        ]}},
        {type:"ls",tl:"Listening",cb:"BEC Preliminary",title:"Audio: A Phone Order",ins:"Listen to a customer placing a small order.",content:{tts:"Sales: Apex Office Supplies, good morning. Customer: Hi, I'd like to order ten boxes of A4 paper, please. Sales: Of course. Each box is twelve dollars, so the total is one hundred and twenty dollars. Customer: OK, and is there a discount for big orders? Sales: Yes, ten percent for orders over one hundred dollars. So your total is one hundred and eight dollars, plus tax. Customer: Great. When can you deliver? Sales: We can deliver on Friday the fifteenth of June. Customer: Perfect. The invoice due date? Sales: Thirty days after delivery. Customer: Thank you very much.",qs:[
            {q:"How many boxes does the customer order?",o:["5","8","10","12"],a:2},
            {q:"What is the discount?",o:["5%","10%","15%","20%"],a:1},
            {q:"When is the delivery?",o:["June 5","June 15","June 25","July 5"],a:1}
        ]}},
        {type:"fl",tl:"Open Cloze",title:"Money & Dates",ins:"Type the missing word.",content:{ss:[
            {t:"The ___ of this laptop is one thousand dollars.",a:"price"},
            {t:"We give a 10% ___ for big clients.",a:"discount"},
            {t:"Please pay the ___ before Friday.",a:"invoice"},
            {t:"The ___ date is the 30th of June.",a:"due"},
            {t:"The ___ is two hundred and fifty euros.",a:"total"}
        ]}},
        {type:"mt",tl:"Matching",title:"Match the Number Style",ins:"Match the number to its written form.",content:{l:["1,500","€3.50","15/06/2026","12.5%","$1,000,000"],r:["one million dollars","fifteenth of June, 2026","one thousand five hundred","twelve point five percent","three euros fifty"],ans:{0:2,1:4,2:1,3:3,4:0}}},
        {type:"wr",tl:"Writing",title:"Write a Short Price Quote",ins:"Write a short email reply with a price quote for a small order. (50-70 words)",content:{prompt:"Hi Maria,\nThank you for your order...",tips:"Include: items, unit price, total, discount, delivery date, due date",minWords:50}}
    ]},
    // ---------- A1-20 CAPSTONE ----------
    {id:"be-a1-20",title:"Unit 20: Capstone - My First Day at Work",subtitle:"Review of A1: introductions, schedule, places, email, numbers",exercises:[
        {type:"rd",tl:"Reading",cb:"BEC Preliminary",title:"Welcome to Globex!",ins:"Read Carla's first day. Then answer.",content:{p:"<p><b>From: hr@globex.com</b><br><b>To: carla.romero@globex.com</b><br><b>Subject: Welcome to Globex</b></p><p>Dear Carla,</p><p>Welcome to Globex! We are happy you join our team. Here is the information for your first day.</p><p>Please come to our office at <b>9:00 AM</b> on Monday, the 8th of June. Reception is on the ground floor. Ask for Mr. Park, Head of HR. Your desk is on the third floor, next to the kitchen.</p><p>Please bring your ID card and your bank details. Lunch is from 1 to 2 PM in the cafeteria. We finish at 6 PM.</p><p>Best regards,<br>Mr. Park, HR Department</p>",src:"COHASSET Original - A1 Capstone",qs:[
            {q:"What time does Carla start?",o:["8:00","8:30","9:00","9:30"],a:2},
            {q:"Where is reception?",o:["Ground floor","Second floor","Third floor","Fifth floor"],a:0},
            {q:"What must Carla bring?",o:["Lunch","ID card and bank details","A laptop","A book"],a:1}
        ]}},
        {type:"mt",tl:"Matching",title:"Review: Match the Question to the Answer",ins:"A short review of A1 functions.",content:{l:["What do you do?","What time do you finish?","Where is your office?","How much is it?","When is the deadline?"],r:["At six o'clock.","Friday the 15th.","On the third floor.","I am an accountant.","Fifty euros."],ans:{0:3,1:0,2:2,3:4,4:1}}},
        {type:"dd",tl:"Drag & Drop",title:"Carla's Reply Email",ins:"Drag each phrase to the right gap.",content:{ws:["Dear Mr. Park,","Thank you for","I will bring","Best regards,","Carla Romero"],ss:[
            {t:"___ (greeting)",b:"Dear Mr. Park,"},
            {t:"___ your warm welcome.",b:"Thank you for"},
            {t:"___ my ID card on Monday.",b:"I will bring"},
            {t:"___ (sign-off)",b:"Best regards,"},
            {t:"___ (name)",b:"Carla Romero"}
        ]}},
        {type:"wr",tl:"Writing",title:"Capstone: Reply to the Welcome Email",ins:"Write a short, polite reply to Mr. Park. Confirm the time, say thank you, ask one question. (60-80 words)",content:{prompt:"Dear Mr. Park,\n\nThank you for your email...\n",tips:"Include: 1) Greeting 2) Thanks 3) Confirm Monday 9:00 AM 4) One simple question (e.g. dress code) 5) Sign-off",minWords:55}}
    ]}
],

// ========== A2 EXTENSION ==========
a2: [
    // ---------- A2-16 ----------
    {id:"be-a2-16",title:"Unit 16: Voicemail - Leaving and Taking Messages",subtitle:"Leave clear messages and write down what callers say",exercises:[
        {type:"vc",tl:"Vocabulary",cb:"BEC Preliminary",title:"Voicemail Phrases",ins:"Learn these phrases for phone messages.",content:{words:[
            {w:"to leave a message",ipa:"/tɪ liv ə ˈmɛsɪʤ/",d:"to record what you want to say"},
            {w:"to take a message",ipa:"/tɪ teɪk ə ˈmɛsɪʤ/",d:"to write down what someone says"},
            {w:"This is...",ipa:"/ðɪs ɪz.../",d:"how you say your name on the phone"},
            {w:"calling regarding...",ipa:"/ˈkɔlɪŋ rɪˈgɑrdɪŋ.../",d:"the topic of your call"},
            {w:"to call back",ipa:"/tɪ kɔl bæk/",d:"to return a phone call"},
            {w:"available",ipa:"/əˈveɪləbəl/",d:"free, able to talk"},
            {w:"please get back to me",ipa:"/pliz gɪt bæk tɪ mi/",d:"please answer me later"},
            {w:"extension",ipa:"/ɪkˈstɛnʃən/",d:"a short internal phone number"}
        ]}},
        {type:"ls",tl:"Listening",cb:"BEC Preliminary",title:"Audio: Two Voicemail Messages",ins:"Listen to two voicemails left for the same person.",content:{tts:"Voicemail one: Hi Tom, this is Sarah from Apex Logistics. I'm calling regarding the shipment to Lima. There was a small delay at customs, but everything is fine now. The boxes will arrive on Thursday morning, not Wednesday. Could you please let your client know? You can call me back on extension three-four-six. Thanks, bye. Voicemail two: Hello Tom, it's Diego from Globex. I tried to reach you about tomorrow's meeting. We need to move it from ten to eleven because the boardroom is busy. Please confirm by email if possible, or call me back on my mobile, nine-eight-seven, six-five-four, three-two-one. Thanks, talk soon.",qs:[
            {q:"Why is Sarah calling?",o:["A new contract","A delayed shipment","A complaint","A meeting"],a:1},
            {q:"When will the boxes arrive?",o:["Tuesday","Wednesday","Thursday","Friday"],a:2},
            {q:"What does Diego want?",o:["To cancel the meeting","To change the time","To change the place","To send an email"],a:1}
        ]}},
        {type:"dd",tl:"Drag & Drop",title:"Build a Clear Voicemail",ins:"Drag each part to the correct order.",content:{ws:["Hi, this is Marco from Cohasset.","I'm calling regarding the May invoice.","Could you please call me back","on extension 215.","Thanks, bye."],ss:[
            {t:"1. ___",b:"Hi, this is Marco from Cohasset."},
            {t:"2. ___",b:"I'm calling regarding the May invoice."},
            {t:"3. ___",b:"Could you please call me back"},
            {t:"4. ___",b:"on extension 215."},
            {t:"5. ___",b:"Thanks, bye."}
        ]}},
        {type:"fl",tl:"Open Cloze",cb:"BEC Preliminary",title:"Phone Phrases",ins:"Type one word in each gap.",content:{ss:[
            {t:"Hi, this ___ Anna from Apex.",a:"is"},
            {t:"I'm ___ regarding your last email.",a:"calling"},
            {t:"Please ___ me back this afternoon.",a:"call"},
            {t:"Could you ___ a message, please?",a:"take"},
            {t:"My ___ number is 215.",a:"extension"}
        ]}},
        {type:"wr",tl:"Writing",title:"Write a Phone Message Note",ins:"You took a call for your boss. Write the note (paper message) for them. (60-90 words)",content:{prompt:"Message for: Ms. Vargas\nFrom:\nCompany:\nPhone:\nTime:\nMessage:\nAction needed:",tips:"Be short and clear. Use bullet points or short lines.",minWords:55}}
    ]},
    // ---------- A2-17 ----------
    {id:"be-a2-17",title:"Unit 17: Office Etiquette & Polite Requests",subtitle:"Make polite requests and respond to colleagues",exercises:[
        {type:"vc",tl:"Vocabulary",cb:"BEC Preliminary",title:"Polite Request Forms",ins:"Learn polite request structures.",content:{words:[
            {w:"Could you...?",ipa:"/kʊd ju...?/",d:"polite request, present"},
            {w:"Would you mind ___ing?",ipa:"/wʊd ju maɪnd ___ɪŋ?/",d:"very polite request"},
            {w:"I was wondering if...",ipa:"/aɪ wɑz ˈwəndərɪŋ ɪf.../",d:"soft, indirect request"},
            {w:"Do you mind if I...?",ipa:"/du ju maɪnd ɪf aɪ...?/",d:"asking permission"},
            {w:"I'd appreciate it if...",ipa:"/aɪd əˈpriʃiˌeɪt ɪt ɪf.../",d:"polite formal request"},
            {w:"Sure, no problem.",ipa:"/ʃʊr, noʊ ˈprɑbləm./",d:"agreeing to a request"},
            {w:"I'm afraid I can't.",ipa:"/əm əˈfreɪd aɪ kænt./",d:"polite refusal"},
            {w:"Let me check.",ipa:"/lɛt mi ʧɛk./",d:"saying you'll find out"}
        ]}},
        {type:"kt",tl:"Key Word Transformation",cb:"BEC Preliminary",title:"Make It More Polite",ins:"Transform direct requests into polite ones using the keyword.",content:{ss:[
            {t:"Open the window.",k:"COULD",a:"Could you open the window?"},
            {t:"Help me with this report.",k:"WOULD",a:"Would you mind helping me with this report?"},
            {t:"I will use your phone.",k:"MIND",a:"Do you mind if I use your phone?"},
            {t:"Send me the file today.",k:"APPRECIATE",a:"I'd appreciate it if you sent me the file today."},
            {t:"Are you free tomorrow?",k:"WONDERING",a:"I was wondering if you were free tomorrow."}
        ]}},
        {type:"ls",tl:"Listening",cb:"BEC Preliminary",title:"Audio: Open-plan Office Etiquette",ins:"Listen to two colleagues solving a small office problem.",content:{tts:"Lucia: Hi Pablo, do you have a minute? Pablo: Sure, what's up? Lucia: I'm trying to focus on this proposal but the music from your speakers is a bit loud. Would you mind using headphones? Pablo: Oh, I'm so sorry! I didn't realize. Of course, I'll plug them in right now. Lucia: Thanks, I really appreciate it. Also, could you please not eat at your desk? The smell is strong and it's an open space. Pablo: Sure, no problem. I'll go to the kitchen for lunch. Lucia: Thank you so much, Pablo. Pablo: No worries, thanks for telling me politely.",qs:[
            {q:"What is Lucia's first request?",o:["Stop talking","Use headphones","Move desks","Turn off the computer"],a:1},
            {q:"What is the second request?",o:["Don't eat at the desk","Don't drink coffee","Be quiet","Close the door"],a:0},
            {q:"How does Pablo react?",o:["Angrily","Politely","He refuses","He laughs"],a:1}
        ]}},
        {type:"mt",tl:"Matching",title:"Request and Response",ins:"Match each polite request with a typical response.",content:{l:["Could you help me with this?","Do you mind if I borrow your charger?","Would you mind closing the door?","I was wondering if you had time today.","I'd appreciate it if you finished by Friday."],r:["Sure, of course, I'll do my best.","I'm afraid I'm busy until 4.","Of course, take it.","Sure, no problem.","Sure, what do you need?"],ans:{0:4,1:2,2:3,3:1,4:0}}},
        {type:"wr",tl:"Writing",title:"Polite Email to a Colleague",ins:"Write a short email asking a colleague to swap shifts on Friday. Be polite. (70-100 words)",content:{prompt:"Hi [name],\nI hope you're well...",tips:"Use: I was wondering if..., Would you mind...?, I'd really appreciate it. End with: Thanks so much / Let me know.",minWords:70}}
    ]},
    // ---------- A2-18 ----------
    {id:"be-a2-18",title:"Unit 18: Visiting Clients - Preparation & Behavior",subtitle:"Prepare, arrive and behave well at a client's office",exercises:[
        {type:"vc",tl:"Vocabulary",title:"Client Visit Words",ins:"Learn words for visiting clients.",content:{words:[
            {w:"appointment",ipa:"/əˈpɔɪntmənt/",d:"a fixed meeting time"},
            {w:"agenda",ipa:"/əˈʤɛndə/",d:"the list of things to discuss"},
            {w:"to confirm",ipa:"/tɪ kənˈfərm/",d:"to say yes again"},
            {w:"dress code",ipa:"/drɛs koʊd/",d:"how you must dress"},
            {w:"on time",ipa:"/ɔn taɪm/",d:"not late"},
            {w:"to introduce",ipa:"/tɪ ˌɪntrəˈdus/",d:"to present someone"},
            {w:"small talk",ipa:"/smɔl tɔk/",d:"polite light conversation"},
            {w:"follow-up",ipa:"/ˈfɑloʊˌəp/",d:"contact after the meeting"}
        ]}},
        {type:"rd",tl:"Reading",cb:"BEC Preliminary",title:"Five Tips Before You Visit a Client",ins:"Read the tips and answer.",content:{p:"<p><b>Five tips for a great client visit</b></p><p>1. <b>Confirm the appointment</b> the day before by email or phone. Clients are busy, and small changes happen often.</p><p>2. <b>Read the agenda</b> in advance. Know who will be in the room and what topics will come up.</p><p>3. <b>Dress one level above</b> the client's normal dress code. If they wear smart casual, wear business casual.</p><p>4. <b>Arrive 10 minutes early</b>. Use this time to relax, check your tablet and review your notes.</p><p>5. <b>Send a follow-up email</b> within 24 hours. Thank the client and write three short bullet points with the next steps.</p>",src:"COHASSET Original - Client Visits",qs:[
            {q:"When should you confirm?",o:["A week before","The day before","Same day","After the visit"],a:1},
            {q:"How early should you arrive?",o:["5 min","10 min","20 min","30 min"],a:1},
            {q:"Within how long must you send a follow-up?",o:["1 hour","6 hours","24 hours","1 week"],a:2}
        ]}},
        {type:"dd",tl:"Drag & Drop",title:"Stages of a Client Visit",ins:"Put the stages in the correct order.",content:{ws:["Confirm the appointment","Arrive 10 minutes early","Make small talk and introductions","Discuss the agenda","Send a follow-up email"],ss:[
            {t:"1. ___",b:"Confirm the appointment"},
            {t:"2. ___",b:"Arrive 10 minutes early"},
            {t:"3. ___",b:"Make small talk and introductions"},
            {t:"4. ___",b:"Discuss the agenda"},
            {t:"5. ___",b:"Send a follow-up email"}
        ]}},
        {type:"fl",tl:"Open Cloze",cb:"BEC Preliminary",title:"Visit Phrases",ins:"Type one word in each gap.",content:{ss:[
            {t:"I'd like to ___ our meeting on Tuesday.",a:"confirm"},
            {t:"What is the dress ___?",a:"code"},
            {t:"Please arrive ___ time.",a:"on"},
            {t:"Let me ___ you to my colleague.",a:"introduce"},
            {t:"I'll send a ___-up email tomorrow.",a:"follow"}
        ]}},
        {type:"wr",tl:"Writing",title:"Follow-up Email After a Visit",ins:"Write a short follow-up email after a client visit. Thank them and list three next steps. (80-100 words)",content:{prompt:"Subject: Thank you - meeting on Tuesday\n\nDear Ms. Vargas,\n",tips:"Structure: 1) Thanks 2) Brief recap 3) 3 short next steps as bullets 4) Polite closing",minWords:70}}
    ]},
    // ---------- A2-19 ----------
    {id:"be-a2-19",title:"Unit 19: Talking About Past Projects & Achievements",subtitle:"Use past simple to describe completed work",exercises:[
        {type:"vc",tl:"Vocabulary",title:"Project Verbs (Past Simple)",ins:"Learn these past forms.",content:{words:[
            {w:"led / managed",ipa:"/lɛd  ˈmænɪʤd/",d:"was the boss of a project or team"},
            {w:"developed",ipa:"/dɪˈvɛləpt/",d:"created something new"},
            {w:"launched",ipa:"/lɔnʧt/",d:"started something new on the market"},
            {w:"reduced",ipa:"/rɪˈdust/",d:"made smaller (costs, time, errors)"},
            {w:"improved",ipa:"/ˌɪmˈpruvd/",d:"made better"},
            {w:"increased",ipa:"/ˌɪnˈkrist/",d:"made bigger (sales, revenue)"},
            {w:"completed",ipa:"/kəmˈplitɪd/",d:"finished"},
            {w:"delivered",ipa:"/dɪˈlɪvərd/",d:"gave to the client on time"}
        ]}},
        {type:"ls",tl:"Listening",cb:"BEC Preliminary",title:"Audio: A Job Interview - Past Project",ins:"Listen to a candidate describe a past project.",content:{tts:"Interviewer: Tell me about a project you are proud of. Candidate: Sure. Last year I led a small team at Apex. We developed a new mobile app for our delivery clients. The project lasted six months. We started in January and we delivered in June. I managed three developers and one designer. We reduced delivery errors by twenty percent and we increased customer satisfaction. The biggest challenge was time, because we had only six months. We also worked with a client in Brazil, so I improved my Portuguese. In the end, we launched on time and the CEO sent a thank-you email to the team.",qs:[
            {q:"How long did the project last?",o:["3 months","4 months","6 months","12 months"],a:2},
            {q:"How many people were on the team?",o:["2","3","4","5"],a:2},
            {q:"What did the project reduce?",o:["Delivery time","Delivery errors","Costs","Staff"],a:1}
        ]}},
        {type:"wf",tl:"Word Formation",title:"Achievement Nouns",ins:"Use the root word in brackets.",content:{ss:[
            {t:"Our biggest (achieve) was reducing costs.",a:"achievement"},
            {t:"The team showed great (leader).",a:"leadership"},
            {t:"The product launch was a real (succeed).",a:"success"},
            {t:"We focused on customer (satisfy).",a:"satisfaction"},
            {t:"Our (improve) plan worked very well.",a:"improvement"}
        ]}},
        {type:"kt",tl:"Key Word Transformation",cb:"BEC Preliminary",title:"Past Achievements",ins:"Rewrite using the keyword.",content:{ss:[
            {t:"I was the leader of the project.",k:"LED",a:"I led the project."},
            {t:"Sales went up by 15% last quarter.",k:"INCREASED",a:"Sales increased by 15% last quarter."},
            {t:"We finished the report on time.",k:"COMPLETED",a:"We completed the report on time."},
            {t:"The new system made things better.",k:"IMPROVED",a:"The new system improved things."}
        ]}},
        {type:"wr",tl:"Writing",title:"Describe a Past Project",ins:"Describe a project you completed last year. Use past simple. (80-100 words)",content:{prompt:"Last year, I worked on a project called...",tips:"Include: 1) Project name 2) Your role 3) Team size 4) Time frame 5) Result with a number 6) One challenge",minWords:70}}
    ]},
    // ---------- A2-20 CAPSTONE ----------
    {id:"be-a2-20",title:"Unit 20: Capstone - Weekly Status Update Email",subtitle:"Write a clear weekly update for your manager",exercises:[
        {type:"rd",tl:"Reading",cb:"BEC Preliminary",title:"A Weekly Update Email",ins:"Read this weekly update and answer.",content:{p:"<p><b>Subject: Weekly update - Week 22</b></p><p>Hi Maria,</p><p>Here is my update for this week.</p><p><b>Done this week:</b><br>- Finished the May report.<br>- Met with the Lima client and confirmed the new contract.<br>- Reduced shipping errors from 8% to 5%.</p><p><b>In progress:</b><br>- Training the new sales assistant.<br>- Preparing the budget for Q3.</p><p><b>Next week:</b><br>- Visit Apex on Tuesday.<br>- Send the first Q3 budget draft on Thursday.</p><p><b>Help needed:</b> I need approval for the travel cost (around $400).</p><p>Best regards,<br>Diego</p>",src:"COHASSET Original - Weekly Updates",qs:[
            {q:"What did Diego finish this week?",o:["The Q3 budget","The May report","The new training","The Lima trip"],a:1},
            {q:"What is in progress?",o:["Lima visit","Training the new assistant","May report","Apex visit"],a:1},
            {q:"How much travel cost approval is needed?",o:["$200","$300","$400","$500"],a:2}
        ]}},
        {type:"mt",tl:"Matching",title:"Match Section to Content",ins:"Match each section with its purpose.",content:{l:["Done this week","In progress","Next week","Help needed","Subject line"],r:["Tasks where you need a decision or resource","Plans for the coming days","Quick title that says what the email is about","Tasks ongoing now","Tasks finished this week"],ans:{0:4,1:3,2:1,3:0,4:2}}},
        {type:"fl",tl:"Open Cloze",cb:"BEC Preliminary",title:"Weekly Update Phrases",ins:"Type one word in each gap.",content:{ss:[
            {t:"Here is my update ___ this week.",a:"for"},
            {t:"I have ___ the May report.",a:"finished"},
            {t:"We are ___ the new assistant.",a:"training"},
            {t:"___ week, I will visit Apex.",a:"Next"},
            {t:"I need ___ for the travel cost.",a:"approval"}
        ]}},
        {type:"wr",tl:"Writing",title:"Capstone: Your Weekly Update",ins:"Write your own weekly update email to your manager. Use the four sections. (90-110 words)",content:{prompt:"Subject: Weekly update - Week ___\n\nHi [Manager],\n",tips:"Use four bullet sections: Done this week / In progress / Next week / Help needed. Keep each item short (one line).",minWords:80}}
    ]}
],

// ========== B1 EXTENSION ==========
b1: [
    // ---------- B1-16 ----------
    {id:"be-b1-16",title:"Unit 16: Cross-Cultural Business Communication",subtitle:"Adapt your style to colleagues from different cultures",exercises:[
        {type:"vc",tl:"Vocabulary",cb:"BEC Vantage",title:"Cross-Cultural Terms",ins:"Learn these key concepts.",content:{words:[
            {w:"high-context / low-context",ipa:"/high-context  low-context/",d:"cultures where meaning is implicit / explicit"},
            {w:"hierarchy",ipa:"/ˈhaɪˌrɑrki/",d:"a system of levels of authority"},
            {w:"face-saving",ipa:"/face-saving/",d:"protecting someone's dignity in public"},
            {w:"directness",ipa:"/dɪˈrɛknəs/",d:"how openly people say what they think"},
            {w:"small talk",ipa:"/smɔl tɔk/",d:"informal social conversation before business"},
            {w:"punctuality",ipa:"/ˌpəŋkʧuˈælɪti/",d:"how strictly people follow time"},
            {w:"to make assumptions",ipa:"/tɪ meɪk əˈsəmpʃənz/",d:"to believe something without proof"},
            {w:"cultural awareness",ipa:"/ˈkəlʧərəl əˈwɛrnəs/",d:"understanding of cultural differences"}
        ]}},
        {type:"rd",tl:"Reading",cb:"BEC Vantage",title:"When Yes Doesn't Mean Yes",ins:"Read the article and answer.",content:{p:"<p>Cross-cultural mistakes rarely happen because of bad intentions. They happen because we expect other people to communicate the way we do. In low-context cultures like Germany or the Netherlands, employees often say exactly what they think; clear disagreement is seen as honest. In high-context cultures such as Japan, Indonesia or many Latin American countries, polite indirect language is preferred, and a soft 'yes' may simply mean 'I have heard you' rather than 'I agree'.</p><p>Hierarchy also matters. In some cultures, junior staff openly challenge their managers in meetings; in others, this would cause embarrassment, or 'loss of face'. International teams should agree on simple ground rules: how to give feedback, how to disagree, and whether decisions are made in the meeting or after private consultation. A short 'culture chart' shared at project kickoff can save weeks of misunderstanding later.</p>",src:"COHASSET Original - inspired by Erin Meyer style",qs:[
            {q:"In high-context cultures, 'yes' often means:",o:["I agree completely","I have heard you","I refuse","Let's vote"],a:1},
            {q:"What can save weeks of trouble?",o:["A long contract","A culture chart at kickoff","Travel","Email only"],a:1},
            {q:"What is 'loss of face'?",o:["Bad lighting","Public embarrassment","Bad signal","Forgetting names"],a:1}
        ]}},
        {type:"mt",tl:"Matching",title:"Cultural Tendencies",ins:"Match each statement with the typical communication style.",content:{l:["Meaning is mostly in the words","Meaning depends on context and tone","Meetings start with 10 minutes of small talk","Decisions are clearly stated and signed in the room","Disagreement is shown through silence or change of subject"],r:["Indirect / high-context","Direct / low-context","Indirect / high-context","Direct / low-context","Relationship-first / high-context"],ans:{0:1,1:0,2:4,3:3,4:2}}},
        {type:"kt",tl:"Key Word Transformation",cb:"BEC Vantage",title:"Polite, Indirect Style",ins:"Make these direct sentences less direct using the keyword.",content:{ss:[
            {t:"This idea is wrong.",k:"CONCERNS",a:"I have some concerns about this idea."},
            {t:"You must change the deadline.",k:"COULD",a:"Could we possibly look at changing the deadline?"},
            {t:"I disagree.",k:"DIFFERENTLY",a:"I see things slightly differently."},
            {t:"Your report has many mistakes.",k:"AREAS",a:"There are a few areas in your report we could improve."}
        ]}},
        {type:"wr",tl:"Writing",title:"Cross-Cultural Briefing Note",ins:"Your team is starting a project with partners in another country. Write a short briefing note (130-180 words) with 4 cultural tips.",content:{prompt:"BRIEFING NOTE\nTo: Project team\nRe: Working with our new partner in [country]\n",tips:"Use bullets. Cover: communication style, hierarchy, time/punctuality, meetings/decisions. End with one clear ground rule.",minWords:120}}
    ]},
    // ---------- B1-17 ----------
    {id:"be-b1-17",title:"Unit 17: Time Management & Prioritization",subtitle:"Plan your week with simple frameworks",exercises:[
        {type:"vc",tl:"Vocabulary",cb:"BEC Vantage",title:"Time Management Terms",ins:"Learn these key terms.",content:{words:[
            {w:"to prioritize",ipa:"/tɪ praɪˈɔrəˌtaɪz/",d:"to decide what to do first"},
            {w:"urgent vs. important",ipa:"/ˈərʤənt ˈvərsəz. ˌɪmˈpɔrtənt/",d:"the basis of the Eisenhower Matrix"},
            {w:"deadline",ipa:"/ˈdɛˌdlaɪn/",d:"the final date to finish a task"},
            {w:"to delegate",ipa:"/tɪ ˈdɛləˌgeɪt/",d:"to give a task to someone else"},
            {w:"backlog",ipa:"/ˈbæˌklɔg/",d:"a list of unfinished tasks"},
            {w:"time-box",ipa:"/time-box/",d:"a fixed time slot for one task"},
            {w:"deep work",ipa:"/dip wərk/",d:"focused work without interruptions"},
            {w:"context switching",ipa:"/ˈkɑntɛkst sˈwɪʧɪŋ/",d:"changing tasks too often, losing focus"}
        ]}},
        {type:"rd",tl:"Reading",cb:"BEC Vantage",title:"The Eisenhower Matrix at Work",ins:"Read about the matrix and answer.",content:{p:"<p>Most professionals are not short of energy; they are short of focus. The Eisenhower Matrix divides every task into four boxes by combining two questions: is it urgent, and is it important?</p><p><b>Quadrant 1 (urgent and important)</b> includes crises, last-minute client issues and deadlines tomorrow. Do these now. <b>Quadrant 2 (important, not urgent)</b> covers planning, training and relationship building. Schedule these on your calendar; they create long-term results.</p><p><b>Quadrant 3 (urgent, not important)</b> includes most interruptions and many emails. Delegate them when possible. <b>Quadrant 4 (not urgent, not important)</b> includes excessive social media and unnecessary meetings. Eliminate these.</p><p>The trap for many managers is spending all day in Q1 and Q3 and never reaching Q2. As a result, the team feels busy but not productive.</p>",src:"COHASSET Original - based on Covey/Eisenhower",qs:[
            {q:"Which quadrant should you SCHEDULE?",o:["Q1","Q2","Q3","Q4"],a:1},
            {q:"What is the trap for managers?",o:["Working in Q4 only","Living in Q1 and Q3","Delegating too much","Refusing emails"],a:1},
            {q:"Q4 means:",o:["Crisis","Planning","Interruption","Eliminate"],a:3}
        ]}},
        {type:"dd",tl:"Drag & Drop",title:"Sort Tasks Into Quadrants",ins:"Drag each task to the correct quadrant.",content:{ws:["Q1","Q2","Q3","Q4","Q2"],ss:[
            {t:"Client server is down right now.",b:"Q1"},
            {t:"Plan next quarter's strategy.",b:"Q2"},
            {t:"Colleague asks for help with a small task.",b:"Q3"},
            {t:"Scrolling LinkedIn at lunch.",b:"Q4"},
            {t:"Coaching a junior team member.",b:"Q2"}
        ]}},
        {type:"fl",tl:"Open Cloze",cb:"BEC Vantage",title:"Time Management Sentences",ins:"One word per gap.",content:{ss:[
            {t:"I need to ___ this report by Friday.",a:"finish"},
            {t:"You should ___ this task to your assistant.",a:"delegate"},
            {t:"Let's ___ the meeting to 30 minutes.",a:"limit"},
            {t:"Deep work means working ___ interruptions.",a:"without"},
            {t:"My to-do list is too ___, I need to prioritize.",a:"long"}
        ]}},
        {type:"wr",tl:"Writing",title:"Productivity Plan",ins:"Write a 150-180-word plan to improve your team's productivity for the next month.",content:{prompt:"PRODUCTIVITY PLAN\nTeam: ___\nGoal: ___\n",tips:"Include: 1) Current problem 2) Two practical changes 3) How you will measure success 4) Risks and mitigation",minWords:130}}
    ]},
    // ---------- B1-18 ----------
    {id:"be-b1-18",title:"Unit 18: Workplace Conflict Resolution",subtitle:"Handle disagreements between colleagues constructively",exercises:[
        {type:"vc",tl:"Vocabulary",cb:"BEC Vantage",title:"Conflict Resolution Vocabulary",ins:"Learn these key terms.",content:{words:[
            {w:"to escalate",ipa:"/tɪ ˈɛskəˌleɪt/",d:"to take the issue to a higher level"},
            {w:"to de-escalate",ipa:"/tɪ de-escalate/",d:"to reduce tension"},
            {w:"common ground",ipa:"/ˈkɑmən graʊnd/",d:"things both sides agree on"},
            {w:"to mediate",ipa:"/tɪ ˈmidiˌeɪt/",d:"to help two sides agree"},
            {w:"a misunderstanding",ipa:"/ə ˌmɪsəndərˈstændɪŋ/",d:"failure to understand correctly"},
            {w:"to acknowledge",ipa:"/tɪ ækˈnɑlɪʤ/",d:"to recognize someone's point"},
            {w:"to compromise",ipa:"/tɪ ˈkɑmprəˌmaɪz/",d:"to find a middle solution"},
            {w:"win-win",ipa:"/ˌwɪnˈwɪn/",d:"a solution good for both sides"}
        ]}},
        {type:"ls",tl:"Listening",cb:"BEC Vantage",title:"Audio: A Manager Mediates a Conflict",ins:"Listen to a manager helping two team members.",content:{tts:"Manager: Thanks for coming, both of you. I'd like to understand what happened in yesterday's meeting. Sara, would you start? Sara: Sure. I felt that Diego ignored my proposal and then presented a similar idea ten minutes later as his own. Diego: That wasn't my intention at all. I didn't realize you had said something similar; I came in late and I missed the first ten minutes. I'm sorry if it looked that way. Manager: OK, so it sounds like there was a misunderstanding rather than bad intent. Sara, can you accept that? Sara: Yes, I appreciate the apology. I just want to be heard in meetings. Manager: That's fair. From now on, let's agree that whoever leads the meeting will recap the first ideas when latecomers join. Diego: That works for me. Sara: For me too. Manager: Great. Thank you both for being open about this.",qs:[
            {q:"What was Sara's feeling?",o:["Diego shouted","Diego copied her idea","Diego was late","Diego refused work"],a:1},
            {q:"What was Diego's reason?",o:["He disagreed","He didn't hear Sara","He was angry","He wanted credit"],a:1},
            {q:"What is the agreed rule?",o:["No latecomers","Recap ideas for latecomers","Send minutes only","No discussion"],a:1}
        ]}},
        {type:"mt",tl:"Matching",title:"Phrases for De-escalation",ins:"Match each function with the phrase.",content:{l:["I see your point.","Help me understand what happened.","Let's find a middle solution.","I think we both agree that...","I'm sorry that came across that way."],r:["Compromise","Acknowledge feeling","Apologize without blaming","Acknowledge the other","Invite explanation"],ans:{0:3,1:4,2:0,3:1,4:2}}},
        {type:"kt",tl:"Key Word Transformation",cb:"BEC Vantage",title:"Soft Conflict Language",ins:"Rewrite using the keyword.",content:{ss:[
            {t:"You are completely wrong.",k:"DIFFERENTLY",a:"I see this differently."},
            {t:"You never listen.",k:"FEEL",a:"I feel I am not always heard."},
            {t:"This is your fault.",k:"HAPPENED",a:"Let's understand what happened."},
            {t:"Stop arguing now.",k:"PAUSE",a:"Let's pause for a moment."}
        ]}},
        {type:"wr",tl:"Writing",title:"Email Resolving a Conflict",ins:"Write an email to a colleague after a disagreement, to repair the relationship. (160-200 words)",content:{prompt:"Subject: Following up on yesterday's conversation\n\nHi [name],\n",tips:"Use: acknowledge their feelings, apologize for any miscommunication, propose a clear next step, end on positive note.",minWords:140}}
    ]},
    // ---------- B1-19 ----------
    {id:"be-b1-19",title:"Unit 19: Vendor Selection & Comparing Quotes",subtitle:"Evaluate suppliers and choose the best offer",exercises:[
        {type:"vc",tl:"Vocabulary",cb:"BEC Vantage",title:"Procurement Vocabulary",ins:"Learn these supply-chain terms.",content:{words:[
            {w:"quote / quotation",ipa:"/kwoʊt  kwoʊˈteɪʃən/",d:"a written price offer"},
            {w:"RFP (Request for Proposal)",ipa:"/rfp (rɪkˈwɛst fər prəˈpoʊzəl)/",d:"a document asking suppliers to bid"},
            {w:"SLA (Service Level Agreement)",ipa:"/sla (ˈsərvɪs ˈlɛvəl əˈgrimənt)/",d:"a contract about quality of service"},
            {w:"lead time",ipa:"/lɛd taɪm/",d:"time from order to delivery"},
            {w:"unit price",ipa:"/ˈjunɪt praɪs/",d:"price per single item"},
            {w:"volume discount",ipa:"/ˈvɑljum ˈdɪskaʊnt/",d:"lower price for big orders"},
            {w:"references",ipa:"/ˈrɛfərənsɪz/",d:"other clients who can recommend the vendor"},
            {w:"shortlist",ipa:"/shortlist/",d:"a small list of finalists"}
        ]}},
        {type:"rd",tl:"Reading",cb:"BEC Vantage",title:"Choosing a New Logistics Partner",ins:"Read the procurement memo.",content:{p:"<p>Cohasset Imports needs a new freight partner for the Lima-Callao route. Three vendors were shortlisted from eleven RFP responses.</p><p><b>Andean Logistics</b> offered the lowest unit price ($1,200 per container) and a 90-day payment term, but their average lead time was 14 days and their references were mixed.</p><p><b>Pacific Freight</b> quoted $1,350 with a 60-day payment term, lead time of 9 days, and three strong references including Globex.</p><p><b>Apex Cargo</b> quoted $1,420, but offered a 7-day lead time, full container tracking, and a 99% on-time SLA backed by penalties.</p><p>The procurement committee recommends Pacific Freight: it is not the cheapest, but it offers the best balance of cost, speed and reliability for our service-sensitive client base. A pilot of 90 days is proposed before signing a 12-month contract.</p>",src:"COHASSET Original - Procurement memo",qs:[
            {q:"Who has the lowest unit price?",o:["Andean Logistics","Pacific Freight","Apex Cargo","All same"],a:0},
            {q:"Who has the shortest lead time?",o:["Andean (14 days)","Pacific (9 days)","Apex (7 days)","Same"],a:2},
            {q:"What is recommended?",o:["Andean","Pacific","Apex","None"],a:1}
        ]}},
        {type:"mt",tl:"Matching",title:"Selection Criteria",ins:"Match each criterion with its short definition.",content:{l:["Cost","Quality","Reliability","Flexibility","Reputation"],r:["Ability to change scope or volume","Total price including hidden fees","Public image and references","Defects and accuracy","Consistency of delivery"],ans:{0:1,1:3,2:4,3:0,4:2}}},
        {type:"kt",tl:"Key Word Transformation",cb:"BEC Vantage",title:"Comparing Vendors",ins:"Rewrite using the keyword.",content:{ss:[
            {t:"Apex is more expensive than Pacific.",k:"AS",a:"Pacific is not as expensive as Apex."},
            {t:"Andean has the longest lead time of all.",k:"FAR",a:"Andean's lead time is by far the longest."},
            {t:"Pacific is a good middle option.",k:"BALANCE",a:"Pacific offers the best balance."},
            {t:"We will test them for 90 days first.",k:"PILOT",a:"We will run a 90-day pilot first."}
        ]}},
        {type:"wr",tl:"Writing",title:"Vendor Recommendation Email",ins:"Write a 150-200-word email recommending one of three vendors. Use clear criteria.",content:{prompt:"Subject: Vendor recommendation - Logistics RFP\n\nDear Procurement Committee,\n",tips:"Structure: 1) Background 2) Three criteria with brief comparison 3) Recommendation with reason 4) Suggested next step (pilot/contract)",minWords:140}}
    ]},
    // ---------- B1-20 CAPSTONE ----------
    {id:"be-b1-20",title:"Unit 20: Capstone - Mini Business Proposal",subtitle:"Write a clear, structured 300-word proposal",exercises:[
        {type:"rd",tl:"Reading",cb:"BEC Vantage",title:"Anatomy of a Mini Proposal",ins:"Read the structure and answer.",content:{p:"<p>A short business proposal usually has six sections. The <b>Executive Summary</b> (2-3 sentences) tells the reader what you propose and why it matters. The <b>Problem or Opportunity</b> section gives evidence: numbers, complaints, market data. The <b>Proposed Solution</b> describes what you will do, in clear active sentences.</p><p>The <b>Implementation Plan</b> lists 3-5 concrete steps with owners and rough dates. The <b>Costs and Benefits</b> show estimated cost, expected return, and the breakeven point. Finally, <b>Next Steps</b> ask the reader for a clear decision: 'approve a pilot of 3 months,' or 'fund a feasibility study by 30 June.'</p><p>Good proposals are read in less than 5 minutes. Use bullet points, short paragraphs, and bold subheadings. Keep adjectives modest and numbers precise.</p>",src:"COHASSET Original - Proposal Writing",qs:[
            {q:"How many sections?",o:["4","5","6","7"],a:2},
            {q:"What does the Executive Summary do?",o:["Lists tasks","Says what and why","Lists costs","Names team"],a:1},
            {q:"How long should reading take?",o:["1 min","Under 5 min","15 min","30 min"],a:1}
        ]}},
        {type:"mt",tl:"Matching",title:"Section to Purpose",ins:"Match each section to its main purpose.",content:{l:["Executive Summary","Problem","Solution","Implementation","Costs & Benefits","Next Steps"],r:["Numbers and ROI","What we propose to do","Action requested from reader","One paragraph overview","Steps with owners","Evidence of the issue"],ans:{0:3,1:5,2:1,3:4,4:0,5:2}}},
        {type:"fl",tl:"Open Cloze",cb:"BEC Vantage",title:"Proposal Phrases",ins:"One word per gap.",content:{ss:[
            {t:"This proposal ___ a 90-day pilot.",a:"recommends"},
            {t:"The current process ___ 12% of staff time.",a:"wastes"},
            {t:"We expect a ___ on investment within 9 months.",a:"return"},
            {t:"___ the issue, customer complaints rose 30%.",a:"Regarding"},
            {t:"We ___ approval by the end of the month.",a:"request"}
        ]}},
        {type:"wr",tl:"Writing",title:"Capstone: Mini Business Proposal",ins:"Write a 280-320-word proposal for an internal improvement at Cohasset Imports (e.g. CRM, training, hybrid work, sustainability). Use all six sections.",content:{prompt:"BUSINESS PROPOSAL\nTitle:\nAuthor:\nDate:\n\n1. Executive Summary\n2. Problem/Opportunity\n3. Proposed Solution\n4. Implementation Plan\n5. Costs & Benefits\n6. Next Steps\n",tips:"Write tight: 50 words per section is fine. Use bullets in 4 and 5. End with one specific decision request.",minWords:240}}
    ]}
],

// ========== B2 EXTENSION ==========
b2: [
    // ---------- B2-16 ----------
    {id:"be-b2-16",title:"Unit 16: Strategic Decision-Making",subtitle:"Use frameworks to choose between options",exercises:[
        {type:"vc",tl:"Vocabulary",cb:"BEC Higher",title:"Decision-Making Frameworks",ins:"Learn these strategic terms.",content:{words:[
            {w:"trade-off",ipa:"/ˈtreɪˌdɔf/",d:"a sacrifice in one area to gain another"},
            {w:"opportunity cost",ipa:"/ˌɑpərˈtunəti kɔst/",d:"the value of the option you don't choose"},
            {w:"risk-adjusted return",ipa:"/risk-adjusted rɪˈtərn/",d:"return considering its risk"},
            {w:"counterfactual",ipa:"/counterfactual/",d:"imagining what would have happened otherwise"},
            {w:"second-order effects",ipa:"/second-order ˈifɛkts/",d:"indirect consequences of a decision"},
            {w:"sunk cost",ipa:"/səŋk kɔst/",d:"money already spent that should not influence future choices"},
            {w:"cognitive bias",ipa:"/ˈkɑgnɪtɪv baɪəs/",d:"a systematic error in thinking"},
            {w:"red team",ipa:"/rɛd tim/",d:"a group that argues against a proposal"}
        ]}},
        {type:"rd",tl:"Reading",cb:"BEC Higher",title:"Beyond the Pros-and-Cons List",ins:"Read and answer.",content:{p:"<p>Pros-and-cons lists feel disciplined, but they often hide more than they reveal. They give equal weight to items of unequal importance, ignore probabilities, and let the most articulate writer set the agenda. Mature organisations now combine four lenses.</p><p>The <b>WRAP</b> approach (Heath brothers) reminds leaders to <i>Widen</i> options, <i>Reality-test</i> assumptions, <i>Attain distance</i> before deciding, and <i>Prepare to be wrong</i>. <b>Pre-mortems</b>, popularised by Gary Klein, ask the team to imagine the project has failed and explain why; this surfaces risks that polite meetings would otherwise bury.</p><p><b>Expected value</b> calculations multiply the size of each outcome by its probability and force teams to be explicit. Finally, <b>red-teaming</b> assigns a separate group to argue against the dominant proposal, neutralising groupthink. Used together, these tools shift debates from rhetoric to evidence and structure.</p>",src:"COHASSET Original - WRAP/Klein synthesis",qs:[
            {q:"What does 'A' stand for in WRAP?",o:["Adapt","Attain distance","Audit","Approve"],a:1},
            {q:"A pre-mortem assumes:",o:["The plan will work","The plan has failed","Random failure","Customer success"],a:1},
            {q:"What does red-teaming counter?",o:["Underfunding","Groupthink","Time pressure","Bad data"],a:1}
        ]}},
        {type:"mt",tl:"Matching",title:"Framework to Use Case",ins:"Match each tool to the situation it's best for.",content:{l:["Pre-mortem","Expected value","Red team","Decision matrix","WRAP"],r:["Comparing many criteria across options","Avoiding optimism bias before launch","Stress-testing a dominant strategy","Quantifying uncertain outcomes","Structuring an entire decision process"],ans:{0:1,1:3,2:2,3:0,4:4}}},
        {type:"kt",tl:"Key Word Transformation",cb:"BEC Higher",title:"Hedged Recommendation Language",ins:"Rewrite using the keyword.",content:{ss:[
            {t:"This is the best option.",k:"APPEARS",a:"This appears to be the best option."},
            {t:"We will succeed.",k:"LIKELY",a:"It is likely that we will succeed."},
            {t:"There are risks.",k:"DOWNSIDE",a:"There is significant downside to consider."},
            {t:"We should not abandon the project because of past spending.",k:"SUNK",a:"We should not let sunk costs influence the decision."}
        ]}},
        {type:"wr",tl:"Writing",title:"Decision Memo",ins:"Write a 180-220-word decision memo recommending one of three strategic options. Apply at least two frameworks above.",content:{prompt:"DECISION MEMO\nTo:\nFrom:\nRe: Choice between Option A, B, C\n\n1. Recommendation\n2. Criteria\n3. Comparison\n4. Risks (pre-mortem)\n5. Decision requested\n",tips:"Use hedged but confident language. Quantify wherever possible. End with one clear ask.",minWords:160}}
    ]},
    // ---------- B2-17 ----------
    {id:"be-b2-17",title:"Unit 17: Crisis Communication & PR Basics",subtitle:"Speak with the public when things go wrong",exercises:[
        {type:"vc",tl:"Vocabulary",cb:"BEC Higher",title:"Crisis Communication Terms",ins:"Learn the basic toolkit.",content:{words:[
            {w:"holding statement",ipa:"/ˈhoʊldɪŋ ˈsteɪtmənt/",d:"a short first-response statement"},
            {w:"key messages",ipa:"/ki ˈmɛsɪʤɪz/",d:"3-5 priority points all spokespeople use"},
            {w:"stakeholders",ipa:"/ˈsteɪˌkhoʊldərz/",d:"groups affected by the crisis"},
            {w:"narrative control",ipa:"/ˈnɛrətɪv kənˈtroʊl/",d:"shaping the story before others do"},
            {w:"on the record / off the record",ipa:"/ɔn ðə ˈrɛkərd  ɔf ðə ˈrɛkərd/",d:"quotable / not quotable"},
            {w:"to apologise without admitting liability",ipa:"/tɪ əˈpɑləˌʤaɪz wɪˈθaʊt ədˈmɪtɪŋ ˌlaɪəˈbɪlɪti/",d:"saying sorry without taking legal blame"},
            {w:"dark site",ipa:"/dɑrk saɪt/",d:"a pre-built crisis website ready to publish"},
            {w:"post-mortem",ipa:"/poʊstˈmɔrtɛm/",d:"analysis after the crisis ends"}
        ]}},
        {type:"rd",tl:"Reading",cb:"BEC Higher",title:"The First 60 Minutes",ins:"Read this PR briefing.",content:{p:"<p>In a crisis, what you say in the first hour can shape weeks of coverage. Three principles guide most modern playbooks. <b>Speed beats polish</b>: a brief holding statement within 60 minutes prevents speculation from filling the void. It does not need details, only acknowledgment, concern, and commitment to investigate.</p><p><b>Empathy beats legalese</b>: language drafted only by lawyers usually sounds cold and amplifies anger. Trained communicators humanise the message while keeping liability in mind. <b>Consistency beats volume</b>: every spokesperson - CEO, social media, customer service, regional offices - must use the same key messages, even if the tone is adapted.</p><p>Above all, never speculate, never promise what you cannot deliver, and never delete posts. The internet has long memory. Apologise where appropriate, correct facts as they emerge, and focus on what you are <i>doing</i>, not how you are feeling about being criticised.</p>",src:"COHASSET Original - Crisis comms briefing",qs:[
            {q:"How quickly should the first statement come?",o:["10 minutes","60 minutes","6 hours","24 hours"],a:1},
            {q:"What should you NOT do?",o:["Apologise","Correct facts","Delete posts","Investigate"],a:2},
            {q:"What beats volume?",o:["Speed","Empathy","Consistency","Lawyers"],a:2}
        ]}},
        {type:"dd",tl:"Drag & Drop",title:"Order of Crisis Actions",ins:"Put these crisis steps in order.",content:{ws:["Activate the crisis team","Issue a holding statement","Brief all spokespeople with key messages","Engage with affected stakeholders directly","Conduct post-mortem and update playbook"],ss:[
            {t:"1. ___",b:"Activate the crisis team"},
            {t:"2. ___",b:"Issue a holding statement"},
            {t:"3. ___",b:"Brief all spokespeople with key messages"},
            {t:"4. ___",b:"Engage with affected stakeholders directly"},
            {t:"5. ___",b:"Conduct post-mortem and update playbook"}
        ]}},
        {type:"fl",tl:"Open Cloze",cb:"BEC Higher",title:"Crisis Holding Statement",ins:"One word per gap.",content:{ss:[
            {t:"We are deeply ___ by the events reported this morning.",a:"concerned"},
            {t:"Our priority ___ the safety of our customers and staff.",a:"is"},
            {t:"A full investigation is ___ underway.",a:"already"},
            {t:"We will ___ further information as soon as it is verified.",a:"share"},
            {t:"We ___ for the inconvenience this has caused.",a:"apologise"}
        ]}},
        {type:"wr",tl:"Writing",title:"Holding Statement",ins:"Cohasset Logistics has a public data breach. Write the company's first holding statement (180-220 words) for the press and customers.",content:{prompt:"FOR IMMEDIATE RELEASE\nCohasset Logistics - Statement on data security incident\n",tips:"Include: acknowledgment, empathy, what is known, what is unknown, immediate steps taken, contact channel, next update time. Avoid speculation.",minWords:160}}
    ]},
    // ---------- B2-18 ----------
    {id:"be-b2-18",title:"Unit 18: Performance Reviews",subtitle:"Give and receive feedback that drives growth",exercises:[
        {type:"vc",tl:"Vocabulary",cb:"BEC Higher",title:"Performance Review Vocabulary",ins:"Learn these terms.",content:{words:[
            {w:"to set objectives",ipa:"/tɪ sɛt əˈbʤɛktɪvz/",d:"to define measurable goals"},
            {w:"SMART goals",ipa:"/smɑrt goʊlz/",d:"Specific, Measurable, Achievable, Relevant, Time-bound"},
            {w:"360-degree feedback",ipa:"/360-degree ˈfidˌbæk/",d:"feedback from manager, peers, reports"},
            {w:"strengths and development areas",ipa:"/strɛŋθs ənd dɪˈvɛləpmənt ˈɛriəz/",d:"polite name for pros and cons"},
            {w:"to calibrate",ipa:"/tɪ ˈkæləˌbreɪt/",d:"to align ratings across managers"},
            {w:"performance improvement plan (PIP)",ipa:"/pərˈfɔrməns ˌɪmˈpruvmənt plæn (pɪp)/",d:"formal plan when performance is below standard"},
            {w:"recognition",ipa:"/ˌrɛkɪgˈnɪʃən/",d:"appreciation for good work"},
            {w:"actionable feedback",ipa:"/ˈækʃənəbəl ˈfidˌbæk/",d:"feedback the person can do something about"}
        ]}},
        {type:"ls",tl:"Listening",cb:"BEC Higher",title:"Audio: A Mid-Year Review Conversation",ins:"Listen to a manager and direct report.",content:{tts:"Manager: Thanks for joining, Andrea. Before we go through ratings, how are you finding the role overall? Andrea: Honestly, the first half was intense. The new system migration consumed most of my time, but I learned a lot. Manager: Agreed - and your work on the migration is one of the strongest things you have done this year. Stakeholders described you as calm under pressure. So that's the good news. The development area is presentation skills. In two recent leadership meetings, your slides were dense and you spoke quickly. The content was strong; the delivery undersold it. Andrea: I noticed that too. I'd like to take a course - something practical, not just theory. Manager: Good. Let's add 'complete a presentation skills course by Q3' as a development goal, and I'll find you two coaching sessions internally. We'll revisit in our next one-to-one. Andrea: That sounds fair, thank you. Manager: Thank you for being so open.",qs:[
            {q:"What was Andrea's main strength?",o:["Coding","Migration leadership","Sales","Recruiting"],a:1},
            {q:"What is the development area?",o:["Time management","Presentation skills","Coding","Negotiation"],a:1},
            {q:"What action is agreed?",o:["Promotion","Course + coaching","Salary review","Transfer"],a:1}
        ]}},
        {type:"mt",tl:"Matching",title:"Feedback Models",ins:"Match each model with its short description.",content:{l:["SBI","STAR","Radical Candor","Feedforward","SMART"],r:["Caring personally + challenging directly","Goals: Specific, Measurable, etc.","Situation, Behaviour, Impact","Future-focused suggestions only","Past-event description in interview"],ans:{0:2,1:4,2:0,3:3,4:1}}},
        {type:"kt",tl:"Key Word Transformation",cb:"BEC Higher",title:"Tactful Feedback Phrasing",ins:"Rewrite using the keyword.",content:{ss:[
            {t:"You always interrupt people in meetings.",k:"NOTICED",a:"I have noticed you sometimes interrupt people in meetings."},
            {t:"Your report was bad.",k:"AREAS",a:"There were a few areas in your report we could improve."},
            {t:"You should improve immediately.",k:"WOULD",a:"It would help if you improved this in the next month."},
            {t:"You did a great job.",k:"CONTRIBUTION",a:"Your contribution this quarter has been outstanding."}
        ]}},
        {type:"wr",tl:"Writing",title:"Year-End Review Comments",ins:"Write a 180-220-word year-end review for a fictional team member: 1 strength, 1 development area, 2 SMART goals.",content:{prompt:"YEAR-END PERFORMANCE REVIEW\nEmployee:\nReviewer:\nPeriod:\n\n1. Overall summary\n2. Strengths\n3. Development areas\n4. SMART goals for next year\n",tips:"Use SBI for examples. Keep tone respectful and specific. Avoid vague adjectives like 'good' or 'bad'.",minWords:160}}
    ]},
    // ---------- B2-19 ----------
    {id:"be-b2-19",title:"Unit 19: International Contracts & Clauses",subtitle:"Read and understand standard contract clauses",exercises:[
        {type:"vc",tl:"Vocabulary",cb:"BEC Higher",title:"Contract Clauses",ins:"Learn the most common clauses.",content:{words:[
            {w:"force majeure",ipa:"/fɔrs məˈʤur/",d:"events beyond reasonable control (war, pandemic)"},
            {w:"governing law",ipa:"/ˈgəvərnɪŋ lɔ/",d:"the country's laws that apply"},
            {w:"jurisdiction",ipa:"/ˌʤʊrɪsˈdɪkʃən/",d:"the courts that have authority"},
            {w:"indemnity",ipa:"/ˌɪnˈdɛmnɪti/",d:"protection against losses caused by the other party"},
            {w:"liability cap",ipa:"/ˌlaɪəˈbɪlɪti kæp/",d:"the maximum amount one party can be held responsible for"},
            {w:"termination for convenience",ipa:"/tərməˈneɪʃən fər kənˈvinjəns/",d:"ending the contract without specific cause"},
            {w:"confidentiality / NDA",ipa:"/ˌkɑnfəˌdɛnʃiˈæləti  nda/",d:"obligation to keep information secret"},
            {w:"warranty",ipa:"/ˈwɔrənti/",d:"a promise about the quality or condition"}
        ]}},
        {type:"rd",tl:"Reading",cb:"BEC Higher",title:"The Contract You Don't Read",ins:"Read the article.",content:{p:"<p>In international procurement, the average commercial contract is read carefully by lawyers and signed by managers who skim it. Yet five clauses recur in almost every dispute. The <b>governing law and jurisdiction</b> clause decides not only which laws apply but, often more importantly, which courts you must travel to. A favourable price loses value if disputes must be heard in a distant jurisdiction.</p><p>The <b>liability cap</b>, often equal to fees paid in the previous twelve months, can leave the buyer dramatically under-protected if the supplier's failure causes downstream damage. <b>Force majeure</b> clauses now routinely include pandemics and cyber-attacks; older templates may not. <b>Indemnities</b> should be mutual where reasonable, and <b>termination for convenience</b> with appropriate notice protects against vendor lock-in.</p><p>Smart procurement teams negotiate from a deal-breaker / nice-to-have hierarchy, focus their energy on these five clauses, and accept boilerplate elsewhere. The contract that nobody reads is the one that ends up in litigation.</p>",src:"COHASSET Original - inspired by HBR contract reviews",qs:[
            {q:"What does the liability cap often equal?",o:["Last 12 months' fees","Total project value","Insurance limit","Stock price"],a:0},
            {q:"What protects against vendor lock-in?",o:["Force majeure","Termination for convenience","Indemnity","NDA"],a:1},
            {q:"How many clauses recur in disputes?",o:["3","4","5","7"],a:2}
        ]}},
        {type:"mt",tl:"Matching",title:"Clause to Risk",ins:"Match each clause with the risk it manages.",content:{l:["Force majeure","Governing law","Liability cap","NDA","Warranty"],r:["Quality of goods/services","Limit on financial exposure","Information leakage","Unforeseeable events","Which courts apply"],ans:{0:3,1:4,2:1,3:2,4:0}}},
        {type:"fl",tl:"Open Cloze",cb:"BEC Higher",title:"Contract Drafting",ins:"One word per gap.",content:{ss:[
            {t:"This Agreement shall be ___ by the laws of Peru.",a:"governed"},
            {t:"Either party may ___ the contract with 30 days' notice.",a:"terminate"},
            {t:"The Supplier shall not be liable for delays caused by ___ majeure.",a:"force"},
            {t:"Total liability shall not ___ the fees paid in the last 12 months.",a:"exceed"},
            {t:"Each party agrees to keep all confidential information ___ secret.",a:"strictly"}
        ]}},
        {type:"wr",tl:"Writing",title:"Contract Negotiation Email",ins:"Write a 180-220-word email to a supplier requesting changes to three clauses (liability cap, governing law, force majeure).",content:{prompt:"Subject: Comments on draft Master Services Agreement\n\nDear [counsel/counterparty],\n",tips:"Use polite firm language. Justify each change briefly. Suggest alternative wording. End with willingness to discuss on a call.",minWords:160}}
    ]},
    // ---------- B2-20 CAPSTONE ----------
    {id:"be-b2-20",title:"Unit 20: Capstone - Pitch Deck Presentation Script",subtitle:"Write a script for a 10-slide investor pitch",exercises:[
        {type:"rd",tl:"Reading",cb:"BEC Higher",title:"The 10-Slide Standard",ins:"Read the briefing and answer.",content:{p:"<p>Most early-stage pitches now follow Guy Kawasaki's 10-slide standard, expanded for modern investor expectations. The slides typically cover: <b>1. Title and one-line vision</b>; <b>2. Problem</b> with a concrete customer story; <b>3. Solution</b> with a single product image; <b>4. Market size</b> using TAM/SAM/SOM; <b>5. Business model</b> and unit economics; <b>6. Traction</b> showing real metrics; <b>7. Competition</b> with a positioning matrix; <b>8. Team</b> emphasising relevant scars; <b>9. Financial projections</b> for 3 years; <b>10. Ask</b> with use of funds.</p><p>The script - what the founder actually says - matters more than the visuals. Investors decide in 7-10 minutes. Strong scripts open with a sharp story, name the problem, and earn the right to talk about solution. They use specific numbers, avoid jargon, and finish with a memorable closing line. Prepared founders rehearse the script aloud at least twenty times before pitch day.</p>",src:"COHASSET Original - based on Kawasaki/Sequoia",qs:[
            {q:"How many slides standard?",o:["8","10","12","15"],a:1},
            {q:"Slide 4 covers:",o:["Team","Market size","Solution","Ask"],a:1},
            {q:"Recommended rehearsals?",o:["5","10","20","50"],a:2}
        ]}},
        {type:"mt",tl:"Matching",title:"Slide to Content",ins:"Match each slide number with its main content.",content:{l:["Slide 2","Slide 5","Slide 6","Slide 8","Slide 10"],r:["Use of funds and ask","Team and relevant experience","Business model","Traction metrics","Problem with customer story"],ans:{0:4,1:2,2:3,3:1,4:0}}},
        {type:"kt",tl:"Key Word Transformation",cb:"BEC Higher",title:"Pitch Language",ins:"Rewrite using the keyword.",content:{ss:[
            {t:"Our market is very large.",k:"REPRESENTS",a:"This represents a sizeable market opportunity."},
            {t:"We grew quickly last year.",k:"EXPANDED",a:"We expanded rapidly over the past year."},
            {t:"We need money to grow.",k:"FUNDING",a:"We are seeking funding to accelerate growth."},
            {t:"Our team is great.",k:"COMBINES",a:"Our team combines deep technical and commercial expertise."}
        ]}},
        {type:"wr",tl:"Writing",title:"Capstone: 10-Slide Pitch Script",ins:"Write the spoken script for a 7-minute pitch of a fictional Cohasset startup. Include all 10 slide notes. (200-240 words)",content:{prompt:"PITCH SCRIPT - [Startup Name]\nFounder: [Name]\nPitch length: 7 minutes\n\nSlide 1: Title\nSlide 2: Problem\nSlide 3: Solution\nSlide 4: Market\nSlide 5: Business model\nSlide 6: Traction\nSlide 7: Competition\nSlide 8: Team\nSlide 9: Financials\nSlide 10: Ask\n",tips:"~20 spoken words per slide. Open with a story. Close with a clear ask amount and use of funds.",minWords:180}}
    ]}
],

// ========== C1 EXTENSION ==========
c1: [
    // ---------- C1-16 ----------
    {id:"be-c1-16",title:"Unit 16: Boardroom Dynamics & Chairing Meetings",subtitle:"Lead a boardroom debate with authority and balance",exercises:[
        {type:"vc",tl:"Vocabulary",cb:"CAE",title:"Boardroom Vocabulary",ins:"Learn this senior-level terminology.",content:{words:[
            {w:"to call the meeting to order",ipa:"/tɪ kɔl ðə ˈmitɪŋ tɪ ˈɔrdər/",d:"to formally start"},
            {w:"to table a motion",ipa:"/tɪ ˈteɪbəl ə ˈmoʊʃən/",d:"to propose a formal decision"},
            {w:"a quorum",ipa:"/ə kˈwɔrəm/",d:"the minimum number of members for a valid vote"},
            {w:"abstention",ipa:"/əbˈstɛnʧən/",d:"choosing neither yes nor no"},
            {w:"executive session",ipa:"/ɪgˈzɛkjətɪv ˈsɛʃən/",d:"closed portion without management"},
            {w:"in camera",ipa:"/ɪn ˈkæmərə/",d:"private and confidential"},
            {w:"casting vote",ipa:"/ˈkæstɪŋ voʊt/",d:"the chair's tie-breaking vote"},
            {w:"minutes",ipa:"/ˈmɪnəts/",d:"the formal written record of the meeting"}
        ]}},
        {type:"rd",tl:"Reading",cb:"CAE",title:"Chairing Without Dominating",ins:"Read this governance article.",content:{p:"<p>The most effective board chairs share a paradox: they are highly authoritative yet deliberately self-effacing. They open debate with crisp framing, but speak relatively little themselves. Research from INSEAD's corporate governance centre suggests that strong chairs spend roughly 70% of meeting time listening, 20% structuring debate, and only 10% expressing personal views.</p><p>Their tools are subtle. They draw out quieter members by name (\"Elena, you've worked closely with this regulator - what's your read?\"); they reframe heat as substance (\"Let me capture the underlying concern\"); and they impose discipline by recapping decisions, owners and deadlines before moving on. When dissent emerges, the strong chair welcomes it explicitly: \"This is exactly the discussion the board exists to have.\"</p><p>Above all, they refuse to push for premature consensus. A board that votes 9-0 every time is rarely doing its job. The chair's deepest responsibility is to ensure that disagreement is heard, examined and resolved on the merits, before, not after, the decision is taken.</p>",src:"COHASSET Original - INSEAD-style synthesis",qs:[
            {q:"How much do strong chairs listen?",o:["50%","60%","70%","80%"],a:2},
            {q:"What is the chair's deepest duty?",o:["Speak first","Push consensus","Surface and resolve dissent","Vote often"],a:2},
            {q:"How do they draw out quiet members?",o:["By voting","By naming them","By emails","By rotating chairs"],a:1}
        ]}},
        {type:"mt",tl:"Matching",title:"Chair Phrase to Function",ins:"Match each phrase with its tactical purpose.",content:{l:["Let me capture the underlying concern.","Elena, what's your read on this?","Just so we're clear, the decision is...","I'd like to invite a dissenting view.","We don't yet have a quorum on item three."],r:["Reframing tension as substance","Recapping a decision","Procedural control","Drawing out a member by name","Inviting principled disagreement"],ans:{0:0,1:3,2:1,3:4,4:2}}},
        {type:"kt",tl:"Key Word Transformation",cb:"CAE",title:"Boardroom Register",ins:"Rewrite at boardroom register using the keyword.",content:{ss:[
            {t:"I think we should look at this again.",k:"REVISIT",a:"I'd suggest we revisit this."},
            {t:"This idea is bad and I disagree.",k:"RESERVATIONS",a:"I have significant reservations about this proposal."},
            {t:"Let's wait, we don't have enough info.",k:"DEFER",a:"I'd recommend we defer the decision pending further information."},
            {t:"Are we all OK with this?",k:"COMFORT",a:"Are we all comfortable proceeding on this basis?"}
        ]}},
        {type:"wr",tl:"Writing",title:"Board Meeting Minutes Excerpt",ins:"Write a 240-260-word excerpt of board minutes for a discussion about a major capex approval.",content:{prompt:"BOARD MINUTES - EXTRACT\nMeeting:\nDate:\nPresent:\nAgenda Item: Approval of $40M capex for new Lima distribution centre\n",tips:"Standard structure: Discussion / Resolution / Decision / Owner / Date. Capture dissenting views. Use third person past tense, formal register.",minWords:220}}
    ]},
    // ---------- C1-17 ----------
    {id:"be-c1-17",title:"Unit 17: Investor Relations & Earnings Calls",subtitle:"Speak to analysts during quarterly results",exercises:[
        {type:"vc",tl:"Vocabulary",cb:"CAE",title:"Investor Relations Vocabulary",ins:"Master these IR terms.",content:{words:[
            {w:"guidance",ipa:"/ˈgaɪdəns/",d:"forward-looking estimates given to the market"},
            {w:"consensus estimate",ipa:"/kənˈsɛnsəs ˈɛstəˌmeɪt/",d:"average of analysts' forecasts"},
            {w:"to beat / miss / meet",ipa:"/tɪ bit  mɪs  mit/",d:"vs. consensus"},
            {w:"non-GAAP measures",ipa:"/non-gaap ˈmɛʒərz/",d:"adjusted figures excluding one-offs"},
            {w:"forward-looking statement",ipa:"/forward-looking ˈsteɪtmənt/",d:"projection covered by safe-harbour disclaimer"},
            {w:"buyback / repurchase",ipa:"/ˈbaɪˌbæk  riˈpərʧəs/",d:"company buying back its shares"},
            {w:"dilution",ipa:"/dɪˈluʃən/",d:"reduction of EPS from new share issuance"},
            {w:"sell-side / buy-side analysts",ipa:"/sell-side  buy-side ˈænəlɪsts/",d:"work for brokers / fund managers"}
        ]}},
        {type:"ls",tl:"Listening",cb:"CAE",title:"Audio: Q3 Earnings Call - CFO Remarks",ins:"Listen to a CFO opening an earnings call.",content:{tts:"Operator: Welcome to Cohasset Holdings' third-quarter earnings call. Please welcome Chief Financial Officer Helena Vargas. Helena: Thank you, and good morning, everyone. We delivered a solid third quarter, with revenue of 412 million dollars, up nine percent year-on-year, modestly ahead of consensus. Adjusted EBITDA reached 88 million, expanding our margin by 110 basis points to 21.4 percent. Free cash flow was 72 million. On capital allocation, we returned 28 million to shareholders this quarter through buybacks. Looking forward, we are reiterating full-year revenue guidance of 1.65 to 1.70 billion dollars and raising our adjusted EBITDA guidance by approximately 5 million at the midpoint, reflecting continued operational discipline. Headwinds remain - notably FX exposure in our Andean segment and softer demand in commercial logistics - but our pricing actions and mix improvements are offsetting them. With that, I'll hand it back for the Q&A. Operator?",qs:[
            {q:"Revenue growth this quarter?",o:["5%","7%","9%","11%"],a:2},
            {q:"What did the company do with EBITDA guidance?",o:["Cut","Reiterate","Raise","Suspend"],a:2},
            {q:"What is mentioned as a headwind?",o:["FX in Andean segment","Higher costs","New regulation","Cyber attack"],a:0}
        ]}},
        {type:"mt",tl:"Matching",title:"IR Question to Function",ins:"Match each analyst question with its purpose.",content:{l:["Can you walk us through the bridge?","What's the cadence of buybacks for Q4?","How comfortable are you with the high end of guidance?","Any change to the FX hedging policy?","How do you think about long-term margin trajectory?"],r:["Strategic margin outlook","Guidance confidence","Hedging policy","Decomposition of variance","Capital return cadence"],ans:{0:3,1:4,2:1,3:2,4:0}}},
        {type:"fl",tl:"Open Cloze",cb:"CAE",title:"IR Disclaimer Language",ins:"One word per gap.",content:{ss:[
            {t:"This call ___ forward-looking statements within the meaning of securities law.",a:"contains"},
            {t:"Actual results may ___ materially from these projections.",a:"differ"},
            {t:"We ___ no obligation to update forward-looking statements.",a:"undertake"},
            {t:"Reconciliation of non-GAAP measures is included in the appendix to today's ___.",a:"presentation"},
            {t:"Investors should ___ caution and consult our risk factors.",a:"exercise"}
        ]}},
        {type:"wr",tl:"Writing",title:"CFO Earnings-Call Script",ins:"Write a 220-260-word script for the CFO's opening remarks at a quarterly earnings call.",content:{prompt:"CFO OPENING REMARKS - Q4 EARNINGS CALL\nCohasset Holdings\n",tips:"Structure: 1) Headline numbers 2) Variance vs guidance 3) Key drivers 4) Capital allocation 5) Updated guidance 6) Hand-off to Q&A. Hedge appropriately on forward-looking statements.",minWords:200}}
    ]},
    // ---------- C1-18 ----------
    {id:"be-c1-18",title:"Unit 18: M&A Communication",subtitle:"Announce mergers and manage integration messaging",exercises:[
        {type:"vc",tl:"Vocabulary",cb:"CAE",title:"M&A Terminology",ins:"Master these deal terms.",content:{words:[
            {w:"acquirer / target",ipa:"/əkˈwaɪərər  ˈtərgət/",d:"buyer / company being bought"},
            {w:"due diligence",ipa:"/du ˈdɪlɪʤəns/",d:"detailed pre-deal investigation"},
            {w:"synergies",ipa:"/ˈsɪnərʤiz/",d:"cost savings or revenue benefits from combining"},
            {w:"earn-out",ipa:"/earn-out/",d:"deferred payment tied to performance"},
            {w:"day one",ipa:"/deɪ wən/",d:"the first day after deal closes"},
            {w:"integration office",ipa:"/ˌɪnəˈgreɪʃən ˈɔfəs/",d:"team that runs post-merger integration"},
            {w:"retention bonus",ipa:"/riˈtɛnʃən ˈboʊnəs/",d:"cash incentive to keep key staff"},
            {w:"cultural alignment",ipa:"/ˈkəlʧərəl əˈlaɪnmənt/",d:"compatibility of working norms"}
        ]}},
        {type:"rd",tl:"Reading",cb:"CAE",title:"The 100-Day Plan",ins:"Read this M&A briefing.",content:{p:"<p>Most merger value is destroyed not at signing but in the months that follow. McKinsey's data suggests roughly 70% of acquisitions fail to deliver projected synergies, with cultural mismatch and communication failures cited more frequently than financial miscalculation.</p><p>Mature acquirers therefore design the integration before they design the deal. A standing <b>integration management office</b> begins working in parallel with due diligence; a 100-day plan with named owners and weekly milestones is in place before announcement. Communication follows a deliberate cascade: regulators and key customers within hours, all employees within 24 hours, and the media on the same news cycle.</p><p>Crucially, leaders communicate even when there is little to say. The greatest enemy of integration is rumour. Where decisions are not yet taken, leaders say so explicitly and commit to a date. Retention of key talent often depends less on financial bonuses than on whether senior leaders remembered to call within 48 hours of the announcement.</p>",src:"COHASSET Original - inspired by McKinsey M&A practice",qs:[
            {q:"What % of M&A deals fail to deliver synergies?",o:["50%","60%","70%","80%"],a:2},
            {q:"When are employees informed?",o:["Same hour","Within 24 hours","One week","One month"],a:1},
            {q:"Talent retention often depends most on?",o:["Bonuses","Stock","Personal calls from leaders","Office location"],a:2}
        ]}},
        {type:"mt",tl:"Matching",title:"Stakeholder to Message Priority",ins:"Match each stakeholder with the message focus they need first.",content:{l:["Employees","Customers","Regulators","Investors","Media"],r:["Continuity of service and points of contact","Strategic rationale and synergies","Compliance with antitrust filings","Job security, integration timeline, leadership","Headline narrative, exclusive sound bites"],ans:{0:3,1:0,2:2,3:1,4:4}}},
        {type:"kt",tl:"Key Word Transformation",cb:"CAE",title:"M&A Register",ins:"Rewrite using the keyword.",content:{ss:[
            {t:"We will save money by combining.",k:"SYNERGIES",a:"We expect to realise synergies from the combination."},
            {t:"This is good for both companies.",k:"COMPLEMENTARY",a:"The two businesses are highly complementary."},
            {t:"There may be job losses.",k:"REDUCTIONS",a:"There will be selective role reductions."},
            {t:"We don't know about everything yet.",k:"DECISIONS",a:"Some decisions remain to be taken."}
        ]}},
        {type:"wr",tl:"Writing",title:"Merger Announcement Email",ins:"Write a 220-260-word announcement email from the CEO of Cohasset Holdings to all employees about an acquisition.",content:{prompt:"To: All Cohasset Holdings employees\nFrom: CEO\nSubject: Acquisition of Apex Logistics - what this means for us\n",tips:"Cover: rationale, financial scope, what is changing day one, what is not changing, town hall date, contact channel for questions, sincere appreciation.",minWords:200}}
    ]},
    // ---------- C1-19 ----------
    {id:"be-c1-19",title:"Unit 19: ESG & Sustainability Reporting",subtitle:"Communicate environmental, social and governance progress",exercises:[
        {type:"vc",tl:"Vocabulary",cb:"CAE",title:"ESG Vocabulary",ins:"Master modern ESG terminology.",content:{words:[
            {w:"materiality assessment",ipa:"/məˌtɪriˈælɪti əˈsɛsmənt/",d:"identifying which ESG issues most affect the business"},
            {w:"Scope 1, 2, 3 emissions",ipa:"/skoʊp 1 2 3 ɪˈmɪʃənz/",d:"direct, indirect-energy, value-chain emissions"},
            {w:"net zero",ipa:"/nɛt ˈziroʊ/",d:"balancing emissions and removals to zero"},
            {w:"greenwashing",ipa:"/greenwashing/",d:"misleading claims about environmental performance"},
            {w:"double materiality",ipa:"/ˈdəbəl məˌtɪriˈælɪti/",d:"financial impact + impact on society/environment"},
            {w:"TCFD / ISSB / CSRD",ipa:"/tcfd  issb  csrd/",d:"climate disclosure frameworks"},
            {w:"science-based target",ipa:"/science-based ˈtərgət/",d:"reduction target validated by SBTi"},
            {w:"just transition",ipa:"/ʤɪst trænˈzɪʃən/",d:"climate action that is socially fair"}
        ]}},
        {type:"rd",tl:"Reading",cb:"CAE",title:"From Slogan to Standard",ins:"Read this disclosure article.",content:{p:"<p>For two decades, sustainability reporting was largely voluntary, narrative-heavy and difficult to compare. The arrival of CSRD in Europe and ISSB-aligned standards globally is reshaping the discipline into something closer to financial reporting: assured, audited, and increasingly comparable.</p><p>The discipline now demands two distinct lenses. <b>Single materiality</b>, traditional in financial reporting, asks how environmental and social issues affect company value. <b>Double materiality</b>, codified in CSRD, additionally requires disclosure of how the company affects environment and society - whether or not it changes shareholder returns. Companies that resist double materiality risk being mis-aligned with the regulatory direction of travel.</p><p>The strategic challenge is no longer whether to report, but how to communicate genuine progress without crossing into greenwashing territory. Regulators in the EU, UK, US and Australia are actively prosecuting misleading sustainability claims. Robust ESG reports now feature science-based targets, third-party assurance, and willingness to disclose where the company is missing its own goals. Authenticity, increasingly, is auditable.</p>",src:"COHASSET Original - based on CSRD/ISSB",qs:[
            {q:"What does double materiality add?",o:["Tax data","Impact on society/env","Marketing","Cybersecurity"],a:1},
            {q:"What are regulators prosecuting?",o:["Targets","Greenwashing","Charity","Lobbying"],a:1},
            {q:"What strengthens authenticity?",o:["Slogans","More photos","Third-party assurance","Press releases"],a:2}
        ]}},
        {type:"mt",tl:"Matching",title:"Framework to Focus",ins:"Match each framework with its focus.",content:{l:["TCFD","ISSB","CSRD","SBTi","GRI"],r:["Broad multi-stakeholder reporting","Science-based emissions targets","Investor-focused sustainability standards","EU mandatory double-materiality reporting","Climate-related financial disclosures"],ans:{0:4,1:2,2:3,3:1,4:0}}},
        {type:"fl",tl:"Open Cloze",cb:"CAE",title:"ESG Disclosure Drafting",ins:"One word per gap.",content:{ss:[
            {t:"We have ___ a 50% reduction in Scope 1 and 2 emissions by 2030.",a:"committed"},
            {t:"Our materiality assessment was ___ in 2024 with multi-stakeholder input.",a:"updated"},
            {t:"We acknowledge we are ___ short of our diversity target this year.",a:"falling"},
            {t:"All disclosures are subject to ___-party assurance by an independent auditor.",a:"third"},
            {t:"We continue to ___ progress quarterly to our Sustainability Committee.",a:"report"}
        ]}},
        {type:"wr",tl:"Writing",title:"Sustainability Report Section",ins:"Write a 220-260-word 'Climate' section of an annual sustainability report - including a target missed.",content:{prompt:"COHASSET HOLDINGS - SUSTAINABILITY REPORT 2026\nSection: Climate\n",tips:"Include: targets, progress, methodology, where you missed and why, next-year actions, governance. Avoid superlatives. Use specific numbers.",minWords:200}}
    ]},
    // ---------- C1-20 CAPSTONE ----------
    {id:"be-c1-20",title:"Unit 20: Capstone - Strategic Plan Executive Summary",subtitle:"Compress a multi-year strategy into one executive page",exercises:[
        {type:"rd",tl:"Reading",cb:"CAE",title:"What Boards Read First (and Sometimes Only)",ins:"Read and answer.",content:{p:"<p>Even on the most engaged boards, the executive summary is the only page some directors will read carefully. Yet too many summaries are written last, in haste, by the same people who drafted the strategy - and reproduce its complexity rather than distilling it.</p><p>The discipline is severe. A senior strategy adviser at Bain has argued that a strong summary answers five questions in less than 400 words: <i>Where will we play, how will we win, what must change, what will it cost, and what can go wrong?</i> Each must be quantified. \"Grow internationally\" is not a strategy; \"Reach $250M revenue in three Andean markets by 2028, funded by a $40M capex programme\" is.</p><p>Strong summaries also state explicitly what the strategy is <i>not</i>. By naming abandoned options, leaders prove the choice was real. They acknowledge headline risks rather than burying them. The literary discipline of the summary is also strategic discipline: a strategy that cannot be summarised in a page is usually one that has not yet been chosen.</p>",src:"COHASSET Original - based on Bain/HBR",qs:[
            {q:"Five questions in how many words?",o:["200","300","400","600"],a:2},
            {q:"What must summaries also state?",o:["The CEO's biography","What the strategy is not","Hours of work","Page count"],a:1},
            {q:"What is 'real' choice proof?",o:["Photos","Naming abandoned options","Long appendix","Many slides"],a:1}
        ]}},
        {type:"mt",tl:"Matching",title:"Five Strategy Questions",ins:"Match each question with the typical content.",content:{l:["Where will we play?","How will we win?","What must change?","What will it cost?","What can go wrong?"],r:["Capabilities, org, capex","Markets, segments, geographies","Differentiated value proposition","Risks and mitigations","3-yr financial projections"],ans:{0:1,1:2,2:0,3:4,4:3}}},
        {type:"kt",tl:"Key Word Transformation",cb:"CAE",title:"Strategic Register",ins:"Rewrite using the keyword.",content:{ss:[
            {t:"We will focus on three new markets.",k:"PRIORITISE",a:"We will prioritise three new markets."},
            {t:"This will cost a lot of money.",k:"INVESTMENT",a:"This will require a substantial capital investment."},
            {t:"We could fail because of competitors.",k:"COMPETITIVE",a:"The principal risk lies in competitive response."},
            {t:"We are not going to do retail anymore.",k:"EXIT",a:"We will exit the retail segment."}
        ]}},
        {type:"wr",tl:"Writing",title:"Capstone: Executive Summary",ins:"Write a 240-280-word executive summary of a 3-year strategic plan for Cohasset Holdings. Cover all five questions.",content:{prompt:"STRATEGIC PLAN 2027-2029 - EXECUTIVE SUMMARY\nCohasset Holdings\nFor: Board of Directors\n",tips:"Structure (one paragraph each): Where we'll play / How we'll win / What must change / What it will cost / What can go wrong. Quantify each. Name what you will NOT do.",minWords:220}}
    ]}
],

// ========== C2 EXTENSION ==========
c2: [
    // ---------- C2-16 ----------
    {id:"be-c2-16",title:"Unit 16: Geopolitical Risk Briefings",subtitle:"Brief boards on geopolitical exposure with rigour",exercises:[
        {type:"vc",tl:"Vocabulary",cb:"CPE",title:"Geopolitical Lexicon",ins:"Master sophisticated geopolitical terminology.",content:{words:[
            {w:"sovereign risk",ipa:"/ˈsɑvrən rɪsk/",d:"risk that a government will default or change rules"},
            {w:"sanctions regime",ipa:"/ˈsæŋkʃənz rəˈʒim/",d:"coordinated trade or financial restrictions"},
            {w:"secondary sanctions",ipa:"/ˈsɛkənˌdɛri ˈsæŋkʃənz/",d:"penalising third-country actors"},
            {w:"derisking vs decoupling",ipa:"/derisking ˈvərsəz diˈkəplɪŋ/",d:"selective vs comprehensive disengagement"},
            {w:"strategic ambiguity",ipa:"/strəˈtiʤɪk ˌæmbɪˈgjuəti/",d:"deliberately undefined commitments"},
            {w:"chokepoint",ipa:"/chokepoint/",d:"a critical bottleneck (e.g. Strait of Hormuz)"},
            {w:"export controls",ipa:"/ˈɛkspɔrt kənˈtroʊlz/",d:"restrictions on dual-use technology"},
            {w:"economic statecraft",ipa:"/ˌɛkəˈnɑmɪk ˈsteɪtˌkræft/",d:"using economic tools for political ends"}
        ]}},
        {type:"rd",tl:"Reading",cb:"CPE",title:"From Globalisation to Fragmentation",ins:"Read this elite-register analysis.",content:{p:"<p>The post-1989 assumption that capital, goods and ideas would flow ever more freely has been quietly abandoned in most boardrooms. What has replaced it is not its opposite, but a more textured architecture: regional blocs anchored by deep trust, transactional ties to neutrals, and managed friction with strategic rivals.</p><p>For multinationals headquartered in middle-power economies, the implications are profound. Whereas Cold War-era 'non-alignment' could be a stable equilibrium, today's environment increasingly demands operational redundancy: parallel supply chains, jurisdictionally diversified data architectures, and contractual provisions anticipating sanctions snapbacks. The marginal cost of resilience has been priced in by markets; the marginal cost of brittleness now exceeds it.</p><p>The most rigorous boards have ceased treating geopolitics as a separate enterprise risk and begun integrating it into capital allocation itself. A new copper smelter, a regional cloud, a long-term offtake - each is now scrutinised through scenarios spanning 5-10 years and 3-5 plausible global orders. Optionality, once a luxury, has become structural.</p>",src:"COHASSET Original - inspired by Foreign Affairs/CFR",qs:[
            {q:"What replaced full globalisation?",o:["Autarky","Regional blocs + managed friction","Cold War","UN governance"],a:1},
            {q:"What has now been priced in?",o:["Marginal cost of resilience","Marginal cost of profit","Currency","Inflation"],a:0},
            {q:"What's now structural?",o:["Aggression","Optionality","Speed","Lobbying"],a:1}
        ]}},
        {type:"mt",tl:"Matching",title:"Mitigation Strategy to Risk",ins:"Match each strategy with its primary geopolitical risk.",content:{l:["Parallel supply chain","Jurisdictionally diverse data architecture","FX hedging across baskets","Sanctions snapback clauses","Local-content joint ventures"],r:["Currency volatility","Sudden re-imposition of sanctions","Single-source disruption","Market-access denial","Cross-border data restrictions"],ans:{0:2,1:4,2:0,3:1,4:3}}},
        {type:"kt",tl:"Key Word Transformation",cb:"CPE",title:"Elevated Hedging",ins:"Rewrite at C2 register using the keyword.",content:{ss:[
            {t:"This will probably happen in 2027.",k:"MATERIALISE",a:"This is likely to materialise in 2027."},
            {t:"We don't really know how China will respond.",k:"VISIBILITY",a:"We have limited visibility on the Chinese response."},
            {t:"We need to be ready for many possibilities.",k:"SCENARIOS",a:"We must remain prepared across a range of plausible scenarios."},
            {t:"This issue is very serious.",k:"GRAVITY",a:"The gravity of this issue cannot be overstated."}
        ]}},
        {type:"wr",tl:"Writing",title:"Geopolitical Briefing Note for the Board",ins:"Write a 280-320-word board briefing note on Cohasset Holdings' exposure to a regional geopolitical scenario. Use elite executive register.",content:{prompt:"CONFIDENTIAL - BOARD GEOPOLITICAL BRIEFING\nCohasset Holdings\nRe: Andean Regional Risk Outlook 2027-2029\nFor: Risk Committee\n",tips:"Sections: Executive judgement / Scenario set / Channel-specific exposure / Mitigation in motion / Decisions sought. Use hedged confidence. Quantify exposures.",minWords:260}}
    ]},
    // ---------- C2-17 ----------
    {id:"be-c2-17",title:"Unit 17: Speech Writing for Executives",subtitle:"Use rhetoric to make a CEO speech memorable",exercises:[
        {type:"vc",tl:"Vocabulary",cb:"CPE",title:"Rhetorical Devices",ins:"Master these classical rhetorical tools.",content:{words:[
            {w:"anaphora",ipa:"/əˈnæfərə/",d:"repetition at the start of successive clauses"},
            {w:"tricolon",ipa:"/tricolon/",d:"a series of three parallel elements"},
            {w:"antithesis",ipa:"/ænˈtɪθəsəs/",d:"contrasting ideas in parallel structure"},
            {w:"chiasmus",d:"reversal of grammatical order (\"ask not what...\")"},
            {w:"metaphor",ipa:"/ˈmɛtəfɔr/",d:"implicit comparison"},
            {w:"praeteritio",ipa:"/praeteritio/",d:"emphasising by saying you will not mention"},
            {w:"hypophora",ipa:"/hypophora/",d:"raising a question and answering it yourself"},
            {w:"epistrophe",ipa:"/epistrophe/",d:"repetition at the end of successive clauses"}
        ]}},
        {type:"rd",tl:"Reading",cb:"CPE",title:"Why Some CEO Speeches Outlive the Quarter",ins:"Read this advanced craft article.",content:{p:"<p>Most CEO speeches dissolve within minutes of delivery. The few that survive - Ken Chenault's post-9/11 remarks, Indra Nooyi's farewell, Jacinda Ardern's pandemic addresses - share recognisable craft. They are short. They surrender the temptation to recite achievements. They are organised around a single, durable image.</p><p>Such speeches typically deploy a small number of devices, deployed with restraint. <b>Anaphora</b> - the repetition of a phrase at the start of clauses - creates the cadence under which audiences retain meaning. <b>Antithesis</b> compresses moral choice into memorable form: \"We did not retreat; we reorganised.\" <b>Tricolon</b> rewards both ear and memory: \"Decision, conviction, action.\"</p><p>What distinguishes the truly great is asymmetry of attention: 80% of preparation is spent on the first sixty seconds and the closing minute. Middles can be honest; openings and closings must be surgical. The CEOs who write their own openings - and accept revisions to everything in between - are almost always the ones whose words travel beyond the room.</p>",src:"COHASSET Original - speechwriting craft",qs:[
            {q:"Where does 80% of preparation go?",o:["Middle","Slides","Opening 60s + closing minute","Logistics"],a:2},
            {q:"What is anaphora?",o:["Repetition at start","Reversal","Three items","Question"],a:0},
            {q:"What kills most CEO speeches?",o:["Length","Achievement-list dilution","No mic","No slides"],a:1}
        ]}},
        {type:"mt",tl:"Matching",title:"Device to Example",ins:"Match each device with its classic example.",content:{l:["Anaphora","Tricolon","Antithesis","Chiasmus","Hypophora"],r:["\"Ask not what your country can do for you...\"","\"What is our task? Our task is to rebuild trust.\"","\"We have nothing to fear but fear itself.\"","\"Government of the people, by the people, for the people.\"","\"Same time, same place, same purpose.\""],ans:{0:2,1:3,2:4,3:0,4:1}}},
        {type:"fl",tl:"Open Cloze",cb:"CPE",title:"Speechwriting Diction",ins:"One word per gap. Elite register.",content:{ss:[
            {t:"This evening, I want to ___ a single, simple proposition.",a:"advance"},
            {t:"For too long, we have ___ short-term comfort over long-term courage.",a:"chosen"},
            {t:"Tonight, I ask you to choose differently. To choose patience. To choose discipline. To choose ___.",a:"each"},
            {t:"What is the alternative? The alternative is a slow, ___ retreat.",a:"managed"},
            {t:"Let history record that we did not ___; we built.",a:"flinch"}
        ]}},
        {type:"wr",tl:"Writing",title:"CEO Speech",ins:"Write a 260-300-word CEO speech for an annual employee gathering. Deploy at least three rhetorical devices, identified in [brackets].",content:{prompt:"ANNUAL EMPLOYEE GATHERING - CEO REMARKS\nCohasset Holdings\nDuration: ~3 minutes\n",tips:"Spend most thought on opening 60s and closing 30s. Single durable image throughout. Mark devices in [brackets]. Avoid achievement-list dilution.",minWords:240}}
    ]},
    // ---------- C2-18 ----------
    {id:"be-c2-18",title:"Unit 18: Crisis Press Conference",subtitle:"Handle hostile Q&A under cameras with composure",exercises:[
        {type:"vc",tl:"Vocabulary",cb:"CPE",title:"Press-Conference Tactics",ins:"Master these advanced media-handling concepts.",content:{words:[
            {w:"bridging",ipa:"/ˈbrɪʤɪŋ/",d:"redirecting from a hostile question to your message"},
            {w:"flagging",ipa:"/ˈflægɪŋ/",d:"signalling an answer's importance ('the key point is...')"},
            {w:"hooking",ipa:"/ˈhʊkɪŋ/",d:"inviting the next question on your terms"},
            {w:"a soundbite",ipa:"/ə ˈsaʊndˌbaɪt/",d:"a short quotable phrase"},
            {w:"a no-comment trap",ipa:"/ə no-comment træp/",d:"refusing in a way that sounds guilty"},
            {w:"a plant question",ipa:"/ə plænt kˈwɛʃən/",d:"a friendly question prepared with an ally"},
            {w:"premise rejection",ipa:"/ˈprɛmɪs rɪˈʤɛkʃən/",d:"refusing the assumption inside a question"},
            {w:"lookback",ipa:"/lookback/",d:"acknowledging what is already settled fact"}
        ]}},
        {type:"ls",tl:"Listening",cb:"CPE",title:"Audio: Hostile Press Q&A",ins:"Listen to a CEO handling a tough press question.",content:{tts:"Reporter: Mrs Vargas, internal documents leaked yesterday show that your senior leadership knew about safety concerns at the Callao plant six months before the incident. Will anyone be held accountable, or is this another case of corporate cover-up? CEO: Thank you. Let me reject the premise of cover-up: at no point did this company conceal information from regulators. What I will acknowledge - and what those documents reflect - is that an internal warning was raised in November and the response was insufficient. That is a failure of management process and it is mine to own. We have already commissioned an independent review by an outside firm. Their full report will be public, not summarised, not sanitised. On accountability: yes, there will be consequences, including for senior leaders. I will not pre-empt the findings, but I want to be clear: no role, including mine, is shielded. Reporter: Will you commit today to resigning if the review finds personal fault? CEO: I have committed myself to whatever the review concludes. The credibility of this process depends on its independence, and I will not undermine it by negotiating my own outcome in front of cameras tonight.",qs:[
            {q:"Which tactic does she use first?",o:["Bridging","Premise rejection","No comment","Flagging"],a:1},
            {q:"What does she own?",o:["Cover-up","Insufficient response","Resignation","Bankruptcy"],a:1},
            {q:"How does she respond to the resignation question?",o:["Refuses to answer","Commits to review outcome","Resigns immediately","Blames team"],a:1}
        ]}},
        {type:"mt",tl:"Matching",title:"Tactic to Example",ins:"Match each press-conference tactic with its example phrase.",content:{l:["Premise rejection","Bridging","Flagging","Lookback","Hooking"],r:["What's already established is...","The key point I want to make is...","Let me reject the premise of...","I'm happy to come back to that next week","Let me come back to your real concern, which is..."],ans:{0:2,1:4,2:1,3:0,4:3}}},
        {type:"kt",tl:"Key Word Transformation",cb:"CPE",title:"Crisis Q&A Phrasing",ins:"Rewrite using the keyword.",content:{ss:[
            {t:"I refuse to accept that idea in your question.",k:"PREMISE",a:"I would respectfully reject the premise of that question."},
            {t:"I take responsibility.",k:"OWN",a:"That is mine to own."},
            {t:"I am not going to decide before the report.",k:"PRE-EMPT",a:"I will not pre-empt the findings."},
            {t:"I won't talk about this in public.",k:"FORUM",a:"This is not the appropriate forum for that conversation."}
        ]}},
        {type:"wr",tl:"Writing",title:"Press-Conference Opening Statement + 3 Q&A Pairs",ins:"Write a CEO's 90-second crisis opening statement and 3 hostile-question / answer pairs. Use elite press-handling tactics. (260-320 words total)",content:{prompt:"CRISIS PRESS CONFERENCE - PREPARED MATERIALS\nCohasset Logistics - Callao Incident\nSpeaker: CEO\n\n[Opening Statement - approx 90 seconds]\n\n[Q1 hostile / A1]\n[Q2 hostile / A2]\n[Q3 hostile / A3]\n",tips:"Mark tactics in [brackets]. Acknowledge what is settled. Reject only false premises. Commit only to what you can verify.",minWords:240}}
    ]},
    // ---------- C2-19 ----------
    {id:"be-c2-19",title:"Unit 19: Letter to Shareholders",subtitle:"Write the annual letter genre - Buffett's craft, Buffett's discipline",exercises:[
        {type:"vc",tl:"Vocabulary",cb:"CPE",title:"Annual-Letter Lexicon",ins:"Master the elevated genre.",content:{words:[
            {w:"intrinsic value",ipa:"/ˌɪnˈtrɪnsɪk ˈvælju/",d:"the discounted value of all future cash"},
            {w:"durable competitive advantage",ipa:"/ˈdʊrəbəl kəmˈpɛtɪtɪv ædˈvæntɪʤ/",d:"sustained moat against competitors"},
            {w:"capital allocation",ipa:"/ˈkæpɪtəl ˌæləˈkeɪʃən/",d:"how leadership deploys retained earnings"},
            {w:"owner-operator mindset",ipa:"/owner-operator ˈmaɪndˌsɛt/",d:"thinking like a long-term shareholder"},
            {w:"to candour",ipa:"/tɪ candour/",d:"frankness, including about mistakes"},
            {w:"ROIC",ipa:"/roic/",d:"return on invested capital"},
            {w:"per-share value",ipa:"/per-share ˈvælju/",d:"value normalised by shares outstanding"},
            {w:"margin of safety",ipa:"/ˈmɑrʤən əv ˈseɪfti/",d:"buying meaningfully below intrinsic value"}
        ]}},
        {type:"rd",tl:"Reading",cb:"CPE",title:"The Shareholder Letter as Literary Form",ins:"Read this analysis.",content:{p:"<p>The annual letter to shareholders has, against all corporate odds, become one of the few enduring literary genres of modern capitalism. The conventions, established by Warren Buffett and refined by figures such as Jeff Bezos and Larry Fink, would have been unthinkable to mid-century executives, who confined themselves to legalistic blandness. The letter is now expected to be candid, contrarian where warranted, witty without being flippant, and grounded in per-share economics.</p><p>What distinguishes the very best is not financial precision, which is taken for granted, but moral seriousness. Buffett's discussion of dividends and retained earnings is, on careful reading, a sustained essay on stewardship. Bezos's repeated insistence on \"Day 1\" was a doctrine of organisational metaphysics. Fink's annual climate letters explicitly attempt to rewrite the social contract of the corporation.</p><p>Aspiring authors of such letters fail in predictable ways: they recite achievements, hide mistakes, smooth over disagreements with regulators, and confuse strategy with adjective. The letter that endures begins with the year's most uncomfortable truth and earns from there the right to talk about anything else.</p>",src:"COHASSET Original - on the genre",qs:[
            {q:"What is taken for granted?",o:["Style","Length","Financial precision","Honesty"],a:2},
            {q:"What distinguishes the best?",o:["Numbers","Moral seriousness","Photos","Length"],a:1},
            {q:"What earns the right to discuss other topics?",o:["Beginning with most uncomfortable truth","Citing competitors","Long appendix","Charity"],a:0}
        ]}},
        {type:"mt",tl:"Matching",title:"Letter Section to Function",ins:"Match each section of an annual letter with its purpose.",content:{l:["Year in candid review","Owner's framework","Capital allocation discussion","Operating segments","Closing reflection"],r:["Long-term company doctrine","Decisions on retained earnings","Granular performance per business","Honest score-keeping including misses","Stewardship philosophy and outlook"],ans:{0:3,1:0,2:1,3:2,4:4}}},
        {type:"fl",tl:"Open Cloze",cb:"CPE",title:"Buffett-Style Diction",ins:"One word per gap. Elite literary register.",content:{ss:[
            {t:"Charlie and I ___ ourselves owners, not employees, of Cohasset Holdings.",a:"consider"},
            {t:"Our preferred holding period ___ remains forever.",a:"emphatically"},
            {t:"We ___ understated our miss in the Andean segment last year, and we will not repeat that.",a:"deliberately"},
            {t:"Per-share value, not headline revenue, is the ___ by which we measure ourselves.",a:"yardstick"},
            {t:"Capital returned to you ___ not from optimism, but from the absence of better internal opportunities.",a:"flowed"}
        ]}},
        {type:"wr",tl:"Writing",title:"CEO Letter to Shareholders",ins:"Write a 280-320-word annual letter from the CEO of Cohasset Holdings. Begin with the year's most uncomfortable truth. Use the conventions of the genre.",content:{prompt:"COHASSET HOLDINGS - LETTER TO OUR SHAREHOLDERS\nFrom: The CEO\nFor: Fiscal year 2026\n\nDear fellow shareholders,\n",tips:"Open with one uncomfortable truth. Cover: candid year review, capital allocation logic, segment-level honesty, philosophy, outlook. Acknowledge a personal mistake. Avoid adjectives that do no work.",minWords:260}}
    ]},
    // ---------- C2-20 CAPSTONE ----------
    {id:"be-c2-20",title:"Unit 20: Capstone - Annual Report Executive Summary",subtitle:"Distil an entire annual report into one elegant page",exercises:[
        {type:"rd",tl:"Reading",cb:"CPE Integrated",title:"What Survives the Annual Report",ins:"Read this masterclass piece.",content:{p:"<p>The annual report is a paradox: it is the most-printed and least-read document a public company produces. Hundreds of pages of audited financials, mandated disclosures, and ESG appendices are condensed, in the only page most readers will actually read, into the executive summary on the inside cover. The asymmetry between effort expended and attention captured is, perhaps, the central craft challenge of corporate communication.</p><p>The masterful summary refuses to substitute breadth for depth. It selects three or four threads that genuinely defined the year - not necessarily the largest in revenue terms, but the largest in <i>signal</i> terms - and treats each with proportionate honesty. It explicitly identifies a strategic choice the board declined to make and the reason. It tells the reader what the company has become, what it is becoming, and what risks could derail that becoming.</p><p>It does this without the ornaments of routine corporate prose: the reflexive superlatives, the trumpeting of awards, the inflation of incremental improvements into transformations. Where the writer of an inferior summary asks \"what should I include?\", the writer of a great one asks the harder question: \"what is so essential that, were it omitted, the reader would have missed the year entirely?\" That single discipline, sustained across forty sentences, is the difference between a document that is filed and one that is read, returned to, and quoted years later.</p>",src:"COHASSET Original - C2 Capstone craft",qs:[
            {q:"What is the central craft challenge?",o:["Page count","Asymmetry of effort vs attention","Print costs","Translation"],a:1},
            {q:"What does the masterful summary identify?",o:["Awards","Office openings","A choice the board declined","Hires"],a:2},
            {q:"What harder question does the great writer ask?",o:["What's nice","What's essential","What's funny","What's cheap"],a:1}
        ]}},
        {type:"mt",tl:"Matching",title:"Annual Report Section to Reader",ins:"Match each section with the reader who scrutinises it most.",content:{l:["MD&A","Risk factors","Notes to financial statements","Sustainability report","CEO letter"],r:["Long-term retail shareholders","Forensic accountants and short-sellers","Plaintiffs' lawyers","ESG portfolio analysts","Sell-side analysts"],ans:{0:4,1:2,2:1,3:3,4:0}}},
        {type:"kt",tl:"Key Word Transformation",cb:"CPE",title:"Distillation",ins:"Compress to elite annual-report register using the keyword.",content:{ss:[
            {t:"This year was very difficult but we still made progress.",k:"NOTWITHSTANDING",a:"Notwithstanding a demanding year, we advanced on every strategic priority."},
            {t:"We decided not to enter the consumer banking market.",k:"DECLINED",a:"We declined entry into consumer banking."},
            {t:"Our strategy continues to work over time.",k:"VINDICATED",a:"Our strategy has been progressively vindicated."},
            {t:"We are not the same company we were five years ago.",k:"BECOME",a:"We are not what we were; we have become something different."}
        ]}},
        {type:"fl",tl:"Open Cloze",cb:"CPE Final",title:"Final Distillation",ins:"One word per gap.",content:{ss:[
            {t:"This summary is, ___ design, brief.",a:"by"},
            {t:"What follows is not an exhaustive recital, ___ a deliberate selection.",a:"but"},
            {t:"We ___ the year on three threads alone.",a:"frame"},
            {t:"We name what we ___ to do.",a:"declined"},
            {t:"And we say, plainly, ___ could undo us in the year ahead.",a:"what"}
        ]}},
        {type:"wr",tl:"Writing",title:"Capstone: Annual Report Executive Summary",ins:"Write a 280-320-word executive summary for Cohasset Holdings' Annual Report 2026. Apply elite craft principles: select 3 threads, name a declined choice, identify risks, refuse routine ornament. This is the final capstone.",content:{prompt:"COHASSET HOLDINGS\nANNUAL REPORT 2026 - EXECUTIVE SUMMARY\n\nA letter to our long-term owners,\n",tips:"Open with one uncomfortable truth. Choose three threads that defined the year. Name a strategic choice declined and why. Identify forward risks honestly. Close with an image, not a slogan. Avoid superlatives.",minWords:260}}
    ]}
]
};

// ============================================================
// Auto-merge into BE_CURRICULUM at load time
// Source file uses property name "lessons" on each level object.
// ============================================================
(function(){
    if (typeof window === 'undefined' || !window.BE_CURRICULUM) return;
    Object.entries(window.BE_CURRICULUM_EXTENSION).forEach(function(entry){
        var level = entry[0], units = entry[1];
        var lvl = window.BE_CURRICULUM[level];
        if (!lvl) return;
        // Detect actual property name used by base curriculum
        var listProp = Array.isArray(lvl.lessons) ? 'lessons'
                     : Array.isArray(lvl.units)   ? 'units'
                     : 'lessons';
        if (!Array.isArray(lvl[listProp])) lvl[listProp] = [];
        units.forEach(function(u){
            // Avoid duplicate-id insertion if extension is loaded twice
            if (!lvl[listProp].some(function(x){ return x && x.id === u.id; })) {
                lvl[listProp].push(u);
            }
        });
    });
})();
