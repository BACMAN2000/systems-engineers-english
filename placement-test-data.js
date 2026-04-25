// ============================================================
// Cohasset Placement Test — 70 questions (source: Paolo's PDF)
// Answer key inferred from standard English grammar/usage
// CEFR banding based on question difficulty progression in the source.
// ============================================================
window.PLACEMENT_QUESTIONS = [
  { q: 'My brother is _________ artist.', options: ['the', 'an', 'a', 'in'], answer: 1 },
  { q: 'A: "Drive carefully". B: "___________, Dad".', options: ["You're welcome.", 'Thank you', 'Hello', "Don't worry."], answer: 3 },
  { q: "Peter is Louise and Molly's father. Molly is ___________", options: ["Peter's wife", "Peter's sister", "Peter's daughter", "Peter's aunt"], answer: 2 },
  { q: "Rose is Bill's niece. Bill is Rose's ____________", options: ['aunt', 'uncle', 'brother', 'father'], answer: 1 },
  { q: '____________ is a bottle of champagne?', options: ['How much', 'How many', 'How', 'What much'], answer: 0 },
  { q: 'first, second, third, ________', options: ['fitfth', 'fourth', 'sixth', 'second'], answer: 1 },
  { q: 'Do you ______ wake up before 7 am? No, ________', options: ['ever, everyday', 'ever, hardly ever', 'no, no', 'sometimes, sometimes'], answer: 1 },
  { q: 'Spring, ________ Autumn, ___________', options: ['Summer, Winter', 'January, February', 'March, April', 'Winter, Fall'], answer: 0 },
  { q: 'Studying is something I _________ do _____ Sunday.', options: ['always, in', 'always, at', 'sometimes, at', 'never, on'], answer: 3 },
  { q: 'A: "_________there ______ flowers in the vase?" B: "Yes, _________"', options: ['Is, any, it is', 'Are, any, there are', 'Is, some, some', 'Are, some, there is'], answer: 1 },
  { q: "Which word doesn't belong to the group?", options: ['sometimes', 'often', 'actually', 'hardly ever'], answer: 2 },
  { q: 'A: "I live ____ a hill". B: "I live ______ the sea". C: "I live _______ the city".', options: ['on, near, in', 'in, in, in', 'at, near, at', 'near, in, at'], answer: 0 },
  { q: 'A: "How _______ milk ____ there?" B: "________"', options: ['many, are, not many', 'much, is, not much', 'much, are, not much', 'many, is, not much'], answer: 1 },
  { q: 'A: "How ______cookies _____there?" B: "_______"', options: ['many, is, many', 'much, are, some', 'many, are, none', 'many, is, none'], answer: 2 },
  { q: 'A: "How ______ peppers _____ there?" B: "There ______ ______"', options: ["much, are, aren't any", 'much, is, not many', "many, are, aren't any", 'much, are, some any'], answer: 2 },
  { q: 'I am ________ ________ my brother. I am _________ than my sister.', options: ['short, tall', 'shorter, bigger', 'shorter than, taller', 'shorter than, tall'], answer: 2 },
  { q: 'I ______ eat my lunch very __________.', options: ['have, slow', 'can, slow', 'do, slow', 'can, slowly'], answer: 3 },
  { q: 'A: "______you speak Chinese?" B: "_____, I ______"', options: ["Can, Yes, can't", "Can, No, can't", "Can, yes, don't", 'Do, No, can'], answer: 1 },
  { q: 'Which is the correct sentence?', options: ['London is a very big city.', 'A very big city is London', 'London city very big is a', 'Very big a London city is'], answer: 0 },
  { q: 'A: "What is the ________?" B: "It is _____________".', options: ['soap opera about, crime', 'programme, about crime', 'contest about, about general knowledge', 'contest, general knowledge'], answer: 0 },
  { q: 'A: "What __________________?" B: "She\'s tall with ______________".', options: ['she looks like?, curly dark hair', 'do she looks like?, dark curly hair', 'does she look like?, dark curly hair', "'s she look like?, curly dark hair"], answer: 2 },
  { q: 'Has this city got _____ good cinemas? Yes, it has got_______.', options: ['any- any', 'most- any', 'much-some', 'any-some'], answer: 3 },
  { q: 'Buy a bunch of _______, a packet of _______ and a can of _______.', options: ['flowers, cigarettes, beans', 'socks, scissors, jeans', 'cake, keys, wood', 'jam, tissues, wood'], answer: 0 },
  { q: 'Tania ____ ______ late for appointments but I ____ _____ late.', options: ['is, always, am always', 'is, always, am, never', 'are, always, are, never', 'is sometimes, was, sometimes'], answer: 1 },
  { q: 'A: "Do you enjoy ___________?" B: "Not really. But after two hours __________"', options: ['going round the shops, I am going home', 'go to the shops, I am going home', 'going round the shops, I want to go home', 'go round the shops, I want to go home'], answer: 2 },
  { q: 'Today I _________ a top from Primark. I ______ wear designer clothes but lately I _________ more high street clothes.', options: ['wear, never, buy', 'am going to wear, usually, hate', 'am wearing, usually, am buying', 'am wearing, never, buy'], answer: 2 },
  { q: 'A: "At 8:30am, ______ you driving ___ work?" B: "Yes, I _____".', options: ['do, to, do', 'do, for, do', 'where, to, was', 'were, to, was'], answer: 3 },
  { q: 'Lauren has a friend _______ never stops eating.', options: ['who', 'whose', 'what', 'whom'], answer: 0 },
  { q: 'I have a cool phone ________ takes good photos.', options: ['which', 'who', 'these', 'whose'], answer: 0 },
  { q: 'Charlotte and I first met when we were in college and we ___________ immediately.', options: ['a lot in common', 'click', 'hit it off', 'close friends'], answer: 2 },
  { q: 'Choose the correct sentence.', options: ['What you were doing at 9pm last Saturday?', 'What did you wearing?', 'Where were you going?', 'What you did after that?'], answer: 2 },
  { q: "Scuba diving in the Bahamas was _________ the most exciting thing I've ever done.", options: ['slightly', 'by far', 'a lot', 'just'], answer: 1 },
  { q: 'I was absolutely ____________ - it was a fantastic present, thank you!', options: ['thrilled', 'worried', 'great', 'embarrassed'], answer: 0 },
  { q: 'Choose the correct sentence.', options: ['Your car is looking very old.', "Yes, I'm thinking of getting a new one.", "I'm having a new car and love it.", 'What are you thinking of the new James Bond movie?'], answer: 1 },
  { q: 'Choose the sentence that is NOT correct.', options: ['Carol is single, but she has been looking for a boyfriend.', 'She is been going to online dating sites.', 'She had been dreaming of finding the ideal partner.', 'She has been on several dates.'], answer: 1 },
  { q: 'I can help you with your homework. I speak ________ French and have _______ free time later today.', options: ['little, plenty', 'lots of, a few', 'a bit of, plenty of', 'some, no'], answer: 2 },
  { q: 'Choose the phrase that is NOT correct.', options: ['a bar of soap', 'a bowl of soup', 'a jar of honey', 'a packet of wine'], answer: 3 },
  { q: 'I first met my wife _____ the spring of 2011, ______ April 17th to be exact. It was ______ a business trip to Belgrade.', options: ['on, near, in', 'in, on, during', 'during, in, on', 'in, on, for'], answer: 1 },
  { q: "We didn't paint the house ourselves.", options: ['We had it painted.', 'I painted it.', 'We painted it.', 'We have it painted.'], answer: 0 },
  { q: 'Choose the phrase that is correct.', options: ['a brand-new Italian colourful tie', 'a pair of baggy ridiculous silk trousers', 'a checked large baseball cap', 'a long plain black leather coat'], answer: 3 },
  { q: 'Al is _______ and has dark, ______ hair with grey ________ and a _________ hairline.', options: ['deep-set, long, freckles, bad', 'tall, straight, wrinkles, recede', 'slim, wavy, streaks, receding', 'short, long, hair, good'], answer: 2 },
  { q: 'I ______ the radio on and listen to the news before ________ a shower and ________ dressed.', options: ['get, take, get', 'turn, to take, get', 'put, having, getting', 'put, washing, getting'], answer: 2 },
  { q: 'I __________ a really cool pair of blue sunglasses. I __________ around Camden Market when I __________ a new designer shop.', options: ['am just buying, walked, have seen', 'have just bought, was walking, saw', 'have just bought, walked, saw', 'bought, walked, saw'], answer: 1 },
  { q: 'I ________ for some Aviator glasses for ages and the shop __________ some very cheaply.', options: ['wanted, sold', 'used to look, had sold', 'looked, would sell', 'had been looking, was selling'], answer: 3 },
  { q: 'A: Heath Ledger was not born in America. B: ____________ Arnold Schwarzeneger.', options: ['Neither was', 'So was', 'Both is', 'Neither is'], answer: 0 },
  { q: 'Choose the sentence that is correct.', options: ['Lidia decided to studying in England.', 'She wanted her parents pay for her sutdies.', 'Unfortunately, they could not afford help her.', 'Lidia found a job and managed to save the money.'], answer: 3 },
  { q: "A: I always try _________ my parents' point of view. B: Oh really? I avoid _______ to my parents about personal things.", options: ['to see, explaining', 'to understand, talking', 'understanding, to talk', 'to understand, to speak'], answer: 1 },
  { q: 'Annoyed or bored with something that you feel you have accepted for too long.', options: ['exhausted', 'irritating', 'fed up', 'tired'], answer: 2 },
  { q: 'Choose the sentence that is NOT correct.', options: ['There was a steady stream of people coming in through the gates of the park.', 'The situation was complicated and it took quite some time for me to digest the information.', 'The opening speech was very powerful and gave us all a lot of food for thought.', "You can't convince me to take up judo, you're wasting your arguments."], answer: 3 },
  { q: "I wish I was _______. I'd __________ on all kinds of things: clothes, shoes, eating out, going on holiday. If I didn't have a family to look after and a home to run, I'd love to just _________ all my money on a round-the-world trip, or something.", options: ['loaded, splash out, blow', 'rich, buy, spending', 'famous, see, waste', 'wealthy, spend, invest'], answer: 0 },
  { q: 'Choose the sentence that is correct.', options: ["If I am the president of my country, I'd spend more money on the environment.", "If I did ever had the chance, I'd take a year off and go travelling.", "If I could live anywhere in the world, I'd probably bought a beach villa in Tahiti.", "If I didn't need to learn English, I would have stopped a long time ago."], answer: 3 },
  { q: "If you'd studied a bit more, ________________________.", options: ['you would be stressed about the test.', "you wouldn't be worrying about the exams.", 'you feel calmer.', 'you will do better in school.'], answer: 1 },
  { q: 'We _________ for the trip ________ three months. I was so disappointed when they ________ it.', options: ['had prepared, for, cancelled', 'had been preparing, for over, cancelled', 'were preparing, since, cancelled', 'prepared, since, rescheduled'], answer: 1 },
  { q: 'Choose the sentence that is correct.', options: ['John was walking home one night.', 'He was hearing a strange noise behind him.', 'It had sounded as if someone had followed him.', 'He was turning around quickly to see who it was.'], answer: 0 },
  { q: 'Choose the sentence that is correct.', options: ["I'll have gone out with friends on Thursday night.", "I'll be having my dinner by the time you get home.", "I won't have gone away on holiday again for at least six months.", "I'll have finished this assignment before I go to bed."], answer: 3 },
  { q: 'Weddings ________ be much simpler in my day. People __________ spend so much money on them for a start. And they certainly _________ go abroad to get married.', options: ["used to, didn't use to, didn't use to", "used to, didn't used to, didn't used to", "didn't use to, used to, used to", "didn't used to, used to, used to"], answer: 0 },
  { q: "I'm not usually superstitious, but you know how sometimes you feel like you've got a _____ - you know, you feel like everything's going wrong?", options: ['loopy', 'unlucky', 'bad luck', 'jinx'], answer: 3 },
  { q: 'I was _________ confidently down the street on my way to work. I was feeling good in a new ______ that I was wearing for the first time.', options: ['strolling, attitude', 'striding, outfit', 'running, car', 'walking, demeanor'], answer: 1 },
  { q: 'Choose the sentence that is NOT correct.', options: ['Chocolate is thought to relieve stress.', 'Pale skin was said to be a sign of great beauty.', 'Cosmetic surgery was once considered to be an expensive luxury.', 'Working in front of a computer is knowed to be bad for your eyes.'], answer: 3 },
  { q: 'Calm and easy-going, not worried about problems and not easily stressed.', options: ['laid-back', 'level-headed', 'relaxed', 'down-to-earth'], answer: 0 },
  { q: "They don't live near here.", options: ['They are not from this neck of the woods.', "They don't need to get it off their chest.", 'They will not play it by ear.', "They haven't made their minds up."], answer: 0 },
  { q: "A: I can't stop thinking about where he might be. B: Yes, anything ____________ have happened to him!", options: ['must', 'may', 'could', 'will'], answer: 2 },
  { q: 'Choose the sentence that is correct.', options: ['I seem to get poorer and poorer every year.', 'He appears to being asleep.', "It seems if we've been here before.", 'The local people all seemed like very friendly.'], answer: 0 },
  { q: "The shopping centre is a little _____________ but they're planning to redevelop it soon.", options: ['eccentric', 'hideous', 'run-down', 'tough'], answer: 2 },
  { q: "It was __________ outside but I hadn't brought my umbrella.", options: ['drizzling', 'wet', 'intriguing', 'spitting'], answer: 0 },
  { q: 'Choose the sentence that is NOT correct.', options: ["What I wouldn't want is to be written about in the tabloid papers.", 'What I really hate is the way that celebrities always sound so sure of themselves.', 'What only thing that matters to some people is being on TV.', "What I don't understand is why people take her so seriously."], answer: 2 },
  { q: 'Choose the sentence that is correct.', options: ['I made out his face for a split second as he walked past.', 'She stared at me across the room.', "I couldn't glance at the details in the photograph because the quality was so bad.", "I caught sight of the rain through the window for ages, thinking about what I'd say to her."], answer: 0 },
  { q: 'Choose the sentence that is correct.', options: ['I get absolutely nervous before exams.', 'That was a totally ridiculous thing to say.', 'His performance was very extraordinary.', 'The film was quite disappointing, but the party afterwards was extremely brilliant.'], answer: 1 },
  { q: 'I got my first ______ of freedom when I went travelling on my own for the first time.', options: ['sign', 'taste', 'right', 'intrigue'], answer: 1 },
  { q: "Osgood, Indiana, isn't the most of exciting place in the world to grow up. There was not hardly anything to do and there were few other kids to play with. In any case, none of the other kids had much of time to play because they had to help their families.", options: ['three extra words (mistakes)', 'two extra words (mistakes)', 'one extra word (mistake)', 'completely correct'], answer: 0 },
];

// CEFR bands (0-indexed question ranges; end exclusive)
window.PLACEMENT_BANDS = [
  { start: 0,  end: 15, level: 'A1', label: 'A1 — Beginner',          desc: 'Basic expressions, simple interactions.' },
  { start: 15, end: 28, level: 'A2', label: 'A2 — Elementary',        desc: 'Everyday topics in simple terms.' },
  { start: 28, end: 42, level: 'B1', label: 'B1 — Intermediate',      desc: 'Familiar topics and travel situations.' },
  { start: 42, end: 55, level: 'B2', label: 'B2 — Upper-Intermediate',desc: 'Complex ideas, abstract topics.' },
  { start: 55, end: 65, level: 'C1', label: 'C1 — Advanced',          desc: 'Fluent and flexible for social, academic and professional use.' },
  { start: 65, end: 70, level: 'C2', label: 'C2 — Proficient',        desc: 'Near-native command of the language.' },
];

// Given total correct 0..70, map to CEFR level
window.scoreToLevel = function(correct){
  if(correct >= 60) return 'C2';
  if(correct >= 50) return 'C1';
  if(correct >= 38) return 'B2';
  if(correct >= 26) return 'B1';
  if(correct >= 15) return 'A2';
  return 'A1';
};
