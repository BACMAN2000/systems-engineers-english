// ===== BUSINESS ENGLISH MATERIALS =====
// Grammar explanations + Vocabulary presentations
// Indexed by topic name (exact match with BE_CURRICULUM[level].grammar[i] / .vocabulary[i])

const BE_GRAMMAR_DB = {
  // ===== A1 =====
  "Present simple (be/have/do)":{
    rule:"Use the present simple to talk about facts, habits, and routines in the workplace.",
    structure:"I/You/We/They + base verb  |  He/She/It + verb+s  |  be: am/is/are  |  have: have/has  |  do: do/does",
    examples:[
      {en:"I work for Cohasset International.",es:"Trabajo para Cohasset International."},
      {en:"She has two meetings today.",es:"Ella tiene dos reuniones hoy."},
      {en:"We don't work on Sundays.",es:"No trabajamos los domingos."},
      {en:"Does he speak English?",es:"¿Él habla inglés?"}
    ],
    notes:["Add -s/-es with he/she/it.","Use don't/doesn't for negatives.","Use do/does for questions."],
    mistakes:[
      {wrong:"She work in finance.",right:"She works in finance.",why:"3rd person singular needs -s"},
      {wrong:"I am work here.",right:"I work here.",why:"Don't use be + base verb for habits"}
    ]
  },
  "There is/are":{
    rule:"Use 'there is' for singular and 'there are' for plural to say something exists.",
    structure:"There is + singular noun  |  There are + plural noun  |  There isn't / There aren't",
    examples:[
      {en:"There is a meeting at 3 PM.",es:"Hay una reunión a las 3 PM."},
      {en:"There are five people in the team.",es:"Hay cinco personas en el equipo."},
      {en:"Is there a problem?",es:"¿Hay un problema?"}
    ],
    notes:["Don't confuse 'there is' (existence) with 'it is' (description)."],
    mistakes:[{wrong:"It is a meeting at 3.",right:"There is a meeting at 3.",why:"'It is' describes; 'there is' announces existence"}]
  },
  "Can/can't":{
    rule:"Use 'can' to express ability, possibility, or polite requests.",
    structure:"Subject + can + base verb  |  can't = cannot",
    examples:[
      {en:"I can speak three languages.",es:"Puedo hablar tres idiomas."},
      {en:"Can you send me the report?",es:"¿Puedes enviarme el reporte?"},
      {en:"He can't attend the meeting.",es:"Él no puede asistir a la reunión."}
    ],
    notes:["'Can' is the same for all persons.","No -s on the main verb after 'can'."],
    mistakes:[{wrong:"He can to drive.",right:"He can drive.",why:"No 'to' after 'can'"}]
  },
  "Possessive 's":{
    rule:"Add 's to a noun to show possession or belonging.",
    structure:"noun + 's = singular possessor  |  plural noun ending in s + ' = plural possessor",
    examples:[
      {en:"Maria's laptop is new.",es:"La laptop de María es nueva."},
      {en:"The company's headquarters is in Lima.",es:"La sede de la empresa está en Lima."},
      {en:"The employees' parking lot is full.",es:"El estacionamiento de los empleados está lleno."}
    ],
    notes:["Use 's even if the name ends in s (James's car)."],
    mistakes:[{wrong:"The laptop of Maria",right:"Maria's laptop",why:"English prefers 's to 'of' for people"}]
  },
  "This/that/these/those":{
    rule:"Use demonstratives to indicate things near or far, singular or plural.",
    structure:"this/that + singular  |  these/those + plural  |  near = this/these, far = that/those",
    examples:[{en:"This is my office.",es:"Esta es mi oficina."},{en:"Those are our clients.",es:"Aquellos son nuestros clientes."}],
    notes:["Use 'this/these' in letters when introducing people."],
    mistakes:[{wrong:"This are my colleagues.",right:"These are my colleagues.",why:"Plural needs 'these'"}]
  },
  "Imperatives":{
    rule:"Use the base form of the verb to give instructions, orders, or invitations.",
    structure:"Base verb + object  |  Don't + base verb (negative)",
    examples:[{en:"Send the email now.",es:"Envía el email ahora."},{en:"Don't forget the deadline.",es:"No olvides la fecha límite."}],
    notes:["Add 'please' to be polite."],
    mistakes:[{wrong:"You send the email.",right:"Send the email.",why:"Drop 'you' in imperatives"}]
  },
  "Present continuous (intro)":{
    rule:"Use the present continuous for actions happening now or around now.",
    structure:"Subject + am/is/are + verb-ing",
    examples:[{en:"I am writing a report.",es:"Estoy escribiendo un reporte."},{en:"They are meeting the client.",es:"Están reuniéndose con el cliente."}],
    notes:["Don't use with stative verbs (know, like, want)."],
    mistakes:[{wrong:"I am knowing him.",right:"I know him.",why:"'Know' is stative"}]
  },
  "Prepositions of place/time":{
    rule:"Use in/on/at for places and times with different rules.",
    structure:"at = specific time/point  |  on = day/date/surface  |  in = month/year/inside",
    examples:[{en:"The meeting is at 3 PM on Monday in March.",es:"La reunión es a las 3 PM el lunes en marzo."}],
    notes:["at work, in the office, on the desk."],
    mistakes:[{wrong:"in Monday",right:"on Monday",why:"Days use 'on'"}]
  },
  "A/an/the basics":{
    rule:"Use 'a/an' for one general thing, 'the' for specific or known things.",
    structure:"a + consonant sound  |  an + vowel sound  |  the + specific noun",
    examples:[{en:"I have a meeting with the CEO.",es:"Tengo una reunión con el CEO."},{en:"She's an engineer at the London office.",es:"Es ingeniera en la oficina de Londres."}],
    notes:["No article with general plurals: 'Managers work hard.'"],
    mistakes:[{wrong:"I am engineer.",right:"I am an engineer.",why:"Jobs need a/an"}]
  },
  "Plural nouns":{
    rule:"Add -s or -es to make most nouns plural; some are irregular.",
    structure:"cat→cats, box→boxes, company→companies, man→men, child→children",
    examples:[{en:"Our companies have offices worldwide.",es:"Nuestras empresas tienen oficinas en todo el mundo."}],
    notes:["Some words are the same singular and plural: equipment, information, staff."],
    mistakes:[{wrong:"two informations",right:"two pieces of information",why:"'Information' is uncountable"}]
  },
  "Question words (who/what/where/when)":{
    rule:"Use WH-words to ask for information.",
    structure:"WH + auxiliary + subject + verb?",
    examples:[{en:"Where do you work?",es:"¿Dónde trabajas?"},{en:"When does the meeting start?",es:"¿Cuándo empieza la reunión?"}],
    notes:["Who can be subject (no auxiliary) or object (with auxiliary)."],
    mistakes:[{wrong:"Where you work?",right:"Where do you work?",why:"Need auxiliary 'do'"}]
  },
  "Like + -ing":{
    rule:"After 'like/love/enjoy/hate', use verb + -ing.",
    structure:"Subject + like/love/enjoy + verb-ing",
    examples:[{en:"I enjoy working with international teams.",es:"Disfruto trabajar con equipos internacionales."}],
    notes:["'Would like' + to + verb: I would like to meet."],
    mistakes:[{wrong:"I enjoy to work",right:"I enjoy working",why:"Enjoy takes -ing"}]
  },
  "Want + infinitive":{
    rule:"After 'want', use to + base verb.",
    structure:"Subject + want + to + base verb",
    examples:[{en:"I want to schedule a call.",es:"Quiero programar una llamada."}],
    notes:["'Want someone to do': I want you to review this."],
    mistakes:[{wrong:"I want meeting",right:"I want to meet",why:"Want needs 'to + verb'"}]
  },
  "Adverbs of frequency":{
    rule:"Use frequency adverbs before the main verb (but after 'be').",
    structure:"always, usually, often, sometimes, rarely, never",
    examples:[{en:"I always check my email in the morning.",es:"Siempre reviso mi email en la mañana."},{en:"He is never late.",es:"Él nunca llega tarde."}],
    notes:["Frequency adverbs go after 'be' but before other verbs."],
    mistakes:[{wrong:"I check always my email",right:"I always check my email",why:"Adverb goes before main verb"}]
  },
  "Countable/uncountable (some/any)":{
    rule:"Use 'some' in positive, 'any' in negative/questions.",
    structure:"some + plural/uncountable (positive)  |  any + plural/uncountable (negative/questions)",
    examples:[{en:"We have some good candidates.",es:"Tenemos algunos buenos candidatos."},{en:"Is there any information about this?",es:"¿Hay alguna información sobre esto?"}],
    notes:["'Some' in offers/requests: Would you like some coffee?"],
    mistakes:[{wrong:"We don't have some time",right:"We don't have any time",why:"Use 'any' in negatives"}]
  },
  // ===== A2 =====
  "Past simple (regular/irregular)":{
    rule:"Use the past simple for completed actions in the past.",
    structure:"regular: verb + -ed  |  irregular: go→went, have→had, be→was/were  |  negative: didn't + base verb",
    examples:[{en:"We launched the product last year.",es:"Lanzamos el producto el año pasado."},{en:"She went to the conference in Paris.",es:"Ella fue a la conferencia en París."},{en:"They didn't finish the report.",es:"No terminaron el reporte."}],
    notes:["Use time markers: yesterday, last week, in 2020, ago."],
    mistakes:[{wrong:"She didn't went",right:"She didn't go",why:"After did/didn't use base verb"}]
  },
  "Past continuous":{
    rule:"Use past continuous for actions in progress in the past.",
    structure:"was/were + verb-ing",
    examples:[{en:"I was preparing the presentation when he called.",es:"Estaba preparando la presentación cuando llamó."}],
    notes:["Often used with past simple: was -ing WHEN + past simple."],
    mistakes:[{wrong:"I was prepare",right:"I was preparing",why:"Need -ing form"}]
  },
  "Comparative & superlative":{
    rule:"Use comparatives to compare two things, superlatives for three or more.",
    structure:"short: -er/-est  |  long: more/most  |  irregular: good→better→best",
    examples:[{en:"Our Q4 results are better than Q3.",es:"Nuestros resultados del Q4 son mejores que el Q3."},{en:"This is the most profitable division.",es:"Esta es la división más rentable."}],
    notes:["'than' with comparatives, 'the' with superlatives."],
    mistakes:[{wrong:"more better",right:"better",why:"Don't combine more + -er"}]
  },
  "Going to (future plans)":{
    rule:"Use 'be going to' for planned future actions or predictions based on evidence.",
    structure:"am/is/are + going to + base verb",
    examples:[{en:"We are going to expand to Brazil next year.",es:"Vamos a expandirnos a Brasil el próximo año."}],
    notes:["For spontaneous decisions, use 'will'."],
    mistakes:[{wrong:"I going to call him",right:"I am going to call him",why:"Need 'be' verb"}]
  },
  "Will (predictions/offers)":{
    rule:"Use 'will' for predictions, offers, spontaneous decisions, and promises.",
    structure:"Subject + will + base verb  |  won't = will not",
    examples:[{en:"I'll send you the contract tomorrow.",es:"Te enviaré el contrato mañana."},{en:"The market won't recover quickly.",es:"El mercado no se recuperará rápido."}],
    notes:["No -s with will: he will (not 'he wills')."],
    mistakes:[{wrong:"He wills call you",right:"He will call you",why:"Will never takes -s"}]
  },
  "Present perfect (experience)":{
    rule:"Use present perfect for experiences, recent actions, or unfinished time periods.",
    structure:"have/has + past participle",
    examples:[{en:"I have worked in five countries.",es:"He trabajado en cinco países."},{en:"She has just finished the report.",es:"Acaba de terminar el reporte."}],
    notes:["Use 'ever/never/just/already/yet' with present perfect."],
    mistakes:[{wrong:"I have worked there yesterday",right:"I worked there yesterday",why:"Specific past time = past simple"}]
  },
  "Should/shouldn't (advice)":{
    rule:"Use 'should' to give advice or recommendations.",
    structure:"Subject + should + base verb",
    examples:[{en:"You should review the proposal before sending.",es:"Deberías revisar la propuesta antes de enviarla."}],
    notes:["'Ought to' and 'had better' have similar meanings."],
    mistakes:[{wrong:"You should to review",right:"You should review",why:"No 'to' after modals"}]
  },
  "Have to/don't have to":{
    rule:"'Have to' = necessity/obligation. 'Don't have to' = not necessary.",
    structure:"Subject + have to / has to + base verb",
    examples:[{en:"We have to submit the report by Friday.",es:"Tenemos que presentar el reporte para el viernes."},{en:"You don't have to come to the meeting.",es:"No tienes que venir a la reunión."}],
    notes:["'Must' is similar but more personal/formal."],
    mistakes:[{wrong:"He have to go",right:"He has to go",why:"3rd person needs 'has'"}]
  },
  "First conditional (if + present)":{
    rule:"Use first conditional for real, likely future situations.",
    structure:"If + present simple, will + base verb",
    examples:[{en:"If we cut costs, we will increase profit margins.",es:"Si reducimos costos, aumentaremos los márgenes de ganancia."}],
    notes:["'Unless' = if not: Unless sales improve, we'll lose money."],
    mistakes:[{wrong:"If we will cut costs",right:"If we cut costs",why:"No 'will' after 'if' in first conditional"}]
  },
  // ===== B1 =====
  "Present perfect vs past simple":{
    rule:"Present perfect = indefinite past or still relevant; Past simple = finished specific time.",
    structure:"PP: have/has + past part.  |  PS: verb + -ed (or irregular)",
    examples:[{en:"I have worked in finance for 10 years.",es:"He trabajado en finanzas por 10 años."},{en:"I worked at HSBC from 2015 to 2020.",es:"Trabajé en HSBC de 2015 a 2020."}],
    notes:["Time markers decide: 'since/for/ever' = PP; 'yesterday/ago' = PS."],
    mistakes:[{wrong:"I have worked there in 2019",right:"I worked there in 2019",why:"Finished time = past simple"}]
  },
  "Present perfect continuous":{
    rule:"Use for ongoing actions from past to now, emphasizing duration.",
    structure:"have/has been + verb-ing",
    examples:[{en:"We have been negotiating for three months.",es:"Hemos estado negociando por tres meses."}],
    notes:["Focus on activity, not completion."],
    mistakes:[{wrong:"I am working here since 2020",right:"I have been working here since 2020",why:"Need present perfect continuous"}]
  },
  "Used to / would":{
    rule:"'Used to' = past habits or states that no longer happen. 'Would' = repeated past actions (not states).",
    structure:"used to + base verb  |  would + base verb",
    examples:[{en:"We used to outsource our IT services.",es:"Solíamos tercerizar nuestros servicios de TI."}],
    notes:["'Would' can't describe past states (used to be, not 'would be')."],
    mistakes:[{wrong:"I would be a manager",right:"I used to be a manager",why:"'Would' doesn't work with states"}]
  },
  "First & second conditional":{
    rule:"1st = real future; 2nd = hypothetical present/future.",
    structure:"1st: if + present, will + base  |  2nd: if + past, would + base",
    examples:[{en:"If we hire more staff, we'll meet the deadline.",es:"Si contratamos más personal, cumpliremos el plazo."},{en:"If I were CEO, I would restructure the company.",es:"Si yo fuera CEO, reestructuraría la empresa."}],
    notes:["Use 'were' (not was) with 'I/he/she' in formal second conditional."],
    mistakes:[{wrong:"If I would be CEO",right:"If I were CEO",why:"No 'would' in if-clause"}]
  },
  "Passive voice (present/past)":{
    rule:"Use passive when the doer is unknown, unimportant, or to sound formal.",
    structure:"be + past participle (+ by + agent)",
    examples:[{en:"The report was submitted yesterday.",es:"El reporte fue presentado ayer."},{en:"Decisions are made by the board.",es:"Las decisiones son tomadas por la junta."}],
    notes:["Common in business reports to sound objective."],
    mistakes:[{wrong:"The report was submit",right:"The report was submitted",why:"Need past participle"}]
  },
  "Reported speech (statements)":{
    rule:"When reporting what someone said, shift tenses back one step.",
    structure:"say/tell + that + shifted clause  |  present→past, will→would, can→could",
    examples:[{en:"He said (that) sales had increased by 20%.",es:"Él dijo que las ventas habían aumentado un 20%."}],
    notes:["'Tell' needs an object: 'She told me that…'; 'Say' doesn't."],
    mistakes:[{wrong:"He said me that",right:"He told me that / He said that",why:"Say doesn't take an object"}]
  },
  "Relative clauses (defining)":{
    rule:"Use who/which/that to add essential information to a noun.",
    structure:"noun + who/which/that + verb ...",
    examples:[{en:"The client who called yesterday wants to renegotiate.",es:"El cliente que llamó ayer quiere renegociar."}],
    notes:["No commas in defining clauses."],
    mistakes:[{wrong:"The client, who called yesterday,...",right:"The client who called yesterday...",why:"No commas for defining info"}]
  },
  "Modal verbs (must/should/might/could)":{
    rule:"Modals express obligation, advice, possibility, ability.",
    structure:"subject + modal + base verb",
    examples:[{en:"You must submit compliance reports quarterly.",es:"Debes presentar reportes de cumplimiento trimestralmente."},{en:"Sales might increase next quarter.",es:"Las ventas podrían aumentar el próximo trimestre."}],
    notes:["Must = strong obligation; should = advice; might/could = possibility."],
    mistakes:[{wrong:"She musts attend",right:"She must attend",why:"Modals never take -s"}]
  },
  "Gerunds vs infinitives":{
    rule:"Some verbs take -ing (gerund), others take to + base (infinitive).",
    structure:"enjoy/avoid/consider + -ing  |  want/decide/plan + to + base",
    examples:[{en:"We decided to invest in new technology.",es:"Decidimos invertir en nueva tecnología."},{en:"I enjoy working with analytics.",es:"Disfruto trabajar con análisis de datos."}],
    notes:["After prepositions, always use -ing: 'interested in learning'."],
    mistakes:[{wrong:"We decided investing",right:"We decided to invest",why:"Decide takes infinitive"}]
  },
  "Phrasal verbs (business)":{
    rule:"Verb + particle with a meaning different from the individual words.",
    structure:"verb + preposition/adverb  |  separable or inseparable",
    examples:[{en:"We need to follow up on that lead.",es:"Necesitamos hacer seguimiento a esa oportunidad."},{en:"The meeting was called off.",es:"La reunión fue cancelada."}],
    notes:["Key phrasal verbs: set up, take over, lay off, roll out, scale up."],
    mistakes:[{wrong:"We will follow up on it up",right:"We will follow up on it",why:"Don't repeat the particle"}]
  },
  // ===== B2 =====
  "Third conditional":{
    rule:"Use for unreal/hypothetical past situations and their imaginary consequences.",
    structure:"If + past perfect, would have + past participle",
    examples:[{en:"If we had invested in AI earlier, we would have led the market.",es:"Si hubiéramos invertido en IA antes, habríamos liderado el mercado."}],
    notes:["Used to express regret or analyze past decisions."],
    mistakes:[{wrong:"If we would have invested",right:"If we had invested",why:"No 'would' in the if-clause"}]
  },
  "Mixed conditionals":{
    rule:"Combine 2nd and 3rd conditional: past condition → present result, or present condition → past result.",
    structure:"If + past perfect, would + base  |  If + past simple, would have + past part.",
    examples:[{en:"If we had hired her, she would be our CTO now.",es:"Si la hubiéramos contratado, sería nuestra CTO ahora."}],
    notes:["Useful for analyzing business decisions."],
    mistakes:[{wrong:"If we hired her, she would be CTO now",right:"If we had hired her, she would be CTO now",why:"Past cause needs past perfect"}]
  },
  "Wish/If only":{
    rule:"Express regrets and hypothetical situations.",
    structure:"wish + past simple (present regret)  |  wish + past perfect (past regret)  |  wish + would (annoyance)",
    examples:[{en:"I wish we had more data on this market.",es:"Ojalá tuviéramos más datos de este mercado."},{en:"I wish we had launched earlier.",es:"Ojalá hubiéramos lanzado antes."}],
    notes:["'If only' is more emphatic than 'wish'."],
    mistakes:[{wrong:"I wish we have more data",right:"I wish we had more data",why:"Wish uses past form for present"}]
  },
  "Passive voice (all tenses)":{
    rule:"Passive across all tenses: be + past participle, with tense carried by 'be'.",
    structure:"is/was/has been/will be/is being + past part.",
    examples:[{en:"The merger is being negotiated.",es:"La fusión está siendo negociada."},{en:"The decision has been made.",es:"La decisión ha sido tomada."}],
    notes:["Common in formal reports and announcements."],
    mistakes:[{wrong:"The report is been written",right:"The report is being written",why:"Progressive passive needs 'being'"}]
  },
  "Reported speech (advanced)":{
    rule:"Beyond backshift: reported questions, orders, suggestions with different structures.",
    structure:"ask + if/wh- + subject + verb  |  tell + object + to + base  |  suggest + -ing",
    examples:[{en:"She asked whether we had met the targets.",es:"Preguntó si habíamos cumplido las metas."},{en:"He told us to reconsider.",es:"Nos dijo que reconsideráramos."}],
    notes:["No question word order in reported questions."],
    mistakes:[{wrong:"She asked what did we do",right:"She asked what we did",why:"Reported questions use statement order"}]
  },
  "Inversion for emphasis":{
    rule:"Invert subject-verb order after negative/limiting adverbs for emphasis.",
    structure:"Never/Rarely/Not only/Hardly + auxiliary + subject + verb",
    examples:[{en:"Never have we faced such a crisis.",es:"Nunca hemos enfrentado tal crisis."},{en:"Not only did we meet targets, but we exceeded them.",es:"No solo cumplimos las metas, sino que las superamos."}],
    notes:["Very formal; use in presentations and reports."],
    mistakes:[{wrong:"Never we have seen this",right:"Never have we seen this",why:"Inversion required"}]
  },
  "Cleft sentences":{
    rule:"Restructure a sentence to emphasize one element.",
    structure:"It is/was + X + that/who...  |  What + clause + is/was + X",
    examples:[{en:"It was the CFO who approved the budget.",es:"Fue el CFO quien aprobó el presupuesto."},{en:"What matters most is customer trust.",es:"Lo que más importa es la confianza del cliente."}],
    notes:["Great for executive-level emphasis."],
    mistakes:[]
  },
  "Future perfect & continuous":{
    rule:"Future perfect = action completed by a future time; Future continuous = action in progress at a future time.",
    structure:"will have + past part.  |  will be + verb-ing",
    examples:[{en:"By 2030, we will have expanded to 15 countries.",es:"Para 2030, habremos expandido a 15 países."},{en:"This time next year, we will be operating in Asia.",es:"Para esta fecha el próximo año, estaremos operando en Asia."}],
    notes:["Use with 'by + time' or 'this time next/in...'."],
    mistakes:[]
  },
  // ===== C1 =====
  "Advanced inversion":{
    rule:"Formal inversion for emphasis, condition, or literary effect.",
    structure:"Had I known... / Were we to... / Should you require...",
    examples:[{en:"Had we anticipated the recession, we would have hedged our portfolio.",es:"Si hubiéramos anticipado la recesión, habríamos cubierto nuestro portafolio."},{en:"Should you require further information, please contact us.",es:"Si necesita más información, por favor contáctenos."}],
    notes:["Replaces 'if'-clauses in formal writing."],
    mistakes:[]
  },
  "Subjunctive mood":{
    rule:"Use base verb after verbs of demand/suggestion/importance (that-clause).",
    structure:"verb + that + subject + base verb  |  It is essential/crucial/vital that + base",
    examples:[{en:"The board recommended that the CEO step down.",es:"La junta recomendó que el CEO renunciara."},{en:"It is essential that every employee comply.",es:"Es esencial que cada empleado cumpla."}],
    notes:["Common with: insist, demand, recommend, suggest, require."],
    mistakes:[{wrong:"recommended that he steps down",right:"recommended that he step down",why:"Subjunctive = base verb"}]
  },
  "Nominalisation":{
    rule:"Convert verbs/adjectives into nouns for a more formal, abstract style.",
    structure:"decide → decision, analyse → analysis, grow → growth",
    examples:[{en:"Their decision reflects strategic prioritisation.",es:"Su decisión refleja una priorización estratégica."}],
    notes:["Heavy nominalisation = academic/legal/corporate register."],
    mistakes:[]
  },
  "Hedging language":{
    rule:"Soften claims to sound diplomatic and academic.",
    structure:"may/might/could/tend to/appear to/seem to/it is possible that...",
    examples:[{en:"Results suggest a modest improvement in Q3.",es:"Los resultados sugieren una ligera mejora en el Q3."}],
    notes:["Critical in executive communication and reports."],
    mistakes:[]
  },
  // ===== C2 =====
  "Stylistic inversion":{
    rule:"Literary/rhetorical inversion for stylistic flair in speeches and editorials.",
    structure:"So + adj + verb + subject  |  Only by + -ing + verb + subject",
    examples:[{en:"So compelling was the proposal that the board approved it unanimously.",es:"Tan convincente fue la propuesta que la junta la aprobó por unanimidad."}],
    notes:["Used for dramatic emphasis in high-register English."],
    mistakes:[]
  },
  "Literary & formal devices":{
    rule:"Parallelism, tricolons, and antithesis in executive communication.",
    structure:"parallel lists; contrasts; balanced clauses",
    examples:[{en:"We build for tomorrow, invest for today, and learn from yesterday.",es:"Construimos para mañana, invertimos para hoy y aprendemos del ayer."}],
    notes:["Essential for keynote speeches and thought leadership."],
    mistakes:[]
  }
};

