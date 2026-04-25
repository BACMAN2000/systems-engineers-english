# -*- coding: utf-8 -*-
"""Generate IB/IGCSE framework metadata for each of 66 CLIL projects."""
import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('clil_plans.json', 'r', encoding='utf-8') as f:
    plans = json.load(f)

# ============= IB FRAMEWORK DATA =============

# IB schemas by grade
# G1-G5: PYP (Primary Years Programme)
# G6-G10: MYP (Middle Years Programme)
# G11: DP (Diploma Programme) / IGCSE for lower secondary prep

# --------- PYP PRIMARY (G1-G5) ---------
# Schema: Transdisciplinary theme, Central idea, 3 lines of inquiry,
# Key concepts, Related concepts, ATL, Learner profile, Success criteria

PYP_PROJECTS = {
"G1_U1": {
  "framework":"PYP", "age_range":"5-6",
  "transdisciplinary_theme":"Who We Are",
  "central_idea":"We are unique individuals who belong to a community.",
  "lines_of_inquiry":["Characteristics that make me unique (names, age, looks)","How I am similar to and different from others","How I belong in my class family"],
  "key_concepts":["Form","Connection"],
  "related_concepts":["identity","belonging","similarity"],
  "atl_skills":["Communication (speaking clearly)","Self-management (organizing myself)","Social (forming friendships)"],
  "learner_profile":["Communicators","Caring","Principled"],
  "success_criteria":["I can say my name, age, and 3 things about me","I can greet a classmate in English","I can point to my self-portrait and describe it","I can listen respectfully to peers"],
  "cambridge_link":"Pre-Starters oral interaction (greetings, self-introduction)"
},
"G1_U2": {
  "framework":"PYP", "age_range":"5-6",
  "transdisciplinary_theme":"How We Organize Ourselves",
  "central_idea":"Classrooms have objects organized in ways that help us learn.",
  "lines_of_inquiry":["Items we find in our classroom","Ways we count and sort them","Why organization helps us"],
  "key_concepts":["Form","Function","Responsibility"],
  "related_concepts":["classification","quantity","order"],
  "atl_skills":["Research (observing, collecting)","Thinking (sorting)","Self-management (using objects)"],
  "learner_profile":["Inquirers","Knowledgeable","Principled"],
  "success_criteria":["I can name 10 classroom objects in English","I can count to 20","I can sort objects by type or colour","I can say: There are X books"],
  "cambridge_link":"Pre-Starters (classroom vocabulary, numbers 1-20)"
},
"G1_U3": {
  "framework":"PYP", "age_range":"5-6",
  "transdisciplinary_theme":"Who We Are",
  "central_idea":"Our bodies let us do amazing things, and we must care for them.",
  "lines_of_inquiry":["Parts of my body and what each does","What my body can do (actions)","How I take care of my body"],
  "key_concepts":["Form","Function","Responsibility"],
  "related_concepts":["health","movement","wellbeing"],
  "atl_skills":["Communication (singing, acting)","Self-management (healthy habits)","Social (group performance)"],
  "learner_profile":["Knowledgeable","Balanced","Risk-takers"],
  "success_criteria":["I can name 10 body parts","I can use 'can' to describe actions (I can jump)","I can participate in a group performance","I can list 3 healthy habits"],
  "cambridge_link":"Pre-Starters (body vocabulary, can for ability)"
},
"G1_U4": {
  "framework":"PYP", "age_range":"5-6",
  "transdisciplinary_theme":"Sharing the Planet",
  "central_idea":"Animals live in different places and have different needs; we share the world with them.",
  "lines_of_inquiry":["Different farm animals and their sounds","What animals can and cannot do","How animals are similar to / different from humans"],
  "key_concepts":["Form","Connection","Perspective"],
  "related_concepts":["habitat","characteristics","respect"],
  "atl_skills":["Research (observing)","Communication (presenting)","Thinking (comparing)"],
  "learner_profile":["Caring","Inquirers","Open-minded"],
  "success_criteria":["I can name 6 farm animals and their sounds","I can say what each animal can do","I can make a mask and perform as an animal","I can respect animals in my talk"],
  "cambridge_link":"Pre-Starters/Starters (animals, can for ability)"
},
"G1_U5": {
  "framework":"PYP", "age_range":"5-6",
  "transdisciplinary_theme":"Who We Are",
  "central_idea":"Families are groups of people connected by love and care.",
  "lines_of_inquiry":["Members of my family and their roles","Different family structures","How my family shows love"],
  "key_concepts":["Connection","Perspective","Responsibility"],
  "related_concepts":["relationships","values","diversity"],
  "atl_skills":["Communication (presenting family)","Social (empathy)","Self-management (gratitude)"],
  "learner_profile":["Caring","Open-minded","Communicators"],
  "success_criteria":["I can name 6 family members in English","I can use 'This is my X' to present photos","I can make a family tree","I can express gratitude (I love my X)"],
  "cambridge_link":"Starters (family, possessive adjectives)"
},
"G1_U6": {
  "framework":"PYP", "age_range":"5-6",
  "transdisciplinary_theme":"Who We Are",
  "central_idea":"The foods we eat affect how healthy and happy we feel.",
  "lines_of_inquiry":["Foods I like and don't like","Which foods help me grow strong","Balanced meals"],
  "key_concepts":["Function","Responsibility","Reflection"],
  "related_concepts":["nutrition","choice","habits"],
  "atl_skills":["Research (observing foods)","Thinking (classifying)","Self-management (healthy choices)"],
  "learner_profile":["Balanced","Knowledgeable","Principled"],
  "success_criteria":["I can name 10 foods in English","I can say: I like/don't like X","I can sort foods into healthy/treats","I can present my healthy plate"],
  "cambridge_link":"Starters (food, like + noun, don't like)"
},

"G2_U1": {
  "framework":"PYP", "age_range":"6-7",
  "transdisciplinary_theme":"Who We Are",
  "central_idea":"Each person has a unique identity shaped by appearance, personality, likes, and relationships.",
  "lines_of_inquiry":["Physical appearance and personality","Things I like and dislike","My family, school, and hobbies"],
  "key_concepts":["Form","Connection","Perspective"],
  "related_concepts":["identity","preferences","self-awareness"],
  "atl_skills":["Communication (writing about self)","Self-management (reflection)","Social (sharing)"],
  "learner_profile":["Communicators","Reflective","Caring"],
  "success_criteria":["I can describe myself in 5 sentences","I can use 'I like/don't like + ing'","I can make a booklet with 5 pages","I can present to peers"],
  "cambridge_link":"Starters (self-description, appearance, likes)"
},
"G2_U2": {
  "framework":"PYP", "age_range":"6-7",
  "transdisciplinary_theme":"Where We Are in Place and Time",
  "central_idea":"Homes are organized spaces that reflect how we live.",
  "lines_of_inquiry":["Rooms in my home and their functions","Furniture and household objects","Where things are located (spatial language)"],
  "key_concepts":["Form","Function","Connection"],
  "related_concepts":["organization","space","routine"],
  "atl_skills":["Research (mapping)","Thinking (spatial)","Communication (describing)"],
  "learner_profile":["Inquirers","Knowledgeable","Communicators"],
  "success_criteria":["I can label 8 rooms and 15 furniture items","I can use prepositions (in, on, under)","I can draw and describe a floor plan","I can give an oral tour (40 words)"],
  "cambridge_link":"Starters (home vocabulary, prepositions of place)"
},
"G2_U3": {
  "framework":"PYP", "age_range":"6-7",
  "transdisciplinary_theme":"Sharing the Planet",
  "central_idea":"Pets and wild animals have different needs and deserve care.",
  "lines_of_inquiry":["Pets and wild animals","Animal characteristics and habits","Responsibility for animal care"],
  "key_concepts":["Form","Function","Responsibility"],
  "related_concepts":["habitat","needs","care"],
  "atl_skills":["Research (fact-gathering)","Communication (writing facts)","Social (responsibility)"],
  "learner_profile":["Caring","Knowledgeable","Principled"],
  "success_criteria":["I can describe an animal with 'has/can/eats'","I can make 5 fact cards","I can explain pet care needs","I can present orally (3-4 sentences each)"],
  "cambridge_link":"Starters (animals, has got, can for ability)"
},
"G2_U4": {
  "framework":"PYP", "age_range":"6-7",
  "transdisciplinary_theme":"Where We Are in Place and Time",
  "central_idea":"Our town is made of places that serve different purposes in our community.",
  "lines_of_inquiry":["Places in my town","How to give and follow directions","What each place is used for"],
  "key_concepts":["Form","Function","Connection"],
  "related_concepts":["community","navigation","service"],
  "atl_skills":["Research (mapping)","Communication (directions)","Thinking (spatial)"],
  "learner_profile":["Communicators","Knowledgeable","Open-minded"],
  "success_criteria":["I can name 10 places in town","I can give directions (go straight, turn)","I can draw a labelled map","I can write a 30-40 word postcard"],
  "cambridge_link":"Starters (places, prepositions of movement)"
},
"G2_U5": {
  "framework":"PYP", "age_range":"6-7",
  "transdisciplinary_theme":"Who We Are",
  "central_idea":"Healthy habits at every meal help us feel and grow well.",
  "lines_of_inquiry":["Different food groups","Why our choices matter","Tracking our eating habits"],
  "key_concepts":["Function","Responsibility","Reflection"],
  "related_concepts":["nutrition","health","data"],
  "atl_skills":["Research (tracking)","Self-management (choices)","Thinking (classifying)"],
  "learner_profile":["Balanced","Principled","Reflective"],
  "success_criteria":["I can classify food groups","I can keep a 5-day food diary","I can explain healthy vs treat","I can make a wellness poster"],
  "cambridge_link":"Starters (food, like + ing, should/shouldn't)"
},
"G2_U6": {
  "framework":"PYP", "age_range":"6-7",
  "transdisciplinary_theme":"How We Express Ourselves",
  "central_idea":"Hobbies help us express who we are and enjoy our time.",
  "lines_of_inquiry":["Different hobbies and sports","Why I like my hobby","How hobbies connect us"],
  "key_concepts":["Form","Perspective","Reflection"],
  "related_concepts":["self-expression","leisure","creativity"],
  "atl_skills":["Communication (show-and-tell)","Self-management (preparing)","Social (sharing)"],
  "learner_profile":["Communicators","Balanced","Reflective"],
  "success_criteria":["I can describe my hobby (4 sentences)","I can explain 2 reasons I like it","I can present show-and-tell","I can write 30-40 word paragraph"],
  "cambridge_link":"Starters (hobbies, like + ing, frequency adverbs)"
},

"G3_U1": {
  "framework":"PYP", "age_range":"7-8",
  "transdisciplinary_theme":"How We Organize Ourselves",
  "central_idea":"Schools organize time and activities so we can learn different things.",
  "lines_of_inquiry":["My school subjects and what I learn","How time structures our day","Why schedules help us"],
  "key_concepts":["Form","Function","Connection"],
  "related_concepts":["organization","time","routine"],
  "atl_skills":["Research (tracking schedule)","Thinking (analyzing patterns)","Communication (explaining)"],
  "learner_profile":["Knowledgeable","Reflective","Communicators"],
  "success_criteria":["I can tell time (o'clock, half past)","I can name 8 school subjects","I can design my schedule","I can write 60w description"],
  "cambridge_link":"Pre-Movers (subjects, time, adverbs of frequency)"
},
"G3_U2": {
  "framework":"PYP", "age_range":"7-8",
  "transdisciplinary_theme":"How the World Works",
  "central_idea":"Our daily routines follow patterns connected to our body clock.",
  "lines_of_inquiry":["Things I do at different times","Why we do things at specific times","How different people organize time"],
  "key_concepts":["Function","Change","Causation"],
  "related_concepts":["cycles","biology","data"],
  "atl_skills":["Research (surveying)","Thinking (identifying patterns)","Communication (reporting)"],
  "learner_profile":["Inquirers","Thinkers","Reflective"],
  "success_criteria":["I can use adverbs of frequency correctly","I can survey classmates","I can make a bar chart","I can write 60w paragraph"],
  "cambridge_link":"Pre-Movers (daily routines, frequency adverbs, time)"
},
"G3_U3": {
  "framework":"PYP", "age_range":"7-8",
  "transdisciplinary_theme":"How the World Works",
  "central_idea":"Weather follows patterns that affect our clothes, activities, and emotions.",
  "lines_of_inquiry":["Different weather conditions and seasons","How we measure and describe weather","How weather changes what we do"],
  "key_concepts":["Form","Change","Connection"],
  "related_concepts":["patterns","cycles","adaptation"],
  "atl_skills":["Research (observing, recording)","Thinking (analysis)","Communication (reporting)"],
  "learner_profile":["Inquirers","Knowledgeable","Communicators"],
  "success_criteria":["I can describe weather (sunny, cloudy, rainy)","I can keep a 7-day log","I can calculate how many sunny days","I can write a 60w report"],
  "cambridge_link":"Pre-Movers (weather vocabulary, present continuous, because)"
},
"G3_U4": {
  "framework":"PYP", "age_range":"7-8",
  "transdisciplinary_theme":"Sharing the Planet",
  "central_idea":"Every species has a role in nature, and humans must protect them.",
  "lines_of_inquiry":["Wild animals and their habitats","Why some species are endangered","How we can protect biodiversity"],
  "key_concepts":["Form","Causation","Responsibility"],
  "related_concepts":["habitat","biodiversity","stewardship"],
  "atl_skills":["Research (species research)","Communication (campaigning)","Thinking (cause-effect)"],
  "learner_profile":["Caring","Principled","Knowledgeable"],
  "success_criteria":["I can describe 1 endangered species","I can explain 2 causes","I can write a 70w plea","I can design a campaign poster"],
  "cambridge_link":"Pre-Movers/Movers (animals, comparatives, must/should)"
},
"G3_U5": {
  "framework":"PYP", "age_range":"7-8",
  "transdisciplinary_theme":"Who We Are",
  "central_idea":"We all feel emotions, and we can learn strategies to handle them.",
  "lines_of_inquiry":["Different emotions we feel","Why we feel them","Strategies to help us regulate"],
  "key_concepts":["Form","Causation","Responsibility"],
  "related_concepts":["wellbeing","self-regulation","empathy"],
  "atl_skills":["Self-management (regulation)","Social (empathy)","Communication (expression)"],
  "learner_profile":["Balanced","Reflective","Caring"],
  "success_criteria":["I can name 8 emotions","I can explain causes (I feel X because)","I can use 'should/must' for strategies","I can present a feelings kit"],
  "cambridge_link":"Pre-Movers (emotions, modals: should/must)"
},
"G3_U6": {
  "framework":"PYP", "age_range":"7-8",
  "transdisciplinary_theme":"How We Organize Ourselves",
  "central_idea":"Communities rely on helpers who each contribute a vital role.",
  "lines_of_inquiry":["Different jobs in our community","What helpers do and why","How to value their work"],
  "key_concepts":["Function","Connection","Responsibility"],
  "related_concepts":["community","interdependence","service"],
  "atl_skills":["Communication (interviewing, performing)","Social (citizenship)","Research (fact-gathering)"],
  "learner_profile":["Caring","Communicators","Open-minded"],
  "success_criteria":["I can name 8 community helpers + their tools","I can perform in a short play","I can interview and write 70w report","I can show appreciation"],
  "cambridge_link":"Pre-Movers (community, present simple, jobs)"
},

"G4_U1": {
  "framework":"PYP", "age_range":"8-9",
  "transdisciplinary_theme":"Where We Are in Place and Time",
  "central_idea":"Our neighbourhoods are organized spaces that meet people's daily needs.",
  "lines_of_inquiry":["Key places in my neighbourhood","Distances and scales","How transport connects places"],
  "key_concepts":["Form","Function","Connection"],
  "related_concepts":["geography","community","scale"],
  "atl_skills":["Research (observation)","Thinking (spatial)","Communication (map-making)"],
  "learner_profile":["Inquirers","Knowledgeable","Communicators"],
  "success_criteria":["I can build a scaled 3D model","I can use relative clauses (the park where…)","I can write 80w description","I can give an oral tour (4 min)"],
  "cambridge_link":"Movers (geography, relatives, past simple)"
},
"G4_U2": {
  "framework":"PYP", "age_range":"8-9",
  "transdisciplinary_theme":"How We Express Ourselves",
  "central_idea":"Video lets us document and share our experiences with others.",
  "lines_of_inquiry":["Spaces in my school and what happens there","How to film a tour","Digital storytelling"],
  "key_concepts":["Form","Function","Perspective"],
  "related_concepts":["media","narrative","technology"],
  "atl_skills":["Communication (scripting, presenting)","Self-management (production)","Thinking (storytelling)"],
  "learner_profile":["Communicators","Risk-takers","Reflective"],
  "success_criteria":["I can plan a 5-stop tour","I can film and edit a 2-min video","I can narrate in English","I can publish and share"],
  "cambridge_link":"Movers (school vocabulary, present + past)"
},
"G4_U3": {
  "framework":"PYP", "age_range":"8-9",
  "transdisciplinary_theme":"Sharing the Planet",
  "central_idea":"Peruvian biodiversity is our heritage and responsibility to protect.",
  "lines_of_inquiry":["Endangered Peruvian species","Causes of endangerment","Actions we can take"],
  "key_concepts":["Causation","Responsibility","Change"],
  "related_concepts":["conservation","heritage","advocacy"],
  "atl_skills":["Research","Communication (campaign)","Thinking (cause-effect)"],
  "learner_profile":["Caring","Principled","Risk-takers"],
  "success_criteria":["I can research 1 Peruvian species","I can write 80w appeal with modals","I can design a persuasive poster","I can deliver an oral pitch"],
  "cambridge_link":"Movers (wildlife, must/should, comparatives)"
},
"G4_U4": {
  "framework":"PYP", "age_range":"8-9",
  "transdisciplinary_theme":"How We Express Ourselves",
  "central_idea":"Sports connect cultures around the world and reveal shared values.",
  "lines_of_inquiry":["Sports from different countries","Cultural context of sports","Values in sport (teamwork, fairness)"],
  "key_concepts":["Form","Connection","Perspective"],
  "related_concepts":["culture","tradition","diversity"],
  "atl_skills":["Research (culture)","Social (teamwork)","Communication (presenting)"],
  "learner_profile":["Open-minded","Balanced","Communicators"],
  "success_criteria":["I can describe a sport from another country","I can demo basic moves","I can write 80-100w cultural profile","I can perform at Olympics Day"],
  "cambridge_link":"Movers (sports, past simple, comparatives)"
},
"G4_U5": {
  "framework":"PYP", "age_range":"8-9",
  "transdisciplinary_theme":"Where We Are in Place and Time",
  "central_idea":"Expeditions combine planning, curiosity, and resilience to explore new places.",
  "lines_of_inquiry":["Destinations and routes","What we need for a trip","Stories of adventure"],
  "key_concepts":["Function","Causation","Connection"],
  "related_concepts":["exploration","planning","narrative"],
  "atl_skills":["Research (geography)","Thinking (planning)","Communication (narrative)"],
  "learner_profile":["Risk-takers","Inquirers","Balanced"],
  "success_criteria":["I can plan a multi-stop route","I can list essential equipment with reasons","I can map my route","I can write a 100w narrative (Day 1)"],
  "cambridge_link":"Movers (travel, past simple, sequencers)"
},
"G4_U6": {
  "framework":"PYP", "age_range":"8-9",
  "transdisciplinary_theme":"Who We Are",
  "central_idea":"Who I become is shaped by what I do today.",
  "lines_of_inquiry":["Jobs and careers","What I'm good at and enjoy","Steps to achieve future goals"],
  "key_concepts":["Change","Perspective","Responsibility"],
  "related_concepts":["goals","aspirations","self-awareness"],
  "atl_skills":["Self-management (goal-setting)","Thinking (planning)","Communication (visualizing)"],
  "learner_profile":["Reflective","Risk-takers","Principled"],
  "success_criteria":["I can list 10 jobs and their skills","I can use 'will' for future plans","I can make a vision board","I can write 100w essay"],
  "cambridge_link":"Movers (jobs, future with will, because/so)"
},

"G5_U1": {
  "framework":"PYP", "age_range":"9-10",
  "transdisciplinary_theme":"Who We Are",
  "central_idea":"Our identity is a unique blend of personality, values, and life experiences.",
  "lines_of_inquiry":["What makes me 'me' (personality, values)","How values shape decisions","Representing identity through art"],
  "key_concepts":["Form","Perspective","Reflection"],
  "related_concepts":["self-awareness","values","expression"],
  "atl_skills":["Self-management (reflection)","Communication (art + writing)","Thinking (self-analysis)"],
  "learner_profile":["Reflective","Principled","Communicators"],
  "success_criteria":["I can describe personality + values","I can produce a mixed-media portrait","I can write a 150w reflective essay","I can present with confidence"],
  "cambridge_link":"Flyers (personality adjectives, past continuous, values)"
}
}

