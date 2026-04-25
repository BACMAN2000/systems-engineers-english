// ===== EXTENDED BUSINESS ENGLISH MATERIALS =====
// Part 2: Case Studies + Additional Grammar + Additional Vocabulary
// Loaded AFTER be-materials.js - extends the existing DBs

// ===== ADDITIONAL GRAMMAR =====
Object.assign(BE_GRAMMAR_DB, {
  // A2 remaining
  "Adverbs of manner":{
    rule:"Adverbs of manner describe HOW an action is done. Usually formed by adding -ly.",
    structure:"adjective + -ly → adverb  |  quick → quickly, careful → carefully",
    examples:[{en:"She presented the results clearly and professionally.",es:"Presentó los resultados clara y profesionalmente."}],
    notes:["Irregular: good → well, fast → fast, hard → hard."],
    mistakes:[{wrong:"He spoke good",right:"He spoke well",why:"'Good' is adjective; 'well' is adverb"}]
  },
  "Too/enough":{
    rule:"Too = more than necessary (negative). Enough = sufficient amount.",
    structure:"too + adj/adv  |  adj/adv + enough  |  enough + noun",
    examples:[{en:"This proposal is too expensive.",es:"Esta propuesta es demasiado cara."},{en:"We don't have enough time.",es:"No tenemos suficiente tiempo."}],
    notes:["'Enough' comes AFTER adjectives but BEFORE nouns."],
    mistakes:[{wrong:"enough good",right:"good enough",why:"Enough follows adjectives"}]
  },
  "Both/neither/either":{
    rule:"Both = A + B (2 things). Neither = not A and not B. Either = A or B.",
    structure:"both + plural verb  |  neither/either + singular verb",
    examples:[{en:"Both proposals have merit.",es:"Ambas propuestas tienen mérito."},{en:"Neither option is viable.",es:"Ninguna opción es viable."}],
    notes:["Neither…nor, either…or are correlative pairs."],
    mistakes:[{wrong:"Both of proposals",right:"Both proposals / Both of the proposals",why:"Both + noun directly, or both of + the"}]
  },
  "Object pronouns":{
    rule:"Object pronouns replace nouns that receive the action.",
    structure:"me, you, him, her, it, us, them",
    examples:[{en:"Please send it to them by Friday.",es:"Por favor envíaselo a ellos para el viernes."}],
    notes:["After prepositions, use object pronouns: 'between you and me' (not 'I')."],
    mistakes:[{wrong:"between you and I",right:"between you and me",why:"After preposition = object form"}]
  },
  "Possessive pronouns":{
    rule:"Possessive pronouns replace 'possessive adjective + noun'.",
    structure:"mine, yours, his, hers, ours, theirs",
    examples:[{en:"This office is mine, that one is theirs.",es:"Esta oficina es mía, aquella es de ellos."}],
    notes:["No apostrophe: 'yours' (not 'your's')."],
    mistakes:[{wrong:"Its mine",right:"It's mine",why:"It's = it is; 'its' = possessive adjective"}]
  },
  "Prepositions of movement":{
    rule:"Prepositions showing direction or movement.",
    structure:"to, from, into, out of, through, across, along, towards, onto",
    examples:[{en:"Please move the meeting from Monday to Wednesday.",es:"Por favor mueve la reunión de lunes a miércoles."}],
    notes:["'To' for destination, 'toward(s)' for direction without arrival."],
    mistakes:[{wrong:"I went at the office",right:"I went to the office",why:"Use 'to' for destination"}]
  },
  // B1 remaining
  "Linking words (however/although/despite)":{
    rule:"Linkers connect ideas showing contrast, reason, result, addition.",
    structure:"However + , + clause  |  Although/Even though + clause  |  Despite/In spite of + noun/-ing",
    examples:[{en:"Sales rose 10%. However, profits fell.",es:"Las ventas subieron 10%. Sin embargo, las ganancias cayeron."},{en:"Despite the downturn, we hired more staff.",es:"A pesar de la recesión, contratamos más personal."}],
    notes:["'Although' introduces a clause; 'despite' introduces a noun/-ing."],
    mistakes:[{wrong:"Despite he was tired",right:"Although he was tired / Despite being tired",why:"Despite needs a noun/-ing"}]
  },
  "Articles (advanced use)":{
    rule:"Zero article with generic plurals, meals, institutions; 'the' with unique/specified things.",
    structure:"no article for generic / the for specific / a|an for one of many",
    examples:[{en:"Managers (generic) often attend the board meetings (specific).",es:"Los gerentes (en general) suelen asistir a las reuniones de junta (específicas)."}],
    notes:["'The' with superlatives, ordinals, and unique nouns: the CEO, the best, the first."],
    mistakes:[{wrong:"I work in the marketing",right:"I work in marketing",why:"Departments = zero article"}]
  },
  "Quantifiers (each/every/all/none)":{
    rule:"Each = individual. Every = group viewed as whole. All = totality. None = zero.",
    structure:"each/every + singular noun + singular verb  |  all + plural/uncountable  |  none of + plural",
    examples:[{en:"Every employee receives bonuses.",es:"Cada empleado recibe bonos."},{en:"All managers attended the retreat.",es:"Todos los gerentes asistieron al retiro."}],
    notes:["'Each of' + plural noun + singular verb: Each of the teams has a leader."],
    mistakes:[{wrong:"Every employees",right:"Every employee",why:"'Every' takes singular"}]
  },
  "Have something done (causative)":{
    rule:"Have/Get + object + past participle: someone else does the action for you.",
    structure:"have + noun + past participle",
    examples:[{en:"We had the contracts reviewed by legal.",es:"Hicimos que legal revisara los contratos."},{en:"I'm getting my laptop repaired.",es:"Estoy haciendo reparar mi laptop."}],
    notes:["Common in business outsourcing contexts."],
    mistakes:[{wrong:"I had reviewed the contracts (if you mean someone did it for you)",right:"I had the contracts reviewed",why:"Order: have + object + past part."}]
  },
  "Future forms review (will/going to/present continuous)":{
    rule:"Will = predictions/offers; Going to = planned intentions/evidence; Present continuous = fixed arrangements.",
    structure:"will + base  |  be going to + base  |  am/is/are + verb-ing",
    examples:[{en:"I'll call him now. We're going to launch in Q3. The meeting is starting at 10.",es:"Lo llamaré ahora. Vamos a lanzar en Q3. La reunión empieza a las 10."}],
    notes:["Use the form that best matches certainty + planning."],
    mistakes:[{wrong:"I go to the airport tomorrow (for fixed plan)",right:"I'm going to the airport tomorrow",why:"Fixed arrangement = present continuous"}]
  },
  // B2 remaining
  "Advanced modal verbs (needn't have/could have)":{
    rule:"Past modals speculate about or evaluate past actions.",
    structure:"must have + past part. (certainty)  |  might/could have + past part. (possibility)  |  needn't have + past part. (unnecessary past action done)  |  should have + past part. (regret/criticism)",
    examples:[{en:"We needn't have hired consultants — we had the expertise in-house.",es:"No hacía falta que contratáramos consultores — teníamos la experiencia internamente."},{en:"The deal must have leaked to the press.",es:"La operación debe haberse filtrado a la prensa."}],
    notes:["'Didn't need to' (didn't do it) vs 'needn't have' (did it but didn't need to)."],
    mistakes:[]
  },
  "Collocations (make/do/take/get)":{
    rule:"Some verbs commonly pair with specific nouns — memorize them as fixed phrases.",
    structure:"make a decision/profit/offer  |  do business/research/a favor  |  take a risk/action/responsibility  |  get results/approval/feedback",
    examples:[{en:"We took immediate action to mitigate the risk and got approval from the board.",es:"Tomamos acción inmediata para mitigar el riesgo y obtuvimos la aprobación de la junta."}],
    notes:["Wrong collocations sound unnatural; learn them as chunks."],
    mistakes:[{wrong:"make a research",right:"do research",why:"Research collocates with 'do'"}]
  },
  "Formal/informal register switching":{
    rule:"Adjust vocabulary, contractions, and structure to match audience and channel.",
    structure:"Formal: no contractions, Latinate vocab, passive  |  Informal: contractions, phrasal verbs, active",
    examples:[{en:"We regret to inform you that the proposal has been declined.",es:"Lamentamos informarle que la propuesta ha sido rechazada."},{en:"Sorry, we couldn't go with your proposal.",es:"Lo siento, no pudimos aceptar tu propuesta."}],
    notes:["Email to clients = formal. Slack to team = informal."],
    mistakes:[]
  },
  "Discourse markers":{
    rule:"Words that organize spoken/written discourse and signal function.",
    structure:"to sum up, on the one hand, in other words, as a matter of fact, speaking of...",
    examples:[{en:"To sum up, we should proceed with Option B.",es:"En resumen, deberíamos proceder con la Opción B."}],
    notes:["Use sparingly — too many markers sound artificial."],
    mistakes:[]
  },
  "Participle clauses":{
    rule:"Use -ing or past participle clauses to replace relative/adverbial clauses for concision.",
    structure:"verb-ing clause (active)  |  past participle clause (passive)",
    examples:[{en:"Facing a recession, the company cut costs.",es:"Enfrentando una recesión, la empresa redujo costos."},{en:"Founded in 1985, Cohasset leads the market.",es:"Fundada en 1985, Cohasset lidera el mercado."}],
    notes:["Common in reports and press releases."],
    mistakes:[]
  },
  "Emphasis structures (It is/What we need)":{
    rule:"Restructure sentences to emphasize a specific element.",
    structure:"It is/was + X + that/who  |  What + clause + is + X  |  The reason + clause + is that...",
    examples:[{en:"It is customer trust that drives retention.",es:"Es la confianza del cliente lo que impulsa la retención."},{en:"What we need is a clear value proposition.",es:"Lo que necesitamos es una propuesta de valor clara."}],
    notes:["Useful in executive presentations."],
    mistakes:[]
  },
  "Advanced phrasal verbs (business)":{
    rule:"Multi-word verbs with non-literal meanings common in business.",
    structure:"roll out (launch), scale up (grow), take on (accept), wind down (reduce), buy out (acquire), spin off (divest)",
    examples:[{en:"We're rolling out the new CRM across all offices and spinning off the non-core divisions.",es:"Estamos implementando el nuevo CRM en todas las oficinas y escindiendo las divisiones no esenciales."}],
    notes:["Common: sign off on, follow up on, reach out to, circle back."],
    mistakes:[]
  },
  // C1 remaining
  "Mixed conditionals (complex)":{
    rule:"Blend time frames to express nuanced hypothetical relationships.",
    structure:"Various combinations of if-clause tense with main clause conditional",
    examples:[{en:"If the board had approved the acquisition, we would now control 40% of the market.",es:"Si la junta hubiera aprobado la adquisición, ahora controlaríamos el 40% del mercado."}],
    notes:["Common in strategic post-mortems."],
    mistakes:[]
  },
  "Ellipsis & substitution":{
    rule:"Omit or replace repeated elements to avoid redundancy.",
    structure:"one/ones, do so, so do I, neither did they, auxiliaries alone",
    examples:[{en:"We expected growth, and so did our competitors.",es:"Esperábamos crecimiento, y nuestros competidores también."}],
    notes:["Common in professional conversation."],
    mistakes:[]
  },
  "Advanced passive structures":{
    rule:"Use impersonal passives and distancing for objectivity and diplomacy.",
    structure:"It is said/believed/claimed + that-clause  |  Subject + is said/believed + to-infinitive",
    examples:[{en:"It is widely believed that regulation will tighten next year.",es:"Se cree ampliamente que la regulación se endurecerá el próximo año."}],
    notes:["Useful to hedge claims in reports."],
    mistakes:[]
  },
  "Fronting for emphasis":{
    rule:"Move a phrase to the front of the sentence for thematic emphasis.",
    structure:"Adverbial phrase + comma + rest of sentence",
    examples:[{en:"In this quarter, we achieved record revenue.",es:"En este trimestre, logramos ingresos récord."}],
    notes:["Common in executive reports."],
    mistakes:[]
  },
  "Complex noun phrases":{
    rule:"Build dense noun phrases with pre/post-modifiers for formal writing.",
    structure:"det + adj + adj + noun + prep phrase + relative clause",
    examples:[{en:"The recently announced multi-year strategic partnership with regional distributors was pivotal.",es:"La asociación estratégica plurianual recientemente anunciada con distribuidores regionales fue fundamental."}],
    notes:["Hallmark of C1+ formal register."],
    mistakes:[]
  },
  "Pragmatic markers":{
    rule:"Signal speaker attitude, stance, or discourse flow.",
    structure:"frankly, arguably, admittedly, to be honest, mind you, in fairness",
    examples:[{en:"Frankly, the numbers don't justify the investment.",es:"Francamente, los números no justifican la inversión."}],
    notes:["Useful in negotiations and boardroom discussions."],
    mistakes:[]
  },
  "Concessive clauses":{
    rule:"Acknowledge an opposing point while maintaining your position.",
    structure:"While/Whilst/Whereas + clause  |  Much as + clause  |  Granted that + clause",
    examples:[{en:"Much as we appreciate your offer, we must decline.",es:"Aunque apreciamos su oferta, debemos declinar."}],
    notes:["Signals diplomatic disagreement."],
    mistakes:[]
  },
  "Distancing language":{
    rule:"Distance yourself from claims to avoid commitment or liability.",
    structure:"reportedly, allegedly, apparently, it would seem, there are indications that...",
    examples:[{en:"The CEO reportedly favors a spin-off.",es:"El CEO supuestamente favorece una escisión."}],
    notes:["Common in journalism and crisis comms."],
    mistakes:[]
  },
  "Advanced reported speech patterns":{
    rule:"Beyond backshift: modal shifts, conditional shifts, verb variety for reporting.",
    structure:"acknowledged, conceded, insisted, maintained, claimed + that-clause",
    examples:[{en:"The CFO conceded that projections had been overly optimistic.",es:"El CFO admitió que las proyecciones habían sido demasiado optimistas."}],
    notes:["Verb choice carries attitudinal meaning."],
    mistakes:[]
  },
  "Hypothetical past (advanced)":{
    rule:"Express regret, criticism, or counterfactual analysis of past events.",
    structure:"should/ought to have + past part.  |  would have + past part.  |  could have + past part.",
    examples:[{en:"We ought to have diversified our portfolio much earlier.",es:"Deberíamos haber diversificado nuestro portafolio mucho antes."}],
    notes:["Tone depends on modal choice."],
    mistakes:[]
  },
  "Formal written grammar conventions":{
    rule:"Observe register-specific rules in business writing.",
    structure:"avoid contractions, use Latinate vocabulary, prefer passive, minimize phrasal verbs, no 2nd-person 'you'",
    examples:[{en:"Recipients are requested to respond by end of business Friday.",es:"Se solicita a los destinatarios responder para el fin del día viernes."}],
    notes:["C1-C2 written business register."],
    mistakes:[]
  },
  // C2 remaining
  "Complex subordination patterns":{
    rule:"Embed multiple clauses with precise logical relationships.",
    structure:"main + relative + adverbial + noun clause, nested",
    examples:[{en:"The proposal, which the board had reviewed before the crisis emerged, was tabled pending further analysis.",es:"La propuesta, que la junta había revisado antes de que surgiera la crisis, fue postergada a la espera de más análisis."}],
    notes:["Typical of high-register legal and boardroom English."],
    mistakes:[]
  },
  "Rhetorical structures":{
    rule:"Use rhetorical devices to persuade and resonate.",
    structure:"anaphora, chiasmus, tricolon, rhetorical questions",
    examples:[{en:"We did not retreat; we did not surrender; we prevailed.",es:"No retrocedimos; no nos rendimos; prevalecimos."}],
    notes:["Hallmark of CEO keynotes and investor letters."],
    mistakes:[]
  },
  "Advanced hedging & mitigation":{
    rule:"Stack hedges for maximum diplomatic ambiguity.",
    structure:"it may be the case that + it would appear that + subject + verb",
    examples:[{en:"It would appear that there may be grounds for reconsidering our position.",es:"Parecería que podría haber razones para reconsiderar nuestra posición."}],
    notes:["Typical of diplomatic and regulatory language."],
    mistakes:[]
  },
  "Pragmatic competence":{
    rule:"Match language to social context, power relations, and face-saving needs.",
    structure:"Politeness strategies: indirect requests, face-threatening act mitigation, off-record implicature",
    examples:[{en:"I wonder if you might be able to share your thinking on that.",es:"Me pregunto si podría compartir su pensamiento sobre eso."}],
    notes:["Critical in cross-cultural executive settings."],
    mistakes:[]
  },
  "Sociolinguistic register shifting":{
    rule:"Shift register fluidly between formal, semi-formal, and informal as context demands.",
    structure:"Reading audience: education, power, culture → select register",
    examples:[{en:"From 'pursuant to our agreement' to 'as we agreed' within the same conversation.",es:"De 'en virtud de nuestro acuerdo' a 'como acordamos' dentro de la misma conversación."}],
    notes:["Code-switching between formal meetings and side conversations."],
    mistakes:[]
  },
  "Irony & understatement in business":{
    rule:"Use ironic distance and understatement for effect, especially in British business culture.",
    structure:"litotes: 'not unreasonable', 'not unwelcome'  |  ironic overstatement",
    examples:[{en:"The results were not entirely disappointing.",es:"Los resultados no fueron del todo decepcionantes."}],
    notes:["High risk of misinterpretation in cross-cultural contexts."],
    mistakes:[]
  },
  "Complex conditional chains":{
    rule:"Chain multiple conditionals to analyze branching scenarios.",
    structure:"If A, then B; but if C, then D, in which case E",
    examples:[{en:"If rates hold, we'll refinance; but if they rise, we'll defer the acquisition, in which case the 2027 target slips.",es:"Si las tasas se mantienen, refinanciaremos; pero si suben, aplazaremos la adquisición, en cuyo caso la meta de 2027 se retrasa."}],
    notes:["Common in scenario planning and strategy sessions."],
    mistakes:[]
  },
  "Nominal clauses (advanced)":{
    rule:"Use that/whether/wh-clauses as subjects, objects, or complements.",
    structure:"That-clause as subject: 'That we underperformed is undeniable.'",
    examples:[{en:"Whether to pursue the acquisition remains under review.",es:"Si perseguir la adquisición sigue en revisión."}],
    notes:["Formal and dense."],
    mistakes:[]
  },
  "Free indirect speech":{
    rule:"Blend narrator and character voice without quotation marks or full reporting structure.",
    structure:"Mix of reported and direct speech features",
    examples:[{en:"The CEO was adamant. The deal would close. Failure was not an option.",es:"El CEO fue categórico. El trato se cerraría. El fracaso no era una opción."}],
    notes:["Used in long-form business journalism and annual letters."],
    mistakes:[]
  },
  "Cleft sentences (advanced)":{
    rule:"Use various cleft patterns to precisely control emphasis.",
    structure:"It-cleft: It was X that... | Wh-cleft: What X did was... | Reversed wh-cleft: X is what...",
    examples:[{en:"What ultimately undermined the deal was a loss of trust between principals.",es:"Lo que finalmente socavó el acuerdo fue la pérdida de confianza entre los principales."}],
    notes:["Advanced focus techniques."],
    mistakes:[]
  },
  "Extraposition":{
    rule:"Move a heavy subject to the end, using dummy 'it' or 'there' as placeholder.",
    structure:"It + be + adj + that-clause/to-infinitive",
    examples:[{en:"It is essential that every stakeholder be consulted.",es:"Es esencial que todo interesado sea consultado."}],
    notes:["Standard in formal academic/business writing."],
    mistakes:[]
  },
  "Garden-path constructions":{
    rule:"Sentences that initially mislead the reader before clarifying.",
    structure:"Syntactically ambiguous leading phrase followed by disambiguating continuation",
    examples:[{en:"The manager blamed for the losses resigned.",es:"El gerente culpado por las pérdidas renunció."}],
    notes:["Avoid in clear business communication; recognize in legal/journalistic prose."],
    mistakes:[]
  },
  "Genre-specific grammar conventions":{
    rule:"Different business genres have distinct grammatical conventions.",
    structure:"Press release: 3rd person, present-tense headlines | Legal: passive, Latinate | Earnings call: hedged, numerate",
    examples:[{en:"'Cohasset reports record Q4 revenue' (press release headline).",es:"'Cohasset reporta ingresos récord en el Q4' (titular de nota de prensa)."}],
    notes:["Know the genre, use the right conventions."],
    mistakes:[]
  }
});

