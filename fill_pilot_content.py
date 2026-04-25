# -*- coding: utf-8 -*-
"""
Pilot content for Systems Engineers English Course.
30 clases (5 por nivel x 6 niveles) con:
 - Passage original calibrado CEFR (longitud y densidad l\u00e9xica)
 - 5 ejercicios con clave (MCQ, T/F/NG, gap-fill, matching, short-answer)
 - Fuente verificada (dominio y licencia)

Niveles y longitudes objetivo:
 A1: 80-100 w   A2: 150-180 w   B1: 280-340 w
 B2: 420-480 w  C1: 600-680 w   C2: 780-880 w
"""
import json
from pathlib import Path

PILOT = {
# =========================================================================
"A1": {
 1: {
  "title":"Hello, I'm a systems engineer",
  "passage": (
   "Hello. My name is Juan Torres. I am twenty-four years old. I am from Lima, Peru. "
   "I am a junior systems engineer. I work at a tech company in San Isidro. "
   "My team has five people. My manager is Ana. She is nice. I go to the office every day. "
   "I start work at nine. I check emails. I help users with their computers. "
   "I fix small problems. I write short reports. At one, I have lunch. "
   "At six, I go home. I like my job. It is not difficult for me."
  ),
  "source":"Original. Inspired by VOA Learning English (learningenglish.voanews.com) \u2013 US gov, public domain.",
  "exercises":[
   {"type":"mcq","q":"What is Juan's job?",
    "options":["pilot","systems engineer","doctor","teacher"],"a":1,
    "explain":"Sentence 4: 'I am a junior systems engineer.'"},
   {"type":"tfng","q":"Juan starts work at eight o'clock.","a":"F",
    "explain":"He starts at nine."},
   {"type":"gap","q":"Juan's manager is ____.","a":"Ana",
    "alts":["ana"]},
   {"type":"match","pairs":[
    ["Juan's age","24"],["City","Lima"],["Team size","5"],["Lunch time","1 pm"]]},
   {"type":"short","q":"Describe your own job in 2 short sentences.",
    "model":"Model: I am a student. I study systems engineering at the university."}
  ]
 },
 2: {
  "title":"The alphabet of URLs and emails",
  "passage": (
   "In IT, we spell many words. We spell URLs. We spell emails. This is hard on the phone. "
   "Some letters sound the same. B and D are hard. M and N are hard. We use code words. "
   "B is Bravo. D is Delta. M is Mike. N is November. This is the NATO alphabet. "
   "For URLs, we say 'dot' for '.' and 'slash' for '/'. For emails, we say 'at' for '@'. "
   "Be careful with zero (0) and the letter O. They look the same. "
   "When you write a URL, write it in lower case. URLs do not like spaces."
  ),
  "source":"Original. NATO phonetic alphabet: public domain (NATO STANAG 5040).",
  "exercises":[
   {"type":"mcq","q":"How do we spell 'B' in the NATO alphabet?",
    "options":["Boy","Bravo","Beta","Bear"],"a":1,
    "explain":"'B is Bravo.'"},
   {"type":"tfng","q":"M and N sound very different on the phone.","a":"F",
    "explain":"The text says M and N are hard."},
   {"type":"gap","q":"We say '____' for the @ symbol.","a":"at","alts":["at"]},
   {"type":"match","pairs":[
    ["@","at"],[".","dot"],["/","slash"],["D","Delta"]]},
   {"type":"short","q":"Spell your email using NATO letters for difficult letters.",
    "model":"Model: p-a-o-l-o at g-mail dot com \u2192 Papa-Alpha-Oscar-Lima-Oscar at Golf-Mike-Alpha-India-Lima dot Charlie-Oscar-Mike."}
  ]
 },
 3: {
  "title":"Numbers, versions and dates",
  "passage": (
   "Software has versions. For example, Windows 11. Or Python 3.12.4. "
   "Numbers are important. The first number is big. We call it 'major'. "
   "The second is 'minor'. The third is 'patch'. A patch is a small fix. "
   "Big numbers mean big changes. Small numbers mean small fixes. "
   "Dates are also important. Companies release updates on special days. "
   "Microsoft uses Patch Tuesday. It is the second Tuesday of the month. "
   "Engineers check for updates. They install them. This keeps computers safe. "
   "If you do not install updates, hackers can enter your system."
  ),
  "source":"Original. Based on Semantic Versioning spec (semver.org) \u2013 CC BY 3.0; Microsoft Patch Tuesday is a public industry term.",
  "exercises":[
   {"type":"mcq","q":"What is the third number in a version?",
    "options":["major","minor","patch","final"],"a":2,
    "explain":"'The third is patch.'"},
   {"type":"tfng","q":"Patch Tuesday happens every Monday.","a":"F",
    "explain":"It is on the second Tuesday of the month."},
   {"type":"gap","q":"In Python 3.12.4, the number '12' is the ____ number.",
    "a":"minor","alts":["minor"]},
   {"type":"match","pairs":[
    ["major","big changes"],["minor","medium changes"],["patch","small fix"],
    ["Patch Tuesday","second Tuesday"]]},
   {"type":"short","q":"Check the version of your phone OS. Write it.",
    "model":"Model: My phone uses Android 14.0.2."}
  ]
 },
 4: {
  "title":"Hardware parts",
  "passage": (
   "A computer has many parts. The CPU is the brain. It does the work. "
   "The RAM is the short memory. The SSD or hard disk is the long memory. "
   "These parts are inside the computer. The monitor shows pictures. "
   "The keyboard is for typing. The mouse is for pointing. We call these peripherals. "
   "A laptop has all parts together in one box. A desktop is bigger. "
   "It has a tower. The tower is the main box. Servers are very big computers. "
   "They live in data centers. Data centers are big buildings with many servers. "
   "They are always on, 24 hours, 7 days."
  ),
  "source":"Original. Inspired by NIST Glossary (nist.gov) \u2013 US gov, public domain.",
  "exercises":[
   {"type":"mcq","q":"Which part is the 'brain' of the computer?",
    "options":["RAM","SSD","CPU","monitor"],"a":2,
    "explain":"'The CPU is the brain.'"},
   {"type":"tfng","q":"A laptop has its parts separate in different boxes.","a":"F",
    "explain":"Laptops have all parts together."},
   {"type":"gap","q":"The ____ is for typing.","a":"keyboard","alts":["keyboard"]},
   {"type":"match","pairs":[
    ["CPU","brain"],["RAM","short memory"],["SSD","long memory"],["tower","main box of a desktop"]]},
   {"type":"short","q":"Name 3 parts of the computer you are using now.",
    "model":"Model: My laptop has a screen, a keyboard and a touchpad."}
  ]
 },
 5: {
  "title":"Software basics",
  "passage": (
   "Software is the program on your computer. Some software is free. "
   "Some software costs money. Windows is not free. Linux is free. "
   "We install software from the official website of the company. "
   "First, we download the file. Then we click on it. A small window opens. "
   "It says 'Next'. We click 'Next', 'Next', 'Next'. Sometimes it asks for our password. "
   "This is normal. At the end, we click 'Finish'. The program is ready. "
   "We can open it now. Always download from the official website. "
   "Do not use strange sites. They can have viruses. Your antivirus can stop many viruses, but not all."
  ),
  "source":"Original. Inspired by CISA guidance (cisa.gov/stopransomware) \u2013 US gov, public domain.",
  "exercises":[
   {"type":"mcq","q":"Linux is...",
    "options":["expensive","free","a phone","a CPU"],"a":1,
    "explain":"'Linux is free.'"},
   {"type":"tfng","q":"You always click 'Next' only one time during install.","a":"F",
    "explain":"'We click Next, Next, Next.'"},
   {"type":"gap","q":"Strange sites can have ____.","a":"viruses","alts":["viruses","virus","malware"]},
   {"type":"match","pairs":[
    ["Windows","not free"],["Linux","free"],["Next","install step"],["Finish","last step"]]},
   {"type":"short","q":"Name one free program you use every day.",
    "model":"Model: I use Firefox every day. It is a free browser."}
  ]
 },
},
# =========================================================================
"A2": {
 1: {
  "title":"Describing IT jobs",
  "passage": (
   "In a modern IT department, there are many different jobs. "
   "A systems engineer designs, builds, and maintains the company's servers and networks. "
   "She also writes documentation and trains new users. "
   "A software developer, on the other hand, writes code. "
   "She programs applications, tests them, and fixes bugs. "
   "These two jobs are very different, but they work together every day. "
   "There are also levels. A junior engineer has less than two years of experience. "
   "A senior engineer has five years or more. A lead engineer guides the team and makes decisions. "
   "A SOC analyst watches for cyber attacks all day. She checks alerts on her screens and reports problems quickly. "
   "In Peru, a junior IT worker usually earns between 3,000 and 4,500 soles per month. "
   "A senior can earn more than 8,000. The IT industry grows every year, "
   "and good English is now almost as important as good technical skills."
  ),
  "source":"Original. Inspired by OpenLearn 'IT careers' (open.edu/openlearn) \u2013 CC BY-NC-SA 4.0.",
  "exercises":[
   {"type":"mcq","q":"Who writes code in a company?",
    "options":["the systems engineer","the software developer","the SOC analyst","the manager"],
    "a":1,"explain":"'A software developer writes code.'"},
   {"type":"tfng","q":"A lead engineer has less experience than a junior.","a":"F",
    "explain":"'A senior has 5+ years; lead guides the team.'"},
   {"type":"gap","q":"A ____ analyst watches for cyber attacks.","a":"SOC","alts":["soc","SOC"]},
   {"type":"match","pairs":[
    ["junior","<2 years experience"],["senior","5+ years"],
    ["lead","guides the team"],["SOC analyst","watches for attacks"]]},
   {"type":"short","q":"Which IT job do you like most? Give 2 reasons.",
    "model":"Model: I like the SOC analyst job because I enjoy investigating and I am always curious."}
  ]
 },
 2: {
  "title":"My work history",
  "passage": (
   "My name is Maria, and I am a systems engineer. I started my career in 2019. "
   "My first job was at a small company in Arequipa. I worked on the help desk. "
   "I answered phone calls, solved easy problems, and reset many passwords. "
   "After one year, I moved to a bank in Lima. The bank was much bigger. "
   "There, I learned a lot about network security and firewalls. "
   "In 2022, I changed jobs again. Now I work at a cloud company. "
   "I design systems on AWS and I manage a small team. I like my new job. "
   "It is more technical and more challenging. My English is very important. "
   "Many of my meetings are in English because my colleagues are from the United States and Spain. "
   "Every year, I try to learn something new. Last year, I got a certificate in cybersecurity. "
   "Next year, I want to study machine learning. In our industry, you have to keep learning. "
   "If you don't, you fall behind quickly."
  ),
  "source":"Original. Scenario; career data from ENISA workforce reports (enisa.europa.eu).",
  "exercises":[
   {"type":"mcq","q":"Where did Maria start her career?",
    "options":["Lima","Arequipa","Trujillo","Cuzco"],"a":1,
    "explain":"'My first job was at a small company in Arequipa.'"},
   {"type":"tfng","q":"Maria still works at the bank.","a":"F",
    "explain":"'In 2022, I changed jobs again.'"},
   {"type":"gap","q":"Maria now designs systems on ____.","a":"AWS",
    "alts":["aws","AWS"]},
   {"type":"match","pairs":[
    ["2019","help desk, Arequipa"],["2020\u20132022","bank, Lima"],
    ["2022\u2013now","cloud company"],["Next year","study ML"]]},
   {"type":"short","q":"Describe one learning goal you have for next year.",
    "model":"Model: Next year I want to pass the Cisco CCNA exam because networks interest me."}
  ]
 },
 3: {
  "title":"Operating systems compared",
  "passage": (
   "There are three main operating systems today: Windows, Linux, and macOS. "
   "Windows is the most popular for office computers. It is not free; you pay for a license. "
   "Windows is user-friendly, and most commercial programs run on it. "
   "Linux is free and open source. This means anyone can read the code and change it. "
   "Linux is very popular for servers. More than 90% of cloud servers in the world run Linux. "
   "macOS is the system used on Apple computers. It is only for Mac devices. "
   "It is elegant and powerful, and many developers prefer it because it has a Unix base, like Linux. "
   "Each system has strengths and weaknesses. Windows has the most games and commercial software. "
   "Linux is the most flexible. macOS has the best design and build quality. "
   "For security, Linux is often safer because less malware targets it, but no system is 100% safe. "
   "All users must update their systems regularly and use strong passwords. "
   "If you are new to IT, start with Windows. Then learn Linux later; it will be essential for your career."
  ),
  "source":"Original. Statistics consistent with W3Techs public server-OS survey; Unix lineage from MIT OCW 6.828 (ocw.mit.edu) CC BY-NC-SA.",
  "exercises":[
   {"type":"mcq","q":"Which OS is free and open source?",
    "options":["Windows","Linux","macOS","iOS"],"a":1,
    "explain":"'Linux is free and open source.'"},
   {"type":"tfng","q":"macOS works on any computer, not only Apple.","a":"F",
    "explain":"'It is only for Mac devices.'"},
   {"type":"gap","q":"More than ____% of cloud servers run Linux.","a":"90","alts":["90","ninety"]},
   {"type":"match","pairs":[
    ["Windows","most games and commercial software"],
    ["Linux","most flexible; dominates servers"],
    ["macOS","Unix base; best build quality"],["All","must be updated regularly"]]},
   {"type":"short","q":"Which OS do you use, and why?",
    "model":"Model: I use Windows at work because my company requires it, but I use Linux at home to practice."}
  ]
 },
 4: {
  "title":"Installing software safely",
  "passage": (
   "Installing software is an everyday task for IT workers, but it is also one of the most common security risks. "
   "The process has several steps if you want to do it safely. "
   "First, always go to the official website of the software. Never use third-party download sites, "
   "because they often repackage installers with malware. Second, download the installer file. "
   "On Windows, it usually ends in .exe or .msi. On macOS, it ends in .dmg. On Linux, it is a .deb or .rpm. "
   "Third, verify the file. Good projects publish a SHA-256 hash next to the download link. "
   "You can calculate the hash of your file and compare the two. If they match, the file has not been modified. "
   "Fourth, run the installer. You may need administrator rights. The system will ask for your password; "
   "this is normal. Fifth, follow the wizard carefully. Read each screen. Many installers include extra software "
   "that you do not need, like toolbars or trial programs. Uncheck those boxes. "
   "Sixth, restart the computer if the installer asks for it. Finally, open the program and test it. "
   "If something does not work, check the application logs for error messages before asking for help."
  ),
  "source":"Original. Based on CISA 'Supply-Chain Software' guidance (cisa.gov) \u2013 US gov, PD.",
  "exercises":[
   {"type":"mcq","q":"Where should you download software from?",
    "options":["any site","the official website","social media links","email attachments"],
    "a":1,"explain":"'Always go to the official website.'"},
   {"type":"tfng","q":"On Windows, installer files often end in .dmg.","a":"F",
    "explain":".dmg is macOS; Windows uses .exe or .msi."},
   {"type":"gap","q":"You can check the file with a ____ hash.","a":"SHA-256",
    "alts":["sha-256","sha256","SHA-256","SHA256"]},
   {"type":"match","pairs":[
    [".exe","Windows"],[".dmg","macOS"],[".deb","Linux (Debian/Ubuntu)"],[".rpm","Linux (Red Hat/Fedora)"]]},
   {"type":"short","q":"What do you do if the program does not start after install?",
    "model":"Model: I check the application logs, read the error message, and search for the error online."}
  ]
 },
 5: {
  "title":"Web browsers and privacy",
  "passage": (
   "A web browser is the program we use to see web pages. The most popular browsers today are "
   "Chrome, Firefox, Safari, and Edge. Chrome has the biggest market share with about 65%. "
   "Firefox is famous for its strong focus on privacy. Safari comes pre-installed on macOS and iPhones. "
   "Edge is the modern browser from Microsoft. All browsers do the same basic things: "
   "you type a URL, and the browser shows the page. However, each one has different features. "
   "Chrome has the largest library of extensions. Firefox has strict tracking protection by default. "
   "Safari is very fast and efficient on Apple devices. Edge integrates well with Windows and Microsoft 365. "
   "For safety, you must keep your browser updated. Old browsers often have security problems that "
   "criminals can use to attack you. Also, be careful with extensions. Only install extensions from "
   "the official store, and only if they have good reviews. Some extensions steal your data or show ads. "
   "A useful tip is to use incognito mode for private browsing. It does not save your history or cookies, "
   "but it does not hide you from your internet provider or from the websites you visit. "
   "For real privacy, you need a VPN or the Tor browser. Both options have advantages and disadvantages."
  ),
  "source":"Original. Browser market-share figures consistent with StatCounter public data; privacy guidance from EFF (eff.org) \u2013 CC BY.",
  "exercises":[
   {"type":"mcq","q":"Which browser is famous for its privacy focus?",
    "options":["Chrome","Firefox","Edge","Internet Explorer"],"a":1,
    "explain":"'Firefox is famous for its strong focus on privacy.'"},
   {"type":"tfng","q":"Incognito mode hides you from your internet provider.","a":"F",
    "explain":"'It does not hide you from your internet provider.'"},
   {"type":"gap","q":"For real privacy, you need a ____ or the Tor browser.","a":"VPN",
    "alts":["vpn","VPN"]},
   {"type":"match","pairs":[
    ["Chrome","most extensions"],["Firefox","best default privacy"],
    ["Safari","fast on Apple devices"],["Edge","Windows + Microsoft 365 integration"]]},
   {"type":"short","q":"Which browser do you use and why?",
    "model":"Model: I use Firefox because I care about privacy and I like its tracking protection."}
  ]
 },
},
# =========================================================================
"B1": {
 1: {
  "title":"The Software Development Lifecycle",
  "passage": (
   "The Software Development Lifecycle, or SDLC, describes every stage that software goes through, "
   "from the first idea to its final retirement. In the traditional waterfall model, each stage must "
   "finish before the next one can start. The five main stages are requirements, design, implementation, "
   "testing, and maintenance. Engineers begin by gathering requirements from stakeholders, including users, "
   "managers, and clients. They document exactly what the software should do and what it should not do. "
   "The design stage then defines the system architecture, the components, and the interfaces between them. "
   "Developers write the actual code during implementation, and testers verify that the code works correctly.\n\n"
   "However, waterfall has been largely replaced by agile approaches in the last two decades. "
   "Agile breaks the project into small iterations called sprints, usually two weeks long. "
   "At the end of every sprint, the team delivers a working piece of software that stakeholders can use and review. "
   "Scrum is the most common agile framework. A Scrum team has a product owner who prioritises the work, "
   "a Scrum Master who removes obstacles, and developers who actually build the software.\n\n"
   "Today, most modern companies go further and practise continuous integration and continuous delivery, "
   "usually written as CI/CD. With CI/CD, every time a developer pushes new code to the repository, "
   "automated pipelines test it and deploy it to production. Large companies like Amazon and Netflix "
   "deploy thousands of times every single day. But speed brings new risks: if a bug reaches production, "
   "it can affect millions of users in minutes. That is why modern teams also practise DevSecOps, "
   "integrating security checks directly into the pipeline from the beginning. Tools such as SAST, SCA, "
   "and secret scanning run automatically on every commit, so that security issues can be caught "
   "before the code ever goes live."
  ),
  "source":"Original. Methodologies from Scrum Guide (scrumguides.org, CC BY-SA) and NIST SP 800-160 (nist.gov, PD).",
  "exercises":[
   {"type":"mcq","q":"In the waterfall model, the stages happen...",
    "options":["in any order","in strict sequential order","at the same time","only when requested"],
    "a":1,"explain":"'Each stage must finish before the next can start.'"},
   {"type":"tfng","q":"A Scrum sprint usually lasts one month.","a":"F",
    "explain":"'Sprints are usually two weeks long.'"},
   {"type":"gap","q":"CI/CD stands for continuous ____ and continuous delivery.",
    "a":"integration","alts":["integration"]},
   {"type":"match","pairs":[
    ["Product Owner","prioritises the work"],
    ["Scrum Master","removes obstacles"],
    ["Developers","build the software"],
    ["DevSecOps","security in the pipeline"]]},
   {"type":"short","q":"Explain one risk of deploying to production many times per day.",
    "model":"Model: If a bug passes the tests, it reaches millions of users in minutes, so rollback plans and monitoring are essential."}
  ]
 },
 2: {
  "title":"Programming languages overview",
  "passage": (
   "Today there are hundreds of programming languages, but only about twenty are really popular in industry. "
   "According to surveys such as the TIOBE Index and the Stack Overflow Developer Survey, the top languages "
   "in 2026 include Python, JavaScript, TypeScript, Java, C#, C++, Go, and Rust. Each language has its own "
   "strengths, and engineers usually learn three or four during their career.\n\n"
   "Python is known for its clean syntax and huge ecosystem of libraries, especially for data science, "
   "machine learning, and automation. JavaScript and its typed brother TypeScript dominate the web: "
   "almost every website uses them. Java and C# are very popular in large companies and banks because "
   "they are mature, stable, and have excellent tooling. C and C++ are still essential for systems "
   "programming, operating systems, and performance-critical code. Go, created by Google, is used for "
   "backend services and cloud infrastructure; Kubernetes itself is written in Go. Rust is the newest "
   "of the popular languages and is famous for being memory-safe without a garbage collector.\n\n"
   "The choice of language matters for security, too. C and C++ are extremely powerful but they allow "
   "memory bugs, which have caused thousands of vulnerabilities over the years. Memory-safe languages "
   "like Rust, Go, and Java prevent many of these bugs by design. In fact, the United States government, "
   "through CISA, has encouraged companies to migrate critical software from C to memory-safe alternatives "
   "whenever it is realistic. For a student starting today, the advice is usually the same: learn Python first "
   "for its simplicity, then add JavaScript for the web, and later a systems language like Go or Rust."
  ),
  "source":"Original. CISA memory-safety guidance from 'The Case for Memory Safe Roadmaps' (cisa.gov, PD).",
  "exercises":[
   {"type":"mcq","q":"Which language was created by Google and is used for Kubernetes?",
    "options":["Rust","Python","Go","Java"],"a":2,
    "explain":"'Go, created by Google, is used for backend services\u2026 Kubernetes itself is written in Go.'"},
   {"type":"tfng","q":"Rust uses a garbage collector to manage memory.","a":"F",
    "explain":"'\u2026memory-safe without a garbage collector.'"},
   {"type":"gap","q":"CISA encourages migration from C to memory-____ languages.",
    "a":"safe","alts":["safe"]},
   {"type":"match","pairs":[
    ["Python","data science, ML, automation"],
    ["TypeScript","the web"],
    ["C/C++","OS, performance"],
    ["Rust","memory-safe systems"]]},
   {"type":"short","q":"Which language would you learn first, and why?",
    "model":"Model: I would learn Python first because the syntax is clean and I can use it for scripts, data, and web APIs."}
  ]
 },
 3: {
  "title":"Databases: relational vs document",
  "passage": (
   "A database is an organised collection of data that a computer can query quickly. "
   "There are two big families of databases today: relational databases, also called SQL databases, "
   "and non-relational databases, often called NoSQL. Relational databases have been the standard "
   "since the 1970s, when Edgar Codd described them at IBM. They store data in tables with fixed rows "
   "and columns, and they enforce strict rules called 'ACID properties' to guarantee that transactions "
   "are reliable. Popular relational databases include PostgreSQL, MySQL, Oracle, and Microsoft SQL Server. "
   "Engineers talk to them using a language called SQL.\n\n"
   "NoSQL databases appeared around 2009, when companies like Google, Amazon and Facebook needed to handle "
   "enormous volumes of data from millions of simultaneous users. NoSQL is an umbrella term that actually "
   "contains several different models. Document databases, like MongoDB, store data as flexible JSON objects. "
   "Key-value stores, like Redis, are extremely fast. Column-family databases, like Cassandra, scale across "
   "hundreds of servers. Graph databases, like Neo4j, are optimised for relationships, which makes them ideal "
   "for social networks.\n\n"
   "Choosing between SQL and NoSQL depends on the problem. If your data is structured and transactions must "
   "be 100% consistent \u2013 a bank account, for example \u2013 then SQL is still the right answer. If your data is "
   "flexible, changes often, and you need to scale horizontally across many servers, NoSQL is usually better. "
   "In practice, large systems use both: a relational database for core business data and a NoSQL database "
   "for logs, sessions, or product catalogues. From a security point of view, the biggest risk for both is "
   "injection attacks: SQL injection for relational databases and NoSQL injection for document databases. "
   "Using parameterised queries prevents almost all of them."
  ),
  "source":"Original. Based on OWASP Top 10 A03 Injection (owasp.org, CC BY-SA) and on Codd, E. F., 'A Relational Model of Data' (1970, public IBM research).",
  "exercises":[
   {"type":"mcq","q":"Which of these is a graph database?",
    "options":["MongoDB","Redis","Neo4j","Cassandra"],"a":2,
    "explain":"'Graph databases, like Neo4j\u2026'"},
   {"type":"tfng","q":"NoSQL is a single type of database.","a":"F",
    "explain":"'NoSQL is an umbrella term that contains several models.'"},
   {"type":"gap","q":"Using ____ queries prevents almost all injection attacks.",
    "a":"parameterised","alts":["parameterized","parameterised","prepared"]},
   {"type":"match","pairs":[
    ["PostgreSQL","relational"],["MongoDB","document"],["Redis","key-value"],["Neo4j","graph"]]},
   {"type":"short","q":"For a banking application, would you choose SQL or NoSQL? Justify.",
    "model":"Model: I would choose SQL because bank transactions must be 100% consistent (ACID), and a relational database enforces that by design."}
  ]
 },
 4: {
  "title":"Cloud computing \u2013 IaaS, PaaS, SaaS",
  "passage": (
   "Cloud computing has transformed the IT industry in less than twenty years. "
   "Instead of owning and operating their own data centres, most companies today rent computing resources "
   "from cloud providers such as Amazon Web Services, Microsoft Azure, and Google Cloud. "
   "The National Institute of Standards and Technology, NIST, published a simple definition in the document "
   "SP 800-145. According to NIST, there are three main service models: Infrastructure as a Service, "
   "Platform as a Service, and Software as a Service. These are usually shortened to IaaS, PaaS, and SaaS.\n\n"
   "With IaaS, the customer rents virtual machines, storage, and networks. The provider manages the physical "
   "hardware, but the customer installs the operating system, patches it, and manages everything else. "
   "Amazon EC2 is the classic example. PaaS goes one step further: the provider manages the operating system "
   "and the runtime, and the customer simply uploads application code. Google App Engine and Heroku are "
   "typical PaaS offerings. With SaaS, the provider manages the whole stack and the customer only uses the "
   "application through a browser. Gmail, Dropbox, and Salesforce are SaaS products that almost everyone has used.\n\n"
   "An important concept in cloud security is the shared responsibility model. The provider is responsible for "
   "the security 'of' the cloud, meaning the physical data centre, the hardware, and the core infrastructure. "
   "The customer is responsible for the security 'in' the cloud, meaning their data, their users, their "
   "configuration and their code. In the last few years, many companies have suffered breaches not because "
   "AWS or Azure were hacked, but because they left a storage bucket open to the internet by mistake. "
   "The famous 2019 Capital One breach is an example: a misconfigured web application firewall in AWS "
   "allowed an attacker to access more than 100 million customer records."
  ),
  "source":"Original. NIST SP 800-145 (nist.gov, PD); shared responsibility model documented by AWS, Azure and GCP.",
  "exercises":[
   {"type":"mcq","q":"In the NIST model, which service model lets the customer only use an application in the browser?",
    "options":["IaaS","PaaS","SaaS","DaaS"],"a":2,
    "explain":"'With SaaS, the customer only uses the application through a browser.'"},
   {"type":"tfng","q":"In the shared responsibility model, the provider is responsible for data configuration by the customer.","a":"F",
    "explain":"'The customer is responsible for their data and configuration.'"},
   {"type":"gap","q":"The 2019 ____ One breach exposed over 100 million customer records.",
    "a":"Capital","alts":["capital","Capital"]},
   {"type":"match","pairs":[
    ["IaaS","rent VMs and networks"],
    ["PaaS","upload code, provider runs the OS"],
    ["SaaS","use the app in a browser"],
    ["Shared responsibility","provider + customer"]]},
   {"type":"short","q":"Why is the shared responsibility model important for cybersecurity?",
    "model":"Model: Because many breaches occur from customer misconfiguration, not provider failures; teams must know which controls are theirs."}
  ]
 },
 5: {
  "title":"Networks and the TCP/IP stack",
  "passage": (
   "When you open a website, dozens of small things happen in less than a second. "
   "Your computer uses a set of protocols known as the TCP/IP stack, which has four layers. "
   "The link layer deals with physical networks, like Wi-Fi and Ethernet. The internet layer, which uses "
   "the IP protocol, gives every device an address and decides how packets travel between networks. "
   "The transport layer, which mostly uses TCP or UDP, controls how packets are delivered. "
   "The application layer is where protocols such as HTTP, DNS, and SMTP live.\n\n"
   "TCP is a reliable protocol. Before sending any data, it performs a three-way handshake: "
   "the client sends a SYN packet, the server answers with SYN-ACK, and the client confirms with ACK. "
   "Only after this handshake does real data start to flow. UDP, on the other hand, does not do any "
   "handshake. It simply sends packets and hopes for the best. UDP is faster, so it is used for video calls, "
   "games, and DNS lookups, where speed is more important than perfect delivery.\n\n"
   "From a security point of view, every layer of the stack has its own risks. At the link layer, attackers "
   "can use ARP spoofing to redirect traffic on a local network. At the internet layer, IP spoofing and "
   "fragmentation attacks are classic techniques. At the transport layer, a SYN flood attack sends millions of "
   "half-open connections to overload a server. At the application layer, the list is longer: phishing, "
   "SQL injection, cross-site scripting, and many more. A good engineer needs to understand all four layers "
   "at least at a high level, because real attacks often combine weaknesses from more than one layer."
  ),
  "source":"Original. Layered model from RFC 1122 (ietf.org / rfc-editor.org, public standards); attack examples from OWASP (owasp.org, CC BY-SA) and MITRE ATT&CK (attack.mitre.org).",
  "exercises":[
   {"type":"mcq","q":"Which protocol is reliable and performs a three-way handshake?",
    "options":["UDP","TCP","IP","ARP"],"a":1,
    "explain":"'TCP is a reliable protocol\u2026 three-way handshake.'"},
   {"type":"tfng","q":"UDP performs a handshake before sending data.","a":"F",
    "explain":"'UDP does not do any handshake.'"},
   {"type":"gap","q":"A SYN flood attack targets the ____ layer.","a":"transport",
    "alts":["transport"]},
   {"type":"match","pairs":[
    ["HTTP","application layer"],["TCP/UDP","transport layer"],
    ["IP","internet layer"],["Ethernet","link layer"]]},
   {"type":"short","q":"Give one example of an attack at the application layer.",
    "model":"Model: SQL injection: an attacker inserts malicious SQL code through a form to read or modify the database."}
  ]
 },
},
# =========================================================================
"B2": {
 1: {
  "title":"Cybersecurity incident response",
  "passage": (
   "When a cyber incident occurs, the difference between a minor disruption and a catastrophic breach "
   "is almost always the quality of the response. The National Institute of Standards and Technology, "
   "NIST, published Special Publication 800-61 Revision 2, which has become the de facto reference across "
   "the industry. It describes a four-phase lifecycle: Preparation, Detection and Analysis, Containment "
   "Eradication and Recovery, and Post-Incident Activity. Each phase is critical, and skipping any of them "
   "tends to have serious consequences later.\n\n"
   "Preparation is the phase that organisations often underestimate. It includes writing playbooks, "
   "building the CSIRT or Computer Security Incident Response Team, practising tabletop exercises and "
   "making sure that basic logging is enabled across every endpoint. A mature programme also includes "
   "retainer agreements with external forensic firms, because a small team rarely has the capacity to "
   "investigate a large-scale compromise alone. When an alert arrives, analysts move to Detection and "
   "Analysis. They triage the event, assess its severity, build an initial timeline, and try to identify "
   "indicators of compromise. Modern SOCs rely heavily on SIEM platforms, EDR agents and threat intelligence "
   "feeds during this phase.\n\n"
   "Containment can be short-term or long-term. Short-term containment means isolating the affected host "
   "immediately, for example by cutting its network connection. Long-term containment includes rebuilding "
   "systems from clean images and rotating credentials. Eradication removes the attacker's tools, persistence "
   "mechanisms and backdoors, while Recovery brings systems back to normal operation with enhanced monitoring "
   "for at least 30 days.\n\n"
   "The final phase, Post-Incident Activity, is where learning happens. A blameless retrospective identifies "
   "what worked, what failed, and which controls need to change. The 2020 SolarWinds compromise, which "
   "affected thousands of organisations including several US federal agencies, is a textbook case study: "
   "it demonstrated the limits of perimeter thinking and accelerated adoption of Zero Trust architectures "
   "worldwide. It also showed how deeply attackers can hide in the software supply chain, a risk that many "
   "organisations had seriously underestimated until then."
  ),
  "source":"Adapted from NIST SP 800-61 Rev 2 (nist.gov, PD) and CISA SolarWinds analysis (cisa.gov, PD).",
  "exercises":[
   {"type":"mcq","q":"Which NIST document defines the incident response lifecycle?",
    "options":["SP 800-53","SP 800-61","SP 800-207","ISO 27001"],"a":1,
    "explain":"'NIST\u2026 SP 800-61 Revision 2\u2026'"},
   {"type":"tfng","q":"Post-incident activity is skipped when the incident is contained.","a":"F",
    "explain":"'\u2026where learning happens\u2026'"},
   {"type":"gap","q":"Isolating an affected host by cutting its network connection is an example of short-term ____.",
    "a":"containment","alts":["containment"]},
   {"type":"match","pairs":[
    ["Preparation","playbooks, CSIRT, tabletop exercises"],
    ["Detection & Analysis","triage, timeline, IOCs"],
    ["Eradication","remove attacker tools"],
    ["Post-incident","blameless retrospective"]]},
   {"type":"short","q":"Why did SolarWinds accelerate Zero Trust adoption?",
    "model":"Model: Because attackers moved laterally after entering through a trusted update, showing that perimeter-based trust assumptions were no longer safe."}
  ]
 },
 2: {
  "title":"Network security architecture",
  "passage": (
   "Modern enterprise networks look nothing like the flat, trusted LANs of the 1990s. Today, segmentation, "
   "defence in depth and strong identity controls are considered baseline requirements, not optional extras. "
   "A well-designed architecture combines perimeter controls, micro-segmentation inside the network, and "
   "rigorous east-west inspection between workloads.\n\n"
   "At the perimeter, next-generation firewalls, or NGFWs, inspect not only IP addresses and ports, but also "
   "application protocols and TLS metadata. Web Application Firewalls, or WAFs, sit in front of web apps and "
   "block common attacks like SQL injection and cross-site scripting. Intrusion detection and prevention "
   "systems generate alerts for suspicious patterns and, in prevention mode, actively drop malicious packets. "
   "DMZs \u2013 demilitarised zones \u2013 isolate public-facing servers from the internal network, so that a compromise "
   "of the web server does not immediately reach the databases.\n\n"
   "Inside the network, micro-segmentation goes several steps further than traditional VLAN-based segmentation. "
   "Each workload is placed in a tiny zone, and only strictly necessary flows are allowed. If an attacker "
   "compromises one server, they cannot easily pivot to another. Approaches such as SASE (Secure Access "
   "Service Edge) combine network security and SD-WAN into a single cloud-delivered service, while ZTNA "
   "(Zero Trust Network Access) replaces traditional VPNs with per-application, identity-aware access.\n\n"
   "TLS inspection deserves a special mention. Because more than 95% of enterprise traffic is now encrypted, "
   "blind spots have grown. Many organisations terminate TLS at a security appliance to inspect payloads "
   "for malware before re-encrypting the traffic. This practice, however, creates its own privacy, performance "
   "and compliance challenges, and it must be balanced carefully against employee rights and regulatory "
   "constraints. A good reference architecture, therefore, is never only technology \u2013 it is the result of a "
   "continuous conversation between security engineers, legal teams, privacy officers and the business."
  ),
  "source":"Adapted from NIST SP 800-207 Zero Trust Architecture (nist.gov, PD) and ENISA 'Guidelines for Securing the IoT' (enisa.europa.eu).",
  "exercises":[
   {"type":"mcq","q":"Which of these replaces traditional VPNs with per-application, identity-aware access?",
    "options":["NGFW","WAF","ZTNA","DMZ"],"a":2,
    "explain":"'ZTNA\u2026 replaces traditional VPNs with per-application, identity-aware access.'"},
   {"type":"tfng","q":"Micro-segmentation is the same as traditional VLAN segmentation.","a":"F",
    "explain":"'Micro-segmentation goes several steps further than VLAN-based segmentation.'"},
   {"type":"gap","q":"A ____ sits in front of web applications and blocks SQL injection and XSS.",
    "a":"WAF","alts":["WAF","waf","web application firewall"]},
   {"type":"match","pairs":[
    ["NGFW","perimeter, layer 7 inspection"],
    ["WAF","web app protection"],
    ["DMZ","isolates public servers"],
    ["SASE","cloud-delivered network security + SD-WAN"]]},
   {"type":"short","q":"Give two drawbacks of performing TLS inspection in an enterprise.",
    "model":"Model: It creates privacy concerns because the company can see employee traffic, and it can introduce performance bottlenecks and legal/compliance issues."}
  ]
 },
 3: {
  "title":"Ransomware and double extortion",
  "passage": (
   "Ransomware is no longer the amateur phenomenon it was a decade ago. The ecosystem has matured into "
   "a professional criminal industry, often organised as Ransomware-as-a-Service, or RaaS. In this model, "
   "a core developer group builds and maintains the malware, while affiliates conduct the actual intrusions "
   "and split the ransom, typically 70\u201380% for the affiliate and the rest for the core operators. Initial "
   "access is frequently bought from specialised brokers who sell corporate credentials or ready-to-use "
   "footholds on underground markets.\n\n"
   "Since around 2019, almost every major operator has moved to double extortion. Before encrypting files, "
   "attackers exfiltrate gigabytes or even terabytes of sensitive data. If the victim refuses to pay, the "
   "criminals publish the data on a leak site. Some groups, such as LockBit and ALPHV, have gone further "
   "and added triple extortion, launching DDoS attacks or contacting the victim's customers directly. "
   "For public companies, the reputational damage can exceed the operational impact of the encryption itself.\n\n"
   "The 2021 attack on Colonial Pipeline is a textbook case. A single compromised VPN credential gave the "
   "DarkSide group access to the internal network. Fearing lateral movement into operational technology, "
   "Colonial shut down the pipeline for six days, triggering fuel shortages across the Eastern United States. "
   "The company paid roughly 4.4 million US dollars in Bitcoin, and although the FBI later recovered most of "
   "it, the lesson was clear: modern organisations can no longer treat ransomware as a purely technical problem.\n\n"
   "Paying or not paying is a complex decision involving legal, ethical and operational dimensions. In some "
   "jurisdictions, payments to sanctioned groups are now illegal. Insurance companies are increasingly "
   "reluctant to reimburse ransoms. The only durable defence is a combination of strong identity controls, "
   "immutable backups, effective detection, and rehearsed response playbooks. Tested backups, in particular, "
   "are the single most important control: if data can be restored quickly from a clean copy, attackers lose "
   "most of their leverage, whatever encryption they have deployed."
  ),
  "source":"Adapted from CISA StopRansomware advisories (cisa.gov, PD) and ENISA Threat Landscape 2024 (enisa.europa.eu).",
  "exercises":[
   {"type":"mcq","q":"In RaaS, who typically conducts the actual intrusions?",
    "options":["The core developers","The affiliates","Government agencies","The victim\u2019s staff"],
    "a":1,"explain":"'Affiliates conduct the actual intrusions\u2026'"},
   {"type":"tfng","q":"Triple extortion can include DDoS or contacting the victim's customers.","a":"T",
    "explain":"'\u2026launching DDoS attacks or contacting the victim's customers\u2026'"},
   {"type":"gap","q":"Initial access is frequently bought from specialised ____ on underground markets.",
    "a":"brokers","alts":["brokers","access brokers","IABs"]},
   {"type":"match","pairs":[
    ["RaaS","business model"],
    ["Double extortion","encrypt + leak"],
    ["Triple extortion","+ DDoS / customer pressure"],
    ["Immutable backups","main durable defence"]]},
   {"type":"short","q":"Give two reasons why paying the ransom is risky.",
    "model":"Model: It funds criminal groups and may violate sanctions; plus, paying does not guarantee decryption or prevent future extortion."}
  ]
 },
 4: {
  "title":"Zero-day vulnerabilities",
  "passage": (
   "A zero-day vulnerability is a flaw that is unknown to the vendor and for which no official patch exists "
   "at the moment of discovery. The term comes from the fact that defenders have had 'zero days' to prepare. "
   "Once a vulnerability is patched, it becomes what the industry calls an n-day. N-days are still dangerous, "
   "because many organisations take weeks or months to apply critical updates, but they are qualitatively "
   "different from true zero-days, which give attackers a significant window of advantage.\n\n"
   "Zero-days are discovered by a wide range of actors. Academic researchers, independent bug hunters and "
   "professional teams like Google Project Zero publish coordinated disclosures after working with vendors "
   "to release a fix. Others operate in the grey market: brokers such as Zerodium buy exploits and resell "
   "them, mostly to government customers. At competitions like Pwn2Own, researchers demonstrate live "
   "exploits against fully patched systems for cash prizes, and the chains of vulnerabilities they build "
   "can be remarkably complex, sometimes combining four or five flaws.\n\n"
   "The severity of a zero-day depends on what it allows. Remote code execution without authentication on "
   "a widely deployed product \u2013 the infamous Log4Shell of 2021 is the canonical example \u2013 is the most "
   "dangerous category. Privilege escalation, sandbox escape and information leaks are also valuable, "
   "especially when they chain with other bugs. The EPSS score, or Exploit Prediction Scoring System, helps "
   "defenders to prioritise vulnerabilities by predicting the probability of exploitation in the wild within "
   "30 days, complementing the traditional CVSS severity rating.\n\n"
   "For defenders, the harsh truth is that a zero-day cannot be patched before public disclosure. The only "
   "effective strategy is defence in depth: network segmentation, endpoint detection, strict application "
   "allow-listing, rigorous logging, and mature incident response. When a zero-day breaks the news, mature "
   "organisations already know which systems run the vulnerable software, where they sit in the network, "
   "and how fast they can be patched or isolated. Those that only start asking those questions after the "
   "news drops are usually the ones that end up in the next breach report."
  ),
  "source":"Adapted from CISA KEV catalogue (cisa.gov, PD), Google Project Zero public blog (googleprojectzero.blogspot.com) and EPSS documentation (first.org, CC BY 4.0).",
  "exercises":[
   {"type":"mcq","q":"What does 'zero-day' mean?",
    "options":["Patched vulnerability","Vulnerability unknown to vendor with no patch",
               "A vulnerability that was fixed yesterday","A CVSS 0 bug"],
    "a":1,"explain":"'A flaw that is unknown to the vendor and for which no patch exists.'"},
   {"type":"tfng","q":"Log4Shell is an example of a pre-auth remote code execution zero-day.","a":"T",
    "explain":"'Log4Shell of 2021 is the canonical example.'"},
   {"type":"gap","q":"The ____ score predicts the probability of exploitation in the wild within 30 days.",
    "a":"EPSS","alts":["epss","EPSS"]},
   {"type":"match","pairs":[
    ["Zero-day","no patch available yet"],
    ["N-day","patched, but still unpatched in many orgs"],
    ["CVSS","severity rating"],
    ["EPSS","exploitation probability"]]},
   {"type":"short","q":"Why is defence in depth essential against zero-days?",
    "model":"Model: Because no patch exists at time of discovery, so multiple independent controls (segmentation, EDR, allow-listing, logging) are needed to reduce impact."}
  ]
 },
 5: {
  "title":"OWASP Top 10 web application risks",
  "passage": (
   "The OWASP Top 10 is the most widely cited document in application security. It is a ranked list of the "
   "most critical risks to modern web applications, compiled from real-world data contributed by dozens of "
   "organisations. It is updated roughly every three to four years, and the 2021 edition \u2013 still widely used "
   "alongside the 2025 draft \u2013 reshuffled the rankings in important ways.\n\n"
   "The number one risk in 2021 is Broken Access Control: applications that fail to properly enforce which "
   "users can access which resources. Classic examples include IDOR bugs, where simply changing an ID in "
   "the URL lets one user read another user's data, and missing function-level authorisation checks. "
   "Cryptographic Failures, previously called 'Sensitive Data Exposure', takes second place and covers "
   "everything from missing TLS to weak hashing algorithms and hard-coded secrets committed to Git.\n\n"
   "Injection, which sat at the top for more than a decade, dropped to third. It still includes the classic "
   "SQL injection but now also covers NoSQL, command, LDAP and template injection. The root cause in almost "
   "every case is the same: the application concatenates untrusted input into a query or command instead of "
   "using parameterised APIs. Insecure Design, a new category, reflects a growing recognition that security "
   "problems often start long before any code is written: a flawed architecture or a missing threat model "
   "cannot be patched by clever input sanitisation.\n\n"
   "Other categories include Security Misconfiguration, Vulnerable and Outdated Components, "
   "Authentication Failures, Software and Data Integrity Failures, Security Logging and Monitoring Failures, "
   "and finally Server-Side Request Forgery, which was promoted into the Top 10 after several high-profile "
   "incidents including the 2019 Capital One breach. For a systems engineer, the practical message is simple: "
   "every category is preventable with well-known techniques, but only when security is designed in from the "
   "beginning, validated through testing, and verified continuously in production. Reading and genuinely "
   "understanding the OWASP Top 10 is no longer optional \u2013 it is a professional baseline."
  ),
  "source":"Adapted from OWASP Top 10 \u2013 2021 (owasp.org, CC BY-SA 4.0) and 2025 release candidate.",
  "exercises":[
   {"type":"mcq","q":"Which category is number 1 in OWASP Top 10 (2021)?",
    "options":["Injection","Broken Access Control","Cryptographic Failures","SSRF"],
    "a":1,"explain":"'The number one risk in 2021 is Broken Access Control.'"},
   {"type":"tfng","q":"Injection is still the number one risk in OWASP Top 10 (2021).","a":"F",
    "explain":"'Injection\u2026 dropped to third.'"},
   {"type":"gap","q":"A new category reflecting problems before code is written is 'Insecure ____'.",
    "a":"Design","alts":["design","Design"]},
   {"type":"match","pairs":[
    ["IDOR","Broken Access Control"],
    ["SQLi","Injection"],
    ["Hard-coded secrets","Cryptographic Failures"],
    ["Log4Shell","Vulnerable & Outdated Components"]]},
   {"type":"short","q":"Why is 'Insecure Design' a useful category separate from misconfiguration?",
    "model":"Model: Because many risks originate at the architecture stage; no amount of input validation compensates for a flawed design or a missing threat model."}
  ]
 },
},
# =========================================================================
"C1": {
 1: {
  "title":"Strategic, operational and tactical threat intelligence",
  "passage": (
   "Cyber Threat Intelligence, or CTI, is often described as the discipline of transforming raw data about "
   "adversaries into decisions that defenders can act on. What that looks like in practice varies enormously "
   "depending on the audience. Analysts traditionally divide intelligence into four layers: strategic, "
   "operational, tactical and technical. Conflating them, as many young programmes do, is one of the "
   "fastest ways to produce reports that satisfy no one.\n\n"
   "Strategic intelligence is aimed at executive and board audiences. It addresses long-horizon questions: "
   "which threat actors are most likely to target our sector over the next eighteen months, how geopolitical "
   "tensions translate into cyber risk, which regulatory shifts will change the exposure surface. The register "
   "is closer to a policy briefing than to a technical report, and the consumers almost never want indicators "
   "of compromise. They want narratives, trends, and implications for investment and staffing.\n\n"
   "Operational intelligence lives one layer down. It focuses on specific adversary campaigns: how a given "
   "group typically gains initial access, which tools they deploy post-exploitation, how they exfiltrate data. "
   "The Diamond Model of Intrusion Analysis, proposed by Caltagirone, Pendergast and Betz in 2013, remains "
   "a powerful cognitive tool here, because it forces analysts to reason simultaneously about adversary, "
   "capability, infrastructure and victim. Operational intelligence typically feeds threat hunting hypotheses "
   "and detection-engineering roadmaps, rather than individual SOC alerts.\n\n"
   "Tactical and technical intelligence are closer to the keyboard. Tactical intelligence describes the "
   "tactics, techniques and procedures \u2013 TTPs \u2013 of specific adversaries, mapped to frameworks such as "
   "MITRE ATT&CK. Technical intelligence is the most perishable of all: IPs, domains, file hashes, URL patterns. "
   "These IOCs are trivially changeable by a motivated adversary, which is why David Bianco's 'Pyramid of Pain' "
   "argues for prioritising TTPs and behavioural analytics over atomic indicators.\n\n"
   "A common but under-appreciated failure mode in CTI is the confusion between collection and analysis. "
   "A team can drown in feeds, STIX bundles and TAXII subscriptions while producing almost no real analysis. "
   "Intelligence-grade thinking \u2013 clearly stated collection requirements, explicit confidence levels, "
   "documented analytic tradecraft following something like the Analysis of Competing Hypotheses \u2013 remains "
   "rare outside a small community of mature programmes. Mature teams invest at least as much in tradecraft "
   "as they do in tools, and the dividends show up when a serious, novel adversary finally appears on the "
   "radar and the team has to decide, in a few hours, what is really happening."
  ),
  "source":"Adapted from Caltagirone, Pendergast & Betz, 'The Diamond Model of Intrusion Analysis' (2013, US Department of Defense, PD); David Bianco's 'Pyramid of Pain' blog (Creative Commons); MITRE ATT&CK (attack.mitre.org).",
  "exercises":[
   {"type":"mcq","q":"Which layer of CTI is most aimed at board-level audiences?",
    "options":["Tactical","Operational","Strategic","Technical"],"a":2,
    "explain":"'Strategic intelligence is aimed at executive and board audiences.'"},
   {"type":"tfng","q":"According to the Pyramid of Pain, atomic IOCs (IPs and hashes) should be the main focus of intelligence programmes.","a":"F",
    "explain":"'\u2026prioritising TTPs and behavioural analytics over atomic indicators.'"},
   {"type":"gap","q":"The Diamond Model forces analysts to reason about adversary, capability, infrastructure and ____.",
    "a":"victim","alts":["victim"]},
   {"type":"match","pairs":[
    ["Strategic","board, long horizon"],
    ["Operational","specific adversary campaigns"],
    ["Tactical","TTPs, ATT&CK"],
    ["Technical","IOCs, most perishable"]]},
   {"type":"short","q":"Why do mature CTI teams distinguish collection from analysis?",
    "model":"Model: Because unlimited raw feeds do not equal insight. Without stated requirements, confidence levels and analytic tradecraft, the team drowns in data and fails to answer the questions that matter."}
  ]
 },
 2: {
  "title":"Advanced Persistent Threats",
  "passage": (
   "The term 'Advanced Persistent Threat' was coined inside the US Air Force around 2006, initially to refer "
   "specifically to Chinese state-linked intrusion sets targeting defence contractors. Two decades later, the "
   "term is used more loosely, but the core idea remains: APTs are well-resourced, strategically motivated "
   "adversaries that maintain long-term access to their targets, often measured in months or even years. "
   "Financial cybercrime groups are now routinely operating at APT tradecraft levels, so the original "
   "state-only connotation has largely faded.\n\n"
   "Famous examples include Russia's APT28 and APT29, China's APT41 and Volt Typhoon, North Korea's Lazarus "
   "and Kimsuky, and Iran's MuddyWater. Each has distinctive patterns. Lazarus, for instance, mixes classic "
   "espionage with aggressive financial operations, particularly against cryptocurrency exchanges, to fund "
   "the regime. Volt Typhoon, by contrast, has drawn unusual public attention from CISA for its pre-positioning "
   "in US critical infrastructure \u2013 water, power, transportation \u2013 seemingly to prepare destructive options "
   "for a future crisis. The blurring between espionage and preparation for destructive operations is one of "
   "the defining trends of the past five years.\n\n"
   "From a technical standpoint, modern APTs increasingly rely on 'living off the land' techniques. Instead "
   "of deploying custom malware that endpoint detection can fingerprint, operators abuse native tools: "
   "PowerShell, WMI, scheduled tasks, signed drivers. Bring-your-own-vulnerable-driver, or BYOVD, has become "
   "a common primitive, allowing attackers to neutralise security products from kernel space by loading an "
   "old, legitimately signed but vulnerable driver. The implication for defenders is uncomfortable: signature-"
   "based approaches are no longer sufficient, and behavioural analytics become the only realistic path.\n\n"
   "Attribution remains deeply political, which is why serious analysts work with explicit confidence levels "
   "rather than categorical claims. ICD 203 defines the US Intelligence Community standard and is widely "
   "adopted by commercial vendors such as Mandiant and CrowdStrike: 'low', 'moderate', 'high' confidence, "
   "each with a clear definition. Conflating 'likely' with 'certain' in a public report can have diplomatic "
   "consequences that outlast the original incident by years. For engineers, the practical takeaway is that "
   "understanding APT tradecraft is no longer a luxury reserved for intelligence analysts: any team running "
   "a modern production network will, sooner or later, face a slice of it. Detection engineering, mature "
   "logging, and tight identity controls have become basic hygiene, not aspirational goals."
  ),
  "source":"Adapted from CISA Volt Typhoon advisory (cisa.gov, PD); Mandiant M-Trends 2024 summary notes; US ODNI ICD 203 Analytic Standards (odni.gov, PD).",
  "exercises":[
   {"type":"mcq","q":"What does BYOVD stand for in modern APT tradecraft?",
    "options":["Bring Your Own Virtual Device","Bring Your Own Vulnerable Driver",
               "Built-in Vulnerability Detection","Business-owned Virtual Desktop"],
    "a":1,"explain":"'Bring-your-own-vulnerable-driver, or BYOVD\u2026'"},
   {"type":"tfng","q":"Volt Typhoon is mainly a financial cybercrime group.","a":"F",
    "explain":"'\u2026pre-positioning in US critical infrastructure\u2026 destructive options\u2026'"},
   {"type":"gap","q":"ICD 203 defines the US Intelligence Community standard for analytic ____ levels.",
    "a":"confidence","alts":["confidence"]},
   {"type":"match","pairs":[
    ["APT28/29","Russia"],["APT41 / Volt Typhoon","China"],
    ["Lazarus / Kimsuky","North Korea"],["MuddyWater","Iran"]]},
   {"type":"short","q":"Why is attribution handled with explicit confidence levels rather than absolute claims?",
    "model":"Model: Because attribution involves incomplete data and active deception, so categorical claims risk diplomatic or legal consequences; confidence levels signal the analytic uncertainty honestly."}
  ]
 },
 3: {
  "title":"Zero Trust Architecture",
  "passage": (
   "Zero Trust Architecture, formalised in the United States by NIST Special Publication 800-207, reframes "
   "a decade of security experience into a compact principle: never trust, always verify. The architecture "
   "assumes, by default, that no user, device or workflow is trustworthy simply because it sits on a "
   "particular network. Every access request is authenticated and authorised individually, based on dynamic "
   "signals that include identity, device posture, location, behaviour and the sensitivity of the resource.\n\n"
   "The reference architecture centres on two logical components: the Policy Decision Point, which evaluates "
   "access requests against policy and risk signals, and the Policy Enforcement Point, which actually allows "
   "or blocks the connection. Around these sit the so-called trust algorithm and various data sources: "
   "identity providers, EDR telemetry, threat intelligence, vulnerability scanners, SIEM analytics. A mature "
   "implementation continuously re-evaluates the session; if the device suddenly shows signs of compromise, "
   "access can be revoked in seconds, not minutes.\n\n"
   "Zero Trust is frequently misunderstood as a product you can buy. No single vendor can deliver it, and "
   "companies that try to simply badge their VPN or firewall as 'Zero Trust' usually end up with expensive "
   "shelfware. A realistic roadmap typically spans three to five years and covers identity modernisation "
   "(phishing-resistant MFA, risk-based conditional access, passwordless where possible), endpoint trust "
   "(EDR on every device, attestation, posture checks), network transformation (moving from VPN to ZTNA, "
   "micro-segmentation, encrypted east-west traffic), and data-centric controls (classification, rights "
   "management, DLP).\n\n"
   "The operational technology sector presents a particularly hard case. Legacy controllers in factories, "
   "refineries and hospitals often cannot run modern agents or even handle certificate rotation; pure Zero "
   "Trust is simply impractical at the device level. Realistic architectures in OT instead combine heavy "
   "segmentation, rigorous jump-host design, one-way data diodes for critical telemetry, and compensating "
   "controls such as protocol gateways. IEC 62443 and NIST SP 800-82 provide the canonical reference "
   "frameworks, and regulators in the EU (through NIS2) and the US (through CISA's cross-sector performance "
   "goals) have made it clear that 'we cannot patch our OT' is no longer an acceptable answer.\n\n"
   "The honest strategic message is that Zero Trust is not a silver bullet. It does not eliminate risk; it "
   "shifts it onto identity, instrumentation and continuous verification. Organisations that invest seriously "
   "in those three pillars dramatically reduce their blast radius when something goes wrong \u2013 and in a "
   "world where something always eventually goes wrong, that reduction is often the difference between an "
   "embarrassing incident and an existential one."
  ),
  "source":"Adapted from NIST SP 800-207 (nist.gov, PD), CISA Zero Trust Maturity Model v2 (cisa.gov, PD), NIST SP 800-82r3 OT Security Guide (PD), IEC 62443 public summaries.",
  "exercises":[
   {"type":"mcq","q":"In NIST SP 800-207, which component evaluates the access request against policy?",
    "options":["Policy Enforcement Point","Policy Decision Point","Identity Provider","EDR agent"],
    "a":1,"explain":"'Policy Decision Point\u2026 evaluates access requests against policy\u2026'"},
   {"type":"tfng","q":"Zero Trust is a single product you can purchase from any major security vendor.","a":"F",
    "explain":"'Zero Trust is frequently misunderstood as a product you can buy.'"},
   {"type":"gap","q":"In OT environments, one-way ____ diodes are used for critical telemetry.",
    "a":"data","alts":["data"]},
   {"type":"match","pairs":[
    ["NIST SP 800-207","Zero Trust reference"],
    ["IEC 62443","OT security"],
    ["NIS2","EU regulation"],
    ["CISA ZTMM","maturity model"]]},
   {"type":"short","q":"Summarise in 2 sentences what Zero Trust actually moves, rather than eliminates.",
    "model":"Model: Zero Trust does not eliminate risk. It shifts risk onto identity, instrumentation and continuous verification \u2014 so investment in those three areas determines the real residual risk."}
  ]
 },
 4: {
  "title":"Modern SOC operations",
  "passage": (
   "The Security Operations Centre has evolved considerably over the last ten years. Early SOCs were built "
   "around perimeter products and noisy signature-based alerts; modern SOCs \u2013 or the outsourced MDR and XDR "
   "services that increasingly replace them \u2013 are closer to a detection-engineering lab that happens to also "
   "triage alerts. The shift matters, because the bottleneck is rarely tooling any more. It is analyst cognitive "
   "load, quality of detections, and tight integration with incident response.\n\n"
   "A typical modern SOC is organised in tiers. Tier 1 performs initial triage against SIEM alerts: closing "
   "false positives, escalating anything suspicious, following playbooks. Tier 2 conducts deeper investigations, "
   "often pivoting across endpoint telemetry, network metadata, identity logs and threat intelligence. Tier 3 "
   "does threat hunting and detection engineering, authoring new rules, tuning existing ones and closing "
   "visibility gaps. Increasingly, SOAR platforms automate the most repetitive Tier 1 work, leaving humans "
   "focused on cases that genuinely benefit from human reasoning.\n\n"
   "Metrics matter, but can mislead. Classic KPIs like Mean Time To Detect and Mean Time To Respond are useful "
   "only when measured honestly across the full detection-to-containment path. Teams that game the metrics by "
   "closing alerts quickly without proper investigation end up with impressive dashboards and invisible breaches. "
   "Leading teams now supplement MTTD and MTTR with measures of detection coverage mapped to MITRE ATT&CK, alert "
   "fidelity rates, and analyst burnout indicators such as shift rotation and attrition.\n\n"
   "Staffing is one of the quietly decisive issues of the field. Burnout is endemic. Follow-the-sun models "
   "across multiple geographic regions alleviate some of the strain; deliberate investment in career paths, "
   "training budgets and research time is at least as important. A SOC where analysts rarely see a successful "
   "detection they built themselves tends to lose its best people within two to three years. The ability of "
   "senior analysts to think adversarially \u2013 to ask 'what would I do if I were the attacker already inside' \u2013 "
   "is what separates a reactive operation from a genuinely resilient one, and that ability does not grow in "
   "an environment that treats analysts as interchangeable ticket-processors.\n\n"
   "Information-sharing, finally, has quietly become one of the highest-leverage activities a SOC can invest "
   "in. ISACs, ISAOs, government partnerships, and trusted private communities allow teams to learn from each "
   "other's incidents before they face the same adversary. TLP \u2013 Traffic Light Protocol \u2013 gives participants "
   "a common vocabulary for what can and cannot be redistributed. In the long run, the teams that share "
   "carefully and consume ruthlessly outperform those that try to go it alone."
  ),
  "source":"Adapted from SANS SOC Survey reports (sans.org, free after registration); FIRST.org TLP 2.0 (first.org, CC BY-NC 4.0); MITRE ATT&CK (attack.mitre.org).",
  "exercises":[
   {"type":"mcq","q":"Which tier is typically responsible for detection engineering and threat hunting?",
    "options":["Tier 1","Tier 2","Tier 3","Tier 0"],"a":2,
    "explain":"'Tier 3 does threat hunting and detection engineering\u2026'"},
   {"type":"tfng","q":"MTTD and MTTR are always sufficient to judge a SOC\u2019s effectiveness.","a":"F",
    "explain":"'Teams that game the metrics\u2026 end up with invisible breaches.'"},
   {"type":"gap","q":"FIRST's ____ Protocol gives participants a common vocabulary for sharing restrictions.",
    "a":"Traffic Light","alts":["traffic light","TLP"]},
   {"type":"match","pairs":[
    ["Tier 1","triage and initial escalation"],
    ["Tier 2","deeper investigation"],
    ["Tier 3","hunting and detection engineering"],
    ["SOAR","automation of repetitive workflows"]]},
   {"type":"short","q":"Why is information-sharing described as 'high-leverage' for SOCs?",
    "model":"Model: Because incidents repeat across the sector; structured sharing via ISACs and TLP lets teams prepare detections and responses for adversary TTPs they have not yet seen themselves."}
  ]
 },
 5: {
  "title":"Threat hunting methodologies",
  "passage": (
   "Threat hunting emerged as a distinct discipline roughly a decade ago, once organisations began to accept "
   "that relying solely on alerts generated by signature-based tools was an incomplete strategy. The core "
   "premise of hunting is that, by the time an alert fires, meaningful damage may already be done; proactive "
   "searches through the environment are therefore needed to surface adversaries that have evaded automated "
   "detection. The discipline is now mature enough that it has developed its own vocabulary, its own "
   "methodologies, and its own maturity models.\n\n"
   "Three broad methodological strands coexist. Hypothesis-driven hunting starts from a specific adversary "
   "hypothesis: 'Given our exposure, an operator like this ransomware affiliate would attempt credential "
   "dumping with Mimikatz within 48 hours of initial access; let us search for evidence consistent with "
   "that technique.' Data-driven hunting reverses the flow: the hunter surveys anomalies in the environment "
   "and works backwards to determine whether they reflect malicious activity. Intelligence-driven hunting "
   "leans most heavily on CTI, mapping specific adversaries and campaigns to concrete hunting plays. In "
   "practice, mature programmes rotate between all three, depending on what is available.\n\n"
   "Frameworks such as the Mandiant Threat Hunting Maturity Model, MaGMa, and the TaHiTI methodology provide "
   "structure. They insist, for example, on documentation: a hunt that is not written up cannot inform future "
   "detection engineering. They also connect hunting to ATT&CK: each hypothesis maps to specific techniques, "
   "and over time the team's coverage against the matrix becomes quantifiable. David Bianco's 'Pyramid of "
   "Pain', mentioned earlier in this course, applies here too: mature hunters target TTPs rather than IOCs, "
   "because TTPs are the most expensive layer for the adversary to change.\n\n"
   "Tooling choices matter, though less than most teams initially assume. Sysmon, ETW and the equivalent "
   "instrumentation on Linux (auditd, eBPF) give hunters the raw material they need. osquery and Velociraptor "
   "allow live querying across large fleets. KQL in Microsoft Sentinel, SPL in Splunk and their equivalents "
   "make time-series correlation tractable. But the most experienced hunters will tell you that the quality "
   "of the data matters more than the query language: if your environment does not log process creation or "
   "command-line arguments, no tool will save you.\n\n"
   "Beyond the technical, a quietly important skill is the ability to reason under uncertainty. A hunt that "
   "finds nothing is not a failed hunt if the hypothesis was well framed and the data quality was adequate; "
   "it is a data point that reduces your estimate of that specific risk. Programmes that treat null results "
   "as failure quickly devolve into theatre, chasing whatever produces the most visually impressive dashboard. "
   "Programmes that treat them as information mature into something rarer: teams that can actually say, with "
   "calibrated confidence, what adversary activity is or is not happening inside their perimeter."
  ),
  "source":"Adapted from 'The TaHiTI Threat Hunting Methodology' (Betaalvereniging Nederland, CC BY-SA); MITRE ATT&CK (attack.mitre.org); David Bianco, 'The Pyramid of Pain' (CC BY).",
  "exercises":[
   {"type":"mcq","q":"Which hunting approach begins from a specific adversary hypothesis?",
    "options":["Data-driven","Hypothesis-driven","Intelligence-driven","Alert-driven"],"a":1,
    "explain":"'Hypothesis-driven hunting starts from a specific adversary hypothesis\u2026'"},
   {"type":"tfng","q":"A hunt with no findings is automatically a failed hunt.","a":"F",
    "explain":"'A hunt that finds nothing is not a failed hunt\u2026'"},
   {"type":"gap","q":"Mature hunters focus on ____ rather than IOCs, following the Pyramid of Pain.",
    "a":"TTPs","alts":["TTPs","ttps","tactics techniques and procedures"]},
   {"type":"match","pairs":[
    ["Hypothesis-driven","starts from adversary hypothesis"],
    ["Data-driven","anomalies first"],
    ["Intelligence-driven","CTI-led plays"],
    ["TaHiTI","Dutch threat hunting methodology"]]},
   {"type":"short","q":"Why is logging quality more important than the query language used?",
    "model":"Model: Because no query language can recover events that were never logged; without process creation and command-line logging, for example, the hunter is blind regardless of tooling."}
  ]
 },
},
# =========================================================================
"C2": {
 1: {
  "title":"Cyber operations and the grey zone below the threshold",
  "passage": (
   "Few concepts in international security have proven as slippery, or as consequential, as the idea of a "
   "'grey zone' in cyberspace. The notion attempts to capture a reality that neither traditional international "
   "relations theory nor the classical law of armed conflict was designed to handle: persistent, state-directed "
   "hostile activity that stays deliberately below the threshold at which it would trigger a conventional, "
   "or indeed cyber, armed response. The phenomenon is not new \u2013 propaganda, sabotage and covert action are "
   "ancient instruments of statecraft \u2013 but the velocity, scale and asymmetric leverage that contemporary "
   "offensive cyber capabilities provide have pushed it into a central place in strategic debate.\n\n"
   "The Tallinn Manual 2.0, drafted by an international group of experts under the auspices of the NATO "
   "Cooperative Cyber Defence Centre of Excellence, attempts to articulate how existing international law "
   "applies to state behaviour in cyberspace. It is emphatic that international law \u2013 the principle of "
   "sovereignty, the prohibition on intervention, the law of state responsibility \u2013 applies in cyberspace "
   "as it does elsewhere. It is more tentative on the precise thresholds: when does a cyber operation amount "
   "to a 'use of force' within the meaning of Article 2(4) of the UN Charter, and when does it cross the "
   "higher threshold of an 'armed attack' triggering the right of self-defence under Article 51? The Manual "
   "surveys the differing views among states and scholars, but does not, and cannot, resolve them. Neither "
   "the UN Group of Governmental Experts nor its successor Open-Ended Working Group has fared much better.\n\n"
   "States, for entirely rational strategic reasons, prefer ambiguity. Over-specifying thresholds constrains "
   "one's own future options; under-specifying allows flexible escalation and deniable competition. The "
   "result is a regime of tacit norms, public attribution campaigns, targeted sanctions, indictments of "
   "named operators, expulsion of diplomats, and occasional overt cyber responses by capable powers. Whether "
   "this emergent practice amounts to customary international law, or merely to strategic bargaining under "
   "the shadow of unresolved legal questions, is itself contested.\n\n"
   "A further layer of complexity arises from the private sector. Unlike previous technological revolutions, "
   "the infrastructure, talent and intelligence capabilities of cyberspace are overwhelmingly owned and "
   "operated by commercial actors. Platforms, cloud providers and security vendors now issue attribution "
   "statements that can be of higher evidentiary quality than government assertions, and in several recent "
   "episodes they have shaped the public narrative more decisively than any official communication. This "
   "diffusion of authority raises uncomfortable questions about accountability, dual loyalties, and the "
   "legitimacy of private actors performing functions historically reserved for states.\n\n"
   "A final and underappreciated dynamic is the blurring between offence, espionage and preparation for "
   "destructive action. Operations historically classed as routine intelligence collection may now leave "
   "behind pre-positioned implants in critical infrastructure, collapsing the clean analytical distinction "
   "between observation and attack. Public advisories from CISA concerning Volt Typhoon are instructive "
   "precisely because they highlight this collapse. For policymakers, the implication is uncomfortable: "
   "drawing meaningful red lines requires accepting that some long-standing categories of statecraft no "
   "longer describe the actual practice, and that the legal and diplomatic architecture built around those "
   "categories may need to evolve faster than governments are institutionally prepared to evolve it."
  ),
  "source":"Adapted from Schmitt (ed.), 'Tallinn Manual 2.0' (Cambridge University Press, 2017; scholarly summary materials at ccdcoe.org); UN GGE 2015 and 2021 reports (un.org, PD); CISA Volt Typhoon advisory (cisa.gov, PD).",
  "exercises":[
   {"type":"mcq","q":"What is the main argument the passage makes about states and cyber thresholds?",
    "options":["States want maximum legal clarity","States actively prefer ambiguity for strategic reasons",
     "The Tallinn Manual has settled the thresholds","Thresholds are defined by UN resolutions"],
    "a":1,"explain":"'States\u2026 prefer ambiguity.'"},
   {"type":"tfng","q":"According to the Tallinn Manual, international law does not apply to cyberspace.","a":"F",
    "explain":"'\u2026international law applies in cyberspace as it does elsewhere.'"},
   {"type":"gap","q":"Article ____ of the UN Charter prohibits the use of force.",
    "a":"2(4)","alts":["2(4)","2.4","2-4"]},
   {"type":"match","pairs":[
    ["Tallinn Manual 2.0","expert-written, non-binding"],
    ["Article 2(4)","use of force"],
    ["Article 51","right of self-defence"],
    ["Volt Typhoon","pre-positioning in critical infrastructure"]]},
   {"type":"short","q":"Why does the passage argue that private sector attribution statements raise 'uncomfortable questions about accountability'?",
    "model":"Model: Because private actors without a public mandate are performing functions traditionally reserved for states; their commercial incentives, loyalties to customers and shareholders, and lack of democratic accountability are not obviously compatible with shaping inter-state narratives."}
  ]
 },
 2: {
  "title":"State-sponsored actors and the mercenary spyware market",
  "passage": (
   "The landscape of state-sponsored cyber operations has transformed in ways that would have been difficult "
   "to predict twenty years ago. The original US Air Force framing of APTs described highly resourced but "
   "relatively narrow state intelligence programmes. Today, the field is far more crowded and more commercial. "
   "Sophisticated operations are carried out not only by traditional agencies, but also by contractors, front "
   "companies, and a thriving industry of so-called mercenary spyware vendors whose products are sold \u2013 "
   "sometimes with inadequate end-use controls \u2013 to an ever-widening list of state customers.\n\n"
   "Public reporting from Citizen Lab, Amnesty International's Security Lab, Google's Threat Analysis Group "
   "and commercial firms has documented how products such as those attributed to NSO Group, Candiru, Cytrox "
   "and Intellexa have been used against journalists, dissidents, human-rights defenders and parliamentarians. "
   "The technical sophistication is often remarkable \u2013 zero-click iOS exploit chains have repeatedly surfaced "
   "\u2013 but the policy implications are arguably more interesting still. Several governments have, in response, "
   "imposed visa restrictions on spyware vendor employees, sanctioned specific companies and placed certain "
   "intrusion technologies on export-control lists under frameworks such as the Wassenaar Arrangement. The "
   "United States Executive Order 14093 of 2023 prohibits federal agencies from operationally using commercial "
   "spyware that presents national-security or human-rights risks.\n\n"
   "These measures have clearly raised costs for the worst-behaving vendors, but they have not dissolved the "
   "market. Demand remains structural. Many states lack the capability to build sophisticated tooling in-house "
   "and are unwilling to abandon the intelligence advantage that commercial products offer. Supply, in turn, "
   "adapts: new companies appear in jurisdictions with weaker export controls, corporate structures are "
   "reconfigured to obscure ownership, and talent flows between firms in ways that are difficult to police. "
   "Whether a durable international regime analogous to those governing chemical, biological or nuclear "
   "dual-use goods is politically feasible remains an open, and largely uncomfortable, question.\n\n"
   "The operational picture is further complicated by state actors' willingness to outsource work to domestic "
   "contractors. Leaks such as the 2024 'i-Soon' disclosures offered a window into the industrialised Chinese "
   "ecosystem of contractors bidding on intelligence-collection tasks against specific foreign organisations. "
   "Similar, less-publicised patterns exist in other jurisdictions. From an analytical standpoint, this "
   "commercialisation of statecraft complicates attribution: the same operators may rotate between contracts, "
   "and the same infrastructure may serve multiple principals over time, rendering the neat 'one group, one "
   "state' mental model of the early APT era increasingly obsolete.\n\n"
   "For defenders, the practical implication is that mercenary spyware and contractor ecosystems expand "
   "the population of capable adversaries considerably beyond the traditional handful of state services. Threat "
   "modelling for high-risk individuals \u2013 journalists, executives in sensitive sectors, human-rights defenders "
   "\u2013 now reasonably assumes that nation-state-grade tooling is available to a far wider set of actors than "
   "used to be plausible, including some with primarily domestic political rather than foreign-intelligence "
   "objectives. That assumption, once controversial, is now uncontroversial; defensive practice is still "
   "catching up."
  ),
  "source":"Adapted from Citizen Lab public research (citizenlab.ca, CC BY); Amnesty International Security Lab reports; Google TAG analyses; US Executive Order 14093 (whitehouse.gov, PD); Wassenaar Arrangement public texts (wassenaar.org).",
  "exercises":[
   {"type":"mcq","q":"Executive Order 14093 primarily:",
    "options":["Bans all cyber operations by US agencies",
               "Prohibits US federal agencies from operational use of commercial spyware with NS/HR risks",
               "Legalises foreign intelligence collection","Regulates cryptocurrency exchanges"],
    "a":1,"explain":"'\u2026prohibits federal agencies from operationally using commercial spyware\u2026'"},
   {"type":"tfng","q":"According to the passage, existing sanctions and export controls have largely eliminated the mercenary spyware market.","a":"F",
    "explain":"'\u2026have not dissolved the market. Demand remains structural.'"},
   {"type":"gap","q":"The 2024 leaks associated with the Chinese contractor ecosystem are known as the ____ disclosures.",
    "a":"i-Soon","alts":["i-soon","iSoon","i-Soon"]},
   {"type":"match","pairs":[
    ["Citizen Lab","academic research into targeted surveillance"],
    ["Wassenaar Arrangement","dual-use export control framework"],
    ["EO 14093","US federal restriction on spyware use"],
    ["i-Soon","Chinese contractor ecosystem leak"]]},
   {"type":"short","q":"How does the commercialisation of state operations complicate attribution?",
    "model":"Model: Contractors may work for multiple principals in rotation, and shared infrastructure and personnel blur the one-group/one-state model; attribution must therefore incorporate commercial supply-chain analysis alongside traditional indicators."}
  ]
 },
 3: {
  "title":"International cyber law and the Schrems II legacy",
  "passage": (
   "The 2020 judgment of the Court of Justice of the European Union in Case C-311/18, universally referred "
   "to as Schrems II, has cast a long shadow over the international transfer of personal data. By "
   "invalidating the EU-US Privacy Shield framework while leaving Standard Contractual Clauses formally "
   "intact but practically conditional, the Court forced controllers to perform case-by-case transfer impact "
   "assessments whenever personal data moves outside the European Economic Area. What was intended as legal "
   "clarification has, in practice, produced half a decade of normative and operational turbulence whose "
   "reverberations are still being felt by privacy teams worldwide.\n\n"
   "At the core of the judgment sits the Court's concern about US signals intelligence authorities, "
   "particularly Section 702 of the FISA Amendments Act and Executive Order 12333. The Court found that "
   "these authorities were not subject to the limitations of necessity and proportionality that EU law "
   "derives from Articles 7, 8 and 47 of the Charter of Fundamental Rights, and that data subjects lacked "
   "effective judicial redress in the United States. The EU-US Data Privacy Framework of 2023, coupled "
   "with Executive Order 14086 and the creation of a Data Protection Review Court within the US intelligence "
   "community, represents an ambitious attempt to cure these deficiencies. Whether it survives Schrems III \u2013 "
   "a challenge already before the European courts at the time of writing \u2013 is an open question, and one "
   "with material consequences for any organisation that relies on US-hosted services to process EU personal "
   "data at scale.\n\n"
   "Beyond the transatlantic axis, an increasingly dense web of cross-border regimes is taking shape. "
   "Brazil's LGPD, India's DPDP Act, China's PIPL, and a rapidly proliferating set of state-level US "
   "privacy statutes modelled on the California CCPA/CPRA collectively complicate any global data-minimisation "
   "strategy. Each regime imposes its own lawful bases, its own data-subject rights, its own notification "
   "deadlines, and, in some cases, its own localisation requirements. The PIPL is particularly notable for "
   "its stringent treatment of cross-border transfers and for the leverage it gives Chinese regulators over "
   "foreign companies operating in the market.\n\n"
   "Overlaying the privacy regimes is a separate, equally important body of law governing cross-border access "
   "to data for law-enforcement purposes. The US CLOUD Act of 2018 and the EU e-Evidence Regulation of 2023, "
   "each in its own way, attempt to reconcile the extraterritorial reach of criminal investigations with "
   "data-sovereignty concerns. The practical outcome for enterprises is that compliance is no longer a matter "
   "of choosing one framework and adhering to it; it is a matter of navigating multiple, occasionally "
   "conflicting, obligations while maintaining defensible records of the reasoning that led to each decision.\n\n"
   "For the systems engineer operating above the role of pure implementer, the implication is that architectural "
   "choices \u2013 where a workload runs, which cryptographic arrangements protect it, whether the provider can "
   "technically be compelled to disclose it \u2013 have become genuinely juridical choices. Effective collaboration "
   "between engineering, legal, privacy and security functions is not a nicety. It is the minimum condition "
   "for building systems that are both operationally useful and legally defensible in a regulatory landscape "
   "that shows every indication of continuing to grow more complex."
  ),
  "source":"Adapted from Court of Justice of the EU, Case C-311/18 (curia.europa.eu, PD); EU-US Data Privacy Framework materials (dataprivacyframework.gov, PD); US Executive Order 14086 (whitehouse.gov, PD); scholarly summaries of LGPD, DPDP, PIPL.",
  "exercises":[
   {"type":"mcq","q":"The core concern of the Court of Justice in Schrems II related to:",
    "options":["GDPR fines","US signals intelligence authorities and lack of effective redress",
               "Cloud pricing","Cross-border shipping"],
    "a":1,"explain":"'\u2026US signals intelligence authorities\u2026 data subjects lacked effective judicial redress\u2026'"},
   {"type":"tfng","q":"After Schrems II, Standard Contractual Clauses were formally invalidated.","a":"F",
    "explain":"'\u2026SCCs formally intact but practically conditional\u2026'"},
   {"type":"gap","q":"The 2023 framework created a Data Protection Review ____ within the US intelligence community.",
    "a":"Court","alts":["court","Court"]},
   {"type":"match","pairs":[
    ["GDPR / Charter Art. 7, 8, 47","EU baseline"],
    ["Section 702 / EO 12333","US surveillance authorities"],
    ["LGPD","Brazil"],["PIPL","China"]]},
   {"type":"short","q":"Why does the passage argue that architectural choices have become 'juridical choices'?",
    "model":"Model: Because where and how data is processed determines which laws apply, which authorities can compel disclosure, and whether compliance obligations can be met; engineering, legal and privacy must therefore co-design the architecture."}
  ]
 },
 4: {
  "title":"Offensive security ethics and the regulation of research",
  "passage": (
   "Few fields have had to build their professional ethics as rapidly, and under such adversarial conditions, "
   "as offensive security research. The work frequently sits at the intersection of activities that, taken "
   "out of context, are criminal offences: unauthorised access, possession of intrusion software, reverse "
   "engineering protected code, testing exploits against live infrastructure. What separates responsible "
   "research from criminal conduct is a structured combination of scope, consent, restraint and disclosure \u2013 "
   "elements that do not always map cleanly onto the statutes under which researchers may be prosecuted.\n\n"
   "The United States Department of Justice's 2022 revision of its Computer Fraud and Abuse Act charging "
   "policy formally abjured prosecution of 'good-faith security research', an announcement widely welcomed "
   "by practitioners, though its substantive effect depends on the discretion of individual prosecutors "
   "and has not been tested by a hard case. The United Kingdom's Computer Misuse Act 1990, despite two "
   "decades of law-reform campaigning by organisations including the CyberUp Campaign, still lacks a formal "
   "safe harbour and remains a source of chilling effect for UK-based researchers. Peru's Law 30096 and "
   "analogous statutes elsewhere in Latin America exhibit similar structural problems. The legal picture, "
   "in short, is uneven and evolving.\n\n"
   "On top of domestic criminal law sits the Wassenaar Arrangement's export-control regime for 'intrusion "
   "software', which, despite well-intentioned amendments following the 2015 backlash from the research "
   "community, continues to impose compliance burdens that disproportionately affect bona fide defenders. "
   "A researcher who discovers a vulnerability in a product made abroad and wishes to share exploit details "
   "with the vendor's security team may find that what counts as ordinary collaboration between professionals "
   "is, in the eyes of export control, a regulated transfer requiring licenses.\n\n"
   "Coordinated vulnerability disclosure, often abbreviated CVD, has emerged as the dominant ethical framework. "
   "Researchers give vendors a reasonable window to patch before publication; vendors commit to acting in "
   "good faith and not pursuing researchers legally; intermediaries like CERT/CC and national CSIRTs mediate "
   "disputes. The ISO/IEC 29147 and 30111 standards offer procedural scaffolding. Yet CVD is not without "
   "tensions. Extended embargoes can leave users exposed for months; aggressive vendors can exploit "
   "asymmetries of legal resources to pressure researchers into silence; and not every vulnerability has a "
   "clear owner to notify, particularly in complex supply chains.\n\n"
   "A more philosophical question hovers over the entire field: whether the marginal benefit of publishing "
   "a given piece of offensive research exceeds its marginal cost in terms of enabling harm. Most researchers "
   "operate under a working presumption that transparent publication, over time, makes defence stronger than "
   "the equivalent knowledge remaining in adversary-only circles. That presumption is empirically plausible "
   "but not airtight, and honest practitioners update it case by case, weighing the specificity of the "
   "capability, the maturity of compensating defences, and the identifiability of likely targets. The capacity "
   "to reason through these dilemmas without collapsing into either techno-libertarian absolutism or "
   "risk-averse paralysis is, arguably, what distinguishes mature researchers from both ideological camps."
  ),
  "source":"Adapted from US DoJ CFAA Charging Policy (May 2022, justice.gov, PD); UK CMA 1990 and CyberUp Campaign public submissions; ISO/IEC 29147:2018 and 30111:2019 scope summaries; Wassenaar Arrangement 2013/2015 public texts.",
  "exercises":[
   {"type":"mcq","q":"In 2022, which policy formally declined to prosecute good-faith security research?",
    "options":["UK CMA amendment","US DoJ CFAA charging policy","Peru Law 30096","Wassenaar 2015"],
    "a":1,"explain":"'The US DoJ\u2019s 2022 revision\u2026 formally abjured prosecution of good-faith security research.'"},
   {"type":"tfng","q":"The Wassenaar Arrangement's 'intrusion software' rules always align smoothly with how research is conducted in practice.","a":"F",
    "explain":"'\u2026continues to impose compliance burdens\u2026'"},
   {"type":"gap","q":"ISO/IEC ____ and 30111 offer procedural scaffolding for CVD.","a":"29147","alts":["29147"]},
   {"type":"match","pairs":[
    ["CFAA","US"],["CMA 1990","UK"],["Law 30096","Peru"],["Wassenaar","dual-use export controls"]]},
   {"type":"short","q":"Why does the passage describe CVD as having 'tensions'?",
    "model":"Model: Because extended embargoes can leave users exposed, vendors may use legal leverage to silence researchers, and some vulnerabilities have no clear owner \u2013 in complex supply chains, no single vendor can fix the issue."}
  ]
 },
 5: {
  "title":"Post-quantum cryptography and the migration problem",
  "passage": (
   "The probability that a cryptographically relevant quantum computer \u2013 one capable of running Shor's "
   "algorithm against RSA-2048 or comparably sized elliptic-curve parameters \u2013 will exist within the next "
   "two decades is not dismissible. Estimates vary widely and should be treated with appropriate analytical "
   "humility, but the strategic posture adopted by responsible institutions already assumes that such a "
   "machine is at least a credible long-term possibility. The central consequence for the cryptographic "
   "community is that the public-key infrastructure that has underpinned internet security for four decades "
   "must be migrated to post-quantum alternatives on a timeline that is aggressive by any realistic measure.\n\n"
   "The National Institute of Standards and Technology concluded the first round of its multi-year selection "
   "process in 2024 with FIPS 203 (ML-KEM, the lattice-based key encapsulation mechanism derived from "
   "CRYSTALS-Kyber), FIPS 204 (ML-DSA, the digital signature scheme derived from CRYSTALS-Dilithium) and "
   "FIPS 205 (SLH-DSA, based on the hash-based SPHINCS+ construction). A fourth-round process continues to "
   "evaluate additional candidates, particularly in the code-based family, to ensure algorithmic diversity "
   "against the possibility of future cryptanalytic advances. The dramatic break of SIKE in 2022 \u2013 once a "
   "promising isogeny-based candidate, reduced to practical insecurity by Castryck and Decru's classical "
   "attack \u2013 offers a salutary reminder that even finalists can fall, and that hedged migration strategies "
   "are prudent rather than paranoid.\n\n"
   "Migration, however, is where the theory collides with operational reality. Cryptography is embedded in "
   "virtually every layer of the computing stack: TLS and IPsec, firmware signing and secure boot, identity "
   "and certificate authorities, code-signing pipelines, long-term document archives, and an enormous variety "
   "of application-layer protocols. Building a Cryptographic Bill of Materials (CBOM) \u2013 an inventory of all "
   "cryptographic dependencies, their algorithms, parameters, and locations \u2013 turns out to be far harder "
   "than most organisations initially believed. A distressing share of enterprise software cannot accurately "
   "answer the apparently simple question of which algorithms it actually uses at runtime.\n\n"
   "The 'harvest now, decrypt later' threat complicates planning further. Adversaries with sufficient storage "
   "capacity can record encrypted traffic today and wait to decrypt it when a capable quantum computer becomes "
   "available. Any data whose confidentiality must survive, say, twenty years \u2013 intelligence sources, "
   "industrial secrets, personal health data \u2013 is already effectively exposed, unless it is re-encrypted with "
   "post-quantum protection before the quantum threshold is crossed. The implication is that the relevant "
   "migration deadline is not the arrival of the quantum computer but the earliest date at which sensitive "
   "long-lived data is transmitted under classical encryption.\n\n"
   "Hybrid schemes, combining a classical primitive with a post-quantum one, offer a pragmatic bridge. "
   "They preserve protection against classical cryptanalytic surprises in the new post-quantum algorithms "
   "while providing post-quantum assurance against the quantum adversary. TLS 1.3 draft experiments at Cloudflare "
   "and Google, and early mandates from agencies such as the US National Security Agency under its CNSA 2.0 "
   "suite, suggest that hybrid deployment is the current consensus. Whether in the long run the industry "
   "settles on pure post-quantum primitives, once confidence in them matures, is a decision that will have "
   "to be made against yet-unfolding results in lattice cryptanalysis. For the systems engineer, the message "
   "is unusually simple: crypto-agility \u2013 the ability to swap primitives as the landscape shifts \u2013 is no "
   "longer a nicety but a minimum architectural requirement for any system with a meaningful design lifespan."
  ),
  "source":"Adapted from NIST FIPS 203/204/205 (csrc.nist.gov, PD); Castryck & Decru, 'An efficient key recovery attack on SIDH' (2022, preprint); CNSA 2.0 suite (nsa.gov, PD); Cloudflare and Google post-quantum TLS deployment notes.",
  "exercises":[
   {"type":"mcq","q":"Which FIPS standard corresponds to ML-KEM (Kyber-derived)?",
    "options":["FIPS 186","FIPS 203","FIPS 204","FIPS 205"],"a":1,
    "explain":"'FIPS 203 (ML-KEM\u2026 from CRYSTALS-Kyber)\u2026'"},
   {"type":"tfng","q":"SIKE remains a recommended NIST post-quantum finalist.","a":"F",
    "explain":"'\u2026dramatic break of SIKE in 2022\u2026'"},
   {"type":"gap","q":"The 'harvest now, decrypt ____' threat motivates urgent migration for long-lived secrets.",
    "a":"later","alts":["later"]},
   {"type":"match","pairs":[
    ["FIPS 203","ML-KEM (Kyber)"],
    ["FIPS 204","ML-DSA (Dilithium)"],
    ["FIPS 205","SLH-DSA (SPHINCS+)"],
    ["CNSA 2.0","NSA post-quantum suite mandate"]]},
   {"type":"short","q":"Why is 'crypto-agility' described as a minimum architectural requirement?",
    "model":"Model: Because the post-quantum landscape is still evolving \u2013 candidates can fall (SIKE), hybrid schemes dominate today, and future breaks are possible \u2013 so systems must be designed so that cryptographic primitives can be swapped without re-architecting the whole product."}
  ]
 },
},
}