# Auto-fill rest of PYP (G5 U2-U6) with a shorter pattern
def make_pyp(theme, central, loi, kc, rc, atl, lp, sc, link, age="9-10"):
    return {"framework":"PYP","age_range":age,"transdisciplinary_theme":theme,
            "central_idea":central,"lines_of_inquiry":loi,
            "key_concepts":kc,"related_concepts":rc,
            "atl_skills":atl,"learner_profile":lp,
            "success_criteria":sc,"cambridge_link":link}

PYP_PROJECTS["G5_U2"] = make_pyp(
  "Who We Are",
  "Our daily habits and economic choices shape our wellbeing.",
  ["Daily habits and their impact","Income, expense, and wants vs needs","Designing a personal budget"],
  ["Function","Causation","Responsibility"],
  ["habits","economy","choice"],
  ["Self-management (tracking)","Thinking (math + analysis)","Research (data)"],
  ["Balanced","Principled","Reflective"],
  ["I can categorize expenses in a spreadsheet","I can use 'used to' and past continuous","I can write 150w reflection on habits","I can present a budget plan"],
  "Flyers (lifestyle, used to, past continuous)"
)
PYP_PROJECTS["G5_U3"] = make_pyp(
  "Sharing the Planet",
  "Ecosystems are interconnected, and human actions affect them.",
  ["Peruvian ecosystems and food chains","Human impact on biodiversity","How we can campaign for change"],
  ["Connection","Causation","Responsibility"],
  ["sustainability","ecosystems","advocacy"],
  ["Research (issue)","Communication (digital campaign)","Thinking (critical)"],
  ["Caring","Principled","Communicators"],
  ["I can explain 1 Peruvian ecosystem issue","I can use passive voice in writing","I can design a digital leaflet","I can deliver a 2-min pitch"],
  "Flyers (environment, passive intro, conditionals 0)"
)
PYP_PROJECTS["G5_U4"] = make_pyp(
  "How We Express Ourselves",
  "Cultures express identity through traditions, food, and celebrations.",
  ["Cultural traditions around the world","How traditions form identity","Representing culture respectfully"],
  ["Form","Perspective","Connection"],
  ["tradition","identity","celebration"],
  ["Research (culture)","Communication (multimodal)","Social (respect)"],
  ["Open-minded","Communicators","Caring"],
  ["I can research 1 culture deeply","I can compare to Peru","I can write 150w profile","I can represent culture respectfully at fair"],
  "Flyers (cultures, present perfect intro, comparatives)"
)
PYP_PROJECTS["G5_U5"] = make_pyp(
  "Who We Are",
  "Wellbeing is a balance of sleep, nutrition, exercise, and mental health.",
  ["Pillars of wellness","Mental health strategies","Designing our own plan"],
  ["Function","Responsibility","Reflection"],
  ["health","balance","self-care"],
  ["Self-management (health plan)","Thinking (rationale)","Social (peer strategies)"],
  ["Balanced","Reflective","Caring"],
  ["I can explain 4 wellness pillars","I can design a 7-day plan","I can use modals (should/must/might)","I can write 150w rationale"],
  "Flyers (health, might/may/should, sensory verbs)"
)
PYP_PROJECTS["G5_U6"] = make_pyp(
  "How We Express Ourselves",
  "Stories let us explore human experience and share emotions.",
  ["Story structure (beginning-middle-end)","Character and setting","Performance as storytelling"],
  ["Form","Perspective","Reflection"],
  ["narrative","performance","emotion"],
  ["Communication (writing + acting)","Self-management (rehearsal)","Social (collaboration)"],
  ["Risk-takers","Communicators","Reflective"],
  ["I can write a 150w story","I can adapt to a stage script","I can perform in a group","I can reflect on my performance"],
  "Flyers (narrative, past continuous, tag questions, connectors)"
)