// ===== ADDITIONAL VOCABULARY =====
Object.assign(BE_VOCAB_DB, {
  // A1 remaining
  "Days/months/time":[
    {en:"Monday",ipa:"/ˈmʌn.deɪ/",es:"lunes",def:"the first workday",ex:"The meeting is on Monday."},
    {en:"weekend",ipa:"/ˌwiːkˈend/",es:"fin de semana",def:"Saturday and Sunday",ex:"I don't work on weekends."},
    {en:"quarter",ipa:"/ˈkwɔː.tər/",es:"trimestre",def:"three-month period",ex:"Q1 covers January to March."},
    {en:"deadline",ipa:"/ˈded.laɪn/",es:"fecha límite",def:"the latest time to finish",ex:"The deadline is Friday."},
    {en:"schedule",ipa:"/ˈʃed.juːl/",es:"horario",def:"plan of times",ex:"Check the schedule for tomorrow."},
    {en:"appointment",ipa:"/əˈpɔɪnt.mənt/",es:"cita",def:"arranged meeting time",ex:"I have an appointment at 3 PM."}
  ],
  "Countries & nationalities":[
    {en:"Peru / Peruvian",ipa:"/pəˈruː/",es:"Perú / peruano",def:"South American country / citizen",ex:"Our Peruvian office is in Lima."},
    {en:"headquarters",ipa:"/ˈhed.kwɔː.təz/",es:"sede central",def:"main office",ex:"Our headquarters is in New York."},
    {en:"branch",ipa:"/brɑːntʃ/",es:"sucursal",def:"local office",ex:"We opened a branch in Bogotá."},
    {en:"overseas",ipa:"/ˌəʊ.vəˈsiːz/",es:"en el extranjero",def:"in foreign countries",ex:"She works for our overseas clients."},
    {en:"multinational",ipa:"/ˌmʌl.tiˈnæʃ.ən.əl/",es:"multinacional",def:"operating in many countries",ex:"We are a multinational corporation."},
    {en:"local",ipa:"/ˈləʊ.kəl/",es:"local",def:"from the immediate area",ex:"We hire local talent."}
  ],
  "Food & drink (business meals)":[
    {en:"lunch meeting",ipa:"/lʌntʃ ˈmiː.tɪŋ/",es:"reunión de almuerzo",def:"meeting over a meal",ex:"Let's have a lunch meeting with the client."},
    {en:"reservation",ipa:"/ˌrez.əˈveɪ.ʃən/",es:"reserva",def:"booked space at a restaurant",ex:"I made a reservation at 1 PM."},
    {en:"menu",ipa:"/ˈmen.juː/",es:"menú",def:"list of food options",ex:"Could we see the menu, please?"},
    {en:"waiter",ipa:"/ˈweɪ.tər/",es:"mesero(a)",def:"person who serves food",ex:"The waiter brought the bill."},
    {en:"bill",ipa:"/bɪl/",es:"cuenta",def:"statement of amount owed",ex:"Could we have the bill, please?"},
    {en:"tip",ipa:"/tɪp/",es:"propina",def:"extra payment for service",ex:"A 15% tip is standard."}
  ],
  "Travel basics":[
    {en:"flight",ipa:"/flaɪt/",es:"vuelo",def:"a journey by plane",ex:"My flight leaves at 9 AM."},
    {en:"boarding pass",ipa:"/ˈbɔː.dɪŋ pɑːs/",es:"pase de abordar",def:"ticket to enter the plane",ex:"Please show your boarding pass."},
    {en:"luggage",ipa:"/ˈlʌɡ.ɪdʒ/",es:"equipaje",def:"bags you travel with",ex:"My luggage is heavy."},
    {en:"check-in",ipa:"/ˈtʃek.ɪn/",es:"registro",def:"registering at an airport or hotel",ex:"Check-in closes 40 minutes before the flight."},
    {en:"layover",ipa:"/ˈleɪˌəʊ.vər/",es:"escala",def:"brief stop between flights",ex:"We have a 2-hour layover in Madrid."},
    {en:"jet lag",ipa:"/ˈdʒet.læɡ/",es:"jet lag, desfase horario",def:"fatigue from time zones",ex:"I always get jet lag flying to Asia."}
  ],
  "Technology basics":[
    {en:"software",ipa:"/ˈsɒft.weər/",es:"software",def:"computer programs",ex:"We use CRM software."},
    {en:"password",ipa:"/ˈpɑːs.wɜːd/",es:"contraseña",def:"secret login code",ex:"Change your password every 90 days."},
    {en:"download",ipa:"/ˌdaʊnˈləʊd/",es:"descargar",def:"get a file from the internet",ex:"Download the report attachment."},
    {en:"update",ipa:"/ˌʌpˈdeɪt/",es:"actualizar",def:"install new version",ex:"Please update your antivirus."},
    {en:"backup",ipa:"/ˈbæk.ʌp/",es:"respaldo",def:"copy of data for safety",ex:"Make a backup before migrating."},
    {en:"server",ipa:"/ˈsɜː.vər/",es:"servidor",def:"main computer storing data",ex:"The server is down again."}
  ],
  "Describing people":[
    {en:"reliable",ipa:"/rɪˈlaɪ.ə.bəl/",es:"confiable",def:"can be trusted",ex:"She is very reliable with deadlines."},
    {en:"proactive",ipa:"/ˌprəʊˈæk.tɪv/",es:"proactivo",def:"taking initiative",ex:"He's a proactive team leader."},
    {en:"organized",ipa:"/ˈɔː.ɡən.aɪzd/",es:"organizado",def:"methodical",ex:"Our CFO is extremely organized."},
    {en:"hardworking",ipa:"/ˌhɑːdˈwɜː.kɪŋ/",es:"trabajador",def:"puts in effort",ex:"She's one of our hardworking interns."},
    {en:"creative",ipa:"/kriˈeɪ.tɪv/",es:"creativo",def:"inventive",ex:"The marketing team is very creative."},
    {en:"detail-oriented",ipa:"/ˈdiː.teɪl ˈɔː.ri.en.tɪd/",es:"detallista",def:"attentive to specifics",ex:"Auditors need to be detail-oriented."}
  ],
  "Giving directions":[
    {en:"turn left/right",ipa:"/tɜːn left|raɪt/",es:"girar a la izquierda/derecha",def:"change direction",ex:"Turn left at the reception."},
    {en:"straight ahead",ipa:"/streɪt əˈhed/",es:"todo recto",def:"continue forward",ex:"Go straight ahead and you'll see the meeting room."},
    {en:"next to",ipa:"/nekst tuː/",es:"al lado de",def:"beside",ex:"My office is next to the kitchen."},
    {en:"across from",ipa:"/əˈkrɒs frɒm/",es:"enfrente de",def:"opposite to",ex:"Our building is across from the bank."},
    {en:"on the corner",ipa:"/ɒn ðə ˈkɔː.nər/",es:"en la esquina",def:"at the intersection",ex:"The office is on the corner of Main and 5th."},
    {en:"floor",ipa:"/flɔːr/",es:"piso",def:"level of a building",ex:"Our office is on the 12th floor."}
  ],
  "Daily routines":[
    {en:"commute",ipa:"/kəˈmjuːt/",es:"trayecto diario",def:"travel to and from work",ex:"My commute takes 45 minutes."},
    {en:"overtime",ipa:"/ˈəʊ.və.taɪm/",es:"horas extra",def:"extra working hours",ex:"We did overtime to meet the deadline."},
    {en:"lunch break",ipa:"/lʌntʃ breɪk/",es:"pausa para el almuerzo",def:"midday rest",ex:"I take a one-hour lunch break."},
    {en:"clock in/out",ipa:"/klɒk ɪn|aʊt/",es:"fichar entrada/salida",def:"register start/end of work",ex:"Clock in before 8 AM."},
    {en:"shift",ipa:"/ʃɪft/",es:"turno",def:"scheduled work period",ex:"I work the night shift."},
    {en:"remote",ipa:"/rɪˈməʊt/",es:"remoto",def:"working from home",ex:"Our team is fully remote."}
  ],
  "Company types":[
    {en:"startup",ipa:"/ˈstɑːt.ʌp/",es:"empresa emergente",def:"new fast-growing company",ex:"He founded a tech startup."},
    {en:"corporation",ipa:"/ˌkɔː.pəˈreɪ.ʃən/",es:"corporación",def:"large formal company",ex:"We work with Fortune 500 corporations."},
    {en:"SME",ipa:"/ˌes.emˈiː/",es:"PYME",def:"small/medium enterprise",ex:"SMEs drive the economy."},
    {en:"NGO",ipa:"/ˌen.dʒiːˈəʊ/",es:"ONG",def:"non-governmental organization",ex:"The NGO supports education."},
    {en:"public",ipa:"/ˈpʌb.lɪk/",es:"cotizada en bolsa",def:"traded on stock market",ex:"We went public in 2020."},
    {en:"private",ipa:"/ˈpraɪ.vət/",es:"privada",def:"not publicly traded",ex:"It's a privately held company."}
  ],
  "Business verbs (make/do/take/get)":[
    {en:"make a deal",ipa:"/meɪk ə diːl/",es:"cerrar un trato",def:"reach an agreement",ex:"We made a deal worth $2M."},
    {en:"do business",ipa:"/duː ˈbɪz.nɪs/",es:"hacer negocios",def:"conduct commercial activity",ex:"We do business in 15 countries."},
    {en:"take over",ipa:"/teɪk ˈəʊ.vər/",es:"tomar el control",def:"assume control",ex:"The CFO took over the project."},
    {en:"get approval",ipa:"/ɡet əˈpruː.vəl/",es:"obtener aprobación",def:"receive authorization",ex:"We got approval from the board."},
    {en:"make an offer",ipa:"/meɪk ən ˈɒf.ər/",es:"hacer una oferta",def:"propose terms",ex:"They made us a generous offer."},
    {en:"do a favor",ipa:"/duː ə ˈfeɪ.vər/",es:"hacer un favor",def:"help someone",ex:"Could you do me a favor?"}
  ],
  // A2 remaining
  "Company types & structure":[
    {en:"hierarchy",ipa:"/ˈhaɪə.rɑːr.ki/",es:"jerarquía",def:"levels of authority",ex:"Our hierarchy is flat."},
    {en:"subsidiary",ipa:"/səbˈsɪd.i.ə.ri/",es:"filial",def:"owned by another company",ex:"They opened a subsidiary in Chile."},
    {en:"division",ipa:"/dɪˈvɪʒ.ən/",es:"división",def:"large internal unit",ex:"Our Asian division is growing fast."},
    {en:"board of directors",ipa:"/bɔːd əv daɪˈrek.təz/",es:"junta directiva",def:"governing body",ex:"The board approved the merger."},
    {en:"shareholder",ipa:"/ˈʃeəˌhəʊl.dər/",es:"accionista",def:"owner of shares",ex:"Shareholders vote on key decisions."},
    {en:"founder",ipa:"/ˈfaʊn.dər/",es:"fundador(a)",def:"person who started a company",ex:"The founder stepped down as CEO."}
  ],
  "Ideas & innovation":[
    {en:"brainstorm",ipa:"/ˈbreɪn.stɔːm/",es:"lluvia de ideas",def:"group idea-generation",ex:"Let's brainstorm solutions."},
    {en:"prototype",ipa:"/ˈprəʊ.tə.taɪp/",es:"prototipo",def:"early model",ex:"The prototype impressed the investors."},
    {en:"pilot",ipa:"/ˈpaɪ.lət/",es:"piloto, prueba",def:"initial test",ex:"We're running a pilot in Peru."},
    {en:"launch",ipa:"/lɔːntʃ/",es:"lanzamiento",def:"product introduction",ex:"The launch date is set for June."},
    {en:"R&D",ipa:"/ˌɑːr ənd ˈdiː/",es:"I+D",def:"research and development",ex:"R&D spending grew by 20%."},
    {en:"patent",ipa:"/ˈpeɪ.tənt/",es:"patente",def:"legal right to an invention",ex:"We filed a patent last month."}
  ],
  "Stress & wellbeing":[
    {en:"burnout",ipa:"/ˈbɜːn.aʊt/",es:"agotamiento",def:"exhaustion from overwork",ex:"We need to prevent burnout in the team."},
    {en:"wellness",ipa:"/ˈwel.nəs/",es:"bienestar",def:"general good health",ex:"We offer wellness programs."},
    {en:"work-life balance",ipa:"/wɜːk laɪf ˈbæl.əns/",es:"equilibrio vida-trabajo",def:"healthy mix of work and personal life",ex:"Our policies protect work-life balance."},
    {en:"mental health",ipa:"/ˈmen.təl helθ/",es:"salud mental",def:"psychological wellbeing",ex:"Mental health is a company priority."},
    {en:"flexible hours",ipa:"/ˈflek.sə.bəl aʊəz/",es:"horario flexible",def:"adjustable schedule",ex:"We offer flexible hours."},
    {en:"time off",ipa:"/taɪm ɒf/",es:"tiempo libre",def:"leave from work",ex:"Take some time off to recharge."}
  ],
  "Marketing basics":[
    {en:"campaign",ipa:"/kæmˈpeɪn/",es:"campaña",def:"coordinated marketing effort",ex:"Our Q4 campaign goes live in October."},
    {en:"customer journey",ipa:"/ˈkʌs.tə.mər ˈdʒɜː.ni/",es:"recorrido del cliente",def:"customer experience path",ex:"We mapped the full customer journey."},
    {en:"lead",ipa:"/liːd/",es:"cliente potencial",def:"potential customer",ex:"We generated 300 leads last week."},
    {en:"conversion",ipa:"/kənˈvɜː.ʃən/",es:"conversión",def:"turning a prospect into a customer",ex:"Our conversion rate is 8%."},
    {en:"channel",ipa:"/ˈtʃæn.əl/",es:"canal",def:"distribution path",ex:"We sell through 5 channels."},
    {en:"ROI",ipa:"/ˌɑːr.əʊˈaɪ/",es:"retorno de inversión",def:"return on investment",ex:"The ROI of this campaign was 250%."}
  ],
  "Email phrases":[
    {en:"Dear Mr/Ms...",ipa:"/dɪər/",es:"Estimado/a señor/a",def:"formal greeting",ex:"Dear Ms Santos,"},
    {en:"I am writing to...",ipa:"",es:"Le escribo para...",def:"formal opening",ex:"I am writing to request a meeting."},
    {en:"Please find attached",ipa:"",es:"Adjunto encontrará",def:"formal attachment phrase",ex:"Please find attached the proposal."},
    {en:"I look forward to hearing from you",ipa:"",es:"Quedo a la espera de su respuesta",def:"formal closing",ex:"I look forward to hearing from you soon."},
    {en:"Best regards",ipa:"",es:"Saludos cordiales",def:"professional sign-off",ex:"Best regards, Ana."},
    {en:"cc / bcc",ipa:"/ˌsiːˈsiː/",es:"con copia / con copia oculta",def:"additional recipients",ex:"Please cc me on that email."}
  ],
  "Meeting phrases":[
    {en:"Let's get started",ipa:"",es:"Empecemos",def:"opening a meeting",ex:"Let's get started — item one on the agenda."},
    {en:"Can I add something?",ipa:"",es:"¿Puedo añadir algo?",def:"requesting floor time",ex:"Can I add something to that point?"},
    {en:"I see your point, but...",ipa:"",es:"Entiendo tu punto, pero...",def:"diplomatic disagreement",ex:"I see your point, but the data suggests otherwise."},
    {en:"Let's move on",ipa:"",es:"Sigamos adelante",def:"change topics",ex:"Let's move on to the next item."},
    {en:"Could you elaborate?",ipa:"",es:"¿Podrías profundizar?",def:"request more detail",ex:"Could you elaborate on the budget concerns?"},
    {en:"action item",ipa:"/ˈæk.ʃən ˈaɪ.təm/",es:"punto de acción",def:"task assigned during a meeting",ex:"That's an action item for Sarah."}
  ],
  // B1 remaining topics
  "Business travel (advanced)":[
    {en:"itinerary",ipa:"/aɪˈtɪn.ər.ər.i/",es:"itinerario",def:"detailed travel plan",ex:"Your itinerary has been sent."},
    {en:"per diem",ipa:"/pɜː ˈdiː.em/",es:"viáticos diarios",def:"daily travel allowance",ex:"The per diem covers meals."},
    {en:"frequent flyer",ipa:"/ˈfriː.kwənt ˈflaɪ.ər/",es:"viajero frecuente",def:"loyalty program member",ex:"I'm a Platinum frequent flyer."},
    {en:"visa",ipa:"/ˈviː.zə/",es:"visa",def:"travel permission document",ex:"Apply for your visa 6 weeks ahead."},
    {en:"expense report",ipa:"/ɪkˈspens rɪˈpɔːt/",es:"informe de gastos",def:"travel cost summary",ex:"Submit your expense report by Friday."},
    {en:"corporate discount",ipa:"/ˈkɔːr.pər.ət ˈdɪs.kaʊnt/",es:"descuento corporativo",def:"business rate",ex:"We have a corporate discount with Marriott."}
  ],
  "Organizational structure":[
    {en:"org chart",ipa:"/ɔːɡ tʃɑːt/",es:"organigrama",def:"diagram of reporting lines",ex:"Here is our updated org chart."},
    {en:"reporting line",ipa:"/rɪˈpɔː.tɪŋ laɪn/",es:"línea de reporte",def:"who reports to whom",ex:"The reporting line is to the COO."},
    {en:"matrix",ipa:"/ˈmeɪ.trɪks/",es:"matricial",def:"multi-axis reporting",ex:"We have a matrix structure."},
    {en:"silo",ipa:"/ˈsaɪ.ləʊ/",es:"silo",def:"isolated team/department",ex:"We need to break down silos."},
    {en:"cross-functional",ipa:"/krɒs ˈfʌŋk.ʃən.əl/",es:"multidisciplinario",def:"team across departments",ex:"Form a cross-functional task force."},
    {en:"restructure",ipa:"/ˌriːˈstrʌk.tʃər/",es:"reestructurar",def:"reorganize",ex:"The company will restructure in Q3."}
  ],
  "Change management":[
    {en:"transition",ipa:"/trænˈzɪʃ.ən/",es:"transición",def:"move from one state to another",ex:"The transition will take 6 months."},
    {en:"stakeholder buy-in",ipa:"/ˈsteɪk.həʊl.dər ˈbaɪ.ɪn/",es:"apoyo de interesados",def:"stakeholder support",ex:"We need stakeholder buy-in."},
    {en:"resistance",ipa:"/rɪˈzɪs.təns/",es:"resistencia",def:"opposition to change",ex:"Employee resistance is common."},
    {en:"rollout",ipa:"/ˈrəʊl.aʊt/",es:"implementación",def:"launching a change",ex:"The rollout is scheduled for May."},
    {en:"adoption",ipa:"/əˈdɒp.ʃən/",es:"adopción",def:"uptake of new system",ex:"User adoption is 80%."},
    {en:"change champion",ipa:"/tʃeɪndʒ ˈtʃæm.pi.ən/",es:"líder del cambio",def:"internal advocate",ex:"We identified 10 change champions."}
  ],
  "Advertising & media":[
    {en:"advertisement",ipa:"/ədˈvɜː.tɪs.mənt/",es:"anuncio",def:"paid promotion",ex:"The advertisement ran for 6 weeks."},
    {en:"social media",ipa:"/ˈsəʊ.ʃəl ˈmiː.di.ə/",es:"redes sociales",def:"digital platforms",ex:"Social media drives 40% of traffic."},
    {en:"influencer",ipa:"/ˈɪn.flu.ən.sər/",es:"influenciador(a)",def:"social media figure",ex:"We partnered with three influencers."},
    {en:"targeting",ipa:"/ˈtɑː.ɡɪ.tɪŋ/",es:"segmentación",def:"audience selection",ex:"Our targeting is very precise."},
    {en:"engagement",ipa:"/ɪnˈɡeɪdʒ.mənt/",es:"interacción",def:"audience interaction",ex:"Engagement rates are up 25%."},
    {en:"viral",ipa:"/ˈvaɪə.rəl/",es:"viral",def:"rapidly spreading",ex:"The video went viral."}
  ],
  "Money & finance basics":[
    {en:"cash flow",ipa:"/kæʃ fləʊ/",es:"flujo de caja",def:"money in vs out",ex:"Cash flow is tight this quarter."},
    {en:"loan",ipa:"/ləʊn/",es:"préstamo",def:"borrowed money",ex:"We took a loan to finance the expansion."},
    {en:"interest rate",ipa:"/ˈɪn.trəst reɪt/",es:"tasa de interés",def:"cost of borrowing",ex:"Interest rates are rising."},
    {en:"debt",ipa:"/det/",es:"deuda",def:"money owed",ex:"We reduced our debt by 30%."},
    {en:"equity",ipa:"/ˈek.wɪ.ti/",es:"capital propio",def:"ownership value",ex:"He has 15% equity in the company."},
    {en:"dividend",ipa:"/ˈdɪv.ɪ.dend/",es:"dividendo",def:"profit share to shareholders",ex:"The board approved a $2 dividend."}
  ],
  "Cross-cultural business":[
    {en:"cultural awareness",ipa:"/ˈkʌl.tʃər.əl əˈweə.nəs/",es:"conciencia cultural",def:"understanding other cultures",ex:"Cultural awareness is critical."},
    {en:"etiquette",ipa:"/ˈet.ɪ.ket/",es:"etiqueta",def:"cultural manners",ex:"Business etiquette varies by country."},
    {en:"time zone",ipa:"/taɪm zəʊn/",es:"zona horaria",def:"geographic time division",ex:"We operate across 6 time zones."},
    {en:"miscommunication",ipa:"/ˌmɪs.kə.mjuː.nɪˈkeɪ.ʃən/",es:"mala comunicación",def:"misunderstanding",ex:"Miscommunication caused the delay."},
    {en:"hierarchy-sensitive",ipa:"",es:"sensible a jerarquía",def:"aware of rank",ex:"Japan is hierarchy-sensitive."},
    {en:"localization",ipa:"/ˌləʊ.kəl.aɪˈzeɪ.ʃən/",es:"localización",def:"adapting to local market",ex:"Localization boosted our Latin sales."}
  ],
  "International markets":[
    {en:"emerging market",ipa:"/ɪˈmɜː.dʒɪŋ ˈmɑː.kɪt/",es:"mercado emergente",def:"growing economy",ex:"Peru is an emerging market."},
    {en:"market share",ipa:"/ˈmɑː.kɪt ʃeər/",es:"cuota de mercado",def:"% of total sales",ex:"We hold 22% market share."},
    {en:"tariff",ipa:"/ˈtær.ɪf/",es:"arancel",def:"import tax",ex:"New tariffs impact imports."},
    {en:"trade agreement",ipa:"/treɪd əˈɡriː.mənt/",es:"acuerdo comercial",def:"cross-border trade deal",ex:"The trade agreement reduces tariffs."},
    {en:"currency exchange",ipa:"/ˈkʌr.ən.si ɪksˈtʃeɪndʒ/",es:"tipo de cambio",def:"money conversion",ex:"Currency exchange hit our margins."},
    {en:"FDI",ipa:"/ˌef.diːˈaɪ/",es:"IED",def:"foreign direct investment",ex:"FDI in Peru grew 15%."}
  ],
  "Business ethics":[
    {en:"integrity",ipa:"/ɪnˈteɡ.rə.ti/",es:"integridad",def:"moral uprightness",ex:"Integrity is a core value."},
    {en:"conflict of interest",ipa:"/ˈkɒn.flɪkt əv ˈɪn.trəst/",es:"conflicto de interés",def:"competing loyalties",ex:"Disclose any conflict of interest."},
    {en:"compliance",ipa:"/kəmˈplaɪ.əns/",es:"cumplimiento",def:"following rules",ex:"Compliance reports are due monthly."},
    {en:"whistleblower",ipa:"/ˈwɪs.əlˌbləʊ.ər/",es:"denunciante",def:"person who reports wrongdoing",ex:"The whistleblower is protected by law."},
    {en:"bribery",ipa:"/ˈbraɪ.bər.i/",es:"soborno",def:"illegal payment",ex:"Bribery is strictly prohibited."},
    {en:"code of conduct",ipa:"/kəʊd əv ˈkɒn.dʌkt/",es:"código de conducta",def:"ethical rules",ex:"Every employee signs the code of conduct."}
  ],
  "Leadership basics":[
    {en:"vision",ipa:"/ˈvɪʒ.ən/",es:"visión",def:"long-term direction",ex:"The CEO shared her vision for 2030."},
    {en:"delegate",ipa:"/ˈdel.ɪ.ɡeɪt/",es:"delegar",def:"assign authority",ex:"Good leaders know how to delegate."},
    {en:"motivate",ipa:"/ˈməʊ.tɪ.veɪt/",es:"motivar",def:"inspire action",ex:"She motivates the team with clarity."},
    {en:"empower",ipa:"/ɪmˈpaʊ.ər/",es:"empoderar",def:"give authority",ex:"We empower managers to decide."},
    {en:"mentor",ipa:"/ˈmen.tɔːr/",es:"mentor",def:"experienced advisor",ex:"Everyone has an assigned mentor."},
    {en:"accountability",ipa:"/əˌkaʊn.təˈbɪl.ə.ti/",es:"responsabilidad",def:"answerability for results",ex:"Accountability drives performance."}
  ],
  "Competition & strategy":[
    {en:"competitive advantage",ipa:"/kəmˈpet.ɪ.tɪv ədˈvɑːn.tɪdʒ/",es:"ventaja competitiva",def:"edge over rivals",ex:"Our technology is our competitive advantage."},
    {en:"disrupt",ipa:"/dɪsˈrʌpt/",es:"disrumpir",def:"radically change",ex:"Netflix disrupted television."},
    {en:"moat",ipa:"/məʊt/",es:"barrera defensiva",def:"defensive barrier",ex:"Network effects build a moat."},
    {en:"benchmarking",ipa:"/ˈbentʃ.mɑː.kɪŋ/",es:"benchmarking",def:"compare vs best-in-class",ex:"Benchmarking reveals gaps."},
    {en:"SWOT analysis",ipa:"/swɒt əˈnæl.ə.sɪs/",es:"análisis FODA",def:"strengths, weaknesses, opportunities, threats",ex:"Run a SWOT before planning."},
    {en:"differentiation",ipa:"/ˌdɪf.ə.ren.ʃiˈeɪ.ʃən/",es:"diferenciación",def:"standing out",ex:"Differentiation protects margins."}
  ],
  "Communication styles":[
    {en:"direct",ipa:"/daɪˈrekt/",es:"directo",def:"straightforward",ex:"Germans tend to be direct."},
    {en:"indirect",ipa:"/ˌɪn.daɪˈrekt/",es:"indirecto",def:"implied or hinted",ex:"Japanese communication is often indirect."},
    {en:"assertive",ipa:"/əˈsɜː.tɪv/",es:"asertivo",def:"confident and clear",ex:"Be assertive but respectful."},
    {en:"diplomatic",ipa:"/ˌdɪp.ləˈmæt.ɪk/",es:"diplomático",def:"tactful",ex:"A diplomatic approach smooths tensions."},
    {en:"active listening",ipa:"/ˈæk.tɪv ˈlɪs.ən.ɪŋ/",es:"escucha activa",def:"fully engaged listening",ex:"Active listening builds rapport."},
    {en:"feedback",ipa:"/ˈfiːd.bæk/",es:"retroalimentación",def:"evaluative response",ex:"Constructive feedback helps growth."}
  ],
  "Project management":[
    {en:"scope",ipa:"/skəʊp/",es:"alcance",def:"project boundaries",ex:"Define the scope clearly."},
    {en:"milestone",ipa:"/ˈmaɪl.stəʊn/",es:"hito",def:"key checkpoint",ex:"Phase 1 is a major milestone."},
    {en:"Gantt chart",ipa:"/ɡænt tʃɑːt/",es:"diagrama de Gantt",def:"project timeline visual",ex:"Update the Gantt chart weekly."},
    {en:"sprint",ipa:"/sprɪnt/",es:"sprint",def:"short work cycle (Agile)",ex:"Our sprints are 2 weeks."},
    {en:"backlog",ipa:"/ˈbæk.lɒɡ/",es:"lista pendiente",def:"queued work",ex:"The backlog grew this month."},
    {en:"dependencies",ipa:"/dɪˈpen.dən.siz/",es:"dependencias",def:"blocking relationships",ex:"Map the critical dependencies."}
  ],
  "Customer relationships":[
    {en:"CRM",ipa:"/ˌsiː.ɑːrˈem/",es:"CRM",def:"customer relationship management",ex:"Our CRM tracks 50,000 contacts."},
    {en:"loyalty",ipa:"/ˈlɔɪ.əl.ti/",es:"fidelización",def:"repeat commitment",ex:"Our loyalty program drives retention."},
    {en:"NPS",ipa:"/ˌen.piːˈes/",es:"NPS",def:"Net Promoter Score",ex:"Our NPS is 72."},
    {en:"churn",ipa:"/tʃɜːn/",es:"deserción",def:"customer loss",ex:"Reduce churn through better support."},
    {en:"upsell",ipa:"/ˈʌp.sel/",es:"venta adicional",def:"sell more to existing customer",ex:"The upsell opportunity is huge."},
    {en:"lifetime value",ipa:"/ˈlaɪf.taɪm ˈvæl.juː/",es:"valor de vida del cliente",def:"total revenue per customer",ex:"Lifetime value grew 30%."}
  ],
  // B2 remaining topics
  "International negotiations":[
    {en:"leverage",ipa:"/ˈliː.vər.ɪdʒ/",es:"influencia",def:"bargaining power",ex:"We have significant leverage in this deal."},
    {en:"concession",ipa:"/kənˈseʃ.ən/",es:"concesión",def:"giving ground",ex:"We made a concession on pricing."},
    {en:"deadlock",ipa:"/ˈded.lɒk/",es:"punto muerto",def:"impasse",ex:"Negotiations hit a deadlock."},
    {en:"BATNA",ipa:"/ˈbæt.nə/",es:"MAAN",def:"best alternative to a negotiated agreement",ex:"Know your BATNA before entering."},
    {en:"win-win",ipa:"/wɪn wɪn/",es:"ganar-ganar",def:"mutually beneficial",ex:"We reached a win-win outcome."},
    {en:"tentative agreement",ipa:"/ˈten.tə.tɪv əˈɡriː.mənt/",es:"acuerdo tentativo",def:"provisional deal",ex:"We have a tentative agreement pending legal review."}
  ],
  "Business reports & proposals":[
    {en:"executive summary",ipa:"/ɪɡˈzek.jə.tɪv ˈsʌm.ər.i/",es:"resumen ejecutivo",def:"1-page overview",ex:"Start with a strong executive summary."},
    {en:"findings",ipa:"/ˈfaɪn.dɪŋz/",es:"hallazgos",def:"research conclusions",ex:"The findings support a pivot."},
    {en:"recommendations",ipa:"/ˌrek.ə.menˈdeɪ.ʃənz/",es:"recomendaciones",def:"proposed actions",ex:"Our recommendations are in Section 5."},
    {en:"appendix",ipa:"/əˈpen.dɪks/",es:"anexo",def:"supplementary material",ex:"See Appendix B for data."},
    {en:"executable",ipa:"/ˈek.sə.kju.tə.bəl/",es:"ejecutable",def:"implementable",ex:"These recommendations are fully executable."},
    {en:"deliverables",ipa:"/dɪˈlɪv.ər.ə.bəlz/",es:"entregables",def:"items to be produced",ex:"Q1 deliverables are on track."}
  ],
  "International team management":[
    {en:"remote team",ipa:"/rɪˈməʊt tiːm/",es:"equipo remoto",def:"distributed workforce",ex:"Managing a remote team requires structure."},
    {en:"asynchronous",ipa:"/eɪˈsɪŋ.krə.nəs/",es:"asíncrono",def:"not in real time",ex:"We communicate asynchronously across time zones."},
    {en:"inclusion",ipa:"/ɪnˈkluː.ʒən/",es:"inclusión",def:"welcoming diversity",ex:"Inclusion practices boost innovation."},
    {en:"time zone coordination",ipa:"",es:"coordinación de zonas horarias",def:"scheduling across regions",ex:"Time zone coordination is a constant challenge."},
    {en:"team charter",ipa:"/tiːm ˈtʃɑː.tər/",es:"carta del equipo",def:"team norms document",ex:"We drafted a team charter."},
    {en:"escalation path",ipa:"/ˌes.kəˈleɪ.ʃən pɑːθ/",es:"ruta de escalamiento",def:"issue-resolution hierarchy",ex:"Follow the escalation path for blockers."}
  ],
  "Market analysis & research":[
    {en:"market research",ipa:"/ˈmɑː.kɪt rɪˈsɜːtʃ/",es:"estudio de mercado",def:"data gathering on customers",ex:"Market research revealed a new segment."},
    {en:"focus group",ipa:"/ˈfəʊ.kəs ɡruːp/",es:"grupo focal",def:"qualitative discussion group",ex:"The focus group validated the concept."},
    {en:"segmentation",ipa:"/ˌseɡ.mənˈteɪ.ʃən/",es:"segmentación",def:"dividing the market",ex:"Segmentation uncovered 4 personas."},
    {en:"addressable market",ipa:"/əˈdres.ə.bəl ˈmɑː.kɪt/",es:"mercado direccionable",def:"reachable customers",ex:"Our addressable market is $2B."},
    {en:"market penetration",ipa:"",es:"penetración de mercado",def:"% of market captured",ex:"Market penetration is 18%."},
    {en:"demand forecasting",ipa:"",es:"proyección de demanda",def:"predicting future sales",ex:"Demand forecasting uses ML models."}
  ],
  "Brand management & strategy":[
    {en:"brand equity",ipa:"/brænd ˈek.wɪ.ti/",es:"valor de marca",def:"brand-derived value",ex:"Apple has enormous brand equity."},
    {en:"brand voice",ipa:"/brænd vɔɪs/",es:"voz de marca",def:"brand personality in communication",ex:"Our brand voice is friendly yet professional."},
    {en:"brand extension",ipa:"",es:"extensión de marca",def:"new product under existing brand",ex:"The brand extension into wellness succeeded."},
    {en:"rebranding",ipa:"/riːˈbrænd.ɪŋ/",es:"cambio de marca",def:"renewing brand identity",ex:"The rebranding cost $5M."},
    {en:"brand loyalty",ipa:"",es:"fidelidad a la marca",def:"repeat customer commitment",ex:"Brand loyalty is our moat."},
    {en:"trademark",ipa:"/ˈtreɪd.mɑːk/",es:"marca registrada",def:"legally protected brand mark",ex:"Register the trademark globally."}
  ],
  "Supply chain & logistics":[
    {en:"supply chain",ipa:"/səˈplaɪ tʃeɪn/",es:"cadena de suministro",def:"product sourcing network",ex:"Supply chain disruptions cost us $10M."},
    {en:"inventory",ipa:"/ˈɪn.vən.tər.i/",es:"inventario",def:"stock on hand",ex:"Inventory turns are up 15%."},
    {en:"just-in-time",ipa:"",es:"justo a tiempo",def:"lean delivery",ex:"Just-in-time reduces holding costs."},
    {en:"warehouse",ipa:"/ˈweə.haʊs/",es:"almacén",def:"storage facility",ex:"We opened a new warehouse."},
    {en:"last mile",ipa:"/lɑːst maɪl/",es:"última milla",def:"final delivery segment",ex:"Last-mile delivery is the costliest."},
    {en:"procurement",ipa:"/prəˈkjʊə.mənt/",es:"abastecimiento",def:"purchasing",ex:"Procurement negotiated better terms."}
  ],
  "Risk assessment & management":[
    {en:"risk appetite",ipa:"/rɪsk ˈæp.ə.taɪt/",es:"apetito de riesgo",def:"tolerance for risk",ex:"Our risk appetite is moderate."},
    {en:"mitigation",ipa:"/ˌmɪt.ɪˈɡeɪ.ʃən/",es:"mitigación",def:"reducing risk impact",ex:"Mitigation plans are in place."},
    {en:"risk matrix",ipa:"/rɪsk ˈmeɪ.trɪks/",es:"matriz de riesgo",def:"likelihood vs impact grid",ex:"Update the risk matrix quarterly."},
    {en:"contingency",ipa:"/kənˈtɪn.dʒən.si/",es:"contingencia",def:"backup plan",ex:"Our contingency kicks in at 20% loss."},
    {en:"black swan",ipa:"/blæk swɒn/",es:"cisne negro",def:"rare extreme event",ex:"COVID was a black-swan event."},
    {en:"hedging",ipa:"/ˈhedʒ.ɪŋ/",es:"cobertura",def:"offsetting risk",ex:"We use hedging to manage currency exposure."}
  ],
  "Corporate social responsibility":[
    {en:"CSR",ipa:"/ˌsiː.esˈɑːr/",es:"RSE",def:"corporate social responsibility",ex:"Our CSR report is public."},
    {en:"stewardship",ipa:"/ˈstjuː.əd.ʃɪp/",es:"custodia, gestión responsable",def:"responsible care",ex:"Environmental stewardship is a priority."},
    {en:"philanthropy",ipa:"/fɪˈlæn.θrə.pi/",es:"filantropía",def:"charitable giving",ex:"Our philanthropy focuses on education."},
    {en:"sustainability",ipa:"/səˌsteɪ.nəˈbɪl.ə.ti/",es:"sostenibilidad",def:"long-term viability",ex:"Sustainability drives our strategy."},
    {en:"community impact",ipa:"",es:"impacto comunitario",def:"local effects",ex:"Measure community impact."},
    {en:"B Corp",ipa:"/biː kɔːp/",es:"empresa B",def:"social-impact certified business",ex:"We became a B Corp in 2022."}
  ],
  "Data-driven decision making":[
    {en:"dashboard",ipa:"/ˈdæʃ.bɔːd/",es:"tablero",def:"visualization panel",ex:"Check the dashboard for real-time KPIs."},
    {en:"insight",ipa:"/ˈɪn.saɪt/",es:"perspectiva, hallazgo",def:"analytical discovery",ex:"The insight reshaped our strategy."},
    {en:"A/B test",ipa:"/ˌeɪ biː test/",es:"prueba A/B",def:"controlled experiment",ex:"A/B tests guide all launches."},
    {en:"cohort analysis",ipa:"/ˈkəʊ.hɔːt əˈnæl.ə.sɪs/",es:"análisis de cohortes",def:"group-over-time analysis",ex:"Cohort analysis revealed churn patterns."},
    {en:"correlation",ipa:"/ˌkɒr.əˈleɪ.ʃən/",es:"correlación",def:"statistical association",ex:"Correlation is not causation."},
    {en:"predictive model",ipa:"",es:"modelo predictivo",def:"forecasting algorithm",ex:"Our predictive model has 85% accuracy."}
  ],
  "Stakeholder management":[
    {en:"investor relations",ipa:"",es:"relaciones con inversionistas",def:"communication with shareholders",ex:"Investor relations handles earnings calls."},
    {en:"regulatory bodies",ipa:"",es:"organismos reguladores",def:"government oversight agencies",ex:"Regulatory bodies scrutinize M&A."},
    {en:"influence map",ipa:"",es:"mapa de influencia",def:"who influences whom",ex:"Build an influence map before negotiating."},
    {en:"engagement plan",ipa:"",es:"plan de interacción",def:"stakeholder outreach plan",ex:"Our engagement plan targets 50 stakeholders."},
    {en:"materiality",ipa:"/məˌtɪə.riˈæl.ə.ti/",es:"materialidad",def:"relevance to stakeholders",ex:"Materiality assessment guides ESG reporting."},
    {en:"alignment",ipa:"/əˈlaɪn.mənt/",es:"alineación",def:"shared direction",ex:"Strategic alignment is critical."}
  ],
  "Contract & legal language":[
    {en:"clause",ipa:"/klɔːz/",es:"cláusula",def:"contract provision",ex:"Review Clause 12.3 carefully."},
    {en:"non-disclosure agreement (NDA)",ipa:"",es:"acuerdo de confidencialidad",def:"secrecy contract",ex:"Sign the NDA before discussions."},
    {en:"indemnity",ipa:"/ɪnˈdem.nə.ti/",es:"indemnización",def:"protection from loss",ex:"The indemnity clause caps liability."},
    {en:"force majeure",ipa:"/ˌfɔːs ˈmæʒ.ɜːr/",es:"fuerza mayor",def:"unforeseeable circumstances",ex:"COVID triggered force majeure clauses."},
    {en:"termination",ipa:"/ˌtɜː.mɪˈneɪ.ʃən/",es:"rescisión",def:"contract ending",ex:"The termination clause requires 90 days' notice."},
    {en:"counterparty",ipa:"",es:"contraparte",def:"other party to a contract",ex:"Verify the counterparty's credit."}
  ],
  "Mergers & acquisitions basics":[
    {en:"merger",ipa:"/ˈmɜː.dʒər/",es:"fusión",def:"combining companies",ex:"The merger creates a $10B company."},
    {en:"acquisition",ipa:"/ˌæk.wɪˈzɪʃ.ən/",es:"adquisición",def:"buying another company",ex:"The acquisition closes in Q2."},
    {en:"due diligence",ipa:"/djuː ˈdɪl.ɪ.dʒəns/",es:"debida diligencia",def:"investigation before deal",ex:"Due diligence takes 60 days."},
    {en:"valuation",ipa:"/ˌvæl.juˈeɪ.ʃən/",es:"valuación",def:"estimated worth",ex:"The valuation is $500M."},
    {en:"synergy",ipa:"/ˈsɪn.ə.dʒi/",es:"sinergia",def:"combined benefit",ex:"Expected synergies are $50M annually."},
    {en:"integration",ipa:"/ˌɪn.tɪˈɡreɪ.ʃən/",es:"integración",def:"post-merger consolidation",ex:"Integration planning starts day one."}
  ],
  // C1 remaining topics
  "Crisis management & PR":[
    {en:"holding statement",ipa:"",es:"declaración preliminar",def:"initial brief public comment",ex:"Issue a holding statement within one hour."},
    {en:"spokesperson",ipa:"/ˈspəʊks.pɜː.sən/",es:"portavoz",def:"official voice",ex:"The CEO is our spokesperson."},
    {en:"damage control",ipa:"",es:"control de daños",def:"mitigating PR harm",ex:"Damage control began immediately."},
    {en:"apology",ipa:"/əˈpɒl.ə.dʒi/",es:"disculpa",def:"formal regret",ex:"A sincere apology was issued."},
    {en:"press conference",ipa:"",es:"rueda de prensa",def:"media briefing",ex:"The press conference is at 5 PM."},
    {en:"reputation risk",ipa:"",es:"riesgo reputacional",def:"brand damage potential",ex:"Reputation risk ranks highest."}
  ],
  "Leadership & influence":[
    {en:"transformational",ipa:"/ˌtræns.fɔːˈmeɪ.ʃən.əl/",es:"transformacional",def:"visionary leadership style",ex:"Transformational leaders inspire change."},
    {en:"servant leadership",ipa:"",es:"liderazgo de servicio",def:"leader serves team",ex:"Servant leadership boosts engagement."},
    {en:"emotional intelligence",ipa:"",es:"inteligencia emocional",def:"social/emotional skill",ex:"Emotional intelligence is non-negotiable."},
    {en:"executive presence",ipa:"",es:"presencia ejecutiva",def:"commanding authority",ex:"She has strong executive presence."},
    {en:"succession planning",ipa:"",es:"planificación de sucesión",def:"preparing future leaders",ex:"Succession planning is a board duty."},
    {en:"thought leadership",ipa:"/θɔːt ˈliː.də.ʃɪp/",es:"liderazgo de pensamiento",def:"industry expertise positioning",ex:"Our thought leadership drives inbound deals."}
  ],
  "Market analysis (advanced)":[
    {en:"Porter's Five Forces",ipa:"",es:"cinco fuerzas de Porter",def:"industry analysis framework",ex:"We applied Porter's Five Forces."},
    {en:"TAM/SAM/SOM",ipa:"",es:"mercado total / direccionable / obtenible",def:"market sizing layers",ex:"Our TAM is $50B, SAM $10B, SOM $2B."},
    {en:"moat analysis",ipa:"",es:"análisis de foso competitivo",def:"sustainable advantage review",ex:"Moat analysis shows durable edge."},
    {en:"PESTEL",ipa:"",es:"PESTEL",def:"political, economic, social, tech, environmental, legal",ex:"PESTEL flags regulatory risk."},
    {en:"substitutes",ipa:"/ˈsʌb.stɪ.tjuːts/",es:"sustitutos",def:"alternative products",ex:"Substitutes threaten pricing power."},
    {en:"barriers to entry",ipa:"",es:"barreras de entrada",def:"obstacles for new competitors",ex:"High barriers to entry protect incumbents."}
  ],
  "Change management (advanced)":[
    {en:"Kotter's 8 steps",ipa:"",es:"8 pasos de Kotter",def:"classic change model",ex:"We followed Kotter's 8 steps."},
    {en:"change fatigue",ipa:"",es:"fatiga de cambio",def:"burnout from constant change",ex:"Change fatigue is real and measurable."},
    {en:"organizational agility",ipa:"",es:"agilidad organizacional",def:"adaptability",ex:"Agility is our key differentiator."},
    {en:"culture shift",ipa:"",es:"cambio cultural",def:"deep norm change",ex:"The culture shift took 3 years."},
    {en:"reskilling",ipa:"/ˌriːˈskɪl.ɪŋ/",es:"reentrenamiento",def:"teaching new skills",ex:"Reskilling protects jobs during automation."},
    {en:"sponsor",ipa:"/ˈspɒn.sər/",es:"patrocinador",def:"senior change backer",ex:"A strong sponsor is essential."}
  ],
  "Corporate governance":[
    {en:"board",ipa:"/bɔːd/",es:"junta",def:"governing body",ex:"The board meets quarterly."},
    {en:"independent director",ipa:"",es:"director independiente",def:"non-executive board member",ex:"Independent directors provide oversight."},
    {en:"audit committee",ipa:"",es:"comité de auditoría",def:"board finance oversight body",ex:"The audit committee reviews financials."},
    {en:"compliance officer",ipa:"",es:"responsable de cumplimiento",def:"ethics/regulation lead",ex:"The compliance officer reports to the board."},
    {en:"shareholder rights",ipa:"",es:"derechos de accionistas",def:"ownership entitlements",ex:"Shareholder rights are protected by law."},
    {en:"executive compensation",ipa:"",es:"compensación ejecutiva",def:"CEO/senior pay",ex:"Executive compensation is shareholder-approved."}
  ],
  "Regulatory compliance":[
    {en:"GDPR",ipa:"",es:"RGPD",def:"EU data protection law",ex:"GDPR compliance is global."},
    {en:"AML",ipa:"",es:"PLD",def:"anti-money laundering",ex:"AML controls are mandatory."},
    {en:"SOX",ipa:"/sɒks/",es:"Ley Sarbanes-Oxley",def:"US financial reporting law",ex:"SOX compliance shapes audit procedures."},
    {en:"KYC",ipa:"",es:"CSC",def:"know your customer",ex:"KYC prevents fraud."},
    {en:"sanctions",ipa:"/ˈsæŋk.ʃənz/",es:"sanciones",def:"restrictions on entities",ex:"Sanctions limit Russian exposure."},
    {en:"audit trail",ipa:"",es:"registro de auditoría",def:"record of actions",ex:"Maintain a complete audit trail."}
  ],
  "Innovation strategy":[
    {en:"disruptive innovation",ipa:"",es:"innovación disruptiva",def:"market-changing innovation",ex:"Disruptive innovation toppled Blockbuster."},
    {en:"incremental innovation",ipa:"",es:"innovación incremental",def:"small improvements",ex:"Incremental innovation protects core business."},
    {en:"lean startup",ipa:"",es:"startup esbelta",def:"rapid-iteration methodology",ex:"We use lean startup principles."},
    {en:"design thinking",ipa:"",es:"pensamiento de diseño",def:"user-centric problem-solving",ex:"Design thinking reframed the problem."},
    {en:"open innovation",ipa:"",es:"innovación abierta",def:"external collaboration",ex:"Open innovation accelerates R&D."},
    {en:"innovation pipeline",ipa:"",es:"pipeline de innovación",def:"stages of ideas to market",ex:"We have 40 projects in the innovation pipeline."}
  ],
  "Talent management & retention":[
    {en:"high potential",ipa:"",es:"alto potencial",def:"future leader candidate",ex:"We identify high-potential employees."},
    {en:"employee value proposition",ipa:"",es:"propuesta de valor al empleado",def:"why work here",ex:"Our EVP attracts top talent."},
    {en:"engagement survey",ipa:"",es:"encuesta de compromiso",def:"employee satisfaction measure",ex:"Our engagement survey scores rose 10%."},
    {en:"retention bonus",ipa:"",es:"bono de retención",def:"stay-incentive payment",ex:"Retention bonuses kept 95% of key talent."},
    {en:"diversity & inclusion",ipa:"",es:"diversidad e inclusión",def:"equitable workplace",ex:"Diversity & inclusion drive innovation."},
    {en:"succession pipeline",ipa:"",es:"canal de sucesión",def:"leader-ready talent bench",ex:"Our succession pipeline has 3 candidates per role."}
  ],
  "Global expansion strategy":[
    {en:"market entry",ipa:"",es:"entrada al mercado",def:"launching in a new geography",ex:"Our market entry in India was phased."},
    {en:"greenfield",ipa:"/ˈɡriːn.fiːld/",es:"inversión nueva",def:"new operations from scratch",ex:"We chose greenfield over acquisition."},
    {en:"joint venture",ipa:"/dʒɔɪnt ˈven.tʃər/",es:"empresa conjunta",def:"shared ownership entity",ex:"A joint venture with a local partner."},
    {en:"licensing",ipa:"/ˈlaɪ.sən.sɪŋ/",es:"licenciamiento",def:"granting use rights",ex:"Licensing let us enter 20 markets quickly."},
    {en:"franchising",ipa:"/ˈfræn.tʃaɪ.zɪŋ/",es:"franquicias",def:"brand replication model",ex:"Franchising scales with low capital."},
    {en:"repatriation",ipa:"",es:"repatriación",def:"bringing profits home",ex:"Profit repatriation faces tax rules."}
  ],
  "Venture capital & fundraising":[
    {en:"seed round",ipa:"",es:"ronda semilla",def:"earliest funding",ex:"We raised a $2M seed round."},
    {en:"Series A/B/C",ipa:"",es:"Serie A/B/C",def:"progressive funding rounds",ex:"Series B closed at $30M."},
    {en:"valuation",ipa:"/ˌvæl.juˈeɪ.ʃən/",es:"valoración",def:"company worth estimate",ex:"The valuation hit $1B — unicorn status."},
    {en:"cap table",ipa:"",es:"tabla de capitalización",def:"ownership breakdown",ex:"Review the cap table before Series C."},
    {en:"dilution",ipa:"/daɪˈluː.ʃən/",es:"dilución",def:"reduced ownership %",ex:"Founder dilution reached 35%."},
    {en:"burn rate",ipa:"",es:"tasa de consumo",def:"monthly cash spend",ex:"Burn rate is $500K monthly."}
  ],
  "Scientific business topics":[
    {en:"clinical trial",ipa:"",es:"ensayo clínico",def:"medical test",ex:"Phase III trials are underway."},
    {en:"peer review",ipa:"",es:"revisión por pares",def:"expert evaluation",ex:"The study passed peer review."},
    {en:"quantum computing",ipa:"",es:"computación cuántica",def:"next-gen computing",ex:"Quantum computing may break encryption."},
    {en:"biotech",ipa:"/ˈbaɪ.əʊ.tek/",es:"biotecnología",def:"biology-based tech",ex:"Biotech investment surged."},
    {en:"peer-reviewed",ipa:"",es:"revisado por pares",def:"scientifically validated",ex:"We cite peer-reviewed sources."},
    {en:"empirical evidence",ipa:"",es:"evidencia empírica",def:"observation-based proof",ex:"Empirical evidence supports the claim."}
  ],
  "Digital transformation":[
    {en:"legacy system",ipa:"",es:"sistema heredado",def:"old technology",ex:"Legacy systems slow us down."},
    {en:"SaaS",ipa:"/sæs/",es:"SaaS",def:"software as a service",ex:"We migrated to SaaS platforms."},
    {en:"API",ipa:"/ˌeɪ.piːˈaɪ/",es:"API",def:"application programming interface",ex:"Our APIs power 100 integrations."},
    {en:"scalability",ipa:"/ˌskeɪ.ləˈbɪl.ə.ti/",es:"escalabilidad",def:"ability to grow",ex:"Scalability was a design principle."},
    {en:"IoT",ipa:"",es:"IoT",def:"internet of things",ex:"IoT sensors monitor the factory."},
    {en:"data lake",ipa:"",es:"lago de datos",def:"centralized data repository",ex:"The data lake unified 50 sources."}
  ],
  "Disruptive technologies & AI":[
    {en:"generative AI",ipa:"",es:"IA generativa",def:"content-creating AI",ex:"Generative AI reshapes creative work."},
    {en:"LLM",ipa:"",es:"LLM",def:"large language model",ex:"LLMs like GPT-4 automate research."},
    {en:"RPA",ipa:"",es:"automatización robótica de procesos",def:"robotic process automation",ex:"RPA handles our invoice processing."},
    {en:"edge computing",ipa:"",es:"computación en el borde",def:"local processing",ex:"Edge computing reduces latency."},
    {en:"5G",ipa:"",es:"5G",def:"fifth-generation mobile network",ex:"5G enables real-time IoT."},
    {en:"deepfake",ipa:"/ˈdiːp.feɪk/",es:"deepfake",def:"AI-forged content",ex:"Deepfakes raise identity-fraud risk."}
  ],
  // C2 remaining topics
  "Financial English (advanced)":[
    {en:"EBITDA",ipa:"",es:"EBITDA",def:"earnings before interest, taxes, depreciation, amortization",ex:"EBITDA margin hit 24%."},
    {en:"free cash flow",ipa:"",es:"flujo de caja libre",def:"cash after CapEx",ex:"Free cash flow funds dividends."},
    {en:"CapEx / OpEx",ipa:"",es:"CapEx / OpEx",def:"capital vs operating expenditure",ex:"CapEx is front-loaded this year."},
    {en:"derivatives",ipa:"/dɪˈrɪv.ə.tɪvz/",es:"derivados",def:"contracts based on assets",ex:"Derivatives hedge our exposure."},
    {en:"leveraged buyout",ipa:"",es:"compra apalancada",def:"debt-financed acquisition",ex:"The leveraged buyout used 70% debt."},
    {en:"quantitative easing",ipa:"",es:"flexibilización cuantitativa",def:"central bank asset buying",ex:"Quantitative easing inflated asset prices."}
  ],
  "M&A advanced terminology":[
    {en:"hostile takeover",ipa:"",es:"toma hostil",def:"acquisition against board's wishes",ex:"The hostile takeover failed."},
    {en:"poison pill",ipa:"",es:"píldora envenenada",def:"defensive anti-takeover measure",ex:"The poison pill deterred the raider."},
    {en:"earn-out",ipa:"",es:"pago contingente",def:"performance-based payment",ex:"The earn-out extends over 3 years."},
    {en:"escrow",ipa:"/ˈes.krəʊ/",es:"custodia",def:"funds held by third party",ex:"$10M sits in escrow."},
    {en:"SPAC",ipa:"/spæk/",es:"SPAC",def:"special purpose acquisition company",ex:"SPACs were popular in 2021."},
    {en:"golden parachute",ipa:"",es:"paracaídas dorado",def:"executive exit payment",ex:"His golden parachute was $20M."}
  ],
  "Media training & PR":[
    {en:"bridging",ipa:"/ˈbrɪdʒ.ɪŋ/",es:"bridging, puente",def:"redirect an interview question",ex:"Use bridging to stay on message."},
    {en:"sound bite",ipa:"",es:"frase impactante",def:"quotable short remark",ex:"A good sound bite makes the headline."},
    {en:"off the record",ipa:"",es:"extraoficial",def:"not for publication",ex:"Everything you say is on the record unless agreed otherwise."},
    {en:"messaging discipline",ipa:"",es:"disciplina de mensaje",def:"staying on script",ex:"Messaging discipline is everything in crisis."},
    {en:"dog-whistle",ipa:"",es:"mensaje subliminal",def:"coded signal to insiders",ex:"Beware of dog-whistle language."},
    {en:"pivot",ipa:"/ˈpɪv.ət/",es:"reorientar",def:"change direction in conversation",ex:"Pivot from the problem to the solution."}
  ],
  "Investor relations":[
    {en:"earnings call",ipa:"",es:"llamada de resultados",def:"quarterly investor briefing",ex:"The earnings call is next Tuesday."},
    {en:"guidance",ipa:"/ˈɡaɪ.dəns/",es:"orientación",def:"forward-looking projections",ex:"We raised guidance for FY24."},
    {en:"forward-looking statement",ipa:"",es:"declaración prospectiva",def:"projection disclaimer",ex:"Forward-looking statements involve risks."},
    {en:"buyback",ipa:"/ˈbaɪ.bæk/",es:"recompra",def:"company repurchasing its shares",ex:"The $1B buyback lifted the stock."},
    {en:"dividend policy",ipa:"",es:"política de dividendos",def:"approach to shareholder payouts",ex:"Our dividend policy targets 40% payout."},
    {en:"analyst day",ipa:"",es:"día del analista",def:"investor briefing event",ex:"Analyst day drew 200 attendees."}
  ],
  "Legal English for executives":[
    {en:"fiduciary",ipa:"/fɪˈdjuː.ʃi.ər.i/",es:"fiduciario",def:"acting on another's behalf",ex:"Fiduciary duty is paramount."},
    {en:"indemnify",ipa:"/ɪnˈdem.nɪ.faɪ/",es:"indemnizar",def:"compensate for loss",ex:"The agreement indemnifies officers."},
    {en:"warranty",ipa:"/ˈwɒr.ən.ti/",es:"garantía contractual",def:"contractual promise",ex:"Breach of warranty triggers damages."},
    {en:"representation",ipa:"",es:"manifestación",def:"contractual statement of fact",ex:"Material representations were false."},
    {en:"subpoena",ipa:"/səˈpiː.nə/",es:"citación judicial",def:"legal summons",ex:"The CEO received a subpoena."},
    {en:"settlement",ipa:"/ˈset.əl.mənt/",es:"acuerdo, conciliación",def:"resolution of dispute",ex:"The settlement cost $50M."}
  ],
  "Geopolitical impact on business":[
    {en:"decoupling",ipa:"/diːˈkʌp.lɪŋ/",es:"desacoplamiento",def:"separating economic ties",ex:"US-China decoupling reshapes supply chains."},
    {en:"sanctions regime",ipa:"",es:"régimen de sanciones",def:"set of penalties",ex:"The sanctions regime targets specific sectors."},
    {en:"nearshoring",ipa:"/ˈnɪəˌʃɔː.rɪŋ/",es:"nearshoring",def:"moving operations closer to home",ex:"Nearshoring to Mexico is accelerating."},
    {en:"sovereign risk",ipa:"",es:"riesgo soberano",def:"country-level political risk",ex:"Sovereign risk affects bond yields."},
    {en:"trade war",ipa:"",es:"guerra comercial",def:"reciprocal tariffs between nations",ex:"The trade war escalated in Q2."},
    {en:"geoeconomics",ipa:"",es:"geoeconomía",def:"economics as geopolitical tool",ex:"Geoeconomics drives semiconductor policy."}
  ],
  "Behavioral economics":[
    {en:"nudge",ipa:"/nʌdʒ/",es:"empuje, nudge",def:"subtle behavioral intervention",ex:"A default nudge doubled enrollment."},
    {en:"anchoring",ipa:"/ˈæŋ.kər.ɪŋ/",es:"anclaje",def:"first number bias",ex:"Anchoring affects salary negotiations."},
    {en:"loss aversion",ipa:"",es:"aversión a la pérdida",def:"losses hurt more than gains please",ex:"Loss aversion explains sticky pricing."},
    {en:"confirmation bias",ipa:"",es:"sesgo de confirmación",def:"seeking confirming info",ex:"Confirmation bias distorts analysis."},
    {en:"sunk cost",ipa:"",es:"costo hundido",def:"unrecoverable past spend",ex:"Don't let sunk cost drive decisions."},
    {en:"heuristic",ipa:"/hjʊəˈrɪs.tɪk/",es:"heurística",def:"mental shortcut",ex:"Heuristics speed but bias decisions."}
  ],
  "Executive coaching":[
    {en:"blind spot",ipa:"",es:"punto ciego",def:"unrecognized weakness",ex:"The coach revealed my blind spot."},
    {en:"360 feedback",ipa:"",es:"retroalimentación 360",def:"all-around review",ex:"The 360 feedback is brutally honest."},
    {en:"executive presence",ipa:"",es:"presencia ejecutiva",def:"gravitas in leadership",ex:"Executive presence separates VPs from SVPs."},
    {en:"development plan",ipa:"",es:"plan de desarrollo",def:"growth roadmap",ex:"The development plan spans 12 months."},
    {en:"stretch goal",ipa:"",es:"meta ambiciosa",def:"challenging target",ex:"Stretch goals drive breakthrough growth."},
    {en:"legacy",ipa:"/ˈleɡ.ə.si/",es:"legado",def:"lasting impact",ex:"What will be your legacy as CEO?"}
  ],
  "IPO & capital markets":[
    {en:"initial public offering",ipa:"",es:"oferta pública inicial",def:"first public share sale",ex:"The IPO raised $2B."},
    {en:"underwriter",ipa:"/ˈʌn.dəˌraɪ.tər/",es:"suscriptor",def:"investment bank leading IPO",ex:"Goldman is our lead underwriter."},
    {en:"roadshow",ipa:"/ˈrəʊd.ʃəʊ/",es:"gira de presentación",def:"investor pitch tour",ex:"The roadshow covered 12 cities."},
    {en:"lock-up period",ipa:"",es:"periodo de bloqueo",def:"post-IPO share-sale restriction",ex:"The 180-day lock-up ends in March."},
    {en:"secondary offering",ipa:"",es:"oferta secundaria",def:"additional share issuance",ex:"The secondary offering raised $500M."},
    {en:"prospectus",ipa:"/prəˈspek.təs/",es:"prospecto",def:"IPO disclosure document",ex:"Read the prospectus carefully."}
  ],
  "Board governance & fiduciary duty":[
    {en:"duty of care",ipa:"",es:"deber de cuidado",def:"diligent decision-making",ex:"Duty of care requires informed votes."},
    {en:"duty of loyalty",ipa:"",es:"deber de lealtad",def:"acting in company's interest",ex:"Duty of loyalty forbids self-dealing."},
    {en:"proxy voting",ipa:"",es:"voto por poder",def:"voting via a representative",ex:"Proxy voting shapes AGM outcomes."},
    {en:"activist investor",ipa:"",es:"inversionista activista",def:"shareholder pushing change",ex:"The activist investor wants board seats."},
    {en:"board independence",ipa:"",es:"independencia de la junta",def:"director autonomy",ex:"Board independence protects shareholders."},
    {en:"D&O insurance",ipa:"",es:"seguro D&O",def:"directors & officers liability",ex:"D&O insurance is a board essential."}
  ],
  "Lobbying & public affairs":[
    {en:"lobbying",ipa:"/ˈlɒb.i.ɪŋ/",es:"cabildeo",def:"influencing policy",ex:"Lobbying budgets doubled this year."},
    {en:"regulatory capture",ipa:"",es:"captura regulatoria",def:"industry dominates regulator",ex:"Regulatory capture distorts markets."},
    {en:"policy paper",ipa:"",es:"documento de política",def:"position document",ex:"Our policy paper was cited in hearings."},
    {en:"think tank",ipa:"",es:"think tank",def:"policy research group",ex:"The think tank influences lawmakers."},
    {en:"stakeholder engagement",ipa:"",es:"engagement de interesados",def:"policymaker outreach",ex:"Stakeholder engagement precedes every launch."},
    {en:"white paper",ipa:"",es:"libro blanco",def:"authoritative position document",ex:"The white paper shaped the regulation."}
  ],
  "Trade policy & international law":[
    {en:"WTO",ipa:"",es:"OMC",def:"World Trade Organization",ex:"The WTO ruled against the tariffs."},
    {en:"free trade agreement",ipa:"",es:"tratado de libre comercio",def:"cross-border trade deal",ex:"The free trade agreement boosts exports."},
    {en:"dumping",ipa:"/ˈdʌmp.ɪŋ/",es:"dumping",def:"below-cost export pricing",ex:"Anti-dumping tariffs were imposed."},
    {en:"intellectual property",ipa:"",es:"propiedad intelectual",def:"legally protected creations",ex:"Protect intellectual property globally."},
    {en:"arbitration",ipa:"/ˌɑː.bɪˈtreɪ.ʃən/",es:"arbitraje",def:"private dispute resolution",ex:"The contract requires arbitration."},
    {en:"jurisdiction",ipa:"/ˌdʒʊə.rɪsˈdɪk.ʃən/",es:"jurisdicción",def:"legal authority area",ex:"This jurisdiction favors plaintiffs."}
  ],
  "Thought leadership & personal branding":[
    {en:"thought leader",ipa:"",es:"líder de opinión",def:"recognized expert voice",ex:"She is a thought leader in ESG."},
    {en:"op-ed",ipa:"/ˌɒp ˈed/",es:"artículo de opinión",def:"opinion editorial",ex:"His op-ed ran in the FT."},
    {en:"keynote",ipa:"/ˈkiː.nəʊt/",es:"discurso de apertura",def:"headline speech",ex:"She gave the Davos keynote."},
    {en:"LinkedIn presence",ipa:"",es:"presencia en LinkedIn",def:"professional social profile",ex:"A strong LinkedIn presence attracts talent."},
    {en:"executive brand",ipa:"",es:"marca ejecutiva",def:"personal leadership identity",ex:"Build your executive brand early."},
    {en:"influence",ipa:"/ˈɪn.flu.əns/",es:"influencia",def:"persuasive power",ex:"Influence compounds over time."}
  ]
});

