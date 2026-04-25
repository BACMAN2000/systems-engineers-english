# -*- coding: utf-8 -*-
"""B1 lessons 6-20: full content (notes + passage + 5 reading + 8 UoE per lesson)."""
import json
from pathlib import Path

EXP = {
"B1": {
 6: {  # Cybersecurity threats overview (Passive with modals)
  "notes":{
   "warmup":"Cybersecurity is now a strategic concern at every level. The first step in defence is understanding the landscape: who attacks, why, and how. Without that, any defensive investment is essentially blind.",
   "grammar":{"title":"Passive voice with modals","rule":"Form: subject + modal + BE + past participle. Used when the action matters more than who performs it. Common modals: must, can, should, may, will.",
    "table":{"head":["Modal","Pattern","Example"],"rows":[
     ["must","must be + p.p.","Logs must be reviewed daily."],
     ["should","should be + p.p.","Endpoints should be monitored continuously."],
     ["can","can be + p.p.","An attack can be detected by anomaly rules."],
     ["will","will be + p.p.","The patch will be deployed tonight."],
     ["may","may be + p.p.","Sensitive data may be encrypted at rest."]]},
    "examples":[{"en":"Phishing emails must be reported, not deleted.","note":"obligation"},
     {"en":"This vulnerability can be exploited remotely.","note":"capability"},
     {"en":"All admin accounts should be protected with hardware keys.","note":"recommendation"}]},
   "phrases":[{"phrase":"This action / actor is motivated by …","use":"explain motive"},
    {"phrase":"The attack surface includes …","use":"scope"},
    {"phrase":"Threat actors range from … to …","use":"continuum"},
    {"phrase":"The kill chain begins with …","use":"sequence"}],
   "mistakes":[{"wrong":"This vulnerability can exploit remotely.","right":"This vulnerability can be exploited remotely.","why":"The vulnerability is the target → passive."},
    {"wrong":"Logs must reviewed daily.","right":"Logs must be reviewed daily.","why":"Modal passive needs BE."}],
   "tip":"Use the Cyber Kill Chain as your map: Recon → Weaponise → Deliver → Exploit → Install → C2 → Actions on Objectives. Every defensive control maps to one of these stages."},
  "passage":{"title":"The cyber threat landscape","text":"Modern cybersecurity teams must understand who is attacking them, why, and how. The threat landscape is more crowded than ever. Opportunistic criminals are still the largest group, but they have become more organised and more profitable. Targeted criminal gangs run ransomware operations like real businesses, with affiliates, brokers, and even customer service. Nation-state actors are mainly interested in espionage, but several groups have moved towards destructive operations against critical infrastructure. Hacktivists target organisations they disagree with. Insiders, both malicious and careless, remain a quiet but very real risk.\n\nLockheed Martin's Cyber Kill Chain is still a useful map. The seven phases are reconnaissance, weaponisation, delivery, exploitation, installation, command and control, and actions on objectives. Each stage gives defenders an opportunity to break the chain. Earlier interventions are usually cheaper. By the time the attacker reaches the actions phase, damage may already be done.\n\nMITRE ATT&CK has become the dominant operational framework. It maps real techniques used by real adversaries to specific tactics: initial access, execution, persistence, privilege escalation, defence evasion, credential access, discovery, lateral movement, collection, command and control, exfiltration, and impact. Detection engineers use it to design alerts. Incident responders use it to understand what they are seeing. Executives use it to compare their coverage against the techniques most likely to be used against them.","wc":225,"source":"Adapted from CISA threat landscape briefings (cisa.gov, PD), Lockheed Martin Cyber Kill Chain (public methodology), and MITRE ATT&CK (attack.mitre.org)."},
  "exercises":[
   {"type":"mcq","q":"Which group does the text describe as 'the largest'?","options":["nation-state actors","opportunistic criminals","insiders","hacktivists"],"a":1,"explain":"'Opportunistic criminals are still the largest group.'"},
   {"type":"tfng","q":"All nation-state operations are limited to espionage.","a":"F","explain":"'Several groups have moved towards destructive operations.'"},
   {"type":"gap","q":"The Cyber Kill Chain has ___ phases.","a":"seven","alts":["seven","7"],"explain":"'The seven phases are…'"},
   {"type":"match","pairs":[["Initial access","ATT&CK tactic"],["Affiliates","ransomware operation"],["Espionage","nation-state"],["Hacktivists","disagreement target"]]},
   {"type":"short","q":"Why are earlier interventions in the Kill Chain cheaper?","model":"Model: Because by later stages the attacker has gained access, established persistence and may have started causing damage. Containing them earlier (recon, delivery) prevents the chain from completing."}],
  "uoe":[
   {"type":"mc_cloze","sentence":"Logs ___ reviewed daily by the SOC team.","options":["must","must be","must been","should being"],"a":1,"explain":"Modal passive: must + BE + p.p."},
   {"type":"mc_cloze","sentence":"This vulnerability ___ remotely without authentication.","options":["can exploit","can be exploit","can be exploited","is can exploit"],"a":2,"explain":"Modal passive."},
   {"type":"cloze","sentence":"All admin accounts should ___ protected with hardware keys.","a":"be","alts":["be"],"explain":"Modal passive needs BE."},
   {"type":"cloze","sentence":"The kill chain begins ___ reconnaissance.","a":"with","alts":["with"],"explain":"Collocation: 'begin with'."},
   {"type":"word_form","base":"DEFEND","sentence":"Strong ___ depends on understanding the landscape.","a":"defence","alts":["defence","defense"],"explain":"Verb → noun."},
   {"type":"word_form","base":"WEAPON","sentence":"___ is the second phase of the kill chain.","a":"Weaponisation","alts":["Weaponisation","Weaponization"],"explain":"-isation noun."},
   {"type":"key_word","original":"Defenders break the kill chain at any phase.","key":"BROKEN","gap_template":"The kill chain ___ defenders at any phase.","a":"can be broken by","alts":["can be broken by"],"explain":"Active → passive with agent."},
   {"type":"key_word","original":"Many companies must report incidents within 72 hours.","key":"REQUIRED","gap_template":"Many companies ___ incidents within 72 hours.","a":"are required to report","alts":["are required to report"],"explain":"'Be required to + base'."}]},
 7: {  # Malware types (Reported statements)
  "notes":{
   "warmup":"Malware is the umbrella term for any software designed to harm. Each family has a distinct profile. Knowing the differences shapes how you detect, contain and recover.",
   "grammar":{"title":"Reported speech (statements)","rule":"To report what someone said, the tense usually shifts back one step (present → past, past → past perfect). Pronouns and time references also change.",
    "table":{"head":["Direct","Reported","Tense shift"],"rows":[
     ["'I am scanning.'","She said she was scanning.","present → past"],
     ["'We deployed it.'","He said they had deployed it.","past → past perfect"],
     ["'The system will fail.'","She said the system would fail.","will → would"],
     ["'I have seen this.'","He said he had seen this.","perfect → past perfect"]]},
    "examples":[{"en":"The analyst said the malware was fileless.","note":"present → past"},
     {"en":"The vendor reported that they had patched the vulnerability.","note":"past → past perfect"},
     {"en":"He confirmed that the wiper would not exfiltrate data.","note":"will → would"}]},
   "phrases":[{"phrase":"Sources confirm that …","use":"reporting CTI"},
    {"phrase":"The vendor stated that …","use":"reference statement"},
    {"phrase":"It has been reported that …","use":"hedged claim"},
    {"phrase":"Initial analysis suggests …","use":"early findings"}],
   "mistakes":[{"wrong":"The analyst said the malware is fileless.","right":"The analyst said the malware was fileless.","why":"Reporting verb in past → tense shift back."},
    {"wrong":"He told that he saw it.","right":"He told me / He said that he had seen it.","why":"TELL needs an object; SAY does not."}],
   "tip":"Distinguish ransomware from wipers. Ransomware encrypts and demands payment (recoverable). Wipers destroy without recovery (no decryption possible). Some attackers disguise wipers as ransomware to delay attribution."},
  "passage":{"title":"The malware family tree","text":"Malware is a broad family with very different members. Viruses attach themselves to legitimate programs and run when those programs run. Worms spread by themselves across networks, exploiting vulnerabilities to move from host to host. Trojans pretend to be useful software but carry malicious payloads. Rootkits hide deep in the operating system, often at kernel level, making detection hard. Spyware quietly collects keystrokes, screenshots and credentials. Ransomware encrypts files and demands payment. Wipers destroy data without any possibility of recovery; they are typically deployed in geopolitical operations rather than for profit.\n\nA security researcher recently said that fileless malware is now one of the fastest-growing categories. Instead of writing files to disk, attackers abuse trusted system tools like PowerShell or Windows Management Instrumentation. Antivirus engines that look for malicious files struggle here, because there are no files to scan. Endpoint Detection and Response platforms have become essential, because they monitor behaviour across the system, not just files.\n\nAttribution is rarely straightforward. Operators reuse code, share infrastructure and sometimes deliberately plant false flags. Mature analysts work with explicit confidence levels: 'low' when the evidence is suggestive but thin, 'high' when multiple independent indicators point in the same direction. The Mandiant report on a recent incident stated that they had observed three distinct toolkits, two of which had been previously linked to a known actor.","wc":221,"source":"Adapted from CISA Malware Analysis Reports (cisa.gov, PD), MITRE ATT&CK (attack.mitre.org), and Mandiant M-Trends public summaries."},
  "exercises":[
   {"type":"mcq","q":"Which malware type spreads by itself across networks?","options":["Virus","Worm","Trojan","Rootkit"],"a":1,"explain":"'Worms spread by themselves across networks.'"},
   {"type":"tfng","q":"Wipers can be decrypted if you have the key.","a":"F","explain":"'Wipers destroy data without any possibility of recovery.'"},
   {"type":"gap","q":"Fileless malware abuses trusted tools like ___ or WMI.","a":"PowerShell","alts":["PowerShell","powershell"],"explain":"From the text."},
   {"type":"match","pairs":[["Trojan","disguised as useful"],["Rootkit","hides in OS"],["Spyware","collects keystrokes"],["Wiper","destroys data"]]},
   {"type":"short","q":"Why are EDR platforms more effective than AV against fileless malware?","model":"Model: Antivirus engines scan files for known patterns. Fileless malware leaves nothing to scan. EDR monitors behaviour across processes and the system, so it detects abuse of legitimate tools."}],
  "uoe":[
   {"type":"mc_cloze","sentence":"The analyst said the worm ___ across networks.","options":["spreads","is spreading","spread","was spreading"],"a":3,"explain":"Reported: present continuous → past continuous."},
   {"type":"mc_cloze","sentence":"Mandiant reported they ___ three distinct toolkits.","options":["have observed","had observed","observed","were observing"],"a":1,"explain":"Reported past simple → past perfect."},
   {"type":"cloze","sentence":"The vendor stated ___ they had patched the bug.","a":"that","alts":["that"],"explain":"Reporting + that-clause."},
   {"type":"cloze","sentence":"Sources confirm ___ the campaign is still active.","a":"that","alts":["that"],"explain":"Same."},
   {"type":"word_form","base":"DETECT","sentence":"Behavioural ___ has replaced signature-based AV.","a":"detection","alts":["detection"],"explain":"Verb → noun: -tion."},
   {"type":"word_form","base":"PERSIST","sentence":"Rootkits use kernel-level ___ techniques.","a":"persistence","alts":["persistence"],"explain":"-ence noun."},
   {"type":"key_word","original":"\"This file is malicious,\" said the engineer.","key":"WAS","gap_template":"The engineer said that the file ___ malicious.","a":"was","alts":["was"],"explain":"Reported: present → past."},
   {"type":"key_word","original":"\"We will rebuild the system,\" she announced.","key":"WOULD","gap_template":"She announced that they ___ the system.","a":"would rebuild","alts":["would rebuild"],"explain":"Will → would in reported speech."}]},
 8: {  # Phishing and social engineering deep dive (Reported questions)
  "notes":{
   "warmup":"Phishing accounts for the majority of confirmed data breaches. The technical countermeasures matter, but the durable defence is people who recognise manipulation in real time. That is a teachable skill.",
   "grammar":{"title":"Reported questions","rule":"In reported questions, normal word order returns (no inversion) and tenses shift back. Use IF or WHETHER for yes/no questions.",
    "table":{"head":["Direct","Reported","Notes"],"rows":[
     ["'Where is the file?'","She asked where the file was.","no inversion"],
     ["'Did you click?'","He asked if I had clicked.","yes/no → IF"],
     ["'What does it do?'","They asked what it did.","wh-question"],
     ["'Have you reported it?'","She asked whether we had reported it.","yes/no → WHETHER"]]},
    "examples":[{"en":"He asked who had received the email first.","note":"reported wh-question"},
     {"en":"She wondered if the link was legitimate.","note":"yes/no with IF"},
     {"en":"The CISO asked when the campaign had started.","note":"reported when-question"}]},
   "phrases":[{"phrase":"Hover over the link before clicking.","use":"action"},
    {"phrase":"Verify the sender out of band.","use":"defensive technique"},
    {"phrase":"This has all the red flags of …","use":"identification"},
    {"phrase":"When in doubt, do not click.","use":"safe rule"}],
   "mistakes":[{"wrong":"She asked where was the file.","right":"She asked where the file was.","why":"No inversion in reported questions."},
    {"wrong":"He asked did I click.","right":"He asked if I had clicked.","why":"Yes/no question → IF + tense shift."}],
   "tip":"Train yourself to read the URL, not the link text. 'Click here' might say one thing while pointing to a completely different domain. Hovering reveals the truth."},
  "passage":{"title":"Anatomy of a spear phish","text":"Anna received an email that looked exactly like an internal HR notification. The sender appeared to be 'hr-notifications@hercompany.com'. The subject line said: 'Action required: confirm your bank details for May payroll.' There was a button labelled 'Update details'. She had a moment of doubt and asked her colleague whether the email was legitimate. He suggested hovering over the button. The actual URL was 'https://her-company-payroll-portal.com/login' — not the company domain. It was a spear-phishing attack.\n\nThe attackers had clearly done their homework. They knew the company was about to issue an internal communication about payroll changes, because the new HR system had been announced on LinkedIn. They had registered a lookalike domain and built a near-perfect copy of the real login page. Anna's colleague reported it to the security team. The team confirmed it was part of a larger campaign and asked whether anyone in the company had clicked. They had, unfortunately. Three employees had submitted credentials before the email was blocked.\n\nThe security team ran the standard playbook. They reset the affected accounts, forced password rotation, reviewed authentication logs, and looked for any subsequent suspicious activity. The chief information security officer asked when the campaign had begun and how the attackers had identified internal communications. The investigation pointed to public LinkedIn posts and a former employee whose access had not been deprovisioned promptly.","wc":236,"source":"Adapted from FBI 'Business Email Compromise' advisory (fbi.gov, PD) and CISA spear-phishing guidance (cisa.gov, PD)."},
  "exercises":[
   {"type":"mcq","q":"How did Anna's colleague help identify the phish?","options":["clicked the link","hovered over the button","called HR","ignored the email"],"a":1,"explain":"'He suggested hovering over the button.'"},
   {"type":"tfng","q":"The attackers used the company's real domain.","a":"F","explain":"'her-company-payroll-portal.com — not the company domain.'"},
   {"type":"gap","q":"___ employees had submitted credentials before the email was blocked.","a":"Three","alts":["Three","3"],"explain":"From the text."},
   {"type":"match","pairs":[["lookalike domain","spoofing"],["LinkedIn","reconnaissance"],["password rotation","containment"],["former employee","deprovisioning gap"]]},
   {"type":"short","q":"What two pieces of public information helped the attackers?","model":"Model: 1) The LinkedIn announcement of the new HR system gave them a credible pretext. 2) Information about a former employee whose access was not properly deprovisioned."}],
  "uoe":[
   {"type":"mc_cloze","sentence":"She asked ___ the email was legitimate.","options":["whether","is","does","that"],"a":0,"explain":"Reported yes/no question → WHETHER."},
   {"type":"mc_cloze","sentence":"He asked when the campaign ___ .","options":["had begun","has begun","is beginning","begins"],"a":0,"explain":"Reported past simple → past perfect."},
   {"type":"cloze","sentence":"The CISO wanted to know ___ anyone had clicked.","a":"if","alts":["if","whether"],"explain":"Reported yes/no."},
   {"type":"cloze","sentence":"Hover over the link ___ clicking.","a":"before","alts":["before"],"explain":"Time preposition + -ing."},
   {"type":"word_form","base":"AUTHENTIC","sentence":"Multi-factor ___ stops most credential phishing.","a":"authentication","alts":["authentication"],"explain":"-ation noun."},
   {"type":"word_form","base":"PROVISION","sentence":"Slow account ___ left a window for abuse.","a":"deprovisioning","alts":["deprovisioning"],"explain":"de- + -ing form."},
   {"type":"key_word","original":"\"Did anyone click the link?\" the CISO asked.","key":"WHETHER","gap_template":"The CISO asked ___ clicked the link.","a":"whether anyone had","alts":["whether anyone had"],"explain":"Reported yes/no + tense shift."},
   {"type":"key_word","original":"\"Where does this URL point?\" she asked.","key":"POINTED","gap_template":"She asked where ___ .","a":"the URL pointed","alts":["the URL pointed"],"explain":"No inversion."}]},
 9: {  # Password management (Verb + -ing / to-infinitive)
  "notes":{
   "warmup":"The password is the most universal authentication method and the most criticised. Modern guidance has shifted: forget complex character rules; focus on length, uniqueness and exposure detection.",
   "grammar":{"title":"Verb + -ing vs verb + to-infinitive","rule":"Some verbs are followed by -ing (avoid, recommend, suggest, mind, enjoy). Others by to-infinitive (decide, plan, want, refuse, agree). A few change meaning depending on the form (stop, remember, try).",
    "table":{"head":["Pattern","Verbs","Example"],"rows":[
     ["+ -ing","avoid, recommend, suggest, mind, enjoy","I avoid reusing passwords."],
     ["+ to-infinitive","decide, plan, want, refuse, agree","She agreed to use a manager."],
     ["+ both (same meaning)","start, begin, like, hate","I started using / to use 2FA."],
     ["+ both (different meaning)","stop, remember, try","I stopped to write it (paused) vs I stopped writing it (no longer)."]]},
    "examples":[{"en":"I recommend using a password manager.","note":"recommend + -ing"},
     {"en":"She decided to enable hardware keys.","note":"decide + to + base"},
     {"en":"I tried changing the rotation policy.","note":"experiment"},
     {"en":"I tried to change the rotation policy.","note":"attempt that may have failed"}]},
   "phrases":[{"phrase":"My password is …","use":"never write this in chat"},
    {"phrase":"I use a password manager.","use":"safe statement"},
    {"phrase":"My account was breached.","use":"report"},
    {"phrase":"Have I been pwned?","use":"public exposure check"}],
   "mistakes":[{"wrong":"I avoid to reuse passwords.","right":"I avoid reusing passwords.","why":"AVOID + -ing."},
    {"wrong":"She decided enabling 2FA.","right":"She decided to enable 2FA.","why":"DECIDE + to + base."}],
   "tip":"Modern NIST guidance: do not enforce periodic rotation unless you suspect compromise. Focus instead on length (≥ 12 characters), checking against breach corpora, and adding a second factor."},
  "passage":{"title":"Modern password management","text":"For decades, organisations enforced passwords that were short, complex and rotated every 90 days. Users responded predictably: they wrote them on sticky notes, varied them by adding a digit at the end, or chose patterns that were easy to remember and easy to break. The 2017 update to NIST Special Publication 800-63B changed the conversation. NIST now recommends focusing on length rather than complexity, banning common and breached passwords, and avoiding mandatory periodic rotation unless there is evidence of compromise.\n\nA password manager is the practical answer for most users. It generates a unique, long password for every site and stores them encrypted under a single master passphrase. Bitwarden, 1Password, and KeePass are well-known options. Security teams sometimes worry that managers create a single point of failure, but the alternative — humans inventing passwords — has been measured many times and the results are consistently worse.\n\nMulti-factor authentication adds a second layer that is not based on what the user knows. Hardware keys based on FIDO2 are now the gold standard, because they are resistant to phishing in a way that SMS or push-notification methods are not. SMS codes can be intercepted through SIM-swap attacks; push fatigue, where attackers spam the user until they accept a prompt, has compromised major companies. The most important habit, however, is checking whether your accounts have already been exposed in known breaches. Free services like Have I Been Pwned make this trivial.","wc":236,"source":"Adapted from NIST SP 800-63B (nist.gov, PD), CISA password guidance (cisa.gov, PD), and the Have I Been Pwned project (haveibeenpwned.com, public service)."},
  "exercises":[
   {"type":"mcq","q":"Modern NIST guidance focuses primarily on:","options":["complexity","length","rotation","case sensitivity"],"a":1,"explain":"'Focusing on length rather than complexity.'"},
   {"type":"tfng","q":"NIST recommends mandatory rotation every 90 days.","a":"F","explain":"'Avoiding mandatory periodic rotation unless there is evidence of compromise.'"},
   {"type":"gap","q":"Hardware keys based on ___ are now the gold standard.","a":"FIDO2","alts":["FIDO2","fido2"],"explain":"From the text."},
   {"type":"match","pairs":[["NIST 800-63B","2017 guidance update"],["Bitwarden","password manager"],["FIDO2","phishing-resistant 2FA"],["Have I Been Pwned","exposure check"]]},
   {"type":"short","q":"Why are SMS codes considered weaker 2FA than hardware keys?","model":"Model: SMS codes can be intercepted via SIM-swap attacks. Hardware keys use cryptographic challenge-response that cannot be replayed by phishers."}],
  "uoe":[
   {"type":"mc_cloze","sentence":"I avoid ___ the same password twice.","options":["use","to use","using","used"],"a":2,"explain":"AVOID + -ing."},
   {"type":"mc_cloze","sentence":"She decided ___ a hardware key.","options":["buying","to buy","buy","bought"],"a":1,"explain":"DECIDE + to + base."},
   {"type":"cloze","sentence":"I recommend ___ a password manager.","a":"using","alts":["using"],"explain":"RECOMMEND + -ing."},
   {"type":"cloze","sentence":"He stopped ___ to take a call.","a":"working","alts":["working","to take"],"explain":"Both possible: paused work to do something else."},
   {"type":"word_form","base":"ROTATE","sentence":"Mandatory ___ is no longer recommended.","a":"rotation","alts":["rotation"],"explain":"-ation noun."},
   {"type":"word_form","base":"COMPROMISE","sentence":"Rotate only after evidence of ___ .","a":"compromise","alts":["compromise"],"explain":"Verb / noun same form."},
   {"type":"key_word","original":"It is a good idea to use a password manager.","key":"USING","gap_template":"I would recommend ___ a password manager.","a":"using","alts":["using"],"explain":"RECOMMEND + -ing."},
   {"type":"key_word","original":"Don't reuse passwords across sites.","key":"AVOID","gap_template":"You should ___ across sites.","a":"avoid reusing passwords","alts":["avoid reusing passwords"],"explain":"AVOID + -ing."}]},
 10: {  # Multi-factor authentication (Zero conditional)
  "notes":{
   "warmup":"MFA is the single highest-impact control for credential abuse. Microsoft estimates it blocks more than 99 % of automated account-takeover attempts. The remaining one per cent matters too, which is why the type of MFA matters.",
   "grammar":{"title":"Zero conditional (general truths)","rule":"Form: IF + present simple, present simple. Used for general truths and natural laws — when X happens, Y always happens.",
    "table":{"head":["IF clause","Result","Use"],"rows":[
     ["IF + present simple","present simple","general truth"],
     ["When + present","present","habitual"],
     ["Unless + present","present","negative condition"]]},
    "examples":[{"en":"If a user enters wrong credentials, the system locks the account.","note":"general rule"},
     {"en":"When MFA is enabled, automated attacks fail.","note":"general truth"},
     {"en":"Unless you use a hardware key, you remain vulnerable to phishing.","note":"negative condition"}]},
   "phrases":[{"phrase":"Enable MFA on every account.","use":"action"},
    {"phrase":"Phishing-resistant factors include …","use":"specify"},
    {"phrase":"This control mitigates …","use":"explain coverage"},
    {"phrase":"In our threat model, …","use":"contextualise"}],
   "mistakes":[{"wrong":"If you will enable MFA, attacks fail.","right":"If you enable MFA, attacks fail.","why":"Zero conditional → present simple in both clauses; never WILL in the IF."},
    {"wrong":"Unless you don't use MFA, you are safer.","right":"Unless you use MFA, you are vulnerable.","why":"UNLESS already negative; do not double-negate."}],
   "tip":"Avoid SMS as your primary MFA. SIM-swap attacks have compromised cryptocurrency exchanges, telecom executives, and even SS7 protocols. Use authenticator apps or, better, FIDO2 hardware keys."},
  "passage":{"title":"Choosing your MFA factor","text":"Multi-factor authentication combines two or more independent factors: something you know (a password), something you have (a phone or a hardware key), and something you are (a fingerprint, a face). When all three are required, attacks become considerably harder. Yet not all MFA factors are equal, and confusing them is a common mistake.\n\nSMS codes were the original second factor. They are simple, but they have well-documented weaknesses. If an attacker convinces a mobile carrier to transfer the victim's number to a new SIM (a SIM-swap attack), the codes go to the attacker. Push notifications, used by apps like Microsoft Authenticator and Duo, are a small step up. They tie the second factor to a specific device. However, push fatigue attacks have shown that users will accept prompts they did not initiate if they are bombarded enough times.\n\nTime-based one-time passwords, or TOTP, are stronger. Apps generate codes locally without needing the internet, which removes the SMS-interception risk. The user still has to copy the code, which makes the method phishable: if the user enters their TOTP into a fake site, the attacker can use it within the 30-second window.\n\nHardware keys based on the FIDO2 / WebAuthn standard are the strongest mainstream option. They sign a cryptographic challenge tied to the actual website domain. If the domain is wrong, the key refuses to authenticate. This makes them genuinely phishing-resistant. The latest evolution, passkeys, brings the same protection to consumer accounts without requiring a separate hardware device.","wc":259,"source":"Adapted from NIST SP 800-63B (nist.gov, PD), FIDO Alliance public specifications (fidoalliance.org), and Microsoft Identity blog (microsoft.com/security)."},
  "exercises":[
   {"type":"mcq","q":"Which factor is described as 'genuinely phishing-resistant'?","options":["SMS","push","TOTP","FIDO2 hardware keys"],"a":3,"explain":"'Hardware keys based on the FIDO2/WebAuthn standard… genuinely phishing-resistant.'"},
   {"type":"tfng","q":"TOTP codes are immune to phishing.","a":"F","explain":"'Phishable: if the user enters their TOTP into a fake site…'"},
   {"type":"gap","q":"A SIM-swap attack convinces a mobile carrier to transfer the victim's ___ .","a":"number","alts":["number"],"explain":"From the text."},
   {"type":"match","pairs":[["SMS","SIM-swap risk"],["Push","fatigue attacks"],["TOTP","phishable"],["FIDO2","phishing-resistant"]]},
   {"type":"short","q":"Why does FIDO2 prevent phishing in a way TOTP cannot?","model":"Model: FIDO2 binds the cryptographic response to the actual domain. If the user is on a fake site, the key refuses to authenticate. TOTP codes have no such binding and can be replayed by an attacker."}],
  "uoe":[
   {"type":"mc_cloze","sentence":"If a user ___ wrong credentials, the system locks the account.","options":["will enter","enter","enters","entered"],"a":2,"explain":"Zero conditional + 3rd person."},
   {"type":"mc_cloze","sentence":"Unless you ___ a hardware key, phishing remains a risk.","options":["use","don't use","will use","using"],"a":0,"explain":"UNLESS + present (no double negative)."},
   {"type":"cloze","sentence":"When MFA is enabled, automated attacks ___ .","a":"fail","alts":["fail"],"explain":"Zero conditional, 3rd plural."},
   {"type":"cloze","sentence":"FIDO2 ties the response ___ the website domain.","a":"to","alts":["to"],"explain":"'Tied to'."},
   {"type":"word_form","base":"AUTHENTICATE","sentence":"FIDO2 provides phishing-resistant ___ .","a":"authentication","alts":["authentication"],"explain":"-tion noun."},
   {"type":"word_form","base":"RESIST","sentence":"FIDO2 keys are ___ to phishing.","a":"resistant","alts":["resistant"],"explain":"-ant adjective."},
   {"type":"key_word","original":"If you do not use MFA, your account is exposed.","key":"UNLESS","gap_template":"___ MFA, your account is exposed.","a":"Unless you use","alts":["Unless you use"],"explain":"UNLESS replaces 'if not'."},
   {"type":"key_word","original":"FIDO2 protects users from phishing.","key":"PROTECTED","gap_template":"Users ___ phishing by FIDO2.","a":"are protected from","alts":["are protected from"],"explain":"Active → passive + 'from'."}]},
 11: {  # Encryption basics (will vs going to)
  "notes":{
   "warmup":"Encryption hides the meaning of data, not its existence. The cryptographic primitives are mathematical, but most security incidents are not about broken math — they are about broken implementations.",
   "grammar":{"title":"Future: WILL vs GOING TO","rule":"WILL = spontaneous decisions, predictions, promises. GOING TO = plans already decided, predictions with present evidence.",
    "table":{"head":["Form","Use","Example"],"rows":[
     ["will","spontaneous decision","I'll rotate the key now."],
     ["will","prediction","Quantum computers will break RSA eventually."],
     ["going to","plan","We're going to migrate to ML-KEM next year."],
     ["going to","evidence-based prediction","Look at this CVE — we're going to need a patch fast."]]},
    "examples":[{"en":"I will check the certificate expiry.","note":"decision now"},
     {"en":"We are going to deploy mTLS in Q3.","note":"existing plan"},
     {"en":"That cipher will be deprecated soon.","note":"prediction"}]},
   "phrases":[{"phrase":"Data at rest is encrypted with …","use":"describe storage"},
    {"phrase":"Data in transit uses TLS 1.3.","use":"describe transport"},
    {"phrase":"The key is rotated every …","use":"describe lifecycle"},
    {"phrase":"We need crypto agility because …","use":"justify"}],
   "mistakes":[{"wrong":"I am going to check the certificate now, immediately.","right":"I will check the certificate now.","why":"Spontaneous decision → WILL."},
    {"wrong":"We will migrate to ML-KEM next year (already decided).","right":"We are going to migrate to ML-KEM next year.","why":"Existing plan → GOING TO."}],
   "tip":"Two rules of crypto in practice: never invent your own primitives, never disable certificate validation. Both are responsible for a disproportionate share of real incidents."},
  "passage":{"title":"What encryption actually does","text":"Encryption transforms readable data, called plaintext, into something unintelligible without the key. The two main families are symmetric and asymmetric. Symmetric encryption uses the same key for both encryption and decryption. AES is the standard symmetric algorithm; AES-256 in GCM mode is the modern recommendation. Asymmetric encryption uses a key pair: a public key, which anyone can have, and a private key, which only the owner has. RSA was the dominant asymmetric algorithm for decades, but it is increasingly being replaced by elliptic curve cryptography for performance reasons.\n\nMost real systems combine both. TLS, the protocol that protects every secure web connection, uses asymmetric cryptography to securely exchange a session key, and then symmetric AES to encrypt the actual traffic. This hybrid approach gives the security of asymmetric and the speed of symmetric.\n\nSecurity does not come from the algorithm alone. Implementation matters enormously. The OpenSSL Heartbleed bug in 2014 had nothing to do with broken AES; it was a buffer over-read that leaked private keys. Padding oracle attacks, timing attacks and side-channel attacks have repeatedly broken otherwise sound algorithms. Modern AEAD modes — Authenticated Encryption with Associated Data — close many of these gaps by binding integrity to confidentiality.\n\nLooking forward, the cryptographic community is preparing for the post-quantum era. NIST has standardised ML-KEM (formerly Kyber) for key encapsulation and ML-DSA for digital signatures. Major browsers and cloud providers are going to deploy hybrid post-quantum TLS in 2026, combining a classical and a post-quantum primitive for safety.","wc":255,"source":"Adapted from NIST FIPS 197 / 203 / 204 (nist.gov, PD), IETF RFC 8446 TLS 1.3 (rfc-editor.org), and Cloudflare research blog (CC BY)."},
  "exercises":[
   {"type":"mcq","q":"Which encryption type uses the same key for encryption and decryption?","options":["asymmetric","symmetric","quantum","hybrid"],"a":1,"explain":"'Symmetric encryption uses the same key for both…'"},
   {"type":"tfng","q":"Heartbleed was caused by a broken AES implementation.","a":"F","explain":"'Heartbleed bug had nothing to do with broken AES.'"},
   {"type":"gap","q":"NIST has standardised ML-KEM (formerly ___).","a":"Kyber","alts":["Kyber"],"explain":"From the text."},
   {"type":"match","pairs":[["AES","symmetric"],["RSA","asymmetric"],["TLS","hybrid"],["ML-KEM","post-quantum"]]},
   {"type":"short","q":"Why are AEAD modes important for modern encryption?","model":"Model: They bind authenticity (integrity) to confidentiality, preventing classic attacks like padding oracles. Without authentication, an attacker can sometimes manipulate ciphertext to learn plaintext."}],
  "uoe":[
   {"type":"mc_cloze","sentence":"Look at this CVE — we ___ to patch fast.","options":["will need","are going to need","need going","needs to"],"a":1,"explain":"Evidence-based plan → GOING TO."},
   {"type":"mc_cloze","sentence":"OK, I ___ rotate the key right now.","options":["am going to","was going to","will","would"],"a":2,"explain":"Spontaneous decision → WILL."},
   {"type":"cloze","sentence":"We are going ___ deploy hybrid TLS next quarter.","a":"to","alts":["to"],"explain":"GOING + TO + base."},
   {"type":"cloze","sentence":"Data at rest must be encrypted ___ AES-256.","a":"with","alts":["with"],"explain":"Encrypted WITH + algorithm."},
   {"type":"word_form","base":"ENCRYPT","sentence":"AES is the standard ___ algorithm.","a":"encryption","alts":["encryption"],"explain":"-tion noun."},
   {"type":"word_form","base":"AUTHENTIC","sentence":"AEAD provides ___ encryption with associated data.","a":"authenticated","alts":["authenticated"],"explain":"-ed past participle adjective."},
   {"type":"key_word","original":"Browsers will deploy hybrid post-quantum TLS in 2026.","key":"GOING","gap_template":"Browsers ___ hybrid post-quantum TLS in 2026.","a":"are going to deploy","alts":["are going to deploy"],"explain":"Plan → GOING TO."},
   {"type":"key_word","original":"Quantum computers will eventually break RSA.","key":"BROKEN","gap_template":"RSA ___ by quantum computers.","a":"will eventually be broken","alts":["will eventually be broken","will be broken eventually"],"explain":"Future passive."}]},
 12: {  # Firewalls and antivirus (Defining and non-defining clauses)
  "notes":{
   "warmup":"Firewalls and antivirus are the oldest household names in security. They still matter, but their role has narrowed. Modern defence is layered, behavioural, and continuously tuned.",
   "grammar":{"title":"Defining vs non-defining relative clauses","rule":"Defining clauses give essential information; no commas. Non-defining clauses give extra information; commas required. WHICH allowed in non-defining; THAT only in defining.",
    "table":{"head":["Type","Example","Punctuation"],"rows":[
     ["defining","The firewall that we deployed last year is end-of-life.","no commas"],
     ["non-defining","Our firewall, which we deployed in 2020, is end-of-life.","commas"],
     ["defining (people)","The analyst who wrote that rule has left.","no commas"],
     ["non-defining (people)","The CISO, who joined in 2024, leads the migration.","commas"]]},
    "examples":[{"en":"The IDS that we tuned last week stopped catching real attacks.","note":"defining"},
     {"en":"Our SIEM, which costs millions per year, has visibility gaps.","note":"non-defining"},
     {"en":"The vendors whose products we evaluate must follow our security questionnaire.","note":"WHOSE"}]},
   "phrases":[{"phrase":"This rule blocks …","use":"describe control"},
    {"phrase":"The firewall is configured to …","use":"describe behaviour"},
    {"phrase":"AV is no longer sufficient because …","use":"justification"},
    {"phrase":"We tuned this rule because …","use":"reason"}],
   "mistakes":[{"wrong":"Our firewall which is from 2020 is old.","right":"Our firewall, which is from 2020, is old.","why":"Non-defining → commas."},
    {"wrong":"The analyst, that wrote it, left.","right":"The analyst who wrote it left.","why":"Defining clauses about people use WHO; no commas."}],
   "tip":"Antivirus is now a commodity. Endpoint Detection and Response is the new floor for any serious enterprise. EDR sees behaviour, not just files, and ships with telemetry that fuels detection engineering."},
  "passage":{"title":"From firewalls to EDR","text":"For two decades, the perimeter firewall was the cornerstone of corporate security. The firewall, which inspected traffic at the network boundary, blocked unauthorised connections based on rules about ports and addresses. As applications moved to the cloud and employees moved to laptops, this model lost much of its relevance. The boundary that the firewall protected is now diffuse: data lives in many cloud providers and devices live everywhere.\n\nNext-generation firewalls added application awareness and TLS inspection. Web Application Firewalls, which sit in front of web applications, look at HTTP traffic for injection patterns. Both still matter, but the bigger story is at the endpoint.\n\nAntivirus, which was the consumer-grade endpoint control for decades, was based on signatures: known patterns of known threats. The model worked when malware was rare and slow-changing. Today's threats are polymorphic, fileless and often built specifically for the target. Endpoint Detection and Response, or EDR, replaced AV as the enterprise floor. EDR continuously records process execution, registry changes, network connections and file activity. Detection rules look for patterns that suggest malicious behaviour, even when no specific malware is known.\n\nExtended Detection and Response (XDR) is the natural next step. XDR, which integrates endpoint, network, identity and cloud telemetry, gives analysts a unified view of an incident. The challenge is no longer collecting data; it is sifting through too much of it. The most valuable engineers in modern security operations are those who write detections that fire on real attacks without flooding the analyst with noise.","wc":252,"source":"Adapted from NIST SP 800-41 (nist.gov, PD), Gartner public research summaries on EDR/XDR, and OWASP CRS public docs (CC BY-SA)."},
  "exercises":[
   {"type":"mcq","q":"What does WAF stand for?","options":["Wireless Authentication Frame","Web Application Firewall","Wide Area Filter","Wired Access Filter"],"a":1,"explain":"From the text."},
   {"type":"tfng","q":"AV is now considered the floor for enterprise endpoint security.","a":"F","explain":"'EDR replaced AV as the enterprise floor.'"},
   {"type":"gap","q":"___ integrates endpoint, network, identity and cloud telemetry.","a":"XDR","alts":["XDR"],"explain":"From the text."},
   {"type":"match","pairs":[["NGFW","app awareness, TLS inspection"],["WAF","HTTP injection patterns"],["EDR","behavioural endpoint"],["XDR","integrated telemetry"]]},
   {"type":"short","q":"Why has signature-based AV become insufficient?","model":"Model: Modern threats are polymorphic, fileless, and often built specifically for the target. Signatures only catch known patterns; they miss novel and behaviour-only attacks."}],
  "uoe":[
   {"type":"mc_cloze","sentence":"The firewall ___ deployed in 2020 is reaching end-of-life.","options":["who","that","whose","what"],"a":1,"explain":"Defining + thing → THAT (or which)."},
   {"type":"mc_cloze","sentence":"Our SIEM, ___ costs millions per year, has visibility gaps.","options":["that","which","who","when"],"a":1,"explain":"Non-defining → WHICH (THAT not allowed)."},
   {"type":"cloze","sentence":"The analyst ___ wrote that rule has left.","a":"who","alts":["who","that"],"explain":"Defining + person."},
   {"type":"cloze","sentence":"Vendors ___ products we test must follow the questionnaire.","a":"whose","alts":["whose"],"explain":"Possessive relative."},
   {"type":"word_form","base":"DETECT","sentence":"EDR is built on behavioural ___ .","a":"detection","alts":["detection"],"explain":"-tion noun."},
   {"type":"word_form","base":"VISIBLE","sentence":"XDR improves ___ across systems.","a":"visibility","alts":["visibility"],"explain":"-ility noun."},
   {"type":"key_word","original":"The CISO joined in 2024 and leads the migration.","key":"WHO","gap_template":"The CISO, ___ , leads the migration.","a":"who joined in 2024","alts":["who joined in 2024"],"explain":"Non-defining clause."},
   {"type":"key_word","original":"AV is based on signatures that match known patterns.","key":"WHICH","gap_template":"AV is based on signatures ___ known patterns.","a":"which match","alts":["which match"],"explain":"Defining (or non-defining) relative."}]},
 13: {  # Ethical hacking introduction (Present perfect vs past simple)
  "notes":{
   "warmup":"Ethical hacking is offensive security with permission. The skills are the same as criminal hacking; the legal authorisation, scope and intent are different. Confusing the two has ended careers.",
   "grammar":{"title":"Present perfect vs past simple","rule":"Present perfect = past event with present relevance, recent or unspecified time, life experience. Past simple = finished event at a specific past time. Time markers determine the choice.",
    "table":{"head":["Tense","Marker","Example"],"rows":[
     ["past simple","yesterday, last week, in 2020","I tested the API yesterday."],
     ["present perfect","ever, never, just, already, yet, since, for","I have tested 30 APIs in my career."],
     ["pres. perfect cont.","since/for + duration","I have been working in pentesting for five years."]]},
    "examples":[{"en":"I have run a pentest on this app twice.","note":"life experience, time unspecified"},
     {"en":"I ran a pentest on this app last May.","note":"specific past"},
     {"en":"She has just submitted her first bug bounty.","note":"recent + relevance"}]},
   "phrases":[{"phrase":"The scope of this engagement covers …","use":"define scope"},
    {"phrase":"This finding has critical impact because …","use":"impact statement"},
    {"phrase":"We followed responsible disclosure …","use":"ethical signal"},
    {"phrase":"The customer authorised testing of …","use":"authorisation"}],
   "mistakes":[{"wrong":"I have run the pentest yesterday.","right":"I ran the pentest yesterday.","why":"Specific time → past simple."},
    {"wrong":"I worked here since 2020.","right":"I have worked here since 2020.","why":"Action continues to now → present perfect."}],
   "tip":"Always have a written authorisation. Without it, the same scan that earns you a bonus on Tuesday earns you a court date on Wednesday."},
  "passage":{"title":"Inside an ethical hacking engagement","text":"Ethical hackers, also called penetration testers or red teamers, simulate the actions of real attackers to find weaknesses before criminals do. Their work is structured by the rules of engagement: a written agreement that defines what is in scope, what is off-limits, and what to do if testing accidentally affects production systems.\n\nA typical engagement begins with reconnaissance. The tester gathers information from public sources — DNS records, LinkedIn profiles, code repositories — building a picture of the target's attack surface. Active scanning follows: the tester probes services, fingerprints software versions, and looks for known vulnerabilities. Then comes exploitation: the tester attempts to gain access in controlled ways, escalates privileges where possible, and tries to move laterally to demonstrate the realistic impact of a compromise. Finally, post-exploitation activities document evidence and prepare for clean-up.\n\nThe report is the deliverable that customers actually pay for. A good report does not just list findings; it explains business impact, recommends prioritised remediation, and provides reproduction steps so that defenders can verify the fix. The best testers I have worked with have always treated the writing as the most important part of the engagement.\n\nThe legal context matters enormously. The US Department of Justice updated its CFAA charging policy in 2022 to abjure prosecution of good-faith security research. The UK Computer Misuse Act of 1990 has not been comparably reformed, despite a decade of campaigning by the CyberUp coalition. Researchers operating internationally have to navigate this patchwork carefully.","wc":253,"source":"Adapted from NIST SP 800-115 Technical Guide to Information Security Testing (nist.gov, PD), OWASP Web Security Testing Guide (owasp.org, CC BY-SA), and US DoJ CFAA Charging Policy 2022 (justice.gov, PD)."},
  "exercises":[
   {"type":"mcq","q":"What document defines what is in scope and off-limits?","options":["the bug bounty","the rules of engagement","the CFAA","the WSTG"],"a":1,"explain":"'Rules of engagement: a written agreement that defines…'"},
   {"type":"tfng","q":"The UK Computer Misuse Act has been reformed for ethical research.","a":"F","explain":"'Has not been comparably reformed.'"},
   {"type":"gap","q":"The most valuable part of the engagement, according to the author, is the ___ .","a":"report","alts":["report","writing"],"explain":"From the text."},
   {"type":"match","pairs":[["Reconnaissance","public-source intel"],["Exploitation","controlled access"],["Post-exploitation","clean-up"],["Report","prioritised remediation"]]},
   {"type":"short","q":"Why is written authorisation essential before testing?","model":"Model: Without written authorisation, the same activity is unauthorised access, which is criminal in most jurisdictions. Authorisation defines scope, protects the tester legally, and clarifies what to do if production is affected."}],
  "uoe":[
   {"type":"mc_cloze","sentence":"I ___ a pentest on this API last month.","options":["have run","ran","run","have been running"],"a":1,"explain":"'Last month' → past simple."},
   {"type":"mc_cloze","sentence":"She ___ in this field for ten years.","options":["worked","is working","has worked","work"],"a":2,"explain":"Duration up to now → present perfect."},
   {"type":"cloze","sentence":"The DoJ updated its CFAA charging policy ___ 2022.","a":"in","alts":["in"],"explain":"IN + year."},
   {"type":"cloze","sentence":"We ___ never seen this kind of chain before.","a":"have","alts":["have"],"explain":"NEVER + present perfect."},
   {"type":"word_form","base":"AUTHORISE","sentence":"Written ___ is essential before testing.","a":"authorisation","alts":["authorisation","authorization"],"explain":"-ation noun."},
   {"type":"word_form","base":"REMEDY","sentence":"The report includes prioritised ___ steps.","a":"remediation","alts":["remediation"],"explain":"-ation noun."},
   {"type":"key_word","original":"I started in pentesting five years ago.","key":"WORKING","gap_template":"I have ___ for five years.","a":"been working in pentesting","alts":["been working in pentesting","been working as a pentester"],"explain":"Present perfect continuous + duration."},
   {"type":"key_word","original":"The CFAA was last updated in 2022.","key":"AGO","gap_template":"The CFAA ___ updated.","a":"was last","alts":["was last"],"explain":"Adverb position."}]},
 14: {  # IoT devices and risks (Would for hypothetical)
  "notes":{
   "warmup":"By 2026, the average household has more connected devices than people. Each one is a potential attack surface — and a potential listener. Understanding the IoT threat model is no longer optional, even at home.",
   "grammar":{"title":"WOULD for hypotheticals (second conditional)","rule":"Form: IF + past simple, WOULD + base verb. Used for unreal or unlikely present/future situations and for polite suggestions.",
    "table":{"head":["Form","Use","Example"],"rows":[
     ["IF + past simple, would + base","unreal present","If everyone changed default passwords, Mirai would not exist."],
     ["I would + base","polite suggestion","I would segment IoT devices on a separate VLAN."],
     ["What would happen if …?","hypothetical question","What would happen if the camera were compromised?"]]},
    "examples":[{"en":"If we segmented IoT, lateral movement would be much harder.","note":"unreal present"},
     {"en":"I wouldn't put a smart speaker in a meeting room.","note":"polite recommendation"},
     {"en":"If you bought a cheap webcam, you would inherit its supply chain.","note":"hypothetical"}]},
   "phrases":[{"phrase":"This device sits on …","use":"network position"},
    {"phrase":"The default credentials are …","use":"flag risk"},
    {"phrase":"Firmware updates are …","use":"availability"},
    {"phrase":"In a worst-case scenario, …","use":"threat modelling"}],
   "mistakes":[{"wrong":"If the camera was compromised, what would happen.","right":"If the camera were compromised, what would happen?","why":"Formal second conditional uses WERE for all persons (WAS accepted informally)."},
    {"wrong":"If everybody would change passwords, Mirai not exists.","right":"If everybody changed passwords, Mirai would not exist.","why":"IF clause uses past simple; never WOULD."}],
   "tip":"Treat every IoT device as hostile until proven otherwise. Default-deny, segregate by VLAN, and require firmware updates before deployment. Consumer-grade IoT in corporate environments is a recurring incident pattern."},
  "passage":{"title":"The Internet of Things and its risks","text":"The Internet of Things describes the explosion of connected devices that surround modern life: smart bulbs, doorbell cameras, fitness trackers, industrial sensors, medical implants. Each adds value, and each adds risk. Many of these devices ship with default passwords, never receive firmware updates, and run software stacks that the original vendor stopped maintaining years ago.\n\nThe Mirai botnet of 2016 was a watershed moment. Mirai infected hundreds of thousands of cheap routers and IP cameras by trying a short list of default credentials. The infected devices were used to launch distributed denial-of-service attacks of unprecedented scale, taking down major DNS providers and household-name websites for hours. The most striking thing about Mirai was its simplicity: no zero-days, no clever exploits, just default passwords nobody had changed.\n\nIn industrial environments, the stakes are higher. Operational Technology controls power grids, water treatment plants, oil pipelines and factory floors. Stuxnet showed in 2010 what targeted OT malware can achieve. Recent incidents at water utilities and a US fuel pipeline have shown that less sophisticated attackers can also cause serious disruption when industrial controllers are connected to the internet without segmentation.\n\nIf consumer IoT manufacturers prioritised security as much as time-to-market, the situation would be very different. Regulators are slowly forcing change. The EU Cyber Resilience Act, the US IoT Cybersecurity Improvement Act, and the UK Product Security and Telecommunications Infrastructure Act all impose minimum requirements. Compliance is costly. Devices without it will be banned from the markets that adopt these laws.","wc":259,"source":"Adapted from CISA OT and IoT advisories (cisa.gov, PD), the Mirai botnet analysis published in academic literature, and ENISA reports on IoT security (enisa.europa.eu)."},
  "exercises":[
   {"type":"mcq","q":"How did Mirai infect devices?","options":["zero-day in firmware","default passwords","social engineering","supply chain attack"],"a":1,"explain":"'Trying a short list of default credentials.'"},
   {"type":"tfng","q":"Stuxnet targeted consumer IoT devices.","a":"F","explain":"'Stuxnet showed… what targeted OT malware can achieve.'"},
   {"type":"gap","q":"The EU regulation on connected products is the Cyber ___ Act.","a":"Resilience","alts":["Resilience"],"explain":"From the text."},
   {"type":"match","pairs":[["Mirai","DDoS, default credentials"],["Stuxnet","OT, targeted"],["Cyber Resilience Act","EU"],["IoT Cybersecurity Act","US"]]},
   {"type":"short","q":"Why is consumer IoT a recurring problem in corporate networks?","model":"Model: Consumer-grade devices ship with weak defaults, rarely receive updates, and are often connected without segmentation. They become persistent footholds and are hard to detect because they are not in any inventory."}],
  "uoe":[
   {"type":"mc_cloze","sentence":"If everybody ___ default passwords, Mirai would not exist.","options":["change","changed","would change","has changed"],"a":1,"explain":"2nd conditional IF: past simple."},
   {"type":"mc_cloze","sentence":"If we ___ IoT on a VLAN, lateral movement would be harder.","options":["segment","segmented","would segment","will segment"],"a":1,"explain":"Past simple in IF."},
   {"type":"cloze","sentence":"I ___ deploy unmanaged IoT in a corporate network.","a":"wouldn't","alts":["wouldn't","would not"],"explain":"Polite negative recommendation."},
   {"type":"cloze","sentence":"Treat every IoT device ___ hostile until proven otherwise.","a":"as","alts":["as"],"explain":"Treat AS."},
   {"type":"word_form","base":"SEGREGATE","sentence":"___ between IT and OT is essential.","a":"Segregation","alts":["Segregation"],"explain":"-ation noun."},
   {"type":"word_form","base":"COMPLY","sentence":"Devices without ___ will be banned.","a":"compliance","alts":["compliance"],"explain":"Verb → noun: -ance."},
   {"type":"key_word","original":"It would be safer to put cameras on a separate VLAN.","key":"PUT","gap_template":"Cameras ___ on a separate VLAN.","a":"would be safer put","alts":["would be safer to put on","should be put"],"explain":"Modal recommendation."},
   {"type":"key_word","original":"If manufacturers cared about security, IoT would be better.","key":"PRIORITISED","gap_template":"If manufacturers ___ security, IoT would be better.","a":"prioritised","alts":["prioritised","prioritized"],"explain":"2nd conditional past simple."}]},
 15: {  # AI & ML intro (Unless, as long as)
  "notes":{
   "warmup":"AI used to be a research curiosity; today it is part of every production stack. The vocabulary is changing fast and full of marketing. Knowing what the words really mean is now an engineering skill.",
   "grammar":{"title":"UNLESS, AS LONG AS, PROVIDED THAT","rule":"UNLESS = if not. AS LONG AS / PROVIDED (THAT) = on condition that. All take present simple in the conditional clause.",
    "table":{"head":["Connector","Meaning","Example"],"rows":[
     ["unless","if not","Models leak training data unless they are properly tuned."],
     ["as long as","on condition","ML works as long as the data is representative."],
     ["provided (that)","on condition (formal)","RAG is safe provided that documents are sanitised."],
     ["on condition that","formal","We will deploy on condition that we pass red-teaming."]]},
    "examples":[{"en":"You should not use customer data unless you have explicit consent.","note":"unless"},
     {"en":"LLMs are useful as long as you verify the output.","note":"as long as"},
     {"en":"We will release the model provided that the safety team approves.","note":"provided"}]},
   "phrases":[{"phrase":"The model has been trained on …","use":"describe data"},
    {"phrase":"This is a discriminative / generative model.","use":"classify"},
    {"phrase":"Hallucination occurs when …","use":"explain failure mode"},
    {"phrase":"Fine-tuning vs prompt engineering …","use":"contrast approaches"}],
   "mistakes":[{"wrong":"Unless you don't sanitise inputs, the model leaks.","right":"Unless you sanitise inputs, the model leaks.","why":"UNLESS already negative."},
    {"wrong":"As long as you will verify, you are safe.","right":"As long as you verify, you are safe.","why":"Conditional clause → present, never WILL."}],
   "tip":"Treat LLM outputs like user input: untrusted, fallible, and capable of triggering downstream actions. Prompt injection is the SQL injection of our era."},
  "passage":{"title":"What machine learning actually is","text":"Machine learning is a sub-field of artificial intelligence in which a computer learns patterns from data instead of being explicitly programmed. Within ML, three main paradigms coexist. Supervised learning trains on labelled data: classification of email as spam or not, prediction of customer churn. Unsupervised learning finds structure without labels: clustering, anomaly detection. Reinforcement learning rewards an agent for achieving objectives in an environment.\n\nDeep learning is a particular family within ML based on neural networks with many layers. The neural network architecture has not changed fundamentally since the 1980s, but the combination of huge datasets, GPUs, and clever training techniques has produced systems that perform astonishingly well on tasks like image recognition and natural-language processing.\n\nLarge Language Models, or LLMs, are the recent wave that has reached the mainstream. They are trained on enormous text corpora to predict the next token. ChatGPT, Claude and Gemini are LLMs accessed through chat interfaces. Their strengths are surprising; their failure modes are also surprising. They confidently generate plausible but false information ('hallucination'), they can be manipulated by adversarial prompts ('prompt injection'), and they reflect biases present in their training data.\n\nAs long as engineers understand these failure modes, LLMs are extraordinarily useful. Unless they understand them, deploying LLMs into critical decisions is dangerous. Retrieval-Augmented Generation grounds the model in trusted documents, which mitigates hallucination but introduces new risks if the document corpus is poisoned. The OWASP Top 10 for LLMs is a good starting point for any team building production AI systems.","wc":259,"source":"Adapted from MIT 6.S191 'Introduction to Deep Learning' (introtodeeplearning.com, CC BY-NC-SA), OWASP Top 10 for LLMs (owasp.org, CC BY-SA) and Anthropic / Stanford HAI public materials."},
  "exercises":[
   {"type":"mcq","q":"Which paradigm trains on labelled data?","options":["Supervised","Unsupervised","Reinforcement","Generative"],"a":0,"explain":"'Supervised learning trains on labelled data.'"},
   {"type":"tfng","q":"Hallucination is when an LLM refuses to answer.","a":"F","explain":"'They confidently generate plausible but false information.'"},
   {"type":"gap","q":"___ Generation grounds the model in trusted documents.","a":"Retrieval-Augmented","alts":["Retrieval-Augmented","RAG"],"explain":"From the text."},
   {"type":"match","pairs":[["Supervised","spam classification"],["Unsupervised","clustering"],["Reinforcement","reward signal"],["LLM","next-token prediction"]]},
   {"type":"short","q":"Why is RAG not a complete solution to hallucination?","model":"Model: RAG grounds answers in retrieved documents, but if the corpus is incomplete or poisoned, the model still produces incorrect outputs. RAG reduces hallucination but does not eliminate it."}],
  "uoe":[
   {"type":"mc_cloze","sentence":"LLMs are useful ___ you verify the output.","options":["unless","as long as","despite","whereas"],"a":1,"explain":"Positive condition."},
   {"type":"mc_cloze","sentence":"___ documents are sanitised, RAG is safe.","options":["Unless","As long as","Provided","Despite"],"a":2,"explain":"Provided + clause."},
   {"type":"cloze","sentence":"Models leak training data ___ they are properly tuned.","a":"unless","alts":["unless"],"explain":"UNLESS = if not."},
   {"type":"cloze","sentence":"Treat LLM outputs ___ untrusted user input.","a":"as","alts":["as","like"],"explain":"Treat AS."},
   {"type":"word_form","base":"HALLUCINATE","sentence":"Reducing ___ is a key research challenge.","a":"hallucination","alts":["hallucination"],"explain":"Verb → noun: -ation."},
   {"type":"word_form","base":"GENERATE","sentence":"LLMs are ___ models.","a":"generative","alts":["generative"],"explain":"-ive adjective."},
   {"type":"key_word","original":"You can deploy the model only if the safety team approves.","key":"PROVIDED","gap_template":"You can deploy the model ___ the safety team approves.","a":"provided that","alts":["provided that","provided"],"explain":"PROVIDED THAT = on condition that."},
   {"type":"key_word","original":"If you don't sanitise inputs, your model is vulnerable.","key":"UNLESS","gap_template":"___ inputs, your model is vulnerable.","a":"Unless you sanitise","alts":["Unless you sanitise","Unless you sanitize"],"explain":"UNLESS replaces 'if not'."}]},
 16: {  # Blockchain intro (Third conditional intro)
  "notes":{
   "warmup":"Blockchain is genuinely innovative for some problems and irrelevant for many others. Knowing the difference is part of professional vocabulary in 2026.",
   "grammar":{"title":"Third conditional (introduction)","rule":"Form: IF + past perfect, WOULD HAVE + past participle. Talks about how the past would have differed if a condition had been met. Counterfactual reasoning.",
    "table":{"head":["Form","Example"],"rows":[
     ["IF + past perfect, would have + p.p.","If they had audited the contract, the hack would not have happened."],
     ["WOULDN'T HAVE","If they had used MFA, the keys wouldn't have been stolen."],
     ["COULD HAVE / MIGHT HAVE","If we had bought BTC in 2010, we could have retired."]]},
    "examples":[{"en":"If The DAO had had timelocks, the attacker would not have succeeded.","note":"counterfactual"},
     {"en":"If the protocol had been more decentralised, governance would have been harder to capture.","note":"counterfactual"}]},
   "phrases":[{"phrase":"This protocol works by …","use":"explain"},
    {"phrase":"In proof-of-stake, validators …","use":"consensus mechanism"},
    {"phrase":"Smart contracts are …","use":"definition"},
    {"phrase":"The use case is questionable because …","use":"critical analysis"}],
   "mistakes":[{"wrong":"If they audited it, the hack wouldn't happen.","right":"If they had audited it, the hack wouldn't have happened.","why":"Past counterfactual → past perfect + would have p.p."},
    {"wrong":"If they would have used MFA, keys safe.","right":"If they had used MFA, keys would have been safe.","why":"IF clause → past perfect; never WOULD HAVE."}],
   "tip":"Most 'blockchain' projects could be a database. The genuine use cases — censorship-resistant value transfer, public-state transparency in adversarial environments — are narrower than the marketing suggests."},
  "passage":{"title":"Blockchain in plain English","text":"A blockchain is a distributed ledger maintained by many independent participants. Each block contains transactions, a timestamp, and a cryptographic hash of the previous block. Changing any historical block would invalidate every block after it, which makes the chain tamper-evident. Bitcoin, launched in 2009 by the pseudonymous Satoshi Nakamoto, was the first widely successful implementation. Ethereum, launched in 2015, generalised the model by adding a built-in programming language for smart contracts.\n\nConsensus is the hard part. Bitcoin uses Proof of Work: participants compete to solve cryptographic puzzles, and the winner adds the next block. The model is robust but consumes vast amounts of electricity. Proof of Stake replaces computational work with economic stake: validators lock up tokens and risk losing them if they misbehave. Ethereum migrated to Proof of Stake in 2022, reducing its energy consumption by more than 99%.\n\nSmart contracts are programs that run on the blockchain. They enable Decentralised Finance (DeFi), Non-Fungible Tokens (NFTs), and Decentralised Autonomous Organisations (DAOs). Their power is also their risk: smart contracts often hold significant value and are immutable once deployed. The 2016 DAO hack, in which an attacker drained roughly 60 million dollars worth of ETH through a re-entrancy bug, would not have happened if the team had subjected the contract to formal verification. Repeated DeFi exploits since then have followed similar patterns.\n\nFor a systems engineer, the practical question is whether a given problem actually needs decentralisation. If the answer is no, blockchain adds complexity without proportional benefit.","wc":260,"source":"Adapted from Bitcoin and Ethereum white papers (bitcoin.org, ethereum.org, public), and DeFi exploit analyses from Rekt News public reports."},
  "exercises":[
   {"type":"mcq","q":"What does Ethereum's 2022 transition reduce?","options":["transaction cost","block size","energy consumption","number of validators"],"a":2,"explain":"'Reducing its energy consumption by more than 99%.'"},
   {"type":"tfng","q":"Smart contracts can be edited after deployment.","a":"F","explain":"'Immutable once deployed.'"},
   {"type":"gap","q":"The DAO hack drained approximately ___ million dollars.","a":"60","alts":["60","sixty"],"explain":"From the text."},
   {"type":"match","pairs":[["PoW","Bitcoin"],["PoS","modern Ethereum"],["DeFi","decentralised finance"],["NFT","non-fungible token"]]},
   {"type":"short","q":"When does blockchain genuinely add value over a database?","model":"Model: When trust is genuinely distributed and adversarial — for example, censorship-resistant value transfer or public-state transparency where no single party can be trusted to maintain the ledger."}],
  "uoe":[
   {"type":"mc_cloze","sentence":"If The DAO ___ formal verification, the hack would not have happened.","options":["had used","used","has used","would have used"],"a":0,"explain":"3rd conditional IF: past perfect."},
   {"type":"mc_cloze","sentence":"If we ___ Bitcoin in 2010, we would have retired.","options":["had bought","bought","have bought","would have bought"],"a":0,"explain":"Past perfect."},
   {"type":"cloze","sentence":"The chain is tamper-___ because changing a block invalidates the next.","a":"evident","alts":["evident","resistant"],"explain":"Compound adjective."},
   {"type":"cloze","sentence":"Validators lock ___ tokens to participate.","a":"up","alts":["up"],"explain":"'Lock up'."},
   {"type":"word_form","base":"DECENTRALISE","sentence":"DeFi means ___ finance.","a":"decentralised","alts":["decentralised","decentralized"],"explain":"-ed past participle adjective."},
   {"type":"word_form","base":"AUTONOMOUS","sentence":"DAOs are decentralised ___ organisations.","a":"autonomous","alts":["autonomous"],"explain":"Adj unchanged."},
   {"type":"key_word","original":"They didn't audit the contract, so the hack happened.","key":"AUDITED","gap_template":"If they ___ the contract, the hack would not have happened.","a":"had audited","alts":["had audited"],"explain":"3rd conditional + past perfect."},
   {"type":"key_word","original":"Without timelocks, the attacker drained the funds.","key":"HAD","gap_template":"If they ___ timelocks, the attacker wouldn't have drained the funds.","a":"had had","alts":["had had","had implemented"],"explain":"3rd conditional past perfect of HAVE."}]},
 17: {  # Project management (Should/ought to + perfect)
  "notes":{
   "warmup":"Most engineering failures are not technical. They are coordination failures: vague scope, unclear ownership, missing handoffs. Project management vocabulary is part of engineering vocabulary.",
   "grammar":{"title":"SHOULD HAVE + past participle","rule":"Used for past criticism, regret, or hindsight: 'we should have tested it'. Negative: SHOULDN'T HAVE. Same pattern with OUGHT TO HAVE (more formal).",
    "table":{"head":["Form","Use","Example"],"rows":[
     ["should have + p.p.","past advice/regret","We should have estimated more time."],
     ["shouldn't have + p.p.","criticism","We shouldn't have skipped the retro."],
     ["ought to have + p.p.","formal advice","The team ought to have raised the risk earlier."],
     ["could have + p.p.","past possibility","We could have automated this years ago."]]},
    "examples":[{"en":"The PO should have prioritised security stories.","note":"hindsight"},
     {"en":"We shouldn't have promised a date without estimating.","note":"regret"},
     {"en":"They could have spotted the dependency in planning.","note":"missed possibility"}]},
   "phrases":[{"phrase":"The acceptance criteria are …","use":"definition"},
    {"phrase":"This story is blocked by …","use":"dependency"},
    {"phrase":"Definition of done: …","use":"quality bar"},
    {"phrase":"The retrospective revealed …","use":"learning"}],
   "mistakes":[{"wrong":"We should tested it.","right":"We should have tested it.","why":"SHOULD + HAVE + p.p."},
    {"wrong":"You shouldn't to have skipped it.","right":"You shouldn't have skipped it.","why":"No 'to' between SHOULDN'T and HAVE."}],
   "tip":"Estimate in story points, not hours. Hours invite false precision. Points capture relative complexity, which is what teams actually have intuition about."},
  "passage":{"title":"Agile in the real world","text":"Most modern software teams describe themselves as agile, but the practice varies enormously. The Agile Manifesto of 2001 emphasised individuals and interactions over processes, working software over comprehensive documentation, customer collaboration over contract negotiation, and responding to change over following a plan. Two decades later, those values are widely accepted; their implementation is the contested part.\n\nScrum is the most common framework. A Scrum team has three roles: a Product Owner who prioritises the backlog, a Scrum Master who facilitates the process, and developers who deliver the work. Sprints are typically two weeks long. Each sprint begins with planning, runs through daily stand-ups, and ends with a review of the increment and a retrospective on the process.\n\nKanban, by contrast, has no fixed iterations. Work flows continuously through stages — backlog, in progress, in review, done — with limits on work in progress that prevent overload. Kanban suits operational work where priorities change frequently. Many real teams use a hybrid: Scrum for new development, Kanban for support and bug fixes.\n\nCommon failure patterns are well documented. Sprints become endurance tests when scope expands during the sprint. Stand-ups become status reports rather than coordination meetings. Retrospectives become rituals where teams complain about the same problems for months. The classic post-mortem comment — 'we should have raised this risk earlier' — appears so often that wise teams turn it into a checklist item. Effective project management is not about following a framework rigidly; it is about building feedback loops that surface problems while they are still cheap to fix.","wc":265,"source":"Adapted from the Scrum Guide (scrumguides.org, CC BY-SA), the Agile Manifesto (agilemanifesto.org, public), and the Kanban method public material."},
  "exercises":[
   {"type":"mcq","q":"Which framework has no fixed iterations?","options":["Scrum","Kanban","Waterfall","SAFe"],"a":1,"explain":"'Kanban, by contrast, has no fixed iterations.'"},
   {"type":"tfng","q":"The Agile Manifesto states processes over individuals.","a":"F","explain":"'Individuals and interactions over processes.'"},
   {"type":"gap","q":"A Scrum sprint is typically ___ weeks long.","a":"two","alts":["two","2"],"explain":"From the text."},
   {"type":"match","pairs":[["Product Owner","prioritises the backlog"],["Scrum Master","facilitates"],["Stand-up","daily coordination"],["Retrospective","process review"]]},
   {"type":"short","q":"Why do retrospectives sometimes lose their value?","model":"Model: When teams complain about the same problems month after month without acting on them, retrospectives become rituals rather than improvement loops. Effective retros translate complaints into specific actions with owners and timelines."}],
  "uoe":[
   {"type":"mc_cloze","sentence":"We ___ the dependency in planning.","options":["should spot","should have spotted","should spotted","should had spot"],"a":1,"explain":"SHOULD HAVE + p.p."},
   {"type":"mc_cloze","sentence":"You ___ the retro.","options":["shouldn't skip","shouldn't have skipped","shouldn't have skip","wouldn't skip"],"a":1,"explain":"Past criticism."},
   {"type":"cloze","sentence":"The team ought ___ have raised the risk earlier.","a":"to","alts":["to"],"explain":"OUGHT + TO + HAVE."},
   {"type":"cloze","sentence":"The PO is responsible ___ prioritising the backlog.","a":"for","alts":["for"],"explain":"Responsible FOR."},
   {"type":"word_form","base":"COORDINATE","sentence":"Stand-ups should be ___ , not status reports.","a":"coordination","alts":["coordination"],"explain":"-ation noun (or coordinational)."},
   {"type":"word_form","base":"DELIVER","sentence":"Each sprint produces a working ___ .","a":"deliverable","alts":["deliverable","delivery"],"explain":"-able noun."},
   {"type":"key_word","original":"It was a mistake not to test the integration.","key":"TESTED","gap_template":"We ___ the integration.","a":"should have tested","alts":["should have tested"],"explain":"Hindsight + p.p."},
   {"type":"key_word","original":"The team didn't escalate the risk early.","key":"OUGHT","gap_template":"The team ___ the risk earlier.","a":"ought to have escalated","alts":["ought to have escalated"],"explain":"OUGHT TO HAVE + p.p."}]},
 18: {  # Writing technical emails (linkers: however, moreover)
  "notes":{
   "warmup":"In international IT teams, your written English defines how senior you sound. The grammar is rarely the bottleneck. Structure, register and conciseness are.",
   "grammar":{"title":"Linking words: HOWEVER, MOREOVER, THEREFORE, NEVERTHELESS","rule":"Use sentence-level connectors followed by a comma to make professional writing flow. They go at the start of a new sentence, not joining two clauses.",
    "table":{"head":["Linker","Function","Example"],"rows":[
     ["However","contrast","The patch is critical. However, the maintenance window is full."],
     ["Moreover / Furthermore","addition","The system is slow. Moreover, the logs are corrupted."],
     ["Therefore / Consequently","cause/effect","The disk is full. Therefore, backups are failing."],
     ["Nevertheless","strong contrast","The risk is documented. Nevertheless, leadership has approved go-live."]]},
    "examples":[{"en":"The vulnerability is severe. However, exploit code is not yet public.","note":"contrast"},
     {"en":"We have completed testing. Moreover, we have run a load test.","note":"addition"},
     {"en":"The team is stretched. Therefore, we propose hiring a contractor.","note":"effect"}]},
   "phrases":[{"phrase":"Following our last conversation, …","use":"reference"},
    {"phrase":"Could you please confirm whether …","use":"polite question"},
    {"phrase":"Please find attached …","use":"attachment"},
    {"phrase":"I would appreciate your confirmation by …","use":"deadline"}],
   "mistakes":[{"wrong":"The patch is critical, however the window is full.","right":"The patch is critical. However, the window is full.","why":"HOWEVER starts a new sentence, with a comma."},
    {"wrong":"Moreover of that, the logs are corrupted.","right":"Moreover, the logs are corrupted.","why":"MOREOVER stands alone."}],
   "tip":"In a professional email, lead with the ask. The first sentence should make clear what you need from the reader. The rest is justification."},
  "passage":{"title":"A professional escalation email","text":"Subject: Action required: vulnerability CVE-2026-12345 in production database\n\nDear Mark,\n\nFollowing our security review on Tuesday, I am writing to escalate a finding that I consider time-sensitive. Our production database server is running version 14.2.0 of PostgreSQL, which is affected by CVE-2026-12345. The vulnerability allows unauthenticated remote code execution. The patched version, 14.2.1, has been available since last week.\n\nWe should patch by this Friday at the latest. However, the standard maintenance window is fully booked until next month. I would propose we treat this as an emergency change. Moreover, similar CVEs have already been observed in the wild within forty-eight hours of disclosure. Therefore, the risk of waiting is, in my judgement, unacceptable.\n\nI have attached a draft change request and a rollback plan. Could you please confirm whether you can sponsor this as an emergency change? I would appreciate your confirmation by 17:00 today, so that we can coordinate with the database team and execute over the weekend if approved.\n\nNevertheless, if you have a different reading of the risk, I am very open to discussing it. I am available for a quick call any time before 16:00.\n\nThank you for your time.\n\nBest regards,\nLaura Mendoza\nSenior Systems Engineer","wc":216,"source":"Original. Email register and CVE handling consistent with NIST SP 800-40 patch management guidance (nist.gov, PD)."},
  "exercises":[
   {"type":"mcq","q":"What is Laura asking Mark to do?","options":["delay the patch","sponsor an emergency change","attend a meeting","approve a hire"],"a":1,"explain":"'Sponsor this as an emergency change.'"},
   {"type":"tfng","q":"Similar CVEs are usually exploited within a year.","a":"F","explain":"'Within forty-eight hours of disclosure.'"},
   {"type":"gap","q":"The version that fixes the issue is 14.2.___.","a":"1","alts":["1"],"explain":"'Patched version, 14.2.1.'"},
   {"type":"match","pairs:":[["However","contrast"],["Moreover","addition"],["Therefore","effect"],["Nevertheless","strong contrast"]],
    "pairs":[["However","contrast"],["Moreover","addition"],["Therefore","effect"],["Nevertheless","strong contrast"]]},
   {"type":"short","q":"Why does Laura include 'I am very open to discussing it'?","model":"Model: To soften the escalation tone and signal that she respects Mark's authority and judgement, while still pushing for urgent action. It is a register move, not a retreat."}],
  "uoe":[
   {"type":"mc_cloze","sentence":"The patch is critical. ___ , the window is full.","options":["But","However","Despite","Although"],"a":1,"explain":"Sentence-initial linker → HOWEVER."},
   {"type":"mc_cloze","sentence":"Tests passed. ___ , we ran a load test.","options":["Moreover","However","Therefore","Nevertheless"],"a":0,"explain":"Addition → MOREOVER."},
   {"type":"cloze","sentence":"The disk is full. ___ , backups are failing.","a":"Therefore","alts":["Therefore","Consequently"],"explain":"Cause/effect."},
   {"type":"cloze","sentence":"I would appreciate your confirmation ___ 17:00.","a":"by","alts":["by"],"explain":"Deadline preposition."},
   {"type":"word_form","base":"ESCALATE","sentence":"This issue requires immediate ___ .","a":"escalation","alts":["escalation"],"explain":"-ation noun."},
   {"type":"word_form","base":"DISCLOSE","sentence":"Within 48 hours of ___ , similar CVEs are exploited.","a":"disclosure","alts":["disclosure"],"explain":"-ure noun."},
   {"type":"key_word","original":"Although the window is full, we must patch.","key":"NEVERTHELESS","gap_template":"The window is full. ___ , we must patch.","a":"Nevertheless","alts":["Nevertheless"],"explain":"Sentence-initial concession."},
   {"type":"key_word","original":"Because the risk is high, we propose emergency change.","key":"THEREFORE","gap_template":"The risk is high. ___ , we propose an emergency change.","a":"Therefore","alts":["Therefore"],"explain":"Cause/effect linker."}]},
 19: {  # Giving a short technical talk (Discourse markers)
  "notes":{
   "warmup":"Engineers underestimate how much speaking matters in their careers. The technical work is judged by how clearly it is communicated. A good 5-minute talk can change a team's direction.",
   "grammar":{"title":"Discourse markers for talks","rule":"Discourse markers signal what is happening in your talk: signposting, transitions, emphasis, summary. They are mostly fixed phrases learned as chunks.",
    "table":{"head":["Function","Markers","Example"],"rows":[
     ["Open","Today I'd like to talk about / I'm going to cover","Today I'd like to talk about our migration."],
     ["Signpost","First, / Next, / Finally,","First, I'll describe the problem."],
     ["Transition","Moving on, / Turning to,","Moving on, let's look at the costs."],
     ["Emphasis","The key point is / What this means is","The key point is reliability."],
     ["Summary","To sum up, / In conclusion,","To sum up, three takeaways."]]},
    "examples":[{"en":"Today I'd like to talk about three things.","note":"opening"},
     {"en":"Moving on, let me show you the architecture.","note":"transition"},
     {"en":"In summary, we have three options.","note":"closing"}]},
   "phrases":[{"phrase":"Thanks for joining.","use":"open"},
    {"phrase":"Let me know if I am clear.","use":"check"},
    {"phrase":"I'll come back to that.","use":"defer question"},
    {"phrase":"That's a great question.","use":"acknowledge"}],
   "mistakes":[{"wrong":"I will explanation about migration.","right":"I'm going to explain the migration.","why":"GOING TO + base verb."},
    {"wrong":"To summarise of the talk, three points.","right":"To summarise the talk, three points.","why":"No 'of' after TO SUMMARISE."}],
   "tip":"Rule of three: structure your talk around three main points. Audiences remember three. Two feels thin. Five feels exhausting."},
  "passage":{"title":"Anatomy of a 5-minute talk","text":"Good morning everyone, and thank you for joining. I'm Carlos Mendez, senior systems engineer in the platform team. Today I'd like to talk about our cloud migration. I'll cover three things: where we are, what we have learned, and what we propose for next quarter.\n\nFirst, where we are. We started the migration in January. As of today, we have moved sixty per cent of services from our on-premise data centre to AWS. The remaining services are mostly databases and integrations with legacy systems.\n\nMoving on, what we have learned. Two things stand out. The first is that the lift-and-shift approach is faster but produces higher running costs. We are paying more on AWS than we were on-premise for some workloads, simply because we did not redesign them. The second is that observability matters. Without good monitoring, you do not know whether the new environment is working until users complain.\n\nFinally, what we propose for next quarter. We want to slow down the lift-and-shift, and start a parallel track of refactoring the most expensive workloads. This will take more engineering time but will reduce running cost by an estimated thirty per cent.\n\nIn summary: sixty per cent migrated, two key lessons, and a proposal to refactor instead of rushing. I am happy to take questions. Thank you.","wc":230,"source":"Original. Talk structure inspired by 'Talk Like TED' (Carmine Gallo) and IEEE professional communication guidance."},
  "exercises":[
   {"type":"mcq","q":"How much has been migrated so far?","options":["30%","50%","60%","90%"],"a":2,"explain":"'We have moved sixty per cent.'"},
   {"type":"tfng","q":"Lift-and-shift produces lower running costs.","a":"F","explain":"'Higher running costs.'"},
   {"type":"gap","q":"The proposed refactoring will reduce cost by an estimated ___ per cent.","a":"thirty","alts":["thirty","30"],"explain":"From the text."},
   {"type":"match","pairs":[["First","signpost"],["Moving on","transition"],["Finally","closing signpost"],["In summary","conclusion"]]},
   {"type":"short","q":"What are the two lessons Carlos highlights?","model":"Model: 1) Lift-and-shift is faster but produces higher running costs because workloads are not redesigned. 2) Observability matters; without monitoring, problems only surface when users complain."}],
  "uoe":[
   {"type":"mc_cloze","sentence":"Today I'd ___ to talk about three things.","options":["like","liked","liking","be like"],"a":0,"explain":"WOULD LIKE TO."},
   {"type":"mc_cloze","sentence":"___ , let me show you the architecture.","options":["Although","Therefore","Moving on","Despite"],"a":2,"explain":"Transition marker."},
   {"type":"cloze","sentence":"In ___ , three takeaways.","a":"summary","alts":["summary","conclusion"],"explain":"Closing."},
   {"type":"cloze","sentence":"That's a great ___ . Let me come back to it.","a":"question","alts":["question"],"explain":"Q&A acknowledgement."},
   {"type":"word_form","base":"OBSERVE","sentence":"___ matters in cloud migrations.","a":"Observability","alts":["Observability"],"explain":"-ability noun."},
   {"type":"word_form","base":"REFACTOR","sentence":"___ workloads reduces cost.","a":"Refactoring","alts":["Refactoring"],"explain":"-ing gerund as subject."},
   {"type":"key_word","original":"Now I will talk about the costs.","key":"TURNING","gap_template":"___ to the costs.","a":"Turning now","alts":["Turning now","Turning"],"explain":"Discourse marker."},
   {"type":"key_word","original":"To sum up, three points.","key":"SUMMARISE","gap_template":"To ___ , three points.","a":"summarise","alts":["summarise","summarize"],"explain":"Closing infinitive."}]},
 20: {  # Mock PET + B1 project
  "notes":{
   "warmup":"You are ready for the B1 Preliminary (PET) exam. The exam tests integrated skills with realistic IT and general topics. This last lesson recaps strategy and key grammar.",
   "grammar":{"title":"B1 grammar recap","rule":"B1 brings together: present perfect vs past simple, conditionals 0/1/2, modals of deduction, passive voice, reported speech, gerunds vs infinitives, defining and non-defining clauses.",
    "table":{"head":["Area","Mini-rule"],"rows":[
     ["Pres. perfect","experience or recent action with present relevance"],
     ["Conditional 1","real future: if + present, will + base"],
     ["Conditional 2","unreal present: if + past, would + base"],
     ["Passive","focus on action, not actor"],
     ["Reported speech","tense shift back, no inversion in questions"]]},
    "examples":[{"en":"I have worked in security for five years.","note":"present perfect"},
     {"en":"If we had backups, we wouldn't pay the ransom.","note":"2nd conditional"},
     {"en":"The data was encrypted before exfiltration.","note":"passive past"}]},
   "phrases":[{"phrase":"Could you say that again, please?","use":"clarify"},
    {"phrase":"I'd say …","use":"hedge opinion"},
    {"phrase":"It depends on …","use":"qualified answer"},
    {"phrase":"In my experience, …","use":"personal evidence"}],
   "mistakes":[{"wrong":"I am working in security since 2020.","right":"I have been working in security since 2020.","why":"Duration to now → present perfect (continuous)."},
    {"wrong":"He told that he is tired.","right":"He said he was tired.","why":"TELL needs object; reported tense shift."}],
   "tip":"In the speaking test, develop your answers. A two-sentence answer beats a one-word answer every time. Build the habit: state, then justify with 'because' or 'for example'."},
  "passage":{"title":"Ready for B1","text":"My name is Daniel and I have been studying English for two years. When I started, I could only describe simple things. Now I can read tech articles, understand video calls in English, and write professional emails to colleagues abroad. I have also passed two practice PET exams with scores around 145 on the Cambridge scale, which is a B1 borderline B2.\n\nIn the last six months, I have focused on Use of English. The transformations were hard at first. If I had not done the daily exercises, I would still be struggling with passive forms and reported speech. The reading is now my strongest skill. I read at least one IEEE Spectrum article a week, and I take notes on five new words each time.\n\nThe weakest area is still listening. Native speakers talk fast, especially in podcasts. I now listen to VOA Learning English at full speed and to BBC Radio Tech twice a week. The first listen is for general meaning, the second for details. I have noticed that my comprehension has jumped in the past month.\n\nThe exam is in three weeks. My plan is: one practice paper every Saturday, vocabulary review every morning, and one IT podcast every evening. If I keep this routine, I will pass. After PET, I want to start B2 First. My goal is C1 in two years and a senior position abroad in three.","wc":238,"source":"Original. PET exam structure from Cambridge Assessment English handbook (cambridgeenglish.org)."},
  "exercises":[
   {"type":"mcq","q":"How long has Daniel been studying English?","options":["one year","two years","three years","five years"],"a":1,"explain":"'For two years.'"},
   {"type":"tfng","q":"Listening is Daniel's strongest skill.","a":"F","explain":"'The weakest area is still listening.'"},
   {"type":"gap","q":"Daniel scored around ___ on the Cambridge scale.","a":"145","alts":["145"],"explain":"From the text."},
   {"type":"match","pairs":[["Reading","strongest"],["Listening","weakest"],["Use of English","improved with daily practice"],["Speaking","natural progress"]]},
   {"type":"short","q":"Write a 4-sentence study plan for the next 3 weeks at B1.","model":"Model: I will do one practice paper every Saturday. I will review 20 new words every morning. I will listen to one tech podcast every evening, twice. I will write one short essay each Sunday and self-evaluate."}],
  "uoe":[
   {"type":"mc_cloze","sentence":"I ___ in security for five years.","options":["am working","work","have worked","worked"],"a":2,"explain":"Duration up to now."},
   {"type":"mc_cloze","sentence":"If we ___ backups, we wouldn't pay the ransom.","options":["have","had","would have","will have"],"a":1,"explain":"2nd conditional past simple."},
   {"type":"cloze","sentence":"The data was encrypted ___ exfiltration.","a":"before","alts":["before"],"explain":"Time preposition."},
   {"type":"cloze","sentence":"He said he ___ tired.","a":"was","alts":["was"],"explain":"Reported tense shift."},
   {"type":"word_form","base":"COMPREHEND","sentence":"My listening ___ has improved.","a":"comprehension","alts":["comprehension"],"explain":"-sion noun."},
   {"type":"word_form","base":"NATIVE","sentence":"___ speakers talk fast.","a":"Native","alts":["Native"],"explain":"Adjective unchanged."},
   {"type":"key_word","original":"It is two years since I started English.","key":"FOR","gap_template":"I have ___ two years.","a":"studied English for","alts":["studied English for","been studying English for"],"explain":"FOR + duration."},
   {"type":"key_word","original":"Daniel did the daily exercises and improved.","key":"NOT","gap_template":"If Daniel ___ done the daily exercises, he would still be struggling.","a":"had not","alts":["had not","hadn't"],"explain":"3rd conditional intro."}]},
}
}