# --------- MYP SECONDARY (G6-G10) ---------
# Schema: Global context, Statement of inquiry, Key concept + Related, Inquiry questions, ATL, Assessment criteria

MYP_PROJECTS = {
"G6_U1": {
  "framework":"MYP", "age_range":"10-11", "year":1,
  "global_context":"Identities and relationships",
  "statement_of_inquiry":"Relationships shape who we become and how we understand our role in communities.",
  "key_concept":"Connection",
  "related_concepts":["Identity","Context"],
  "inquiry_questions":{
    "factual":"Who are the key people in my life and what roles do they play?",
    "conceptual":"How do relationships shape our identity?",
    "debatable":"Is identity determined more by relationships or by individual choice?"
  },
  "atl_skills":["Communication (A1: give and receive feedback)","Social (C1: collaboration)","Self-management (D1: organization)"],
  "learner_profile":["Reflective","Communicators","Caring"],
  "assessment_criteria":{
    "A":"Listening: identify main ideas in conversations about relationships",
    "B":"Reading: comprehend texts about people and roles",
    "C":"Speaking: present a relationship map with justification (2-min)",
    "D":"Writing: produce 140w profile + KET email (25w)"
  },
  "success_criteria":["Map 8+ key relationships with clear roles","Use present perfect (ever/never) correctly","Write KET-format email with 3 prompts","Present orally for 2 minutes"],
  "cambridge_link":"KET Writing Parts 6-7 · Speaking collaborative task"
},
"G6_U2": {
  "framework":"MYP", "age_range":"10-11", "year":1,
  "global_context":"Orientation in space and time",
  "statement_of_inquiry":"Places carry histories and meaning for the communities that inhabit them.",
  "key_concept":"Perspective",
  "related_concepts":["Culture","Context"],
  "inquiry_questions":{
    "factual":"What places make up my neighbourhood?",
    "conceptual":"How do places hold meaning for people?",
    "debatable":"Should neighbourhoods change or preserve their character?"
  },
  "atl_skills":["Research (D3: information literacy)","Communication (A1, A2)","Thinking (C1: critical)"],
  "learner_profile":["Knowledgeable","Communicators","Open-minded"],
  "assessment_criteria":{
    "A":"Listening: understand interviews about local places",
    "B":"Reading: interpret signs, notices, short articles",
    "C":"Speaking: narrate a virtual tour (video voiceover)",
    "D":"Writing: email (25w) + video script"
  },
  "success_criteria":["Plan a 6-scene storyboard","Film and edit 3-min tour video","Use present perfect (just/already/yet)","Produce KET email"],
  "cambridge_link":"KET Reading/Writing · Listening"
},
"G6_U3": {
  "framework":"MYP", "age_range":"10-11", "year":1,
  "global_context":"Orientation in space and time",
  "statement_of_inquiry":"Travel planning balances geography, budget, and cultural curiosity.",
  "key_concept":"Systems",
  "related_concepts":["Purpose","Audience"],
  "inquiry_questions":{
    "factual":"How do we plan a trip itinerary?",
    "conceptual":"How do budget constraints shape travel decisions?",
    "debatable":"Is cultural immersion more valuable than tourism?"
  },
  "atl_skills":["Research (D1: organization)","Thinking (C3: transfer)","Communication (A1)"],
  "learner_profile":["Open-minded","Risk-takers","Knowledgeable"],
  "assessment_criteria":{
    "A":"Listening: travel announcements, timetables",
    "B":"Reading: travel brochures, itineraries",
    "C":"Speaking: pitch my itinerary (2-min)",
    "D":"Writing: blog post 140w + KET story 35w"
  },
  "success_criteria":["Design a 7-day itinerary with budget","Use present perfect (for/since) + 1st conditional","Write 140w blog","Produce KET story 35w"],
  "cambridge_link":"KET Writing (email + story) · Speaking"
},
"G6_U4": {
  "framework":"MYP", "age_range":"10-11", "year":1,
  "global_context":"Fairness and development",
  "statement_of_inquiry":"Services connect people, and polite communication builds trust.",
  "key_concept":"Communication",
  "related_concepts":["Purpose","Context"],
  "inquiry_questions":{
    "factual":"What services exist in our community?",
    "conceptual":"How does politeness enable trust in transactions?",
    "debatable":"Can good service exist without real care?"
  },
  "atl_skills":["Communication (A1, A2)","Social (C1)","Self-management (D2)"],
  "learner_profile":["Communicators","Caring","Principled"],
  "assessment_criteria":{
    "A":"Listening: customer service exchanges",
    "B":"Reading: service signs, menus, forms",
    "C":"Speaking: perform a scripted role-play",
    "D":"Writing: 140w service-review report"
  },
  "success_criteria":["Write a 4-turn role-play dialogue","Use full modals (can/could/may/might) for politeness","Perform with appropriate register","Report observations (140w)"],
  "cambridge_link":"KET Speaking collaborative · Listening Part 3"
},
"G6_U5": {
  "framework":"MYP", "age_range":"10-11", "year":1,
  "global_context":"Identities and relationships",
  "statement_of_inquiry":"Knowledge of body systems empowers healthy choices.",
  "key_concept":"Systems",
  "related_concepts":["Function","Evidence"],
  "inquiry_questions":{
    "factual":"How do body systems work?",
    "conceptual":"How do systems interact to keep us healthy?",
    "debatable":"Is exercise the most important factor for wellness?"
  },
  "atl_skills":["Research (D3, D4)","Communication (A1)","Thinking (C2: creative)"],
  "learner_profile":["Knowledgeable","Balanced","Communicators"],
  "assessment_criteria":{
    "A":"Listening: health-related talks",
    "B":"Reading: body system texts, diagrams",
    "C":"Speaking: 5-min presentation of 1 system",
    "D":"Writing: 140w science-style article"
  },
  "success_criteria":["Research 1 body system in depth","Use passive voice (pres/past simple)","Design an informative slide deck","Present orally for 5 minutes"],
  "cambridge_link":"KET Reading longer articles · Writing informative"
},
"G6_U6": {
  "framework":"MYP", "age_range":"10-11", "year":1,
  "global_context":"Personal and cultural expression",
  "statement_of_inquiry":"Audio storytelling creates connection with audiences beyond our classroom.",
  "key_concept":"Communication",
  "related_concepts":["Purpose","Audience","Creativity"],
  "inquiry_questions":{
    "factual":"What is a podcast?",
    "conceptual":"How does audio shape storytelling differently from video?",
    "debatable":"Do we need formal training to become content creators?"
  },
  "atl_skills":["Communication (A3: informed)","Self-management (D2: states of mind)","Thinking (C2: creative)"],
  "learner_profile":["Risk-takers","Communicators","Reflective"],
  "assessment_criteria":{
    "A":"Listening: kid podcasts, key details",
    "B":"Reading: podcast scripts",
    "C":"Speaking: record 3-min podcast with clear delivery",
    "D":"Writing: podcast script + KET story 35w"
  },
  "success_criteria":["Script a 3-min engaging episode","Interview a guest (audio)","Edit with basic tools","Produce KET 35w story"],
  "cambridge_link":"KET Speaking long turn · Writing story"
},

"G7_U1": {
  "framework":"MYP", "age_range":"11-12", "year":2,
  "global_context":"Personal and cultural expression",
  "statement_of_inquiry":"Cultures express identity through music, language, and history — and understanding them broadens our perspective.",
  "key_concept":"Culture",
  "related_concepts":["Identity","Context"],
  "inquiry_questions":{
    "factual":"What cultural elements define a country?",
    "conceptual":"How does culture shape individual identity?",
    "debatable":"Can a culture be fully understood by outsiders?"
  },
  "atl_skills":["Research (D3, D4)","Communication (A1, A2)","Social (C2: intercultural)"],
  "learner_profile":["Open-minded","Knowledgeable","Communicators"],
  "assessment_criteria":{
    "A":"Listening: cultural documentaries (B1 level)",
    "B":"Reading: articles about traditions, history",
    "C":"Speaking: 5-min cultural presentation with Q&A",
    "D":"Writing: 200w country profile"
  },
  "success_criteria":["Research from 3+ reliable sources","Use past perfect in narrative","Deliver 5-min presentation","Engage with Q&A"],
  "cambridge_link":"KET+/PET bridge (extended reading, longer listening)"
},
"G7_U2": {
  "framework":"MYP", "age_range":"11-12", "year":2,
  "global_context":"Identities and relationships",
  "statement_of_inquiry":"Effective study strategies are shaped by how we learn, not by rules others impose.",
  "key_concept":"Change",
  "related_concepts":["Purpose","Audience"],
  "inquiry_questions":{
    "factual":"What study techniques exist?",
    "conceptual":"How does metacognition improve learning?",
    "debatable":"Are there universal study habits that work for everyone?"
  },
  "atl_skills":["Self-management (D1, D2, D3)","Communication (A1)","Thinking (C3)"],
  "learner_profile":["Reflective","Risk-takers","Communicators"],
  "assessment_criteria":{
    "A":"Listening: study advice podcasts",
    "B":"Reading: educational psych articles (adapted)",
    "C":"Speaking: 3-min video tutorial",
    "D":"Writing: 180w how-to guide"
  },
  "success_criteria":["Survey peers on study habits","Use 2nd conditional (if I studied more, I would…)","Create a 3-min tutorial video","Write 180w guide"],
  "cambridge_link":"PET bridge (discussing preferences, conditionals)"
},
"G7_U3": {
  "framework":"MYP", "age_range":"11-12", "year":2,
  "global_context":"Globalization and sustainability",
  "statement_of_inquiry":"Budget travel is a lens through which we balance exploration with economic reality.",
  "key_concept":"Systems",
  "related_concepts":["Purpose","Resources"],
  "inquiry_questions":{
    "factual":"How much does travel cost?",
    "conceptual":"How do financial constraints shape travel choices?",
    "debatable":"Is ethical tourism possible for all budgets?"
  },
  "atl_skills":["Research (D3)","Thinking (C3: transfer)","Communication (A2: literacy)"],
  "learner_profile":["Open-minded","Balanced","Risk-takers"],
  "assessment_criteria":{
    "A":"Listening: travel vlogs, interviews",
    "B":"Reading: travel blogs and guides",
    "C":"Speaking: oral itinerary pitch (3-min)",
    "D":"Writing: 220w blog post"
  },
  "success_criteria":["Plan a real trip within budget","Use reported speech + 2nd conditional","Write casual blog voice (220w)","Calculate currency conversions"],
  "cambridge_link":"PET bridge (blog writing, reported speech)"
},
"G7_U4": {
  "framework":"MYP", "age_range":"11-12", "year":2,
  "global_context":"Fairness and development",
  "statement_of_inquiry":"Digital citizenship protects ourselves and others in online spaces.",
  "key_concept":"Ethics",
  "related_concepts":["Purpose","Audience"],
  "inquiry_questions":{
    "factual":"What is digital citizenship?",
    "conceptual":"How do our online actions affect others?",
    "debatable":"Should tech platforms be responsible for user behaviour?"
  },
  "atl_skills":["Communication (A3)","Social (C1, C2)","Thinking (C1: critical)"],
  "learner_profile":["Principled","Caring","Communicators"],
  "assessment_criteria":{
    "A":"Listening: cyber-safety resources",
    "B":"Reading: articles on online ethics",
    "C":"Speaking: present campaign video (60s)",
    "D":"Writing: 240w script with relative clauses"
  },
  "success_criteria":["Research a specific issue","Use relative clauses (def + non-def)","Create 60-sec impact video","Measure engagement"],
  "cambridge_link":"PET bridge (relative clauses, formal/informal register)"
},
"G7_U5": {
  "framework":"MYP", "age_range":"11-12", "year":2,
  "global_context":"Orientation in space and time",
  "statement_of_inquiry":"Career paths reveal the diverse ways humans contribute to society.",
  "key_concept":"Perspective",
  "related_concepts":["Identity","Context"],
  "inquiry_questions":{
    "factual":"What careers exist in our community?",
    "conceptual":"How does work shape identity and purpose?",
    "debatable":"Is it better to follow passion or pragmatism in career choice?"
  },
  "atl_skills":["Communication (A1, A2)","Research (D4)","Social (C2)"],
  "learner_profile":["Inquirers","Communicators","Open-minded"],
  "assessment_criteria":{
    "A":"Listening: interview audio",
    "B":"Reading: job descriptions, career articles",
    "C":"Speaking: conduct + present interview (3-min)",
    "D":"Writing: 200w interview summary"
  },
  "success_criteria":["Draft 10 thoughtful questions","Conduct professional interview","Use modal passive + causative have","Summarize in 200w"],
  "cambridge_link":"PET bridge (career vocabulary, formal interview register)"
},
"G7_U6": {
  "framework":"MYP", "age_range":"11-12", "year":2,
  "global_context":"Fairness and development",
  "statement_of_inquiry":"News media shapes public understanding and requires careful, balanced storytelling.",
  "key_concept":"Communication",
  "related_concepts":["Audience","Purpose","Context"],
  "inquiry_questions":{
    "factual":"What makes a news story?",
    "conceptual":"How do we balance information vs opinion?",
    "debatable":"Can news ever be objective?"
  },
  "atl_skills":["Research (D3, D4)","Communication (A3: source evaluation)","Thinking (C1: critical)"],
  "learner_profile":["Principled","Communicators","Balanced"],
  "assessment_criteria":{
    "A":"Listening: news broadcasts",
    "B":"Reading: news articles, editorials",
    "C":"Speaking: record podcast (5-min)",
    "D":"Writing: 250w script"
  },
  "success_criteria":["Verify 3 stories from multiple sources","Use connectors (however, although, despite)","Produce 5-min news podcast","Write journalistic script"],
  "cambridge_link":"PET bridge (connectors, news register)"
}
}