// ===== CASE STUDIES =====
// Key: `${level}-${lessonIndex}`  (e.g. "b2-0" = B2 Unit 1)
// If missing, fallback generator is used.
const BE_CASE_DB = {
  // A1 - simple cases
  "a1-0":{
    company:"Cohasset Trading Lima",industry:"Import/Export",location:"Lima, Peru",
    background:"Cohasset Trading Lima is a small import company with 25 employees. They just hired a new sales manager from Argentina, Ricardo.",
    bgEs:"Cohasset Trading Lima es una pequeña empresa de importación con 25 empleados. Acaban de contratar un nuevo gerente de ventas de Argentina, Ricardo.",
    situation:"Ricardo needs to introduce himself to the team on his first day. He is nervous because his English is not perfect.",
    sitEs:"Ricardo necesita presentarse al equipo en su primer día. Está nervioso porque su inglés no es perfecto.",
    data:[{v:"25",l:"Employees"},{v:"First",l:"Day"},{v:"3 min",l:"Intro time"}],
    questions:["How should Ricardo introduce himself?","What 3 things should he say about his job?","How does he greet colleagues politely?"],
    vocabFocus:["Hello I'm","Nice to meet you","I work for","I'm from","Here's my card"],
    task:"Write Ricardo's 50-word business introduction for his first day.",minWords:50
  },
  "a1-1":{
    company:"Tanaka Engineering",industry:"Manufacturing",location:"Nagoya, Japan",
    background:"Kenji Tanaka is an engineer at Toyota. He has a new Peruvian colleague, Carmen, who just arrived in Japan.",
    situation:"Kenji wants to help Carmen understand daily routines in the Japanese office: start time, lunch break, meetings, and end of day.",
    questions:["What is a typical daily routine in this office?","How do they describe their jobs?","What work-life topics can they discuss?"],
    vocabFocus:["start work","have lunch","finish work","have a meeting","study English"],
    task:"Write a 50-word daily routine description for Carmen.",minWords:50
  },
  "a1-2":{
    company:"TechHelp Lima",industry:"IT Support",location:"Lima, Peru",
    background:"Maria works in IT support at a small company. Every day she receives calls about computer and printer problems.",
    situation:"Today she must handle 3 problems: printer broken, slow laptop, no WiFi. She needs polite phrases to respond.",
    questions:["How should Maria ask about problems?","What polite phrases can she use?","How does she offer solutions?"],
    vocabFocus:["The printer doesn't work","Can you help me","I'll come to your desk","Have you tried"],
    task:"Write a 60-word dialogue between Maria and a colleague with a computer problem.",minWords:60
  },
  // A2
  "a2-0":{
    company:"MegaSales Peru",industry:"Sales",location:"Lima, Peru",
    background:"MegaSales is hiring. Three candidates applied for the Sales Manager role: Ana (5 years experience), Luis (10 years), and Priya (3 years, MBA).",
    situation:"You are the HR manager. You must evaluate their past experience and write a recommendation.",
    data:[{v:"5 yrs",l:"Ana"},{v:"10 yrs",l:"Luis"},{v:"3 yrs + MBA",l:"Priya"}],
    questions:["What did each candidate do in their past jobs?","Who had the most experience?","Who seems most qualified and why?"],
    vocabFocus:["worked at","managed","grew sales by","led a team","promoted"],
    task:"Write a 70-word recommendation for which candidate to hire, using past simple tense.",minWords:70
  },
  // B1
  "b1-0":{
    company:"Andina Beverages",industry:"Consumer Goods",location:"Lima, Peru",
    background:"Andina Beverages has been selling traditional sodas for 30 years. Younger customers now prefer healthier options. Market share has dropped from 25% to 17%.",
    situation:"The marketing director has proposed a full rebranding, including a new logo, a new name for the main product, and a shift to healthy positioning. Budget: $2M.",
    data:[{v:"30 yrs",l:"Brand age"},{v:"17%",l:"Current share"},{v:"$2M",l:"Rebrand budget"}],
    options:[
      {t:"Full rebrand",d:"New logo + new name + new positioning (highest risk, highest reward)"},
      {t:"Refresh only",d:"Update visuals but keep name and core product (moderate risk)"},
      {t:"Sub-brand launch",d:"Keep classic line; launch healthy sub-brand (lowest risk, requires 2 budgets)"}
    ],
    questions:["What are the risks of a full rebrand?","How would you communicate the change to loyal customers?","Which option best balances tradition and growth?"],
    vocabFocus:["brand equity","rebranding","target audience","positioning","market share"],
    task:"Write a 100-word recommendation using present perfect and modal verbs.",minWords:100
  },
  // B2
  "b2-0":{
    company:"TechNova AI",industry:"SaaS / Enterprise AI",location:"São Paulo, Brazil",
    background:"TechNova AI is preparing for a critical board presentation. The company must decide whether to pivot from B2B analytics to a consumer AI product. They have 18 months of runway and growing competition from well-funded startups.",
    bgEs:"TechNova AI se está preparando para una presentación crucial ante la junta directiva. La empresa debe decidir si girar de analítica B2B a un producto de IA para consumidores. Tienen 18 meses de capital disponible y competencia creciente de startups bien financiadas.",
    situation:"You are the CEO. In 20 minutes you must present strategic options to the board: (1) Pivot fully to consumer AI, (2) Split the team into two products, or (3) Double down on B2B with a new enterprise tier.",
    sitEs:"Eres el CEO. En 20 minutos debes presentar opciones estratégicas a la junta: (1) Girar completamente hacia IA para consumidores, (2) Dividir el equipo en dos productos, o (3) Doblar la apuesta en B2B con un nuevo nivel enterprise.",
    data:[{v:"$12M",l:"ARR"},{v:"18 mo",l:"Runway"},{v:"65",l:"Employees"},{v:"3",l:"Major competitors"}],
    options:[
      {t:"Full pivot to consumer",d:"Abandon B2B, bet everything on consumer AI. High risk, potentially uncapped market."},
      {t:"Split teams",d:"Run both products in parallel. Dilutes focus but hedges the bet."},
      {t:"Double down B2B",d:"Release enterprise tier, raise prices, go upmarket. Lower ceiling, higher certainty."}
    ],
    questions:["Which option best preserves optionality given the 18-month runway?","If we had pivoted a year ago, how would the situation be different? (Third conditional)","What would you say to the board to build confidence in your choice?"],
    vocabFocus:["pivot","runway","ARR","competitive moat","capital efficiency","product-market fit"],
    task:"Write a 120-word executive recommendation using third conditional and modal verbs.",minWords:120
  },
  // C1
  "c1-0":{
    company:"Andean Airlines",industry:"Aviation",location:"Lima, Peru",
    background:"Andean Airlines, a regional carrier with 42 aircraft, faces an existential decision. Fuel costs have risen 35%, low-cost competitors have entered the domestic market, and passenger loyalty is eroding. The CEO must deliver a strategic communication to investors, employees, and regulators simultaneously.",
    bgEs:"Andean Airlines, una aerolínea regional con 42 aviones, enfrenta una decisión existencial. Los costos de combustible han subido 35%, competidores de bajo costo han ingresado al mercado doméstico y la lealtad de los pasajeros se erosiona. El CEO debe comunicar estratégicamente a inversores, empleados y reguladores simultáneamente.",
    situation:"You are the Chief Strategy Officer. Draft the messaging architecture for a 3-year transformation plan that addresses cost, competition, and trust — without panicking any audience.",
    sitEs:"Eres el Director de Estrategia. Diseña la arquitectura de mensajes para un plan de transformación de 3 años que aborde costos, competencia y confianza — sin alarmar a ninguna audiencia.",
    data:[{v:"42",l:"Aircraft"},{v:"+35%",l:"Fuel YoY"},{v:"-12%",l:"Loyalty score"},{v:"3 yr",l:"Horizon"}],
    options:[
      {t:"Aggressive cost cutting",d:"Layoffs, route cuts, fleet reduction — quick impact, morale damage."},
      {t:"Premium repositioning",d:"Move upmarket, smaller fleet, higher margin — takes longer, needs brand work."},
      {t:"Strategic alliance",d:"Partnership or code-share with a global carrier — loss of autonomy."}
    ],
    questions:["How should messaging differ for investors vs employees vs regulators?","What hedging language is appropriate to discuss future uncertainty?","If you could rewrite the last decade's strategy, what would you change? (Mixed conditional)"],
    vocabFocus:["narrative","positioning statement","stakeholder mapping","crisis comms","thought leadership"],
    task:"Draft a 150-word executive communication using hedging language and advanced inversion.",minWords:150
  },
  // C2
  "c2-0":{
    company:"Cohasset Holdings Group",industry:"Diversified Conglomerate",location:"Lima, Peru",
    background:"Cohasset Holdings is a family-controlled conglomerate founded by Leonard Cohasset in 1987, now spanning education (flagship: COHASSET Exams), agribusiness, and fintech. Leonard, 72, must address his board on succession. His daughter Sofía leads the education division and favours aggressive international expansion; his son Mateo runs fintech and prefers a spin-off. Two independent directors demand an external CEO search.",
    bgEs:"Cohasset Holdings es un conglomerado familiar fundado por Leonard Cohasset en 1987, que abarca educación (insignia: COHASSET Exams), agroindustria y fintech. Leonard, de 72 años, debe dirigirse a su junta sobre la sucesión. Su hija Sofía dirige la división educativa y favorece la expansión internacional agresiva; su hijo Mateo dirige fintech y prefiere una escisión. Dos directores independientes exigen una búsqueda de CEO externo.",
    situation:"You are Leonard. Deliver the opening statement of a 2-hour closed-door board meeting that frames the succession decision with gravitas, diplomatic ambiguity, and decisiveness — without publicly favouring either child.",
    sitEs:"Eres Leonard. Pronuncia el discurso de apertura de una reunión de junta a puerta cerrada de 2 horas que enmarque la decisión de sucesión con gravedad, ambigüedad diplomática y determinación — sin favorecer públicamente a ningún hijo.",
    data:[{v:"$1.4B",l:"Group revenue"},{v:"3",l:"Divisions"},{v:"12",l:"Board members"},{v:"1987",l:"Founded"}],
    options:[
      {t:"Internal succession",d:"Name Sofía or Mateo — risks family rupture and loss of the other."},
      {t:"External CEO",d:"Hire outside CEO with founder as Executive Chair — preserves peace, dilutes legacy."},
      {t:"Spin-off + split",d:"Split group; each heir runs their own company — clean but destroys synergies."}
    ],
    questions:["Craft a formal opening that acknowledges the weight of the moment without signalling preference.","How would you use stylistic inversion and literary devices to elevate the tone?","Which diplomatic phrases can buy you time while committing to nothing?"],
    vocabFocus:["fiduciary duty","duty of care","succession planning","board independence","executive presence","legacy"],
    task:"Write a 180-word opening statement in C2 register using stylistic inversion, hedging, and rhetorical structures.",minWords:180
  }
};