# ---- merge into existing JSON ----
path = Path(r"E:\CLAUDE\PAOLO BACA MANRIQUE\course-app\course_data.json")
course = json.loads(path.read_text(encoding="utf-8"))

merged = 0
for level in course["levels"]:
    lvl_code = level["code"]
    for lesson in level["lessons"]:
        pilot = PILOT.get(lvl_code, {}).get(lesson["n"])
        if pilot:
            text = pilot["passage"]
            wc = len([w for w in text.replace("\n"," ").split() if w])
            lesson["passage"] = {
                "title": pilot.get("title", lesson["topic"]),
                "text": text,
                "word_count": wc,
                "source": pilot["source"],
            }
            lesson["exercises"] = pilot["exercises"]
            lesson["has_content"] = True
            merged += 1
        else:
            lesson.setdefault("has_content", False)

path.write_text(json.dumps(course, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"OK: Merged {merged} pilot lessons into course_data.json")
# stats
total = 0
for lv in course["levels"]:
    filled = sum(1 for le in lv["lessons"] if le.get("has_content"))
    wc = sum(le.get("passage",{}).get("word_count",0) for le in lv["lessons"] if le.get("has_content"))
    print(f"  {lv['code']}: {filled}/20 lecciones con texto, {wc} palabras")
    total += wc
print(f"  TOTAL palabras en textos piloto: {total}")