# Continue with G8-G11... I'll use the make_myp helper for efficiency
def make_myp(year, gc, soi, kc, rc, iq, atl, lp, ac, sc, link):
    return {"framework":"MYP","age_range":f"{year+10}-{year+11}","year":year,
            "global_context":gc,"statement_of_inquiry":soi,
            "key_concept":kc,"related_concepts":rc,
            "inquiry_questions":iq,"atl_skills":atl,"learner_profile":lp,
            "assessment_criteria":ac,"success_criteria":sc,"cambridge_link":link}

# G8 PET year
MYP_PROJECTS["G8_U1"] = make_myp(3, "Identities and relationships",
  "Personality frameworks help us understand ourselves but don't determine who we become.",
  "Identity", ["Perspective","Context"],
  {"factual":"What are major personality theories?","conceptual":"How do frameworks shape self-understanding?","debatable":"Are personality tests reliable predictors?"},
  ["Research (D3)","Self-management (D2)","Thinking (C1)"],
  ["Reflective","Open-minded","Balanced"],
  {"A":"Listening: psychology talks","B":"Reading: personality articles","C":"Speaking: self-analysis presentation","D":"Writing: 220w reflection + PET email (100w)"},
  ["Take multiple personality assessments","Use word formation (confident→confidence)","Write 220w + PET email","Present self-analysis"],
  "PET (word formation, all tenses)")

