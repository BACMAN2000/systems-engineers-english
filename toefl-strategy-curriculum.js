// TOEFL Strategy Curriculum - Cohasset Language Center
// 23 lessons covering Reading (10), Listening (4), Speaking (6), Writing (3)
// Score coverage: 60-120 | CEFR: B1-C2 | Created: 2026-05-07

window.TOEFL_CURRICULUM = {
    metadata: {
        total_lessons: 23,
        total_hours: 23,
        sections: { reading: 10, listening: 4, speaking: 6, writing: 3 },
        score_coverage: "60-120",
        cefr_coverage: "B1-C2",
        version: "1.0",
        created: "2026-05-07",
        platform: "Cohasset Language Center",
        target_test: "TOEFL iBT (2023+ format)"
    },
    lessons: [
        {
            id: "toefl-reading-1",
            section: "reading",
            score_target: "60-120",
            cefr: "B1-C2",
            title: "Reading: 10 Question Types Overview",
            subtitle: "Map of all question formats and time strategy",
            duration_min: 60,
            objectives: [
                "Identify all 10 TOEFL Reading question types",
                "Understand timing per passage (18 min)",
                "Learn order strategy and skip-then-return tactic"
            ],
            sections: [
                {
                    type: "intro",
                    title: "Reading section structure",
                    content: "TOEFL iBT Reading = 2 passages, ~700 words each, academic level. 10 questions per passage, 18 min per passage, 36 min total. No separate reading time — clock starts immediately."
                },
                {
                    type: "strategy",
                    title: "The 10 question types",
                    content: "<ol><li><b>Factual Information</b> (3-5 per passage) — 'According to paragraph X...'</li><li><b>Negative Factual</b> (1-2) — 'All EXCEPT' or 'NOT mentioned'</li><li><b>Inference</b> (1-2) — 'It can be inferred...'</li><li><b>Rhetorical Purpose</b> (1-2) — 'Why does the author mention X?'</li><li><b>Vocabulary</b> (1-2) — word in context</li><li><b>Reference</b> (0-1) — pronoun referent</li><li><b>Sentence Simplification</b> (0-1) — paraphrase highlighted sentence</li><li><b>Insert Text</b> (1) — place sentence at marker</li><li><b>Prose Summary</b> OR <b>Fill-in-Table</b> (always last, 2 points)</li></ol>"
                },
                {
                    type: "tips",
                    title: "Time budget per passage (18 min)",
                    content: "Min 0-3: skim passage (paragraph topic sentences + conclusion). Min 3-15: answer Q1-9 in order. Min 15-18: tackle Prose Summary (worth 2 points). Skip stuck questions and flag — return at end. Never leave blank: guess 'C' if running out."
                },
                {
                    type: "common_mistakes",
                    title: "Pitfalls to avoid",
                    content: "1) Reading every word slowly — TOEFL allows skim-and-scan. 2) Skipping the Prose Summary — it's worth 2 raw points. 3) Not eliminating wrong answers first. 4) Spending 5+ min on one Q. 5) Trusting memory instead of re-reading the cited paragraph."
                }
            ],
            practice_items: [
                { type: "reflection", q: "How many minutes per passage do you have?", a: "18 minutes (36 total / 2 passages)" },
                { type: "reflection", q: "Which question is worth 2 points?", a: "The last one (Prose Summary or Fill-in-Table)" }
            ],
            next_steps: ["toefl-reading-2 (Factual Information)"]
        },
        {
            id: "toefl-reading-2",
            section: "reading",
            score_target: "60-120",
            cefr: "B1-C2",
            title: "Reading: Factual Information Questions",
            subtitle: "Most common type — 3 to 5 per passage",
            duration_min: 60,
            objectives: [
                "Recognize Factual Information question stems",
                "Use scan-and-verify strategy",
                "Avoid common distractors (extreme words, half-truths)"
            ],
            sections: [
                {
                    type: "intro",
                    title: "What it tests",
                    content: "Factual = explicit information stated in the passage. NOT inference, NOT main idea. The answer is literally written in the text — usually in the cited paragraph."
                },
                {
                    type: "strategy",
                    title: "Question stems to recognize",
                    content: "<ul><li>'According to paragraph X, what...'</li><li>'The author states that...'</li><li>'Paragraph X mentions which of the following...'</li><li>'Which of the following is true about...'</li></ul>"
                },
                {
                    type: "strategy",
                    title: "4-step scan method",
                    content: "<b>Step 1:</b> Read the question — identify the keyword (name, date, term). <b>Step 2:</b> Scan the cited paragraph for that keyword. <b>Step 3:</b> Read the sentence containing it carefully (and the next sentence). <b>Step 4:</b> Match meaning (not exact words) to one answer choice."
                },
                {
                    type: "tips",
                    title: "Distractor patterns",
                    content: "<b>Extreme language:</b> 'always', 'never', 'all', 'only' — usually wrong unless passage uses same. <b>Half-true:</b> first half matches passage, second half adds false info. <b>Out-of-paragraph:</b> info from a different paragraph. <b>Reversed cause/effect:</b> swaps the relationship."
                },
                {
                    type: "common_mistakes",
                    title: "Pitfalls",
                    content: "1) Choosing answer with same wording as passage but wrong meaning. 2) Using outside knowledge instead of passage. 3) Going beyond cited paragraph. 4) Skipping the 'verify' re-read step."
                }
            ],
            practice_items: [
                { type: "drill", q: "If a question says 'According to paragraph 3...', where do you look?", a: "Only paragraph 3 — never paragraphs 1, 2, or 4." },
                { type: "drill", q: "An answer says 'always X'. The passage says 'often X'. Correct?", a: "No — 'always' is too extreme." }
            ],
            next_steps: ["toefl-reading-3 (Negative Factual)"]
        },
        {
            id: "toefl-reading-3",
            section: "reading",
            score_target: "70-120",
            cefr: "B2-C2",
            title: "Reading: Negative Factual Questions",
            subtitle: "Find what is NOT stated — process of elimination",
            duration_min: 60,
            objectives: [
                "Recognize EXCEPT/NOT question stems",
                "Apply elimination method (mark TRUE → odd one out)",
                "Manage longer time required (2-3 min)"
            ],
            sections: [
                {
                    type: "intro",
                    title: "What it tests",
                    content: "Negative Factual = three answers ARE stated; one is NOT (or contradicts the passage). The wrong-three are correct in the passage; the 'right' answer is the false one."
                },
                {
                    type: "strategy",
                    title: "Question stems",
                    content: "<ul><li>'All of the following are mentioned EXCEPT...'</li><li>'Which of the following is NOT mentioned...'</li><li>'The author mentions all of the following EXCEPT...'</li></ul>"
                },
                {
                    type: "strategy",
                    title: "T/F elimination method",
                    content: "<b>Step 1:</b> Read all 4 choices. <b>Step 2:</b> For each, scan passage and mark T (true/stated) or ? (can't find). <b>Step 3:</b> The '?' choice is your answer. <b>Step 4:</b> Double-check by scanning entire cited section once more — TOEFL hides wording (synonyms, paraphrase)."
                },
                {
                    type: "tips",
                    title: "Time management",
                    content: "These take 2-3 min, longer than Factual. Don't rush — but if 3 min in and stuck, mark and move on. Often the 'NOT' is something specific (a name, a number) — easier to scan."
                },
                {
                    type: "common_mistakes",
                    title: "Pitfalls",
                    content: "1) Forgetting the question is reversed — picking a TRUE answer. 2) Marking T too quickly without verifying. 3) Not searching outside cited paragraph (sometimes info is in 2 paragraphs). 4) Mistaking paraphrase for absence — 'transportation' might be 'cars and trains'."
                }
            ],
            practice_items: [
                { type: "drill", q: "In a NOT question, the correct answer is the one that is...", a: "Not stated in the passage (or contradicts it)." },
                { type: "drill", q: "If 3 choices are clearly TRUE, what does that tell you?", a: "The 4th is the answer — you don't even need to verify it." }
            ],
            next_steps: ["toefl-reading-4 (Inference)"]
        },
        {
            id: "toefl-reading-4",
            section: "reading",
            score_target: "75-120",
            cefr: "B2-C2",
            title: "Reading: Inference Questions",
            subtitle: "What is implied but not stated",
            duration_min: 60,
            objectives: [
                "Distinguish inference from factual",
                "Use 'logical bridge' method",
                "Avoid over-inference (too far from text)"
            ],
            sections: [
                {
                    type: "intro",
                    title: "What it tests",
                    content: "Inference = the author implies, doesn't state. The answer is NOT in the passage word-for-word — but it MUST be supported by the passage. Not your opinion, not common knowledge — only what the text logically requires."
                },
                {
                    type: "strategy",
                    title: "Question stems",
                    content: "<ul><li>'It can be inferred from paragraph X that...'</li><li>'Paragraph X suggests/implies that...'</li><li>'What can be concluded about...'</li><li>'The author would most likely agree that...'</li></ul>"
                },
                {
                    type: "strategy",
                    title: "Logical bridge method",
                    content: "<b>Step 1:</b> Re-read cited paragraph. <b>Step 2:</b> For each choice, ask: 'Does the passage GUARANTEE this?' If you need to add outside info, NO. <b>Step 3:</b> The correct answer is a small step beyond the text — usually 1 logical inch, not 1 mile. <b>Step 4:</b> Eliminate choices that contradict, are too extreme, or require info not in passage."
                },
                {
                    type: "tips",
                    title: "Cause-effect and contrast clues",
                    content: "Inference often hinges on words like 'however', 'although', 'despite', 'whereas'. If passage says 'Although X is common, Y is rare' — you can infer X is more common than Y. Look for what's logically necessary."
                },
                {
                    type: "common_mistakes",
                    title: "Pitfalls",
                    content: "1) Over-inferring — 'the author probably hates technology' when text just describes drawbacks. 2) Confusing inference with factual — picking a stated fact. 3) Using world knowledge ('birds fly' isn't an inference if passage didn't say it). 4) Picking the most extreme option."
                }
            ],
            practice_items: [
                { type: "drill", q: "Passage: 'Unlike most birds, penguins cannot fly.' Inference about most birds?", a: "Most birds can fly (logically required by 'unlike')." },
                { type: "drill", q: "What's the difference between Factual and Inference?", a: "Factual = stated explicitly. Inference = implied; you bridge the gap with logic." }
            ],
            next_steps: ["toefl-reading-5 (Rhetorical Purpose)"]
        },
        {
            id: "toefl-reading-5",
            section: "reading",
            score_target: "80-120",
            cefr: "B2-C2",
            title: "Reading: Rhetorical Purpose Questions",
            subtitle: "Why did the author include this?",
            duration_min: 60,
            objectives: [
                "Identify rhetorical functions (illustrate, contrast, define, support)",
                "Connect a sentence to its paragraph's main idea",
                "Memorize purpose verbs"
            ],
            sections: [
                {
                    type: "intro",
                    title: "What it tests",
                    content: "Rhetorical Purpose = WHY the author wrote a specific sentence/paragraph. Not WHAT it says (Factual) — but its FUNCTION in the argument: to illustrate? to contrast? to define? to challenge a previous claim?"
                },
                {
                    type: "strategy",
                    title: "Question stems",
                    content: "<ul><li>'Why does the author mention X?'</li><li>'The author discusses Y in order to...'</li><li>'What is the purpose of paragraph 3?'</li><li>'The author mentions X as an example of...'</li></ul>"
                },
                {
                    type: "strategy",
                    title: "Purpose verbs to know",
                    content: "<b>Common correct answers use:</b> illustrate, exemplify, demonstrate, contrast, compare, define, clarify, support, challenge, refute, introduce, summarize, emphasize. <b>Method:</b> read sentence BEFORE and AFTER the cited part — the function is usually signaled by surrounding context."
                },
                {
                    type: "tips",
                    title: "Connect to paragraph topic",
                    content: "A detail's purpose serves the paragraph's main point. If paragraph argues 'X is harmful', and author mentions a study, the study's purpose is likely 'to support the claim that X is harmful' — NOT 'to describe a study'."
                },
                {
                    type: "common_mistakes",
                    title: "Pitfalls",
                    content: "1) Picking 'to describe X' when the real purpose is to illustrate something larger. 2) Ignoring transition words ('however' = contrast; 'for instance' = exemplify). 3) Treating it like Factual and just summarizing the sentence. 4) Picking the most specific/literal choice."
                }
            ],
            practice_items: [
                { type: "drill", q: "Paragraph topic: 'Volcanoes affect climate.' Author mentions Mount Pinatubo. Purpose?", a: "To provide an example/illustrate how a volcano affected climate." },
                { type: "drill", q: "After 'However,' the author cites a study. Likely purpose?", a: "To contrast with / challenge the previous idea." }
            ],
            next_steps: ["toefl-reading-6 (Vocabulary in Context)"]
        },
        {
            id: "toefl-reading-6",
            section: "reading",
            score_target: "60-120",
            cefr: "B1-C2",
            title: "Reading: Vocabulary in Context",
            subtitle: "Choose the synonym that fits this passage",
            duration_min: 60,
            objectives: [
                "Treat vocab as 'best fit in context', not pure synonym",
                "Use surrounding clues (definition, example, contrast)",
                "Recognize academic words (Coxhead AWL)"
            ],
            sections: [
                {
                    type: "intro",
                    title: "What it tests",
                    content: "A word is highlighted; pick the best synonym from 4 choices. ALL 4 may be valid synonyms in some context — only one fits THIS passage. So context > dictionary memory."
                },
                {
                    type: "strategy",
                    title: "Substitution method",
                    content: "<b>Step 1:</b> Read the sentence containing the word. <b>Step 2:</b> Cover the word — guess your own synonym from context. <b>Step 3:</b> Try each choice in the sentence. <b>Step 4:</b> Pick the one that preserves meaning AND fits the tone (formal academic)."
                },
                {
                    type: "tips",
                    title: "Context clue types",
                    content: "<b>Definition:</b> '...X, that is, Y...' → Y defines X. <b>Example:</b> '...X, such as A, B, C...' → X is the category. <b>Contrast:</b> '...X, unlike Y...' → X is opposite of Y. <b>Restatement:</b> '...X — in other words, Y...'"
                },
                {
                    type: "common_mistakes",
                    title: "Pitfalls",
                    content: "1) Picking the most common meaning when passage uses a secondary meaning. 2) Picking a word that's a synonym in everyday English but wrong tone for academic prose. 3) Skipping the substitution test. 4) Choosing the longest/fanciest word."
                }
            ],
            practice_items: [
                { type: "drill", q: "Word: 'novel'. Sentence: 'a novel approach to...' Synonym?", a: "New/innovative — NOT 'book' (different meaning)." },
                { type: "drill", q: "If you don't know the word, what do you do?", a: "Substitute each choice in the sentence; pick the one that keeps the passage logical." }
            ],
            next_steps: ["toefl-reading-7 (Reference)"]
        },
        {
            id: "toefl-reading-7",
            section: "reading",
            score_target: "60-110",
            cefr: "B1-C1",
            title: "Reading: Reference Questions",
            subtitle: "What does this pronoun refer to?",
            duration_min: 45,
            objectives: [
                "Find the antecedent of pronouns (it, they, this, these, such)",
                "Apply the substitution test",
                "Handle abstract referents (this/which referring to a clause)"
            ],
            sections: [
                {
                    type: "intro",
                    title: "What it tests",
                    content: "A pronoun is highlighted. Pick what it refers back to. Rare in modern TOEFL (0-1 per passage), but easy points if you see one."
                },
                {
                    type: "strategy",
                    title: "Substitution test",
                    content: "<b>Step 1:</b> Replace the pronoun with each choice. <b>Step 2:</b> Check grammar (singular/plural agreement). <b>Step 3:</b> Check meaning — does the sentence still make sense? <b>Step 4:</b> The antecedent is usually the most recent matching noun before the pronoun."
                },
                {
                    type: "tips",
                    title: "Abstract referents",
                    content: "'This' or 'which' can refer to an entire clause/idea, not a single noun. Example: 'Temperatures rose. This caused...' — 'this' = 'the rise in temperatures'."
                },
                {
                    type: "common_mistakes",
                    title: "Pitfalls",
                    content: "1) Picking the closest noun without checking agreement (singular pronoun ≠ plural noun). 2) Ignoring meaning in favor of proximity. 3) Forgetting that 'such' or 'these' often refer back across sentences."
                }
            ],
            practice_items: [
                { type: "drill", q: "'The scientists tested the samples. They were contaminated.' What does 'they' refer to?", a: "The samples (plural; scientists is plural too, but logic favors samples)." }
            ],
            next_steps: ["toefl-reading-8 (Sentence Simplification)"]
        },
        {
            id: "toefl-reading-8",
            section: "reading",
            score_target: "75-120",
            cefr: "B2-C2",
            title: "Reading: Sentence Simplification",
            subtitle: "Pick the paraphrase that keeps essential meaning",
            duration_min: 60,
            objectives: [
                "Identify essential vs. non-essential information",
                "Recognize paraphrase patterns",
                "Eliminate choices that omit core info or add new info"
            ],
            sections: [
                {
                    type: "intro",
                    title: "What it tests",
                    content: "A long sentence is highlighted. Pick the answer that means essentially the same thing. The correct paraphrase keeps the MAIN clauses and key relationships, even if it drops a minor modifier."
                },
                {
                    type: "strategy",
                    title: "Decompose the sentence",
                    content: "<b>Step 1:</b> Find the MAIN subject + main verb. <b>Step 2:</b> Identify the key relationship (cause-effect? contrast? sequence?). <b>Step 3:</b> Note any qualifying words ('only', 'usually', 'except'). <b>Step 4:</b> Match a choice that preserves: main idea + relationship + qualifiers."
                },
                {
                    type: "tips",
                    title: "Wrong-answer patterns",
                    content: "<b>Omits essential info:</b> drops a key qualifier or main clause. <b>Contradicts:</b> reverses cause/effect or 'most' to 'few'. <b>Adds new info:</b> inserts something the original didn't say. <b>Changes meaning:</b> swaps the subject of an action."
                },
                {
                    type: "common_mistakes",
                    title: "Pitfalls",
                    content: "1) Picking the choice with most words from original — often a trap. 2) Picking the shortest (oversimplification). 3) Ignoring 'although', 'because', 'unless'. 4) Missing a flipped subject ('X causes Y' → 'Y causes X')."
                }
            ],
            practice_items: [
                { type: "drill", q: "Original: 'Although X failed, Y succeeded.' Paraphrase: 'X and Y both succeeded.' Correct?", a: "No — 'although X failed' is essential; the paraphrase contradicts." }
            ],
            next_steps: ["toefl-reading-9 (Insert Text)"]
        },
        {
            id: "toefl-reading-9",
            section: "reading",
            score_target: "75-120",
            cefr: "B2-C2",
            title: "Reading: Insert Text Questions",
            subtitle: "Place a sentence at the right black square",
            duration_min: 60,
            objectives: [
                "Identify cohesion clues (pronouns, transitions, repeated terms)",
                "Test all 4 positions before deciding",
                "Recognize 'orphan' phrasing (this/these/such requires antecedent)"
            ],
            sections: [
                {
                    type: "intro",
                    title: "What it tests",
                    content: "A sentence is given; 4 black squares (■) appear in the passage. Pick where the sentence fits best. There's exactly 1 per passage. The answer is signaled by COHESION CLUES in the new sentence."
                },
                {
                    type: "strategy",
                    title: "Cohesion clue checklist",
                    content: "<b>In the NEW sentence, look for:</b> 'this', 'these', 'such', 'this idea', 'this approach' → must follow a sentence introducing that idea. 'However', 'In contrast' → previous sentence is opposite. 'For example' → previous sentence stated a general claim. 'Therefore', 'As a result' → previous sentence is a cause."
                },
                {
                    type: "strategy",
                    title: "Test method",
                    content: "<b>Step 1:</b> Read the new sentence; identify cohesion clue. <b>Step 2:</b> Try each ■ position; read the sentence before and after. <b>Step 3:</b> Pick the position where the cohesion clue links naturally AND the surrounding flow still makes sense."
                },
                {
                    type: "common_mistakes",
                    title: "Pitfalls",
                    content: "1) Only checking the position that 'feels right' — always test all 4. 2) Ignoring 'this/these' — these REQUIRE a specific previous sentence. 3) Picking based on topic match alone — flow matters more. 4) Forgetting that the new sentence also affects the next sentence."
                }
            ],
            practice_items: [
                { type: "drill", q: "New sentence starts with 'However, this view has critics.' Where does it go?", a: "Right after a sentence presenting 'this view' (a specific opinion)." }
            ],
            next_steps: ["toefl-reading-10 (Prose Summary)"]
        },
        {
            id: "toefl-reading-10",
            section: "reading",
            score_target: "80-120",
            cefr: "B2-C2",
            title: "Reading: Prose Summary (2-point question)",
            subtitle: "Pick 3 main ideas from 6 choices",
            duration_min: 75,
            objectives: [
                "Distinguish main ideas from minor details",
                "Reject 'wrong' or 'unstated' info",
                "Manage 4-min budget for the highest-value question"
            ],
            sections: [
                {
                    type: "intro",
                    title: "What it tests",
                    content: "A 1-sentence intro thesis is given. Pick 3 of 6 statements that BEST summarize the passage. Worth 2 points (3 of 3 = 2; 2 of 3 = 1; 1 or 0 = 0). Always last question."
                },
                {
                    type: "strategy",
                    title: "Pick MAIN ideas, reject MINOR ones",
                    content: "<b>Correct (3):</b> represent paragraph-level main ideas — the major points the author argued. <b>Wrong distractors (3):</b> (a) MINOR DETAIL — true but a small example, not a main point. (b) UNSTATED — sounds plausible but not in passage. (c) DISTORTED — exaggerates or reverses what passage said."
                },
                {
                    type: "strategy",
                    title: "Workflow",
                    content: "<b>Step 1:</b> Read intro thesis — anchors what 'main' means. <b>Step 2:</b> Recall paragraph topic sentences. <b>Step 3:</b> Mark each choice: M (main), D (detail), W (wrong/unstated). <b>Step 4:</b> Pick the 3 M's."
                },
                {
                    type: "tips",
                    title: "Time and partial credit",
                    content: "Budget 4 min. Even if you get 2 of 3, you score 1 point — never leave blank. If unsure, prefer broader/general statements (more likely 'main idea') over specific names/dates (more likely 'detail')."
                },
                {
                    type: "common_mistakes",
                    title: "Pitfalls",
                    content: "1) Picking 3 details from one paragraph instead of 3 paragraph-level ideas. 2) Picking distorted statements with familiar wording. 3) Running out of time. 4) Forgetting it's worth 2 points and rushing."
                }
            ],
            practice_items: [
                { type: "drill", q: "How many points is the Prose Summary worth?", a: "2 points (3-of-3 correct = 2; 2-of-3 = 1)." },
                { type: "drill", q: "A choice mentions a specific scientist's name. Likely main idea or detail?", a: "Detail — specific names usually indicate examples, not main ideas." }
            ],
            next_steps: ["toefl-listening-1 (Note-Taking)"]
        },
        {
            id: "toefl-listening-1",
            section: "listening",
            score_target: "60-120",
            cefr: "B1-C2",
            title: "Listening: Note-Taking Strategy",
            subtitle: "Capture structure, not transcript",
            duration_min: 60,
            objectives: [
                "Use a 2-column or T-chart note format",
                "Distinguish main idea from supporting detail",
                "Mark speaker attitude and emphasis"
            ],
            sections: [
                {
                    type: "intro",
                    title: "Listening section structure",
                    content: "TOEFL iBT Listening = 2 conversations (3 min each, 5 Q each) + 3 lectures (3-5 min each, 6 Q each). Total 28 questions, ~36 min. You hear ONCE — notes are critical."
                },
                {
                    type: "strategy",
                    title: "T-chart template",
                    content: "<b>Lecture template:</b><br>Topic: ___<br>Main idea: ___<br>| Point 1 | example/detail |<br>| Point 2 | example/detail |<br>| Point 3 | example/detail |<br>Conclusion / speaker attitude: ___<br><br><b>Conversation template:</b><br>Speakers: ___ | Setting: ___<br>Problem: ___<br>Speaker A view: ___ | Speaker B view: ___<br>Resolution / next step: ___"
                },
                {
                    type: "strategy",
                    title: "Abbreviations and symbols",
                    content: "Use: → (causes/leads to), ↑↓ (increase/decrease), ≠ (different from), ex (example), bc (because), w/ (with), b/w (between), e.g. (such as), Q (question), prof (professor), stu (student), gov (government), env (environment)."
                },
                {
                    type: "tips",
                    title: "What to capture vs. skip",
                    content: "<b>CAPTURE:</b> definitions, lists, contrasts, examples, names/dates, speaker attitude, transitions ('the key point is...', 'however'). <b>SKIP:</b> filler words, repetition, full sentences. Aim for 15-25 words of notes per minute of audio."
                },
                {
                    type: "common_mistakes",
                    title: "Pitfalls",
                    content: "1) Trying to write everything — you'll miss the next sentence. 2) Writing in full sentences instead of keywords. 3) Not marking emphasis (prof says 'this is important' — STAR it). 4) Ignoring tone clues (sarcasm, hesitation)."
                }
            ],
            practice_items: [
                { type: "reflection", q: "Should you write full sentences in your notes?", a: "No — keywords, abbreviations, and symbols only." },
                { type: "reflection", q: "What signals you should write something down?", a: "'The main point is...', 'For example...', 'However...', 'In contrast...', repeated terms." }
            ],
            next_steps: ["toefl-listening-2 (Conversation Q types)"]
        },
        {
            id: "toefl-listening-2",
            section: "listening",
            score_target: "60-120",
            cefr: "B1-C2",
            title: "Listening: Conversation Question Types",
            subtitle: "Office hours and service encounters",
            duration_min: 60,
            objectives: [
                "Recognize conversation Q types (gist/purpose, detail, function, attitude, inference)",
                "Predict the problem-solution structure",
                "Handle 'replay' questions"
            ],
            sections: [
                {
                    type: "intro",
                    title: "Conversation structure",
                    content: "2 conversations: usually (1) student + professor about coursework/research, (2) student + service staff (registrar, librarian, dorm advisor). Always: PROBLEM → discussion → POSSIBLE SOLUTION. 5 questions, ~3 min each."
                },
                {
                    type: "strategy",
                    title: "5 question types",
                    content: "<ol><li><b>Gist-purpose:</b> 'Why does the student visit the professor?' — Listen to opening 30 sec.</li><li><b>Detail:</b> Specific fact — your notes should have this.</li><li><b>Function ('replay'):</b> 'Why does the speaker say this:'  → audio replay. Test: tone/sarcasm/clarification.</li><li><b>Attitude:</b> 'How does the speaker feel?' — listen for tone words and hesitation.</li><li><b>Inference:</b> 'What can be concluded?' — needs logical bridge.</li></ol>"
                },
                {
                    type: "tips",
                    title: "Predict, then confirm",
                    content: "Once you hear the problem, PREDICT the solution. Likely outcomes: extension granted, alternative suggested, referral to another office. Listening for confirmation is faster than listening blank."
                },
                {
                    type: "common_mistakes",
                    title: "Pitfalls",
                    content: "1) Missing the gist by waiting for it — it's stated in the first 30 sec. 2) Picking literal meaning on Function Qs (sarcasm/irony are tested). 3) Confusing speaker attitudes — track who said what. 4) Not noting the resolution/next step."
                }
            ],
            practice_items: [
                { type: "drill", q: "First 30 seconds of a conversation give you which question's answer?", a: "Gist-purpose (why is the student there?)." },
                { type: "drill", q: "If a student says 'Oh, great...' with a flat tone, what attitude?", a: "Sarcastic/displeased — NOT genuine enthusiasm." }
            ],
            next_steps: ["toefl-listening-3 (Lecture Q types)"]
        },
        {
            id: "toefl-listening-3",
            section: "listening",
            score_target: "70-120",
            cefr: "B2-C2",
            title: "Listening: Lecture Question Types",
            subtitle: "Academic talks across 4 disciplines",
            duration_min: 60,
            objectives: [
                "Handle all 6 lecture Q types",
                "Manage Connecting-Content questions (matching, ordering)",
                "Identify professor's stance on competing theories"
            ],
            sections: [
                {
                    type: "intro",
                    title: "Lecture structure",
                    content: "3 lectures, 3-5 min each, 6 Q each. Topics: arts/humanities, life sciences, physical sciences, social sciences. Often: thesis → 2-3 supporting points → counter-view → conclusion."
                },
                {
                    type: "strategy",
                    title: "6 question types",
                    content: "<ol><li><b>Gist-content:</b> 'What is the lecture mainly about?'</li><li><b>Gist-purpose:</b> 'Why does the professor discuss X?'</li><li><b>Detail:</b> specific facts/definitions</li><li><b>Function (replay):</b> why prof says X</li><li><b>Attitude:</b> 'How does the prof feel about X?'</li><li><b>Connecting Content:</b> matching (concept → example), ordering (steps), categorizing (yes/no table)</li></ol>"
                },
                {
                    type: "tips",
                    title: "Listen for signposts",
                    content: "<b>Main idea:</b> 'Today we're going to look at...', 'The key point is...'. <b>List:</b> 'There are three types...'. <b>Contrast:</b> 'However...', 'On the other hand...'. <b>Example:</b> 'Take for instance...'. <b>Conclusion:</b> 'So, what this means is...'"
                },
                {
                    type: "tips",
                    title: "Connecting Content tips",
                    content: "These need precise notes. If prof contrasts 2 theories, draw a T-chart with their features. If prof lists 4 stages, number them. Categorization Qs: build a yes/no checklist as you listen."
                },
                {
                    type: "common_mistakes",
                    title: "Pitfalls",
                    content: "1) Losing focus during 5-min lectures. 2) Confusing competing theories — label clearly in notes. 3) Mistaking an example for the main point. 4) Missing the conclusion (often stated quickly at end)."
                }
            ],
            practice_items: [
                { type: "drill", q: "Professor says 'There are three reasons.' Your immediate action?", a: "Number 1, 2, 3 in your notes — ready to list." },
                { type: "drill", q: "Categorization question asks: which features apply to Theory A vs B?", a: "Use your T-chart notes; check each feature against your column." }
            ],
            next_steps: ["toefl-listening-4 (Inference)"]
        },
        {
            id: "toefl-listening-4",
            section: "listening",
            score_target: "85-120",
            cefr: "C1-C2",
            title: "Listening: Inference & Function Questions",
            subtitle: "Tone, implication, and replay analysis",
            duration_min: 60,
            objectives: [
                "Decode tone and intonation cues",
                "Handle 'Why does the speaker say:' replay items",
                "Distinguish inference from detail"
            ],
            sections: [
                {
                    type: "intro",
                    title: "What these test",
                    content: "Inference and Function questions are the hardest because they require interpretation, not recall. The answer is NOT directly stated — you must read between the lines from tone, context, and pragmatics."
                },
                {
                    type: "strategy",
                    title: "Tone/intonation clues",
                    content: "<b>Doubt:</b> 'Well... I suppose...', rising intonation, pauses. <b>Sarcasm:</b> flat or exaggerated tone, opposite of literal meaning. <b>Enthusiasm:</b> rising pitch, faster speech. <b>Hesitation:</b> 'um', 'er', repeated words — usually means uncertainty or politeness softening bad news."
                },
                {
                    type: "strategy",
                    title: "Function question method",
                    content: "When you hear 'Listen again to part of the lecture' → replay → 'Why does the speaker say:' [replay]: <br>1) Identify what came BEFORE (context). <br>2) Identify the speaker's TONE. <br>3) Determine FUNCTION — is it: clarifying? expressing doubt? emphasizing? changing topic? joking?"
                },
                {
                    type: "tips",
                    title: "Common functions tested",
                    content: "To clarify a misunderstanding | To express skepticism/doubt | To emphasize importance | To indicate a change of topic | To make a joke or lighten mood | To politely disagree | To confirm understanding"
                },
                {
                    type: "common_mistakes",
                    title: "Pitfalls",
                    content: "1) Picking literal meaning on Function Qs (sarcasm trap). 2) Going too far on inference — answer must be passage-supported. 3) Ignoring rhetorical questions (often emphasis, not real questions). 4) Forgetting context before the replayed line."
                }
            ],
            practice_items: [
                { type: "drill", q: "Prof says 'Well, that's ONE way to look at it...' What's the function?", a: "Express doubt / disagree politely with the previous statement." },
                { type: "drill", q: "Inference vs detail — what's different?", a: "Detail = stated; Inference = implied, requires logic on tone/context." }
            ],
            next_steps: ["toefl-speaking-1 (Overview & Rubric)"]
        },
        {
            id: "toefl-speaking-1",
            section: "speaking",
            score_target: "60-120",
            cefr: "B1-C2",
            title: "Speaking: Overview & Rubric",
            subtitle: "4 tasks, 17 minutes, scoring 0-30",
            duration_min: 60,
            objectives: [
                "Know all 4 task formats and timing",
                "Understand the 0-4 rubric (Delivery, Language Use, Topic Development)",
                "Avoid score-killing habits (long silences, off-topic answers)"
            ],
            sections: [
                {
                    type: "intro",
                    title: "Speaking section structure",
                    content: "<b>Task 1 (Independent):</b> 15 sec prep, 45 sec speak. Personal opinion on a familiar topic. <br><b>Task 2 (Integrated — Campus):</b> Read 75-100 words (45-50 sec) → listen to convo (60-80 sec) → 30 sec prep, 60 sec speak. Summarize speaker's opinion + reasons. <br><b>Task 3 (Integrated — Academic concept):</b> Read 75-100 words → listen to lecture (60-90 sec) → 30 sec prep, 60 sec speak. Explain concept using lecture examples. <br><b>Task 4 (Integrated — Lecture only):</b> Listen 90-120 sec → 20 sec prep, 60 sec speak. Summarize lecture's main points."
                },
                {
                    type: "strategy",
                    title: "Rubric: 0-4 per task → scaled to 30",
                    content: "<b>3 categories scored equally:</b> <br>(1) <b>Delivery:</b> clear pronunciation, natural pacing, intonation, minimal pauses. <br>(2) <b>Language Use:</b> grammar, vocabulary range, accuracy. <br>(3) <b>Topic Development:</b> response is full, on-topic, well-organized, with examples. <br><b>Score 4:</b> highly intelligible, sustained speech, well-developed. <br><b>Score 3:</b> generally clear, mostly developed, minor issues. <br><b>Score 2:</b> understandable but with notable issues. <br><b>Score 1:</b> very limited."
                },
                {
                    type: "tips",
                    title: "Score-killing habits",
                    content: "<b>AVOID:</b> long silences (>3 sec), 'um/uh' fillers, reading from screen flatly, monotone, mispronouncing key terms, abandoning sentences mid-way, going off-topic. <b>DO:</b> use linkers (first/then/finally), full sentences, stress key words, finish your last thought (even if cut off)."
                },
                {
                    type: "common_mistakes",
                    title: "Pitfalls",
                    content: "1) Stopping early — fill all the time. 2) Memorized templates that don't fit prompt. 3) Speaking too fast (drops clarity). 4) Forgetting to support opinion with example. 5) Repeating wording from prompt without paraphrasing."
                }
            ],
            practice_items: [
                { type: "reflection", q: "How is each Speaking task scored?", a: "0-4 by 1+ raters across 3 categories (Delivery, Language Use, Topic Development); averaged across 4 tasks; scaled to 0-30." },
                { type: "reflection", q: "What are the 3 rubric categories?", a: "Delivery, Language Use, Topic Development." }
            ],
            next_steps: ["toefl-speaking-2 (Task 1 Independent)"]
        },
        {
            id: "toefl-speaking-2",
            section: "speaking",
            score_target: "60-110",
            cefr: "B1-C1",
            title: "Speaking Task 1: Independent (Personal Choice)",
            subtitle: "15 sec prep + 45 sec answer — your opinion + 2 reasons",
            duration_min: 75,
            objectives: [
                "Use the OREO template (Opinion-Reason-Example-Opinion)",
                "Generate quick examples from your life",
                "Stretch a simple opinion to 45 sec confidently"
            ],
            sections: [
                {
                    type: "intro",
                    title: "Task 1 format",
                    content: "Prompt example: 'Some people prefer to study alone. Others prefer to study in groups. Which do you prefer and why?' You have 15 sec prep, 45 sec speak. Pick a side IMMEDIATELY — don't hedge."
                },
                {
                    type: "strategy",
                    title: "OREO template (45 sec)",
                    content: "<b>O — Opinion (5 sec):</b> 'In my opinion, I prefer studying in groups for two main reasons.' <br><b>R1 — Reason 1 (10 sec):</b> 'First, group study allows me to clarify difficult concepts.' <br><b>E1 — Example (10 sec):</b> 'For example, last semester in my biology class, my study group helped me understand cell division by drawing diagrams together.' <br><b>R2/E2 — Reason 2 + ex (15 sec):</b> 'Second, it keeps me motivated; when I study alone, I get distracted by my phone, but in a group everyone stays focused.' <br><b>O — Closing (5 sec):</b> 'For these reasons, I prefer group study.'"
                },
                {
                    type: "strategy",
                    title: "15-second prep checklist",
                    content: "1) Pick the EASIER side (more examples = better). 2) Jot 2 keywords for reasons (e.g. 'clarify' / 'motivation'). 3) Recall 1 personal example for each. Don't write sentences — keywords only."
                },
                {
                    type: "tips",
                    title: "Useful phrases (memorize)",
                    content: "<b>Opinion:</b> 'In my opinion...', 'Personally, I prefer...', 'I strongly believe that...' <br><b>Adding reasons:</b> 'First and foremost...', 'Furthermore...', 'On top of that...' <br><b>Examples:</b> 'For instance...', 'A good example is...', 'In my own experience...' <br><b>Closing:</b> 'For these reasons...', 'That's why I think...'"
                },
                {
                    type: "common_mistakes",
                    title: "Pitfalls",
                    content: "1) Hedging ('Both have advantages...') — pick one side. 2) Generic examples ('It is good for everyone') — use SPECIFIC personal stories. 3) Running out at 30 sec — keep talking with the closing line. 4) Memorized opening that doesn't fit prompt."
                }
            ],
            practice_items: [
                { type: "drill", q: "Prompt: 'Is it better to live in a big city or small town?' Your 5-sec opening?", a: "'In my opinion, I prefer living in a big city for two main reasons.'" },
                { type: "drill", q: "How long should each reason+example be?", a: "About 10-15 seconds; total 2 reasons = 25-30 sec, plus opening (5) and closing (5)." }
            ],
            next_steps: ["toefl-speaking-3 (Task 2 Campus)"]
        },
        {
            id: "toefl-speaking-3",
            section: "speaking",
            score_target: "70-115",
            cefr: "B2-C1",
            title: "Speaking Task 2: Campus Announcement + Conversation",
            subtitle: "Summarize the speaker's opinion and 2 reasons",
            duration_min: 75,
            objectives: [
                "Read the announcement efficiently in 45-50 sec",
                "Take notes during the 60-80 sec conversation",
                "Use the Task 2 template for a 60 sec response"
            ],
            sections: [
                {
                    type: "intro",
                    title: "Task 2 format",
                    content: "Step 1: Read a 75-100 word campus announcement (45-50 sec) — e.g., 'University will close library at midnight.' Step 2: Listen to 2 students discussing it; ONE student gives a clear opinion + 2 reasons (60-80 sec). Step 3: 30 sec prep. Step 4: 60 sec response — summarize the announcement briefly + the speaker's opinion + 2 reasons."
                },
                {
                    type: "strategy",
                    title: "Note template",
                    content: "<b>READING (45 sec):</b><br>What change: ___<br>Why (2 reasons given): ___<br><br><b>LISTENING:</b><br>Speaker (M/F): ___<br>Opinion: agrees / disagrees<br>Reason 1: ___<br>Reason 2: ___"
                },
                {
                    type: "strategy",
                    title: "60-second response template",
                    content: "<b>Intro (10 sec):</b> 'The university announced that [change] because [brief reason from reading].' <br><b>Speaker's opinion (10 sec):</b> 'In the conversation, the [woman/man] [agrees/disagrees] with this decision.' <br><b>Reason 1 (15-20 sec):</b> 'Her first reason is that [reason 1]. She explains that [supporting detail from convo].' <br><b>Reason 2 (15-20 sec):</b> 'Additionally, she mentions that [reason 2]. Specifically, [detail].' <br><b>Closing (5 sec, optional):</b> 'For these reasons, she opposes/supports the change.'"
                },
                {
                    type: "tips",
                    title: "Useful phrases",
                    content: "<b>Reporting opinion:</b> 'The woman expresses her support for...', 'The man strongly disagrees with...' <br><b>Reporting reasons:</b> 'According to her,...', 'She points out that...', 'He argues that...' <br><b>Linking:</b> 'Her first reason is...', 'In addition,...', 'Moreover,...'"
                },
                {
                    type: "common_mistakes",
                    title: "Pitfalls",
                    content: "1) Giving YOUR opinion — never. Only report the speaker's. 2) Spending too long on the reading summary. 3) Missing one of the 2 reasons. 4) Not identifying the speaker's stance clearly. 5) Quoting the convo word-for-word instead of paraphrasing."
                }
            ],
            practice_items: [
                { type: "drill", q: "Should you give your own opinion in Task 2?", a: "No — only summarize the speaker's view and reasons." },
                { type: "drill", q: "If only ONE student gives a strong opinion, which do you report?", a: "The one with the clear opinion + reasons (the other usually just asks questions)." }
            ],
            next_steps: ["toefl-speaking-4 (Task 3 Academic)"]
        },
        {
            id: "toefl-speaking-4",
            section: "speaking",
            score_target: "75-115",
            cefr: "B2-C1",
            title: "Speaking Task 3: Academic Concept + Lecture Examples",
            subtitle: "Define a concept; explain it using lecture examples",
            duration_min: 75,
            objectives: [
                "Extract a concept definition from the reading",
                "Connect 1-2 lecture examples to that concept",
                "Use Task 3 template for 60-sec response"
            ],
            sections: [
                {
                    type: "intro",
                    title: "Task 3 format",
                    content: "Step 1: Read a 75-100 word academic passage defining a concept (45-50 sec) — e.g., 'Confirmation bias is the tendency to seek info that supports beliefs.' Step 2: Listen to 60-90 sec lecture giving 1-2 examples. Step 3: 30 sec prep. Step 4: 60 sec response — define + use lecture examples to illustrate."
                },
                {
                    type: "strategy",
                    title: "Note template",
                    content: "<b>READING (45 sec):</b><br>Concept name: ___<br>Definition (1 sentence): ___<br><br><b>LECTURE:</b><br>Example 1: ___<br>How it shows the concept: ___<br>Example 2 (if any): ___<br>How it shows the concept: ___"
                },
                {
                    type: "strategy",
                    title: "60-sec response template",
                    content: "<b>Intro (10-15 sec):</b> 'The reading introduces the concept of [X], which is defined as [definition in your own words].' <br><b>Transition (5 sec):</b> 'In the lecture, the professor illustrates this concept with [an example / two examples].' <br><b>Example 1 (20 sec):</b> 'First, the professor describes [example 1]. This shows [concept] because [link to definition].' <br><b>Example 2 (20 sec):</b> 'Second, [example 2]. This also demonstrates [concept] since [link].' <br><b>Closing (optional, 5 sec):</b> 'These examples clearly illustrate [concept].'"
                },
                {
                    type: "tips",
                    title: "Useful phrases",
                    content: "<b>Defining:</b> 'X refers to...', 'X is defined as...', 'In other words, X means...' <br><b>Linking example to concept:</b> 'This is an example of X because...', 'This illustrates X since...', 'This demonstrates how X works...' <br><b>Sequencing:</b> 'First...', 'Second...', 'Furthermore...'"
                },
                {
                    type: "common_mistakes",
                    title: "Pitfalls",
                    content: "1) Defining the concept but not linking examples to it. 2) Over-explaining the example without showing how it illustrates. 3) Reading definition word-for-word from passage. 4) Missing one of two examples. 5) Confusing the concept with its example."
                }
            ],
            practice_items: [
                { type: "drill", q: "Task 3 requires you to do what with the lecture examples?", a: "Use them to illustrate/explain the concept defined in the reading." },
                { type: "drill", q: "Should you read the definition word-for-word?", a: "No — paraphrase in your own words to show language ability." }
            ],
            next_steps: ["toefl-speaking-5 (Task 4 Lecture summary)"]
        },
        {
            id: "toefl-speaking-5",
            section: "speaking",
            score_target: "80-120",
            cefr: "B2-C2",
            title: "Speaking Task 4: Lecture Summary",
            subtitle: "Summarize a 90-120 sec academic lecture in 60 sec",
            duration_min: 75,
            objectives: [
                "Capture the lecture's main concept and 2 sub-points",
                "Use efficient note-taking under pressure",
                "Deliver a clear, organized 60-sec summary in 20 sec prep"
            ],
            sections: [
                {
                    type: "intro",
                    title: "Task 4 format",
                    content: "ONLY listening — no reading. Listen to 90-120 sec academic lecture explaining a topic with 2 sub-concepts/aspects/examples. 20 sec prep (shortest of all tasks). 60 sec response: summarize the main topic + the 2 sub-points with their examples."
                },
                {
                    type: "strategy",
                    title: "Note template",
                    content: "<b>Topic:</b> ___<br><b>Sub-concept 1:</b> ___<br>&nbsp;&nbsp;Definition/explanation: ___<br>&nbsp;&nbsp;Example: ___<br><b>Sub-concept 2:</b> ___<br>&nbsp;&nbsp;Definition/explanation: ___<br>&nbsp;&nbsp;Example: ___"
                },
                {
                    type: "strategy",
                    title: "60-sec response template",
                    content: "<b>Intro (10 sec):</b> 'In the lecture, the professor discusses [topic] and explains [two types/aspects/factors/strategies].' <br><b>Sub-point 1 (22-25 sec):</b> 'The first is [sub-concept 1], which means [definition]. For example, the professor mentions [example details].' <br><b>Sub-point 2 (22-25 sec):</b> 'The second is [sub-concept 2], which involves [definition]. To illustrate, [example details].' <br><b>Closing (optional, 3-5 sec):</b> 'These two examples show how [topic] works.'"
                },
                {
                    type: "tips",
                    title: "Useful phrases",
                    content: "<b>Intro variations:</b> 'The professor explains two types of...', 'The lecture is about [topic], specifically two aspects...' <br><b>Transitions:</b> 'The first type is...', 'Moving on to the second...', 'The other example involves...' <br><b>Reporting:</b> 'According to the professor...', 'The professor uses the example of...', 'She points out that...'"
                },
                {
                    type: "common_mistakes",
                    title: "Pitfalls",
                    content: "1) Only covering 1 of the 2 sub-points. 2) Spending too long on intro (waste of time). 3) Vague examples ('she gave an example') without details. 4) Ignoring topic — diving straight into example 1. 5) Running out of time before sub-point 2."
                }
            ],
            practice_items: [
                { type: "drill", q: "How much prep time for Task 4?", a: "Only 20 seconds — the shortest of any speaking task." },
                { type: "drill", q: "If a lecture has 2 sub-concepts, how much time per sub-concept in your response?", a: "About 22-25 sec each (after a 10-sec intro)." }
            ],
            next_steps: ["toefl-speaking-6 (Pronunciation/Pacing)"]
        },
        {
            id: "toefl-speaking-6",
            section: "speaking",
            score_target: "70-120",
            cefr: "B2-C2",
            title: "Speaking: Pronunciation, Pacing & Intonation",
            subtitle: "Delivery is 1/3 of your score",
            duration_min: 60,
            objectives: [
                "Identify and fix common L1 pronunciation interferences",
                "Use sentence stress and pausing for clarity",
                "Achieve natural pace (140-160 wpm)"
            ],
            sections: [
                {
                    type: "intro",
                    title: "Why delivery matters",
                    content: "Delivery = 1/3 of every Speaking task score. Even with perfect grammar and ideas, poor delivery (mumbling, monotone, wrong stress) drops you from 4 to 2. The TOEFL rater is judging INTELLIGIBILITY — can a non-specialist understand you easily?"
                },
                {
                    type: "strategy",
                    title: "Pacing (140-160 wpm)",
                    content: "<b>Too slow (<120 wpm):</b> sounds hesitant, runs out of content. <b>Too fast (>180 wpm):</b> drops clarity. <b>Target:</b> 140-160 wpm — natural conversational. <b>Practice:</b> read a passage aloud while timing; aim for ~25 words per 10 sec."
                },
                {
                    type: "strategy",
                    title: "Sentence stress = MEANING",
                    content: "English stresses CONTENT words (nouns, main verbs, adjectives) and reduces FUNCTION words (the, of, in, is, are). <br><b>Wrong:</b> 'I think THE first reason IS that...' (every word stressed). <br><b>Right:</b> 'I THINK the FIRST REASON is that...' (only key words stressed). <br>Stressing key words signals importance and improves comprehensibility."
                },
                {
                    type: "tips",
                    title: "Common L1 interferences (Spanish-speakers)",
                    content: "<b>Vowel issues:</b> 'sheep' vs. 'ship' — practice the /i/ vs. /ɪ/ contrast. <b>Final consonants:</b> don't add 'e' before initial 'sp/st/sk' (es-tudent → student). <b>Th sounds:</b> 'think' (/θ/) and 'this' (/ð/) — tongue between teeth. <b>Word stress:</b> 'PHOtograph' vs. 'phoTOgraphy' vs. 'photoGRAPHic' — stress shifts."
                },
                {
                    type: "tips",
                    title: "Intonation patterns",
                    content: "<b>Statements:</b> falling tone at end. <b>Yes/No questions:</b> rising tone. <b>Lists:</b> rising on each item, falling on the last ('apples ↑, oranges ↑, and pears ↓'). <b>Importance:</b> raise pitch + slow down on key word. Avoid monotone — TOEFL raters dock for it."
                },
                {
                    type: "common_mistakes",
                    title: "Pitfalls",
                    content: "1) Speaking in monotone (sounds like reading aloud). 2) Filler words ('um', 'uh', 'you know') >2x in 60 sec. 3) Not pausing at sentence boundaries. 4) Mispronouncing the topic word (kills credibility). 5) Speeding up when nervous."
                }
            ],
            practice_items: [
                { type: "drill", q: "What's the target speaking pace?", a: "140-160 words per minute (~25 words per 10 sec)." },
                { type: "drill", q: "Which words get stressed in English?", a: "Content words: nouns, main verbs, adjectives, adverbs. NOT function words (the, of, is)." },
                { type: "drill", q: "Practice exercise:", a: "Record yourself speaking on a Task 1 prompt. Listen back and count: (a) fillers, (b) long pauses, (c) misstressed words. Aim to halve each over a week." }
            ],
            next_steps: ["toefl-writing-1 (Overview & Rubric)"]
        },
        {
            id: "toefl-writing-1",
            section: "writing",
            score_target: "60-120",
            cefr: "B1-C2",
            title: "Writing: Overview & Rubric",
            subtitle: "2 tasks, 29 minutes, scoring 0-30",
            duration_min: 60,
            objectives: [
                "Know both task formats (Integrated, Academic Discussion)",
                "Understand the 0-5 rubric (per task)",
                "Plan word-count targets and timing"
            ],
            sections: [
                {
                    type: "intro",
                    title: "Writing section structure",
                    content: "<b>Task 1 — Integrated Writing:</b> Read 230-300 word passage (3 min) → Listen to 2-min lecture → Write 150-225 word response in 20 min summarizing how the lecture relates to (usually challenges) the reading. <br><b>Task 2 — Academic Discussion (replaces Independent since 2023):</b> Read a professor's question + 2 student posts → Write 100+ words in 10 min responding with your own opinion + reasoning."
                },
                {
                    type: "strategy",
                    title: "Rubric: 0-5 per task → scaled to 30",
                    content: "<b>Score 5:</b> Selects info accurately, organized, well-developed, occasional minor errors. <br><b>Score 4:</b> Generally good but minor info issues, organization, or grammar. <br><b>Score 3:</b> Conveys some info but with notable omissions/inaccuracies, awkward expression. <br><b>Score 2:</b> Significant content/grammar problems. <br><b>Score 1:</b> Very limited."
                },
                {
                    type: "strategy",
                    title: "Word-count targets",
                    content: "<b>Integrated Task:</b> aim 200-250 words (do not exceed 300). Quality > quantity. <br><b>Academic Discussion:</b> aim 110-150 words (minimum is 100, but 110-130 lets you fully develop). 'Well-developed' >>> word count."
                },
                {
                    type: "tips",
                    title: "Time management per task",
                    content: "<b>Integrated (20 min):</b> 2 min plan, 15 min write, 3 min revise (typos, subject-verb, articles). <br><b>Discussion (10 min):</b> 1 min read & plan, 7 min write, 2 min revise."
                },
                {
                    type: "common_mistakes",
                    title: "Pitfalls",
                    content: "1) Skipping revision time. 2) Over-quoting from reading. 3) Memorized templates that don't engage with the actual prompt. 4) Going off-topic in Discussion task. 5) Writing too short (<100 in Discussion, <150 in Integrated)."
                }
            ],
            practice_items: [
                { type: "reflection", q: "What's the word count target for Integrated Writing?", a: "200-250 words (range 150-225 is acceptable; quality matters most)." },
                { type: "reflection", q: "How is each Writing task scored?", a: "0-5 per task, averaged & scaled to 0-30." }
            ],
            next_steps: ["toefl-writing-2 (Integrated Task)"]
        },
        {
            id: "toefl-writing-2",
            section: "writing",
            score_target: "70-120",
            cefr: "B2-C2",
            title: "Writing Task 1: Integrated (Reading + Lecture)",
            subtitle: "Show how the lecture casts doubt on the reading",
            duration_min: 90,
            objectives: [
                "Take parallel notes (3 reading points + 3 lecture rebuttals)",
                "Use the 4-paragraph Integrated template",
                "Paraphrase precisely without distorting"
            ],
            sections: [
                {
                    type: "intro",
                    title: "Task 1 format",
                    content: "Read 3 min: passage with 1 main thesis + 3 supporting points. Listen 2 min: lecture that USUALLY CHALLENGES (rarely supports) the reading point-by-point. Then 20 min to write 200-250 words summarizing HOW the lecture responds to the reading."
                },
                {
                    type: "strategy",
                    title: "Parallel-notes template",
                    content: "Reading thesis: ___ <br><table border='1'><tr><td><b>Reading point 1:</b> ___</td><td><b>Lecture rebuttal 1:</b> ___</td></tr><tr><td><b>Reading point 2:</b> ___</td><td><b>Lecture rebuttal 2:</b> ___</td></tr><tr><td><b>Reading point 3:</b> ___</td><td><b>Lecture rebuttal 3:</b> ___</td></tr></table><br>The lecture goes in the SAME ORDER as the reading 90% of the time."
                },
                {
                    type: "strategy",
                    title: "4-paragraph template",
                    content: "<b>Para 1 — Intro (2-3 sent):</b> 'The reading argues that [thesis]. However, the lecturer challenges this view, providing three specific counter-arguments to each of the reading's points.' <br><b>Para 2 — Point/Rebuttal 1:</b> 'First, the reading states that [point 1]. The professor disputes this, explaining that [rebuttal 1, with detail].' <br><b>Para 3 — Point/Rebuttal 2:</b> 'Second, the reading claims [point 2]. In contrast, the lecturer points out that [rebuttal 2].' <br><b>Para 4 — Point/Rebuttal 3:</b> 'Finally, while the reading suggests [point 3], the professor argues that [rebuttal 3]. Therefore, the lecture undermines each of the reading's main claims.'"
                },
                {
                    type: "tips",
                    title: "Useful phrases",
                    content: "<b>Reporting reading:</b> 'The reading argues/claims/suggests that...', 'According to the passage...', 'The author maintains that...' <br><b>Reporting lecture (challenge):</b> 'However, the lecturer disputes/refutes/challenges this by...', 'In contrast, the professor points out that...', 'The lecture casts doubt on this claim, asserting that...' <br><b>Linking:</b> 'First/Second/Finally', 'Moreover', 'On the other hand'"
                },
                {
                    type: "common_mistakes",
                    title: "Pitfalls",
                    content: "1) Giving your OWN opinion — never; only report. 2) Copy-pasting from reading. 3) Missing one of three points. 4) Treating reading and lecture in separate paragraphs (must be paired). 5) Going over 300 words — diminishing returns. 6) Misrepresenting lecture (e.g. saying it 'agrees' when it challenges)."
                }
            ],
            practice_items: [
                { type: "drill", q: "Does the lecture usually agree or disagree with the reading?", a: "Usually disagrees (~95% of cases) — challenges each of 3 reading points." },
                { type: "drill", q: "What's the ideal paragraph structure?", a: "Intro + 3 body paragraphs (one per reading point/lecture rebuttal pair)." }
            ],
            next_steps: ["toefl-writing-3 (Academic Discussion)"]
        },
        {
            id: "toefl-writing-3",
            section: "writing",
            score_target: "60-120",
            cefr: "B1-C2",
            title: "Writing Task 2: Academic Discussion (2023+ format)",
            subtitle: "100+ words in 10 min — opinion, reasons, engagement",
            duration_min: 75,
            objectives: [
                "Engage with the professor's question and at least one student post",
                "Develop a clear opinion with 2 specific reasons",
                "Hit 110-150 words with strong language variety"
            ],
            sections: [
                {
                    type: "intro",
                    title: "Task 2 format (replaced old Independent in 2023)",
                    content: "Screen shows: <br>1) <b>Professor's question</b> (introduces a debate, e.g., 'Should governments fund space exploration or focus on Earth's problems?'). <br>2) <b>Student A post</b> (one view, ~3 sentences). <br>3) <b>Student B post</b> (opposing view, ~3 sentences). <br>You: 10 min, 100+ words. Take a position, give reasons, engage with at least one student."
                },
                {
                    type: "strategy",
                    title: "Plan in 1 minute",
                    content: "(a) Read prof Q + Student A + Student B. (b) Pick a side — agree with A, agree with B, or hybrid (most common: pick A or B). (c) Plan 2 specific reasons + 1 example. (d) Pick which student to mention by name."
                },
                {
                    type: "strategy",
                    title: "Response template (110-150 words, 4-5 sentences)",
                    content: "<b>Sent 1 — Position + reference (20-25 wd):</b> 'This is a complex issue, but I lean toward [Student A]'s view that [their position]. While [Student B] makes a fair point about [B's claim], I find A's argument more compelling.' <br><b>Sent 2 — Reason 1 (25-30 wd):</b> 'My main reason is that [reason]. For instance, [specific example — research, country, personal experience].' <br><b>Sent 3 — Reason 2 (25-30 wd):</b> 'Additionally, [reason 2]. A clear example is [example].' <br><b>Sent 4 — Engage with the OTHER student (15-20 wd):</b> 'I understand why [Student B] worries about [issue], but [counter / qualification].' <br><b>Sent 5 — Closing (10-15 wd):</b> 'Ultimately, the benefits of [your position] outweigh the concerns.'"
                },
                {
                    type: "tips",
                    title: "Useful phrases",
                    content: "<b>Position:</b> 'I tend to agree with [Name] that...', 'I share [Name]'s view...', 'My view aligns more with...' <br><b>Engaging:</b> 'Building on [Name]'s point...', 'While [Name] raises a valid concern...', 'I would extend [Name]'s argument by...' <br><b>Reasons:</b> 'My primary reason is...', 'For instance...', 'A specific example is...' <br><b>Concession:</b> 'Although [opposing point] has some merit...', 'I see why some might argue...'"
                },
                {
                    type: "common_mistakes",
                    title: "Pitfalls",
                    content: "1) Ignoring both students — not engaging by name. 2) Generic essay (could be written without reading the posts). 3) Vague example ('It is good for everyone'). 4) Going below 100 words. 5) Memorized template that doesn't fit prompt. 6) Just summarizing the students without giving YOUR view."
                }
            ],
            practice_items: [
                { type: "drill", q: "Minimum word count for Discussion task?", a: "100 words; aim for 110-150." },
                { type: "drill", q: "Should you mention a student by name?", a: "Yes — engaging with at least one student boosts your 'topic development' score." },
                { type: "drill", q: "How much time to plan?", a: "About 1 min (read all 3 inputs + decide position + jot reasons), then write 7-8 min, revise 1-2 min." }
            ],
            next_steps: ["Full mock test"]
        }
    ],
    score_calculator: {
        reading: {
            items: 20,
            scoring: "Each Q = 1 point except Prose Summary (2). Raw 0-22 scaled to 0-30 (~linear, ~1.5x).",
            sample_conversion: "Raw 18 → ~24 scaled, Raw 14 → ~19 scaled, Raw 22 → 30 scaled"
        },
        listening: {
            items: 28,
            scoring: "Most Q = 1 point; some matching/connecting Q = 2 points. Raw scaled to 0-30 (~linear).",
            sample_conversion: "Raw 24 → ~24 scaled, Raw 18 → ~17 scaled"
        },
        speaking: {
            tasks: 4,
            scoring: "Each task scored 0-4 by raters; sum (max 16) scaled to 0-30 (~×1.875).",
            sample_conversion: "Sum 12 → ~22 scaled, Sum 14 → ~26 scaled, Sum 16 → 30 scaled"
        },
        writing: {
            tasks: 2,
            scoring: "Each task scored 0-5; sum (max 10) scaled to 0-30 (~×3).",
            sample_conversion: "Sum 7 → ~21 scaled, Sum 8 → ~24 scaled, Sum 9 → ~27 scaled, Sum 10 → 30 scaled"
        },
        total_max: 120,
        cefr_thresholds: {
            B1: "57-71",
            B2: "72-94",
            C1: "95-113",
            C2: "114-120"
        }
    },
    common_phrases: {
        speaking_independent: [
            "In my opinion, the most important factor is...",
            "Personally, I strongly believe that...",
            "There are two main reasons. First,...",
            "For example, when I was in high school,...",
            "A good example from my own experience is...",
            "Furthermore / Moreover / On top of that,...",
            "To sum up, I believe that...",
            "For these reasons, I prefer..."
        ],
        speaking_integrated_campus: [
            "The university announced that...",
            "In the conversation, the woman/man expresses her/his support for / opposition to...",
            "Her first reason is that...",
            "She also points out that...",
            "According to the speaker,...",
            "The man argues that...",
            "Specifically, the speaker mentions..."
        ],
        speaking_integrated_academic: [
            "The reading defines [concept] as...",
            "In the lecture, the professor illustrates this concept with two examples.",
            "The first example involves...",
            "This demonstrates [concept] because...",
            "Similarly, the second example...",
            "These examples clearly show how [concept] works."
        ],
        speaking_lecture_summary: [
            "In the lecture, the professor discusses...",
            "She explains two types/factors/aspects of...",
            "The first type/factor is...",
            "To illustrate, the professor describes...",
            "The second type/factor involves...",
            "The professor uses the example of..."
        ],
        writing_integrated: [
            "The reading and the lecture both discuss...",
            "The reading argues that..., however the lecturer casts doubt on this view.",
            "First, the reading claims that...; the professor counters that...",
            "Second, while the reading suggests that..., the lecture refutes this by...",
            "Finally, although the passage maintains that..., the professor disputes this claim, asserting that...",
            "In contrast / On the other hand,...",
            "Therefore, the lecture undermines each of the reading's main points."
        ],
        writing_discussion: [
            "I tend to agree with [Student] that...",
            "While [Student]'s argument has some merit, I believe...",
            "Building on [Student]'s point, I would add that...",
            "My primary reason is that...",
            "For instance, in my country,...",
            "Although some might argue that..., I think...",
            "Ultimately, the benefits outweigh the concerns."
        ],
        transitions_academic: [
            "Furthermore", "Moreover", "In addition", "Additionally",
            "However", "Nevertheless", "On the other hand", "In contrast",
            "Therefore", "Consequently", "As a result", "Thus",
            "For example", "For instance", "Specifically", "To illustrate",
            "First / Second / Finally", "Most importantly", "In conclusion"
        ]
    },
    note_taking_templates: {
        listening_lecture: "Topic: ___ | Main idea: ___ | Detail/Point 1: ___ (example: ___) | Point 2: ___ (example: ___) | Point 3: ___ (example: ___) | Conclusion / Speaker attitude: ___",
        listening_conversation: "Speakers: ___ | Setting: ___ | Problem: ___ | Speaker A view: ___ | Speaker B view: ___ | Resolution / Next step: ___",
        speaking_t2: "READING (45 sec): What change = ___ | Reason given = ___ || CONVERSATION: Speaker (M/F) = ___ | Opinion = agrees/disagrees | Reason 1 = ___ | Reason 2 = ___",
        speaking_t3: "READING (45 sec): Concept = ___ | Definition = ___ || LECTURE: Example 1 = ___ (links to concept how? = ___) | Example 2 = ___ (links how? = ___)",
        speaking_t4: "Topic = ___ | Sub-concept 1 (def + example) = ___ | Sub-concept 2 (def + example) = ___",
        writing_integrated: "READING thesis: ___ | Pt 1 = ___ | Pt 2 = ___ | Pt 3 = ___ || LECTURE (challenges): Rebuttal 1 = ___ | Rebuttal 2 = ___ | Rebuttal 3 = ___",
        writing_discussion: "Prof Q: ___ | Student A view: ___ | Student B view: ___ | MY position: ___ | Reason 1 + example: ___ | Reason 2 + example: ___ | Engage with [name]: ___"
    },
    study_plan_template: {
        weeks_1_2: "Reading lessons 1-5 + Listening lesson 1; daily 30-min vocab (AWL + topic-based)",
        weeks_3_4: "Reading lessons 6-10 + Listening lessons 2-4; 2 timed mock Reading sections",
        weeks_5_6: "Speaking lessons 1-3; daily 15-min recording + self-review",
        weeks_7_8: "Speaking lessons 4-6 + Writing lesson 1; full Speaking mock",
        weeks_9_10: "Writing lessons 2-3; full Writing mock + revision practice",
        week_11: "Full TOEFL mock test (under timed conditions)",
        week_12: "Targeted review of weakest section + final mock"
    }
};

// End of TOEFL_CURRICULUM
// Total: 23 lessons | Reading 10 + Listening 4 + Speaking 6 + Writing 3
// Cohasset Language Center - v1.0 - 2026-05-07