const BE_VOCAB_DB = {
  // ===== A1 =====
  "Office equipment":[
    {en:"laptop",ipa:"/ˈlæp.tɒp/",es:"laptop, portátil",def:"a small, portable computer",ex:"I carry my laptop to every meeting."},
    {en:"printer",ipa:"/ˈprɪn.tər/",es:"impresora",def:"a device that prints documents",ex:"The printer is out of ink."},
    {en:"desk",ipa:"/desk/",es:"escritorio",def:"a table where you work",ex:"Her desk is by the window."},
    {en:"chair",ipa:"/tʃeər/",es:"silla",def:"a seat for one person",ex:"This chair is very comfortable."},
    {en:"whiteboard",ipa:"/ˈwaɪt.bɔːd/",es:"pizarra blanca",def:"a board for writing with markers",ex:"Let me draw it on the whiteboard."},
    {en:"stapler",ipa:"/ˈsteɪ.plər/",es:"engrapador",def:"a tool to join papers",ex:"Can I borrow your stapler?"}
  ],
  "Job titles":[
    {en:"manager",ipa:"/ˈmæn.ɪ.dʒər/",es:"gerente",def:"person in charge of a team",ex:"She is the marketing manager."},
    {en:"accountant",ipa:"/əˈkaʊn.tənt/",es:"contador(a)",def:"person who handles money and taxes",ex:"Our accountant prepares the reports."},
    {en:"engineer",ipa:"/ˌen.dʒɪˈnɪər/",es:"ingeniero(a)",def:"person who designs and builds",ex:"He is a software engineer."},
    {en:"CEO",ipa:"/ˌsiːˌiːˈəʊ/",es:"director ejecutivo",def:"chief executive officer",ex:"The CEO will present the strategy."},
    {en:"intern",ipa:"/ˈɪn.tɜːn/",es:"practicante",def:"a student or trainee worker",ex:"We have two interns this summer."},
    {en:"assistant",ipa:"/əˈsɪs.tənt/",es:"asistente",def:"a person who helps",ex:"My assistant manages my calendar."}
  ],
  "Departments":[
    {en:"Human Resources",ipa:"/ˈhjuː.mən rɪˈsɔː.sɪz/",es:"Recursos Humanos",def:"department managing employees",ex:"HR will contact you tomorrow."},
    {en:"Finance",ipa:"/ˈfaɪ.næns/",es:"Finanzas",def:"department managing money",ex:"Finance approved the budget."},
    {en:"Marketing",ipa:"/ˈmɑː.kɪ.tɪŋ/",es:"Marketing",def:"department promoting products",ex:"Marketing launched a campaign."},
    {en:"Sales",ipa:"/seɪlz/",es:"Ventas",def:"department selling products",ex:"Sales exceeded targets."},
    {en:"IT",ipa:"/ˌaɪˈtiː/",es:"TI, Tecnología de la Información",def:"information technology",ex:"Call IT about the server issue."},
    {en:"Legal",ipa:"/ˈliː.ɡəl/",es:"Legal",def:"department handling laws and contracts",ex:"Legal reviewed the contract."}
  ],
  "Numbers & money":[
    {en:"invoice",ipa:"/ˈɪn.vɔɪs/",es:"factura",def:"a bill for goods or services",ex:"Please send the invoice by Friday."},
    {en:"budget",ipa:"/ˈbʌdʒ.ɪt/",es:"presupuesto",def:"planned money for spending",ex:"Our budget is limited this quarter."},
    {en:"revenue",ipa:"/ˈrev.ən.juː/",es:"ingresos",def:"total income earned",ex:"Revenue grew by 15%."},
    {en:"cost",ipa:"/kɒst/",es:"costo",def:"amount of money required",ex:"We need to reduce costs."},
    {en:"profit",ipa:"/ˈprɒf.ɪt/",es:"ganancia",def:"money earned after costs",ex:"Our profit margin is 12%."},
    {en:"currency",ipa:"/ˈkʌr.ən.si/",es:"moneda",def:"money used in a country",ex:"The local currency is the sol."}
  ],
  "Telephone basics":[
    {en:"answer the phone",ipa:"/ˈɑːn.sər ðə fəʊn/",es:"contestar el teléfono",def:"to pick up a ringing phone",ex:"Can you answer the phone, please?"},
    {en:"hold the line",ipa:"/həʊld ðə laɪn/",es:"esperar en la línea",def:"to wait on a call",ex:"Please hold the line for a moment."},
    {en:"put through",ipa:"/pʊt θruː/",es:"pasar la llamada",def:"to connect a caller",ex:"I'll put you through to Mr. Lee."},
    {en:"leave a message",ipa:"/liːv ə ˈmes.ɪdʒ/",es:"dejar un mensaje",def:"to record a voice note",ex:"Can I leave a message?"},
    {en:"speak up",ipa:"/spiːk ʌp/",es:"hablar más alto",def:"to speak louder",ex:"Could you speak up, please?"},
    {en:"extension",ipa:"/ɪkˈsten.ʃən/",es:"anexo",def:"internal phone number",ex:"My extension is 4521."}
  ],
  // ===== A2 =====
  "Career vocabulary":[
    {en:"promotion",ipa:"/prəˈməʊ.ʃən/",es:"ascenso",def:"a move to a higher position",ex:"She got a promotion last month."},
    {en:"resign",ipa:"/rɪˈzaɪn/",es:"renunciar",def:"to officially leave a job",ex:"He resigned to start his own company."},
    {en:"apply",ipa:"/əˈplaɪ/",es:"postular",def:"to formally request a job",ex:"I applied for three positions."},
    {en:"hire",ipa:"/haɪər/",es:"contratar",def:"to employ someone",ex:"We hired five engineers this quarter."},
    {en:"salary",ipa:"/ˈsæl.ər.i/",es:"salario",def:"monthly payment for a job",ex:"The salary is competitive."},
    {en:"colleague",ipa:"/ˈkɒl.iːɡ/",es:"colega",def:"a person you work with",ex:"My colleague helped me finish the task."}
  ],
  "Sales & selling":[
    {en:"customer",ipa:"/ˈkʌs.tə.mər/",es:"cliente",def:"a person who buys",ex:"Our customers trust our brand."},
    {en:"discount",ipa:"/ˈdɪs.kaʊnt/",es:"descuento",def:"a reduction in price",ex:"We offer a 10% discount."},
    {en:"quote",ipa:"/kwəʊt/",es:"cotización",def:"a price estimate",ex:"I'll send you a quote tomorrow."},
    {en:"invoice",ipa:"/ˈɪn.vɔɪs/",es:"factura",def:"a bill for a sale",ex:"The invoice is due in 30 days."},
    {en:"commission",ipa:"/kəˈmɪʃ.ən/",es:"comisión",def:"percentage payment for sales",ex:"Sales reps earn a 5% commission."},
    {en:"pitch",ipa:"/pɪtʃ/",es:"presentación de venta",def:"a sales presentation",ex:"Her sales pitch was very persuasive."}
  ],
  // ===== B1 =====
  "Brands & branding":[
    {en:"brand identity",ipa:"/brænd aɪˈden.tə.ti/",es:"identidad de marca",def:"how a brand is perceived",ex:"We're redesigning our brand identity."},
    {en:"logo",ipa:"/ˈləʊ.ɡəʊ/",es:"logo",def:"visual symbol of a brand",ex:"The new logo is minimalist."},
    {en:"positioning",ipa:"/pəˈzɪʃ.ən.ɪŋ/",es:"posicionamiento",def:"market perception strategy",ex:"Our positioning is premium quality."},
    {en:"target audience",ipa:"/ˈtɑː.ɡɪt ˈɔː.di.əns/",es:"público objetivo",def:"intended customers",ex:"Our target audience is millennials."},
    {en:"rebranding",ipa:"/ˌriːˈbrænd.ɪŋ/",es:"cambio de imagen",def:"changing a brand's image",ex:"The rebranding cost $2 million."},
    {en:"awareness",ipa:"/əˈweə.nəs/",es:"reconocimiento",def:"how well known a brand is",ex:"Brand awareness grew by 30%."}
  ],
  "Human resources":[
    {en:"recruitment",ipa:"/rɪˈkruːt.mənt/",es:"reclutamiento",def:"process of hiring",ex:"Recruitment takes about six weeks."},
    {en:"onboarding",ipa:"/ˈɒn.bɔː.dɪŋ/",es:"inducción",def:"integrating new employees",ex:"Onboarding includes two weeks of training."},
    {en:"appraisal",ipa:"/əˈpreɪ.zəl/",es:"evaluación de desempeño",def:"performance review",ex:"Annual appraisals happen in December."},
    {en:"redundancy",ipa:"/rɪˈdʌn.dən.si/",es:"despido",def:"layoff due to restructuring",ex:"The company announced 50 redundancies."},
    {en:"retention",ipa:"/rɪˈten.ʃən/",es:"retención",def:"keeping employees",ex:"Our retention rate is 95%."},
    {en:"benefits",ipa:"/ˈben.ɪ.fɪts/",es:"beneficios",def:"non-salary compensation",ex:"The benefits package includes health insurance."}
  ],
  // ===== B2 =====
  "Executive presentations":[
    {en:"stakeholder",ipa:"/ˈsteɪk.həʊl.dər/",es:"parte interesada",def:"someone with interest in a project",ex:"We need buy-in from all stakeholders."},
    {en:"KPI",ipa:"/ˌkeɪ.piːˈaɪ/",es:"indicador clave",def:"key performance indicator",ex:"Our main KPIs are revenue and retention."},
    {en:"roadmap",ipa:"/ˈrəʊd.mæp/",es:"hoja de ruta",def:"strategic plan",ex:"The product roadmap covers 18 months."},
    {en:"deliverable",ipa:"/dɪˈlɪv.ər.ə.bəl/",es:"entregable",def:"item to be produced",ex:"Our Q2 deliverables include the beta launch."},
    {en:"synergy",ipa:"/ˈsɪn.ə.dʒi/",es:"sinergia",def:"combined positive effect",ex:"The merger creates significant synergies."},
    {en:"bottleneck",ipa:"/ˈbɒt.əl.nek/",es:"cuello de botella",def:"point of congestion",ex:"Approval processes are a bottleneck."}
  ],
  "AI & digital transformation":[
    {en:"machine learning",ipa:"/məˈʃiːn ˈlɜː.nɪŋ/",es:"aprendizaje automático",def:"AI that learns from data",ex:"Machine learning predicts customer churn."},
    {en:"algorithm",ipa:"/ˈæl.ɡə.rɪ.ðəm/",es:"algoritmo",def:"a set of rules for a computer",ex:"The algorithm processes millions of transactions."},
    {en:"automation",ipa:"/ˌɔː.təˈmeɪ.ʃən/",es:"automatización",def:"using machines instead of people",ex:"Automation cut processing time by 70%."},
    {en:"chatbot",ipa:"/ˈtʃæt.bɒt/",es:"chatbot",def:"an automated chat assistant",ex:"Our chatbot handles 80% of inquiries."},
    {en:"cloud computing",ipa:"/klaʊd kəmˈpjuː.tɪŋ/",es:"computación en la nube",def:"remote computing services",ex:"We migrated to cloud computing last year."},
    {en:"data analytics",ipa:"/ˈdeɪ.tə ˌæn.əˈlɪt.ɪks/",es:"análisis de datos",def:"analysing data for insights",ex:"Data analytics drives our decisions."}
  ],
  "Cryptocurrency & Fintech":[
    {en:"blockchain",ipa:"/ˈblɒk.tʃeɪn/",es:"cadena de bloques",def:"distributed ledger technology",ex:"Blockchain enables secure transactions."},
    {en:"cryptocurrency",ipa:"/ˌkrɪp.təʊˈkʌr.ən.si/",es:"criptomoneda",def:"digital currency",ex:"Bitcoin is the leading cryptocurrency."},
    {en:"wallet",ipa:"/ˈwɒl.ɪt/",es:"billetera",def:"digital storage for crypto",ex:"Keep your wallet keys secure."},
    {en:"decentralized",ipa:"/diːˈsen.trəl.aɪzd/",es:"descentralizado",def:"without central control",ex:"DeFi stands for decentralized finance."},
    {en:"mining",ipa:"/ˈmaɪ.nɪŋ/",es:"minería",def:"validating blockchain transactions",ex:"Bitcoin mining consumes massive energy."},
    {en:"volatility",ipa:"/ˌvɒl.əˈtɪl.ə.ti/",es:"volatilidad",def:"high price variability",ex:"Crypto volatility deters institutional investors."}
  ],
  // ===== C1 =====
  "Strategic communication":[
    {en:"narrative",ipa:"/ˈnær.ə.tɪv/",es:"narrativa",def:"a coherent story",ex:"We need a compelling narrative for investors."},
    {en:"messaging",ipa:"/ˈmes.ɪ.dʒɪŋ/",es:"mensajes clave",def:"strategic key messages",ex:"Align all messaging with corporate values."},
    {en:"stakeholder mapping",ipa:"/ˈsteɪk.həʊl.dər ˈmæp.ɪŋ/",es:"mapeo de interesados",def:"identifying key parties",ex:"Stakeholder mapping reveals hidden allies."},
    {en:"positioning statement",ipa:"/pəˈzɪʃ.ən.ɪŋ ˈsteɪt.mənt/",es:"declaración de posicionamiento",def:"concise brand purpose",ex:"The positioning statement is one sentence."},
    {en:"crisis comms",ipa:"/ˈkraɪ.sɪs kɒmz/",es:"comunicación de crisis",def:"communication during emergencies",ex:"Our crisis comms plan is activated."},
    {en:"thought leadership",ipa:"/θɔːt ˈliː.də.ʃɪp/",es:"liderazgo de pensamiento",def:"expertise-based influence",ex:"Thought leadership builds long-term trust."}
  ],
  "Sustainability & ESG reporting":[
    {en:"ESG",ipa:"/ˌiː.esˈdʒiː/",es:"ASG",def:"Environmental, Social, Governance",ex:"ESG ratings affect institutional investment."},
    {en:"carbon footprint",ipa:"/ˈkɑː.bən ˈfʊt.prɪnt/",es:"huella de carbono",def:"total CO2 emissions",ex:"We aim to halve our carbon footprint by 2030."},
    {en:"net zero",ipa:"/net ˈzɪə.rəʊ/",es:"cero neto",def:"zero net greenhouse emissions",ex:"Our net zero target is 2040."},
    {en:"greenwashing",ipa:"/ˈɡriːn.wɒʃ.ɪŋ/",es:"lavado verde",def:"false sustainability claims",ex:"Regulators crack down on greenwashing."},
    {en:"materiality",ipa:"/məˌtɪə.riˈæl.ə.ti/",es:"materialidad",def:"relevance to stakeholders",ex:"Materiality assessment guides our reporting."},
    {en:"disclosure",ipa:"/dɪˈskləʊ.ʒər/",es:"divulgación",def:"formal release of information",ex:"SEC disclosure rules now include climate risk."}
  ],
  // ===== C2 =====
  "Boardroom English & governance":[
    {en:"fiduciary duty",ipa:"/fɪˈdjuː.ʃi.ər.i ˈdjuː.ti/",es:"deber fiduciario",def:"legal obligation to act in another's interest",ex:"Directors owe fiduciary duties to shareholders."},
    {en:"quorum",ipa:"/ˈkwɔː.rəm/",es:"quórum",def:"minimum members for a meeting",ex:"We lack a quorum to vote."},
    {en:"motion",ipa:"/ˈməʊ.ʃən/",es:"moción",def:"formal proposal in a meeting",ex:"I'd like to table a motion."},
    {en:"chair",ipa:"/tʃeər/",es:"presidente(a)",def:"the leader of a meeting",ex:"The chair called the meeting to order."},
    {en:"proxy",ipa:"/ˈprɒk.si/",es:"poder, representante",def:"authority to vote for another",ex:"Please sign the proxy form."},
    {en:"bylaw",ipa:"/ˈbaɪ.lɔː/",es:"estatuto",def:"internal rule of an organization",ex:"The bylaws specify a three-year term."}
  ],
  "Corporate diplomacy":[
    {en:"diplomatic immunity",ipa:"/ˌdɪp.ləˈmæt.ɪk ɪˈmjuː.nə.ti/",es:"inmunidad diplomática",def:"protection from local laws",ex:"Ambassadors enjoy diplomatic immunity."},
    {en:"geopolitical risk",ipa:"/ˌdʒiː.əʊ.pəˈlɪt.ɪ.kəl rɪsk/",es:"riesgo geopolítico",def:"political risk across borders",ex:"Geopolitical risk drove up oil prices."},
    {en:"back-channel",ipa:"/ˈbæk.tʃæn.əl/",es:"canal reservado",def:"unofficial communication",ex:"Back-channel talks preceded the deal."},
    {en:"MoU",ipa:"/ˌem.əʊˈjuː/",es:"memorando de entendimiento",def:"memorandum of understanding",ex:"We signed an MoU with the ministry."},
    {en:"détente",ipa:"/deɪˈtɒnt/",es:"distensión",def:"easing of tensions",ex:"A period of détente benefits both parties."},
    {en:"realpolitik",ipa:"/reɪˈɑːl.pəʊ.lɪˌtiːk/",es:"realpolitik",def:"pragmatic political approach",ex:"Trade agreements often reflect realpolitik."}
  ]
};