MYP_PROJECTS["G8_U2"] = make_myp(3, "Personal and cultural expression",
  "Film is a powerful medium that shapes narrative, emotion, and cultural memory.",
  "Creativity", ["Perspective","Audience","Purpose"],
  {"factual":"What are film genres?","conceptual":"How do films construct meaning?","debatable":"Is film a reflection of culture or a shaper of it?"},
  ["Communication (A1, A2, A3)","Self-management (D1)","Social (C1)"],
  ["Risk-takers","Communicators","Creators"],
  {"A":"Listening: film dialogue","B":"Reading: film scripts and reviews","C":"Speaking: film production discussion","D":"Writing: 240w script"},
  ["Write 240w script with dialogue","Use reported speech (Q + commands)","Film + edit 3-min short","Premiere with reflection"],
  "PET (reported speech, narrative genres)")

MYP_PROJECTS["G8_U3"] = make_myp(3, "Identities and relationships",
  "Health campaigns use evidence and empathy to change behaviours.",
  "Change", ["Systems","Evidence"],
  {"factual":"What are the main health issues in our school?","conceptual":"How does data drive health behaviour change?","debatable":"Is awareness enough to change behaviour?"},
  ["Research (D3, D4)","Communication (A2)","Thinking (C1)"],
  ["Balanced","Principled","Caring"],
  {"A":"Listening: health documentaries","B":"Reading: health articles + stats","C":"Speaking: campaign pitch","D":"Writing: 260w article + PET article (100w)"},
  ["Survey 30+ students","Design evidence-based campaign","Use conditionals 0-1-2","Write 260w article"],
  "PET (conditionals, formal article writing)")