# ---- MERGE ----
path = Path(r"E:\CLAUDE\PAOLO BACA MANRIQUE\course-app\course_data.json")
course = json.loads(path.read_text(encoding="utf-8"))

merged_lessons = 0
for level in course["levels"]:
    code = level["code"]
    for lesson in level["lessons"]:
        entry = EXP.get(code, {}).get(lesson["n"])
        if not entry:
            continue
        if lesson.get("has_content"):
            continue
        if entry.get("notes"):
            lesson["lesson_notes"] = entry["notes"]
        if entry.get("passage"):
            p = entry["passage"]
            lesson["passage"] = {
                "title": p.get("title", lesson["topic"]),
                "text": p["text"],
                "word_count": p.get("wc", len(p["text"].split())),
                "source": p["source"],
            }
        if entry.get("exercises"):
            lesson["exercises"] = entry["exercises"]
        if entry.get("uoe"):
            lesson["use_of_english"] = entry["uoe"]
        lesson["has_content"] = True
        merged_lessons += 1

path.write_text(json.dumps(course, ensure_ascii=False, indent=1), encoding="utf-8")

print(f"OK: Added full content to {merged_lessons} lessons")
for lv in course["levels"]:
    filled = sum(1 for le in lv["lessons"] if le.get("has_content"))
    uoe = sum(len(le.get("use_of_english",[])) for le in lv["lessons"])
    print(f"  {lv['code']}: {filled}/20 lessons, {uoe} UoE exercises")