// ===== FALLBACK GENERATORS =====
// Used when a topic isn't in the DB
function BE_makeGrammarFallback(topic){
  return {
    rule:`Master the key rules of ${topic} to communicate accurately in business contexts.`,
    structure:`See the examples below for the structure of ${topic}.`,
    examples:[
      {en:`This example illustrates ${topic} in a business sentence.`,es:`Este ejemplo ilustra ${topic} en una oración de negocios.`},
      {en:`Study how ${topic} is applied in formal communication.`,es:`Observa cómo se aplica ${topic} en la comunicación formal.`},
      {en:`Practice ${topic} to improve fluency in meetings and reports.`,es:`Practica ${topic} para mejorar la fluidez en reuniones y reportes.`}
    ],
    notes:[`Focus on accuracy before speed.`,`Review related grammar points for reinforcement.`],
    mistakes:[]
  };
}
function BE_makeVocabFallback(topic){
  // Generate 6 generic business words themed around topic
  return [
    {en:"approach",ipa:"/əˈprəʊtʃ/",es:"enfoque",def:"a way of dealing with something",ex:`Our approach to ${topic.toLowerCase()} is data-driven.`},
    {en:"strategy",ipa:"/ˈstræt.ə.dʒi/",es:"estrategia",def:"a long-term plan",ex:`Our ${topic.toLowerCase()} strategy is under review.`},
    {en:"framework",ipa:"/ˈfreɪm.wɜːk/",es:"marco",def:"a structure for decisions",ex:`We use a clear framework for ${topic.toLowerCase()}.`},
    {en:"metrics",ipa:"/ˈmet.rɪks/",es:"métricas",def:"measurements used to track progress",ex:`We review ${topic.toLowerCase()} metrics weekly.`},
    {en:"initiative",ipa:"/ɪˈnɪʃ.ə.tɪv/",es:"iniciativa",def:"a new plan to solve a problem",ex:`This initiative targets ${topic.toLowerCase()} improvement.`},
    {en:"stakeholders",ipa:"/ˈsteɪk.həʊl.dəz/",es:"partes interesadas",def:"people affected by a decision",ex:`Align ${topic.toLowerCase()} decisions with stakeholders.`}
  ];
}

function BE_getGrammar(topic){
  return BE_GRAMMAR_DB[topic] || BE_makeGrammarFallback(topic);
}
function BE_getVocab(topic){
  return BE_VOCAB_DB[topic] || BE_makeVocabFallback(topic);
}