MYP_PROJECTS["G8_U4"] = make_myp(3, "Fairness and development",
  "Human rights require protection through critical discussion and civic engagement.",
  "Ethics", ["Systems","Perspective"],
  {"factual":"What are the UN human rights articles?","conceptual":"How are rights protected or violated?","debatable":"Can universal rights apply across all cultures?"},
  ["Communication (A1, A3)","Social (C1)","Thinking (C1, C3)"],
  ["Principled","Open-minded","Communicators"],
  {"A":"Listening: rights debates","B":"Reading: UN declarations, case studies","C":"Speaking: debate participation (formal)","D":"Writing: 260w position paper"},
  ["Argue position with 3+ evidence points","Use passive all simple tenses","Deliver debate opening + rebuttal","Write formal 260w paper"],
  "PET (formal register, passive, reported)")

MYP_PROJECTS["G8_U5"] = make_myp(3, "Globalization and sustainability",
  "Individual choices aggregate into global environmental impact.",
  "Systems", ["Change","Evidence"],
  {"factual":"What is a carbon footprint?","conceptual":"How do individual choices connect to global systems?","debatable":"Can personal action alone address climate change?"},
  ["Research (D3)","Thinking (C1)","Communication (A2)"],
  ["Balanced","Principled","Reflective"],
  {"A":"Listening: environment podcasts","B":"Reading: climate reports","C":"Speaking: present calculator findings","D":"Writing: 260w environmental report"},
  ["Build spreadsheet calculator","Collect household data (5 days)","Analyze patterns","Write 260w report"],
  "PET (environment vocab, data reporting)")

MYP_PROJECTS["G8_U6"] = make_myp(3, "Personal and cultural expression",
  "Literary genres shape how stories reach and affect audiences.",
  "Form", ["Audience","Creativity"],
  {"factual":"What defines sci-fi, romance, thriller?","conceptual":"How do genre conventions shape meaning?","debatable":"Do genres limit or enable creative expression?"},
  ["Communication (A3)","Thinking (C2)","Social (C1)"],
  ["Reflective","Communicators","Open-minded"],
  {"A":"Listening: genre audiobook excerpts","B":"Reading: genre samples","C":"Speaking: adaptation explanation","D":"Writing: 250w adaptation + PET story (100w)"},
  ["Adapt a story to a new genre (250w)","Analyze changes critically (150w)","Compare original vs adapted","Produce PET story"],
  "PET (narrative genres, story writing)")

# G9 FCE year
MYP_PROJECTS["G9_U1"] = make_myp(4, "Identities and relationships",
  "Identity is a dynamic intersection of cultural, social, and personal narratives.",
  "Identity", ["Culture","Perspective"],
  {"factual":"What factors shape identity?","conceptual":"How are identities negotiated within cultures?","debatable":"Is identity primarily individual or collective?"},
  ["Communication (A1, A2, A3)","Research (D3)","Thinking (C1)"],
  ["Open-minded","Reflective","Communicators"],
  {"A":"Listening: identity documentaries","B":"Reading: essays on identity","C":"Speaking: doc premiere + Q&A","D":"Writing: 170w FCE essay"},
  ["Film 3 interviews","Edit 5-min documentary","Use conditional 3 + mixed","Write FCE 170w essay"],
  "FCE Writing Part 1 (essay) · Listening Parts 1-4")

