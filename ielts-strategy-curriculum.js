// ============================================================
// COHASSET IELTS STRATEGY CURRICULUM — 38 LESSONS
// Reading 8 + Listening 6 + Writing T1 Academic 6 + Writing T1 General 4
// + Writing T2 8 + Speaking 6 = 38 lessons
// Aligned to IELTS Academic & General Training, Bands 5.0–9.0
// CEFR B1–C2 — Author: Cohasset Language Center
// ============================================================

window.IELTS_CURRICULUM = {
    metadata: {
        total_lessons: 38,
        total_hours: 57,
        sections: {
            "reading": 8,
            "listening": 6,
            "writing-t1-academic": 6,
            "writing-t1-general": 4,
            "writing-t2": 8,
            "speaking": 6
        },
        band_coverage: "5.0–9.0",
        cefr_coverage: "B1–C2",
        version: "1.0",
        created: "2026-05-07",
        author: "Cohasset Language Center"
    },

    // ============================================================
    // READING — 8 LESSONS
    // ============================================================
    lessons: [

        // ---------- READING LESSON 1 ----------
        {
            id: "ielts-reading-1",
            section: "reading",
            band_target: "5.5-9.0",
            cefr: "B1-C2",
            title: "Skimming & Scanning Techniques",
            subtitle: "Master the two most fundamental reading speeds for IELTS Academic & GT.",
            duration_min: 50,
            objectives: [
                "Distinguish between skimming (gist) and scanning (specific information).",
                "Develop a 90-second skim routine that captures topic, structure, and tone.",
                "Apply scanning to locate names, numbers, dates, and keywords under 30 seconds.",
                "Build the 60-minute timing template (20 min per passage, 3 minutes per question on average)."
            ],
            sections: [
                {
                    type: "intro",
                    title: "Why these two skills decide your Reading band",
                    content: "IELTS Reading gives you 60 minutes to answer 40 questions across three passages of roughly 700–950 words each. There is no time to read every word. Candidates who score Band 7+ never read linearly the first time. They skim to build a mental map of the passage, then scan to lock down each question. Reading without these two gears is the single biggest reason students stall at Band 5.5–6.0."
                },
                {
                    type: "strategy",
                    title: "Skimming: the 90-second mental map",
                    content: "Skimming is reading for the GIST — what the text is about and how it is organised. Move your eyes quickly over: (1) the title and any subtitle, (2) the FIRST sentence of every paragraph, (3) the LAST sentence of paragraphs 1 and final paragraph, (4) any bold words, italics, capitalised proper nouns, or numbers. Do NOT stop at unknown vocabulary. By the end of 90 seconds you should be able to answer in your head: What is this passage about? What is the writer's stance — neutral, critical, supportive? Roughly how many sub-topics are there?"
                },
                {
                    type: "strategy",
                    title: "Scanning: hunting specific information",
                    content: "Scanning is the OPPOSITE — you ignore meaning and hunt for a target. Targets fall into 4 classes: (a) NUMBERS (years, percentages, ages), (b) PROPER NOUNS (capitalised — names, places, organisations), (c) UNUSUAL WORDS (technical terms, hyphenated compounds), (d) PARAPHRASED KEYWORDS. Use your finger or pen as a guide. Move your eyes in vertical sweeps, not horizontal lines. When the target appears, slow down and read the sentences around it — that's where the answer lives."
                },
                {
                    type: "example",
                    title: "Worked example — skim then scan",
                    content: "Imagine a passage titled 'The Return of Urban Beekeeping'. After skimming you know: paragraph A introduces the trend, B gives history, C explains hive economics, D describes hazards, E concludes with policy. Question: 'Which paragraph mentions a 2018 ban in Paris?' Step 1 — note the targets: '2018' (number) and 'Paris' (proper noun). Step 2 — scan only for those tokens; ignore everything else. Step 3 — when you find them in paragraph D, read the surrounding two sentences to confirm. Total time: under 40 seconds."
                },
                {
                    type: "tips",
                    title: "Timing template (60 minutes, 3 passages)",
                    content: "Minutes 0–1: skim Passage 1. Minutes 1–18: answer Passage 1 questions while scanning. Minute 19: transfer or check. Minutes 20–21: skim Passage 2. Minutes 21–38: answer Passage 2. Minute 39: check. Minutes 40–41: skim Passage 3 (longest, hardest). Minutes 41–58: answer Passage 3. Minutes 58–60: final check, fill any blanks with your best guess (NEVER leave blanks — there is no penalty for wrong answers in IELTS Reading)."
                },
                {
                    type: "common_mistakes",
                    title: "Mistakes that cost half a band",
                    content: "1) Reading the passage word-for-word before looking at questions — wastes 10 minutes. 2) Looking up unknown vocabulary — there is no dictionary in the test. 3) Re-skimming for every question — skim ONCE, then scan. 4) Spending more than 1.5 minutes on a single question — flag it, move on, return at the end. 5) Forgetting to copy answers to the answer sheet — there is NO extra transfer time in Reading (unlike Listening). Write directly on the answer sheet."
                }
            ],
            practice_items: [
                {
                    type: "matching",
                    content: {
                        instruction: "Match the technique (1–4) with the correct moment to use it.",
                        items: [
                            { q: "Skimming", a: "Building a 90-second mental map of structure" },
                            { q: "Scanning", a: "Hunting for a year, name, or specific term" },
                            { q: "Detailed reading", a: "Confirming an answer in 2–3 sentences around your target" },
                            { q: "Inference reading", a: "True/False/Not Given and Yes/No/Not Given questions" }
                        ],
                        explanation: "All four reading speeds appear in one IELTS passage. Strong candidates shift gears constantly; weak candidates read at one speed throughout."
                    }
                },
                {
                    type: "tfng",
                    content: {
                        instruction: "Decide TRUE / FALSE / NOT GIVEN about IELTS Reading.",
                        items: [
                            { q: "There is a penalty for wrong answers in IELTS Reading.", a: "FALSE", why: "Unanswered and wrong both score zero. Always guess." },
                            { q: "The Listening test gives 10 minutes to transfer answers; Reading does not.", a: "TRUE", why: "Reading answers must be written directly on the answer sheet within the 60 minutes." },
                            { q: "All three Reading passages contain 13 questions each.", a: "NOT GIVEN", why: "The number per passage varies — only the total of 40 is fixed." }
                        ]
                    }
                }
            ],
            band_descriptors: {
                "5.0": "Reads slowly and linearly; misses paraphrase; runs out of time and leaves blanks.",
                "6.0": "Skims partially; finds direct lexical matches but misses synonyms; finishes ~80% of questions.",
                "7.0": "Skims efficiently in under 2 minutes; recognises paraphrase; manages all 40 questions in time.",
                "8.0": "Predicts question type from stem alone; uses scanning for nearly all factual questions; less than 5 errors total."
            },
            next_steps: [
                "Lesson Reading 2: Matching Headings — apply skimming directly.",
                "Take Cambridge IELTS practice Test 1, Passage 1 with strict 18-minute timer."
            ]
        },

        // ---------- READING LESSON 2 ----------
        {
            id: "ielts-reading-2",
            section: "reading",
            band_target: "5.5-9.0",
            cefr: "B1-C2",
            title: "Matching Headings",
            subtitle: "The question type that punishes detail-readers and rewards skimmers.",
            duration_min: 55,
            objectives: [
                "Identify the main idea (not detail) of each paragraph in under 60 seconds.",
                "Use the 'topic sentence + concluding sentence' rule to locate paragraph theme.",
                "Eliminate distractor headings systematically.",
                "Avoid the 'first-sentence trap' set by IELTS examiners."
            ],
            sections: [
                {
                    type: "intro",
                    title: "What this question type tests",
                    content: "Matching Headings gives you a list of 8–12 possible headings (i, ii, iii…) and asks you to assign one to each paragraph (A, B, C…). There are always more headings than paragraphs — that's the trap. The skill being tested is whether you can identify the MAIN IDEA of a paragraph, not a detail mentioned inside it."
                },
                {
                    type: "strategy",
                    title: "The 4-step Matching Headings method",
                    content: "Step 1: read all the headings first and underline the KEY NOUN/VERB in each. Group similar-looking headings — examiners always include 2 headings that look alike to test whether you can distinguish them. Step 2: read paragraph A's first sentence AND last sentence. Ignore the middle on first pass. Step 3: ask yourself — which heading captures BOTH sentences? If two headings fit, read one middle sentence. Step 4: cross out the chosen heading. Move to paragraph B. Headings cannot repeat."
                },
                {
                    type: "strategy",
                    title: "The first-sentence trap",
                    content: "Roughly 30% of IELTS paragraphs begin with a sentence that is NOT the topic sentence — it might introduce a counter-argument, a question, an anecdote, or a transition from the previous paragraph. The TRUE topic often appears in sentence 2 or 3. Whenever sentence 1 starts with: 'However…', 'But…', 'Some people argue…', 'Imagine that…', or a rhetorical question, the topic sentence is later. Train yourself to spot these openers."
                },
                {
                    type: "example",
                    title: "Worked example",
                    content: "Paragraph: 'However, this view is now being challenged. A growing body of research suggests that urban green spaces actually reduce crime by up to 12%. Studies in Chicago, London, and Cape Town all confirm the trend.' Distractor heading: 'The contested impact of green spaces' — sounds plausible but is too vague. Correct heading: 'Evidence that parks reduce urban crime' — captures the SUPPORTED finding (the topic) and the EVIDENCE (the studies)."
                },
                {
                    type: "common_mistakes",
                    title: "Common errors that drop your band",
                    content: "1) Choosing a heading because it contains a word from the paragraph — examiners specifically design distractors with shared keywords. 2) Choosing the heading that matches sentence 1 only — falls into the topic-sentence trap. 3) Reading the whole paragraph word by word — wastes time. 4) Re-using a heading — you cannot. 5) Leaving paragraph A for last — it sets the topic frame; do it first."
                },
                {
                    type: "tips",
                    title: "Pro tip: do Matching Headings LAST",
                    content: "Many top-scoring students answer Matching Headings AFTER all other questions on that passage. Why? Because the other questions force you to read the passage in detail, and by the time you return to headings, you already know what each paragraph is about. This single habit can lift your Reading band by 0.5."
                }
            ],
            practice_items: [
                {
                    type: "matching",
                    content: {
                        instruction: "Match the paragraph excerpt to the correct heading.",
                        items: [
                            { q: "Paragraph A: 'For decades, scientists assumed that bees navigated by smell alone. Recent experiments show this is incomplete: bees also use the position of the sun and polarised light patterns invisible to humans.'", a: "Heading iv: New findings overturn an old assumption" },
                            { q: "Paragraph B: 'The economic value of pollination is staggering. Crops worth USD 235 billion globally depend partly or wholly on insect pollinators, with almonds and apples among the most reliant.'", a: "Heading vii: The financial stakes of pollinator decline" },
                            { q: "Paragraph C: 'Imagine a single bee returning to its hive after a successful foraging trip. Within seconds, it begins a precise figure-of-eight dance. The dance encodes the direction and distance of the food source.'", a: "Heading ii: How bees communicate location" }
                        ],
                        explanation: "In B, candidates often pick a heading about 'crop diseases' because the paragraph names crops — that's the keyword trap. The CORE idea is economic value, not crops themselves."
                    }
                }
            ],
            band_descriptors: {
                "5.0": "Picks headings based on shared keywords; falls for first-sentence trap; gets ~3 of 6 correct.",
                "6.0": "Identifies most main ideas but is fooled by 1–2 distractors per set; ~4 of 6.",
                "7.0": "Distinguishes detail from main idea reliably; recognises distractor patterns; ~5 of 6.",
                "8.0": "Uses Matching Headings as a verification step after other questions; 6 of 6."
            },
            next_steps: [
                "Lesson Reading 3: True / False / Not Given — the most-feared question type.",
                "Practice 2 Matching Headings sets back-to-back, strict 8-minute limit."
            ]
        },

        // ---------- READING LESSON 3 ----------
        {
            id: "ielts-reading-3",
            section: "reading",
            band_target: "5.5-9.0",
            cefr: "B1-C2",
            title: "True / False / Not Given",
            subtitle: "Decode the most misunderstood question type — and stop guessing.",
            duration_min: 55,
            objectives: [
                "Define precisely what TRUE, FALSE, and NOT GIVEN mean.",
                "Distinguish FALSE (contradicted) from NOT GIVEN (absent).",
                "Recognise the 4 paraphrase patterns examiners use.",
                "Apply the 'one-keyword test' to confirm answers."
            ],
            sections: [
                {
                    type: "intro",
                    title: "Why this question type breaks candidates",
                    content: "Most students lose 3–5 marks here every test because they confuse FALSE with NOT GIVEN. The cost is brutal: those marks alone separate Band 6.0 from Band 7.0 in many candidates. The good news: once the rule is clear, your accuracy can jump from 50% to 90%."
                },
                {
                    type: "strategy",
                    title: "The three definitions you must memorise",
                    content: "TRUE = the statement AGREES with information stated in the passage. FALSE = the statement CONTRADICTS information stated in the passage. NOT GIVEN = there is no information about the statement in the passage — neither agreeing nor disagreeing. Note: 'NOT GIVEN' is NOT the same as 'I don't know' or 'I can't find it'. It means the passage is silent."
                },
                {
                    type: "strategy",
                    title: "Three diagnostic questions to apply",
                    content: "For every statement, ask: (1) Does the passage explicitly say this? → TRUE. (2) Does the passage explicitly say the OPPOSITE? → FALSE. (3) Does the passage simply NOT mention this? → NOT GIVEN. The trick: read the question, find the matching paragraph, then ask yourself those three questions IN ORDER."
                },
                {
                    type: "example",
                    title: "Worked example — three possible answers",
                    content: "PASSAGE: 'Hummingbirds beat their wings up to 80 times per second. They are found exclusively in the Americas.' STATEMENT 1: 'Hummingbirds beat their wings 80 times per second.' Answer: TRUE — the passage explicitly says this. STATEMENT 2: 'Hummingbirds are found in Africa.' Answer: FALSE — the passage says 'exclusively in the Americas', which contradicts. STATEMENT 3: 'Hummingbirds migrate in winter.' Answer: NOT GIVEN — the passage says nothing about migration."
                },
                {
                    type: "strategy",
                    title: "Paraphrase patterns to watch for",
                    content: "Examiners almost always paraphrase. Four patterns recur: (1) SYNONYMS: 'reduce' → 'decrease', 'major' → 'significant'. (2) NEGATION: 'common' → 'not rare'. (3) ACTIVE/PASSIVE shift: 'scientists discovered X' → 'X was discovered'. (4) NOMINALISATION: 'rapidly increasing' → 'a rapid increase'. Train your eye to recognise these — surface words rarely match between question and passage."
                },
                {
                    type: "tips",
                    title: "Quantifier traps",
                    content: "Watch for: 'all', 'never', 'always', 'every', 'only', 'unique'. If the question says 'ALL X are Y' but the passage only says 'MANY X are Y' — the question is FALSE (the universal claim is contradicted by the limited claim). Similarly, if the question says 'X is the FIRST/ONLY/BEST', verify the superlative is explicit in the passage."
                },
                {
                    type: "common_mistakes",
                    title: "Mistakes that cost marks",
                    content: "1) Using outside knowledge — even if you know the statement is true in real life, if the passage doesn't say so, it's NOT GIVEN. 2) Confusing FALSE and NOT GIVEN. 3) Writing 'F' for both False and Not Given. 4) Hesitating and changing correct answers — first instinct is usually right. 5) Spending 4 minutes on one statement — limit yourself to 90 seconds."
                }
            ],
            practice_items: [
                {
                    type: "tfng",
                    content: {
                        instruction: "PASSAGE: 'The first commercial coffeehouse in England opened in Oxford in 1650, run by a Lebanese man named Jacob. Within 15 years, hundreds had appeared in London. They were nicknamed penny universities because, for the price of a single cup, customers could listen to lectures and debates.'",
                        items: [
                            { q: "Coffee was first sold commercially in England in the 17th century.", a: "TRUE", why: "1650 is in the 17th century — paraphrase of date." },
                            { q: "Jacob was English.", a: "FALSE", why: "Passage says he was Lebanese — direct contradiction." },
                            { q: "Coffee was more expensive in London than in Oxford.", a: "NOT GIVEN", why: "No price comparison appears." },
                            { q: "Coffeehouse customers could attend educational events for the price of a coffee.", a: "TRUE", why: "Paraphrase of 'penny universities' — listen to lectures." },
                            { q: "Coffeehouses replaced traditional universities in England.", a: "NOT GIVEN", why: "No comparison to traditional universities is made." }
                        ]
                    }
                }
            ],
            band_descriptors: {
                "5.0": "Confuses FALSE with NOT GIVEN frequently; about 50% accuracy.",
                "6.0": "Distinguishes the three categories most of the time; misses paraphrase in ~30% of items.",
                "7.0": "Reads paraphrase fluently; spots quantifier traps; ~80% accuracy.",
                "8.0": "Diagnostic 3-question routine fully automatic; under 90 seconds per item; near-perfect."
            },
            next_steps: [
                "Lesson Reading 4: Summary Completion — vocabulary precision.",
                "Drill 30 T/F/NG statements from Cambridge IELTS 16."
            ]
        },

        // ---------- READING LESSON 4 ----------
        {
            id: "ielts-reading-4",
            section: "reading",
            band_target: "5.5-9.0",
            cefr: "B1-C2",
            title: "Summary Completion",
            subtitle: "Fill the gaps without falling for grammatical or paraphrase traps.",
            duration_min: 50,
            objectives: [
                "Predict the part of speech needed for each gap before searching.",
                "Use a word-bank when given; deduce when not.",
                "Respect the word-limit rule (NO MORE THAN TWO/THREE WORDS).",
                "Avoid the most common spelling-related mark losses."
            ],
            sections: [
                {
                    type: "intro",
                    title: "What this question type tests",
                    content: "Summary Completion gives you a paragraph (or two) summarising part of the passage with blanks. Sometimes a word-bank is provided (you choose from 10–12 options); sometimes it isn't (you must take exact words from the passage). It tests your ability to recognise paraphrase AND to use grammatically correct word forms."
                },
                {
                    type: "strategy",
                    title: "The pre-reading routine",
                    content: "Before scanning the passage, READ THE SUMMARY FIRST. For each blank, decide: (a) part of speech needed (noun? adjective? verb?), (b) singular or plural, (c) approximate meaning expected. Example: 'Birds use the position of the ___ to navigate.' You know the gap is a noun (singular or plural), and meaning is something celestial/visible — likely 'sun' or 'stars'. This narrows your search dramatically."
                },
                {
                    type: "strategy",
                    title: "Two scenarios",
                    content: "SCENARIO A — Word-bank given: read all the bank words first; group them by part of speech. Eliminate options as you fill blanks. Each word is used only once unless stated. SCENARIO B — Words from the passage: you must use the EXACT word(s). Do not change tense, number, or form. If the passage says 'pollination', do not write 'pollinate'."
                },
                {
                    type: "tips",
                    title: "The word-limit rule",
                    content: "Read the instruction carefully: 'NO MORE THAN TWO WORDS' means 1 or 2 words allowed. 'NO MORE THAN THREE WORDS AND/OR A NUMBER' means up to 3 words plus optionally a number. EXCEEDING the limit means an automatic zero on that item, even if your meaning is correct. Hyphenated words (e.g. 'self-evident') count as ONE word. 'A' or 'the' counts as a word."
                },
                {
                    type: "common_mistakes",
                    title: "Costly errors",
                    content: "1) Misspelling the answer — exact passage spelling required. 2) Changing the word form (e.g. writing 'industrial' when passage has 'industry'). 3) Writing more words than allowed. 4) Filling gaps in random order — gaps usually appear in passage order. 5) Ignoring grammar — if the gap follows 'a/an', you need a singular noun starting with consonant/vowel respectively."
                }
            ],
            practice_items: [
                {
                    type: "completion",
                    content: {
                        instruction: "Complete the summary using NO MORE THAN TWO WORDS from the passage.",
                        passage: "Bee colonies operate as superorganisms. The queen lays up to 2,000 eggs per day during peak season. Worker bees, all female, perform every other task: foraging, nursing larvae, building wax cells, and defending the hive. Drones — the only males — exist solely to mate with new queens.",
                        items: [
                            { q: "A bee colony functions like a single ___.", a: "superorganism", why: "Direct paraphrase from sentence 1." },
                            { q: "The queen can lay around ___ eggs daily.", a: "2,000", why: "Number from passage; the limit allows it." },
                            { q: "Drones are male bees whose only purpose is ___.", a: "to mate / mating", why: "Either form acceptable depending on grammar of full sentence." }
                        ]
                    }
                }
            ],
            band_descriptors: {
                "5.0": "Inserts plausible-sounding words but wrong form or wrong number; ~50%.",
                "6.0": "Mostly correct meaning; loses 1–2 marks on spelling or word limit.",
                "7.0": "Predicts part of speech reliably; clean spelling; ~85%.",
                "8.0": "Uses word-bank elimination; respects all rules; near-perfect."
            },
            next_steps: [
                "Lesson Reading 5: Multiple Choice (single + multiple).",
                "Practice 2 summary-completion sets, one with bank, one without."
            ]
        },

        // ---------- READING LESSON 5 ----------
        {
            id: "ielts-reading-5",
            section: "reading",
            band_target: "5.5-9.0",
            cefr: "B1-C2",
            title: "Multiple Choice (single + multiple answers)",
            subtitle: "Beat the distractors — the IELTS examiner's favourite trap-laying ground.",
            duration_min: 50,
            objectives: [
                "Identify the question stem keyword before reading options.",
                "Recognise the four standard distractor types.",
                "Differentiate single-answer (A/B/C/D) from multi-answer (TWO/THREE of A–E).",
                "Apply elimination rather than positive selection."
            ],
            sections: [
                {
                    type: "intro",
                    title: "Why MCQ is a paraphrase test in disguise",
                    content: "IELTS MCQ rarely has obviously wrong options. Three of the four choices will overlap meaningfully with content in the passage — only one captures the EXACT idea. The skill being tested is paraphrase recognition under time pressure."
                },
                {
                    type: "strategy",
                    title: "The 5-step MCQ routine",
                    content: "1) Read the STEM first; ignore the options. 2) Underline the keyword in the stem. 3) Locate the keyword (or its paraphrase) in the passage. 4) Read 2–3 sentences around it carefully. 5) NOW look at options A/B/C/D. Eliminate the three that don't match. The single survivor is your answer. Reading options before the passage primes you to find what isn't there."
                },
                {
                    type: "strategy",
                    title: "The four distractor patterns",
                    content: "PATTERN 1 — Right idea, wrong detail: option uses correct topic but adds a number, year, or quantifier not in the passage. PATTERN 2 — Wrong scope: option overgeneralises ('all scientists agree') when passage says 'some'. PATTERN 3 — Half-true: first half matches; second half contradicts. PATTERN 4 — Out of passage: completely true in real life but not stated in the text."
                },
                {
                    type: "example",
                    title: "Worked example",
                    content: "PASSAGE: 'Most paleontologists now accept that the dinosaurs went extinct due to a combination of an asteroid impact and prolonged volcanic activity.' STEM: 'According to the passage, dinosaur extinction was caused by:' OPTIONS: A) an asteroid alone — Pattern 3, half-true. B) volcanic activity alone — Pattern 3. C) a combination of asteroid impact and volcanic activity — CORRECT. D) climate change driven by mammals — Pattern 4, out of passage. Always look for the option that captures BOTH causes."
                },
                {
                    type: "strategy",
                    title: "Multi-answer questions ('Choose TWO of A–E')",
                    content: "When asked to pick TWO or THREE answers, treat each option as a mini-True/False decision. Don't pick the first two that look right and stop — verify all five against the passage. Marks are usually awarded per correct selection, so partial credit is possible."
                },
                {
                    type: "common_mistakes",
                    title: "Errors that drop your score",
                    content: "1) Reading options first, biasing your search. 2) Choosing options based on familiar words. 3) Choosing the longest or most complex option (not always correct). 4) Forgetting that 'According to the writer' means the writer's view only, not yours. 5) Selecting only one answer when two were required."
                }
            ],
            practice_items: [
                {
                    type: "mcq",
                    content: {
                        instruction: "Read the passage and answer.",
                        passage: "Although exercise has long been linked to physical health, recent studies show its strongest effects are on mental wellbeing. A 2023 meta-analysis of 97 trials found that regular moderate aerobic exercise reduced depression symptoms by an average of 43%, outperforming many first-line medications in mild-to-moderate cases.",
                        question: "What does the writer suggest about exercise?",
                        options: [
                            { letter: "A", text: "It is a substitute for all anti-depressant medication.", correct: false, why: "Overstates — passage says only mild-to-moderate cases, and many not all medications." },
                            { letter: "B", text: "Its impact on mental health is greater than on physical health.", correct: true, why: "Direct paraphrase: 'strongest effects are on mental wellbeing'." },
                            { letter: "C", text: "It works only for severely depressed patients.", correct: false, why: "Opposite — mild-to-moderate cases." },
                            { letter: "D", text: "Its mental benefits emerged only after 2023.", correct: false, why: "Pattern 4 — passage doesn't claim this." }
                        ]
                    }
                }
            ],
            band_descriptors: {
                "5.0": "Picks options based on shared vocabulary; ~50% MCQ accuracy.",
                "6.0": "Spots obvious distractors but falls for half-true; ~70%.",
                "7.0": "Eliminates systematically; ~85%.",
                "8.0": "Predicts the answer before looking at options; verifies via elimination; near-perfect."
            },
            next_steps: [
                "Lesson Reading 6: Sentence Completion.",
                "Drill 20 MCQ items from past papers."
            ]
        },

        // ---------- READING LESSON 6 ----------
        {
            id: "ielts-reading-6",
            section: "reading",
            band_target: "5.5-9.0",
            cefr: "B1-C2",
            title: "Sentence Completion",
            subtitle: "Lock down the sentence stem and the grammatical fit before searching.",
            duration_min: 45,
            objectives: [
                "Use sentence stems as both location markers and grammatical filters.",
                "Apply the same word-limit rules as Summary Completion.",
                "Recognise that answers usually appear in passage order.",
                "Distinguish from Summary Completion (single sentences vs full paragraph)."
            ],
            sections: [
                {
                    type: "intro",
                    title: "What this question type tests",
                    content: "Sentence Completion gives you a list of incomplete sentences (5–8 of them). Each must be completed with words taken DIRECTLY from the passage, respecting a word limit. Unlike Summary Completion, sentences are independent of each other."
                },
                {
                    type: "strategy",
                    title: "The 4-step routine",
                    content: "1) Read the FIRST half of the sentence (the stem) — it tells you what to search for. 2) Predict the part of speech needed for the gap. 3) Scan the passage in order — answers usually appear sequentially. 4) Once located, copy the EXACT word(s) from the passage; do not change form."
                },
                {
                    type: "tips",
                    title: "Why answers appear in order",
                    content: "IELTS examiners typically structure question sets so that answers run roughly in the order of the passage. This means once you find Q1 in paragraph B, Q2 will be in B or later, never earlier. Use this to narrow your scanning area and save time."
                },
                {
                    type: "common_mistakes",
                    title: "What costs you marks",
                    content: "1) Paraphrasing your answer instead of copying the passage word. 2) Changing singular/plural. 3) Exceeding word limit. 4) Spelling errors. 5) Misreading the stem and searching for the wrong concept."
                }
            ],
            practice_items: [
                {
                    type: "completion",
                    content: {
                        instruction: "Complete the sentences with NO MORE THAN THREE WORDS from the passage.",
                        passage: "Solar panels lose efficiency at high temperatures. Engineers have developed micro-channel cooling systems that pump water through tiny tubes behind each panel. Tests in Arizona showed efficiency gains of up to 18% during peak summer hours.",
                        items: [
                            { q: "High temperatures cause solar panels to ___.", a: "lose efficiency", why: "Direct phrase from sentence 1." },
                            { q: "Cooling is achieved by pumping water through ___.", a: "tiny tubes / micro-channel cooling systems", why: "Either acceptable; check exact wording." },
                            { q: "In Arizona summer, efficiency improved by up to ___.", a: "18%", why: "Number with % sign." }
                        ]
                    }
                }
            ],
            band_descriptors: {
                "5.0": "Often paraphrases; misses word limit; 50%.",
                "6.0": "Mostly direct quotes; occasional grammar mismatch; 70%.",
                "7.0": "Predicts part of speech; respects all rules; 85%+.",
                "8.0": "Sub-60-second per item; clean spelling; near-perfect."
            },
            next_steps: [
                "Lesson Reading 7: Matching Features / Sentence Endings.",
                "Practice 2 timed Sentence Completion sets."
            ]
        },

        // ---------- READING LESSON 7 ----------
        {
            id: "ielts-reading-7",
            section: "reading",
            band_target: "5.5-9.0",
            cefr: "B1-C2",
            title: "Matching Features / Sentence Endings",
            subtitle: "Two cousin question types — same skill, different layout.",
            duration_min: 50,
            objectives: [
                "Match information, opinions, or claims to people / categories / theories.",
                "Complete sentences by joining a stem to one of many endings.",
                "Recognise that the matching items can repeat (matching features) or not (sentence endings — varies).",
                "Use scanning for proper nouns to locate match candidates fast."
            ],
            sections: [
                {
                    type: "intro",
                    title: "What these question types test",
                    content: "Matching Features asks you to assign a piece of information (e.g. a finding, an opinion, an event) to an item from a list (e.g. a researcher, a country, a decade). Sentence Endings gives you sentence beginnings and a longer list of endings; you choose the right ending for each. Both test paraphrase recognition + scanning."
                },
                {
                    type: "strategy",
                    title: "Method for Matching Features",
                    content: "1) Note the list of items (e.g. researchers Smith, Jones, Park). These are usually proper nouns — easy to scan. 2) For each statement, read carefully what it claims. 3) Scan the passage for each name; read the surrounding sentences. 4) Match the statement to the name whose stated view aligns. 5) Note: items CAN be reused (e.g. 'one researcher might match 2 statements'); read the instructions."
                },
                {
                    type: "strategy",
                    title: "Method for Sentence Endings",
                    content: "1) Read all sentence beginnings (the stems). 2) Read all endings. 3) For each stem, scan the passage, find the relevant section, then choose the ending that grammatically AND semantically completes it correctly. 4) Endings usually appear in passage order, like Sentence Completion. 5) There are always more endings than stems — extras are distractors."
                },
                {
                    type: "tips",
                    title: "Speed tip",
                    content: "Matching Features is one of the FASTEST question types if you focus on proper-noun scanning. Don't read the passage in detail — just hunt names. Often you can answer 5 of these in under 6 minutes, leaving more time for harder questions."
                },
                {
                    type: "common_mistakes",
                    title: "Common errors",
                    content: "1) Assuming each item is used only once when instructions say otherwise. 2) Choosing the answer based on the first occurrence of a name (the writer might mention them, then quote them later). 3) Skipping the instruction about reuse. 4) Choosing the closest-looking ending without checking grammar fit."
                }
            ],
            practice_items: [
                {
                    type: "matching",
                    content: {
                        instruction: "Match each statement (1–3) to the correct researcher (A=Tanaka, B=Okonkwo, C=Lindholm). NB: a researcher may be used more than once.",
                        passage_extract: "Tanaka argued that screen time before bedtime suppresses melatonin. Okonkwo, working in Lagos, found that adolescents using phones after 10pm slept on average 47 minutes less. Lindholm reviewed 28 studies and concluded that light wavelength matters more than total exposure time. Tanaka further suggested that filters reducing blue light could reverse this effect.",
                        items: [
                            { q: "Suggested a possible technological solution.", a: "A — Tanaka", why: "'Filters reducing blue light could reverse this effect'." },
                            { q: "Quantified sleep loss in a specific population.", a: "B — Okonkwo", why: "47 minutes less in adolescents." },
                            { q: "Found that the type of light is more important than duration.", a: "C — Lindholm", why: "Wavelength matters more than total exposure time." }
                        ]
                    }
                }
            ],
            band_descriptors: {
                "5.0": "Slow to scan names; confuses similar findings; 50%.",
                "6.0": "Locates names but mismatches statements occasionally; 70%.",
                "7.0": "Fast proper-noun scanning; clear paraphrase recognition; 85%+.",
                "8.0": "Completes 5 items in under 6 minutes; near-perfect."
            },
            next_steps: [
                "Lesson Reading 8: Diagram Labelling + Time Management.",
                "Practice timed Matching Features sets."
            ]
        },

        // ---------- READING LESSON 8 ----------
        {
            id: "ielts-reading-8",
            section: "reading",
            band_target: "5.5-9.0",
            cefr: "B1-C2",
            title: "Diagram Labelling + Reading Time Management",
            subtitle: "The visual question type plus the master plan for 60 minutes.",
            duration_min: 50,
            objectives: [
                "Label diagrams using exact words from the passage.",
                "Read diagrams in the same logical order as the passage description.",
                "Build a personal 60-minute timing plan that fits your strengths.",
                "Master the 'flag and return' habit for hard questions."
            ],
            sections: [
                {
                    type: "intro",
                    title: "Diagram labelling — the underrated easy points",
                    content: "Diagram Labelling appears in process-based passages (e.g. how a machine works, how a natural cycle operates). It's almost always among the EASIEST questions in the test — once you find the right paragraph, the answers are usually adjacent words. Yet candidates often skip them due to time pressure."
                },
                {
                    type: "strategy",
                    title: "How to attack a diagram label question",
                    content: "1) Look at the diagram carefully. Identify what's already labelled and what isn't. 2) Read the surrounding context — captions, arrows, sequence numbers. 3) Locate the matching paragraph in the passage (process descriptions usually concentrate in 1–2 paragraphs). 4) Match each unlabelled feature to the corresponding word(s). 5) Respect the word limit; copy exact words."
                },
                {
                    type: "tips",
                    title: "Building your personal 60-minute plan",
                    content: "TYPICAL: Passage 1 (easiest) 17 mins, Passage 2 (medium) 20 mins, Passage 3 (hardest) 23 mins. ADJUSTMENT: if you find Passage 3 less hard than Passage 2 (varies by topic), reverse times. Always leave 2 minutes at the end to fill blanks. NEVER spend more than 90 seconds on a single question first time round."
                },
                {
                    type: "strategy",
                    title: "The flag-and-return system",
                    content: "When you hit a hard question: (1) write your best guess on the answer sheet, (2) put a small mark next to the question number on the question paper (not the answer sheet), (3) move on. At the end, return to flagged items only if time permits. This single habit prevents the 'lost 8 minutes on one question' disaster that pushes scores down."
                },
                {
                    type: "common_mistakes",
                    title: "Time-management failures",
                    content: "1) Spending equal time on each passage regardless of length and difficulty. 2) Not transferring answers to the sheet (Reading has NO transfer time). 3) Leaving blanks. 4) Going back to old passages once you've moved on (very rarely worth the time). 5) Ignoring the diagram because it 'looks complicated'."
                }
            ],
            practice_items: [
                {
                    type: "completion",
                    content: {
                        instruction: "Label the diagram of a hydroelectric dam using NO MORE THAN TWO WORDS from the passage.",
                        passage: "Water flows from the reservoir through an intake gate into a long pipe called the penstock. The fast-moving water spins a turbine. The turbine shaft rotates a generator, which produces electricity. Used water exits through the tailrace into the river below.",
                        items: [
                            { q: "Label A — the pipe carrying water from the reservoir.", a: "penstock" },
                            { q: "Label B — the wheel-like component spun by water.", a: "turbine" },
                            { q: "Label C — the device that produces electricity.", a: "generator" },
                            { q: "Label D — the exit channel for used water.", a: "tailrace" }
                        ],
                        explanation: "Process descriptions follow the order of the diagram. Read once, label all four in 90 seconds."
                    }
                }
            ],
            band_descriptors: {
                "5.0": "Often skips diagrams; runs out of time; ~5/40 unanswered.",
                "6.0": "Attempts diagrams but misses paraphrase; finishes 38/40.",
                "7.0": "Smooth time-management; flag-and-return automatic; 40/40 attempted.",
                "8.0": "Personal timing plan; uses spare 2 mins to verify; near-perfect."
            },
            next_steps: [
                "Take a full 60-minute Reading mock under exam conditions.",
                "Move to Listening section, Lesson 1."
            ]
        },

        // ============================================================
        // LISTENING — 6 LESSONS
        // ============================================================

        // ---------- LISTENING LESSON 1 ----------
        {
            id: "ielts-listening-1",
            section: "listening",
            band_target: "5.5-9.0",
            cefr: "B1-C2",
            title: "Note-Taking + Predicting Answers",
            subtitle: "The two habits that separate Band 6 from Band 8 in Listening.",
            duration_min: 50,
            objectives: [
                "Build a 30-second pre-listening prediction routine.",
                "Use abbreviations and symbols for fast note-taking.",
                "Identify the part of speech needed for each gap before audio plays.",
                "Use signposting words to track where the speaker is."
            ],
            sections: [
                {
                    type: "intro",
                    title: "Why these are the master skills",
                    content: "IELTS Listening plays each recording ONCE. There is no replay. The test rewards candidates who anticipate what they will hear — not those who try to understand every word. Prediction reduces cognitive load; note-taking captures what your working memory can't hold."
                },
                {
                    type: "strategy",
                    title: "The 30-second prediction routine",
                    content: "Before each section, you get 20–30 seconds to read the questions. Use them to: (1) underline keywords in each question, (2) predict the type of answer needed (number? name? place? noun? verb?), (3) note any logical limits (e.g. if a gap follows 'a/an', the answer is a singular noun). Walking into a section blind costs you 2–3 marks every time."
                },
                {
                    type: "strategy",
                    title: "Note-taking system",
                    content: "Don't write full words. Use: '+/-' for increase/decrease, '→' for leads to, '∴' for therefore, '?' for unsure, '@' for at/about, '£/$' for money, '#' for number, '~' for approximately. For names, write first 3 letters and check spelling later. The audio is faster than your handwriting — abbreviate."
                },
                {
                    type: "strategy",
                    title: "Listening for signposts",
                    content: "Speakers signal where they are with phrases. Recognise these in real time: 'First of all…' (start), 'Moving on to…' (transition), 'However…' (contrast — answer changes), 'Actually…' (correction — previous info revoked), 'In conclusion…' (final summary). Pay extra attention after 'actually' and 'however' — examiners love placing answers there."
                },
                {
                    type: "common_mistakes",
                    title: "Mistakes that drop your score",
                    content: "1) Writing too much — focus on the gap, not the surrounding speech. 2) Stopping when you miss one answer — keep moving; you'll lose more if you fall behind. 3) Ignoring spelling — incorrect spelling = wrong answer. 4) Failing to use the 10-minute transfer time at the end (Listening DOES give 10 mins to copy answers). 5) Forgetting plurals."
                }
            ],
            practice_items: [
                {
                    type: "completion",
                    content: {
                        instruction: "Predict the part of speech for each gap before checking the answer key.",
                        items: [
                            { q: "Name: Sarah ___", prediction: "Surname (proper noun, capitalised)", a: "e.g., Pemberton" },
                            { q: "Phone number: ___", prediction: "Digits, possibly with country code", a: "e.g., 0044 7700 900123" },
                            { q: "Date of arrival: ___", prediction: "Date in DD Month or Month DD format", a: "e.g., 14 March" },
                            { q: "Type of accommodation: ___", prediction: "Noun, possibly compound (host family / hostel)", a: "e.g., host family" },
                            { q: "Cost per week: £___", prediction: "Number only, possibly with decimal", a: "e.g., 185" }
                        ],
                        explanation: "Prediction primes your ear. Without it, you hear undifferentiated speech and miss critical words."
                    }
                }
            ],
            band_descriptors: {
                "5.0": "No prediction; full-word note-taking; falls behind; 25/40.",
                "6.0": "Some prediction; uses some abbreviations; 28–32/40.",
                "7.0": "Full prediction; signposting awareness; clean spelling; 33–35/40.",
                "8.0": "Anticipates corrections; almost no notes — direct answer capture; 36+/40."
            },
            next_steps: [
                "Lesson Listening 2: Form / Note Completion (Section 1).",
                "Drill 5 sets of pre-listening prediction without playing audio."
            ]
        },

        // ---------- LISTENING LESSON 2 ----------
        {
            id: "ielts-listening-2",
            section: "listening",
            band_target: "5.5-9.0",
            cefr: "B1-C2",
            title: "Form / Note Completion (Section 1)",
            subtitle: "The most predictable section — bank these marks early.",
            duration_min: 45,
            objectives: [
                "Master the conversational format of Section 1.",
                "Capture personal information (names, addresses, phone, dates) accurately.",
                "Spell common UK/Australian/US names correctly.",
                "Recognise number formats (00 vs double-O, decimals, fractions)."
            ],
            sections: [
                {
                    type: "intro",
                    title: "Why Section 1 is your foundation",
                    content: "Section 1 is a real-world conversation between two speakers (e.g. someone enquiring about a course / booking accommodation / registering as a member). It contains 10 questions, mostly form completion. It's the EASIEST section. Top candidates aim for 10/10 here to give themselves a buffer for harder later sections."
                },
                {
                    type: "strategy",
                    title: "Number conventions",
                    content: "Spelt zero: 'oh' or 'zero'. Phone numbers: '00' often said as 'double oh'; '777' as 'triple seven'. Currency: '£3.50' said as 'three pounds fifty'. Years: '1985' as 'nineteen eighty-five'; '2008' as 'two thousand and eight' or 'twenty oh eight'. Be ready for British conventions — postcodes and house numbers especially."
                },
                {
                    type: "strategy",
                    title: "Spelling alphabet",
                    content: "When names are spelt out, expect tricky letters: M/N (often confused), B/V/P, A/E/I, F/S, J/G, K/Q, U/W, X/H. Practise hearing these clearly. Speakers may also use the radio alphabet (Alpha, Bravo, Charlie…) for clarity."
                },
                {
                    type: "tips",
                    title: "Address formats",
                    content: "Typical UK address: '14 Greenway Road, Bristol, BS6 7QH'. Listen for: house number, road type (Road / Street / Avenue / Lane), city, postcode (always 1–2 letters + 1–2 digits, space, 1 digit + 2 letters). Postcode letters may be spelt out."
                },
                {
                    type: "common_mistakes",
                    title: "Mistakes that lose easy marks",
                    content: "1) Writing 'eteen' or 'fifty' wrong — '15' (fifteen) vs '50' (fifty) sound similar. 2) Confusing 'thirteen' and 'thirty'. 3) Misspelling common names (e.g. Stevens vs Stephens, Smith vs Smyth). 4) Using digits when answer requires words (read the instruction). 5) Adding currency symbol when the question already shows it."
                }
            ],
            practice_items: [
                {
                    type: "completion",
                    content: {
                        instruction: "Predict the kind of answer for each gap.",
                        items: [
                            { q: "Surname: ___", prediction: "Proper noun, often spelt out", a: "e.g., HARGREAVES" },
                            { q: "Date of birth: ___", prediction: "DD/MM/YYYY", a: "e.g., 14/02/1996" },
                            { q: "Postcode: ___", prediction: "UK postcode format", a: "e.g., NE2 4PL" },
                            { q: "Email: ___@___.com", prediction: "Username + domain; often spelt", a: "e.g., j.harg@gmail.com" },
                            { q: "Membership type: ___", prediction: "Word: standard / premium / family", a: "e.g., family" }
                        ]
                    }
                }
            ],
            band_descriptors: {
                "5.0": "6–7/10 in Section 1; spelling/number errors.",
                "6.0": "8/10; occasional spelling slip.",
                "7.0": "9–10/10 reliably.",
                "8.0": "10/10; no slip; uses Section 1 confidence boost for Section 2."
            },
            next_steps: [
                "Lesson Listening 3: Multiple Choice (Sections 2–4).",
                "Drill 3 Section 1 audios with strict no-replay rule."
            ]
        },

        // ---------- LISTENING LESSON 3 ----------
        {
            id: "ielts-listening-3",
            section: "listening",
            band_target: "5.5-9.0",
            cefr: "B1-C2",
            title: "Multiple Choice (Sections 2–4)",
            subtitle: "Beat the verbal distractors and the change-of-mind trap.",
            duration_min: 50,
            objectives: [
                "Understand the change-of-mind trap unique to Listening MCQ.",
                "Read all options in advance and underline differences.",
                "Listen for paraphrase rather than exact words.",
                "Use elimination when fully sure of two wrong options."
            ],
            sections: [
                {
                    type: "intro",
                    title: "Listening MCQ vs Reading MCQ",
                    content: "In Reading you can re-read; in Listening you hear once. Listening MCQ adds a unique trap: the speaker may state one option, then change their mind. The correct answer is the FINAL position, not the first one heard. Examiners use phrases like 'actually', 'on second thought', 'I changed my mind', 'I was going to say X but…'."
                },
                {
                    type: "strategy",
                    title: "The pre-listening preparation",
                    content: "1) Read the question stem fully. 2) Read all 3 (or 4) options. 3) Underline the DIFFERENCE between them — usually one keyword separates option B from C. 4) Predict possible signposting language. 5) Listen with the differences in mind."
                },
                {
                    type: "strategy",
                    title: "Spotting the change-of-mind",
                    content: "Phrases that signal a change: 'Actually…', 'Although I considered…', 'I had thought…but', 'On reflection…', 'Hmm, no, I'd rather…'. When you hear them, the previous answer just got CANCELLED. Listen carefully for the new statement; that's your answer."
                },
                {
                    type: "common_mistakes",
                    title: "Pitfalls",
                    content: "1) Picking the first option mentioned. 2) Picking the option whose words you heard most clearly. 3) Not reading all options before audio plays. 4) Looking for exact word matches (paraphrase is the norm). 5) Hesitating — circle and move on."
                }
            ],
            practice_items: [
                {
                    type: "mcq",
                    content: {
                        instruction: "Audio script extract: 'For the field trip, I was going to suggest the museum, but the head of department said it's closed for refurbishment. So we'll go to the botanical garden instead. The art gallery was another option but it's too far.' Question: Where will the field trip go?",
                        options: [
                            { letter: "A", text: "Museum", correct: false, why: "Closed — initial idea cancelled." },
                            { letter: "B", text: "Botanical garden", correct: true, why: "Final decision after change-of-mind." },
                            { letter: "C", text: "Art gallery", correct: false, why: "Mentioned but rejected (too far)." }
                        ]
                    }
                }
            ],
            band_descriptors: {
                "5.0": "Picks first-heard option; 50% MCQ.",
                "6.0": "Catches some change-of-mind; 70%.",
                "7.0": "Reliable change-of-mind detection; 85%+.",
                "8.0": "Listens for final decision exclusively; near-perfect."
            },
            next_steps: [
                "Lesson Listening 4: Plan / Map / Diagram Labelling.",
                "Drill 10 MCQ items focusing on change-of-mind."
            ]
        },

        // ---------- LISTENING LESSON 4 ----------
        {
            id: "ielts-listening-4",
            section: "listening",
            band_target: "5.5-9.0",
            cefr: "B1-C2",
            title: "Plan / Map / Diagram Labelling",
            subtitle: "Spatial language: north, opposite, next to, between.",
            duration_min: 50,
            objectives: [
                "Master directional vocabulary for Section 2 maps.",
                "Track the speaker's movement on the visual.",
                "Locate landmarks using two reference points.",
                "Recognise British spatial conventions (anticlockwise, opposite, far end)."
            ],
            sections: [
                {
                    type: "intro",
                    title: "Why this question type intimidates",
                    content: "Most candidates haven't studied spatial vocabulary in their grammar courses. They know 'next to' but not 'opposite', 'across from', 'on the corner of', 'directly behind'. Without these, the audio washes over them. The good news: there are only ~30 phrases to master, and they recur in every test."
                },
                {
                    type: "strategy",
                    title: "Vocabulary you must know",
                    content: "Cardinal: north, south, east, west, north-east, etc. Position: opposite, across from, next to, beside, between A and B, in front of, behind. Movement: turn left/right, go straight on, take the second left, follow the path until, just past. Sides: on the left/right, on the corner, at the far end, at the back, in the middle."
                },
                {
                    type: "strategy",
                    title: "The trace-and-track method",
                    content: "Use your pencil. As the speaker describes the map, trace their path or mark each location with the question number. Don't try to remember spatially — your pencil is your memory. Update labels in real time."
                },
                {
                    type: "tips",
                    title: "Two-reference rule",
                    content: "Each location is usually pinned by TWO references: e.g. 'The café is on the corner of Main Street, opposite the library'. Listen for both — if you only catch one, you might confuse the location with a nearby distractor. Examiners place 2–3 distractor buildings on every map."
                },
                {
                    type: "common_mistakes",
                    title: "Errors",
                    content: "1) Confusing 'opposite' with 'next to'. 2) Forgetting the speaker may move anticlockwise around a building. 3) Missing 'just past' (which means you've already walked past it). 4) Locking onto the first plausible spot."
                }
            ],
            practice_items: [
                {
                    type: "matching",
                    content: {
                        instruction: "Imagine a map with: A=café, B=bookshop, C=museum, D=fountain, E=bus stop. Match each speaker description to the location.",
                        items: [
                            { q: "'It's at the far end of Park Road, just past the fountain.'", a: "Likely C (museum)" },
                            { q: "'It's directly opposite the museum, on the corner.'", a: "Possibly A (café) if café faces museum" },
                            { q: "'It's between the café and the bus stop.'", a: "B (bookshop) — pinned by two references" }
                        ],
                        explanation: "Without seeing the map, prediction is partial — but the two-reference rule still applies."
                    }
                }
            ],
            band_descriptors: {
                "5.0": "Knows basic vocab; loses position with anticlockwise; 4/8.",
                "6.0": "Tracks most directions; 5–6/8.",
                "7.0": "Full spatial vocab; pencil trace; 7/8.",
                "8.0": "Anticipates distractors; 8/8."
            },
            next_steps: [
                "Lesson Listening 5: Matching + Classification.",
                "Drill 3 map-labelling sections."
            ]
        },

        // ---------- LISTENING LESSON 5 ----------
        {
            id: "ielts-listening-5",
            section: "listening",
            band_target: "5.5-9.0",
            cefr: "B1-C2",
            title: "Matching + Classification",
            subtitle: "Assign options to people, categories, or time periods.",
            duration_min: 45,
            objectives: [
                "Match items to a list of people, categories, or descriptors.",
                "Track classification when the speaker reorders ideas.",
                "Use abbreviations to keep up with rapid attribution.",
                "Recognise that options may repeat or not."
            ],
            sections: [
                {
                    type: "intro",
                    title: "What this looks like",
                    content: "Matching/Classification questions in Listening typically present statements (1–6) and a list of options A/B/C (sometimes more). Examples: 'Match each opinion to the speaker who held it' or 'Classify each course as suitable for beginners / intermediate / advanced'."
                },
                {
                    type: "strategy",
                    title: "Two-column note system",
                    content: "Before audio plays, draw 2 columns on your scratch space: left = the items being classified; right = the option letters. As you listen, write the letter next to the item the moment you hear it confirmed. Don't wait — by the time the speaker moves on, you'll forget."
                },
                {
                    type: "strategy",
                    title: "Listening for classification cues",
                    content: "Cue phrases: 'This one is great for beginners…', 'Only suitable for advanced…', 'I'd recommend the X for newcomers…'. Often the speaker doesn't say the question word literally — they describe the level/type. Be ready for paraphrase: 'no prior experience needed' = beginner."
                },
                {
                    type: "common_mistakes",
                    title: "Errors",
                    content: "1) Assuming each option is used once when reuse is allowed. 2) Locking in answer too early before speaker qualifies. 3) Missing the second classification when speaker changes topic quickly. 4) Confusing similar-sounding categories."
                }
            ],
            practice_items: [
                {
                    type: "matching",
                    content: {
                        instruction: "Audio extract: 'The French course is fully online — no campus visits required. The German course is hybrid: half online, half in person. The Spanish course requires daily attendance.' Match each course to a delivery mode.",
                        items: [
                            { q: "French", a: "Fully online" },
                            { q: "German", a: "Hybrid" },
                            { q: "Spanish", a: "Fully on-campus" }
                        ],
                        explanation: "Direct attribution. Note that 'daily attendance' paraphrases 'fully on-campus'."
                    }
                }
            ],
            band_descriptors: {
                "5.0": "Confuses speakers; 4/6.",
                "6.0": "Tracks most attributions; 5/6.",
                "7.0": "Two-column system fluent; 6/6.",
                "8.0": "Anticipates reuse; perfect."
            },
            next_steps: [
                "Lesson Listening 6: Section 4 Mastery.",
                "Drill 2 classification sets."
            ]
        },

        // ---------- LISTENING LESSON 6 ----------
        {
            id: "ielts-listening-6",
            section: "listening",
            band_target: "5.5-9.0",
            cefr: "B1-C2",
            title: "Section 4 Mastery: Academic Lecture Notes",
            subtitle: "The hardest 10 questions — and how to handle them.",
            duration_min: 55,
            objectives: [
                "Understand the academic monologue structure.",
                "Take notes on a partially-completed framework.",
                "Recognise lecturer signposting.",
                "Push through unfamiliar topics by following structure, not vocabulary."
            ],
            sections: [
                {
                    type: "intro",
                    title: "What Section 4 demands",
                    content: "Section 4 is a 5-minute academic lecture by a single speaker. Topics range widely: archaeology, marine biology, urban planning, anthropology, climate science. The questions are usually note completion — fill blanks in a structured outline. There is NO break between halves; you hear the whole lecture once."
                },
                {
                    type: "strategy",
                    title: "Read the outline first",
                    content: "Use the 30-second prep time to read the entire outline. The outline reveals the lecture's structure: main topic, sub-topics, examples, conclusions. Even if you've never heard of the topic, the structure shows you where the lecturer will go. Predict the part of speech for each gap."
                },
                {
                    type: "strategy",
                    title: "Lecturer signposting",
                    content: "Academic lecturers signal heavily: 'Today I'll cover three points…', 'First…', 'Moving on…', 'A key example is…', 'In summary…'. Use these to locate yourself in the outline. If you miss an answer, the next signpost tells you which section is starting — jump ahead in your outline."
                },
                {
                    type: "strategy",
                    title: "Don't panic on unfamiliar vocabulary",
                    content: "You will hear unknown technical words (e.g. 'photosynthetic plankton', 'archaeobotany', 'tectonic uplift'). DO NOT STOP. Most of the time, the technical word is itself the answer — write down what you hear phonetically and check spelling later. Lecturers often spell technical terms or repeat them."
                },
                {
                    type: "common_mistakes",
                    title: "Common failures",
                    content: "1) Falling behind on one missed answer. 2) Trying to fully understand the topic — only the outline matters. 3) Writing too many words per gap. 4) Not using the 10 minutes at the end to copy onto answer sheet (mandatory for paper-based test)."
                }
            ],
            practice_items: [
                {
                    type: "completion",
                    content: {
                        instruction: "Lecture extract: 'Mangrove forests serve three critical functions in coastal ecosystems. First, they reduce wave energy by up to 70%, protecting shorelines from erosion. Second, they store carbon at four times the rate of tropical rainforests — a process scientists call blue carbon sequestration. Finally, they provide nursery habitat for over a thousand fish species, supporting global fisheries.'",
                        items: [
                            { q: "Function 1: reduce ___ energy by up to 70%.", a: "wave" },
                            { q: "Function 2: store carbon at ___ times the rate of tropical rainforests.", a: "four / 4" },
                            { q: "Term for this process: ___", a: "blue carbon sequestration" },
                            { q: "Function 3: provide ___ habitat for fish species.", a: "nursery" }
                        ]
                    }
                }
            ],
            band_descriptors: {
                "5.0": "Falls behind on technical vocab; 4–5/10.",
                "6.0": "Tracks most signposts; 6–7/10.",
                "7.0": "Outline strategy fluent; 8–9/10.",
                "8.0": "Anticipates structure; 9–10/10."
            },
            next_steps: [
                "Take a full Listening mock with all 4 sections.",
                "Move to Writing T1 Academic Lesson 1."
            ]
        },

        // ============================================================
        // WRITING TASK 1 ACADEMIC — 6 LESSONS
        // ============================================================

        // ---------- W T1 ACADEMIC LESSON 1 ----------
        {
            id: "ielts-w1a-1",
            section: "writing-t1-academic",
            band_target: "6.0-9.0",
            cefr: "B2-C2",
            title: "Line Graph Description",
            subtitle: "Trends, comparisons, and the 4-paragraph template that works every time.",
            duration_min: 60,
            objectives: [
                "Apply the 4-paragraph structure: intro, overview, body 1, body 2.",
                "Use a wide range of trend vocabulary (rose, declined, plateaued, fluctuated).",
                "Compare data without listing every figure.",
                "Hit the 150-word minimum without padding."
            ],
            sections: [
                {
                    type: "intro",
                    title: "What Task 1 Academic tests",
                    content: "Task 1 Academic gives you a visual (line graph, bar chart, pie chart, table, process diagram, or map) and asks you to write a 150-word report describing the main features. You have 20 minutes. It tests: (a) ability to summarise data, (b) range of trend vocabulary, (c) accurate paraphrase of the prompt, (d) clear paragraph organisation. NO opinion is required. NO speculation about causes."
                },
                {
                    type: "strategy",
                    title: "The 4-paragraph template",
                    content: "PARAGRAPH 1 (Introduction, ~25 words): paraphrase the prompt — say what the visual shows, the unit of measurement, and the time period. PARAGRAPH 2 (Overview, ~30 words): identify 2–3 KEY TRENDS without numbers. Use phrases: 'Overall…', 'It is clear that…'. PARAGRAPH 3 (Body 1, ~50 words): describe the first half of the data with figures. PARAGRAPH 4 (Body 2, ~50 words): describe the second half or a contrasting trend with figures. Total: ~150–170 words."
                },
                {
                    type: "strategy",
                    title: "Trend vocabulary toolkit",
                    content: "RISE: increase, rise, climb, grow, surge, soar (sharp), edge up (slight). FALL: decrease, decline, drop, fall, plummet (sharp), dip (slight). NO CHANGE: remain stable, stay constant, level off, plateau. FLUCTUATION: fluctuate, vary, oscillate. ADVERBS: dramatically, sharply, steadily, gradually, slightly, marginally. NOUN FORMS: a rise, a decline, a sharp increase, a steady fall."
                },
                {
                    type: "example",
                    title: "Model answer (Band 7+)",
                    content: "PROMPT: The line graph shows the population (in millions) of three cities — Lagos, Cairo, and Mumbai — between 1990 and 2020. MODEL: 'The line graph illustrates the change in population, in millions, of Lagos, Cairo, and Mumbai over the three decades from 1990 to 2020. Overall, all three cities experienced significant growth, although Lagos saw the most dramatic rise, eventually overtaking the other two by 2020. In 1990, Mumbai had the largest population at approximately 12 million, followed by Cairo (9 million) and Lagos (6 million). Mumbai grew steadily to around 18 million by 2010 before plateauing. Cairo rose more gradually, reaching 14 million in 2020. By contrast, Lagos surged from 6 million in 1990 to over 21 million in 2020, a more than threefold increase that placed it ahead of both Mumbai and Cairo by the end of the period.' (Word count: 152)"
                },
                {
                    type: "common_mistakes",
                    title: "Mistakes that cap your score at Band 6.0",
                    content: "1) Copying the prompt verbatim — automatic deduction. 2) Including opinion or speculation about causes ('possibly because of urbanisation' — NEVER in T1). 3) Missing the overview paragraph — guaranteed Band 5 ceiling. 4) Listing every data point with no comparison. 5) Under 150 words — automatic penalty. 6) Wrong tense (use past for past data, present for predicted)."
                },
                {
                    type: "tips",
                    title: "Time allocation",
                    content: "0–2 mins: analyse the visual, mark 2–3 key trends. 2–3 mins: plan paragraph content. 3–18 mins: write. 18–20 mins: check word count, tense, spelling. NEVER over-run into Task 2's time — Task 2 is worth twice as many marks."
                }
            ],
            practice_items: [
                {
                    type: "writing_prompt",
                    content: {
                        prompt: "The line graph shows monthly average temperatures (°C) in three cities — Reykjavik, Madrid, and Singapore — over a year.",
                        band_6_response: "The graph show temperatures of three cities in one year. Reykjavik is cold all year, between 0 and 12 degrees. Madrid is hot in summer, around 30 in July, and cold in winter, 5 in January. Singapore is hot all year, around 28 every month. The hottest is Madrid in summer. The coldest is Reykjavik in winter. Singapore has no big change. (Note: under 150 words, no overview, repetitive, basic vocabulary.)",
                        band_8_response: "The line graph compares average monthly temperatures in degrees Celsius across three cities — Reykjavik, Madrid, and Singapore — throughout a calendar year. Overall, while Madrid exhibits pronounced seasonal variation and Reykjavik remains consistently cool, Singapore's tropical climate produces remarkably stable temperatures year-round. Reykjavik's temperatures fluctuate within a narrow band, climbing from approximately 0°C in January to a peak of just 12°C in July before declining again. Madrid, by contrast, shows the steepest seasonal swing: temperatures rise sharply from around 6°C in January to a high of 31°C in July and August, then fall steadily back. Singapore stands apart entirely, hovering between 26°C and 29°C every month with no discernible seasonal pattern. The most striking contrast occurs in winter, when Madrid is roughly 6 degrees warmer than Reykjavik but 20 degrees cooler than Singapore. (Word count: 152)",
                        analysis: "Band 8 has clear overview, comparative language ('exhibits', 'by contrast', 'stands apart'), accurate paraphrase, range of trend vocabulary, complex sentences, and accurate data."
                    }
                }
            ],
            band_descriptors: {
                "6.0": "Covers main features; basic vocab; some grammatical errors; clear but mechanical organisation.",
                "7.0": "Clear overview; range of trend vocab; accurate data; complex sentences attempted with occasional errors.",
                "8.0": "Skilful comparison; wide vocabulary; rare errors; sophisticated paragraphing.",
                "9.0": "Fully natural language; flawless data integration; insightful overview."
            },
            next_steps: [
                "Lesson W1A 2: Bar Chart Description.",
                "Write 1 line graph response under 20-min timer."
            ]
        },

        // ---------- W T1 ACADEMIC LESSON 2 ----------
        {
            id: "ielts-w1a-2",
            section: "writing-t1-academic",
            band_target: "6.0-9.0",
            cefr: "B2-C2",
            title: "Bar Chart Description",
            subtitle: "Compare categories without listing every bar.",
            duration_min: 60,
            objectives: [
                "Group similar bars to avoid listing.",
                "Use comparative structures (twice as many, three times higher).",
                "Distinguish stacked bar charts from grouped bar charts.",
                "Highlight the highest, lowest, and surprising data points."
            ],
            sections: [
                {
                    type: "intro",
                    title: "Why bar charts trip students up",
                    content: "Bar charts often present 6–10 categories. Listing each one wastes words and bores the examiner. The skill is GROUPING: which bars share a pattern, which is the outlier? Top responses describe groups, not individual bars."
                },
                {
                    type: "strategy",
                    title: "Comparison structures",
                    content: "EQUAL: as high as, similar to, comparable with. UNEQUAL (small): slightly higher than, marginally lower than, just above. UNEQUAL (large): twice as much as, three times higher than, significantly above, far below. SUPERLATIVE: the highest, the lowest, the most popular, the least common. Use multiples ('twice', 'three-fold') for impact."
                },
                {
                    type: "strategy",
                    title: "Grouping technique",
                    content: "Look at the chart. Mentally cluster bars: 'top tier', 'mid tier', 'bottom tier'. Or: 'rising group', 'declining group', 'stable group'. Or by category: 'all developed countries', 'all Asian countries'. Describe each group in a sentence with one or two illustrative numbers."
                },
                {
                    type: "example",
                    title: "Model answer (Band 7+)",
                    content: "PROMPT: The bar chart shows the percentage of people who exercise regularly, by age group, in five countries. MODEL: 'The bar chart compares the proportion of people exercising regularly across five age brackets in five countries — Australia, Brazil, Japan, the UK, and the US. Overall, exercise rates decline with age in every country, but the gap between young and old is far wider in some nations than others. Australia consistently records the highest rates: 78% of those aged 18–24 exercise regularly, falling to 41% among those 65+. The UK and US follow a similar pattern, with rates roughly 5–10 percentage points lower in each age bracket. By contrast, Brazil and Japan show steeper declines: in Japan, only 22% of over-65s exercise compared to 65% of 18–24-year-olds — a gap of more than 40 percentage points, the largest of any country shown.' (Word count: 153)"
                },
                {
                    type: "common_mistakes",
                    title: "Errors that limit your band",
                    content: "1) Listing every bar — boring and over the word limit. 2) Forgetting the overview. 3) Using only 'higher' and 'lower' — examiners want range. 4) Missing the outlier (the most striking data point). 5) Mismatching units (percentage vs absolute number)."
                }
            ],
            practice_items: [
                {
                    type: "writing_prompt",
                    content: {
                        prompt: "The bar chart compares the number of international tourists (in millions) visiting four cities — Paris, Bangkok, Dubai, and Istanbul — in 2010, 2015, and 2020.",
                        band_6_response: "The bar chart shows tourists in four cities. Paris had 15 million in 2010 and 18 million in 2015. Bangkok had 12 million and then 20 million. Dubai had 8 and 16. Istanbul had 9 and 11. In 2020 all numbers go down because of pandemic. Bangkok grew most. Paris and Istanbul did not grow much. (Listing, no clear overview, speculation about causes — penalty.)",
                        band_8_response: "The bar chart compares the volume of international tourist arrivals, in millions, in Paris, Bangkok, Dubai, and Istanbul across three years — 2010, 2015, and 2020. Overall, all four cities saw growth between 2010 and 2015, but tourist numbers in 2020 collapsed dramatically across the board, with Bangkok suffering the steepest decline. Paris was the most-visited city in 2010, attracting 15 million visitors, and grew modestly to 18 million by 2015. Bangkok, however, displayed the most dynamic growth, surging from 12 to 20 million over the same five years and overtaking Paris. Dubai doubled from 8 to 16 million, while Istanbul rose only marginally, from 9 to 11 million. The 2020 figures tell a uniform story of decline: every city dropped by at least 60%, with Bangkok plunging to just 4 million — a fivefold decrease from its 2015 peak. Even Paris, the most resilient, fell to 7 million. (Word count: 162)",
                        analysis: "Grouping by year, comparative multiples ('fivefold', 'doubled'), no causal speculation."
                    }
                }
            ],
            band_descriptors: {
                "6.0": "Covers main features; lists most bars; basic comparison vocab.",
                "7.0": "Groups data; uses comparison structures; clear overview.",
                "8.0": "Skilful grouping; multiples and proportions; sharp overview.",
                "9.0": "Effortless analysis; idiomatic precision."
            },
            next_steps: [
                "Lesson W1A 3: Pie Chart Description.",
                "Write 1 bar chart under 20-min timer."
            ]
        },

        // ---------- W T1 ACADEMIC LESSON 3 ----------
        {
            id: "ielts-w1a-3",
            section: "writing-t1-academic",
            band_target: "6.0-9.0",
            cefr: "B2-C2",
            title: "Pie Chart Description",
            subtitle: "Proportions and percentages — and the dual-pie comparison.",
            duration_min: 55,
            objectives: [
                "Use proportion vocabulary (a quarter, two-thirds, the majority).",
                "Compare two pies (often before/after or two countries).",
                "Verify percentages sum to 100% in each pie.",
                "Highlight the dominant slice and the smallest slice."
            ],
            sections: [
                {
                    type: "intro",
                    title: "Pie chart fundamentals",
                    content: "A pie chart shows parts of a whole. IELTS often gives you TWO pies for comparison: same data different times, or different countries with same categories. The challenge is to describe proportions, not raw numbers, and to compare across pies effectively."
                },
                {
                    type: "strategy",
                    title: "Proportion vocabulary",
                    content: "MAJORITY (>50%): the majority, more than half, over half. AROUND 50%: approximately half, roughly a half. AROUND 25%: a quarter, one in four, 25%. AROUND 33%: a third, one in three. SMALL (<10%): a small fraction, a tiny proportion, a minority of less than. EXACT: precisely / exactly X%. APPROXIMATE: about / around / approximately / roughly."
                },
                {
                    type: "strategy",
                    title: "Dual-pie comparison",
                    content: "When comparing two pies, focus on: (1) which slice grew, (2) which shrank, (3) which stayed similar, (4) the most dramatic change. Use linkers: 'compared to', 'whereas', 'in contrast', 'while'. Don't list every percentage — group changes."
                },
                {
                    type: "example",
                    title: "Model answer (Band 7+)",
                    content: "PROMPT: The two pie charts show how households spent their income in the UK in 1980 and 2020. MODEL: 'The two pie charts compare the breakdown of household spending in the UK between 1980 and 2020. Overall, while housing costs consumed a far larger share of income in 2020 than in 1980, spending on food fell by more than half, reflecting profound shifts in British household budgets over four decades. In 1980, food was the dominant expense at 32%, followed by housing (22%), transport (15%), entertainment (10%), clothing (10%), and savings (11%). By 2020, the picture had been transformed: housing had surged to become the single largest category at 38%, while food had dropped to 14% — less than half its earlier share. Transport remained relatively stable at 16%, and entertainment expanded modestly to 13%. The most striking decline came in clothing, which fell from 10% to just 4%, while savings showed a slight reduction to 9%, suggesting tighter household budgets overall.' (Word count: 158)"
                },
                {
                    type: "common_mistakes",
                    title: "Errors",
                    content: "1) Listing every slice in order. 2) Missing comparison between pies. 3) Confusing percentage with percentage point. 4) Giving causes ('because of inflation' — opinion, not allowed). 5) Wrong proportion language ('a quarter' for 18%)."
                }
            ],
            practice_items: [
                {
                    type: "writing_prompt",
                    content: {
                        prompt: "The pie charts show the energy mix in Country A in 2000 and 2020 (coal, gas, nuclear, hydroelectric, solar/wind).",
                        instruction: "Write a 150-word report comparing the two pies. Identify the largest shifts.",
                        sample_outline: "Intro: paraphrase. Overview: shift away from coal toward renewables. Body 1: 2000 data — coal dominant. Body 2: 2020 data — solar/wind grew most; coal halved."
                    }
                }
            ],
            band_descriptors: {
                "6.0": "Covers all slices; basic proportions; weak comparison.",
                "7.0": "Strong proportions; clear comparison structure; overview.",
                "8.0": "Sophisticated comparison; sharp overview; varied vocab.",
                "9.0": "Effortless integration; idiomatic precision."
            },
            next_steps: [
                "Lesson W1A 4: Table Description.",
                "Write 1 dual-pie response under 20-min timer."
            ]
        },

        // ---------- W T1 ACADEMIC LESSON 4 ----------
        {
            id: "ielts-w1a-4",
            section: "writing-t1-academic",
            band_target: "6.0-9.0",
            cefr: "B2-C2",
            title: "Table Description",
            subtitle: "The data-dense visual — pick the trends, ignore the noise.",
            duration_min: 55,
            objectives: [
                "Select 4–5 key data points from a 20+ cell table.",
                "Group rows or columns to find patterns.",
                "Use ranking language (the highest, the second-most, the least).",
                "Compare across rows AND columns where useful."
            ],
            sections: [
                {
                    type: "intro",
                    title: "Why tables intimidate",
                    content: "A table can have 4 columns x 5 rows = 20 numbers. You cannot describe all of them in 150 words. The skill is SELECTION: pick the most striking 4–5 figures that tell a story. Examiners reward intelligent selection, not comprehensive listing."
                },
                {
                    type: "strategy",
                    title: "What to select",
                    content: "(1) The largest value in the table. (2) The smallest value. (3) The biggest change (if time-series). (4) The most consistent column or row. (5) The outlier — a data point that breaks the pattern. These 5 numbers usually carry the story. Build your two body paragraphs around them."
                },
                {
                    type: "strategy",
                    title: "Ranking and comparison",
                    content: "RANKING: the highest, the lowest, came in second/third place, ranked first, dominated the category. COMPARISON: more than double, nearly half, on a par with, roughly comparable to. CONTRAST: by contrast, however, in stark contrast, whereas."
                },
                {
                    type: "example",
                    title: "Model answer fragment (Band 7+)",
                    content: "'The table compares average annual rainfall (mm) in five cities across four climate zones. Overall, tropical cities receive far more rainfall than continental ones, with the rainiest city receiving over ten times as much as the driest. Tropical Singapore tops the table at 2,340 mm, followed by Mumbai at 2,100 mm. Mediterranean Athens and continental Moscow trail far behind at 410 mm and 690 mm respectively. The starkest contrast is between Singapore and Cairo, the desert outlier, which receives a mere 180 mm — roughly one-thirteenth of Singapore's total. Mumbai stands out within the tropical zone for the extreme concentration of its rainfall: nearly 90% falls between June and September, whereas Singapore's rainfall is distributed evenly across the year.' (Word count: 124, can extend with second body paragraph.)"
                },
                {
                    type: "common_mistakes",
                    title: "Errors",
                    content: "1) Trying to mention every number. 2) No grouping. 3) Forgetting the ranking. 4) No outlier highlight. 5) Going over 200 words by listing."
                }
            ],
            practice_items: [
                {
                    type: "writing_prompt",
                    content: {
                        prompt: "The table shows university enrolment numbers across five faculties (Engineering, Arts, Business, Medicine, Sciences) at three universities in 2010 and 2020.",
                        sample_strategy: "Find the largest number, the smallest, the biggest growth, the biggest decline. Write about ONE row's striking shift and ONE column's stable pattern."
                    }
                }
            ],
            band_descriptors: {
                "6.0": "Lists too many numbers; weak grouping.",
                "7.0": "Selects key data; ranks; clear overview.",
                "8.0": "Sharp selection; comparison; outlier; varied vocab.",
                "9.0": "Effortless analysis."
            },
            next_steps: [
                "Lesson W1A 5: Process / Diagram Description.",
                "Write 1 table response under 20-min timer."
            ]
        },

        // ---------- W T1 ACADEMIC LESSON 5 ----------
        {
            id: "ielts-w1a-5",
            section: "writing-t1-academic",
            band_target: "6.0-9.0",
            cefr: "B2-C2",
            title: "Process / Diagram Description",
            subtitle: "Sequential language and the passive voice — the rare T1 task type that needs different skills.",
            duration_min: 55,
            objectives: [
                "Use passive voice for impersonal processes.",
                "Apply sequential connectors (first, next, subsequently, finally).",
                "Distinguish natural cycles from manufactured processes.",
                "Number stages and describe each clearly."
            ],
            sections: [
                {
                    type: "intro",
                    title: "Why processes need different language",
                    content: "Process diagrams (e.g. how cement is made, how rain forms, how recycling works) require describing stages, not numbers. The vocabulary is: passive verbs, sequence connectors, technical nouns. There is NO trend vocabulary needed."
                },
                {
                    type: "strategy",
                    title: "Passive voice — your default",
                    content: "Most processes don't have a human agent. Use passive: 'The ore is crushed', 'Water is heated', 'The mixture is poured into moulds'. Passive structure: BE + past participle. Mix passive with active where natural ('The process begins…', 'Water flows from…')."
                },
                {
                    type: "strategy",
                    title: "Sequence connectors",
                    content: "BEGINNING: First, To begin with, The process begins when, Initially. MIDDLE: Next, Then, After this, Subsequently, Following this, At this stage. END: Finally, Lastly, In the final stage, Ultimately. CYCLES: This cycle then repeats, The process is then repeated, Thus the cycle continues."
                },
                {
                    type: "example",
                    title: "Model answer (Band 7+)",
                    content: "PROMPT: The diagram illustrates how rainwater is collected, filtered, and stored for household use. MODEL: 'The diagram illustrates the four-stage process by which rainwater is captured and prepared for domestic use, beginning at a roof and ending at indoor taps. Overall, the system consists of collection, filtration, storage, and distribution, with each stage feeding directly into the next. To begin with, rainwater is gathered as it falls onto a sloped roof and is channelled through gutters into a vertical downpipe. From there, it passes through a leaf filter, which removes debris before the water enters the next stage. Subsequently, the water flows into a sediment tank where finer particles settle to the bottom. Cleaner water rises to the top and is then transferred via a pump into a large underground storage tank. Finally, when needed, the stored water is pumped through a fine-mesh filter and a UV steriliser before being distributed to taps throughout the house.' (Word count: 156)"
                },
                {
                    type: "common_mistakes",
                    title: "Errors",
                    content: "1) Using past simple ('was crushed') for a process described in general terms — use present passive ('is crushed'). 2) Skipping sequence connectors. 3) Adding causes or evaluations. 4) Using 'I' or 'we'. 5) Misordering stages."
                }
            ],
            practice_items: [
                {
                    type: "writing_prompt",
                    content: {
                        prompt: "The diagram shows the process of producing chocolate from cocoa beans (drying, fermenting, roasting, grinding, conching, tempering, moulding).",
                        sample_strategy: "7 stages = ~22 words per stage if straightforward. Group: collection (drying+fermenting), processing (roasting+grinding), refinement (conching+tempering), final (moulding)."
                    }
                }
            ],
            band_descriptors: {
                "6.0": "Most stages described; mixed tense; basic connectors.",
                "7.0": "Consistent passive; clear sequence; overview.",
                "8.0": "Skilful sequencing; varied connectors; precise verbs.",
                "9.0": "Effortless and natural."
            },
            next_steps: [
                "Lesson W1A 6: Map / Comparison Description.",
                "Write 1 process under 20-min timer."
            ]
        },

        // ---------- W T1 ACADEMIC LESSON 6 ----------
        {
            id: "ielts-w1a-6",
            section: "writing-t1-academic",
            band_target: "6.0-9.0",
            cefr: "B2-C2",
            title: "Map / Comparison Description",
            subtitle: "Before-and-after maps — describe change, not just objects.",
            duration_min: 55,
            objectives: [
                "Describe spatial changes between two maps.",
                "Use directional and locative vocabulary effectively.",
                "Choose between past simple and present perfect for changes.",
                "Group changes thematically (built / removed / converted)."
            ],
            sections: [
                {
                    type: "intro",
                    title: "Map task fundamentals",
                    content: "A map task usually shows a location at two points in time (1990 vs 2020) and asks you to describe how it changed. Or it shows two proposed designs. The skill is identifying which features were ADDED, REMOVED, EXPANDED, RELOCATED, or CONVERTED."
                },
                {
                    type: "strategy",
                    title: "Change vocabulary",
                    content: "ADDED: was built, was constructed, has been added, has appeared. REMOVED: was demolished, has been removed, no longer exists, was cleared. EXPANDED: was extended, has been enlarged, doubled in size. CONVERTED: was transformed into, was converted to, was replaced by. RELOCATED: was moved to, was relocated. UNCHANGED: remains, is unchanged, retains."
                },
                {
                    type: "strategy",
                    title: "Spatial vocabulary",
                    content: "DIRECTIONS: north / south / east / west of, in the north-east corner, along the northern edge. PROXIMITY: adjacent to, beside, opposite, across from, between A and B. ALONG: alongside the river, running parallel to the road. CENTRAL: in the centre, at the heart of the town."
                },
                {
                    type: "example",
                    title: "Model answer fragment",
                    content: "'The two maps illustrate how the village of Greenfield evolved between 1985 and 2020. Overall, the village transformed from a predominantly agricultural settlement into a small commuter town, with farmland giving way to housing and a new transport link bisecting the area. In 1985, Greenfield comprised a single main street with a church at its northern end, a primary school adjacent to a small shop, and large fields covering most of the surrounding land. By 2020, the picture had changed dramatically. The fields to the south had been replaced by two housing estates, while a new ring road had been constructed, encircling the village from east to west. The primary school remained in its original location, but the small shop had been demolished and replaced by a supermarket. A railway station had appeared in the north-east, providing direct services to the nearest city.' (Word count: 153)"
                },
                {
                    type: "common_mistakes",
                    title: "Errors",
                    content: "1) Listing each building one by one. 2) Mixing tenses inconsistently. 3) Forgetting the overview. 4) Vague spatial language. 5) Not noting the unchanged features (which create useful contrast)."
                }
            ],
            practice_items: [
                {
                    type: "writing_prompt",
                    content: {
                        prompt: "The two maps show the layout of a coastal town centre in 1990 and after 2025 redevelopment.",
                        sample_strategy: "Group changes: removed (old factory, parking), added (pedestrian zone, cafés, plaza), modified (harbour expanded). Use thematic grouping in body paragraphs."
                    }
                }
            ],
            band_descriptors: {
                "6.0": "Most changes mentioned; weak grouping; basic spatial vocab.",
                "7.0": "Grouped changes; clear past tense; spatial range.",
                "8.0": "Thematic grouping; varied vocabulary; sharp overview.",
                "9.0": "Effortless and natural."
            },
            next_steps: [
                "Move to Writing T1 General Training section.",
                "Write 1 map task under 20-min timer."
            ]
        }

        // ============================================================
        // WRITING TASK 1 GENERAL TRAINING — 4 LESSONS
        // ============================================================

        // ---------- W T1 GT LESSON 1 ----------
        ,{
            id: "ielts-w1g-1",
            section: "writing-t1-general",
            band_target: "6.0-9.0",
            cefr: "B2-C2",
            title: "Formal Letters",
            subtitle: "Complaints, applications, requests — the bedrock of GT Writing.",
            duration_min: 60,
            objectives: [
                "Identify when a formal register is required.",
                "Use formal openings (Dear Sir/Madam) and closings (Yours faithfully/sincerely).",
                "Structure a 3-bullet GT letter into 3 paragraphs of equal weight.",
                "Use polite, distance-creating language without sounding cold."
            ],
            sections: [
                {
                    type: "intro",
                    title: "When the letter is formal",
                    content: "GT Task 1 always gives you 3 bullet points to address. Recipient determines tone. FORMAL = unknown recipient (To Whom It May Concern, customer service, an organisation), or someone of higher status whose name you don't know. Examples: complaint to a shop manager, application for a job, request to the local council."
                },
                {
                    type: "strategy",
                    title: "Opening and closing conventions",
                    content: "Formal: 'Dear Sir or Madam,' (no name) → close with 'Yours faithfully,'. Formal but you have name: 'Dear Mr Smith,' → close with 'Yours sincerely,'. Sign your name printed on the next line. NEVER use 'Hi' or 'Hey' in formal. NEVER use contractions ('I am' not 'I'm', 'cannot' not 'can't')."
                },
                {
                    type: "strategy",
                    title: "Paragraph structure",
                    content: "PARAGRAPH 1 (Opening, 2–3 sentences): state purpose. 'I am writing to express my dissatisfaction with…', 'I am writing in response to your advertisement for…'. PARAGRAPH 2 (Detail of the issue): describe the situation in 4–5 sentences using specific dates, products, references. PARAGRAPH 3 (Request and close): state what you expect or request. 'I would appreciate a full refund…', 'I look forward to your prompt response.' Word count: 150+."
                },
                {
                    type: "strategy",
                    title: "Formal phrase bank",
                    content: "OPENINGS: 'I am writing to draw your attention to…', 'I would like to bring to your attention…'. POLITE COMPLAINTS: 'I was extremely disappointed to find…', 'It was most inconvenient to discover…'. REQUESTS: 'I would be grateful if you could…', 'I would appreciate it if you would…'. CLOSINGS: 'I look forward to hearing from you at your earliest convenience.', 'Thank you for your attention to this matter.'"
                },
                {
                    type: "example",
                    title: "Model formal letter (Band 7+)",
                    content: "PROMPT: You recently bought a piece of electronic equipment that did not work. Write a letter to the shop manager. Explain what you bought, what the problem is, and what you would like them to do.\n\nMODEL:\n'Dear Sir or Madam,\n\nI am writing to express my disappointment with a laptop computer I purchased from your branch on 14 March, with receipt number 287-44J. Unfortunately, the device has developed a serious fault that has rendered it unusable.\n\nThe laptop in question is a model TXR-15, costing £849. From the moment I unboxed it, the screen flickered intermittently, and after just three days, it began shutting down without warning every twenty minutes. I have followed the troubleshooting steps in the user manual and reinstalled the operating system, but the problem persists. As I rely on the laptop for my postgraduate studies, this fault has caused me considerable inconvenience.\n\nGiven that the product is well within its warranty period and clearly defective, I would be grateful if you could either provide a full refund or replace it with a new unit of the same model at no extra cost. I have enclosed a copy of my receipt and would be happy to return the faulty device at your convenience. I look forward to your prompt reply.\n\nYours faithfully,\n\nMaria Castillo'\n(Word count: 196)"
                },
                {
                    type: "common_mistakes",
                    title: "Errors that cap your band",
                    content: "1) Mixing formal and informal ('Hi Sir'). 2) Using contractions in formal letters. 3) Forgetting one of the 3 bullet points. 4) Closing with 'Yours sincerely' to 'Sir or Madam' (must be 'Yours faithfully'). 5) No paragraph breaks. 6) Under 150 words."
                }
            ],
            practice_items: [
                {
                    type: "writing_prompt",
                    content: {
                        prompt: "You have seen a job advertisement for a position you are interested in. Write a letter to the employer. Tell them where you saw the advert, explain why you are interested, describe your relevant experience.",
                        sample_outline: "Para 1: source of advert + position. Para 2: motivation + qualifications. Para 3: experience + close (request interview).",
                        key_phrases: ["I am writing in response to the position of X advertised in…", "I believe my background in X makes me well-suited to…", "I would welcome the opportunity to discuss my application in person."]
                    }
                }
            ],
            band_descriptors: {
                "6.0": "Correct formal register but mechanical phrasing; covers all 3 bullets.",
                "7.0": "Consistent register; varied phrasing; clear paragraphing.",
                "8.0": "Sophisticated formal vocabulary; nuanced tone; rare errors.",
                "9.0": "Effortless and idiomatic."
            },
            next_steps: [
                "Lesson W1G 2: Semi-Formal Letters.",
                "Write 1 formal complaint under 20-min timer."
            ]
        },

        // ---------- W T1 GT LESSON 2 ----------
        {
            id: "ielts-w1g-2",
            section: "writing-t1-general",
            band_target: "6.0-9.0",
            cefr: "B2-C2",
            title: "Semi-Formal Letters",
            subtitle: "Manager, colleague, neighbour — the tricky middle register.",
            duration_min: 55,
            objectives: [
                "Pitch tone between formal and informal.",
                "Use first-name address while keeping politeness.",
                "Switch register fluidly within a single letter.",
                "Avoid the two opposite traps: too stiff, too chatty."
            ],
            sections: [
                {
                    type: "intro",
                    title: "What semi-formal means",
                    content: "Semi-formal is used with people you know but with whom a friendly-but-respectful tone is needed: your manager you call by first name, a colleague, a neighbour you greet daily, a business contact you've met. Contractions are usually OK; first names are fine; idioms are limited."
                },
                {
                    type: "strategy",
                    title: "Opening and closing",
                    content: "Opening: 'Dear David,' or 'Dear Mrs Patel,' (using known surname). Closing: 'Best regards,' / 'Kind regards,' / 'With best wishes,' — NEVER 'Yours faithfully'. Sign with first name only if recipient knows you well; full name otherwise."
                },
                {
                    type: "strategy",
                    title: "Tone calibration",
                    content: "Avoid: 'Dear Sir' (too formal for a known person). Avoid: 'Hi Dave!' (too casual for a manager). Use: 'Dear David,' or 'Dear Mr Roberts,'. Mid-letter, you may use 'I'd' and 'I'm' (contractions OK), but maintain politeness markers ('please', 'I'd appreciate', 'if possible')."
                },
                {
                    type: "example",
                    title: "Model semi-formal letter",
                    content: "PROMPT: Write to your manager asking for one week of leave next month, explaining why and offering to cover your work.\n\nMODEL:\n'Dear David,\n\nI hope this message finds you well. I am writing to formally request one week of annual leave from 12 to 18 June, if this is possible.\n\nThe reason for the request is that my elder sister is getting married in Lima on 14 June, and I would very much like to be there for the family celebration. As we have not all been together for over three years, this trip is particularly meaningful.\n\nI have already spoken with Marco and Sofía, who have both kindly agreed to cover the weekly Friday client meetings during my absence. I will also make sure all reports for May are submitted ahead of schedule, and I'll be reachable by email for anything urgent.\n\nThank you for considering my request, David. Please let me know if you would like to discuss this in person.\n\nBest regards,\n\nElena'\n(Word count: 162)"
                },
                {
                    type: "common_mistakes",
                    title: "Errors",
                    content: "1) Sliding into formal phrasing ('Dear Sir or Madam') when name is known. 2) Sliding into informal ('Hey Dave!'). 3) Forgetting one bullet. 4) Closing with 'Yours faithfully'. 5) Too many idioms ('Hope you're keeping your head above water')."
                }
            ],
            practice_items: [
                {
                    type: "writing_prompt",
                    content: {
                        prompt: "You are organising a community event in your neighbourhood. Write to your neighbour. Invite them, explain what the event involves, and ask them to help with one aspect.",
                        sample_outline: "Para 1: greet + invitation. Para 2: event details (date, place, activities). Para 3: specific help request (e.g. bake a cake / lend chairs)."
                    }
                }
            ],
            band_descriptors: {
                "6.0": "Recognises semi-formal but slips into formal or informal at moments.",
                "7.0": "Consistent register; appropriate contractions; clear tone.",
                "8.0": "Fluid switches; warmth without informality.",
                "9.0": "Effortless and natural."
            },
            next_steps: [
                "Lesson W1G 3: Informal Letters.",
                "Write 1 semi-formal letter to a colleague."
            ]
        },

        // ---------- W T1 GT LESSON 3 ----------
        {
            id: "ielts-w1g-3",
            section: "writing-t1-general",
            band_target: "6.0-9.0",
            cefr: "B2-C2",
            title: "Informal Letters",
            subtitle: "Friend, family — warm, natural, but still structured.",
            duration_min: 50,
            objectives: [
                "Use first-name greeting, contractions, and idioms appropriately.",
                "Maintain coherence even in a casual register.",
                "Avoid slipping into slang that examiners penalise.",
                "Hit 150 words without padding."
            ],
            sections: [
                {
                    type: "intro",
                    title: "When informal is right",
                    content: "Informal = writing to a friend, family member, or someone you know well. Contractions, idioms, exclamations, and rhetorical questions are all welcome. But the letter still needs structure — IELTS rewards organisation regardless of register."
                },
                {
                    type: "strategy",
                    title: "Opening and closing",
                    content: "Opening: 'Hi Sara!' / 'Dear Mum,' / 'Hey Tom,' . Closing: 'Take care,', 'Lots of love,', 'Speak soon,', 'Hope to hear from you soon!'. Sign with first name only or nickname."
                },
                {
                    type: "strategy",
                    title: "Tone markers",
                    content: "USE: contractions ('I'm', 'don't', 'won't'), exclamations ('Great news!'), questions ('How are you?'), softeners ('to be honest', 'you know'), warmth phrases ('I miss you', 'thinking of you'). AVOID: heavy slang ('innit', 'gonna', 'lol'), formal vocab ('thereafter', 'consequently'), cold tone."
                },
                {
                    type: "example",
                    title: "Model informal letter",
                    content: "PROMPT: Write to a friend describing a recent holiday. Tell them where you went, what you did, and invite them to visit the same place with you next year.\n\nMODEL:\n'Hi Karim!\n\nHow are you? I hope work hasn't been too crazy. I've been meaning to write for ages — sorry I went quiet, but I've got loads to tell you!\n\nI just got back from two amazing weeks in northern Vietnam. We started in Hanoi, which is wonderfully chaotic — scooters everywhere, incredible street food, and the best coffee I've ever tasted. After that, we took an overnight train up to Sapa and trekked through the rice terraces for three days. Honestly, I don't think I've ever seen anywhere so beautiful. The people we met were so kind, and the food was unbelievable.\n\nThis is the bit you really need to hear: I'm planning to go back next October, and I'd absolutely love it if you came too. I know you've been talking about taking a proper break, and trust me, this is the place. We could share a guesthouse to keep costs down, and I'll happily play tour guide.\n\nLet me know what you think — even just roughly. Miss you loads!\n\nTake care,\n\nDanny'\n(Word count: 198)"
                },
                {
                    type: "common_mistakes",
                    title: "Errors",
                    content: "1) Heavy slang that confuses examiners. 2) Too short (under 150 words). 3) No structure — one big paragraph. 4) Forgetting one of the 3 bullets. 5) Becoming overly formal mid-letter."
                }
            ],
            practice_items: [
                {
                    type: "writing_prompt",
                    content: {
                        prompt: "Write to a friend who is moving to your city. Welcome them, describe the area you live in, and offer to help them settle in.",
                        sample_outline: "Para 1: warm welcome + excitement. Para 2: description of area (cafés, parks, transport). Para 3: specific offers (collect from airport, show around)."
                    }
                }
            ],
            band_descriptors: {
                "6.0": "Casual but flat; basic structure.",
                "7.0": "Warm tone; varied phrasing; clear paragraphs.",
                "8.0": "Natural voice; appropriate idioms; sharp organisation.",
                "9.0": "Effortless and idiomatic."
            },
            next_steps: [
                "Lesson W1G 4: Common Phrases & Closings by Tone.",
                "Write 1 informal letter to a friend."
            ]
        },

        // ---------- W T1 GT LESSON 4 ----------
        {
            id: "ielts-w1g-4",
            section: "writing-t1-general",
            band_target: "6.0-9.0",
            cefr: "B2-C2",
            title: "Common Phrases & Closings by Tone",
            subtitle: "The phrase bank that lets you write any letter in any register.",
            duration_min: 50,
            objectives: [
                "Memorise 12 openings, 12 body phrases, 12 closings across registers.",
                "Match phrases to recipient correctly.",
                "Adapt the same content into formal / semi-formal / informal versions.",
                "Build a personal phrase bank for the test."
            ],
            sections: [
                {
                    type: "intro",
                    title: "Why phrase banks matter",
                    content: "Under 20-minute pressure, you don't have time to invent phrasing. The fastest band-7+ writers have memorised 30–40 modular phrases that they assemble. This lesson gives you the phrase bank and shows how to deploy it."
                },
                {
                    type: "strategy",
                    title: "Phrase bank — OPENINGS",
                    content: "FORMAL: 'I am writing to express…', 'I am writing in response to…', 'I am writing with regard to…', 'I would like to bring to your attention…'. SEMI-FORMAL: 'I hope this message finds you well.', 'I am writing to ask whether…', 'I'd like to discuss the matter of…'. INFORMAL: 'How are you?', 'It's been ages!', 'Hope you're well.', 'Just dropping you a line to…'."
                },
                {
                    type: "strategy",
                    title: "Phrase bank — REQUESTS",
                    content: "FORMAL: 'I would be grateful if you could…', 'I would appreciate it if you would…', 'Could you possibly…'. SEMI-FORMAL: 'I'd really appreciate it if you could…', 'Would you mind…', 'Could you let me know…'. INFORMAL: 'Could you do me a favour and…', 'Any chance you could…', 'Would you mind…'."
                },
                {
                    type: "strategy",
                    title: "Phrase bank — APOLOGIES & EXPLANATIONS",
                    content: "FORMAL: 'I sincerely apologise for…', 'Please accept my apologies for…', 'I regret to inform you that…'. SEMI-FORMAL: 'I am very sorry that…', 'I'm afraid I won't be able to…'. INFORMAL: 'I'm so sorry I missed…', 'Sorry I haven't been in touch.'"
                },
                {
                    type: "strategy",
                    title: "Phrase bank — CLOSINGS",
                    content: "FORMAL: 'I look forward to your prompt reply.', 'Thank you in advance for your attention to this matter.', 'I await your response.' Sign: 'Yours faithfully,' (no name) / 'Yours sincerely,' (named). SEMI-FORMAL: 'Thank you for your time.', 'Looking forward to hearing from you.' Sign: 'Best regards,' / 'Kind regards,'. INFORMAL: 'Take care!', 'Speak soon!', 'Give my love to the family!'. Sign: 'Love,' / 'Cheers,' / first name only."
                },
                {
                    type: "example",
                    title: "Same content, three registers",
                    content: "MESSAGE: I cannot attend the meeting on Friday because I have a doctor's appointment.\n\nFORMAL: 'I regret to inform you that I shall be unable to attend the meeting scheduled for Friday, as I have a previously arranged medical appointment.'\n\nSEMI-FORMAL: 'I'm afraid I won't be able to make Friday's meeting — I have a doctor's appointment that I can't reschedule.'\n\nINFORMAL: 'Just letting you know I can't make Friday — got a doctor's thing.'"
                },
                {
                    type: "common_mistakes",
                    title: "Errors",
                    content: "1) Mixing registers within one letter. 2) Wrong sign-off ('Yours sincerely' to 'Sir or Madam'). 3) Forgetting closing entirely. 4) Direct translation from native language ('I send you greetings'). 5) Over-formal informal letters that sound robotic."
                }
            ],
            practice_items: [
                {
                    type: "writing_prompt",
                    content: {
                        prompt: "Take this brief and write it as (1) formal, (2) semi-formal, (3) informal: 'I want to thank someone for helping me.'",
                        sample_responses: {
                            formal: "I am writing to express my sincere gratitude for your invaluable assistance with my application. Without your timely intervention, the matter would not have been resolved successfully.",
                            semi_formal: "I just wanted to say a proper thank you for your help last week. It really made a difference, and I'm very grateful.",
                            informal: "Just wanted to say a HUGE thanks for the other day — you're a star! Couldn't have done it without you."
                        }
                    }
                }
            ],
            band_descriptors: {
                "6.0": "Uses some bank phrases; occasional register slip.",
                "7.0": "Reliable register matching; varied phrasing.",
                "8.0": "Skilful adaptation; idiomatic precision.",
                "9.0": "Effortless and natural across all registers."
            },
            next_steps: [
                "Move to Writing T2 section, Lesson 1.",
                "Drill: write the same prompt in 3 registers."
            ]
        },

        // ============================================================
        // WRITING TASK 2 — 8 LESSONS
        // ============================================================

        // ---------- W T2 LESSON 1 ----------
        {
            id: "ielts-w2-1",
            section: "writing-t2",
            band_target: "6.0-9.0",
            cefr: "B2-C2",
            title: "Opinion Essays (Agree/Disagree)",
            subtitle: "Take a clear stance and defend it across 4 paragraphs.",
            duration_min: 70,
            objectives: [
                "Identify Opinion-type prompts ('To what extent do you agree?').",
                "Decide between fully agree, partly agree, fully disagree.",
                "Build a 4-paragraph essay: intro / body 1 / body 2 / conclusion.",
                "State a clear thesis in paragraph 1 and reaffirm in paragraph 4."
            ],
            sections: [
                {
                    type: "intro",
                    title: "Recognising opinion prompts",
                    content: "Opinion prompts ask: 'To what extent do you agree or disagree?', 'Do you agree?', 'What is your opinion?'. Your job: state a position clearly and defend it with reasons and examples. There must be a single, consistent stance throughout the essay. Sitting on the fence drops you to Band 5."
                },
                {
                    type: "strategy",
                    title: "Three valid positions",
                    content: "POSITION 1 — Fully agree: 'I strongly agree because A and B.' Easy to argue clearly; often the safest choice. POSITION 2 — Fully disagree: 'I strongly disagree because A and B.' POSITION 3 — Partly agree: 'I agree that X is true, but I disagree that Y.' Higher band ceiling but harder to keep consistent — recommended only if you're confident. NOT RECOMMENDED: 'It depends.' This often becomes incoherent."
                },
                {
                    type: "strategy",
                    title: "The 4-paragraph template",
                    content: "PARA 1 (Intro, 50 words): Paraphrase the prompt + state your thesis (clear position) + preview your two reasons. PARA 2 (Body 1, 100 words): First reason — topic sentence, explanation, example, mini-conclusion (PEEEL). PARA 3 (Body 2, 100 words): Second reason — same structure. PARA 4 (Conclusion, 30 words): Restate position; summarise reasons; do NOT add new ideas. Total: ~280 words (over the 250-word minimum)."
                },
                {
                    type: "strategy",
                    title: "Stance language",
                    content: "FULLY AGREE: 'I firmly agree that…', 'I am convinced that…', 'There is little doubt that…'. FULLY DISAGREE: 'I strongly disagree with this view.', 'I am unconvinced by the claim that…'. PARTLY: 'While I agree that X, I cannot accept that Y.', 'I agree to a certain extent, but…'. AVOID: 'I think', 'In my opinion' (overused — vary)."
                },
                {
                    type: "example",
                    title: "Model essay (Band 7+)",
                    content: "PROMPT: Some people believe that universities should focus only on subjects useful for future employment, such as science and technology. To what extent do you agree or disagree?\n\nMODEL:\n'In recent years, debate has intensified over whether universities should restrict their offerings to subjects with clear employment value, such as engineering or computer science. While I acknowledge the importance of equipping graduates for the labour market, I firmly disagree with the view that universities should narrow their focus exclusively to vocational disciplines. I believe both intellectual breadth and humanities research remain essential.\n\nFirstly, universities have always served a broader function than job training. They cultivate critical thinking, ethical reasoning, and cultural understanding — skills that disciplines like philosophy, history, and literature develop better than any technical course. A society without scholars who study these subjects risks losing the capacity to question its own assumptions. For example, much of the public debate around artificial intelligence today depends on philosophical and ethical insights, not engineering knowledge alone.\n\nSecondly, the assumption that humanities degrees lack employment value is empirically questionable. Many of the world's most successful entrepreneurs, lawyers, journalists, and policymakers studied subjects such as English, anthropology, or political science. Employers in fields like consulting and management consistently report that graduates with strong analytical writing and communication skills outperform purely technical hires. Closing humanities departments would deprive the economy of these graduates, not enrich it.\n\nIn conclusion, although STEM subjects play a vital role in modern universities, restricting study to them would be both intellectually impoverishing and economically short-sighted. A balanced curriculum that values both technical and humanistic learning serves students and society far more effectively.'\n(Word count: 286)"
                },
                {
                    type: "common_mistakes",
                    title: "Mistakes that cap your band at 5–6",
                    content: "1) Sitting on the fence — never commit to a position. 2) Switching positions mid-essay. 3) No examples (just abstract claims). 4) Using personal anecdotes ('My friend studied X…') — examiners want general examples. 5) Under 250 words — automatic penalty. 6) Repeating the prompt verbatim. 7) Listing — 'Firstly… Secondly… Thirdly… Fourthly…' (max two body reasons in 280 words)."
                }
            ],
            practice_items: [
                {
                    type: "writing_prompt",
                    content: {
                        prompt: "Some people believe that wealthy countries have a moral obligation to share their wealth with poorer nations through aid. Others argue that this aid is ineffective and creates dependence. To what extent do you agree?",
                        thinking_pattern: "Pick: agree (aid is moral and beneficial), or disagree (aid is wasted, creates dependency), or partly (yes moral, but should be reform-conditional). Choose one and stick with it.",
                        band_6_response_summary: "Clear position but only one reason developed; example is anecdotal; conclusion adds new ideas; word count 230.",
                        band_8_response_summary: "Strong thesis with two reasons previewed; both reasons fully developed with concrete general examples (Marshall Plan, Korean miracle); sophisticated linking; conclusion synthesises; 290 words."
                    }
                }
            ],
            band_descriptors: {
                "6.0": "Clear position; basic reasons; mostly relevant; some grammar errors.",
                "7.0": "Clear thesis; two well-developed reasons; concrete examples; varied vocabulary.",
                "8.0": "Sophisticated argumentation; nuanced position; precise vocabulary; rare errors.",
                "9.0": "Effortless persuasion; idiomatic; insightful examples."
            },
            next_steps: [
                "Lesson W2 2: Discussion Essays (Discuss Both Views + Opinion).",
                "Write 1 opinion essay under 40-min timer."
            ]
        },

        // ---------- W T2 LESSON 2 ----------
        {
            id: "ielts-w2-2",
            section: "writing-t2",
            band_target: "6.0-9.0",
            cefr: "B2-C2",
            title: "Discussion Essays (Discuss Both Views + Opinion)",
            subtitle: "Discuss both sides fairly — then commit to one.",
            duration_min: 70,
            objectives: [
                "Recognise discussion prompts ('Discuss both views and give your opinion').",
                "Allocate equal weight to both views, then state a stance.",
                "Build a 5-paragraph structure: intro / view 1 / view 2 / opinion / conclusion. (Or 4-paragraph with opinion folded in.)",
                "Avoid the most common error: forgetting to give YOUR opinion."
            ],
            sections: [
                {
                    type: "intro",
                    title: "What discussion prompts demand",
                    content: "Phrases: 'Discuss both these views and give your own opinion.' / 'Some people think X, while others argue Y. Discuss both sides.' This is the MOST COMMON Task 2 type. You must (a) explain both views fairly, (b) give your own opinion clearly. Missing either drops you to Band 5."
                },
                {
                    type: "strategy",
                    title: "5-paragraph structure (recommended)",
                    content: "PARA 1 (Intro, ~50 w): paraphrase prompt + brief mention of two views + state your stance. PARA 2 (View 1, ~80 w): explain the first view + reasons + example. Use neutral language: 'Proponents argue…', 'Some maintain that…'. PARA 3 (View 2, ~80 w): same for the second view. PARA 4 (Your opinion, ~70 w): state which view you find more persuasive and why. PARA 5 (Conclusion, ~30 w): restate stance briefly. Total: ~310 words."
                },
                {
                    type: "strategy",
                    title: "Alternative 4-paragraph structure",
                    content: "PARA 1 (Intro): paraphrase + state stance immediately. PARA 2 (Body 1): View 1 + brief why I disagree (or partly agree). PARA 3 (Body 2): View 2 + why I agree. PARA 4 (Conclusion): restate. This works well at Band 7+ but requires confident weaving."
                },
                {
                    type: "strategy",
                    title: "Neutral discussion language",
                    content: "INTRODUCING VIEW: 'On the one hand…', 'Proponents of X argue that…', 'Some people maintain…', 'It can be argued that…'. PRESENTING THE OTHER: 'On the other hand…', 'Conversely…', 'In contrast, others contend…'. STATING YOUR POSITION: 'In my view…', 'Personally, I find the second argument more persuasive because…', 'While both views have merit, I lean towards…'."
                },
                {
                    type: "example",
                    title: "Model essay (Band 7+)",
                    content: "PROMPT: Some people believe that children should start learning a foreign language as early as possible, ideally before age six. Others argue that foreign languages should be introduced only in secondary school. Discuss both views and give your own opinion.\n\nMODEL:\n'There is ongoing debate over the optimal age for children to begin studying a foreign language. While some advocate immersion before the age of six, others argue that secondary school is early enough. In my view, the case for an early start is significantly stronger, although secondary instruction has practical merit.\n\nSupporters of early language learning point to neuroscience: the human brain absorbs phonetic and grammatical patterns most effortlessly before puberty. Children exposed to a second language at three or four often achieve native-like pronunciation, something far harder to acquire later. Countries such as Singapore and the Netherlands, where bilingualism begins in early childhood, consistently produce graduates who function professionally in two or more languages.\n\nOn the other hand, critics argue that introducing a foreign language too early can confuse children still consolidating their first language, and that valuable curriculum time would be better spent on literacy and numeracy. Furthermore, in countries with strained education budgets, training enough specialised early-years language teachers may be unrealistic.\n\nWeighing both arguments, I find the early-start position more convincing. The cognitive evidence for a sensitive period in language acquisition is robust, and concerns about confusion are not supported by recent bilingual research. Practical constraints are real but solvable; many countries have shown that even modest weekly exposure in early years yields measurable benefits.\n\nIn conclusion, while delaying language instruction until secondary school is feasible, beginning earlier offers clear linguistic and cognitive advantages and should be the goal wherever resources allow.'\n(Word count: 305)"
                },
                {
                    type: "common_mistakes",
                    title: "Errors that drop your band",
                    content: "1) Forgetting to give your opinion. 2) Treating one view sympathetically and the other dismissively (unfair = lower coherence). 3) Repeating the same idea on both sides. 4) Mixing up which paragraph is which view. 5) Stance flip-flop in the conclusion."
                }
            ],
            practice_items: [
                {
                    type: "writing_prompt",
                    content: {
                        prompt: "Some people believe that working from home is better for both employees and employers. Others argue that office attendance produces stronger team performance. Discuss both views and give your own opinion.",
                        sample_outline: "Para 1: paraphrase + your stance (e.g. hybrid is best). Para 2: WFH benefits (productivity, work-life balance). Para 3: office benefits (collaboration, mentorship). Para 4: your reasoning. Para 5: brief conclusion."
                    }
                }
            ],
            band_descriptors: {
                "6.0": "Both views covered; opinion stated late or unclearly; basic vocabulary.",
                "7.0": "Both views fairly developed; clear opinion; varied linkers.",
                "8.0": "Nuanced engagement with both views; precise vocabulary; sharp opinion.",
                "9.0": "Effortless balance and persuasion."
            },
            next_steps: [
                "Lesson W2 3: Problem-Solution Essays.",
                "Write 1 discussion essay under 40-min timer."
            ]
        },

        // ---------- W T2 LESSON 3 ----------
        {
            id: "ielts-w2-3",
            section: "writing-t2",
            band_target: "6.0-9.0",
            cefr: "B2-C2",
            title: "Problem-Solution Essays",
            subtitle: "Identify problems, propose realistic solutions — and link cause to fix.",
            duration_min: 65,
            objectives: [
                "Recognise problem-solution prompts.",
                "Build cause-effect chains in problem paragraphs.",
                "Propose specific solutions with mechanisms ('how it would work').",
                "Match solutions to the problems you identified."
            ],
            sections: [
                {
                    type: "intro",
                    title: "Recognising problem-solution prompts",
                    content: "Phrases: 'What problems does X cause and what solutions can be implemented?' / 'Why is X a problem? How can it be solved?' / 'What are the causes of X and what can be done?' The structure: identify problems (or causes), then propose solutions. Solutions should LOGICALLY ADDRESS the problems you raised."
                },
                {
                    type: "strategy",
                    title: "4-paragraph structure",
                    content: "PARA 1 (Intro, ~50 w): paraphrase + signal the structure ('This essay will examine two key problems and suggest practical solutions.'). PARA 2 (Problems, ~110 w): two related problems with cause-effect explanation and an example. PARA 3 (Solutions, ~110 w): two solutions, each addressing one of the problems, with mechanism. PARA 4 (Conclusion, ~30 w): summarise."
                },
                {
                    type: "strategy",
                    title: "Cause-effect language",
                    content: "CAUSE: 'is largely caused by', 'stems from', 'is rooted in', 'is driven by'. EFFECT: 'leads to', 'results in', 'gives rise to', 'has consequences for', 'culminates in'. CHAINS: 'X leads to Y, which in turn produces Z'. AVOID: vague 'because of' alone."
                },
                {
                    type: "strategy",
                    title: "Solution language",
                    content: "PROPOSING: 'One effective remedy would be…', 'Governments could introduce…', 'A practical step would be to…'. MECHANISM: 'This would work by…', 'The intended effect is…', 'This would directly address X by…'. EVALUATION: 'Although not without cost, this measure would…'."
                },
                {
                    type: "example",
                    title: "Model essay fragment",
                    content: "PROMPT: Many cities suffer from severe air pollution. What are the causes, and what measures can be taken to address it?\n\nINTRO + PROBLEMS PARAGRAPH:\n'Air pollution has become one of the defining urban challenges of the 21st century, with cities from Delhi to Mexico City regularly recording hazardous levels. This essay will examine two principal causes — vehicle emissions and unregulated industry — and propose two corresponding solutions.\n\nThe most pervasive cause of urban air pollution is the explosive growth of private car ownership. As cities expand horizontally, residents commute longer distances by car, releasing nitrogen oxides and particulate matter into the air. The cumulative effect is a daily smog that, over decades, raises rates of asthma, heart disease, and premature death. London, for instance, exceeded annual EU pollution limits within just six days of January 2024 — driven almost entirely by traffic. A second major cause is unregulated industrial activity, particularly in rapidly industrialising economies where coal-fired plants and small factories operate without effective filtration, releasing sulphur dioxide and heavy metals.'\n\nSOLUTIONS PARAGRAPH:\n'Two complementary solutions can address these causes. To tackle vehicle emissions, cities should implement low-emission zones charging high-polluting vehicles to enter the city centre, while heavily investing in public transport. London's Ultra Low Emission Zone has already cut roadside nitrogen dioxide by 44%, demonstrating the potential. To address industrial pollution, governments must enforce emission caps backed by independent monitoring, and offer subsidised retrofits for older plants. This approach reduces pollution without forcing businesses to close, balancing environmental and economic priorities.'"
                },
                {
                    type: "common_mistakes",
                    title: "Errors",
                    content: "1) Solutions that don't match the problems raised. 2) Vague solutions ('the government should do something'). 3) Listing more than 2 problems with no depth. 4) Forgetting examples. 5) Confusing problem-solution with cause-effect (if prompt says causes, focus on causes, not problems)."
                }
            ],
            practice_items: [
                {
                    type: "writing_prompt",
                    content: {
                        prompt: "Many young people in developed countries are increasingly inactive and overweight. What problems does this cause and what can be done?",
                        sample_outline: "Problems: health outcomes (diabetes, depression), economic burden on health systems. Solutions: school PE reform, family-targeted public health campaigns, urban planning for walkability."
                    }
                }
            ],
            band_descriptors: {
                "6.0": "Problems and solutions identified but underdeveloped; solutions not always linked.",
                "7.0": "Clear problem-solution mapping; mechanisms explained; concrete examples.",
                "8.0": "Sophisticated cause-effect chains; nuanced solutions with evaluation.",
                "9.0": "Effortless and insightful."
            },
            next_steps: [
                "Lesson W2 4: Advantages-Disadvantages Essays.",
                "Write 1 problem-solution under 40-min timer."
            ]
        },

        // ---------- W T2 LESSON 4 ----------
        {
            id: "ielts-w2-4",
            section: "writing-t2",
            band_target: "6.0-9.0",
            cefr: "B2-C2",
            title: "Advantages-Disadvantages Essays",
            subtitle: "Two prompt subtypes — and the structures that fit each.",
            duration_min: 65,
            objectives: [
                "Distinguish 'discuss advantages and disadvantages' (no opinion) from 'do advantages outweigh disadvantages?' (opinion required).",
                "Allocate paragraphs accordingly.",
                "Use weighing language to decide.",
                "Avoid listing more than 2 advantages or 2 disadvantages."
            ],
            sections: [
                {
                    type: "intro",
                    title: "Two subtypes",
                    content: "TYPE A: 'Discuss the advantages and disadvantages of X.' — describe both, no opinion needed. TYPE B: 'Do the advantages outweigh the disadvantages?' — describe both AND give your opinion. Most students confuse these and lose marks."
                },
                {
                    type: "strategy",
                    title: "Type A structure (no opinion)",
                    content: "PARA 1: paraphrase + signal that you'll examine pros and cons. PARA 2: 1–2 advantages with development. PARA 3: 1–2 disadvantages with development. PARA 4: summary that pros and cons are roughly balanced (no preference required)."
                },
                {
                    type: "strategy",
                    title: "Type B structure (opinion needed)",
                    content: "PARA 1: paraphrase + state which side outweighs ('In my view, the disadvantages outweigh the advantages.'). PARA 2: opposite-side first (e.g. advantages, briefly). PARA 3: your-side (disadvantages, fully developed). PARA 4: restate that the negatives are weightier and why."
                },
                {
                    type: "strategy",
                    title: "Weighing language",
                    content: "BENEFITS: 'A clear advantage is that…', 'One major benefit is…'. DRAWBACKS: 'A significant drawback is…', 'On the negative side…'. WEIGHING: 'Although X has clear merit, the long-term costs are greater because…', 'Despite the obvious benefits of Y, I am persuaded that the disadvantages are more serious.'"
                },
                {
                    type: "example",
                    title: "Model intro for Type B",
                    content: "PROMPT: Many people now choose to live in mega-cities. Do the advantages of this trend outweigh the disadvantages?\n\nINTRO: 'In recent decades, the global population has shifted dramatically toward mega-cities — urban centres exceeding ten million inhabitants. While such cities offer real economic and cultural benefits, in my view their environmental and social drawbacks substantially outweigh these advantages, particularly when measured over the long term.'"
                },
                {
                    type: "common_mistakes",
                    title: "Errors",
                    content: "1) Giving an opinion when the prompt didn't ask for one (Type A). 2) NOT giving an opinion when prompt asks 'do they outweigh?' (Type B). 3) Equal weight to both sides in a Type B essay = unclear position. 4) Listing 4 advantages, no depth."
                }
            ],
            practice_items: [
                {
                    type: "writing_prompt",
                    content: {
                        prompt: "More and more parents work from home. Do the advantages outweigh the disadvantages for their children?",
                        sample_outline: "Para 1: state opinion (e.g. yes, advantages outweigh). Para 2: briefly acknowledge disadvantages (parental distraction). Para 3: develop advantages (more time, role modelling). Para 4: restate."
                    }
                }
            ],
            band_descriptors: {
                "6.0": "Both sides covered; weak weighing.",
                "7.0": "Clear allocation; weighing language; concrete examples.",
                "8.0": "Sharp opinion; nuanced weighing; precise vocabulary.",
                "9.0": "Effortless and insightful."
            },
            next_steps: [
                "Lesson W2 5: Two-Part Questions.",
                "Write 1 adv-disadv essay under 40-min timer."
            ]
        },

        // ---------- W T2 LESSON 5 ----------
        {
            id: "ielts-w2-5",
            section: "writing-t2",
            band_target: "6.0-9.0",
            cefr: "B2-C2",
            title: "Two-Part Questions (Compound prompts)",
            subtitle: "Two questions in one prompt — answer both equally.",
            duration_min: 65,
            objectives: [
                "Recognise compound prompts (two distinct questions).",
                "Allocate one body paragraph to each question.",
                "Avoid the trap of answering only one question.",
                "Maintain consistency between the two answers."
            ],
            sections: [
                {
                    type: "intro",
                    title: "What two-part prompts look like",
                    content: "Examples: 'Why is X happening, and what can be done about it?' / 'What are the reasons for X, and what effects does it have?' / 'Is X a positive or negative trend, and why?' Each prompt has 2 distinct questions. Both must be answered with roughly equal depth."
                },
                {
                    type: "strategy",
                    title: "4-paragraph structure",
                    content: "PARA 1 (Intro): paraphrase + signal both questions. PARA 2 (Question 1, ~110 w): full answer with examples. PARA 3 (Question 2, ~110 w): full answer with examples. PARA 4 (Conclusion): synthesise both answers."
                },
                {
                    type: "strategy",
                    title: "Linking the two parts",
                    content: "Make sure your answer to part 2 is consistent with part 1. If part 1 asks 'why?' and you say 'rapid urbanisation', part 2 ('what can be done?') should suggest urban-planning solutions, not unrelated ones. Coherence between the two halves is what separates Band 7 from Band 8."
                },
                {
                    type: "example",
                    title: "Model intro and part-1 paragraph",
                    content: "PROMPT: Children in many countries spend less time playing outdoors than they did a generation ago. Why is this the case, and is it a positive or negative development?\n\nINTRO + PART 1:\n'Across many parts of the world, today's children spend dramatically less time playing outdoors compared to their parents' generation. This essay will examine the principal causes of this shift and argue that, on balance, the trend is a clearly negative development.\n\nThe primary cause is the explosion of digital entertainment. Smartphones, tablets, and gaming consoles deliver instant, low-effort stimulation indoors, making outdoor play comparatively uninviting. A secondary factor is parental anxiety: high-profile reporting on traffic and stranger danger has led many parents to restrict unsupervised outdoor play, even in safe areas. Finally, urban design itself has changed — many neighbourhoods built since 2000 lack the wide pavements, accessible parks, and safe cul-de-sacs that supported earlier generations of outdoor play.'"
                },
                {
                    type: "common_mistakes",
                    title: "Errors",
                    content: "1) Answering only one of the two questions. 2) Spending 80% on Q1 and 20% on Q2 (or vice versa). 3) Inconsistent reasoning between the two. 4) Misreading 'and' as 'or'. 5) Skipping the conclusion."
                }
            ],
            practice_items: [
                {
                    type: "writing_prompt",
                    content: {
                        prompt: "More people are choosing to live alone than ever before. Why is this the case, and what consequences does this trend have for society?"
                    }
                }
            ],
            band_descriptors: {
                "6.0": "Both questions answered but unequally.",
                "7.0": "Both fully answered with concrete examples; consistent.",
                "8.0": "Sharp consistency; varied vocabulary; precise.",
                "9.0": "Effortless and integrated."
            },
            next_steps: [
                "Lesson W2 6: Strong Introductions & Thesis Statements.",
                "Write 1 two-part essay under 40-min timer."
            ]
        },

        // ---------- W T2 LESSON 6 ----------
        {
            id: "ielts-w2-6",
            section: "writing-t2",
            band_target: "6.0-9.0",
            cefr: "B2-C2",
            title: "Strong Introductions & Thesis Statements",
            subtitle: "The first 50 words decide whether the examiner expects Band 6 or Band 8.",
            duration_min: 50,
            objectives: [
                "Build a 3-sentence introduction reliably.",
                "Paraphrase the prompt without copying.",
                "Write a clear, position-stating thesis.",
                "Preview the essay's structure briefly."
            ],
            sections: [
                {
                    type: "intro",
                    title: "Why introductions matter disproportionately",
                    content: "Examiners read 5–10 essays per hour. The introduction is your one chance to signal that you understand the prompt and can structure an argument. A muddled intro biases the examiner toward Band 5–6 even if the body is strong. A clean intro buys you the benefit of the doubt."
                },
                {
                    type: "strategy",
                    title: "The 3-sentence formula",
                    content: "SENTENCE 1: paraphrase the prompt to show understanding. SENTENCE 2: state your thesis (your position) clearly. SENTENCE 3: preview the structure ('This essay will examine X and Y.' or fold preview into the thesis)."
                },
                {
                    type: "strategy",
                    title: "Paraphrase techniques",
                    content: "TECHNIQUE 1 — synonym swap: 'children' → 'young people', 'university' → 'higher education'. TECHNIQUE 2 — reorder: 'Some people think X' → 'There is a view that X'. TECHNIQUE 3 — change voice: active to passive. TECHNIQUE 4 — change structure: noun to verb ('the increase in' → 'has increased'). NEVER copy more than 3 consecutive words from the prompt."
                },
                {
                    type: "strategy",
                    title: "Thesis statements that earn marks",
                    content: "WEAK: 'I will discuss this topic.' (No position.) WEAK: 'There are advantages and disadvantages.' (Vague.) STRONG: 'In my view, the disadvantages of social media use among children significantly outweigh its educational benefits, primarily due to its impact on mental health and attention.' STRONG: 'I firmly believe that governments, rather than individuals, bear the primary responsibility for tackling climate change because only they can coordinate the structural changes required.'"
                },
                {
                    type: "example",
                    title: "Three intros — Band 5, 6, 8",
                    content: "PROMPT: Some believe that art and music should be compulsory in school. Others say only academic subjects should be taught. Discuss both views and give your opinion.\n\nBAND 5: 'There are people who think art and music should be in schools. Other people don't think so. I will discuss both views and give my opinion. Both have advantages and disadvantages.' (Repetitive, vague, no clear thesis.)\n\nBAND 6: 'Some people argue that art and music must be taught in school, while others believe academic subjects are enough. I will discuss both opinions in this essay and explain my own view at the end.' (Better paraphrase, but thesis withheld and announced rather than stated.)\n\nBAND 8: 'Educators have long debated whether the school curriculum should include creative subjects such as art and music, or whether limited classroom time is better spent on traditional academic disciplines. Both views have merit, but in my view a curriculum without creative subjects fails to develop the imagination, emotional literacy, and cultural identity that a complete education must include.' (Sharp paraphrase, clear thesis stated immediately, sophisticated vocabulary.)"
                },
                {
                    type: "common_mistakes",
                    title: "Errors",
                    content: "1) Copying the prompt verbatim. 2) Withholding the thesis ('I will discuss…') instead of stating it. 3) Background sentences too long ('Since the dawn of civilisation…'). 4) Writing more than 60 words in the introduction. 5) Vague thesis ('It depends on the situation.')."
                }
            ],
            practice_items: [
                {
                    type: "writing_prompt",
                    content: {
                        prompt: "Some people think governments should ban dangerous sports. Others believe individuals should have the freedom to choose. Discuss both views and give your opinion.",
                        instruction: "Write only the 3-sentence introduction (not the whole essay).",
                        sample_band_8: "Whether governments should restrict participation in dangerous sports, or whether such decisions should remain with the individual, has become a contentious public debate. While I acknowledge the case for state intervention where reckless behaviour endangers others, in my view personal autonomy should generally prevail, and bans should be limited to genuinely catastrophic risks. This essay will examine both positions before defending the latter view."
                    }
                }
            ],
            band_descriptors: {
                "6.0": "Paraphrase attempted but partial; thesis vague or absent.",
                "7.0": "Clean paraphrase; clear thesis; structure previewed.",
                "8.0": "Sophisticated paraphrase; sharp thesis; nuance.",
                "9.0": "Effortless and elegant."
            },
            next_steps: [
                "Lesson W2 7: Body Paragraphs PEEL/PEEEL.",
                "Drill: write 3 introductions in 15 minutes total."
            ]
        },

        // ---------- W T2 LESSON 7 ----------
        {
            id: "ielts-w2-7",
            section: "writing-t2",
            band_target: "6.0-9.0",
            cefr: "B2-C2",
            title: "Body Paragraphs: PEEL/PEEEL Structure",
            subtitle: "Point–Explanation–Example–(Effect)–Link: the 5-step formula examiners reward.",
            duration_min: 60,
            objectives: [
                "Apply PEEL or PEEEL to every body paragraph.",
                "Write topic sentences that announce a single idea.",
                "Develop ideas with mechanism (the 'because' chain).",
                "Use concrete general examples (countries, statistics, named events)."
            ],
            sections: [
                {
                    type: "intro",
                    title: "Why structure matters as much as content",
                    content: "An examiner can identify a Band 7 paragraph in 5 seconds: it has a clear topic sentence, an explanation, an example, and a closing link. Band 5 paragraphs are flat — sentences in random order. PEEL/PEEEL is the bridge."
                },
                {
                    type: "strategy",
                    title: "PEEL — the 4 elements",
                    content: "P (Point): topic sentence — one clear claim. E (Explanation): why this is true; the mechanism. E (Example): a concrete general example (country, study, well-known event). L (Link): tie back to the thesis. ~80–110 words."
                },
                {
                    type: "strategy",
                    title: "PEEEL — adding Effect",
                    content: "P (Point) → E (Explanation) → E (Example) → E (Effect — the consequence) → L (Link). Adding the EFFECT step turns Band 6 paragraphs into Band 7+. Effects show you can extend an argument beyond a single claim."
                },
                {
                    type: "strategy",
                    title: "Topic sentence templates",
                    content: "POINT 1: 'The most significant reason is that…', 'A primary advantage of this trend is…'. POINT 2: 'A second consideration is that…', 'Equally important is…'. AVOID: 'Firstly… Secondly…' alone — too mechanical. Combine with content: 'Firstly, and most importantly, the long-term economic benefits…'."
                },
                {
                    type: "strategy",
                    title: "Examples that earn marks",
                    content: "GOOD examples: countries (Norway's parental leave, Singapore's housing policy), well-known studies (the 1972 Stanford marshmallow experiment), named events (the 2008 financial crisis), statistics (UN data: 60% of urban workers commute over 1 hour). BAD examples: personal anecdotes ('My uncle…'), invented studies ('A recent study showed 80%…' with no source-style detail), overgeneralised claims ('Everyone knows…')."
                },
                {
                    type: "example",
                    title: "Model PEEEL paragraph",
                    content: "TOPIC: The benefits of public investment in cycling infrastructure.\n\nP — Point: 'A primary advantage of investing in dedicated cycling infrastructure is the substantial public health gain.'\n\nE — Explanation: 'When cities provide segregated cycle paths, residents are far more likely to commute by bike instead of car. This shift produces daily moderate exercise for tens of thousands of people who would otherwise be sedentary, while simultaneously reducing the air pollution that worsens respiratory illness.'\n\nE — Example: 'Copenhagen offers compelling evidence: after extending its cycle network to over 380 kilometres, the city now sees more than 60% of residents cycle to work daily, and population-level rates of obesity and cardiovascular disease have measurably declined.'\n\nE — Effect: 'The downstream consequence is a significant reduction in healthcare expenditure — funds that can be redirected to other priorities — alongside higher productivity from a healthier workforce.'\n\nL — Link: 'Cycling investment is therefore not merely a transport decision but a health and economic one, strengthening the case for prioritising it in urban budgets.'\n\n(Word count: 158)"
                },
                {
                    type: "common_mistakes",
                    title: "Errors",
                    content: "1) Topic sentence with two ideas — confuses the paragraph. 2) Example without explanation. 3) Generalised claims with no example. 4) Forgetting the link back to thesis. 5) Switching ideas mid-paragraph."
                }
            ],
            practice_items: [
                {
                    type: "writing_prompt",
                    content: {
                        prompt: "Write a PEEEL paragraph on this topic: 'A primary disadvantage of working from home is the erosion of mental separation between work and personal life.'",
                        sample_paragraph: "P: 'A primary disadvantage of working from home is the erosion of the mental boundary between work and personal life.' E: 'When the same physical space hosts both professional duties and family routines, employees find it harder to switch off, often checking emails late into the evening or feeling guilty during personal moments.' E: 'A 2023 OECD survey found that remote workers in seven countries reported working an average of 48 minutes longer per day than office workers, with a parallel rise in burnout indicators.' E: 'The cumulative effect over months is chronic stress, declining sleep quality, and reduced engagement with family — costs that are invisible to employers but real for employees.' L: 'For this reason, however attractive home working may appear in convenience terms, its psychological costs deserve serious weight in any policy debate about its expansion.'"
                    }
                }
            ],
            band_descriptors: {
                "6.0": "Topic sentence present but underdeveloped; weak example.",
                "7.0": "Full PEEL; concrete example; clear linking.",
                "8.0": "Full PEEEL; nuanced example; precise mechanism.",
                "9.0": "Effortless and persuasive."
            },
            next_steps: [
                "Lesson W2 8: Conclusions & Common Mistakes.",
                "Drill: write 2 PEEEL paragraphs on different topics."
            ]
        },

        // ---------- W T2 LESSON 8 ----------
        {
            id: "ielts-w2-8",
            section: "writing-t2",
            band_target: "6.0-9.0",
            cefr: "B2-C2",
            title: "Conclusions & Common Mistakes",
            subtitle: "End strong, avoid clichés, and run the final 30-second checklist.",
            duration_min: 50,
            objectives: [
                "Write conclusions that synthesise without repeating.",
                "Avoid the 5 most common Task 2 mistakes.",
                "Run a final 30-second self-check.",
                "Hit 250+ words consistently."
            ],
            sections: [
                {
                    type: "intro",
                    title: "Why conclusions are easy marks (or easy losses)",
                    content: "A conclusion is short (30–50 words) but heavily affects the examiner's impression. Skipping it = automatic Band 6 ceiling. A weak conclusion that just repeats the intro = no impression. A strong conclusion synthesises and projects forward."
                },
                {
                    type: "strategy",
                    title: "The 2-sentence conclusion formula",
                    content: "SENTENCE 1: synthesise — restate your thesis using DIFFERENT words from the intro. Reference the two body reasons briefly. SENTENCE 2: optional projection — implication, recommendation, or balanced acknowledgement. NEVER introduce new arguments in the conclusion."
                },
                {
                    type: "strategy",
                    title: "Conclusion phrase bank",
                    content: "OPENING: 'In conclusion…', 'To conclude…', 'Overall…', 'On balance…'. RESTATEMENT: 'it seems clear that…', 'the evidence supports the view that…', 'the case for X is more compelling than Y because…'. PROJECTION: 'governments would do well to…', 'further research is needed before…', 'the longer-term implication is…'."
                },
                {
                    type: "strategy",
                    title: "Example conclusion",
                    content: "FROM the cycling-infrastructure essay: 'In conclusion, while the upfront costs of cycling infrastructure are real, the long-term gains in public health and productivity strongly justify the investment, particularly for cities seeking sustainable urban futures. Cycling investment should therefore be treated not as an optional environmental measure but as a strategic public-health priority.'"
                },
                {
                    type: "common_mistakes",
                    title: "The 10 most common Task 2 mistakes",
                    content: "1) Under 250 words — automatic penalty. 2) Off-topic body paragraphs. 3) No clear thesis. 4) Anecdotal examples ('my friend'). 5) Listing 4–5 short reasons instead of 2 deep ones. 6) No conclusion. 7) Conclusion repeats intro verbatim. 8) Inconsistent stance. 9) Memorised generic phrases overused. 10) Weak vocabulary range — same word repeated 5+ times."
                },
                {
                    type: "tips",
                    title: "The 30-second final check",
                    content: "(1) Did I state a clear thesis? (2) Did I cover all parts of the prompt? (3) Did I write at least 250 words? (4) Did I write a conclusion? (5) Tense consistent? (6) Spelling errors? (7) Linkers varied (not just 'and', 'but')? Allocate the last minute to this check."
                }
            ],
            practice_items: [
                {
                    type: "writing_prompt",
                    content: {
                        prompt: "Read this thesis: 'I firmly believe that governments should restrict private car use in city centres because of pollution and congestion.' Write a 2-sentence conclusion.",
                        sample_band_8: "In conclusion, although restricting cars imposes short-term inconvenience on motorists, the resulting reductions in air pollution and traffic congestion offer substantial long-term gains in public health and urban liveability. City governments should therefore proceed with such measures, despite resistance, as part of any serious commitment to sustainable urban planning."
                    }
                }
            ],
            band_descriptors: {
                "6.0": "Conclusion present but mechanical.",
                "7.0": "Synthesises clearly; varied phrasing.",
                "8.0": "Sharp synthesis; forward-looking projection.",
                "9.0": "Effortless and memorable."
            },
            next_steps: [
                "Move to Speaking section, Lesson 1.",
                "Write 1 full Task 2 essay under 40-min timer with 30-second check."
            ]
        },

        // ============================================================
        // SPEAKING — 6 LESSONS
        // ============================================================

        // ---------- SPEAKING LESSON 1 ----------
        {
            id: "ielts-speaking-1",
            section: "speaking",
            band_target: "5.5-9.0",
            cefr: "B1-C2",
            title: "Part 1 Strategy: Personal Topics",
            subtitle: "Work, study, hometown — extend short answers without padding.",
            duration_min: 45,
            objectives: [
                "Understand the format of Part 1 (4–5 minutes, 12 questions).",
                "Extend each answer to 2–3 sentences.",
                "Add reasons and examples without rambling.",
                "Use natural fillers and discourse markers."
            ],
            sections: [
                {
                    type: "intro",
                    title: "What Part 1 tests",
                    content: "Part 1 is a warm-up — friendly questions about your life, work, study, hometown, and 2–3 simple topics (e.g. food, weather, hobbies). The examiner is checking that you can speak naturally about familiar topics. Yes/no answers kill your Band score; over-long answers waste time; the sweet spot is 2–3 sentences per question."
                },
                {
                    type: "strategy",
                    title: "The PER formula (Point + Example + Reason)",
                    content: "POINT: directly answer the question. EXAMPLE: give a concrete instance. REASON: explain why. Example — Q: 'Do you enjoy cooking?' A (PER): 'Yes, I really do. I cook dinner from scratch about four nights a week, mostly Peruvian dishes my grandmother taught me. I find it relaxing after a long day at work.' Three sentences, full answer, no padding."
                },
                {
                    type: "strategy",
                    title: "Discourse markers (natural English)",
                    content: "STARTING: 'Well…', 'To be honest…', 'Actually…', 'Let me think…'. ADDING: 'On top of that…', 'Plus…', 'Another thing is…'. EXPLAINING: 'I mean…', 'You know…', 'The thing is…'. CONTRASTING: 'Although…', 'Having said that…'. These signal natural fluency to the examiner."
                },
                {
                    type: "tips",
                    title: "Avoiding the rookie mistakes",
                    content: "1) DO NOT memorise scripted answers — examiners spot them in 5 seconds and downgrade. 2) DO NOT speak in formal essay register ('Furthermore, in my opinion…'). 3) DO NOT freeze on 'don't know' answers — give an honest brief response: 'Hmm, I haven't really thought about that. I'd guess…'. 4) DO NOT correct yourself constantly — examiners reward fluency over hesitation."
                },
                {
                    type: "example",
                    title: "Sample Part 1 exchange (Band 7+)",
                    content: "Q1: 'Do you work or study?' A1: 'I'm currently working as a logistics coordinator at a shipping company in Lima — I've been there for about three years now, and I really enjoy the variety.' Q2: 'Why did you choose that job?' A2: 'Honestly, it wasn't planned. I studied international business but ended up taking a temporary role in logistics, and it grew on me. I like the problem-solving side — every shipment has its own little puzzle.' Q3: 'Is it a popular career in your country?' A3: 'It's becoming more popular, actually. With Peru's exports growing — especially fruit and copper — there's real demand for logistics people, so I'd say it's a good time to be in the field.'"
                },
                {
                    type: "common_mistakes",
                    title: "Errors that cap Band 6",
                    content: "1) One-word answers. 2) Memorised speeches. 3) Over-formal vocabulary. 4) Long pauses with 'Ehm…ehm…'. 5) Going off topic. 6) Speaking too quickly to mask uncertainty."
                }
            ],
            practice_items: [
                {
                    type: "cue_card",
                    content: {
                        instruction: "Practise these Part 1 exchanges. Give 2–3 sentence answers using PER.",
                        questions: [
                            "Where is your hometown?",
                            "Do you like the area where you live? Why?",
                            "Is your hometown changing?",
                            "What kind of food do you usually eat?",
                            "Do you cook at home?",
                            "Are restaurants popular in your country?"
                        ]
                    }
                }
            ],
            band_descriptors: {
                "5.0": "Short answers; frequent pauses; basic vocab.",
                "6.0": "PER attempted; some hesitation; basic linkers.",
                "7.0": "Smooth PER; varied vocab; natural discourse markers.",
                "8.0": "Effortless extension; precise vocabulary; native-like fluency markers.",
                "9.0": "Indistinguishable from a fluent native speaker."
            },
            next_steps: [
                "Lesson Speaking 2: Part 1 Common Topics.",
                "Record yourself answering 12 Part 1 questions under timer."
            ]
        },

        // ---------- SPEAKING LESSON 2 ----------
        {
            id: "ielts-speaking-2",
            section: "speaking",
            band_target: "5.5-9.0",
            cefr: "B1-C2",
            title: "Part 1 Common Topics: Hobbies, Food, Travel, Technology",
            subtitle: "Build a topic-specific phrase bank for the most-asked Part 1 categories.",
            duration_min: 50,
            objectives: [
                "Memorise topic-specific vocabulary for 4 high-frequency Part 1 categories.",
                "Apply PER to each topic seamlessly.",
                "Avoid clichéd answers ('I like reading').",
                "Add personal authenticity that examiners reward."
            ],
            sections: [
                {
                    type: "intro",
                    title: "The big four Part 1 topic areas",
                    content: "After your work/study/hometown opening, examiners pick 2–3 themes from a rotating bank: HOBBIES, FOOD, TRAVEL, TECHNOLOGY, WEATHER, MUSIC, BOOKS, SPORTS, SHOPPING, FRIENDS. The first four are statistically the most common. Build a personal answer bank for each."
                },
                {
                    type: "strategy",
                    title: "HOBBIES — vocabulary boost",
                    content: "INSTEAD OF 'I like': 'I'm really into…', 'I'm a big fan of…', 'I'm passionate about…'. INSTEAD OF 'reading': 'getting lost in a good novel', 'devouring biographies'. INSTEAD OF 'sports': 'staying active', 'pickup football matches', 'casual hiking on weekends'. AUTHENTICITY: include a specific detail (genre, place, frequency)."
                },
                {
                    type: "strategy",
                    title: "FOOD — vocabulary boost",
                    content: "TASTE: savoury, spicy, rich, fresh, hearty, light, comforting, indulgent. PROCESSES: stir-fried, slow-cooked, grilled, marinated, baked from scratch. JUDGEMENT: 'I have a real soft spot for…', 'I'm not particularly fond of…', 'It's an acquired taste.' EXAMPLE ANSWER: 'I'd say I'm fairly adventurous when it comes to food — I love trying dishes from different cuisines, especially anything spicy. Thai green curry is probably my all-time favourite.'"
                },
                {
                    type: "strategy",
                    title: "TRAVEL — vocabulary boost",
                    content: "TYPES: backpacking, road trips, weekend getaways, city breaks, beach holidays, all-inclusive resorts. ACTIVITIES: sightseeing, getting off the beaten track, soaking up the local culture, sampling street food. REACTIONS: 'It blew me away.', 'I was completely taken aback by…', 'It exceeded my expectations.'"
                },
                {
                    type: "strategy",
                    title: "TECHNOLOGY — vocabulary boost",
                    content: "DEVICES: smartphone, smartwatch, e-reader, smart speaker, gaming console. USES: streaming, scrolling, video-calling, online banking, navigating. PROS/CONS: 'It's a real time-saver.', 'I find it indispensable.', 'I worry about how addictive it is.', 'It's a bit of a double-edged sword.' Avoid: 'good' / 'bad' / 'easy' as your primary vocabulary."
                },
                {
                    type: "common_mistakes",
                    title: "Errors",
                    content: "1) Memorised paragraphs that sound rehearsed. 2) Cliché answers identical to thousands of other candidates. 3) Generic vocabulary. 4) Forgetting examples. 5) Topic vocabulary used incorrectly."
                }
            ],
            practice_items: [
                {
                    type: "cue_card",
                    content: {
                        instruction: "Answer each question with PER and topic-specific vocabulary.",
                        questions: [
                            "What hobbies were you into as a child?",
                            "Has your hobby changed over time?",
                            "Are there any foods you don't like?",
                            "Do you prefer eating at home or in restaurants?",
                            "Have you travelled abroad recently?",
                            "Do you prefer travelling alone or with others?",
                            "What kind of technology do you use every day?",
                            "Has technology changed how you communicate with friends?"
                        ]
                    }
                }
            ],
            band_descriptors: {
                "5.0": "Generic vocabulary; clichéd answers.",
                "6.0": "Some topic vocab; PER attempted.",
                "7.0": "Strong topic vocab; authentic answers.",
                "8.0": "Idiomatic; precise; natural personal voice.",
                "9.0": "Indistinguishable from fluent native."
            },
            next_steps: [
                "Lesson Speaking 3: Part 2 Cue Card.",
                "Record 8 topic-specific Part 1 answers."
            ]
        },

        // ---------- SPEAKING LESSON 3 ----------
        {
            id: "ielts-speaking-3",
            section: "speaking",
            band_target: "5.5-9.0",
            cefr: "B1-C2",
            title: "Part 2 Cue Card: Structure & 2-Minute Talk Method",
            subtitle: "The long turn — how to fill 2 minutes without freezing.",
            duration_min: 60,
            objectives: [
                "Use the 1 minute of preparation effectively.",
                "Apply the WHO/WHAT/WHEN/WHERE/WHY/HOW skeleton.",
                "Speak fluently for 1:30–2:00 without stopping.",
                "Cover all 4 bullet points on the cue card."
            ],
            sections: [
                {
                    type: "intro",
                    title: "What Part 2 demands",
                    content: "The examiner gives you a cue card with a topic and 4 bullet points (e.g. 'Describe a memorable journey. You should say where you went, who you went with, what happened, and explain why it was memorable.'). You have 1 minute to prepare with paper and pencil, then must speak for 1–2 minutes. The examiner stops you at 2 minutes."
                },
                {
                    type: "strategy",
                    title: "The 60-second prep",
                    content: "0–10 seconds: choose your topic instance — pick something you can talk about for 2 minutes, even if not the most exciting. 10–40 seconds: write 4–6 keyword notes (NOT full sentences) covering all bullet points. 40–60 seconds: think of vocabulary you want to deploy and how you'll start. NEVER write full sentences — you don't have time."
                },
                {
                    type: "strategy",
                    title: "WHO/WHAT/WHEN/WHERE/WHY/HOW skeleton",
                    content: "If your bullet points don't fully fill 2 minutes, layer in: WHO was involved, WHAT exactly happened, WHEN it took place, WHERE it was, WHY it mattered, HOW it ended. These six prompts give you 6 angles to elaborate."
                },
                {
                    type: "strategy",
                    title: "Opening, middle, closing structure",
                    content: "OPENING (~15 sec): 'I'd like to talk about [topic]. It's something that happened back in [time/context].' MIDDLE (~75 sec): cover all 4 bullets in order. Use clear transitions: 'The first thing worth mentioning is…', 'Then…', 'Looking back…'. CLOSING (~20 sec): 'So overall, this experience really stayed with me because…'."
                },
                {
                    type: "tips",
                    title: "Survival tactics if you blank",
                    content: "1) Use the cue card as a visual prompt — read the bullet points aloud if needed: 'And the next thing to mention is…'. 2) Buy time with fillers: 'Let me think about this for a second…'. 3) Repeat in different words: 'It was really, really memorable — it just stuck with me.' 4) NEVER apologise — keep going. The examiner counts FLUENCY, not accuracy."
                },
                {
                    type: "example",
                    title: "Model 2-minute talk",
                    content: "CUE CARD: 'Describe a skill you would like to learn. You should say: what the skill is, why you want to learn it, how you would go about learning it, and explain how this skill might benefit you in the future.'\n\nMODEL TALK (~280 words = ~2 min spoken):\n'Right, well, the skill I'd really like to learn is sailing — particularly small-boat sailing on lakes or near the coast. I've been thinking about this for a couple of years now, ever since I went on a short sailing course while on holiday in southern Chile.\n\nThe main reason I want to learn properly is that I find being on the water genuinely calming. Day-to-day life in Lima is quite intense — traffic, deadlines, all of that — and the few hours I spent on a small sailing boat were the most peaceful I'd felt in years. There's something about reading the wind and using only natural force to move that completely takes you out of your head.\n\nIn terms of how I'd go about learning, I've actually done some research. There's a sailing club in Paracas, about three hours south of Lima, that runs weekend courses for beginners. My plan would be to do their introductory programme over a few weekends, then maybe go further afield if I really get hooked.\n\nAs for the long-term benefits, well, beyond the obvious mental health side, sailing teaches you a lot about patience, problem-solving, and reading conditions — skills that transfer surprisingly well to everyday life. Plus, if I ever managed to get really good, I love the idea of sailing across longer distances one day, maybe down the coast of Patagonia. It's a bit of a dream, but you have to start somewhere, right?'"
                },
                {
                    type: "common_mistakes",
                    title: "Errors",
                    content: "1) Stopping at 45 seconds. 2) Memorised general answer that ignores the cue card. 3) Skipping bullet points. 4) Speaking in present simple only. 5) Apologising or self-correcting constantly."
                }
            ],
            practice_items: [
                {
                    type: "cue_card",
                    content: {
                        instruction: "Practise these cue cards. Use 1 minute of prep, then speak for 2 minutes.",
                        cards: [
                            "Describe a person who has had a positive influence on you. You should say: who they are, how you know them, what they have done, and explain why they have influenced you positively.",
                            "Describe a piece of technology you find useful. You should say: what it is, when you started using it, how you use it, and explain why you find it useful.",
                            "Describe a time when you received good news. You should say: what the news was, how you received it, who you shared it with, and explain how it made you feel."
                        ]
                    }
                }
            ],
            band_descriptors: {
                "5.0": "Stops under 1 minute; misses bullets.",
                "6.0": "Reaches 1.5 min; hesitations; covers most bullets.",
                "7.0": "Full 2 minutes; smooth transitions; varied vocab.",
                "8.0": "Effortless; idiomatic; precise.",
                "9.0": "Indistinguishable from native."
            },
            next_steps: [
                "Lesson Speaking 4: Part 2 Practice (People, Places, Events, Objects).",
                "Record 3 cue-card responses with timer."
            ]
        },

        // ---------- SPEAKING LESSON 4 ----------
        {
            id: "ielts-speaking-4",
            section: "speaking",
            band_target: "5.5-9.0",
            cefr: "B1-C2",
            title: "Part 2 Practice: People, Places, Events, Objects",
            subtitle: "The four cue-card families — and the templates that work for each.",
            duration_min: 60,
            objectives: [
                "Recognise the four standard cue-card families.",
                "Apply family-specific vocabulary and structure.",
                "Re-use prepared content flexibly across topics.",
                "Avoid the trap of forcing one rehearsed answer."
            ],
            sections: [
                {
                    type: "intro",
                    title: "The cue-card taxonomy",
                    content: "Almost every Part 2 topic falls into one of four families. PEOPLE: a person you admire, a relative, a teacher, a friend, a celebrity. PLACES: a city you visited, a beach, a building, your hometown. EVENTS: a holiday, a celebration, a memorable day, a difficult time. OBJECTS: a gift, a piece of technology, a book, a possession. Knowing the family lets you select vocabulary instantly."
                },
                {
                    type: "strategy",
                    title: "PEOPLE template",
                    content: "INTRODUCTION: 'I'd like to talk about [name], who is my [relation].' DESCRIPTION: physical (only briefly), personality, voice/manner. WHAT THEY DO: profession, hobbies. CONNECTION: how I know them, shared experiences. WHY THEY MATTER: lasting influence, specific moment that captures their character. Vocabulary: thoughtful, warm-hearted, sharp-witted, down-to-earth, patient, larger-than-life."
                },
                {
                    type: "strategy",
                    title: "PLACES template",
                    content: "INTRODUCTION + LOCATION: 'I'd like to talk about [place], a [type] in [country/region].' SENSORY: what you see, hear, smell. ATMOSPHERE: bustling, peaceful, isolated, vibrant. ACTIVITIES: what you do there. WHY MEMORABLE: an emotion, a moment, a connection. Vocabulary: breathtaking, off the beaten track, picture-postcard, hidden gem, world-famous landmark."
                },
                {
                    type: "strategy",
                    title: "EVENTS template",
                    content: "WHEN: time/season. CONTEXT: what was happening in your life. WHAT HAPPENED: chronological order, cover the climax. WHO ELSE: people involved. WHY MEMORABLE: lasting emotion, lessons learned. Use past simple for actions, past continuous for background, past perfect for prior events."
                },
                {
                    type: "strategy",
                    title: "OBJECTS template",
                    content: "WHAT IT IS + ORIGIN: where it came from, when. APPEARANCE: brief sensory description. FUNCTION/USE: how you use it. EMOTIONAL VALUE: why it matters beyond function. SPECIFIC MEMORY: a moment associated with it. Vocabulary: keepsake, memento, prized possession, sentimental value, well-worn, irreplaceable."
                },
                {
                    type: "tips",
                    title: "The flexibility principle",
                    content: "Practise 4 'core' answers — one per family — that you can adapt to many cue cards. E.g. your PEOPLE answer about your grandmother can flex to: a person who influenced you, a person you admire, an older relative, a teacher (if she taught you something). Examiners are NOT impressed by perfect-fit cards — they reward natural extension."
                },
                {
                    type: "common_mistakes",
                    title: "Errors",
                    content: "1) Forcing a rehearsed answer onto an ill-fitting prompt. 2) Using only present-tense for past events. 3) Skipping sensory description. 4) Going one minute, stopping. 5) Memorised opening that sounds robotic."
                }
            ],
            practice_items: [
                {
                    type: "cue_card",
                    content: {
                        instruction: "Practise one cue card per family. 1 min prep + 2 min talk.",
                        cards: [
                            "PEOPLE: Describe a teacher who influenced you when you were younger.",
                            "PLACES: Describe a beautiful place you have visited.",
                            "EVENTS: Describe a celebration that was important in your culture.",
                            "OBJECTS: Describe a present you received that you really liked."
                        ]
                    }
                }
            ],
            band_descriptors: {
                "5.0": "Forces rehearsed answer; tense errors.",
                "6.0": "Family-appropriate vocab; some hesitation.",
                "7.0": "Smooth family-specific structure; varied tense.",
                "8.0": "Effortless adaptation; idiomatic.",
                "9.0": "Indistinguishable from native."
            },
            next_steps: [
                "Lesson Speaking 5: Part 3 Strategy.",
                "Record 4 cue-card answers, one per family."
            ]
        },

        // ---------- SPEAKING LESSON 5 ----------
        {
            id: "ielts-speaking-5",
            section: "speaking",
            band_target: "5.5-9.0",
            cefr: "B1-C2",
            title: "Part 3 Strategy: Abstract Discussion + Hedging",
            subtitle: "Move from personal to abstract — and answer like a thoughtful adult, not a parrot.",
            duration_min: 60,
            objectives: [
                "Recognise Part 3's abstract, opinion-based questions.",
                "Use hedging language to express nuance.",
                "Build mini-arguments in 4–5 sentences.",
                "Avoid the trap of repeating Part 2 personal stories."
            ],
            sections: [
                {
                    type: "intro",
                    title: "Why Part 3 is the highest-band gatekeeper",
                    content: "Part 3 (4–5 minutes) follows Part 2 and zooms out: questions become abstract and societal. From 'a memorable journey' (Part 2) you might be asked 'How has tourism changed in your country in the last 20 years?' or 'Should governments restrict international travel for environmental reasons?' Part 3 separates Band 7+ from Band 6 because it tests both vocabulary AND argument."
                },
                {
                    type: "strategy",
                    title: "Hedging — the language of nuance",
                    content: "Native English uses hedges constantly: 'I suppose…', 'I'd say…', 'It tends to…', 'in many cases…', 'broadly speaking…', 'at least in my experience…'. These mark you as a thoughtful speaker, not a memoriser. Avoid absolutist language ('always', 'never', 'all', 'none') — it sounds simplistic."
                },
                {
                    type: "strategy",
                    title: "The 4-step Part 3 answer",
                    content: "STEP 1 — Restate / hedge: 'That's an interesting question. I'd say…' / 'Well, broadly speaking…'. STEP 2 — Position: state a clear view. STEP 3 — Reason / mechanism: why is this the case? STEP 4 — Concrete illustration: country, group, well-known example. Optional STEP 5 — counter-acknowledgement: 'although obviously not in every case…'. ~30–45 seconds per answer is ideal."
                },
                {
                    type: "strategy",
                    title: "Comparison and contrast vocabulary",
                    content: "COMPARING ERAS: 'Twenty years ago…', 'Compared to a generation ago…', 'It's a far cry from how things were…'. COMPARING PLACES: 'In countries like X…', 'Whereas in more developed economies…'. PREDICTING: 'It's hard to say with certainty, but…', 'If current trends continue…'. EVALUATING: 'On balance, I'd argue…', 'It cuts both ways, but…'."
                },
                {
                    type: "example",
                    title: "Sample Part 3 exchange (Band 7+)",
                    content: "Q: 'Do you think international travel will become more or less common in the next 20 years?' A: 'That's a tricky one. On balance, I'd say it'll probably continue to grow overall, but the way people travel will likely change a lot. The reason is that flying has become genuinely affordable for emerging middle classes in countries like Brazil, India, and Vietnam, and those markets are still expanding. Having said that, I think we'll see a real shift toward fewer, longer trips rather than frequent short hops, partly because of climate concerns and partly because of the rise of remote work, which lets people stay abroad longer. So the total number of journeys might rise, but the pattern will look different.'"
                },
                {
                    type: "common_mistakes",
                    title: "Errors that cap Band 6",
                    content: "1) Returning to your Part 2 personal story instead of zooming out. 2) Absolutist statements. 3) One-sentence answers. 4) Memorised templates that don't fit the question. 5) Saying 'I don't know' and stopping. 6) Ignoring 'why?' and just stating opinion."
                }
            ],
            practice_items: [
                {
                    type: "cue_card",
                    content: {
                        instruction: "Practise these Part 3 questions. Apply the 4-step structure.",
                        questions: [
                            "How has the way people travel changed in recent decades?",
                            "Is mass tourism beneficial or harmful for local communities?",
                            "Should children be encouraged to travel from a young age?",
                            "How might virtual reality affect tourism in the future?",
                            "Why are some cities more popular with tourists than others?",
                            "Should governments tax air travel more heavily?"
                        ]
                    }
                }
            ],
            band_descriptors: {
                "5.0": "Returns to personal story; one-sentence answers.",
                "6.0": "Some abstract engagement; basic argument; few hedges.",
                "7.0": "Clear position + reason + example; natural hedging.",
                "8.0": "Sophisticated argumentation; nuance; idiomatic.",
                "9.0": "Effortless and insightful."
            },
            next_steps: [
                "Lesson Speaking 6: Pronunciation, Fluency & Band Descriptors.",
                "Record 6 Part 3 answers using the 4-step structure."
            ]
        },

        // ---------- SPEAKING LESSON 6 ----------
        {
            id: "ielts-speaking-6",
            section: "speaking",
            band_target: "5.5-9.0",
            cefr: "B1-C2",
            title: "Pronunciation, Fluency & Band Descriptors",
            subtitle: "How the four marking criteria work — and how to lift each one.",
            duration_min: 60,
            objectives: [
                "Understand the 4 marking criteria: Fluency & Coherence, Lexical Resource, Grammar, Pronunciation.",
                "Identify your current band per criterion.",
                "Apply targeted improvements for each.",
                "Develop natural intonation and word stress."
            ],
            sections: [
                {
                    type: "intro",
                    title: "The four pillars",
                    content: "Your overall Speaking band is the average of four sub-scores: (1) Fluency & Coherence, (2) Lexical Resource, (3) Grammatical Range and Accuracy, (4) Pronunciation. Each is band 0–9. The aggregate is rounded. Knowing which pillar is weakest tells you exactly where to invest practice time."
                },
                {
                    type: "strategy",
                    title: "Fluency & Coherence",
                    content: "BAND 6: speaks at length but with hesitation; uses range of connectors with some inappropriate use. BAND 7: speaks at length without noticeable effort; uses some less common discourse markers. BAND 8: develops topics fully and appropriately. To lift: practise 2-minute talks daily; use discourse markers ('having said that', 'on top of that', 'to be fair')."
                },
                {
                    type: "strategy",
                    title: "Lexical Resource",
                    content: "BAND 6: enough vocabulary to discuss familiar topics; basic paraphrase. BAND 7: flexible vocabulary including some idiomatic items. BAND 8: wide vocabulary used naturally; less common lexis with full appropriacy. To lift: learn 10 collocations per week (e.g. 'a long-standing tradition', 'to weigh up the pros and cons'); use them deliberately in practice."
                },
                {
                    type: "strategy",
                    title: "Grammatical Range and Accuracy",
                    content: "BAND 6: mix of simple and complex; frequent errors. BAND 7: range of complex structures with flexibility; some errors. BAND 8: wide range used flexibly; majority error-free. To lift: master conditionals (if I had…I would…), passive voice, perfect tenses (have been, had been), relative clauses (which, that, who)."
                },
                {
                    type: "strategy",
                    title: "Pronunciation",
                    content: "BAND 6: shows some features of natural pronunciation; mostly intelligible. BAND 7: wide range of pronunciation features; sustains them most of the time. BAND 8: easy to understand throughout; L1 accent has minimal effect. KEY TARGETS: word stress (PHO-to-graph vs pho-TO-gra-pher), sentence stress (stressing content words), connected speech (linking, weak forms), intonation (rising for questions, falling for statements)."
                },
                {
                    type: "tips",
                    title: "Self-recording protocol",
                    content: "Once a week: record yourself answering 4–6 IELTS-style questions. Listen back with a pen. Mark: (1) every long pause, (2) every grammar error, (3) every word you over-used, (4) every mispronounced word. Targeted weekly practice on these spots is the fastest band-lifter."
                },
                {
                    type: "common_mistakes",
                    title: "Pronunciation pitfalls common to Spanish-L1 speakers",
                    content: "1) Adding 'e' before s+consonant ('eschool' for 'school'). 2) Confusing /b/ and /v/ ('berry' / 'very'). 3) Schwa (the unstressed 'uh' sound) — overstressing every vowel sounds robotic. 4) /θ/ (think) and /ð/ (this) — practise tongue between teeth. 5) Word stress — Spanish often stresses the second-to-last syllable; English varies."
                }
            ],
            practice_items: [
                {
                    type: "cue_card",
                    content: {
                        instruction: "Self-assessment exercise: record yourself answering, then listen back and rate yourself per criterion (1–9).",
                        questions: [
                            "Talk for 1 minute about your favourite season and why.",
                            "Discuss whether technology has improved or worsened modern friendships.",
                            "Describe a public figure you respect and explain why."
                        ],
                        rubric_self_check: [
                            "Fluency: were there any pauses longer than 3 seconds?",
                            "Lexical: did I use the same word more than 3 times?",
                            "Grammar: did I attempt at least one complex structure (relative clause, conditional, perfect tense)?",
                            "Pronunciation: were any words clearly mispronounced?"
                        ]
                    }
                }
            ],
            band_descriptors: {
                "5.0": "Limited range across all 4 criteria; comprehensible with effort.",
                "6.0": "Functional in all 4; weakest one drags average.",
                "7.0": "Strong in 3 of 4; weakest area remains visible.",
                "8.0": "Strong in all 4; minor errors only.",
                "9.0": "Native-like across all four."
            },
            next_steps: [
                "Take a full Speaking mock with all 3 parts.",
                "Identify your weakest criterion and dedicate 70% of practice to it for 4 weeks."
            ]
        }

    ],

    // ============================================================
    // BAND DESCRIPTORS — FULL REFERENCE
    // ============================================================
    band_descriptors_full: {
        reading: {
            "5.0": "Understands main ideas in straightforward texts; struggles with paraphrase and inference; ~15/40.",
            "6.0": "Reads with reasonable understanding; misses some detail; ~23/40.",
            "7.0": "Reads with full understanding of main ideas and most details; ~30/40.",
            "8.0": "Near-perfect comprehension including inference and tone; ~35/40.",
            "9.0": "Complete and precise understanding; 39–40/40."
        },
        listening: {
            "5.0": "Understands main ideas in clear, slow speech; misses much detail; ~16/40.",
            "6.0": "Generally understands main ideas and detail in standard speech; ~23/40.",
            "7.0": "Understands range of accents and details with little effort; ~30/40.",
            "8.0": "Near-perfect understanding including nuance; ~35/40.",
            "9.0": "Complete understanding; 39–40/40."
        },
        writing_task1: {
            "5.0": "Generally addresses task; basic data; mechanical organisation; limited vocabulary.",
            "6.0": "Addresses task; covers main features; some inaccuracies; clear paragraphing.",
            "7.0": "Covers all key features clearly; strong overview; varied vocabulary and grammar.",
            "8.0": "Skilful summary; sharp comparison; precise vocabulary; rare errors.",
            "9.0": "Effortless integration; idiomatic precision."
        },
        writing_task2: {
            "5.0": "Addresses task partially; weak position; limited development; basic vocabulary.",
            "6.0": "Clear position; reasons given; some development; coherent organisation.",
            "7.0": "Clear position throughout; well-developed reasons; varied vocabulary; complex grammar.",
            "8.0": "Sophisticated argument; nuanced position; precise vocabulary; rare errors.",
            "9.0": "Effortless and insightful argumentation."
        },
        speaking: {
            "5.0": "Maintains conversation but with hesitation; basic vocabulary; frequent errors; mostly intelligible.",
            "6.0": "Speaks at length with some hesitation; range of vocabulary; mix of simple and complex grammar.",
            "7.0": "Speaks at length without noticeable effort; flexible vocabulary; complex structures used regularly.",
            "8.0": "Wide vocabulary used naturally; precise grammar; near-native pronunciation.",
            "9.0": "Effortless, fluent, idiomatic; indistinguishable from native."
        }
    },

    // ============================================================
    // COMMON PHRASES — DEPLOYABLE BANK
    // ============================================================
    common_phrases: {
        speaking_part1: [
            "Well, to be honest…",
            "I'd say…",
            "Actually, that's a good question.",
            "I'm a big fan of…",
            "I'm really into…",
            "Let me think for a moment.",
            "It depends, but generally…",
            "On the whole, yes/no.",
            "I haven't really thought about it, but…",
            "I'd probably say…",
            "It's something I do quite often.",
            "Not as much as I used to."
        ],
        speaking_part2: [
            "I'd like to talk about…",
            "The thing that comes to mind is…",
            "I remember it like it was yesterday.",
            "Looking back, what stood out was…",
            "What I particularly remember is…",
            "It really stayed with me because…",
            "It's hard to put into words, but…",
            "Now that I think about it…",
            "To set the scene a bit…",
            "Just to give you some background…"
        ],
        speaking_part3: [
            "That's an interesting question.",
            "Broadly speaking…",
            "I'd say it cuts both ways.",
            "Having said that…",
            "On balance, I'd argue…",
            "It's hard to say with certainty, but…",
            "If current trends continue…",
            "From my perspective…",
            "I think there's a strong argument that…",
            "Some people would say…, but I'd push back on that.",
            "It tends to be the case that…",
            "In countries like X…"
        ],
        writing_intro: [
            "In recent years, debate has intensified over…",
            "It is increasingly argued that…",
            "There is ongoing discussion about whether…",
            "Few topics divide opinion as sharply as…",
            "While some maintain that X, others contend that Y.",
            "The question of whether… has become particularly pressing.",
            "Educators / governments / commentators have long debated…"
        ],
        writing_body: [
            "The most significant reason is that…",
            "A primary advantage of this trend is…",
            "Equally important is the fact that…",
            "Furthermore, evidence suggests that…",
            "A clear example is…",
            "This is illustrated by the case of…",
            "The downstream consequence is that…",
            "Critics would argue, however, that…",
            "On the other hand, it could be said that…"
        ],
        writing_conclusion: [
            "In conclusion, while X has clear merit…",
            "On balance, the evidence supports the view that…",
            "To conclude, although both sides offer valid points…",
            "It seems clear, therefore, that…",
            "Governments would do well to…",
            "The longer-term implication is that…",
            "A balanced approach that recognises both X and Y is therefore preferable."
        ],
        trend_vocabulary_writing: [
            "rose sharply / surged / soared",
            "increased steadily / climbed gradually",
            "edged up / inched up",
            "fell sharply / plummeted / collapsed",
            "declined steadily / dropped gradually",
            "dipped slightly / fell marginally",
            "remained stable / levelled off / plateaued",
            "fluctuated / oscillated",
            "doubled / tripled / halved",
            "reached a peak of / hit a low of"
        ]
    }
};

