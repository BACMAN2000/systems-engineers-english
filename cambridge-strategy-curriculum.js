// ============================================================
// CAMBRIDGE ENGLISH EXAMS STRATEGY CURRICULUM
// Cohasset Language Center
// 20 lessons: 4 lessons x 5 exams (KET A2, PET B1, FCE B2, CAE C1, CPE C2)
// ============================================================

const cambridgeStrategyCurriculum = {
    metadata: {
        title: "Cambridge English Exams Strategy",
        institution: "Cohasset Language Center",
        version: "2026.1",
        total_lessons: 20,
        exams: ["KET (A2)", "PET (B1)", "FCE (B2)", "CAE (C1)", "CPE (C2)"],
        skills_per_exam: ["Reading & UoE", "Writing", "Listening", "Speaking"]
    },

    lessons: [

        // ============================================================
        // KET (A2 KEY) — 4 LESSONS
        // ============================================================

        {
            id: "cam-ket-reading-uoe",
            exam: "ket",
            cefr: "A2",
            skill: "reading-uoe",
            title: "KET Reading & Writing — Strategy",
            subtitle: "Master 7 parts in 60 minutes",
            duration_min: 60,
            paper_overview: { time: "60 min", parts: 7, questions: 32, marks: "50% of total" },
            objectives: [
                "Identify each Reading & Writing part type",
                "Apply timing per part (~7-9 min each)",
                "Use elimination for multiple choice",
                "Spot signal words in short texts"
            ],
            parts_breakdown: [
                { part: 1, name: "Signs/Notices", questions: 6, time: "5 min", strategy: "Match short texts (signs, emails, notes) to A/B/C meanings. Focus on key verbs.", example: "'Closed for repairs' -> meaning: not open" },
                { part: 2, name: "Multiple matching (3 texts + sentences)", questions: 7, time: "8 min", strategy: "Scan all 3 texts first, then read each sentence and locate keywords.", example: "Match person to hobby description" },
                { part: 3, name: "Multiple choice (long text)", questions: 5, time: "8 min", strategy: "Read full text once, then questions in order (questions follow text order).", example: "Story about a holiday — Q1 about start, Q5 about end" },
                { part: 4, name: "Gapped text (vocabulary)", questions: 6, time: "7 min", strategy: "Read whole text first. Look at words BEFORE and AFTER the gap. Eliminate wrong word class.", example: "He ___ to school every day -> goes/walks/runs" },
                { part: 5, name: "Open cloze (grammar)", questions: 6, time: "7 min", strategy: "One word per gap. Usually grammar words: prepositions, articles, auxiliaries, pronouns.", example: "I have lived here ___ 2010 -> since" },
                { part: 6, name: "Short writing (email 25+ words)", questions: 1, time: "10 min", strategy: "Cover 3 bullet points. Include greeting + closing.", example: "Email a friend about your weekend" },
                { part: 7, name: "Picture story (35+ words)", questions: 1, time: "15 min", strategy: "Describe 3 pictures in order. Use past simple + connectors (then, after that).", example: "Three pictures showing a lost dog" }
            ],
            sections: [
                { type: "strategy", title: "Timing strategy", content: "Spend 35 min on Parts 1-5 (reading), 25 min on Parts 6-7 (writing). Always leave 3 min to check answers." },
                { type: "tips", title: "Top 5 KET R&W tips", content: "1) Read the question BEFORE the text. 2) Underline key words. 3) Eliminate clearly wrong options. 4) Never leave blanks — guess. 5) Check spelling on writing tasks." },
                { type: "common_mistakes", title: "Avoid these", content: "Wrong word class in Part 4 (noun where verb needed). Multiple words in Part 5 (only ONE word allowed). Forgetting greetings in Part 6 email." }
            ],
            next_steps: ["Practice Test 1 — Parts 1-3", "Vocabulary list: A2 high-frequency 1500 words"]
        },

        {
            id: "cam-ket-writing",
            exam: "ket",
            cefr: "A2",
            skill: "writing",
            title: "KET Writing — Email & Story",
            subtitle: "Two short tasks, big impact",
            duration_min: 60,
            paper_overview: { time: "Within R&W 60 min", parts: 2, questions: 2, marks: "Part 6: 25-35w; Part 7: 35+ w" },
            objectives: [
                "Write a 25-word email covering 3 bullet points",
                "Write a 35-word story from 3 pictures",
                "Use simple connectors and past simple confidently"
            ],
            parts_breakdown: [
                { part: 6, name: "Email", questions: 1, time: "10 min", strategy: "Greeting + cover all 3 bullets + closing. Use: Hi [name], Thanks for..., See you soon, [your name].", example: "Reply to friend's invitation" },
                { part: 7, name: "Story (3 pictures)", questions: 1, time: "15 min", strategy: "Use past simple. Connect with: First, Then, After that, Finally.", example: "Picture 1: girl at park. Picture 2: rain. Picture 3: girl at home" }
            ],
            sections: [
                { type: "template", title: "Email template (Part 6)", content: "Hi [Name], Thanks for your email. [Bullet 1 response]. [Bullet 2 response]. [Bullet 3 response]. See you soon, [Your name]" },
                { type: "model_answer", title: "Model email (B/passing)", content: "Hi Sam, Thanks for the invite! I'd love to come to your party on Saturday. I will bring some snacks. Can I bring my brother too? See you soon, Alex. (32 words)" },
                { type: "template", title: "Story template (Part 7)", content: "Last [day/weekend], [character] [action]. First, [picture 1 event]. Then, [picture 2 event]. Finally, [picture 3 event]. [feeling]." },
                { type: "model_answer", title: "Model story (B/passing)", content: "Last Saturday, Anna went to the park to play football. First, she met her friends and they started the game. Then, it began to rain heavily. Finally, they all ran home and watched a movie together. They had a fun day! (40 words)" },
                { type: "band_descriptors", title: "How examiners score (0-5)", content: "Content (3 bullets covered), Communicative Achievement (right register), Organisation (clear flow), Language (A2 grammar/vocab accuracy)." },
                { type: "common_mistakes", title: "Avoid", content: "Under 25 words (lose marks). Missing a bullet point. Wrong tense in story (must be past simple). No greeting/closing." }
            ],
            next_steps: ["Write 5 emails on different topics", "Write 5 picture stories from prompts"]
        },

        {
            id: "cam-ket-listening",
            exam: "ket",
            cefr: "A2",
            skill: "listening",
            title: "KET Listening — 5 Parts in 30 min",
            subtitle: "Note-taking for short conversations",
            duration_min: 60,
            paper_overview: { time: "30 min (incl. 8 min transfer)", parts: 5, questions: 25, marks: "25% of total" },
            objectives: [
                "Recognize 5 part formats",
                "Use prediction before audio plays",
                "Take notes without missing the next question"
            ],
            parts_breakdown: [
                { part: 1, name: "5 short dialogues, 3 pictures each", questions: 5, time: "5 min", strategy: "Look at pictures BEFORE audio. Listen for the chosen item, not the rejected ones.", example: "What did he buy? A) apple B) bread C) milk" },
                { part: 2, name: "Long conversation, gap-fill", questions: 5, time: "5 min", strategy: "Read gaps first. Predict word type (number, name, time).", example: "Time of meeting: ___ pm" },
                { part: 3, name: "Long conversation, 3-option MC", questions: 5, time: "6 min", strategy: "Underline key words in question. Watch for distractors.", example: "What does Tom suggest? A) cinema B) cafe C) park" },
                { part: 4, name: "5 short MC dialogues", questions: 5, time: "6 min", strategy: "Read all options first. Listen for paraphrasing.", example: "Why is she late? A) traffic B) overslept C) phone" },
                { part: 5, name: "Long monologue, matching", questions: 5, time: "5 min", strategy: "Match 5 items to 8 options. Cross out used options.", example: "Match person to gift" }
            ],
            sections: [
                { type: "template", title: "Note-taking template", content: "Q# | Keyword | Heard? | Answer | 1: bought, apple, A | 2: time, 7pm, 7. Use abbreviations: w/ (with), b/c (because), -> (leads to)" },
                { type: "strategy", title: "Prediction technique", content: "BEFORE Part 2 audio: read gaps and write expected word class above each gap (NUM, NAME, TIME, PLACE). This primes your brain." },
                { type: "tips", title: "Top tips", content: "1) Audio plays TWICE — relax on first listen. 2) Spell names/places carefully. 3) Numbers: write digits, not words. 4) Don't change correct answers without good reason." },
                { type: "common_mistakes", title: "Avoid", content: "Choosing first option you hear (often a distractor). Misspelling common words. Leaving answers blank — always guess A2 vocabulary." }
            ],
            next_steps: ["Listen to 3 KET sample tests", "Practice numbers/dates dictation daily"]
        },

        {
            id: "cam-ket-speaking",
            exam: "ket",
            cefr: "A2",
            skill: "speaking",
            title: "KET Speaking — Paired Test",
            subtitle: "8-10 min with a partner, 2 parts",
            duration_min: 60,
            paper_overview: { time: "8-10 min", parts: 2, questions: "Personal Q + photo discussion", marks: "25% of total" },
            objectives: [
                "Answer personal questions confidently",
                "Discuss preferences with a partner",
                "Use simple connectors and fillers naturally"
            ],
            parts_breakdown: [
                { part: 1, name: "Interview (3-4 min)", questions: "8-10 personal Qs", time: "4 min", strategy: "Extend answers — don't say just yes/no. Add a reason or example.", example: "Q: Do you like sports? A: Yes, I love football. I play every Saturday with my friends." },
                { part: 2, name: "Collaborative task (5-6 min)", questions: "Discuss 5 pictures with partner", time: "5 min", strategy: "Take turns, ask partner's opinion, agree/disagree politely, choose one option together.", example: "Which is the best gift? -> I think the book is best because she likes reading. What do you think?" }
            ],
            sections: [
                { type: "intro", title: "What examiners look for", content: "Grammar/Vocabulary, Pronunciation, Interactive Communication, Global Achievement. Each scored 0-5." }
            ],
            common_phrases: [
                "Personal info: My name is..., I'm from..., I live in...",
                "Likes: I really like..., I love..., My favourite ... is...",
                "Dislikes: I don't like..., I'm not keen on...",
                "Reasons: ...because..., ...so...",
                "Opinion: I think..., In my opinion..., For me...",
                "Agreeing: Yes, I agree, That's a good idea, Me too",
                "Disagreeing politely: I'm not sure, I prefer..., Maybe but...",
                "Asking partner: What about you?, Do you agree?, What do you think?",
                "Time: First..., Then..., After that..., Finally...",
                "Filling pause: Well..., Let me think..., That's a good question"
            ],
            next_steps: ["Record yourself answering 20 personal Qs", "Practice pair task with classmate using picture sets"]
        }

        // ============================================================
        // PET (B1 PRELIMINARY) — 4 LESSONS
        // ============================================================

        {
            id: "cam-pet-reading-uoe",
            exam: "pet",
            cefr: "B1",
            skill: "reading-uoe",
            title: "PET Reading — 6 Parts in 45 min",
            subtitle: "Skim, scan, and select with precision",
            duration_min: 60,
            paper_overview: { time: "45 min", parts: 6, questions: 32, marks: "25% of total" },
            objectives: [
                "Master 6 PET Reading part formats",
                "Allocate ~7 min per part with checking buffer",
                "Distinguish gist vs detail questions",
                "Identify writer's attitude / opinion"
            ],
            parts_breakdown: [
                { part: 1, name: "Signs/short messages MC", questions: 5, time: "5 min", strategy: "Read each text fully — meaning often hinges on one verb. Pick A/B/C closest in meaning.", example: "'Please let staff know if you require help' = staff will assist if asked" },
                { part: 2, name: "Multiple matching (5 people, 8 texts)", questions: 5, time: "8 min", strategy: "Underline ALL requirements per person. Match only if ALL conditions met.", example: "Wants beach + cheap + family hotel" },
                { part: 3, name: "Long text MC", questions: 5, time: "10 min", strategy: "Read full text first for gist, then 5 questions in order. Watch for opinion vs fact.", example: "What does the writer think about... ?" },
                { part: 4, name: "Gapped text (sentence insertion)", questions: 5, time: "8 min", strategy: "Read context BEFORE and AFTER gap. Use referencing words (it, this, however) to confirm.", example: "Insert sentence with 'this idea' -> previous gap mentions an idea" },
                { part: 5, name: "Cloze MC (vocabulary)", questions: 6, time: "7 min", strategy: "Word collocations & phrasal verbs. Try each option in the gap, read aloud.", example: "He ___ in love with her -> fell (collocation)" },
                { part: 6, name: "Open cloze (grammar)", questions: 6, time: "7 min", strategy: "One word per gap — articles, prepositions, auxiliaries, relatives, comparatives.", example: "She is taller ___ her brother -> than" }
            ],
            sections: [
                { type: "strategy", title: "Two-pass approach", content: "Pass 1: answer confident questions (~30 min). Pass 2: revisit uncertain ones (~10 min). Pass 3: check (~5 min). Never leave blanks." },
                { type: "tips", title: "Top tips", content: "1) Watch synonyms/paraphrases in matching. 2) In Part 4 check pronouns/connectors. 3) For Part 5 think collocations not just meaning. 4) Part 6: contractions count as one word." },
                { type: "common_mistakes", title: "Avoid", content: "Choosing option that uses same word as text (often a trap). Inserting wrong sentence in Part 4 due to surface-level match. Two words in Part 6 open cloze." }
            ],
            next_steps: ["Daily 1 PET practice text", "Phrasal verbs flashcards (B1 list)"]
        },

        {
            id: "cam-pet-writing",
            exam: "pet",
            cefr: "B1",
            skill: "writing",
            title: "PET Writing — Email + Article/Story",
            subtitle: "100 words each, two strong tasks",
            duration_min: 60,
            paper_overview: { time: "45 min", parts: 2, questions: 2, marks: "25% of total. Each task ~100 words." },
            objectives: [
                "Write a structured 100-word email response",
                "Write an article OR story (student choice)",
                "Use B1 connectors and varied tenses"
            ],
            parts_breakdown: [
                { part: 1, name: "Email response (100 words)", questions: 1, time: "20 min", strategy: "Respond to email + 4 prompts in margins. Cover ALL 4 notes in order. Match register of received email.", example: "Email from friend + 4 notes: Thank, Suggest, Ask, Promise" },
                { part: 2, name: "Article OR Story (100 words)", questions: 1, time: "20 min", strategy: "ARTICLE: engaging title + 3 paragraphs + opinion. STORY: starts with given sentence, past tenses, clear ending.", example: "Article: 'Is technology good for children?' OR Story starting 'When I opened the door, I couldn't believe my eyes.'" }
            ],
            sections: [
                { type: "template", title: "Email template", content: "Hi [Name], Thanks for your email about [topic]. [Note 1 response] [Note 2 response]. As for [Note 3] — [response]. Finally, [Note 4 response]. Looking forward to hearing from you. Best wishes, [Name]" },
                { type: "model_answer", title: "Model email (B1 passing)", content: "Hi Jamie, Thanks for inviting me to the camping trip — sounds amazing! I'd love to come on Saturday. I think we should bring a small tent and warm sleeping bags because nights can be cold. Could you tell me what time we are leaving? I'll bring sandwiches and snacks for everyone. I can't wait! Let me know about the timing soon. Best wishes, Sam (about 100 words)" },
                { type: "template", title: "Article template", content: "Title: [Engaging question or statement]. P1: Hook + state opinion. P2: Reason 1 with example. P3: Reason 2 with example. P4: Conclusion + invitation to reader. Use rhetorical questions: 'Don't you think...?'" },
                { type: "model_answer", title: "Model article (B1 passing)", content: "Title: Is reading still important? In my opinion, reading is more important than ever. First, books help us learn new words and ideas. When I read a novel, I always discover something new about the world. Second, reading is a great way to relax. After a busy day at school, I love sitting with a good story. Although phones are everywhere, books still offer something special. Why not pick one up today? (about 100 words)" },
                { type: "template", title: "Story template (uses given first line)", content: "[Given sentence]. Then [past simple action]. Suddenly, [twist with past continuous]. After that, [reaction]. In the end, [resolution + feeling]." },
                { type: "common_mistakes", title: "Avoid", content: "Missing one of the 4 notes in email. Wrong register (too formal with friend). Not using past tenses in story. Less than 100 words (lose Content marks)." }
            ],
            next_steps: ["Write 5 emails responding to friend prompts", "Compare your articles with model answers"]
        },

        {
            id: "cam-pet-listening",
            exam: "pet",
            cefr: "B1",
            skill: "listening",
            title: "PET Listening — 4 Parts, 36 min",
            subtitle: "Detail, gist, attitude, gap-fill",
            duration_min: 60,
            paper_overview: { time: "36 min", parts: 4, questions: 25, marks: "25% of total" },
            objectives: [
                "Distinguish between 4 part task types",
                "Develop confident note-taking shorthand",
                "Recognize paraphrasing and distractors"
            ],
            parts_breakdown: [
                { part: 1, name: "7 short recordings, picture MC", questions: 7, time: "10 min", strategy: "Look at all 3 pictures BEFORE audio. Note what's different between options.", example: "What time does the train leave? Pictures show 3 clocks." },
                { part: 2, name: "Long monologue, MC", questions: 6, time: "10 min", strategy: "Read all 6 questions FIRST. Underline question keywords. Listen for paraphrases.", example: "Speaker about a holiday — questions on cost, weather, food, etc." },
                { part: 3, name: "Long monologue, gap-fill", questions: 6, time: "8 min", strategy: "Read text & predict word type per gap. Words in audio appear in same order as gaps.", example: "Talk about an event — fill in date, location, ticket price" },
                { part: 4, name: "Interview, MC", questions: 6, time: "8 min", strategy: "Watch for opinion shifts ('but', 'however', 'actually'). Final answer often comes after a hesitation.", example: "Interview with athlete — Qs about training, motivation, future" }
            ],
            sections: [
                { type: "template", title: "Part 3 note-taking template", content: "Gap | Word type | Prediction | Heard | 1: NUM | how many | 250 | 2: PLACE | where | London | 3: TIME | when | 7:30pm" },
                { type: "strategy", title: "Distractor awareness", content: "Speakers often mention wrong answers FIRST, then correct themselves. Listen for: 'I thought... but actually...', 'No, wait...', 'I changed my mind'." },
                { type: "tips", title: "Top tips", content: "1) Spelling matters in Part 3 — practice numbers/dates. 2) Don't write more than the limit (usually 1-3 words). 3) First listen = answers; second listen = check. 4) Use the pause time wisely to read ahead." },
                { type: "common_mistakes", title: "Avoid", content: "Writing exact word from question (rarely correct). Spelling errors on common words (Wednesday, February). Leaving blanks — always guess plausibly." }
            ],
            next_steps: ["Daily dictation practice (numbers + dates)", "1 full PET listening test per week"]
        },

        {
            id: "cam-pet-speaking",
            exam: "pet",
            cefr: "B1",
            skill: "speaking",
            title: "PET Speaking — 4 Parts, 12-17 min",
            subtitle: "Interview, photo, collaboration, discussion",
            duration_min: 60,
            paper_overview: { time: "12-17 min (paired)", parts: 4, questions: "Personal + photo + decision-making + discussion", marks: "25% of total" },
            objectives: [
                "Describe a photo for 1 minute",
                "Collaborate on a decision-making task",
                "Discuss broader themes confidently"
            ],
            parts_breakdown: [
                { part: 1, name: "Interview (2-3 min)", questions: "Personal info Qs", time: "3 min", strategy: "Extend with reasons + examples. Use full sentences, not single words.", example: "Q: What do you do? A: I'm a student at... I'm studying... because..." },
                { part: 2, name: "Individual photo description (1 min each)", questions: "1 photo", time: "2 min", strategy: "Describe location, people, action, atmosphere. Use 'There is/are', present continuous, prepositions.", example: "In this photo I can see a family in a park. They are having a picnic..." },
                { part: 3, name: "Collaborative task (2-3 min)", questions: "Discuss 5 pictures + decide", time: "3 min", strategy: "Comment on each option, ask partner's view, justify, agree on final choice.", example: "Best gift for a teacher — discuss 5 options together" },
                { part: 4, name: "Discussion (3 min)", questions: "Broader theme follow-up", time: "3 min", strategy: "Give opinion + reason + example. Build on partner's ideas.", example: "Do you think gifts are important? Why?" }
            ],
            sections: [
                { type: "intro", title: "Examiner criteria", content: "Grammar & Vocabulary, Discourse Management, Pronunciation, Interactive Communication, Global Achievement. Scored 0-5 each." }
            ],
            common_phrases: [
                "Photo description: In this photo I can see..., In the foreground..., In the background..., On the left/right..., It looks like..., I'd say...",
                "Speculation: It could be..., It might be..., Maybe they are..., They seem to be...",
                "Suggesting: How about...?, Why don't we...?, We could..., What if we...?",
                "Asking opinion: What do you think about...?, Do you agree?, What's your view?",
                "Agreeing: Absolutely, I totally agree, You're right, That's a great point",
                "Disagreeing politely: I see what you mean, but..., I'm not sure I agree..., I have a different idea...",
                "Giving reasons: The reason is..., This is because..., For example..., Such as...",
                "Concluding: So I think we should choose..., Let's go with..., We've agreed on...",
                "Hesitation fillers: Well..., Let me think..., That's a difficult question",
                "Linking: Also, In addition, Moreover, On the other hand, However"
            ],
            next_steps: ["Photo description drills (1 min recordings)", "Mock decision-making tasks with partner"]
        },

        // ============================================================
        // FCE (B2 FIRST) — 4 LESSONS
        // ============================================================

        {
            id: "cam-fce-reading-uoe",
            exam: "fce",
            cefr: "B2",
            skill: "reading-uoe",
            title: "FCE Reading & Use of English — 7 Parts",
            subtitle: "75 min, 52 questions, 40% of total",
            duration_min: 90,
            paper_overview: { time: "75 min", parts: 7, questions: 52, marks: "40% of total" },
            objectives: [
                "Master 7 R&UoE part formats and timing",
                "Apply word-formation rules systematically",
                "Use key word transformation techniques",
                "Identify writer's tone and inference"
            ],
            parts_breakdown: [
                { part: 1, name: "Multiple choice cloze (vocab)", questions: 8, time: "8 min", strategy: "Test each option for collocation, idiom, fixed phrase. Often 2 options have correct meaning but only 1 collocates.", example: "He ___ a deep impression -> made (collocation)" },
                { part: 2, name: "Open cloze (grammar)", questions: 8, time: "8 min", strategy: "Grammar words only — articles, pronouns, prepositions, modals, comparatives, conjunctions.", example: "She ran out ___ time -> of" },
                { part: 3, name: "Word formation", questions: 8, time: "8 min", strategy: "Read whole sentence — decide noun/verb/adj/adv. Watch for negative prefixes (un-, dis-, in-) and plurals.", example: "The ___ was huge (DIFFER) -> difference" },
                { part: 4, name: "Key word transformation", questions: 6, time: "12 min", strategy: "2-5 words including the given word UNCHANGED. Keep meaning. Each word counts (contractions = 2).", example: "It's such a long time since I saw him. (NOT) -> I haven't seen him for a long time" },
                { part: 5, name: "Long text MC (6 Qs)", questions: 6, time: "12 min", strategy: "Read text once for gist, then questions in order. Inference questions need reading 'between lines'.", example: "What does the writer imply about... ?" },
                { part: 6, name: "Gapped text (sentence insertion)", questions: 6, time: "12 min", strategy: "Use cohesion clues: pronouns, time markers, demonstratives. One extra sentence not used.", example: "Sentence with 'this approach' refers to a method just mentioned" },
                { part: 7, name: "Multiple matching (10 Qs)", questions: 10, time: "15 min", strategy: "Read questions FIRST, scan text for keywords/synonyms. Texts can be reused.", example: "In which section does the writer mention... ?" }
            ],
            sections: [
                { type: "strategy", title: "UoE timing (Parts 1-4)", content: "Aim for 36 min on UoE (4-12 min each). Reading takes 39 min. Always check word count in transformations." },
                { type: "template", title: "Word formation map", content: "Noun: -tion, -ment, -ity, -ness, -er. Verb: -ise/-ize, -ate, -en, -ify. Adj: -able, -ful, -less, -ous, -ive. Adv: -ly. Negatives: un-, in-, im-, dis-, mis-." },
                { type: "tips", title: "Key word transformation drills", content: "Common transformations: passive voice, reported speech, conditionals, comparatives, modals (must/have to), wish + past simple, would rather, used to. Practice 5 daily." },
                { type: "common_mistakes", title: "Avoid", content: "Changing the given word in Part 4. Forgetting negative prefix in Part 3. Skipping Part 7 (10 Qs = lots of marks). Wrong word class in Part 3." }
            ],
            next_steps: ["10 transformations daily", "FCE wordlist: 100 word families per week"]
        },

        {
            id: "cam-fce-writing",
            exam: "fce",
            cefr: "B2",
            skill: "writing",
            title: "FCE Writing — Essay + Choice",
            subtitle: "80 min, 2 tasks, 140-190 words each",
            duration_min: 90,
            paper_overview: { time: "80 min", parts: 2, questions: "Part 1 essay (compulsory) + Part 2 choice (article/email/letter/report/review)", marks: "20% of total. 140-190 words each." },
            objectives: [
                "Plan and write a balanced opinion essay",
                "Adapt register for different task types",
                "Use B2 cohesion: linkers, referencing, paraphrase"
            ],
            parts_breakdown: [
                { part: 1, name: "Essay (compulsory, 140-190 words)", questions: 1, time: "40 min", strategy: "Title + 2 given points + 1 your own idea. Balanced view OR opinion. 4-paragraph structure.", example: "Should young people learn 2 languages at school? Points: time, jobs, your idea" },
                { part: 2, name: "Choice (article/email/letter/report/review, 140-190 words)", questions: 1, time: "40 min", strategy: "Choose the type you know best. Match register to audience. Article = engaging; report = headings + neutral.", example: "Review: a film you saw recently for a magazine" }
            ],
            sections: [
                { type: "template", title: "Essay 4-paragraph plan", content: "P1 INTRO: paraphrase question + thesis. P2 POINT 1 + reason + example. P3 POINT 2 + reason + example. P4 YOUR IDEA + conclusion. Use linkers: Firstly, Moreover, On the other hand, In conclusion." },
                { type: "model_answer", title: "Model essay (B2 passing)", content: "TITLE: Should schools teach two foreign languages? In today's globalised world, the question of whether students should study two foreign languages at school is increasingly relevant. Firstly, learning two languages can open more career opportunities. Many international companies value employees who speak several languages, which can lead to better job prospects. Secondly, however, mastering two languages requires significant time and effort. Students may struggle to balance language study with other subjects, possibly affecting their overall performance. In my view, the most important factor is motivation. If students are genuinely interested, they will benefit from learning two languages; if not, focusing on one is wiser. Schools should therefore offer choice. (about 165 words)" },
                { type: "template", title: "Article template", content: "TITLE: question or hook. P1: Engage reader (rhetorical question / surprising fact). P2: Main point + example. P3: Second point or counter-view. P4: Personal conclusion + invitation to think. Tone: friendly, direct address ('you', 'we')." },
                { type: "model_answer", title: "Model review (B2 passing)", content: "TITLE: A movie that surprised me. Last weekend I watched 'The Quiet Place', and I have to admit it exceeded my expectations. The plot follows a family forced to live in silence after monsters attack the world. What makes the film special is its use of silence — the audience holds their breath alongside the characters. The acting, particularly by Emily Blunt, is outstanding and adds emotional depth. There are a few moments where the storyline feels unrealistic, but the tension keeps you hooked. Overall, I would highly recommend this movie to anyone who enjoys clever, thought-provoking thrillers. Just make sure you watch it somewhere quiet! (about 145 words)" },
                { type: "band_descriptors", title: "FCE Writing scales (0-5 each)", content: "Content: covers task fully. Communicative Achievement: register suits audience. Organisation: clear structure + linkers. Language: B2 vocab + grammar with attempts at complex structures." },
                { type: "common_mistakes", title: "Avoid", content: "Ignoring own idea in essay. Wrong register (formal language in informal article). Under 140 / over 190 words. Memorised phrases that don't fit task. No clear paragraphing." }
            ],
            next_steps: ["1 essay + 1 choice task per week", "Build 'linker bank' for cohesion"]
        },

        {
            id: "cam-fce-listening",
            exam: "fce",
            cefr: "B2",
            skill: "listening",
            title: "FCE Listening — 4 Parts, 40 min",
            subtitle: "MC, gap-fill, multiple matching, MC interview",
            duration_min: 60,
            paper_overview: { time: "40 min", parts: 4, questions: 30, marks: "20% of total" },
            objectives: [
                "Identify gist, detail, opinion, attitude",
                "Develop fast keyword note-taking",
                "Predict content from instructions and Qs"
            ],
            parts_breakdown: [
                { part: 1, name: "8 short extracts, MC (3 options)", questions: 8, time: "10 min", strategy: "Each extract is independent. Read Q + 3 options BEFORE audio. Each extract plays twice.", example: "Why is the man calling? A) complain B) book C) ask for info" },
                { part: 2, name: "Long monologue, sentence completion (1-3 word answers)", questions: 10, time: "10 min", strategy: "Predict word type per gap. Words in audio appear in same order as gaps. Spell carefully.", example: "The lecture took place in ___ Hall. -> Maple" },
                { part: 3, name: "5 short monologues, multiple matching", questions: 5, time: "10 min", strategy: "Match 5 speakers to 8 options (3 unused). Listen for paraphrasing of options.", example: "Match each speaker's main feeling about their job" },
                { part: 4, name: "Long interview, MC (3 options)", questions: 7, time: "10 min", strategy: "Read all 7 Qs first. Underline keywords. Watch for distractors said early then corrected.", example: "Interview with author about new book — opinions on writing process" }
            ],
            sections: [
                { type: "template", title: "Part 2 note-taking grid", content: "Q | Predicted word class | Heard | Confirmed | 1: NOUN | book title | 2: NUM | 1995 | 3: ADJ | colourful" },
                { type: "strategy", title: "Distractor patterns", content: "Common traps: 1) Speaker mentions option but rejects it. 2) Half-correct wording (changes a key word). 3) Two speakers disagree — pick the one Q asks about. 4) Strong words ('always', 'never') often wrong." },
                { type: "tips", title: "Top tips", content: "1) Trust second listen for verification. 2) Spell common nouns correctly (lose marks). 3) Don't write more than 3 words. 4) Pencil tentative answers on first listen." },
                { type: "common_mistakes", title: "Avoid", content: "Repeating exact words from question. Misreading question word ('except', 'mainly'). Spelling errors. Picking option mentioned first (often distractor)." }
            ],
            next_steps: ["1 full FCE listening test weekly", "Daily 10-min BBC Learning English podcast"]
        },

        {
            id: "cam-fce-speaking",
            exam: "fce",
            cefr: "B2",
            skill: "speaking",
            title: "FCE Speaking — 4 Parts, 14 min",
            subtitle: "Interview, long turn, collaboration, discussion",
            duration_min: 60,
            paper_overview: { time: "14 min (paired)", parts: 4, questions: "Interview + photos + decision + discussion", marks: "20% of total" },
            objectives: [
                "Compare 2 photos for 1 minute (long turn)",
                "Negotiate decisions with a partner",
                "Engage in extended discussion on abstract topics"
            ],
            parts_breakdown: [
                { part: 1, name: "Interview (2 min)", questions: "Personal Qs", time: "2 min", strategy: "Extend with reasons + examples. Avoid memorised answers — examiners spot them.", example: "Q: How important is family? A: Family is essential because... For example, when I..." },
                { part: 2, name: "Long turn (1 min each, 2 photos)", questions: "Compare + answer Q", time: "4 min", strategy: "Compare BOTH photos throughout. Answer the Q at top of page. Use comparative language + speculation.", example: "Compare 2 photos of jobs. Q: Why might people choose these jobs?" },
                { part: 3, name: "Collaborative task (2-3 min)", questions: "5 prompts + decision", time: "3 min", strategy: "Discuss EACH option (2-3 min). Then 1 min to decide. Don't just agree — explore.", example: "Which 2 are best ways to relax? Discuss 5 options" },
                { part: 4, name: "Discussion (4 min)", questions: "Abstract Qs related to Part 3 theme", time: "4 min", strategy: "Develop ideas with reasons + examples. Engage with partner's points.", example: "Do you think people are too busy these days?" }
            ],
            sections: [
                { type: "intro", title: "Examiner criteria", content: "Grammar & Vocabulary (range + accuracy), Discourse Management (extended turns + cohesion), Pronunciation (intelligibility, stress, intonation), Interactive Communication. Scored 0-5 each." }
            ],
            common_phrases: [
                "Comparing photos: Both photos show..., Whereas the first..., the second..., One similarity is..., A clear difference is...",
                "Speculation: It looks as if..., They might be..., I'd guess that..., Perhaps they're..., Judging by their faces...",
                "Opinion strong: I'm convinced that..., I strongly believe..., There's no doubt...",
                "Opinion soft: It seems to me..., I tend to think..., I'd say...",
                "Negotiation: Shall we start with...?, How about we look at...?, Let's consider...",
                "Building on partner: That's a good point and..., Following on from what you said..., I see your point but...",
                "Disagreeing: I see it differently..., I'm not entirely convinced..., On the contrary...",
                "Examples: Take ... for instance, A good example would be..., If we look at...",
                "Concluding: So overall..., All things considered..., Weighing it up...",
                "Buying time: Hmm, that's an interesting question, Let me think for a moment, That's a tricky one"
            ],
            next_steps: ["Daily 1-min photo comparison drills", "Mock Part 3 negotiations with partner"]
        },

        // ============================================================
        // CAE (C1 ADVANCED) — 4 LESSONS
        // ============================================================

        {
            id: "cam-cae-reading-uoe",
            exam: "cae",
            cefr: "C1",
            skill: "reading-uoe",
            title: "CAE Reading & Use of English — 8 Parts",
            subtitle: "90 min, 56 questions, demanding precision",
            duration_min: 90,
            paper_overview: { time: "90 min", parts: 8, questions: 56, marks: "40% of total" },
            objectives: [
                "Master 8 R&UoE part formats at C1 level",
                "Handle complex word formation including suffix chains",
                "Tackle 3-paragraph multiple matching efficiently",
                "Read between the lines for tone and inference"
            ],
            parts_breakdown: [
                { part: 1, name: "MC cloze (vocab + collocation)", questions: 8, time: "8 min", strategy: "C1 collocations, idioms, dependent prepositions, phrasal verbs. Subtle differences between options.", example: "He took ___ of the opportunity -> advantage" },
                { part: 2, name: "Open cloze", questions: 8, time: "8 min", strategy: "Grammar focus + fixed phrases. Often relative clauses, modals, comparative structures, linkers.", example: "He works hard, ___ which he wouldn't succeed -> without" },
                { part: 3, name: "Word formation", questions: 8, time: "8 min", strategy: "May need TWO changes (negative prefix + suffix). Read FULL paragraph for sense.", example: "It was a complete ___ (UNDERSTAND) -> misunderstanding" },
                { part: 4, name: "Key word transformation (3-6 words)", questions: 6, time: "12 min", strategy: "Range of B2-C1 transformations. Watch fixed phrases, inversion, cleft sentences.", example: "Hardly had I arrived when... (NO SOONER) -> No sooner had I arrived than..." },
                { part: 5, name: "Long text MC (6 Qs)", questions: 6, time: "12 min", strategy: "Inference, attitude, purpose, reference. Read carefully — often two options seem possible.", example: "The writer's tone in paragraph 3 is best described as..." },
                { part: 6, name: "Cross-text multiple matching (4 short texts)", questions: 4, time: "10 min", strategy: "Identify each writer's opinion on shared topic. Match Q ('which writer agrees with X about Y?').", example: "Which writer shares B's view on remote work?" },
                { part: 7, name: "Gapped text (paragraphs)", questions: 6, time: "12 min", strategy: "Insert paragraphs (not just sentences). Use cohesion: pronouns, demonstratives, time/topic links.", example: "Paragraph beginning 'Such an approach...' refers back to method just mentioned" },
                { part: 8, name: "Multiple matching (10 Qs)", questions: 10, time: "20 min", strategy: "Read Qs first; scan text using paraphrased keywords. Sections can be reused.", example: "In which section is X first mentioned?" }
            ],
            sections: [
                { type: "strategy", title: "Time discipline", content: "UoE Parts 1-4: 36 min. Reading Parts 5-8: 54 min. Stick to plan — Part 8 (10 marks) often abandoned by panicking candidates." },
                { type: "template", title: "Cross-text matching grid (Part 6)", content: "Topic | Writer A | Writer B | Writer C | Writer D | Q1: agreement on X | + | - | + | ? | -> A & C agree" },
                { type: "tips", title: "Top tips", content: "1) Part 4: count words including contractions (don't = 2). 2) Part 3 often needs negative prefix — check sense. 3) Part 7: extra paragraph IS a distractor. 4) Mark uncertain answers + return." },
                { type: "common_mistakes", title: "Avoid", content: "Choosing literal matches in Part 8 (paraphrasing is the norm). Wrong word class in Part 3. Misreading question stem in Part 5 ('NOT', 'EXCEPT')." }
            ],
            next_steps: ["10 transformations daily (focus on inversions)", "C1 collocations dictionary (Macmillan)"]
        },

        {
            id: "cam-cae-writing",
            exam: "cae",
            cefr: "C1",
            skill: "writing",
            title: "CAE Writing — Essay + Choice",
            subtitle: "90 min, 220-260 words each",
            duration_min: 90,
            paper_overview: { time: "90 min", parts: 2, questions: "Part 1 essay (compulsory) + Part 2 choice (letter/proposal/report/review)", marks: "20% of total. 220-260 words each." },
            objectives: [
                "Argue from input texts with synthesis",
                "Adapt to formal task types (proposal, report)",
                "Use C1 cohesion: nominalisation, participle clauses, hedging"
            ],
            parts_breakdown: [
                { part: 1, name: "Essay from prompt + 3 ideas (compulsory, 220-260w)", questions: 1, time: "45 min", strategy: "Choose 2 of 3 given points. Discuss BOTH. Reach reasoned conclusion. Don't summarise — evaluate.", example: "What are the most effective ways to encourage reading among teenagers? Choose 2 from: schools, technology, role models" },
                { part: 2, name: "Choice (letter/proposal/report/review, 220-260w)", questions: 1, time: "45 min", strategy: "Match TASK to your strength. Proposal = future + recommend; Report = past + analyse; Review = evaluate + recommend.", example: "Proposal to manager about improving staff training" }
            ],
            sections: [
                { type: "template", title: "Essay 4-paragraph plan (CAE)", content: "P1 INTRO: paraphrase task + thesis + 'this essay will'. P2 POINT 1: state + reasoned argument + counter + concession. P3 POINT 2: same structure. P4 CONCLUSION: synthesise + evaluate which is more effective + final stance. Linkers: nevertheless, by the same token, in light of, while it may be argued that..." },
                { type: "model_answer", title: "Model essay (C1 passing)", content: "Encouraging reading among teenagers has become a pressing concern in our digital age. While schools, technology and role models all play a role, this essay will argue that schools and role models offer the most lasting impact. Schools, on the one hand, can foster a culture of reading through carefully curated reading lists and dedicated reading time. By exposing students to diverse genres in supportive environments, schools build foundational habits. Critics may argue that compulsory reading breeds resentment, but skilled teachers can mitigate this by allowing student choice. Role models, on the other hand, exert a more subtle yet powerful influence. When teenagers see admired figures — parents, teachers, celebrities — engaged in reading, they internalise it as desirable. Studies consistently show that homes with visible readers produce more avid young readers. In conclusion, although technology offers convenient access to texts, sustained reading habits are best cultivated through structured school exposure combined with the modelling of trusted adults. Without these human elements, no app, however sophisticated, can replicate the deeper engagement reading demands. (about 235 words)" },
                { type: "template", title: "Proposal template", content: "TITLE / TO/FROM/DATE/SUBJECT. INTRO: Aim — what proposal addresses. CURRENT SITUATION: brief background. PROPOSED CHANGES: 2-3 sub-headings, each with rationale. BENEFITS: itemised. CONCLUSION + RECOMMENDATION. Use formal modals: would, could, recommend that + subjunctive." },
                { type: "model_answer", title: "Model proposal (C1 passing)", content: "TO: Mr Patel, Operations Manager. FROM: Sara Lin, Team Leader. SUBJECT: Improving Customer Service Training. AIM This proposal sets out three changes to enhance the effectiveness of our current customer service training programme, in light of recent feedback. CURRENT SITUATION New staff complete a one-week induction, but exit surveys reveal limited confidence handling complaints. PROPOSED CHANGES — Mentoring scheme: pair each new hire with an experienced colleague for the first month, ensuring real-time guidance. — Scenario workshops: replace passive lectures with role-play sessions covering high-pressure cases. — Quarterly refreshers: short follow-up sessions to maintain skills and share emerging issues. BENEFITS These measures would not only build practical competence but also strengthen team cohesion and reduce staff turnover, a persistent challenge. RECOMMENDATION I therefore recommend piloting the mentoring and workshop changes from next quarter, with refreshers introduced once initial feedback has been reviewed. Should you wish, I would be glad to outline implementation costs in further detail. (about 230 words)" },
                { type: "band_descriptors", title: "CAE Writing scales (0-5 each)", content: "Content (task fully addressed). Communicative Achievement (consistent register, audience aware). Organisation (varied cohesion, clear progression). Language (range of structures + sophisticated vocabulary; minor errors don't impede)." },
                { type: "common_mistakes", title: "Avoid", content: "Discussing only one of two required points. Wrong genre conventions (review without recommendation, proposal without future suggestions). Memorised idioms forced into wrong contexts. Over/under word count." }
            ],
            next_steps: ["Weekly: 1 essay + 1 task type from choice", "Build genre-conventions checklist"]
        },

        {
            id: "cam-cae-listening",
            exam: "cae",
            cefr: "C1",
            skill: "listening",
            title: "CAE Listening — 4 Parts, 40 min",
            subtitle: "Inference, gist, attitude at C1",
            duration_min: 60,
            paper_overview: { time: "40 min", parts: 4, questions: 30, marks: "20% of total" },
            objectives: [
                "Track speaker attitude and implication",
                "Extract precise data despite paraphrasing",
                "Match nuanced opinions across speakers"
            ],
            parts_breakdown: [
                { part: 1, name: "3 short extracts, 2 MC Qs each (6 Qs)", questions: 6, time: "10 min", strategy: "Each extract has 2 Qs. Read both BEFORE listening. Watch for attitude vs detail Qs.", example: "Q1: What does the woman think? Q2: What do they agree on?" },
                { part: 2, name: "Long monologue, sentence completion", questions: 8, time: "10 min", strategy: "Predict word class. Words in same order as gaps. Often 1-word answer.", example: "The species was first observed in ___ -> Madagascar" },
                { part: 3, name: "Long interview, MC (6 Qs)", questions: 6, time: "10 min", strategy: "Read 6 Qs first. Watch for distractors said but rejected ('I used to think... but actually...').", example: "Interview with film director — Qs on inspiration, challenges, opinion" },
                { part: 4, name: "5 short monologues, multiple matching (DOUBLE — 2 tasks of 5 Qs)", questions: 10, time: "10 min", strategy: "TWO tasks per speaker — listen for BOTH (e.g. main point + speaker feeling). Read both Q sets first.", example: "Task 1: speaker's job. Task 2: how they feel about it" },
                { part: 4, name: "(continued — same audio, double matching)", questions: 0, time: "Included above", strategy: "Use 2 columns of notes per speaker.", example: "Sp1: doctor / frustrated; Sp2: artist / fulfilled" }
            ],
            sections: [
                { type: "template", title: "Part 4 dual-matching grid", content: "Speaker | Task 1 (job) | Task 2 (feeling) | Sp1: A doctor | F frustrated | Sp2: B artist | G fulfilled" },
                { type: "strategy", title: "Attitude detection", content: "Listen for: tone (sarcasm, enthusiasm), hedges ('I suppose', 'sort of'), strong stance ('absolutely', 'no question'). Adverbs reveal attitude: surprisingly, regrettably, ironically." },
                { type: "tips", title: "Top tips", content: "1) Part 4 double task — don't try to fill both on first listen; pick one. 2) Spell technical/place names carefully in Part 2. 3) C1 distractors are subtle — don't pick first match. 4) Use second listen for verification." },
                { type: "common_mistakes", title: "Avoid", content: "Choosing option that re-uses speaker's exact words (often distractor at C1). Mis-spelling on technical terms. Skipping Part 4 second task — both score equally." }
            ],
            next_steps: ["Daily 15-min TED talk + summary", "1 full CAE listening test weekly"]
        },

        {
            id: "cam-cae-speaking",
            exam: "cae",
            cefr: "C1",
            skill: "speaking",
            title: "CAE Speaking — 4 Parts, 15 min",
            subtitle: "Sustained interaction at C1",
            duration_min: 60,
            paper_overview: { time: "15 min (paired)", parts: 4, questions: "Interview + long turn + collab + discussion", marks: "20% of total" },
            objectives: [
                "Sustain a 1-minute long turn comparing photos",
                "Negotiate complex decisions over 3 minutes",
                "Develop abstract arguments with nuance"
            ],
            parts_breakdown: [
                { part: 1, name: "Interview (2 min)", questions: "Personal Qs", time: "2 min", strategy: "Develop answers — show range. Avoid clearly memorised lines.", example: "Q: How has your hometown changed? A: Significantly. When I was younger... whereas now..." },
                { part: 2, name: "Long turn (1 min each, 3 photos to choose 2)", questions: "Compare 2 + answer Q", time: "4 min", strategy: "Choose 2 of 3 photos. Compare CONSISTENTLY. Speculate + answer Q. After partner finishes, comment briefly.", example: "Why might these people have chosen these activities?" },
                { part: 3, name: "Collaborative task (3 min)", questions: "5 prompts + decision", time: "3 min", strategy: "Discuss EACH prompt deeply (2 min). Then decide (1 min). Don't rush.", example: "Discuss factors that make a successful business; choose 2 most important" },
                { part: 4, name: "Discussion (5 min)", questions: "Abstract Qs related to Part 3 theme", time: "5 min", strategy: "Develop with reasons + examples + counter-views. Engage partner ideas.", example: "How important is luck in success? Has the meaning of success changed?" }
            ],
            sections: [
                { type: "intro", title: "Examiner criteria", content: "Grammar & Vocabulary (range + accuracy at C1), Discourse Management (extended, coherent contributions), Pronunciation (intelligible + natural stress/intonation), Interactive Communication (initiate, develop, respond)." }
            ],
            common_phrases: [
                "Comparing: Both images depict..., A striking difference is..., Whereas ... in contrast..., One thing they share is...",
                "Speculation: I'd hazard a guess that..., It strikes me as..., Conceivably..., It could well be that...",
                "Hedging: To some extent..., Up to a point..., One might argue..., Arguably...",
                "Strong opinion: I'm absolutely convinced..., Without question..., There's no escaping the fact that...",
                "Nuanced view: It depends on..., On balance..., Taking everything into account..., While it's true that..., it's also worth noting...",
                "Negotiating: How would you feel about..., Where do you stand on..., I can see merit in both...",
                "Building on partner: That ties in with..., Exactly the point I was going to make..., To pick up on what you said...",
                "Disagreeing diplomatically: I take a slightly different view..., I see where you're coming from, but..., I'd push back on that...",
                "Concluding: All things considered..., Weighing the arguments..., What it boils down to is...",
                "Buying time: That's a thought-provoking question, Let me give that some consideration, Off the top of my head..."
            ],
            next_steps: ["Daily 1-min long turn drills", "Weekly mock Part 3 + 4 with partner"]
        },

        // ============================================================
        // CPE (C2 PROFICIENCY) — 4 LESSONS
        // ============================================================

        {
            id: "cam-cpe-reading-uoe",
            exam: "cpe",
            cefr: "C2",
            skill: "reading-uoe",
            title: "CPE Reading & Use of English — 7 Parts",
            subtitle: "90 min, 53 questions, near-native precision",
            duration_min: 90,
            paper_overview: { time: "90 min", parts: 7, questions: 53, marks: "40% of total" },
            objectives: [
                "Master 7 R&UoE part formats at C2 level",
                "Handle abstract literary/academic registers",
                "Recognise irony, understatement, and rhetorical stance",
                "Achieve near-native precision in transformations"
            ],
            parts_breakdown: [
                { part: 1, name: "MC cloze", questions: 8, time: "8 min", strategy: "Subtle distinctions: idioms, semi-fixed expressions, register, dependent prepositions. Often only 1 collocate available.", example: "He paid scant ___ to the warning -> attention" },
                { part: 2, name: "Open cloze", questions: 8, time: "8 min", strategy: "Sophisticated grammar + linkers. Inversions, subjunctives, fixed phrases (e.g. 'no sooner', 'were it not').", example: "Were it ___ for his help, we would have failed -> not" },
                { part: 3, name: "Word formation", questions: 8, time: "8 min", strategy: "Compound forms, multi-step transformations, less common derivations. Read full paragraph for context.", example: "His ___ behaviour shocked everyone (RECONCILE) -> irreconcilable" },
                { part: 4, name: "Key word transformation (3-8 words)", questions: 6, time: "12 min", strategy: "Up to 8 words. Inversions, cleft sentences, advanced reporting structures, near-synonyms with shift.", example: "I really regret not studying harder. (WISH) -> I wish I had studied harder" },
                { part: 5, name: "Long text MC (6 Qs)", questions: 6, time: "12 min", strategy: "Literary or argumentative texts. Inference, tone, purpose, attitudes — nuanced options.", example: "What is the writer implying in lines 14-17?" },
                { part: 6, name: "Gapped text (paragraph insertion)", questions: 7, time: "12 min", strategy: "7 paragraphs to insert + 1 distractor. Cohesion via topic links, pronouns, demonstratives, lexical chains.", example: "Paragraph beginning 'Such resistance...' refers back to opposition mentioned" },
                { part: 7, name: "Multiple matching (10 Qs)", questions: 10, time: "20 min", strategy: "Read Qs first, scan sections for paraphrased ideas. Sections can be reused.", example: "In which section does the writer express scepticism about... ?" }
            ],
            sections: [
                { type: "strategy", title: "Time discipline", content: "UoE Parts 1-4: 36 min. Reading Parts 5-7: 44 min. Last 10 min for review. Don't get stuck on transformations." },
                { type: "template", title: "C2 transformation patterns", content: "Inversions: Hardly had..., Not until..., Only by..., Little did..., Under no circumstances... Cleft: It was X who..., What I need is..., The thing that... Subjunctive: were I to..., would rather you..." },
                { type: "tips", title: "Top tips", content: "1) Part 4 — count words including contractions. 2) Part 7 expects paraphrase, not direct match. 3) C2 distractors are intentionally close — second-guess only with text evidence. 4) Don't translate; think in English." },
                { type: "common_mistakes", title: "Avoid", content: "Choosing literal matches in Part 7. Wrong word class in Part 3. Inserting distractor paragraph. Adding/dropping the keyword in Part 4 transformations." }
            ],
            next_steps: ["10 C2 transformations daily (focus inversions + cleft)", "Weekly: 1 broadsheet article + summary"]
        },

        {
            id: "cam-cpe-writing",
            exam: "cpe",
            cefr: "C2",
            skill: "writing",
            title: "CPE Writing — Essay + Choice",
            subtitle: "90 min, essay 240-280w + choice 280-320w",
            duration_min: 90,
            paper_overview: { time: "90 min", parts: 2, questions: "Part 1 essay (240-280w) + Part 2 choice (article/letter/report/review, 280-320w)", marks: "20% of total" },
            objectives: [
                "Synthesise two source texts into a coherent essay",
                "Adapt to highly formal task types",
                "Use C2 stylistic features: nominalisation, hedging, rhetorical devices"
            ],
            parts_breakdown: [
                { part: 1, name: "Essay summarising 2 source texts (240-280w)", questions: 1, time: "45 min", strategy: "Read both texts. Identify 2 key points from EACH. Summarise + EVALUATE. Don't just paraphrase — engage critically.", example: "Two texts about technology in education. Summarise key points + give your own evaluation." },
                { part: 2, name: "Choice: article, letter, report, review (280-320w)", questions: 1, time: "45 min", strategy: "Match to your strength. Letters often to editor/director. Reviews evaluate + recommend with sophistication.", example: "Letter to editor responding to article on cultural identity" }
            ],
            sections: [
                { type: "template", title: "Essay 4-paragraph plan (CPE)", content: "P1 INTRO: paraphrase + thesis + signal evaluation. P2 KEY POINT 1 (covering both texts' position) + critique. P3 KEY POINT 2 (contrasting view from texts) + critique. P4 EVALUATION + reasoned conclusion. Use: insofar as, given that, despite the fact that, paradoxically, all things considered." },
                { type: "model_answer", title: "Model essay (C2 passing)", content: "The two texts present contrasting yet complementary perspectives on the role of technology in modern education. While Text 1 celebrates digital tools as democratising agents, Text 2 raises concerns about depth of engagement, suggesting that conveniences can come at a cognitive cost. This essay will argue that, taken together, both views point to a need for thoughtful integration rather than wholesale adoption. Text 1 makes a compelling case that online platforms broaden access. Students in remote regions can now attend lectures from world-class universities — a transformation unthinkable a generation ago. However, Text 2 rightly counters that access alone is not learning. The author identifies a worrying decline in sustained reading and the kind of slow thinking complex subjects demand. The crux of the disagreement seems to lie in what one considers 'education' to be. If we view it merely as information transfer, technology has indeed levelled the playing field. If, however, we conceive of it as the cultivation of judgement, persistence, and critical inquiry, then the cautions of Text 2 deserve serious weight. In my view, the most defensible position is that technology should serve, not supplant, the rigour of traditional pedagogy. Used judiciously — to spark curiosity, broaden exposure, and enable feedback — it can amplify learning. Yet without disciplined frameworks and engaged teachers, the very tools that promise inclusion may, paradoxically, deepen disparities of intellectual depth. (about 260 words)" },
                { type: "template", title: "Letter to editor template (Part 2)", content: "ADDRESS / Date / Sir or Madam, OPENING: state article you are responding to + your stance. P2: Acknowledge merit in argument (concession). P3: Counter-argument with evidence/example. P4: Wider implications + call to action. CLOSING: Yours faithfully + name. Tone: formal, measured, persuasive." },
                { type: "model_answer", title: "Model letter (C2 passing)", content: "Sir or Madam, I am writing in response to your editorial of last Sunday, 'The Death of the High Street', which painted an unduly bleak picture of urban retail. While I share concerns about empty storefronts, the conclusion that town centres are beyond saving seems both premature and counter-productive. Your piece rightly highlights structural challenges: rising rents, the convenience of e-commerce, and shifting consumer habits. To dismiss the human dimension of physical shopping, however, is to miss the point. People do not visit high streets purely to buy; they go for chance encounters, sensory experience, and a sense of belonging that no algorithm has yet replicated. Several towns I have visited recently — Margate, Frome, Bristol's Stokes Croft — illustrate that decline can be reversed when councils invest in distinctive independent retailers, public spaces, and cultural programming. The recipe is hardly mysterious: make a place worth lingering in, and people will linger. There is a wider risk in narratives of inevitability: they discourage the very civic action that revitalisation requires. Local businesses, planners and residents need encouragement, not eulogies. I would urge your paper to feature the towns that are succeeding alongside those that are struggling, and to engage readers in the question of what we want our shared spaces to become. The high street is not, after all, a balance sheet; it is a public good. Yours faithfully, J. Morales (about 290 words)" },
                { type: "band_descriptors", title: "CPE Writing scales (0-5 each)", content: "Content (sophisticated handling of task). Communicative Achievement (consistent, appropriate register; reader sustained). Organisation (varied cohesion, paragraphing serves argument). Language (wide range of structures + vocab; errors only on rare ambitious attempts)." },
                { type: "common_mistakes", title: "Avoid", content: "Quoting source texts directly (paraphrase + integrate). Failing to evaluate (descriptive only). Forced idioms. Wrong genre conventions (review without recommendation). Word-count breaches." }
            ],
            next_steps: ["Weekly: 1 essay synthesising 2 sources + 1 choice task", "Read C2 model answers from Cambridge handbook"]
        },

        {
            id: "cam-cpe-listening",
            exam: "cpe",
            cefr: "C2",
            skill: "listening",
            title: "CPE Listening — 4 Parts, 40 min",
            subtitle: "Inference, irony, abstract argument",
            duration_min: 60,
            paper_overview: { time: "40 min", parts: 4, questions: 30, marks: "20% of total" },
            objectives: [
                "Track abstract academic and literary argument",
                "Detect irony, understatement, and tone",
                "Match nuanced opinions across speakers"
            ],
            parts_breakdown: [
                { part: 1, name: "4 short extracts, MC (8 Qs, 2 per extract)", questions: 8, time: "10 min", strategy: "2 Qs per extract on different aspects (gist, attitude, detail). Each extract plays twice.", example: "Extract: lecture clip. Q1: main point. Q2: speaker's attitude" },
                { part: 2, name: "Long monologue, sentence completion (1-3 word answers)", questions: 9, time: "10 min", strategy: "Predict word class. Words in order of gaps. Often technical/abstract vocabulary.", example: "Researchers found the species ___ in cold climates -> thrives" },
                { part: 3, name: "Long interview, MC (5 Qs)", questions: 5, time: "10 min", strategy: "Read 5 Qs first. C2 distractors paraphrase incorrectly or cite rejected views.", example: "What does the speaker imply about her early career?" },
                { part: 4, name: "5 short monologues, multiple matching (8 Qs total — Tasks 1 & 2)", questions: 8, time: "10 min", strategy: "TWO tasks per speaker. Listen for both, but commit to one task per listen. Re-listen for second.", example: "Task 1: speaker's profession. Task 2: their main concern" }
            ],
            sections: [
                { type: "template", title: "Part 4 dual-matching grid", content: "Speaker | Task 1 | Task 2 | Sp1: A scientist | F funding | Sp2: B writer | G recognition | (8 options each, 3 unused)" },
                { type: "strategy", title: "Tone & irony detection", content: "Listen for: laughing tone with negative words (sarcasm), pause before 'compliment' (insincerity), strong denials ('I'd hardly call it...'). Adverbs reveal: ostensibly, supposedly, allegedly." },
                { type: "tips", title: "Top tips", content: "1) Part 4 — pick ONE task per listen, switch on second. 2) Spell precisely — academic/scientific terms common. 3) C2 distractors paraphrase imperfectly — verify with text logic. 4) Stay focused; topics can be unfamiliar/abstract." },
                { type: "common_mistakes", title: "Avoid", content: "Choosing option that paraphrases speaker poorly but uses similar words. Mis-spelling on technical terms. Trying to do both Part 4 tasks simultaneously on first listen." }
            ],
            next_steps: ["Daily: BBC Radio 4 / academic podcast 20 min", "Weekly: 1 full CPE listening test"]
        },

        {
            id: "cam-cpe-speaking",
            exam: "cpe",
            cefr: "C2",
            skill: "speaking",
            title: "CPE Speaking — 3 Parts, 16 min",
            subtitle: "Sustained, sophisticated interaction",
            duration_min: 60,
            paper_overview: { time: "16 min (paired)", parts: 3, questions: "Interview + collab task + extended discussion", marks: "20% of total" },
            objectives: [
                "Sustain sophisticated argument across 16 min",
                "Engage with abstract concepts at C2",
                "Use rhetorical devices and stylistic range"
            ],
            parts_breakdown: [
                { part: 1, name: "Interview (2 min)", questions: "Personal Qs", time: "2 min", strategy: "Showcase range from the start. Develop with examples + nuance. Avoid memorised lines.", example: "Q: What's the best decision you've made? A: Probably... Looking back, what made it sound was..." },
                { part: 2, name: "Collaborative task with prompt cards (4 min)", questions: "Discuss prompts + reach decision", time: "4 min", strategy: "Read prompt aloud, develop each in turn, build on partner's ideas, reach reasoned conclusion. Don't rush to decide.", example: "Discuss factors influencing public trust in institutions" },
                { part: 3, name: "Long turn (2 min each) + discussion (8 min)", questions: "Individual long turn + paired discussion", time: "10 min", strategy: "2-min monologue on a question linked to a written prompt. Then 4-min discussion on related broader Qs.", example: "Long turn: How important is privacy in the digital age? Discussion: Are some freedoms worth surrendering?" }
            ],
            sections: [
                { type: "intro", title: "Examiner criteria", content: "Grammar & Vocabulary (range + accuracy at C2), Discourse Management (extended, sophisticated, coherent), Pronunciation (clear with natural rhythm/stress), Interactive Communication (initiate, develop, sustain). Scored 0-5 each." }
            ],
            common_phrases: [
                "Framing: At the heart of this question lies..., What is at stake here is..., This raises a deeper issue of...",
                "Hedging at C2: To a large extent..., One might venture to suggest..., It would not be unreasonable to argue..., There's at least a case to be made that...",
                "Nuance: That said..., To be fair..., While not denying that..., There's a kernel of truth in...",
                "Strong stance: I'd go so far as to say..., Frankly..., Unequivocally..., Without reservation...",
                "Counter-argument: Yet one could equally argue..., A counter-view holds that..., This is, however, only half the story...",
                "Building on partner: Picking up your thread..., That dovetails with..., Pushing your idea further...",
                "Diplomatic disagreement: I'd take issue with that, gently..., I see things rather differently..., I'm not entirely persuaded by that line...",
                "Concluding: Weighing the considerations..., What it ultimately comes down to..., The crux of the matter is..., If pressed, I'd conclude that...",
                "Buying time elegantly: That deserves a moment's reflection, There's much to unpack there, Let me approach this differently...",
                "Rhetorical: Is it not the case that...?, How can we ignore...?, Surely we'd agree that..."
            ],
            next_steps: ["Daily 2-min long turn on abstract themes", "Weekly mock Part 3 with debate-style follow-up"]
        }

    ],

    band_descriptors_summary: {
        ket: {
            grade_a: "Pass with Distinction (C1 demonstrated)",
            grade_b: "Pass with Merit (B1 demonstrated)",
            grade_c: "Pass (A2 achieved — target)",
            level_a1: "A1 indicated (140-149)",
            below: "Below A1 (below 140)"
        },
        pet: {
            grade_a: "Pass with Distinction (B2 demonstrated)",
            grade_b: "Pass with Merit (B1+ strong)",
            grade_c: "Pass (B1 achieved — target)",
            level_a2: "A2 indicated (140-149)",
            below: "Below A2 (below 140)"
        },
        fce: {
            grade_a: "Grade A (C1 demonstrated, 180-190)",
            grade_b: "Grade B (B2 strong, 173-179)",
            grade_c: "Grade C (B2 achieved, 160-172 — target)",
            level_b1: "B1 indicated (140-159)",
            below: "Below B1 (below 140)"
        },
        cae: {
            grade_a: "Grade A (C2 demonstrated, 200-210)",
            grade_b: "Grade B (C1 strong, 193-199)",
            grade_c: "Grade C (C1 achieved, 180-192 — target)",
            level_b2: "B2 indicated (160-179)",
            below: "Below B2 (below 160)"
        },
        cpe: {
            grade_a: "Grade A (C2 with distinction, 220-230)",
            grade_b: "Grade B (C2 strong, 213-219)",
            grade_c: "Grade C (C2 achieved, 200-212 — target)",
            level_c1: "C1 indicated (180-199)",
            below: "Below C1 (below 180)"
        },
        scoring_overview: "Cambridge English Scale runs 80-230. Each paper scored equally. Average across 4 papers = candidate's scale score. Grade boundaries vary slightly per session.",
        speaking_criteria: "Grammar & Vocabulary, Discourse Management, Pronunciation, Interactive Communication, Global Achievement — each 0-5 across all exams.",
        writing_criteria: "Content, Communicative Achievement, Organisation, Language — each 0-5 across all exams."
    },

    teacher_notes: {
        suggested_pacing: "1 lesson per week = 20-week course, OR 2 lessons per week = 10-week intensive.",
        prerequisite_levels: {
            ket: "Students should be roughly A1+ entering",
            pet: "Students should have completed A2 / KET prep",
            fce: "Students should have completed B1 / PET prep",
            cae: "Students should have completed B2 / FCE prep",
            cpe: "Students should have completed C1 / CAE prep"
        },
        homework_pattern: "Each lesson: 1 timed practice paper section + reflection. Writing tasks rotated weekly with peer review.",
        mock_exam_schedule: "Full mock at week 4, 8, 12, 16, and 20 — track score progression on Cambridge scale.",
        resources: ["Official Cambridge handbooks per exam", "Cambridge English Practice Tests Plus series", "test-english.com for free practice", "writeandimprove.com for AI writing feedback"]
    }
};

if (typeof module !== 'undefined' && module.exports) {
    module.exports = cambridgeStrategyCurriculum;
}
