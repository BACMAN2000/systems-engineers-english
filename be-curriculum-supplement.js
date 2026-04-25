// ============================================================
// COHASSET BUSINESS ENGLISH — A1-B1 Supplement
// Adds 2 extra exercises per unit for A1, A2 and B1 (units 2-14)
// so every unit ends up with ≥4 exercises.
// Progression matches Market Leader's thematic syllabus (topics only —
// all passages, dialogues, questions and vocabulary are original).
// ============================================================

(function(){
  // Helper: push exercises into an existing lesson across both data sources
  // (BE_CURRICULUM in business-course-platform.html
  //  + PROGRAMS.business.levels in COHASSET-platform-standalone.html)
  function addEx(levelKey, lessonId, exercises){
    const sources = [];
    if(typeof BE_CURRICULUM !== 'undefined' && BE_CURRICULUM[levelKey]) sources.push(BE_CURRICULUM[levelKey]);
    if(typeof PROGRAMS !== 'undefined' && PROGRAMS.business && PROGRAMS.business.levels && PROGRAMS.business.levels[levelKey]) sources.push(PROGRAMS.business.levels[levelKey]);
    sources.forEach(lv => {
      if(!lv || !lv.lessons) return;
      const lesson = lv.lessons.find(l => l.id === lessonId);
      if(!lesson) return;
      // Avoid double-adding on hot reload: check if first extra exercise already present
      const first = exercises[0];
      if(lesson.exercises.some(e => e && e.title === first.title && e.tl === first.tl)) return;
      lesson.exercises = lesson.exercises.concat(exercises);
    });
  }

  // ==========================================================
  // A1 — ELEMENTARY (Units 2–14)
  // Original scenarios, simple grammar (present simple, can/can't,
  // countables/uncountables, wh-questions).
  // ==========================================================

  addEx('a1','be-a1-2',[
    {type:'vc',tl:'Vocabulary',title:'Daily Work Activities',ins:'Study these common verbs and expressions used at work every day.',content:{words:[
      {w:'start work',d:'Begin your working day'},{w:'have a break',d:'Stop for rest or coffee'},
      {w:'check emails',d:'Read and reply to messages'},{w:'attend a meeting',d:'Go to and participate in a meeting'},
      {w:'finish work',d:'End your working day'},{w:'work from home',d:'Do your job from your house'},
      {w:'take a day off',d:'Not work that day'},{w:'have lunch',d:'Eat in the middle of the day'}
    ]}},
    {type:'rd',tl:'Reading',title:'Ana\'s Typical Day',ins:'Read about Ana and answer the questions.',content:{
      p:'Ana works at Cohasset Trading. She starts work at 8:30 a.m. First, she checks her emails for about thirty minutes. At 9:15 she has a short team meeting. Ana has lunch at 1 p.m. with her colleagues in the cafeteria. In the afternoon she calls clients and writes short reports. She finishes work at 5:30 p.m. On Fridays she works from home because her office closes early.',
      src:'COHASSET Original Material',
      qs:[
        {q:'What time does Ana start work?',o:['7:30','8:30','9:15','5:30'],a:1},
        {q:'Where does she have lunch?',o:['At home','In a restaurant','In the cafeteria','At her desk'],a:2},
        {q:'What does Ana do on Fridays?',o:['Takes a day off','Works from home','Travels','Has a long meeting'],a:1}
      ]}}
  ]);

  addEx('a1','be-a1-3',[
    {type:'rd',tl:'Reading',title:'A Small Problem',ins:'Read the short email and choose the best answers.',content:{
      p:'From: daniel@cohasset.com\nTo: support@cohasset.com\nSubject: Printer problem\n\nHi team,\n\nThe printer on the second floor is not working. I need to print ten reports for a client meeting at 3 p.m. today. Can someone help me? I am on extension 212. Thank you.\n\nDaniel',
      src:'COHASSET Original Material',
      qs:[
        {q:'What is the problem?',o:['No paper','The computer is slow','The printer is not working','The meeting is cancelled'],a:2},
        {q:'When is the meeting?',o:['At 2 p.m.','At 3 p.m.','Tomorrow','Next week'],a:1},
        {q:'What does Daniel want?',o:['A new printer','Help from a colleague','More time','A new client'],a:1}
      ]}},
    {type:'wr',tl:'Writing',title:'Reply to a Problem',ins:'Write a short reply (40–60 words) offering help. Include: greeting, offer of help, time you can come, polite closing.',content:{
      prompt:'Type your reply to Daniel here…',tips:'Start with "Hi Daniel," then offer to help, say when, finish with "Best regards" + your name.',minWords:30}}
  ]);

  addEx('a1','be-a1-4',[
    {type:'ls',tl:'Listening',title:'Booking a Flight',ins:'Listen to the dialogue and answer the questions.',content:{
      tts:'Agent: Good morning, Cohasset Travel. How can I help you? Customer: Hello, I need a flight from Lima to São Paulo for Monday the 14th. Agent: Morning or afternoon? Customer: Morning, please. Agent: We have a 7:40 a.m. flight. It arrives at 1:15 p.m. Customer: Perfect. Is there a return flight on Friday evening? Agent: Yes, at 8:30 p.m. Customer: Great, I\'ll take both. My name is Carlos Mendoza.',
      qs:[
        {q:'Where does Carlos want to go?',o:['Lima','São Paulo','Buenos Aires','Bogotá'],a:1},
        {q:'What day does he travel?',o:['Sunday','Monday','Wednesday','Friday'],a:1},
        {q:'What time is the return flight?',o:['7:40 a.m.','1:15 p.m.','8:30 p.m.','10:00 p.m.'],a:2}
      ]}},
    {type:'fl',tl:'Fill in Blanks',title:'Travel Phrases',ins:'Type the missing word in each sentence.',content:{
      ss:[
        {t:'I would like to ___ a flight to Miami.',a:'book'},
        {t:'What time does the plane ___?',a:'leave'},
        {t:'I have a ___ in London before my final destination.',a:'stopover'},
        {t:'Please check your ___ before going to the airport.',a:'ticket'}
      ]}}
  ]);

  addEx('a1','be-a1-5',[
    {type:'rd',tl:'Reading',title:'A Business Dinner Invitation',ins:'Read the email and answer the questions.',content:{
      p:'Dear Ms. Patel,\n\nThank you for visiting our office today. We would like to invite you and your team to dinner on Thursday evening at 7 p.m. The restaurant is called Casa Andina and it is five minutes from your hotel. Please tell us if you have any food allergies or preferences.\n\nBest regards,\nSales Team, Cohasset International',
      src:'COHASSET Original Material',
      qs:[
        {q:'Who is the dinner for?',o:['All employees','Ms. Patel and her team','New customers only','The CEO'],a:1},
        {q:'What day is the dinner?',o:['Monday','Wednesday','Thursday','Friday'],a:2},
        {q:'What does the host want to know?',o:['Phone number','Room number','Food allergies','Payment method'],a:2}
      ]}},
    {type:'mt',tl:'Matching',title:'Food & Menu Vocabulary',ins:'Match each word with its meaning.',content:{
      l:['Starter','Main course','Dessert','Vegetarian','Bill','Waiter'],
      r:['The person who serves food','A sweet dish after the meal','Without meat or fish','The paper you pay','The first small dish','The biggest dish of the meal'],
      ans:{0:4,1:5,2:1,3:2,4:3,5:0}}}
  ]);

  addEx('a1','be-a1-6',[
    {type:'ls',tl:'Listening',title:'At the Shop',ins:'Listen to a salesperson helping a customer.',content:{
      tts:'Seller: Good afternoon. Can I help you? Customer: Yes, I\'m looking for a small laptop bag. Seller: We have several. This black one is forty-five dollars. The brown one is fifty-five. Customer: How much is the grey one? Seller: The grey one is on sale — thirty-nine dollars. Customer: I\'ll take the grey one, please. Can I pay by card? Seller: Of course.',
      qs:[
        {q:'What does the customer want?',o:['A suitcase','A small laptop bag','A backpack','A wallet'],a:1},
        {q:'How much is the grey bag?',o:['$45','$55','$39','$29'],a:2},
        {q:'How will the customer pay?',o:['Cash','Card','Cheque','Transfer'],a:1}
      ]}},
    {type:'dd',tl:'Drag & Drop',title:'Order the Shopping Dialogue',ins:'Put the sentences in the correct order.',content:{
      ws:['Hello, can I help you?','Yes, I\'m looking for blue pens.','They are on aisle three.','How much are they?','They are two dollars each.','I\'ll take five, please.'],
      ss:[
        {t:'1. ___',b:'Hello, can I help you?'},
        {t:'2. ___',b:'Yes, I\'m looking for blue pens.'},
        {t:'3. ___',b:'They are on aisle three.'},
        {t:'4. ___',b:'How much are they?'},
        {t:'5. ___',b:'They are two dollars each.'},
        {t:'6. ___',b:'I\'ll take five, please.'}
      ]}}
  ]);

  addEx('a1','be-a1-7',[
    {type:'rd',tl:'Reading',title:'Meet the Team',ins:'Read the short staff profiles.',content:{
      p:'Laura Gómez is the Operations Manager. She is from Spain. She speaks three languages: Spanish, English and French. In her free time she likes hiking.\n\nKenji Tanaka is the Lead Designer. He is from Japan but he lives in Lima. He is married and has two children. He enjoys photography.\n\nSarah Mbeki is the Junior Accountant. She is from South Africa. She loves numbers, coffee and running.',
      src:'COHASSET Original Material',
      qs:[
        {q:'Who is the Lead Designer?',o:['Laura Gómez','Kenji Tanaka','Sarah Mbeki','Nobody mentioned'],a:1},
        {q:'Where does Kenji live now?',o:['Japan','Madrid','Lima','Cape Town'],a:2},
        {q:'What does Sarah like?',o:['Hiking','Photography','Coffee and running','Languages'],a:2}
      ]}},
    {type:'fl',tl:'Fill in Blanks',title:'Describing People',ins:'Type the correct adjective.',content:{
      ss:[
        {t:'Maria is always happy and smiles a lot. She is very ___.',a:'friendly'},
        {t:'Tom arrives on time every day. He is ___.',a:'punctual'},
        {t:'She works quickly and well. She is very ___.',a:'efficient'},
        {t:'He doesn\'t like big parties. He is a bit ___.',a:'shy'}
      ]}}
  ]);

  addEx('a1','be-a1-8',[
    {type:'vc',tl:'Vocabulary',title:'Market Basics',ins:'Learn key market words.',content:{words:[
      {w:'customer',d:'A person who buys products or services'},
      {w:'product',d:'Something a company makes to sell'},
      {w:'price',d:'The money you pay for something'},
      {w:'demand',d:'How many people want to buy a product'},
      {w:'supply',d:'How much of a product is available'},
      {w:'competitor',d:'Another company selling similar products'},
      {w:'share',d:'Part of a market that belongs to a company'},
      {w:'brand',d:'The name and image of a product'}
    ]}},
    {type:'ls',tl:'Listening',title:'Market News',ins:'Listen to the short market update.',content:{
      tts:'Good morning. Here is today\'s quick market update. The price of coffee is going up this week because of low supply in Brazil. Demand for electric cars is growing fast in Europe. In technology, a new phone from a Korean company is getting good reviews. That\'s all for now.',
      qs:[
        {q:'Why is coffee going up?',o:['More demand','Low supply in Brazil','New taxes','A new brand'],a:1},
        {q:'Where is demand for electric cars growing?',o:['Asia','Africa','Europe','South America'],a:2},
        {q:'What country is the new phone from?',o:['Japan','China','Korea','Taiwan'],a:2}
      ]}}
  ]);

  addEx('a1','be-a1-9',[
    {type:'vc',tl:'Vocabulary',title:'Types of Companies',ins:'Match each company type with what it does.',content:{words:[
      {w:'multinational',d:'A company that works in many countries'},
      {w:'start-up',d:'A new, small company, often in technology'},
      {w:'subsidiary',d:'A smaller company owned by a bigger one'},
      {w:'headquarters',d:'The main office of a company'},
      {w:'branch',d:'A smaller office of a company in another city'},
      {w:'supplier',d:'A company that sells materials to another company'}
    ]}},
    {type:'rd',tl:'Reading',title:'About Our Company',ins:'Read the short company profile.',content:{
      p:'Cohasset International is a multinational trading company with headquarters in Lima, Peru. We have branches in Bogotá, Santiago and Mexico City. We have around 400 employees and our CEO is Andrea Vargas. We started in 2003 as a small import business. Today we work with more than 120 suppliers around the world.',
      src:'COHASSET Original Material',
      qs:[
        {q:'Where is the head office?',o:['Bogotá','Santiago','Lima','Mexico City'],a:2},
        {q:'When did the company start?',o:['1993','2003','2013','2023'],a:1},
        {q:'How many employees are there?',o:['About 40','About 120','About 400','About 1200'],a:2}
      ]}}
  ]);

  addEx('a1','be-a1-10',[
    {type:'rd',tl:'Reading',title:'Office Technology',ins:'Read the IT support notice.',content:{
      p:'Good morning, team. This is a reminder from IT Support. Please do not click links in emails from unknown senders. If you see a suspicious email, forward it to security@cohasset.com and then delete it. Remember to change your password every three months. If your computer is slow, restart it first before calling support. Thank you.',
      src:'COHASSET Original Material',
      qs:[
        {q:'What should you do with suspicious emails?',o:['Open them','Reply immediately','Forward to security and delete','Print them'],a:2},
        {q:'How often should you change your password?',o:['Every week','Every month','Every 3 months','Every year'],a:2},
        {q:'What should you do first if your computer is slow?',o:['Call IT','Buy a new one','Restart it','Turn it off for the day'],a:2}
      ]}},
    {type:'mt',tl:'Matching',title:'Tech Vocabulary',ins:'Match each word with its definition.',content:{
      l:['Password','Download','Upload','Backup','Attachment','Folder'],
      r:['A copy of your files kept for safety','A secret code to enter your account','A file sent with an email','A place to organize files','Move a file from the internet to your computer','Move a file from your computer to the internet'],
      ans:{0:1,1:4,2:5,3:0,4:2,5:3}}}
  ]);

  addEx('a1','be-a1-11',[
    {type:'ls',tl:'Listening',title:'Cultural Differences',ins:'Listen to a short advice talk.',content:{
      tts:'When you travel for business, small things are important. In Japan, people usually bow when they meet. In Brazil, a handshake is normal but people also greet with a smile and sometimes a hug. In Germany, punctuality is very important — arrive on time or early. In Saudi Arabia, business lunches can last two hours and it is polite to accept tea or coffee.',
      qs:[
        {q:'What do people do in Japan when they meet?',o:['Hug','Kiss','Bow','Shake hands strongly'],a:2},
        {q:'In Germany, what is very important?',o:['Gifts','Punctuality','Formal clothes','Long lunches'],a:1},
        {q:'What should you accept in Saudi Arabia?',o:['Wine','Tea or coffee','A gift','A handshake'],a:1}
      ]}},
    {type:'wr',tl:'Writing',title:'Write a Cultural Tip',ins:'Write 3–5 sentences about a cultural tip for someone visiting your country. (40–60 words)',content:{
      prompt:'Write your cultural tip here…',tips:'Mention: how people greet, how formal people are, what visitors should or shouldn\'t do.',minWords:30}}
  ]);

  addEx('a1','be-a1-12',[
    {type:'rd',tl:'Reading',title:'A Simple Job Advertisement',ins:'Read the advertisement and answer.',content:{
      p:'JUNIOR CUSTOMER SUPPORT ASSISTANT — Cohasset International\n\nWe are looking for a friendly person to join our Customer Support team.\n\nRequirements:\n• Good English (spoken and written)\n• Basic computer skills\n• Patience and a positive attitude\n• No experience needed — we will train you\n\nWorking hours: Monday to Friday, 9 a.m. to 6 p.m.\nSalary: competitive + monthly bonus\n\nSend your CV to jobs@cohasset.com by Friday 28th.',
      src:'COHASSET Original Material',
      qs:[
        {q:'Do you need experience for this job?',o:['Yes, a lot','Yes, a little','No, they will train you','Only in IT'],a:2},
        {q:'When do you work?',o:['Weekends only','Monday to Friday','Only mornings','Only evenings'],a:1},
        {q:'How do you apply?',o:['Call them','Visit the office','Send CV by email','Fill a paper form'],a:2}
      ]}},
    {type:'dd',tl:'Drag & Drop',title:'Build a CV Email',ins:'Put the email parts in order.',content:{
      ws:['Best regards, Laura Pérez','Dear Hiring Team,','Please find my CV attached.','Subject: Application — Junior Customer Support','I am writing to apply for the Junior Customer Support position.'],
      ss:[
        {t:'1. Subject',b:'Subject: Application — Junior Customer Support'},
        {t:'2. Greeting',b:'Dear Hiring Team,'},
        {t:'3. Opening',b:'I am writing to apply for the Junior Customer Support position.'},
        {t:'4. Attachment',b:'Please find my CV attached.'},
        {t:'5. Sign-off',b:'Best regards, Laura Pérez'}
      ]}}
  ]);

  addEx('a1','be-a1-13',[
    {type:'rd',tl:'Reading',title:'Our Online Shop',ins:'Read the short company notice.',content:{
      p:'Cohasset Shop is our online store. Customers can buy our products 24 hours a day. Delivery in the city takes one to two days. For other countries, delivery can take five to ten days. If you are not happy with your product, you can return it in 15 days for a full refund. Payment is by card or bank transfer. All prices include tax.',
      src:'COHASSET Original Material',
      qs:[
        {q:'How long does city delivery take?',o:['1–2 days','3–4 days','5–10 days','2 weeks'],a:0},
        {q:'How many days do you have to return a product?',o:['7','10','15','30'],a:2},
        {q:'What is NOT a payment option?',o:['Card','Bank transfer','Cash at the door','Both cards are accepted'],a:2}
      ]}},
    {type:'mt',tl:'Matching',title:'E-commerce Words',ins:'Match each word with its meaning.',content:{
      l:['Cart','Checkout','Tracking','Refund','Wishlist','Coupon'],
      r:['A special code that reduces the price','The place where you finish and pay','Money returned to the customer','A list of products you want to buy later','Where you put products to buy','Following a package on its way'],
      ans:{0:4,1:1,2:5,3:2,4:3,5:0}}}
  ]);

  addEx('a1','be-a1-14',[
    {type:'rd',tl:'Reading',title:'This Week\'s Plan',ins:'Read the team plan.',content:{
      p:'Hi team,\n\nHere is our plan for this week. On Monday we have a short meeting at 10 a.m. to review last week. On Tuesday Carla is going to call three clients. On Wednesday we are going to visit the warehouse. On Thursday Peter is going to write the monthly report. On Friday we are going to have lunch together at 1 p.m. to celebrate the end of the month. Please tell me if you cannot attend any of these.',
      src:'COHASSET Original Material',
      qs:[
        {q:'What is on Wednesday?',o:['A meeting','Calls to clients','A visit to the warehouse','A lunch'],a:2},
        {q:'Who is going to write the monthly report?',o:['Carla','Peter','The manager','No one'],a:1},
        {q:'Why is the lunch on Friday?',o:['Someone\'s birthday','End of the month celebration','A new client','No special reason'],a:1}
      ]}},
    {type:'fl',tl:'Fill in Blanks',title:'Future Plans with "going to"',ins:'Complete each sentence with "going to".',content:{
      ss:[
        {t:'Tomorrow I ___ ___ call the client.',a:'am going to'},
        {t:'Next week we ___ ___ visit Madrid.',a:'are going to'},
        {t:'On Friday she ___ ___ send the report.',a:'is going to'},
        {t:'They ___ ___ start the new project on Monday.',a:'are going to'}
      ]}}
  ]);

  // ==========================================================
  // A2 — PRE-INTERMEDIATE (Units 2–14) — Market Leader theme set
  // ==========================================================

  addEx('a2','be-a2-2',[
    {type:'vc',tl:'Vocabulary',title:'Sales Basics',ins:'Study these key sales words.',content:{words:[
      {w:'lead',d:'A possible customer'},{w:'prospect',d:'A lead that looks promising'},
      {w:'pitch',d:'A short presentation to sell something'},{w:'close a deal',d:'Successfully finish a sale'},
      {w:'discount',d:'A reduction in price'},{w:'target',d:'A goal, e.g. monthly sales figure'},
      {w:'commission',d:'Extra money a salesperson earns per sale'},{w:'quota',d:'The minimum sales a person must reach'}
    ]}},
    {type:'ls',tl:'Listening',title:'A Sales Call',ins:'Listen and answer.',content:{
      tts:'Salesperson: Good morning, Ms. Lim. I\'m calling from Cohasset Office Solutions. Do you have two minutes? Customer: Yes, but only two. Salesperson: We\'re launching new standing desks with a 20% discount this month. They can be delivered in three working days. Customer: Interesting. Can you send me a short brochure by email? Salesperson: Of course. What is your email? Customer: lim@nortec.com.',
      qs:[
        {q:'What is the salesperson selling?',o:['Office chairs','Standing desks','Laptops','Software'],a:1},
        {q:'What is the discount?',o:['10%','15%','20%','25%'],a:2},
        {q:'What does the customer ask for?',o:['A phone call later','A visit','A brochure by email','A free sample'],a:2}
      ]}}
  ]);

  addEx('a2','be-a2-3',[
    {type:'rd',tl:'Reading',title:'Types of Companies',ins:'Read and answer.',content:{
      p:'Companies come in many sizes. A micro-company has up to 9 employees — often a family business. A small company has 10 to 49. A medium company has 50 to 249. A large company has 250 or more. Around 99% of all companies in the world are small or medium. They create most of the jobs in any country, which is why governments often support them with training and loans.',
      src:'COHASSET Original Material',
      qs:[
        {q:'How many employees does a medium company have?',o:['0–9','10–49','50–249','250+'],a:2},
        {q:'What percentage of companies are small or medium?',o:['49%','75%','99%','100%'],a:2},
        {q:'How do governments often help them?',o:['Free offices','Training and loans','Tax-free forever','All of the above'],a:1}
      ]}},
    {type:'wr',tl:'Writing',title:'Describe a Company',ins:'Write 60–80 words describing a real or imaginary company: name, size, location, what it does, number of employees.',content:{
      prompt:'Write your company description here…',tips:'Use present simple. Include: name, sector, location, size, main products/services.',minWords:50}}
  ]);

  addEx('a2','be-a2-4',[
    {type:'ls',tl:'Listening',title:'A New Idea',ins:'Listen to a short pitch.',content:{
      tts:'Hi everyone. My idea is called Green Lunch. We deliver healthy, affordable lunches to small offices. The price is five dollars per person and we only use reusable containers. Companies can subscribe weekly. I believe offices want a simple, eco-friendly lunch option. I need some investment to buy a small electric van and to build a simple website.',
      qs:[
        {q:'What is the idea?',o:['A restaurant','Healthy lunch delivery for offices','A food blog','A cooking class'],a:1},
        {q:'What makes it eco-friendly?',o:['Organic food only','Reusable containers','Solar kitchen','Paper bags'],a:1},
        {q:'What does the speaker need money for?',o:['Staff','A van and a website','Marketing only','Ingredients'],a:1}
      ]}},
    {type:'wr',tl:'Writing',title:'Your Business Idea',ins:'Pitch your own simple business idea in 80–100 words.',content:{
      prompt:'Describe your idea here…',tips:'Cover: problem, solution, who the customer is, price, what you need to start.',minWords:60}}
  ]);

  addEx('a2','be-a2-5',[
    {type:'rd',tl:'Reading',title:'Managing Stress',ins:'Read the wellness tip and answer.',content:{
      p:'Stress at work is common, but too much stress can make you ill. Simple steps can help. Take short breaks every 90 minutes. Walk outside during your lunch hour if you can. Don\'t check emails after 8 p.m. Sleep at least seven hours. Talk with a colleague or a friend when you feel overwhelmed. Small changes every day are more effective than big changes once a year.',
      src:'COHASSET Original Material',
      qs:[
        {q:'How often should you take a break?',o:['Every 30 minutes','Every 60 minutes','Every 90 minutes','Every 3 hours'],a:2},
        {q:'What should you avoid after 8 p.m.?',o:['Coffee','Checking emails','Exercise','Heavy food'],a:1},
        {q:'What is more effective according to the text?',o:['One big change yearly','Small daily changes','Taking a long vacation','Changing jobs'],a:1}
      ]}},
    {type:'mt',tl:'Matching',title:'Wellness Vocabulary',ins:'Match each word with its meaning.',content:{
      l:['Burnout','Overwhelmed','Work-life balance','Mindfulness','Resilience','Time off'],
      r:['The ability to recover from problems','Extreme exhaustion from long work stress','A holiday or rest from work','When you separate work and personal life well','Focusing on the present moment','Having too much to handle'],
      ans:{0:1,1:5,2:3,3:4,4:0,5:2}}}
  ]);

  addEx('a2','be-a2-6',[
    {type:'rd',tl:'Reading',title:'Hosting a Client',ins:'Read the short guide.',content:{
      p:'When you entertain a client, preparation matters. Choose a restaurant you know. Ask about allergies or diet restrictions in advance. Arrive 10 minutes early. Let the client choose the table side with the best view. Don\'t start business topics until after you have ordered. Keep the conversation light at first — travel, food, sports. Pay the bill discreetly, away from the table if possible.',
      src:'COHASSET Original Material',
      qs:[
        {q:'What should you ask in advance?',o:['Their favourite food','Allergies or diet restrictions','Their salary','The menu'],a:1},
        {q:'How early should you arrive?',o:['At the exact time','5 minutes early','10 minutes early','30 minutes early'],a:2},
        {q:'When should you start business topics?',o:['Immediately','After ordering','Only after dessert','Not at all'],a:1}
      ]}},
    {type:'wr',tl:'Writing',title:'Invite a Client',ins:'Write a short email (60–80 words) inviting a client to lunch next Thursday at 1 p.m.',content:{
      prompt:'Write your invitation here…',tips:'Include: reason, place, time, ask about dietary needs, polite closing.',minWords:50}}
  ]);

  addEx('a2','be-a2-7',[
    {type:'ls',tl:'Listening',title:'Marketing Brief',ins:'Listen to a short brief and answer.',content:{
      tts:'Hi team. This campaign is for our new healthy snack bar. Target audience: office workers aged 25 to 40 who care about health. Budget: twenty thousand dollars. Channels: Instagram, LinkedIn and one newspaper ad. Message: "Real energy, real ingredients." The goal is to reach 50,000 people and sell at least 3,000 bars in the first month. The deadline is the 15th of next month.',
      qs:[
        {q:'Who is the target audience?',o:['Teenagers','Office workers 25–40','Retired people','Athletes'],a:1},
        {q:'What is the budget?',o:['$5,000','$10,000','$20,000','$50,000'],a:2},
        {q:'What is the sales goal for the first month?',o:['300 bars','1,000 bars','3,000 bars','10,000 bars'],a:2}
      ]}},
    {type:'dd',tl:'Drag & Drop',title:'Build a Mini Campaign Plan',ins:'Match each part of the plan with an example.',content:{
      ws:['Instagram + LinkedIn','Healthy snack bar','Office workers 25–40','"Real energy, real ingredients."','$20,000','50,000 people reached'],
      ss:[
        {t:'Product: ___',b:'Healthy snack bar'},
        {t:'Target: ___',b:'Office workers 25–40'},
        {t:'Message: ___',b:'"Real energy, real ingredients."'},
        {t:'Channels: ___',b:'Instagram + LinkedIn'},
        {t:'Budget: ___',b:'$20,000'},
        {t:'Reach goal: ___',b:'50,000 people reached'}
      ]}}
  ]);

  addEx('a2','be-a2-8',[
    {type:'rd',tl:'Reading',title:'Weekly Planning',ins:'Read and answer.',content:{
      p:'Good planning saves time. On Friday afternoon, write down your three main goals for the next week. On Monday, divide each goal into smaller tasks. Put the most difficult task first, ideally in the morning. Block 90-minute focus slots in your calendar. Leave 20% of your week free for urgent things that always appear. Review what you did every Friday and adjust.',
      src:'COHASSET Original Material',
      qs:[
        {q:'When should you write your weekly goals?',o:['Monday morning','Friday afternoon','Sunday night','Any day'],a:1},
        {q:'What should you do first in the day?',o:['Easy tasks','The most difficult task','Meetings','Emails'],a:1},
        {q:'How much of the week should you leave free?',o:['5%','10%','20%','50%'],a:2}
      ]}},
    {type:'mt',tl:'Matching',title:'Planning Vocabulary',ins:'Match each term with its definition.',content:{
      l:['Deadline','Milestone','Priority','Task','Schedule','Deliverable'],
      r:['A plan of times and activities','The last day to finish something','Something that must be done','An important point in a project','Something more important than others','A concrete result you must produce'],
      ans:{0:1,1:3,2:4,3:2,4:0,5:5}}}
  ]);

  addEx('a2','be-a2-9',[
    {type:'ls',tl:'Listening',title:'Feedback Conversation',ins:'Listen to a short performance review.',content:{
      tts:'Manager: Thanks for coming, Javier. Overall, your work this quarter has been strong. Your reports are clear and on time. One thing I\'d like you to work on is speaking up more in team meetings — you have good ideas but you share them only afterwards. Javier: I understand. Sometimes I feel I need more time to think. Manager: That\'s fine. Maybe prepare your main point before the meeting and share it in the first ten minutes.',
      qs:[
        {q:'What does the manager say is strong?',o:['Speaking in meetings','Reports','Sales numbers','Teamwork only'],a:1},
        {q:'What does the manager want Javier to improve?',o:['Punctuality','Speaking up in meetings','Email style','Dress code'],a:1},
        {q:'What is the practical tip?',o:['Speak less','Prepare a point in advance','Avoid meetings','Only send emails'],a:1}
      ]}},
    {type:'wr',tl:'Writing',title:'Give Positive Feedback',ins:'Write 60–80 words giving positive feedback to a colleague about a recent project.',content:{
      prompt:'Type your feedback message here…',tips:'Start with what went well, give a specific example, end with encouragement.',minWords:50}}
  ]);

  addEx('a2','be-a2-10',[
    {type:'rd',tl:'Reading',title:'Handling Conflict',ins:'Read and answer.',content:{
      p:'Disagreement at work is normal. The problem is not the disagreement itself, but how we handle it. First, listen carefully without interrupting. Second, repeat the other person\'s main point to show you understand it — this is called "active listening". Third, focus on the problem, not on the person. Avoid words like "always" and "never", which sound accusing. Finally, suggest a small next step you can both agree on.',
      src:'COHASSET Original Material',
      qs:[
        {q:'What is "active listening"?',o:['Listening quickly','Repeating the other person\'s main point','Writing everything down','Agreeing with everything'],a:1},
        {q:'Which words should you avoid?',o:['"Maybe" and "perhaps"','"Always" and "never"','"Please" and "thanks"','"Why" and "how"'],a:1},
        {q:'What should you end with?',o:['An apology','A small next step','A complaint','A joke'],a:1}
      ]}},
    {type:'mt',tl:'Matching',title:'Conflict Vocabulary',ins:'Match term with meaning.',content:{
      l:['Compromise','Apologise','Mediator','Resolve','Escalate','Misunderstanding'],
      r:['A person who helps two sides agree','Make a problem bigger or send it to a boss','Say sorry','Solve a problem','An agreement where both sides give something','When people did not understand each other'],
      ans:{0:4,1:2,2:0,3:3,4:1,5:5}}}
  ]);

  addEx('a2','be-a2-11',[
    {type:'rd',tl:'Reading',title:'Products vs Services',ins:'Read and answer.',content:{
      p:'A product is something physical you can touch — like a laptop, a chair or a coffee. A service is something a company does for you — like cleaning, consulting or transport. Many modern companies sell both. For example, a software company sells the software (product) and also training and support (services). Services often give more repeat income, while products can be sold one by one at high volume.',
      src:'COHASSET Original Material',
      qs:[
        {q:'Which of these is a service?',o:['A laptop','A coffee','Consulting','A chair'],a:2},
        {q:'What do modern companies often do?',o:['Sell only products','Sell only services','Sell both products and services','Buy from one supplier'],a:2},
        {q:'What is an advantage of services?',o:['They are cheaper','They give repeat income','They are always digital','They have no staff costs'],a:1}
      ]}},
    {type:'wr',tl:'Writing',title:'Describe a Product/Service',ins:'Write 80–100 words describing a product OR a service your company offers (real or imagined). Include features, price range, who it is for.',content:{
      prompt:'Write your description here…',tips:'Paragraph 1: What it is. Paragraph 2: Main features. Paragraph 3: Who buys it and why.',minWords:60}}
  ]);

  addEx('a2','be-a2-12',[
    {type:'ls',tl:'Listening',title:'A Start-up Story',ins:'Listen to the founder and answer.',content:{
      tts:'I started VerdaBox two years ago. We sell a subscription of fresh local vegetables delivered every week. At the beginning it was only me and my partner with an old van. Now we have twelve employees and three vans. The secret was listening to customers. In the first year we changed the box size three times and added a vegan option because people asked for it. This year we are opening a second city.',
      qs:[
        {q:'What does VerdaBox sell?',o:['Frozen food','A vegetable box subscription','Online cooking classes','Kitchen tools'],a:1},
        {q:'How many vans do they have now?',o:['1','2','3','12'],a:2},
        {q:'What did they add in the first year?',o:['A meat option','A vegan option','Free delivery','A gift card'],a:1}
      ]}},
    {type:'dd',tl:'Drag & Drop',title:'Order the Startup Journey',ins:'Put the stages in order.',content:{
      ws:['Hire the first team members','Find a problem to solve','Open a second location','Launch the product','Get your first paying customers','Test the idea with a small group'],
      ss:[
        {t:'1',b:'Find a problem to solve'},
        {t:'2',b:'Test the idea with a small group'},
        {t:'3',b:'Launch the product'},
        {t:'4',b:'Get your first paying customers'},
        {t:'5',b:'Hire the first team members'},
        {t:'6',b:'Open a second location'}
      ]}}
  ]);

  addEx('a2','be-a2-13',[
    {type:'rd',tl:'Reading',title:'Business Travel Tips',ins:'Read and answer.',content:{
      p:'Business travel can be exhausting if you are not prepared. Book flights with enough time between connections — two hours is safer than one. Choose hotels close to your meeting locations to save commute time. Keep digital copies of all travel documents in your email and a cloud drive. Pack one professional outfit and one casual one. Don\'t forget a power bank for your phone — airports have fewer plugs than you think.',
      src:'COHASSET Original Material',
      qs:[
        {q:'How much time between connections does the text recommend?',o:['30 minutes','1 hour','2 hours','4 hours'],a:2},
        {q:'Why keep digital copies of documents?',o:['To save paper','In case you lose the originals','Because they look better','Airlines require it'],a:1},
        {q:'Why bring a power bank?',o:['For medical reasons','Airports have fewer plugs than expected','Power banks are cheaper abroad','Hotels don\'t have electricity'],a:1}
      ]}},
    {type:'fl',tl:'Fill in Blanks',title:'Travel Vocabulary',ins:'Fill in the missing word.',content:{
      ss:[
        {t:'My flight has a two-hour ___ in Panama.',a:'layover'},
        {t:'Please pick me up from the hotel at 7 a.m. sharp by ___.',a:'taxi'},
        {t:'The airport bus will drop us at the ___ terminal.',a:'departures'},
        {t:'Don\'t forget to bring your ___ to the check-in counter.',a:'passport'}
      ]}}
  ]);

  addEx('a2','be-a2-14',[
    {type:'rd',tl:'Reading',title:'Meetings in Different Cultures',ins:'Read and answer.',content:{
      p:'Meetings look different around the world. In Northern Europe, meetings start on time and follow the agenda strictly. In Latin America, meetings often start a few minutes late and include time for social conversation. In Japan, decisions are usually made before the meeting; the meeting itself is to confirm them. In the United States, people often express disagreement openly. Knowing these differences helps you work better with international colleagues.',
      src:'COHASSET Original Material',
      qs:[
        {q:'Where do meetings strictly follow the agenda?',o:['Latin America','Japan','Northern Europe','United States'],a:2},
        {q:'Where are decisions often made before the meeting?',o:['Japan','Brazil','Germany','USA'],a:0},
        {q:'Where is open disagreement common?',o:['Japan','Northern Europe','United States','Everywhere equally'],a:2}
      ]}},
    {type:'wr',tl:'Writing',title:'Tips for Visiting Your Country',ins:'Write 80–100 words with three tips for someone visiting your country for business meetings.',content:{
      prompt:'Write your tips here…',tips:'Mention: punctuality, dress, small talk, gifts, language.',minWords:60}}
  ]);

  // ==========================================================
  // B1 — INTERMEDIATE (Units 2–14)
  // ==========================================================

  addEx('b1','be-b1-2',[
    {type:'rd',tl:'Reading',title:'Frequent Flyer Benefits',ins:'Read and answer.',content:{
      p:'Corporate travel programmes offer business travellers many benefits. Frequent flyers earn "miles" they can use for free flights or upgrades. Priority boarding saves time. Access to airport lounges means you can work quietly before a flight or between connections. Some programmes now offer carbon-offset options so companies can reduce their environmental impact. For heavy travellers, these benefits easily add up to thousands of dollars in time and comfort saved every year.',
      src:'COHASSET Original Material',
      qs:[
        {q:'What can you do with miles?',o:['Only get free coffee','Get free flights or upgrades','Buy luggage','Pay for hotels only'],a:1},
        {q:'What is one new option in programmes?',o:['Free spa access','Carbon-offset','Free upgrades always','No more security'],a:1},
        {q:'Who benefits most?',o:['Occasional travellers','Heavy travellers','Students','Retired people'],a:1}
      ]}},
    {type:'wr',tl:'Writing',title:'Travel Policy Proposal',ins:'Write 100–120 words proposing a simple corporate travel policy for a small company.',content:{
      prompt:'Type your policy here…',tips:'Cover: preferred airlines, budget limits, booking process, expenses, environmental consideration.',minWords:80}}
  ]);

  addEx('b1','be-b1-3',[
    {type:'ls',tl:'Listening',title:'Leading Change',ins:'Listen to the manager\'s message.',content:{
      tts:'Team, I want to talk honestly about the changes coming this quarter. We will migrate to a new CRM system. Yes, it will be uncomfortable for a few weeks. Some processes will slow down before they speed up. But our current system is 12 years old and already losing us customers. I will organise weekly training and a support channel in Slack. Please bring your questions — there are no stupid ones. We will do this together.',
      qs:[
        {q:'What is changing?',o:['The office location','The CRM system','The company name','The CEO'],a:1},
        {q:'How old is the current system?',o:['5 years','8 years','12 years','20 years'],a:2},
        {q:'What support will there be?',o:['Only a user manual','Weekly training + Slack channel','External consultants','No support'],a:1}
      ]}},
    {type:'wr',tl:'Writing',title:'Change Announcement',ins:'Write a 100–120 word message announcing a change to your team (real or imagined).',content:{
      prompt:'Type your announcement here…',tips:'Be honest, explain the "why", acknowledge the challenge, offer support, end with confidence.',minWords:80}}
  ]);

  addEx('b1','be-b1-4',[
    {type:'rd',tl:'Reading',title:'Flat vs Hierarchical Structures',ins:'Read and answer.',content:{
      p:'Traditional hierarchical organisations have many management levels: CEO, Vice Presidents, Directors, Managers, Team Leaders, Employees. Decisions flow from top to bottom. Flat organisations have few levels — sometimes only two or three. Teams have more autonomy but can feel lost without clear direction. Most real companies mix both: flat inside teams for speed, hierarchical between departments for coordination. The key question is not "which is better" but "what does this specific team need right now?".',
      src:'COHASSET Original Material',
      qs:[
        {q:'What is a feature of hierarchical structures?',o:['Few management levels','Decisions flow top to bottom','Total autonomy','No managers'],a:1},
        {q:'What can be a problem in flat organisations?',o:['Too many managers','Feeling lost without direction','Everyone earning the same','No communication'],a:1},
        {q:'What is the main point of the text?',o:['Flat is always better','Hierarchical is always better','Mix both according to needs','Avoid structure'],a:2}
      ]}},
    {type:'wr',tl:'Writing',title:'Analyse Your Structure',ins:'Write 100–120 words analysing your own organisation: is it more flat or hierarchical? What works, what doesn\'t?',content:{
      prompt:'Write your analysis here…',tips:'Describe the structure, give one strength, give one weakness, suggest one improvement.',minWords:80}}
  ]);

  addEx('b1','be-b1-5',[
    {type:'ls',tl:'Listening',title:'Choosing a Channel',ins:'Listen to the marketing meeting.',content:{
      tts:'For the new product we need to decide on channels. Instagram reaches our younger audience but engagement is dropping. LinkedIn is slower but the people we reach are decision-makers. Podcasts are expensive per listener but the listeners are very loyal. Traditional TV is out of our budget. My recommendation is: 50% LinkedIn, 30% Instagram, 20% sponsored podcast episodes.',
      qs:[
        {q:'What is the issue with Instagram?',o:['Too expensive','Dropping engagement','Wrong country','Text only'],a:1},
        {q:'Who do you reach on LinkedIn?',o:['Teenagers','Decision-makers','Retirees','Students'],a:1},
        {q:'What is the recommended LinkedIn percentage?',o:['20%','30%','50%','100%'],a:2}
      ]}},
    {type:'wr',tl:'Writing',title:'Channel Decision Email',ins:'Write 100–120 words recommending a marketing channel mix for a fictional product launch.',content:{
      prompt:'Type your email here…',tips:'Justify each channel with the audience it reaches and expected impact.',minWords:80}}
  ]);

  addEx('b1','be-b1-6',[
    {type:'rd',tl:'Reading',title:'Reading a Simple P&L',ins:'Read and answer.',content:{
      p:'A Profit and Loss (P&L) statement shows if a company made or lost money. The top line is revenue — the total money from sales. Next come costs: what the company paid for materials, staff and rent. Revenue minus costs equals profit. If costs are higher than revenue, the result is a loss. Investors read P&Ls to see how healthy a business is. Two important details: is revenue growing? And is profit growing faster than revenue? If both are yes, the company is usually in good shape.',
      src:'COHASSET Original Material',
      qs:[
        {q:'What is "revenue"?',o:['Profit','Total money from sales','Costs','Taxes'],a:1},
        {q:'What happens if costs are higher than revenue?',o:['Profit','Break-even','Loss','Growth'],a:2},
        {q:'What is a good sign according to the text?',o:['Costs growing','Profit growing faster than revenue','No sales','Only more staff'],a:1}
      ]}},
    {type:'mt',tl:'Matching',title:'Finance Terms',ins:'Match term with meaning.',content:{
      l:['Revenue','Expenses','Profit','Loss','Investor','Break-even'],
      r:['Money coming into the business','Someone who gives money hoping for a return','Total costs','Revenue equals costs exactly','Revenue minus costs when positive','Revenue minus costs when negative'],
      ans:{0:0,1:2,2:4,3:5,4:1,5:3}}}
  ]);

  addEx('b1','be-b1-7',[
    {type:'rd',tl:'Reading',title:'Virtual Teams Across Cultures',ins:'Read and answer.',content:{
      p:'When you lead a virtual team across cultures, small habits matter. Rotate meeting times so one region doesn\'t always meet at 6 a.m. Share written agendas in advance for people who are less comfortable speaking spontaneously in English. Be patient with silence — in some cultures, pausing shows respect, not confusion. Summarise decisions in writing at the end of each meeting to avoid different interpretations. And celebrate in ways that feel inclusive: not everyone drinks, not everyone celebrates the same holidays.',
      src:'COHASSET Original Material',
      qs:[
        {q:'Why rotate meeting times?',o:['Less bandwidth in one region','Fairness to all regions','It\'s cheaper','It\'s faster'],a:1},
        {q:'Why share agendas in advance?',o:['Legal reasons','Helps people less comfortable speaking spontaneously','To save paper','To save time'],a:1},
        {q:'What can silence mean in some cultures?',o:['Disagreement','Confusion','Respect','Boredom'],a:2}
      ]}},
    {type:'mt',tl:'Matching',title:'Cross-Cultural Vocabulary',ins:'Match each term with its meaning.',content:{
      l:['Stereotype','Context','Directness','Hierarchy','High-context culture','Low-context culture'],
      r:['An over-simplified idea about a group','Where a lot is communicated without words','Levels of authority in a group','Where most is said explicitly','Saying exactly what you mean','The situation around a message'],
      ans:{0:0,1:5,2:4,3:2,4:1,5:3}}}
  ]);

  addEx('b1','be-b1-8',[
    {type:'ls',tl:'Listening',title:'A Recruitment Call',ins:'Listen to the HR interview.',content:{
      tts:'HR: Thanks for applying, Mr. Ortiz. Can you tell me briefly about your last job? Candidate: Sure. I was a Junior Analyst at Delta Financial for three years. I worked in the risk team and I learned Python and SQL there. HR: What was your main achievement? Candidate: I built a dashboard that reduced weekly reporting time from six hours to forty minutes. HR: Impressive. Why did you leave? Candidate: I want to move into consulting to see more industries.',
      qs:[
        {q:'How long did he work at Delta Financial?',o:['1 year','2 years','3 years','5 years'],a:2},
        {q:'What was his main achievement?',o:['A new product','A dashboard that reduced reporting time','Hiring a team','Opening a new office'],a:1},
        {q:'Why does he want to change?',o:['Higher salary','Closer to home','Move into consulting to see more industries','Learn a language'],a:2}
      ]}},
    {type:'wr',tl:'Writing',title:'STAR Answer',ins:'Using the STAR technique (Situation, Task, Action, Result), write a 120-word interview answer to: "Tell me about a time you solved a difficult problem at work."',content:{
      prompt:'Type your STAR answer here…',tips:'S: context, T: your responsibility, A: what you did, R: quantifiable result.',minWords:90}}
  ]);

  addEx('b1','be-b1-9',[
    {type:'ls',tl:'Listening',title:'Entering a New Market',ins:'Listen to the expansion briefing.',content:{
      tts:'Before we enter the Colombian market we need three checks. One: legal — registering the local entity takes about ten weeks. Two: financial — we need to plan for six months of losses before break-even. Three: cultural — our Lima playbook won\'t work directly. For example, payment habits are different. We need to partner with a local distributor in year one, and consider opening our own subsidiary in year two if results are positive.',
      qs:[
        {q:'How long does it take to register the local entity?',o:['2 weeks','6 weeks','10 weeks','6 months'],a:2},
        {q:'How long of losses should they plan for?',o:['1 month','3 months','6 months','2 years'],a:2},
        {q:'What is the strategy for year one?',o:['Own subsidiary','Partner with a local distributor','Franchise','Only online'],a:1}
      ]}},
    {type:'wr',tl:'Writing',title:'Market Entry Recommendation',ins:'Write 120–150 words recommending how a fictional company should enter a new country (distributor, joint venture or subsidiary).',content:{
      prompt:'Type your recommendation here…',tips:'State the mode, justify with risk, cost and speed. Mention one cultural consideration.',minWords:100}}
  ]);

  addEx('b1','be-b1-10',[
    {type:'rd',tl:'Reading',title:'The Whistle-blower Dilemma',ins:'Read and answer.',content:{
      p:'Imagine you discover that your company is hiding a product defect that could harm customers. What do you do? Staying silent protects your job but damages customers. Speaking up is ethically right but can cost you your career. Many countries now have whistle-blower protection laws that shield employees who report illegal or unsafe practices through proper channels. Before going public, ethics experts recommend: document what you saw, report internally first in writing, keep a copy outside the company, and seek legal advice.',
      src:'COHASSET Original Material',
      qs:[
        {q:'What is a "whistle-blower"?',o:['A person who reports illegal or unsafe practices','A company lawyer','A customer who complains','A retired employee'],a:0},
        {q:'What do ethics experts recommend FIRST?',o:['Call the media','Document what you saw','Quit immediately','Confront the CEO'],a:1},
        {q:'Why report internally first?',o:['It\'s more polite','It\'s the proper channel in most laws','To save costs','To stay anonymous'],a:1}
      ]}},
    {type:'mt',tl:'Matching',title:'Ethics Vocabulary',ins:'Match term with meaning.',content:{
      l:['Conflict of interest','Bribery','Transparency','Accountability','Compliance','Integrity'],
      r:['Openness about decisions and information','Following rules and laws','Honesty and strong moral principles','Being responsible for your actions','Paying someone illegally for a favour','A situation where duty conflicts with personal gain'],
      ans:{0:5,1:4,2:0,3:3,4:1,5:2}}}
  ]);

  addEx('b1','be-b1-11',[
    {type:'ls',tl:'Listening',title:'Leadership Interview',ins:'Listen to a short interview with a team leader.',content:{
      tts:'Interviewer: What is the most important lesson you learned as a leader? Leader: I used to think leadership was about having answers. Now I think it\'s about asking the right questions and creating space for the team to find answers. When I moved from giving instructions to coaching, engagement scores in my team went up by twenty percent in six months. It\'s not about me solving everything — it\'s about the team becoming stronger every week.',
      qs:[
        {q:'What did she used to think leadership was?',o:['Control','Having all the answers','Being friendly','Working more hours'],a:1},
        {q:'How did engagement change?',o:['Dropped 10%','Up 10%','Up 20%','Up 50%'],a:2},
        {q:'What is her current view?',o:['Solve everything yourself','Ask right questions and coach the team','Only delegate','Avoid decisions'],a:1}
      ]}},
    {type:'wr',tl:'Writing',title:'Leadership Philosophy',ins:'Write 120–150 words describing your leadership philosophy (real or aspirational).',content:{
      prompt:'Type your philosophy here…',tips:'Include: one core principle, one everyday practice, one example of when it helped.',minWords:100}}
  ]);

  addEx('b1','be-b1-12',[
    {type:'ls',tl:'Listening',title:'Competitive Positioning',ins:'Listen to a short strategy update.',content:{
      tts:'Our biggest competitor just lowered prices by fifteen percent. We have three options. Match the price — but our margin goes from 35% to 20%. Add features at the same price — but engineering needs six months. Target a different segment where price is less important — premium customers who value service. My recommendation is the third option: we move upmarket and invest in customer service. We lose 10% of current customers but gain a healthier business.',
      qs:[
        {q:'What did the competitor do?',o:['Raised prices','Lowered prices by 15%','Launched a new product','Exited the market'],a:1},
        {q:'How would matching the price affect margin?',o:['Stays at 35%','Drops to 20%','Grows to 50%','Irrelevant'],a:1},
        {q:'What is the recommendation?',o:['Match price','Add features','Move upmarket and invest in service','Do nothing'],a:2}
      ]}},
    {type:'wr',tl:'Writing',title:'Competitive Response',ins:'Write 120–150 words advising a company how to respond when a competitor drops prices.',content:{
      prompt:'Type your advice here…',tips:'Pick ONE option (match price, add value, reposition) and justify with numbers and risk.',minWords:100}}
  ]);

  addEx('b1','be-b1-13',[
    {type:'rd',tl:'Reading',title:'Clearer Emails',ins:'Read and answer.',content:{
      p:'Most professional emails are too long. Three habits improve clarity fast. First: the subject line should be a one-line summary of the email, not a vague "Hello". Second: put your request in the first sentence — "I need your approval on X by Friday" — before any context. Third: use short paragraphs and bullet points for readable structure. Anything longer than four sentences usually needs a meeting or a document, not an email.',
      src:'COHASSET Original Material',
      qs:[
        {q:'What should the subject line do?',o:['Be vague','Summarise the email in one line','Be a question','Include emojis'],a:1},
        {q:'Where should the request go?',o:['The end','The first sentence','In a footer','Not at all'],a:1},
        {q:'When does the text suggest a meeting instead of email?',o:['Always','When email is longer than 4 sentences','Never','Only on Mondays'],a:1}
      ]}},
    {type:'wr',tl:'Writing',title:'Rewrite a Vague Email',ins:'Rewrite this vague email in a clearer style (120–150 words): "Hi John, hope you are well. I wanted to follow up on the thing we talked about last week. Let me know if you have a moment. Thanks."',content:{
      prompt:'Type your rewrite here…',tips:'Clear subject, specific request in first line, deadline, contact if questions.',minWords:90}}
  ]);

  addEx('b1','be-b1-14',[
    {type:'rd',tl:'Reading',title:'Project Basics',ins:'Read and answer.',content:{
      p:'A project has four basic constraints: scope, time, cost and quality. Scope is what you will deliver. Time is the deadline. Cost is the budget. Quality is how good the result must be. Changing one usually affects the others — the classic "pick any two" triangle. A good project manager makes these trade-offs visible to stakeholders. If the client wants more scope, they must accept more cost or time. Surprises are rarely the problem; hiding trade-offs is.',
      src:'COHASSET Original Material',
      qs:[
        {q:'What are the four constraints?',o:['Team, budget, tools, deadline','Scope, time, cost, quality','Vision, mission, values, goals','People, process, product, profit'],a:1},
        {q:'What happens if you change one constraint?',o:['Nothing','Only one other is affected','It usually affects the others','The project ends'],a:2},
        {q:'What is the real problem according to the text?',o:['Surprises','Hiding trade-offs','Too many meetings','Lack of budget'],a:1}
      ]}},
    {type:'wr',tl:'Writing',title:'Scope Change Email',ins:'Write 120–150 words explaining to a client that a scope change they requested will require additional time and cost.',content:{
      prompt:'Type your email here…',tips:'Acknowledge the request, explain implications clearly, give options, invite a decision.',minWords:100}}
  ]);

  console.log('[Cohasset] Business English supplement loaded — 39 units enriched (A1 + A2 + B1).');
})();