MYP_PROJECTS["G9_U2"] = make_myp(4, "Scientific and technical innovation",
  "Scientific inquiry reveals patterns through systematic evidence-based methods.",
  "Change", ["Systems","Evidence"],
  {"factual":"What is the scientific method?","conceptual":"How does systematic inquiry reveal patterns?","debatable":"Can science explain everything?"},
  ["Research (D4: media literacy)","Thinking (C1: critical)","Communication (A2)"],
  ["Inquirers","Thinkers","Knowledgeable"],
  {"A":"Listening: science podcasts","B":"Reading: scientific papers (adapted)","C":"Speaking: fair presentation + Q&A","D":"Writing: 170w FCE report"},
  ["Formulate testable question","Design + execute valid method","Analyze + visualize data","Write FCE report (170w)"],
  "FCE Writing (report) · Use of English · Speaking long turn")

MYP_PROJECTS["G9_U3"] = make_myp(4, "Fairness and development",
  "Global challenges require coordinated international responses informed by diverse perspectives.",
  "Systems", ["Context","Perspective"],
  {"factual":"How does the UN work?","conceptual":"How do nations negotiate shared challenges?","debatable":"Is the UN effective at addressing global problems?"},
  ["Communication (A1, A3)","Social (C1, C2)","Thinking (C3)"],
  ["Principled","Communicators","Open-minded"],
  {"A":"Listening: UN speeches","B":"Reading: position papers, resolutions","C":"Speaking: opening speech + debate","D":"Writing: 180w position paper"},
  ["Write MUN-format position paper","Deliver 90-sec opening","Negotiate amendments","Represent country perspective"],
  "FCE Speaking (interview + discussion)")

MYP_PROJECTS["G9_U4"] = make_myp(4, "Personal and cultural expression",
  "Cultures shape and are shaped by the languages, traditions, and histories they share.",
  "Culture", ["Perspective","Change"],
  {"factual":"What distinguishes cultures?","conceptual":"How do cultures influence each other?","debatable":"Does globalization enrich or erode cultures?"},
  ["Research (D3, D4)","Communication (A1, A2)","Social (C2)"],
  ["Open-minded","Knowledgeable","Communicators"],
  {"A":"Listening: cultural programs","B":"Reading: comparative essays","C":"Speaking: bilingual oral (5-min)","D":"Writing: 180w FCE essay"},
  ["Compare Peru with another culture","Use advanced relatives (with prepositions)","Write comparative FCE essay","Present respectfully"],
  "FCE Writing (comparative essay)")

MYP_PROJECTS["G9_U5"] = make_myp(4, "Scientific and technical innovation",
  "AI raises ethical questions about our future relationship with technology.",
  "Ethics", ["Systems","Change"],
  {"factual":"What can AI do today?","conceptual":"How do AI tools challenge existing norms?","debatable":"Should AI development be regulated globally?"},
  ["Research (D4)","Thinking (C1, C3)","Communication (A3)"],
  ["Principled","Thinkers","Risk-takers"],
  {"A":"Listening: AI panels","B":"Reading: AI ethics articles","C":"Speaking: panel discussion","D":"Writing: 180w FCE prediction essay"},
  ["Research an AI ethical issue","Use wish / if only","Prepare panel statement","Write 180w prediction essay"],
  "FCE Writing (opinion essay) · Speaking collaborative")

MYP_PROJECTS["G9_U6"] = make_myp(4, "Globalization and sustainability",
  "Global problems demand creative, systems-level solutions shared widely.",
  "Systems", ["Purpose","Change"],
  {"factual":"What are pressing global problems?","conceptual":"How do problems connect across systems?","debatable":"Whose responsibility is solving global issues?"},
  ["Communication (A1, A2, A3)","Research (D3)","Thinking (C2)"],
  ["Communicators","Principled","Risk-takers"],
  {"A":"Listening: TED talks","B":"Reading: reviews of solutions","C":"Speaking: deliver TED-Ed talk","D":"Writing: 150w FCE review"},
  ["Script TED-Ed problem-solution","Use connectors (whereas/nevertheless)","Edit 3-min video","Write 150w FCE review"],
  "FCE Writing (review) · Speaking long turn")

# G10 FCE consolidation / CAE bridge
MYP_PROJECTS["G10_U1"] = make_myp(5, "Identities and relationships",
  "Personal growth is intentional — we become through reflection, goal-setting, and action.",
  "Change", ["Identity","Purpose"],
  {"factual":"What are my strengths, values, goals?","conceptual":"How does metacognition drive growth?","debatable":"Can we engineer our personal growth?"},
  ["Self-management (D1, D2)","Communication (A1)","Thinking (C1)"],
  ["Reflective","Risk-takers","Balanced"],
  {"A":"Listening: self-development talks","B":"Reading: memoirs, essays","C":"Speaking: portfolio walk","D":"Writing: 350w reflection"},
  ["Audit self honestly","Design SMART 1-yr + 5-yr goals","Use mixed conditionals + subjunctive","Write 350w reflection"],
  "FCE / CAE bridge (personal essay)")

MYP_PROJECTS["G10_U2"] = make_myp(5, "Fairness and development",
  "Media literacy is essential for informed citizens in a world of abundant misinformation.",
  "Communication", ["Evidence","Ethics"],
  {"factual":"What is misinformation?","conceptual":"How does media shape public understanding?","debatable":"Should platforms be required to fact-check?"},
  ["Research (D4: critical)","Thinking (C1: critical)","Communication (A3)"],
  ["Principled","Thinkers","Communicators"],
  {"A":"Listening: media-lit podcasts","B":"Reading: fact-checking articles","C":"Speaking: audit presentation","D":"Writing: 400w audit report"},
  ["Collect 5 questionable claims","Fact-check using primary sources","Use subjunctive + reported speech","Write 400w academic audit"],
  "CAE bridge (academic register, critical analysis)")

MYP_PROJECTS["G10_U3"] = make_myp(5, "Scientific and technical innovation",
  "Research drives progress when questions are well-defined and methods rigorous.",
  "Inquiry", ["Systems","Evidence"],
  {"factual":"What is a research proposal?","conceptual":"How do we design rigorous inquiry?","debatable":"Is rigor more valuable than innovation?"},
  ["Research (D3, D4)","Thinking (C3)","Communication (A2)"],
  ["Inquirers","Thinkers","Knowledgeable"],
  {"A":"Listening: academic seminars","B":"Reading: research papers","C":"Speaking: defend proposal (10-min)","D":"Writing: 400w proposal"},
  ["Define researchable question","Review 5+ academic sources","Use complex relatives + participle clauses","Write 400w proposal"],
  "CAE bridge (IB-style research)")

MYP_PROJECTS["G10_U4"] = make_myp(5, "Fairness and development",
  "Social movements shape history by mobilizing collective action around shared values.",
  "Change", ["Systems","Perspective"],
  {"factual":"What is a social movement?","conceptual":"How do movements achieve change?","debatable":"Are movements more effective than institutions?"},
  ["Research (D3, D4)","Communication (A2)","Thinking (C1)"],
  ["Principled","Open-minded","Communicators"],
  {"A":"Listening: historical speeches","B":"Reading: movement histories","C":"Speaking: 10-min presentation","D":"Writing: 400w analytical essay"},
  ["Analyze a movement's tactics + impact","Use inversion + cleft sentences","Write 400w essay with clear thesis","Present with slides"],
  "CAE bridge (analytical essay, advanced syntax)")