// Fallback case study generator
function BE_makeCaseFallback(level, lessonIdx, lesson){
  const title = lesson.title || ('Unit '+(lessonIdx+1));
  const subtitle = lesson.subtitle || '';
  // Pick company/location details based on level (advanced levels → more complex cases)
  const lvSetup = {
    a1:{co:"Pacific Foods Peru",ind:"Food & Beverage",loc:"Lima, Peru",scale:"small"},
    a2:{co:"Andina Retail",ind:"Retail Chain",loc:"Arequipa, Peru",scale:"regional"},
    b1:{co:"Inca Logistics",ind:"Logistics",loc:"Callao, Peru",scale:"national"},
    b2:{co:"Nuevo Mundo SA",ind:"Consumer Goods",loc:"Lima, Peru",scale:"multinational Latin America"},
    c1:{co:"Pacifico Strategic Partners",ind:"Strategy Consulting",loc:"Lima & Mexico City",scale:"regional consultancy"},
    c2:{co:"Cohasset Ventures Group",ind:"Private Equity",loc:"Lima, Peru",scale:"global"}
  }[level] || {co:"Global Co",ind:"General",loc:"Peru",scale:"national"};
  return {
    company:lvSetup.co,industry:lvSetup.ind,location:lvSetup.loc,
    background:`${lvSetup.co} (${lvSetup.scale}) operates in ${lvSetup.ind}. The organization has identified a critical need to improve its approach to "${title}".`,
    bgEs:`${lvSetup.co} (${lvSetup.scale}) opera en ${lvSetup.ind}. La organización ha identificado una necesidad crítica de mejorar su enfoque hacia "${title}".`,
    situation:`The leadership team must address challenges related to ${title}${subtitle?' — '+subtitle:''}. You have been asked to analyse the situation and propose a recommendation.`,
    sitEs:`El equipo directivo debe abordar los desafíos relacionados con ${title}${subtitle?' — '+subtitle:''}. Se te ha pedido analizar la situación y proponer una recomendación.`,
    data:[{v:"12",l:"Months horizon"},{v:"$"+((lessonIdx+2)*100)+"K",l:"Estimated investment"},{v:"3",l:"Options"},{v:(50+lessonIdx*3),l:"Affected staff"}],
    options:[
      {t:"Conservative path",d:`Small incremental steps in ${title.toLowerCase()}. Low risk, limited impact.`},
      {t:"Balanced approach",d:`Moderate investment to modernize ${title.toLowerCase()} with measurable milestones.`},
      {t:"Bold transformation",d:`Full transformation of ${title.toLowerCase()} — high upside, execution risk.`}
    ],
    questions:[
      `What is the strongest argument for acting on ${title.toLowerCase()} now rather than later?`,
      `How would you measure success in the first 90 days?`,
      `What risks must be communicated to stakeholders?`
    ],
    vocabFocus:["stakeholders","strategy","execution","KPI","roadmap","risk"],
    task:`Write a concise recommendation applying the unit's grammar and vocabulary to the ${title.toLowerCase()} challenge.`,
    minWords: level==='a1'?50 : level==='a2'?60 : level==='b1'?80 : level==='b2'?100 : level==='c1'?140 : 170
  };
}

function BE_getCase(level, lessonIdx, lesson){
  const k = `${level}-${lessonIdx}`;
  return BE_CASE_DB[k] || BE_makeCaseFallback(level, lessonIdx, lesson);
}