MYP_PROJECTS["G10_U5"] = make_myp(5, "Globalization and sustainability",
  "Businesses can create value and contribute to sustainability through design choices.",
  "Systems", ["Purpose","Change"],
  {"factual":"What is sustainable business?","conceptual":"How do businesses balance profit and planet?","debatable":"Can capitalism be sustainable?"},
  ["Thinking (C2: creative)","Research (D3)","Communication (A1)"],
  ["Risk-takers","Balanced","Principled"],
  {"A":"Listening: entrepreneur pitches","B":"Reading: business plans","C":"Speaking: pitch in Shark-Tank format","D":"Writing: 400w business plan"},
  ["Design a triple-bottom-line business","Use causative + phrasal verbs academic","Write 400w plan","Deliver 5-min pitch + Q&A"],
  "CAE bridge (persuasive writing, professional English)")

MYP_PROJECTS["G10_U6"] = make_myp(5, "Identities and relationships",
  "Professional identity is crafted through how we present our skills and story.",
  "Communication", ["Identity","Audience"],
  {"factual":"What goes into a CV and cover letter?","conceptual":"How do professionals signal value?","debatable":"Is authenticity possible in professional contexts?"},
  ["Communication (A1, A2)","Self-management (D1)","Social (C2)"],
  ["Communicators","Reflective","Risk-takers"],
  {"A":"Listening: mock interviews","B":"Reading: professional bios","C":"Speaking: mock interview + review","D":"Writing: CV + 350w cover letter"},
  ["Produce industry-standard CV","Write 350w cover letter","Build LinkedIn-style profile","Perform in mock interview"],
  "CAE bridge (formal register, professional communication)")

# G11 CAE / DP bridge
def make_dp(gc, eu, kc, rc, tok, atl, lp, sc, link):
    return {"framework":"IB DP bridge","age_range":"15-16","year":6,
            "global_context":gc,"essential_understanding":eu,
            "key_concept":kc,"related_concepts":rc,"tok_links":tok,
            "atl_skills":atl,"learner_profile":lp,"success_criteria":sc,
            "cambridge_link":link}

DP_PROJECTS = {}
DP_PROJECTS["G11_U1"] = make_dp(
  "Personal and cultural expression",
  "Rhetoric shapes public discourse and reveals how power operates through language.",
  "Communication", ["Perspective","Audience","Purpose"],
  ["How does rhetoric shape what we know?","Are emotional and logical appeals equally valid?","Can rhetoric exist without manipulation?"],
  ["Communication (critical analysis)","Thinking (C1)","Research (D4)"],
  ["Communicators","Principled","Thinkers"],
  ["Analyze a historic speech (ethos/pathos/logos)","Use inversion fluently","Write 260w CAE essay","Deliver 10-min masterclass"],
  "CAE Writing Part 1 (essay) · TOK: WOKs (language)")

DP_PROJECTS["G11_U2"] = make_dp(
  "Personal and cultural expression",
  "Literary criticism illuminates texts through frameworks that reveal implicit meaning.",
  "Perspective", ["Culture","Context"],
  ["How do theoretical frameworks shape interpretation?","Can literature have universal meaning?","Is the author's intent relevant to interpretation?"],
  ["Research (D3)","Thinking (C1, C2)","Communication (A3)"],
  ["Inquirers","Open-minded","Thinkers"],
  ["Apply one lit theory to a novel","Use cleft sentences + nominalisation","Write CAE 260w review","Present seminar-style"],
  "CAE Writing (review) · TOK: AOKs (arts)")

DP_PROJECTS["G11_U3"] = make_dp(
  "Scientific and technical innovation",
  "Academic research is a structured conversation that extends human understanding.",
  "Inquiry", ["Systems","Evidence"],
  ["How do we know what we know?","What counts as evidence?","Can research be truly objective?"],
  ["Research (D3, D4)","Thinking (C1)","Communication (A2)"],
  ["Inquirers","Thinkers","Knowledgeable"],
  ["Craft focused RQ","Write 10-source lit review","Use impersonal passive + nominalisation","Full 2500w paper + CAE 260w report"],
  "CAE Writing (report) · TOK: knowledge production · EE preparation")

DP_PROJECTS["G11_U4"] = make_dp(
  "Globalization and sustainability",
  "Economic policy choices shape inequality, opportunity, and wellbeing at scale.",
  "Systems", ["Change","Responsibility"],
  ["How are economic decisions made?","Who benefits and who bears costs?","Can economic growth be sustainable?"],
  ["Research (D3)","Thinking (C1, C3)","Communication (A2)"],
  ["Principled","Thinkers","Communicators"],
  ["Propose a specific policy","Use inversion + fronting","Write CAE 260w proposal","Deliver ministerial-style briefing"],
  "CAE Writing (proposal) · TOK: ethics, economics")

DP_PROJECTS["G11_U5"] = make_dp(
  "Fairness and development",
  "Policy briefs translate research into decision-ready recommendations for change.",
  "Communication", ["Purpose","Audience"],
  ["How do we translate evidence into policy?","Whose voices are heard in policy?","Is there a universal 'good policy'?"],
  ["Research (D3)","Communication (A2)","Thinking (C1)"],
  ["Principled","Communicators","Reflective"],
  ["Research a Peruvian issue with data","Use hedging + ellipsis advanced","Write 260w CAE proposal","Present to mock audience"],
  "CAE Writing (proposal) · TOK: ethics")

DP_PROJECTS["G11_U6"] = make_dp(
  "Fairness and development",
  "Ethical reasoning frameworks help us navigate moral dilemmas thoughtfully.",
  "Ethics", ["Perspective","Context"],
  ["What ethical frameworks exist?","How do we decide between competing values?","Are ethics universal or culturally bound?"],
  ["Thinking (C1)","Communication (A1, A3)","Social (C1)"],
  ["Principled","Reflective","Thinkers"],
  ["Apply one ethical framework","Use impersonal passive + complex noun phrases","Write CAE 260w essay (timed)","Deliver symposium paper"],
  "CAE Writing (essay, timed) · TOK: ethics (core)")

# ============= COMBINE =============
enhanced = {}
for k, v in PYP_PROJECTS.items(): enhanced[k] = v
for k, v in MYP_PROJECTS.items(): enhanced[k] = v
for k, v in DP_PROJECTS.items(): enhanced[k] = v

print(f'Total enhanced projects: {len(enhanced)}')
missing = [k for k in plans if k not in enhanced]
if missing: print(f'⚠ Missing framework for: {missing}')

# Merge with plans: add IB metadata to each plan entry
merged = {}
for key, plan in plans.items():
    merged[key] = dict(plan)
    if key in enhanced:
        merged[key]['ib'] = enhanced[key]

with open('clil_plans.json', 'w', encoding='utf-8') as f:
    json.dump(merged, f, ensure_ascii=False, indent=None, separators=(',', ':'))

print(f'✓ Merged IB schemas into clil_plans.json')
print(f'  Frameworks: PYP={len([k for k,v in enhanced.items() if v["framework"]=="PYP"])}, MYP={len([k for k,v in enhanced.items() if v["framework"]=="MYP"])}, DP={len([k for k,v in enhanced.items() if v["framework"]=="IB DP bridge"])}')
