"""
Flyers Practice Tests 6-10 content.
"""

from flyers_content import _rw, _listening


# =====================================================================
# TEST 6 – WEATHER & SEASONS
# =====================================================================
TEST_6 = {
    'number': 6,
    'theme': 'Weather & Seasons',
    'rw': _rw(
        p1={
            'words': ['an umbrella', 'a rainbow', 'sunglasses', 'snowflakes', 'wellies',
                      'a scarf', 'gloves', 'a coat', 'a cloud', 'lightning',
                      'a raincoat', 'sandals', 'thunder', 'autumn leaves', 'ice'],
            'example': 'a rainbow',
            'defs': [
                'You wear this to cover your hands when it is cold.',
                'You open this over your head when it is raining.',
                'Small pieces of frozen water that fall from the sky in winter.',
                'Long and soft, you put it around your neck when it is cold.',
                'A big coat that keeps you dry when it rains.',
                'Big boots to walk in water or mud.',
                'You wear these on your eyes when the sun is very bright.',
                'Water on the ground that becomes hard when it is very cold.',
                'Open shoes for the hot summer.',
                'This is a big sound you hear during a storm.',
            ],
        },
        p2={
            'speakerA': 'Max', 'speakerB': 'Zoe',
            'line0_a': 'Zoe, look at the sky! Do you think it\u2019s going to rain?',
            'line0_b_letter': 'A',
            'line0_b_text': 'I think so – those clouds are very dark.',
            'pairs': [
                {'a': 'Should we take our umbrellas to school?'},
                {'a': 'Good idea. What about our football lesson outside?'},
                {'a': 'Yes, the teacher told us yesterday it might rain today.'},
                {'a': 'Shall we wear our raincoats too?'},
                {'a': 'Perfect. Remember my new wellies!'},
                {'a': 'OK, see you at the bus stop!'},
            ],
            'options': [
                ('A', 'I think so – those clouds are very dark.'),
                ('B', 'Bye, see you in five minutes.'),
                ('C', 'Definitely. Mine is the red one.'),
                ('D', 'Yes, let\u2019s put on the yellow ones.'),
                ('E', 'I forgot mine! I will borrow Dad\u2019s.'),
                ('F', 'Oh yes! They have dinosaurs on them, right?'),
                ('G', 'Maybe we can play basketball in the gym instead.'),
                ('H', 'I hate the rain. It\u2019s so cold!'),
            ],
        },
        p3={
            'words': ['beach', 'sunny', 'hot', 'umbrella', 'played', 'swam', 'holiday', 'family'],
            'title': 'A summer day',
            'text': ('Last August, my __(1)__ and I went on __(2)__ to the seaside. The weather was very '
                     '__(3)__ and beautifully __(4)__. We took our big blue __(5)__ with us to sit under. '
                     'In the morning, we __(6)__ in the sea, and later we ate ice cream on the beach.'),
            'title_choices': [
                ('A', 'A rainy Monday'),
                ('B', 'A summer day'),
                ('C', 'My new school'),
            ],
        },
        p4={
            'title': 'The four seasons',
            'text': ('In many parts of the world, there are four seasons: spring, summer, autumn and winter. '
                     'Each __(1)__ is different. In spring, the flowers start __(2)__ and the weather is fresh. '
                     'In summer, the sun __(3)__ very bright and many children go on holiday. '
                     'In autumn, the leaves turn red, yellow and brown, and __(4)__ start to wear jackets. '
                     'In winter, some places __(5)__ lots of snow and it is very cold. '
                     'Near the equator, there __(6)__ only two seasons – a dry and a rainy one.'),
            'items': [
                {'q': '1', 'options': {'A': 'year', 'B': 'day', 'C': 'season'}},
                {'q': '2', 'options': {'A': 'grow', 'B': 'growing', 'C': 'grew'}},
                {'q': '3', 'options': {'A': 'is', 'B': 'are', 'C': 'has'}},
                {'q': '4', 'options': {'A': 'people', 'B': 'animals', 'C': 'trees'}},
                {'q': '5', 'options': {'A': 'got', 'B': 'get', 'C': 'gets'}},
                {'q': '6', 'options': {'A': 'is', 'B': 'are', 'C': 'be'}},
            ],
        },
        p5={
            'title': 'The snow day',
            'text': ('Last January, there was a big surprise in my town. When I woke up on Tuesday morning, '
                     'I looked out of the window and I couldn\u2019t believe my eyes. There was snow everywhere! '
                     'It was the first snow in our town for six years. '
                     'I quickly put on my coat, scarf and gloves and I ran outside. My neighbour Joe was already '
                     'there with his little dog, Bertie. We decided to build a snowman together. '
                     'Our snowman was 1 metre 20 tall. We gave him two round black stones for eyes, a carrot '
                     'for his nose, and Joe\u2019s old red hat. We called him Mr Chilly. '
                     'Then my sister Kate came outside. She had a big plastic plate and we used it to slide '
                     'down the small hill near our house. At lunchtime, Mum called us for hot chocolate. '
                     'By the afternoon, the snow started to melt, but Mr Chilly stayed until the next morning.'),
            'example_q': 'When did it snow?',
            'example_a': 'Tuesday (morning)',
            'questions': [
                'When was the last time it snowed in the town?',
                'Who did the writer build a snowman with?',
                'What is Joe\u2019s dog called?',
                'How tall was the snowman?',
                'What was used for the snowman\u2019s nose?',
                'What did Kate bring outside?',
                'What did they drink at lunchtime?',
            ],
        },
        p6={
            'title': 'Winter in the mountains',
            'text': ('Every December, __(ex)__ go to the mountains with my parents. We love skiing and playing '
                     'in the snow. Our house there is small but __(1)__ is very warm inside. '
                     'We always __(2)__ lots of warm clothes: coats, hats, scarves and boots. '
                     'In the morning, we go skiing. In the afternoon, we __(3)__ hot chocolate in a café. '
                     'I\u2019m not __(4)__ good skier as my brother, but I try hard. Once, my brother fell '
                     '__(5)__ his skis – it was very funny! In the evening, we watch films and play cards '
                     '__(6)__ the fire.'),
            'example': 'I',
            'answers': ['it', 'wear', 'drink', 'as', 'off', 'by/near'],
        },
        p7={
            'title': 'A sudden storm',
            'p1': 'Three friends are having a picnic under a big tree on a sunny day.',
            'p2': 'Dark clouds come and it starts to rain heavily – their sandwiches get wet.',
            'p3': 'They run to a small shelter and laugh together while they wait for the rain to stop.',
        },
    ),
    'listening': _listening(
        p1={
            'scene': 'A park on a windy day: a boy flying a kite, a woman with a red hat running, '
                     'a girl with a blue umbrella, a man with a dog on a lead, children on a merry-go-round, '
                     'a girl reading on a bench, a boy with a yellow coat.',
            'example_name': 'Lucy',
            'names': ['Dylan', 'Robert', 'Olga', 'Tim', 'Poppy'],
        },
        p2={
            'heading': 'Weather report – Town radio',
            'example_label': 'Reporter\u2019s name',
            'example': 'Miss Green',
            'labels': [
                'Day',
                'Highest temperature (°C)',
                'Strong wind starts at (time)',
                'Rain: until which day?',
                'Best for: sunglasses / umbrella / ______ (one word)',
            ],
        },
        p3={
            'instruction': 'Alex is telling her grandma about the weather in different places last week.',
            'example_item': 'Monday (Spain)', 'example_letter': 'E',
            'items': ['Tuesday (Brazil)', 'Wednesday (Norway)', 'Thursday (Canada)',
                      'Friday (Egypt)', 'Saturday (UK)'],
            'options': [
                ('A', 'foggy'), ('B', 'windy'), ('C', 'snowy'), ('D', 'rainy'),
                ('E', 'sunny'), ('F', 'stormy'), ('G', 'hot and dry'), ('H', 'cloudy'),
            ],
        },
        p4={
            'items': [
                {'q': 'What clothes will the boy wear today?',
                 'A': 'shorts and a T-shirt', 'B': 'a raincoat and wellies',
                 'C': 'a coat and a scarf'},
                {'q': 'Where did the family go on holiday last summer?',
                 'A': 'to the mountains', 'B': 'to the beach', 'C': 'to a city'},
                {'q': 'What season does the girl like best?',
                 'A': 'spring', 'B': 'summer', 'C': 'autumn'},
                {'q': 'What did the children do when it rained?',
                 'A': 'watched TV', 'B': 'played a board game', 'C': 'read books'},
                {'q': 'What time will the sun come out?',
                 'A': '12 noon', 'B': '2 p.m.', 'C': '4 p.m.'},
            ],
        },
        p5={
            'scene': 'A winter garden: a snowman in the middle, a small tree with no leaves, a fence, '
                     'a bird on the fence, a child in a coat, a bench covered with snow, a ball in the snow.',
            'example': 'Colour the scarf of the snowman red.',
            'items': [
                'Colour the bird on the fence blue.',
                'Draw a carrot on the snowman\u2019s face.',
                'Colour the coat of the child green.',
                'Write the word COLD on the bench.',
                'Colour the ball in the snow yellow.',
            ],
        },
    ),
    'speaking': {
        'p1_ex': 'A park on a sunny day: a girl eating an ice cream, a dog running, a blue kite, '
                 'three balloons, a man reading a book, a bench with a bottle of water.',
        'p1_cand': 'A park on a RAINY day: a girl eating an ice cream, a dog running, a RED kite, '
                   'three balloons, a man reading a NEWSPAPER, a bench with a bottle of water.',
        'p1_diffs': [
            'Sunny vs rainy weather.',
            'Blue kite vs red kite.',
            'Book vs newspaper.',
            '(Plus: in one picture people might use an umbrella).',
        ],
        'p2_topic': 'Two summer camps',
        'p2_cand_card': 'CAMP: Mountain Days – Month: ______ – Temperature: usually ______°C – '
                        'Activities: ______, ______ and ______ – Clothes to bring: ______.',
        'p2_cand_qs': [
            'What\u2019s the name of the other summer camp?',
            'What month is it?',
            'What\u2019s the weather usually like?',
            'What activities can you do?',
            'What must you bring?',
        ],
        'p2_ex_card': 'CAMP: Sunny Beach Camp – July – usually 28°C – swimming, volleyball, sailing – '
                      'swimsuit, sunglasses, sun hat.',
        'p2_ex_qs': [
            'What\u2019s your camp called?',
            'When is the camp?',
            'What is the temperature normally?',
            'What activities do children do?',
            'What clothes should children bring?',
        ],
        'p3_title': 'The rainy party',
        'p3_p1': 'Children are preparing a birthday party in the garden with balloons and cakes.',
        'p3_p2': 'It starts raining a lot and the cakes get wet.',
        'p3_p3': 'The children move everything inside the house quickly.',
        'p3_p4': 'They have fun dancing indoors, and the rain stops at the end.',
        'p3_examiner_open': 'These pictures tell a story called "The rainy party". The children are preparing a party in the garden. Now you tell the rest.',
        'p4_questions': [
            'What\u2019s your favourite season? Why?',
            'What is the weather like today?',
            'What do you like doing in summer / in winter?',
            'Tell me about a very cold day you remember.',
            'Do you prefer sun or snow?',
        ],
    },
    'scripts': {
        'p1': ('Look at the park on a windy day. Lucy is the woman running with a red hat – that\u2019s the example.\n'
               '1. Where\u2019s Dylan? Dylan is the boy flying the kite.\n'
               '2. Now Robert. Robert is the boy wearing a yellow coat.\n'
               '3. Olga? Olga is the girl with the blue umbrella.\n'
               '4. Tim is the man with the dog on a lead.\n'
               '5. And Poppy? Poppy is the girl reading on the bench.'),
        'p2': ('Listen to the local radio weather report. Example: the reporter\u2019s name is Miss Green.\n'
               '— Hello, today is Friday.\n'
               '— The highest temperature today will be 22 degrees.\n'
               '— Strong wind will start at four o\u2019clock.\n'
               '— Rain will continue until Sunday.\n'
               '— Today is best for sunglasses, an umbrella or a hat – bring a hat if you go out!'),
        'p3': ('Alex is telling her grandma about the weather last week. Example: Spain on Monday was sunny.\n'
               '— Tuesday in Brazil – it was very hot and dry, almost 40 degrees!\n'
               '— Wednesday in Norway – it was really snowy all day.\n'
               '— Thursday in Canada – thick fog everywhere, you couldn\u2019t see cars.\n'
               '— Friday in Egypt – terribly windy, sand in the air.\n'
               '— And Saturday in the UK – as usual, rainy!'),
        'p4': ('1. — What will you wear today? — Not shorts. And not a coat – it\u2019s not that cold. I\u2019ll wear '
               'my raincoat and my wellies.\n'
               '2. — Where did you go last summer? — Not the mountains – too cold for me. Not a city either. We '
               'went to the beach.\n'
               '3. — Which season do you love? — I like spring, summer is nice, but autumn with the coloured '
               'leaves is definitely my favourite.\n'
               '4. — What did you do when it rained? — No TV, no books. We got out the big board game and '
               'played all afternoon.\n'
               '5. — What time will the sun come out? — It won\u2019t stop raining until two in the afternoon. '
               'After that the sun will shine.'),
        'p5': ('Look at the winter garden. Example: colour the scarf of the snowman red.\n'
               '1. On the fence, there\u2019s a bird. Colour it blue.\n'
               '2. On the snowman\u2019s face, draw a carrot – for his nose.\n'
               '3. The child is wearing a coat. Colour the coat green.\n'
               '4. Now on the bench, write the word COLD.\n'
               '5. There\u2019s a ball in the snow. Colour it yellow.'),
    },
    'answers': {
        'rw': {
            'p1': '1 gloves, 2 an umbrella, 3 snowflakes, 4 a scarf, 5 a raincoat, 6 wellies, '
                  '7 sunglasses, 8 ice, 9 sandals, 10 thunder',
            'p2': '1 C, 2 G, 3 D, 4 D, 5 F, 6 B',
            'p3': '1 family, 2 holiday, 3 hot, 4 sunny, 5 umbrella, 6 swam — Best title: B',
            'p4': '1 C (season), 2 B (growing), 3 A (is), 4 A (people), 5 B (get), 6 B (are)',
            'p5': '1 six years ago, 2 Joe (his neighbour), 3 Bertie, 4 1 metre 20 / 1.20 m, '
                  '5 a carrot, 6 a (big) plastic plate, 7 hot chocolate',
            'p6': '(ex) I — 1 it, 2 wear, 3 drink, 4 as, 5 off, 6 by',
            'p7': 'Sample: "Last Sunday, three friends went to the park for a picnic. The sun was shining '
                  'and they sat under a big tree. Suddenly, dark clouds came and it started to rain very '
                  'heavily! Their sandwiches got wet. They ran to a small shelter, laughing. They waited '
                  'there until the rain stopped." (52 words)',
        },
        'listening': {
            'p1': 'Dylan → boy with kite; Robert → yellow coat; Olga → blue umbrella; Tim → man with dog; '
                  'Poppy → girl reading.',
            'p2': '1 Friday, 2 22, 3 4 o\u2019clock / 4 p.m., 4 Sunday, 5 hat',
            'p3': '1 G, 2 C, 3 A, 4 B, 5 D',
            'p4': '1 B, 2 B, 3 C, 4 B, 5 B',
            'p5': '1 Bird blue; 2 Carrot drawn on snowman\u2019s face; 3 Coat green; 4 "COLD" on bench; '
                  '5 Ball yellow.',
        },
        'speaking': {
            'Part 1': 'Sunny vs rainy; blue/red kite; book/newspaper; accept any plausible 4 differences.',
            'Part 2': 'Examiner info: Sunny Beach Camp, July, 28°C, swimming/volleyball/sailing, swimsuit, '
                      'sunglasses, sun hat.',
            'Part 3': 'Accept: "It starts to rain. The children take everything inside. They dance in the '
                      'house. The rain stops."',
            'Part 4': 'Any answer with reason; weather vocabulary; past simple for "remember".',
        },
    },
}


# =====================================================================
# TEST 7 – TRAVEL & TRANSPORT
# =====================================================================
TEST_7 = {
    'number': 7,
    'theme': 'Travel & Transport',
    'rw': _rw(
        p1={
            'words': ['a train', 'a passport', 'a suitcase', 'a ticket', 'a station',
                      'a helicopter', 'a ferry', 'a lorry', 'an airport', 'a taxi',
                      'a map', 'a tram', 'a tunnel', 'a plane', 'a motorbike'],
            'example': 'a plane',
            'defs': [
                'A big vehicle for a family that carries things from one place to another, on the road.',
                'You need this special book to travel to other countries.',
                'This flies and it can go up and down without moving forward.',
                'A big boat that carries people and cars across the sea.',
                'You put your clothes in this when you travel.',
                'You need this to get on a train or a bus.',
                'A place where trains stop to collect passengers.',
                'A long hole through a mountain or under the river.',
                'A car you pay to take you somewhere fast.',
                'A big place with lots of planes coming and going.',
            ],
        },
        p2={
            'speakerA': 'Tourist', 'speakerB': 'Guide',
            'line0_a': 'Good morning. Can you tell me how to get to the museum, please?',
            'line0_b_letter': 'B',
            'line0_b_text': 'Of course. Are you travelling on foot or by bus?',
            'pairs': [
                {'a': 'On foot. Is it very far?'},
                {'a': 'Perfect. Which street is it on?'},
                {'a': 'Great. How long does it take to walk?'},
                {'a': 'OK. And how much are the tickets?'},
                {'a': 'Thanks. Can we eat inside the museum?'},
                {'a': 'Perfect, thank you very much!'},
            ],
            'options': [
                ('A', 'It\u2019s on the corner of King Street and Park Road.'),
                ('B', 'Of course. Are you travelling on foot or by bus?'),
                ('C', 'Just ten minutes from here.'),
                ('D', 'There\u2019s a café on the second floor.'),
                ('E', 'You\u2019re welcome. Enjoy your visit!'),
                ('F', 'Five pounds for adults and two pounds for children.'),
                ('G', 'No, not at all. About 15 minutes.'),
                ('H', 'The bus leaves at a quarter past ten.'),
            ],
        },
        p3={
            'words': ['airport', 'suitcases', 'waited', 'family', 'excited', 'watched', 'plane', 'holiday'],
            'title': 'Our trip to London',
            'text': ('Last summer, my __(1)__ and I went to London on __(2)__. We went to the __(3)__ '
                     'very early in the morning with all our __(4)__. We were all very __(5)__ because '
                     'it was my little brother\u2019s first time on a __(6)__. After two hours, we arrived '
                     'in London and we went to visit Big Ben.'),
            'title_choices': [
                ('A', 'Our trip to London'),
                ('B', 'A day at the farm'),
                ('C', 'A swimming lesson'),
            ],
        },
        p4={
            'title': 'Travelling by train',
            'text': ('Trains are a very comfortable and safe way to travel. You can see a __(1)__ of beautiful '
                     'places from the window. Trains do not __(2)__ in traffic like cars. '
                     'Some trains are very fast and can go from one city __(3)__ another in a few hours. '
                     'Many trains have a special carriage where you __(4)__ buy food and drinks. '
                     'Children under four years old usually travel for __(5)__. In some countries, you can '
                     'take a night train with small beds and you __(6)__ sleep while you travel.'),
            'items': [
                {'q': '1', 'options': {'A': 'lot', 'B': 'lots', 'C': 'many'}},
                {'q': '2', 'options': {'A': 'stop', 'B': 'stopped', 'C': 'stopping'}},
                {'q': '3', 'options': {'A': 'from', 'B': 'for', 'C': 'to'}},
                {'q': '4', 'options': {'A': 'can', 'B': 'must', 'C': 'are'}},
                {'q': '5', 'options': {'A': 'empty', 'B': 'free', 'C': 'nothing'}},
                {'q': '6', 'options': {'A': 'can', 'B': 'did', 'C': 'must'}},
            ],
        },
        p5={
            'title': 'An adventure on the ferry',
            'text': ('Last month, my class went on an adventure day to visit a small island near our town. '
                     'We travelled on a big red and white ferry. The trip was only 45 minutes but it was very fun. '
                     'Our teacher, Mr Lloyd, gave each of us a map with red marks for the important places. '
                     'First we visited the old lighthouse, which is 75 metres tall. '
                     'Then we had lunch in a little café called The Salty Fish. I had fish and chips, my best '
                     'friend Zara had a cheese sandwich. Zara said the café owner\u2019s dog was really cute. '
                     'After lunch, we walked to the top of a small hill and took lots of photos. '
                     'On the way back, the sea was rougher and some students felt sick, but I love the ferry '
                     'so I was happy. We arrived back at school at four o\u2019clock. What an amazing day!'),
            'example_q': 'What colour was the ferry?',
            'example_a': 'red and white',
            'questions': [
                'How long was the ferry trip?',
                'What did the teacher give to everyone?',
                'How tall is the lighthouse?',
                'What is the café called?',
                'What did Zara have for lunch?',
                'Why did some students feel sick?',
                'What time did they arrive at school?',
            ],
        },
        p6={
            'title': 'My journey to school',
            'text': ('I live in a village, so my __(ex)__ to school is quite long. Every morning, I wake up '
                     'at seven and __(1)__ breakfast with my parents. At half past seven, I leave the house '
                     '__(2)__ my bike. I ride for about twenty minutes to the next village. '
                     'There I take the school bus with __(3)__ friends. On the bus we talk, laugh __(4)__ '
                     'sometimes do homework. We __(5)__ at school at half past eight. '
                     'Yesterday, my bike had a problem and my dad took me in the __(6)__. It was faster '
                     'but I prefer the bike.'),
            'example': 'journey',
            'answers': ['have', 'on', 'my', 'and', 'arrive', 'car'],
        },
        p7={
            'title': 'The long train',
            'p1': 'A family is at the train station with lots of luggage.',
            'p2': 'They get on a very long train and sit next to the window.',
            'p3': 'They arrive at the beach and start to play in the sand.',
        },
    ),
    'listening': _listening(
        p1={
            'scene': 'A busy airport: a woman with a big red suitcase, a boy reading a travel book, '
                     'a man with a blue backpack, a girl with a camera around her neck, a pilot '
                     'with sunglasses, a woman in a uniform holding a clipboard, a small boy with his '
                     'teddy bear.',
            'example_name': 'Pilot John',
            'names': ['Mrs Baker', 'Sophie', 'Harry', 'Ryan', 'Tina'],
        },
        p2={
            'heading': 'Booking a holiday – Travel agency',
            'example_label': 'Agent\u2019s name',
            'example': 'Mrs White',
            'labels': [
                'Country',
                'Day of the flight',
                'Flight number (two numbers)',
                'Hotel name (star + word)',
                'Total price (£)',
            ],
        },
        p3={
            'instruction': 'Jamie is telling his friend which transport he used each day on holiday.',
            'example_item': 'Monday', 'example_letter': 'F',
            'items': ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
            'options': [
                ('A', 'bus'), ('B', 'train'), ('C', 'ferry'), ('D', 'bike'),
                ('E', 'taxi'), ('F', 'plane'), ('G', 'tram'), ('H', 'on foot'),
            ],
        },
        p4={
            'items': [
                {'q': 'How will the boy get to the party?',
                 'A': 'by taxi', 'B': 'by bike', 'C': 'by bus'},
                {'q': 'What time does the bus leave?',
                 'A': '10:15', 'B': '10:30', 'C': '10:45'},
                {'q': 'Where did Granny go last weekend?',
                 'A': 'to Spain', 'B': 'to Greece', 'C': 'to Italy'},
                {'q': 'What is the boy\u2019s favourite vehicle?',
                 'A': 'a lorry', 'B': 'a motorbike', 'C': 'a helicopter'},
                {'q': 'Where is the station?',
                 'A': 'next to the bank', 'B': 'behind the supermarket', 'C': 'opposite the hospital'},
            ],
        },
        p5={
            'scene': 'A busy street: a taxi, a bus, a tree, a man on a bike, a shop with a big window, '
                     'a traffic light, a dog crossing the road, a boy with a scooter.',
            'example': 'Colour the taxi yellow.',
            'items': [
                'Colour the bus orange.',
                'Draw a flag on the bus.',
                'Colour the dog white.',
                'Write STOP on the traffic light.',
                'Colour the man\u2019s bike pink.',
            ],
        },
    ),
    'speaking': {
        'p1_ex': 'A train station: a woman with a big suitcase, a boy eating an apple, a clock at 9:00, '
                 'three travellers in a queue, a blue train arriving, a cat on the platform.',
        'p1_cand': 'A train station: a woman with a big suitcase, a boy eating a BANANA, a clock at 9:00, '
                   'FIVE travellers in a queue, a RED train arriving, a cat on the platform.',
        'p1_diffs': [
            'Apple vs banana.',
            'Three travellers vs five.',
            'Blue train vs red train.',
            '(Clock same, suitcase same – find remaining different detail).',
        ],
        'p2_topic': 'Two holidays',
        'p2_cand_card': 'HOLIDAY: Blue Island – Transport: ______ – Days: ______ – Hotel: ______ stars – '
                        'Activities: ______, ______ – Weather: ______.',
        'p2_cand_qs': [
            'Where is your holiday?',
            'How do people go there?',
            'How many days is the holiday?',
            'What\u2019s the hotel like?',
            'What activities can you do there?',
        ],
        'p2_ex_card': 'HOLIDAY: Forest Lodge – Transport: train – 5 days – 4-star lodge – hiking, fishing, '
                      'biking – cool and fresh.',
        'p2_ex_qs': [
            'What\u2019s the name of your holiday?',
            'How do you travel there?',
            'How many nights do you stay?',
            'What are the rooms like?',
            'What\u2019s the weather like?',
        ],
        'p3_title': 'The bus home',
        'p3_p1': 'A boy misses the school bus and watches it leave.',
        'p3_p2': 'He calls his mum on the phone.',
        'p3_p3': 'His mum picks him up in the car.',
        'p3_p4': 'He arrives home and they have dinner together.',
        'p3_examiner_open': 'These pictures tell a story called "The bus home". The boy is running but he misses the school bus. Now you tell the rest.',
        'p4_questions': [
            'How do you usually travel to school?',
            'Tell me about a long journey you have made.',
            'Do you like planes or cars? Why?',
            'Where would you like to go for your next holiday?',
            'Have you been on a boat or ferry? What was it like?',
        ],
    },
    'scripts': {
        'p1': ('Look at the airport. Pilot John is the pilot with the sunglasses – that\u2019s the example.\n'
               '1. Mrs Baker is the woman in a uniform holding the clipboard.\n'
               '2. Sophie is the girl with the camera around her neck.\n'
               '3. Harry is the man with the blue backpack.\n'
               '4. Ryan is the boy reading the travel book.\n'
               '5. Tina is the small girl, actually the small boy… Tina is the small girl who isn\u2019t here, '
               'sorry, Tina is the woman with the big red suitcase.'),
        'p2': ('A family is booking a holiday. Example: the agent is Mrs White.\n'
               '— Which country, please?\n— Italy!\n'
               '— Day of the flight?\n— On Saturday, please.\n'
               '— Your flight number is IA 27.\n'
               '— What about the hotel?\n— It\u2019s the 5-star Sunshine.\n'
               '— And the total price?\n— That\u2019s £950 for the whole family.'),
        'p3': ('Jamie is telling his friend about his holiday transport. Example: Monday – plane.\n'
               '— Tuesday we took a tram all around the city.\n'
               '— Wednesday we went on foot to the old town – everywhere is close.\n'
               '— Thursday we rented bikes and had a race.\n'
               '— Friday we took a ferry to a small island.\n'
               '— Saturday we came home by train.'),
        'p4': ('1. — How will you go to the party? — My dad can\u2019t drive. The bus finishes too early. '
               'I\u2019ll take a taxi.\n'
               '2. — What time does the bus go? — Not a quarter past. Quarter to eleven. Oh sorry, half past '
               'ten actually.\n'
               '3. — Where did Granny go? — She went to Spain last year. This weekend – Greece!\n'
               '4. — What vehicle do you love? — Lorries are cool, motorbikes too, but helicopters are my '
               'absolute favourite.\n'
               '5. — Where\u2019s the station? — Not next to the bank. Not behind the supermarket. It\u2019s '
               'exactly opposite the hospital.'),
        'p5': ('Example: colour the taxi yellow.\n'
               '1. The bus – colour it orange.\n'
               '2. On the bus, draw a flag.\n'
               '3. The dog crossing the road – colour it white.\n'
               '4. On the traffic light, write STOP.\n'
               '5. The man on the bike – colour his bike pink.'),
    },
    'answers': {
        'rw': {
            'p1': '1 a lorry, 2 a passport, 3 a helicopter, 4 a ferry, 5 a suitcase, 6 a ticket, '
                  '7 a station, 8 a tunnel, 9 a taxi, 10 an airport',
            'p2': '1 G, 2 A, 3 C, 4 F, 5 D, 6 E',
            'p3': '1 family, 2 holiday, 3 airport, 4 suitcases, 5 excited, 6 plane — Best title: A',
            'p4': '1 B (lots), 2 A (stop), 3 C (to), 4 A (can), 5 B (free), 6 A (can)',
            'p5': '1 45 minutes, 2 a map, 3 75 metres, 4 The Salty Fish, 5 a cheese sandwich, '
                  '6 the sea was rougher, 7 (at) four o\u2019clock',
            'p6': '(ex) journey — 1 have, 2 on, 3 my, 4 and, 5 arrive, 6 car',
            'p7': 'Sample: "The Jones family went on holiday. They arrived at the station with lots of '
                  'luggage. They got on a very long train and sat next to the window. They watched the '
                  'countryside for three hours. Finally the train stopped at the beach and the children '
                  'ran happily onto the sand." (50 words)',
        },
        'listening': {
            'p1': 'Mrs Baker → woman in uniform with clipboard; Sophie → girl with camera; Harry → blue '
                  'backpack; Ryan → boy with travel book; Tina → woman with red suitcase.',
            'p2': '1 Italy, 2 Saturday, 3 IA 27 (27), 4 5-star Sunshine, 5 950',
            'p3': '1 G, 2 H, 3 D, 4 C, 5 B',
            'p4': '1 A, 2 B, 3 B, 4 C, 5 C',
            'p5': '1 Bus orange; 2 Flag drawn on bus; 3 Dog white; 4 "STOP" on traffic light; '
                  '5 Bike pink.',
        },
        'speaking': {
            'Part 1': 'Apple/banana; 3/5 travellers; blue/red train; plus any plausible 4th difference '
                      '(e.g. cat colour).',
            'Part 2': 'Examiner info: Forest Lodge, train, 5 days, 4-star, hiking/fishing/biking, cool '
                      'and fresh.',
            'Part 3': 'Accept: "The boy calls his mum. She comes with the car. They arrive home and have '
                      'dinner."',
            'Part 4': 'Transport vocabulary; past participle/past simple for experience; reasons for '
                      'preferences.',
        },
    },
}


# =====================================================================
# TEST 8 – JOBS & ROUTINES
# =====================================================================
TEST_8 = {
    'number': 8,
    'theme': 'Jobs & Daily Routines',
    'rw': _rw(
        p1={
            'words': ['a doctor', 'a nurse', 'a dentist', 'a mechanic', 'a farmer',
                      'a waiter', 'a firefighter', 'a police officer', 'a pilot', 'a teacher',
                      'a cook', 'a journalist', 'a librarian', 'a singer', 'a painter'],
            'example': 'a teacher',
            'defs': [
                'This person flies a plane.',
                'This person helps sick people in a hospital (not a doctor).',
                'This person checks your teeth and cleans them.',
                'This person works with farm animals and grows food.',
                'This person puts out fires.',
                'This person helps you in a restaurant and brings your food.',
                'This person fixes cars when they are broken.',
                'This person makes lovely food in a restaurant.',
                'This person writes for newspapers or magazines.',
                'This person works in a library and helps people find books.',
            ],
        },
        p2={
            'speakerA': 'Andy', 'speakerB': 'Mia',
            'line0_a': 'Hi Mia. What would you like to be when you grow up?',
            'line0_b_letter': 'E',
            'line0_b_text': 'I\u2019d love to be a vet – I really like animals!',
            'pairs': [
                {'a': 'That\u2019s great! What animals do you like most?'},
                {'a': 'Do you already have a pet?'},
                {'a': 'Wow, three pets! What are their names?'},
                {'a': 'Cute names. Are they difficult to look after?'},
                {'a': 'What about you, do you help your mum with them?'},
                {'a': 'Brilliant. I\u2019m sure you\u2019ll be an amazing vet.'},
            ],
            'options': [
                ('A', 'Yes, I feed them every morning before school.'),
                ('B', 'I like dogs and horses the best.'),
                ('C', 'Yes, I have a dog, a cat and a rabbit.'),
                ('D', 'Sometimes, especially when the rabbit gets out of her cage.'),
                ('E', 'I\u2019d love to be a vet – I really like animals!'),
                ('F', 'Thanks! I practise every day!'),
                ('G', 'My rabbit is called Bunny.'),
                ('H', 'Rex, Shadow and Coco.'),
            ],
        },
        p3={
            'words': ['mum', 'hospital', 'busy', 'visits', 'helped', 'kind', 'home', 'uniform'],
            'title': 'My mum\u2019s job',
            'text': ('My __(1)__ is a nurse at the big __(2)__ in town. She wears a blue __(3)__ every day. '
                     'Her job is very __(4)__ but she is always __(5)__ to the sick children. '
                     'Yesterday, my mum __(6)__ a little boy who broke his arm. '
                     'She gave him a sticker and a big smile. My mum is my hero.'),
            'title_choices': [
                ('A', 'My Saturday at the zoo'),
                ('B', 'My mum\u2019s job'),
                ('C', 'A trip to the cinema'),
            ],
        },
        p4={
            'title': 'What firefighters do',
            'text': ('Firefighters have a very important and __(1)__ job. Their main work is to put out fires '
                     'in houses, shops and forests. They __(2)__ a big red truck with lots of water and '
                     'special ladders. When there is a fire, they __(3)__ very quickly to help people. '
                     'Firefighters wear special yellow clothes and a helmet __(4)__ protect them from the heat. '
                     'They also rescue animals or people __(5)__ are stuck in dangerous places. '
                     'To become a firefighter, you must be __(6)__ strong and very brave.'),
            'items': [
                {'q': '1', 'options': {'A': 'easy', 'B': 'difficult', 'C': 'boring'}},
                {'q': '2', 'options': {'A': 'drive', 'B': 'drives', 'C': 'driven'}},
                {'q': '3', 'options': {'A': 'came', 'B': 'come', 'C': 'comes'}},
                {'q': '4', 'options': {'A': 'to', 'B': 'for', 'C': 'so'}},
                {'q': '5', 'options': {'A': 'where', 'B': 'which', 'C': 'who'}},
                {'q': '6', 'options': {'A': 'very', 'B': 'too', 'C': 'much'}},
            ],
        },
        p5={
            'title': 'Dad\u2019s new bakery',
            'text': ('Two months ago, my dad opened a small bakery on Queen Street. He has wanted to be a baker '
                     'since he was young, so we are all very proud of him. The name of the bakery is "Sweet '
                     'Morning" and it has a big window with a yellow sign. '
                     'My dad wakes up every day at four o\u2019clock to bake fresh bread. He makes 100 loaves '
                     'of bread every morning. He also makes chocolate cakes, strawberry tarts and cookies. '
                     'My favourite cookies are the ones with white chocolate chips. '
                     'My big sister helps him on Saturdays. She puts the cakes in the shop window and she '
                     'serves the customers. Last Saturday, she served more than fifty people! '
                     'I can\u2019t work in the bakery yet because I\u2019m only nine, but I help by tasting '
                     'everything. That\u2019s the best job!'),
            'example_q': 'Where is the bakery?',
            'example_a': 'on Queen Street',
            'questions': [
                'What is the name of the bakery?',
                'At what time does dad wake up?',
                'How many loaves of bread does he make?',
                'Who helps on Saturdays?',
                'How many people did she serve last Saturday?',
                'Why can\u2019t the writer work there?',
                'What is the writer\u2019s job?',
            ],
        },
        p6={
            'title': 'My daily routine',
            'text': ('Every school day, I wake __(ex)__ at seven o\u2019clock. I have breakfast with my family '
                     'and __(1)__ I brush my teeth. I usually wear my blue school uniform. '
                     'My mother takes me to school __(2)__ car. My first lesson starts at half past eight. '
                     'I __(3)__ four lessons before lunchtime. In the afternoon, we __(4)__ maths and music. '
                     'I come home at four and I play __(5)__ my dog, Bruno. Before dinner, I do my homework. '
                     'At nine o\u2019clock, I go __(6)__ bed. I love my routine.'),
            'example': 'up',
            'answers': ['then', 'by', 'have', 'do/have', 'with', 'to'],
        },
        p7={
            'title': 'A day in the life of a vet',
            'p1': 'A young vet arrives at her clinic and puts on her white coat.',
            'p2': 'She looks after a little puppy with a sore paw.',
            'p3': 'The happy owner thanks the vet and the puppy wags its tail.',
        },
    ),
    'listening': _listening(
        p1={
            'scene': 'A hospital corridor: a doctor looking at a chart, a nurse pushing a wheelchair, '
                     'a man in pyjamas reading a book, a child with a bandage on her arm, a cleaner '
                     'with a mop, a visitor carrying flowers, a cook pushing a food trolley.',
            'example_name': 'Dr Smith',
            'names': ['Nurse Ava', 'Mr Black', 'Emma', 'Mrs Lee', 'Chef Pablo'],
        },
        p2={
            'heading': 'New job – Babysitting',
            'example_label': 'Babysitter\u2019s name',
            'example': 'Olivia',
            'labels': [
                'First day',
                'Number of children',
                'Start time',
                'Money per hour (£)',
                'Family\u2019s last name',
            ],
        },
        p3={
            'instruction': 'Tom is telling his friend what he does each afternoon after school.',
            'example_item': 'Monday', 'example_letter': 'A',
            'items': ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday morning'],
            'options': [
                ('A', 'homework'), ('B', 'piano lesson'), ('C', 'football practice'), ('D', 'dance class'),
                ('E', 'swimming'), ('F', 'computer club'), ('G', 'help at the farm'),
                ('H', 'cinema with mum'),
            ],
        },
        p4={
            'items': [
                {'q': 'What does the girl want to be?',
                 'A': 'a doctor', 'B': 'a singer', 'C': 'a pilot'},
                {'q': 'What time does the dad usually start work?',
                 'A': '6:00', 'B': '7:00', 'C': '8:00'},
                {'q': 'What does the boy do first in the morning?',
                 'A': 'has a shower', 'B': 'brushes his teeth', 'C': 'eats breakfast'},
                {'q': 'Where does Mia\u2019s aunt work?',
                 'A': 'in a hospital', 'B': 'in a school', 'C': 'in a shop'},
                {'q': 'What did the children do after class yesterday?',
                 'A': 'went to the park', 'B': 'played music', 'C': 'watched a film'},
            ],
        },
        p5={
            'scene': 'A hospital waiting room: a nurse at a desk, a man with a broken leg on crutches, '
                     'a mother holding a baby, a small girl with a doll, a clock, a television on the wall, '
                     'a shelf with magazines.',
            'example': 'Colour the nurse\u2019s uniform green.',
            'items': [
                'Colour the television blue.',
                'Draw a flower on the desk.',
                'Colour the doll\u2019s dress red.',
                'Write the word HELP on the wall behind the nurse.',
                'Colour the biggest magazine purple.',
            ],
        },
    ),
    'speaking': {
        'p1_ex': 'A doctor\u2019s office: a doctor in a white coat, a child on a chair, a stethoscope, '
                 'a picture of a flower, a window with sun, a plant on the desk.',
        'p1_cand': 'A doctor\u2019s office: a doctor in a white coat, a child on a chair, a stethoscope, '
                   'a picture of a DOG, a window with sun, a CUP on the desk.',
        'p1_diffs': [
            'Picture of flower vs picture of dog.',
            'Plant vs cup on the desk.',
            '(Accept other small differences).',
            '(Accept other small differences).',
        ],
        'p2_topic': 'Two workers',
        'p2_cand_card': 'WORKER: Mr Brown – Job: ______ – Starts work at: ______ – Goes to work by: ______ – '
                        'Favourite part of the job: ______ – Uniform colour: ______.',
        'p2_cand_qs': [
            'What\u2019s the worker\u2019s job?',
            'How long has she/he worked there?',
            'How does she/he go to work?',
            'What time does she/he start?',
            'What does she/he like about the job?',
        ],
        'p2_ex_card': 'WORKER: Mrs Fox – Job: police officer – 12 years – Goes by bike – Starts 8 a.m. – '
                      'Likes helping people – Uniform: dark blue.',
        'p2_ex_qs': [
            'What\u2019s his job?',
            'What time does he start?',
            'How does he go to work?',
            'What\u2019s the best part of his job?',
            'What colour is his uniform?',
        ],
        'p3_title': 'Tom\u2019s morning',
        'p3_p1': 'Tom wakes up when his alarm clock rings.',
        'p3_p2': 'He eats breakfast with his family.',
        'p3_p3': 'He rides his bike to school with his friends.',
        'p3_p4': 'He arrives at school and gives a big smile to his teacher.',
        'p3_examiner_open': 'These pictures show Tom\u2019s morning. Tom wakes up when his alarm clock rings. Now you tell the rest.',
        'p4_questions': [
            'Tell me about your morning routine.',
            'What do you want to be when you grow up? Why?',
            'Who is your favourite person at school? Why?',
            'What jobs do people do in your family?',
            'Do you think being a teacher is easy or difficult?',
        ],
    },
    'scripts': {
        'p1': ('Look at the hospital. Dr Smith is the doctor looking at a chart – that\u2019s the example.\n'
               '1. Nurse Ava is the one pushing the wheelchair.\n'
               '2. Mr Black is the man in pyjamas reading a book.\n'
               '3. Emma is the child with a bandage on her arm.\n'
               '4. Mrs Lee is the visitor carrying flowers.\n'
               '5. Chef Pablo is the cook pushing the food trolley.'),
        'p2': ('A mum is calling a babysitter. Example: her name is Olivia.\n'
               '— When can you start?\n— On Monday, please.\n'
               '— How many children?\n— Two – a boy and a girl.\n'
               '— And the start time?\n— Six o\u2019clock in the evening.\n'
               '— Perfect. How much per hour?\n— I usually charge twelve pounds an hour.\n'
               '— Great. Our family name?\n— Our surname is Wilson.'),
        'p3': ('Tom is telling his friend about his afternoons. Example: Monday – homework.\n'
               '— Tuesday I go to football practice.\n'
               '— Wednesday is swimming – my favourite!\n'
               '— Thursday is piano lesson.\n'
               '— Friday I have dance class with my cousin.\n'
               '— And Saturday morning? I help at my grandpa\u2019s farm.'),
        'p4': ('1. — What do you want to be, Lily? — Not a doctor – I don\u2019t like blood. Not a singer – '
               'I can\u2019t sing. A pilot – that\u2019s my dream!\n'
               '2. — What time does Dad start? — Not at eight and not at seven. Very early – at six in the morning.\n'
               '3. — What do you do first, Ben? — I don\u2019t have breakfast yet. First I have a shower and '
               'then I brush my teeth.\n'
               '4. — Mia, where does your aunt work? — Not in the hospital. Not in a school either. She has '
               'a nice clothes shop.\n'
               '5. — What did you do after class? — Not the park – too cold. No films. We played our '
               'instruments in the music room.'),
        'p5': ('This is the hospital waiting room. Example: colour the nurse\u2019s uniform green.\n'
               '1. The television on the wall – colour it blue.\n'
               '2. On the desk, draw a flower.\n'
               '3. The little girl has a doll. Colour the doll\u2019s dress red.\n'
               '4. Behind the nurse, on the wall, write HELP.\n'
               '5. On the shelf there are magazines. Colour the biggest one purple.'),
    },
    'answers': {
        'rw': {
            'p1': '1 a pilot, 2 a nurse, 3 a dentist, 4 a farmer, 5 a firefighter, 6 a waiter, '
                  '7 a mechanic, 8 a cook, 9 a journalist, 10 a librarian',
            'p2': '1 B, 2 C, 3 H, 4 D, 5 A, 6 F',
            'p3': '1 mum, 2 hospital, 3 uniform, 4 busy, 5 kind, 6 helped — Best title: B',
            'p4': '1 B (difficult), 2 A (drive), 3 B (come), 4 A (to), 5 C (who), 6 A (very)',
            'p5': '1 Sweet Morning, 2 (at) four o\u2019clock, 3 100 loaves, 4 (his) big sister, '
                  '5 more than fifty, 6 (because) he is only nine, 7 tasting (everything)',
            'p6': '(ex) up — 1 then, 2 by, 3 have, 4 do, 5 with, 6 to',
            'p7': 'Sample: "Anna is a young vet. Every morning, she arrives at her clinic and puts on her '
                  'white coat. Yesterday, a little puppy with a sore paw came in. Anna cleaned the paw '
                  'carefully and gave the puppy some medicine. The puppy\u2019s owner said thank you and '
                  'the happy puppy wagged its tail." (52 words)',
        },
        'listening': {
            'p1': 'Nurse Ava → pushing wheelchair; Mr Black → pyjamas reading; Emma → bandage on arm; '
                  'Mrs Lee → visitor with flowers; Chef Pablo → food trolley.',
            'p2': '1 Monday, 2 2 (a boy and a girl), 3 6 o\u2019clock / 6 p.m., 4 12, 5 Wilson',
            'p3': '1 C, 2 E, 3 B, 4 D, 5 G',
            'p4': '1 C, 2 A, 3 A, 4 C, 5 B',
            'p5': '1 TV blue; 2 Flower drawn on desk; 3 Doll\u2019s dress red; 4 "HELP" on wall; '
                  '5 Biggest magazine purple.',
        },
        'speaking': {
            'Part 1': 'Flower vs dog picture; plant vs cup; accept any other two small differences.',
            'Part 2': 'Examiner info: Mrs Fox, police officer, 12 years, bike, 8 a.m., likes helping people, '
                      'dark blue uniform.',
            'Part 3': 'Accept: "Tom eats breakfast with his family. He rides his bike to school with his '
                      'friends. He arrives and smiles at his teacher."',
            'Part 4': 'Daily routine vocabulary; future with "want to be"; jobs in family; opinions.',
        },
    },
}


# =====================================================================
# TEST 9 – CLOTHES & BODY
# =====================================================================
TEST_9 = {
    'number': 9,
    'theme': 'Clothes & Body',
    'rw': _rw(
        p1={
            'words': ['a jumper', 'a dress', 'a skirt', 'a shirt', 'a tie',
                      'shorts', 'socks', 'a jacket', 'pyjamas', 'boots',
                      'a belt', 'a hat', 'a swimsuit', 'a scarf', 'earrings'],
            'example': 'a swimsuit',
            'defs': [
                'You wear this under your shoes on your feet.',
                'You wear these clothes in bed at night.',
                'Small things that girls (and some boys) wear on their ears.',
                'A kind of warm top you put over your head when it is cold.',
                'Boys or men wear this around their neck, with a shirt.',
                'A piece of clothing for girls or women – it goes around the waist.',
                'You wear this to keep your trousers up around your waist.',
                'This is a short piece of clothing for the legs. You wear it in summer.',
                'This goes over your other clothes when it\u2019s a little cold.',
                'You wear these tall shoes in the rain or snow.',
            ],
        },
        p2={
            'speakerA': 'Kate', 'speakerB': 'Lily',
            'line0_a': 'Lily, can you help me choose an outfit for the party?',
            'line0_b_letter': 'G',
            'line0_b_text': 'Of course! Is it a smart party or a casual one?',
            'pairs': [
                {'a': 'It\u2019s quite smart. My pink dress or my blue skirt?'},
                {'a': 'Perfect, the pink one. What shoes should I wear?'},
                {'a': 'Great idea! What about a necklace?'},
                {'a': 'Yes! And should I wear my long earrings?'},
                {'a': 'Thanks so much for helping me.'},
                {'a': 'OK. See you at seven!'},
            ],
            'options': [
                ('A', 'No problem – you always help me too!'),
                ('B', 'See you then. Have fun!'),
                ('C', 'Your silver necklace would be lovely.'),
                ('D', 'The pink dress is nicer – it\u2019s more elegant.'),
                ('E', 'Definitely! Your black shoes with small heels.'),
                ('F', 'Yes, they go perfectly with the pink dress.'),
                ('G', 'Of course! Is it a smart party or a casual one?'),
                ('H', 'I already have my dress for the party!'),
            ],
        },
        p3={
            'words': ['bought', 'shoes', 'special', 'shop', 'happy', 'tried', 'mum', 'clothes'],
            'title': 'A trip to the shopping centre',
            'text': ('Last Saturday, I went to the new shopping centre with my __(1)__. We went to buy '
                     '__(2)__ for school. First, we went to my favourite __(3)__, and I __(4)__ on many '
                     'jumpers. In the end, my mum __(5)__ me a blue one. We also bought new __(6)__ '
                     'because my feet have grown a lot!'),
            'title_choices': [
                ('A', 'A trip to the shopping centre'),
                ('B', 'My homework day'),
                ('C', 'A visit to the beach'),
            ],
        },
        p4={
            'title': 'How to stay healthy',
            'text': ('To have a healthy body, children __(1)__ do several things. First, it is important to eat '
                     'a lot of fruit and __(2)__. Second, we need to drink lots of water every day. '
                     'It is also important __(3)__ sleep between nine and eleven hours per night. '
                     'Exercise is __(4)__ very important – a good walk or playing in the park is great. '
                     'And remember, don\u2019t forget to __(5)__ your teeth after every meal! '
                     'Finally, when you __(6)__ not well, always tell an adult and go to see the doctor.'),
            'items': [
                {'q': '1', 'options': {'A': 'should', 'B': 'want', 'C': 'are'}},
                {'q': '2', 'options': {'A': 'vegetable', 'B': 'vegetables', 'C': 'a vegetable'}},
                {'q': '3', 'options': {'A': 'at', 'B': 'for', 'C': 'to'}},
                {'q': '4', 'options': {'A': 'too', 'B': 'also', 'C': 'either'}},
                {'q': '5', 'options': {'A': 'brush', 'B': 'brushing', 'C': 'brushed'}},
                {'q': '6', 'options': {'A': 'are', 'B': 'be', 'C': 'is'}},
            ],
        },
        p5={
            'title': 'The fashion show',
            'text': ('My school organised a fashion show last Friday evening. The show was in the big school '
                     'hall, and more than 200 people came to watch. The money from the tickets was for a '
                     'new sports area in the playground. '
                     'I was very nervous because I had to walk in front of everyone. I wore a beautiful green '
                     'dress and golden shoes. My friend Lola wore a red skirt, a white shirt and a small hat. '
                     'My classmate Felix was the funniest – he wore a huge purple jacket, very big sunglasses '
                     'and trainers with lights! Everyone laughed and clapped a lot. '
                     'Our maths teacher, Mr Grant, was the presenter. He told jokes between each outfit. '
                     'At the end, my sister took a photo of the whole group. I will keep it forever. '
                     'We raised £450 for the school – amazing!'),
            'example_q': 'Where was the fashion show?',
            'example_a': 'in the (school) hall',
            'questions': [
                'How many people came?',
                'What was the money for?',
                'What colour were the writer\u2019s shoes?',
                'Who wore a small hat?',
                'What did Felix wear on his feet?',
                'Who was the presenter?',
                'How much money did they raise?',
            ],
        },
        p6={
            'title': 'The circus outfit',
            'text': ('Last summer, my cousin Alex and __(ex)__ went to a circus show. When we arrived, a clown '
                     '__(1)__ colourful clothes gave us a programme. He was wearing a big red nose and green '
                     'shoes __(2)__ were enormous! In the show, we saw dancers __(3)__ beautiful silver '
                     'dresses and acrobats in tight blue suits. My favourite part was __(4)__ acrobat family '
                     'called the Flying Stars. They all wore matching outfits with stars. The dad __(5)__ '
                     'caught his daughter in the air. We clapped for five minutes. On the __(6)__ home, I '
                     'wanted to be an acrobat!'),
            'example': 'I',
            'answers': ['with/in', 'which/that', 'in', 'the/an', 'always', 'way'],
        },
        p7={
            'title': 'The lost shoe',
            'p1': 'A girl is running fast down a garden path.',
            'p2': 'One of her shoes falls off and she doesn\u2019t notice.',
            'p3': 'Her dad finds the shoe later and the girl laughs.',
        },
    ),
    'listening': _listening(
        p1={
            'scene': 'A family party: grandma in a yellow dress, a boy in a pirate costume, a girl in '
                     'a ballerina dress, a man in a blue suit, a woman in red trousers, a baby in '
                     'pink pyjamas, a teenage boy in a football shirt.',
            'example_name': 'Grandma Rose',
            'names': ['Jack', 'Mia', 'Uncle Tim', 'Aunt Zoe', 'Baby Eli'],
        },
        p2={
            'heading': 'Order at a clothes shop – online',
            'example_label': 'Customer\u2019s name',
            'example': 'Mr Khan',
            'labels': [
                'Item (clothing)',
                'Size (S, M, L, XL)',
                'Colour',
                'Price (£)',
                'Delivery day',
            ],
        },
        p3={
            'instruction': 'Maya is telling her sister what clothes different friends wore at school.',
            'example_item': 'Lily (Monday)', 'example_letter': 'D',
            'items': ['Ava (Tuesday)', 'Ben (Wednesday)', 'Mo (Thursday)', 'Sara (Friday)',
                      'Teacher Mrs Lu (Friday)'],
            'options': [
                ('A', 'green jumper'), ('B', 'pink dress'), ('C', 'white shirt & tie'), ('D', 'yellow T-shirt'),
                ('E', 'blue jeans'), ('F', 'red skirt'), ('G', 'black jacket'), ('H', 'sports shorts'),
            ],
        },
        p4={
            'items': [
                {'q': 'What does the boy want to buy?',
                 'A': 'a blue jacket', 'B': 'red trainers', 'C': 'black jeans'},
                {'q': 'Which part of the body does Mia have a problem with?',
                 'A': 'her arm', 'B': 'her leg', 'C': 'her ear'},
                {'q': 'What did Dad buy for the birthday?',
                 'A': 'a scarf', 'B': 'a belt', 'C': 'a watch'},
                {'q': 'What is the team\u2019s uniform colour?',
                 'A': 'green and white', 'B': 'yellow and black', 'C': 'red and blue'},
                {'q': 'What did the girl wear for the school play?',
                 'A': 'a long pink dress', 'B': 'a crown and a cape', 'C': 'a witch\u2019s costume'},
            ],
        },
        p5={
            'scene': 'A children\u2019s bedroom: a wardrobe, a bed with a teddy bear, a mirror, a shelf with '
                     'three boxes, a lamp, a window with curtains, a pair of shoes on the floor, a hat on a hook.',
            'example': 'Colour the teddy bear brown.',
            'items': [
                'Colour the curtains purple.',
                'Draw a T-shirt on the bed next to the teddy bear.',
                'Colour the hat on the hook pink.',
                'Write the word ROOM on the mirror.',
                'Colour the shoes on the floor blue.',
            ],
        },
    ),
    'speaking': {
        'p1_ex': 'A shop: a girl trying on a hat, a boy with a big backpack, a cashier with glasses, '
                 'three dresses on a rack, a blue mirror, a window with rain outside.',
        'p1_cand': 'A shop: a girl trying on a hat, a boy with a SMALL backpack, a cashier with glasses, '
                   'FIVE dresses on a rack, a GREEN mirror, a window with rain outside.',
        'p1_diffs': [
            'Big backpack vs small backpack.',
            'Three dresses vs five dresses.',
            'Blue mirror vs green mirror.',
            '(Accept additional reasonable difference).',
        ],
        'p2_topic': 'Two clothes shops',
        'p2_cand_card': 'SHOP: Star Fashion – Location: ______ – Most popular item: ______ – '
                        'Prices: from ______ pounds – Special day: ______ – Staff uniform: ______.',
        'p2_cand_qs': [
            'What\u2019s the shop\u2019s name?',
            'Where is it?',
            'What can you buy there?',
            'What is the cheapest thing?',
            'Is there a sale?',
        ],
        'p2_ex_card': 'SHOP: Happy Wear – 42 Queen Street – T-shirts, jeans, dresses – cheapest £8 – '
                      'sale on Saturdays – big sign says 50%.',
        'p2_ex_qs': [
            'What\u2019s the name of your shop?',
            'Where is Star Fashion?',
            'What do they sell a lot?',
            'How much is a T-shirt?',
            'What\u2019s special?',
        ],
        'p3_title': 'The birthday present',
        'p3_p1': 'A girl gives her mum a big box.',
        'p3_p2': 'Her mum opens the box and sees a new handbag.',
        'p3_p3': 'Her mum puts it on her shoulder and smiles.',
        'p3_p4': 'They go out together for a walk with the new bag.',
        'p3_examiner_open': 'These pictures tell a story called "The birthday present". A girl gives her mum a big box. Now you tell the rest.',
        'p4_questions': [
            'What clothes are you wearing today?',
            'What\u2019s your favourite colour for clothes? Why?',
            'What do you wear on special days?',
            'Do you prefer warm clothes or cool clothes? Why?',
            'Tell me about a new item of clothing you got.',
        ],
    },
    'scripts': {
        'p1': ('Look at the family party. Grandma Rose is in the yellow dress – that\u2019s the example.\n'
               '1. Jack is the boy in the pirate costume.\n'
               '2. Mia is the girl in the ballerina dress.\n'
               '3. Uncle Tim is the man in the blue suit.\n'
               '4. Aunt Zoe is the woman in the red trousers.\n'
               '5. Baby Eli is the baby in pink pyjamas.'),
        'p2': ('A man is ordering from an online shop. Example: his name is Mr Khan.\n'
               '— What would you like to buy?\n— A winter coat, please.\n'
               '— Size?\n— Large.\n'
               '— What colour?\n— Dark green, please.\n'
               '— The price is 65 pounds.\n'
               '— Delivery?\n— We can deliver on Wednesday.'),
        'p3': ('Maya is telling her sister about clothes. Example: Lily wore a yellow T-shirt on Monday.\n'
               '— Tuesday: Ava wore a pink dress – very pretty!\n'
               '— Wednesday: Ben was wearing a white shirt and a tie. Smart!\n'
               '— Thursday: Mo had sports shorts for PE all day.\n'
               '— Friday: Sara came in a black jacket – very cool.\n'
               '— And the teacher Mrs Lu wore a lovely red skirt on Friday.'),
        'p4': ('1. — What are you buying? — No jackets today – too warm. Black jeans? Maybe next time. I\u2019ll '
               'get these red trainers – so cool!\n'
               '2. — What\u2019s wrong, Mia? — My arm is fine. My leg too. But my ear hurts a lot.\n'
               '3. — What did Dad buy? — A scarf? No. A belt? No. A nice silver watch.\n'
               '4. — What colour\u2019s the team? — Not green. Not yellow. Red and blue, like always.\n'
               '5. — What did the girl wear? — Not a pink dress. Not a witch costume. She was a queen, so '
               'a crown and a cape.'),
        'p5': ('This is a bedroom. Example: colour the teddy bear brown.\n'
               '1. Colour the curtains purple.\n'
               '2. On the bed, next to the teddy bear, draw a T-shirt.\n'
               '3. The hat on the hook – colour it pink.\n'
               '4. On the mirror, write the word ROOM.\n'
               '5. The shoes on the floor – colour them blue.'),
    },
    'answers': {
        'rw': {
            'p1': '1 socks, 2 pyjamas, 3 earrings, 4 a jumper, 5 a tie, 6 a skirt, 7 a belt, '
                  '8 shorts, 9 a jacket, 10 boots',
            'p2': '1 D, 2 E, 3 C, 4 F, 5 A, 6 B',
            'p3': '1 mum, 2 clothes, 3 shop, 4 tried, 5 bought, 6 shoes — Best title: A',
            'p4': '1 A (should), 2 B (vegetables), 3 C (to), 4 B (also), 5 A (brush), 6 A (are)',
            'p5': '1 more than 200, 2 a new sports area, 3 golden/gold, 4 Lola, '
                  '5 trainers with lights, 6 Mr Grant, 7 £450',
            'p6': '(ex) I — 1 with (or in), 2 which (or that), 3 in, 4 the/an, 5 always, 6 way',
            'p7': 'Sample: "Nina was running very fast down the garden path because she was late. Suddenly, '
                  'one of her shoes fell off! She didn\u2019t notice and kept running. Later, her dad found '
                  'the shoe in the garden. He brought it to her and she laughed – what a silly moment!" '
                  '(53 words)',
        },
        'listening': {
            'p1': 'Jack → pirate costume; Mia → ballerina dress; Uncle Tim → blue suit; Aunt Zoe → red '
                  'trousers; Baby Eli → pink pyjamas.',
            'p2': '1 coat, 2 L (large), 3 dark green, 4 65, 5 Wednesday',
            'p3': '1 B, 2 C, 3 H, 4 G, 5 F',
            'p4': '1 B, 2 C, 3 C, 4 C, 5 B',
            'p5': '1 Curtains purple; 2 T-shirt drawn on bed; 3 Hat pink; 4 "ROOM" on mirror; '
                  '5 Shoes blue.',
        },
        'speaking': {
            'Part 1': 'Big/small backpack; 3/5 dresses; blue/green mirror; accept 4th plausible difference.',
            'Part 2': 'Examiner info: Happy Wear, 42 Queen Street, T-shirts/jeans/dresses, cheapest £8, '
                      'sale on Saturdays (50%).',
            'Part 3': 'Accept: "Mum opens the box and finds a new handbag. She puts it over her shoulder. '
                      'They go for a walk together."',
            'Part 4': 'Clothing vocabulary; opinions with reason; past simple for "new item"; comparative '
                      'structures.',
        },
    },
}


# =====================================================================
# TEST 10 – HOLIDAYS & CELEBRATIONS
# =====================================================================
TEST_10 = {
    'number': 10,
    'theme': 'Holidays & Celebrations',
    'rw': _rw(
        p1={
            'words': ['a candle', 'a balloon', 'a cake', 'fireworks', 'a present',
                      'a costume', 'a party', 'a card', 'decorations', 'a ribbon',
                      'an invitation', 'music', 'dancing', 'a guest', 'a photo'],
            'example': 'a party',
            'defs': [
                'A small round light that you put on a birthday cake.',
                'You write a nice message on this and give it to a friend on their birthday.',
                'These are beautiful lights that explode in the sky at special events.',
                'You wear this special outfit at a Halloween party.',
                'A sweet food with candles for a birthday.',
                'You blow air into this and it goes up in the sky.',
                'A person you invite to your house for a celebration.',
                'You receive this piece of paper and it tells you about a special event.',
                'You use this to tie a beautiful present.',
                'Colourful paper or lights you put on walls for a party.',
            ],
        },
        p2={
            'speakerA': 'Jenny', 'speakerB': 'Liam',
            'line0_a': 'Hey Liam, are you going to the school Halloween party?',
            'line0_b_letter': 'F',
            'line0_b_text': 'Of course! I\u2019m really excited. Are you?',
            'pairs': [
                {'a': 'Yes! What\u2019s your costume going to be?'},
                {'a': 'Cool! Did your mum help you make it?'},
                {'a': 'Are you going to eat lots of sweets?'},
                {'a': 'Haha! What about the scary films?'},
                {'a': 'Me neither! Shall we meet at the party?'},
                {'a': 'Perfect. See you on Saturday!'},
            ],
            'options': [
                ('A', 'Great. Don\u2019t forget your costume!'),
                ('B', 'Yes, she\u2019s really good at making costumes.'),
                ('C', 'Definitely! Especially chocolate ones.'),
                ('D', 'Yes, outside the school at seven p.m.'),
                ('E', 'I\u2019m going to be a vampire, with a black cape.'),
                ('F', 'Of course! I\u2019m really excited. Are you?'),
                ('G', 'No way, I hate scary things.'),
                ('H', 'The party was last weekend.'),
            ],
        },
        p3={
            'words': ['cousins', 'birthday', 'presents', 'big', 'happy', 'candles', 'sang', 'house'],
            'title': 'My birthday party',
            'text': ('Last Saturday was my ninth __(1)__ and I had a __(2)__ party at my __(3)__. '
                     'All my __(4)__ came with their parents. My mum made a huge chocolate cake with nine '
                     '__(5)__ on top. Everybody __(6)__ "Happy Birthday" and I got lots of __(7)__.'),
            'title_choices': [
                ('A', 'A boring homework day'),
                ('B', 'My birthday party'),
                ('C', 'A day at the doctor\u2019s'),
            ],
        },
        p4={
            'title': 'Celebrations around the world',
            'text': ('In different countries, people celebrate special days __(1)__ very different ways. '
                     'In China, the New Year is famous for beautiful red __(2)__ and dragon dances. '
                     'In Mexico, people __(3)__ the Day of the Dead with colourful flowers and special food. '
                     'In India, during Diwali, __(4)__ light candles and small oil lamps in their houses. '
                     'In the United States, children wear costumes and __(5)__ "trick or treat!" on Halloween. '
                     'Every country has its own celebration, but all around the world they are all days '
                     '__(6)__ are full of joy.'),
            'items': [
                {'q': '1', 'options': {'A': 'in', 'B': 'on', 'C': 'at'}},
                {'q': '2', 'options': {'A': 'decoration', 'B': 'decorations', 'C': 'decorating'}},
                {'q': '3', 'options': {'A': 'remember', 'B': 'remembers', 'C': 'remembering'}},
                {'q': '4', 'options': {'A': 'people', 'B': 'a person', 'C': 'someone'}},
                {'q': '5', 'options': {'A': 'say', 'B': 'tell', 'C': 'speak'}},
                {'q': '6', 'options': {'A': 'who', 'B': 'where', 'C': 'that'}},
            ],
        },
        p5={
            'title': 'Our summer camp',
            'text': ('Last July, I went to a summer camp called "Wild Adventures" with my twin brother Max. '
                     'The camp was in the countryside, next to a big lake. We stayed for 14 days. '
                     'There were 60 children in the camp, from 8 to 12 years old. Our leader, Aisha, was '
                     'really fun and always had good ideas for activities. '
                     'Every morning we had a different activity: swimming in the lake, climbing, archery, or '
                     'cooking around the campfire. My favourite was kayaking. Max\u2019s favourite was '
                     'making music with other children around the fire at night. '
                     'On the last day, we had a talent show. I sang a song with my new friends Petra and Juno. '
                     'Max did a magic trick and made a coin disappear. Everyone clapped loudly. '
                     'We went home with lots of stories and a small photo album. I want to go back next year!'),
            'example_q': 'What\u2019s the camp called?',
            'example_a': 'Wild Adventures',
            'questions': [
                'Where was the camp?',
                'How many children were there?',
                'Who was the leader?',
                'What was the writer\u2019s favourite activity?',
                'What did Max love doing?',
                'Who sang with the writer?',
                'What did Max do in the talent show?',
            ],
        },
        p6={
            'title': 'New Year\u2019s Eve',
            'text': ('New Year\u2019s Eve is my favourite celebration of the year. My family always stays '
                     '__(ex)__ home. My dad cooks a special dinner __(1)__ my mum decorates the living room '
                     'with balloons. My sister and I write a little letter about __(2)__ we want to do in '
                     'the new year. At eleven, we start __(3)__ a funny film together. At midnight, we open '
                     'the window __(4)__ we can hear the fireworks! My grandparents always phone us to say '
                     '"Happy __(5)__ Year". We eat a piece of cake and give __(6)__ other a big hug. Then '
                     'we go to bed very tired.'),
            'example': 'at',
            'answers': ['and', 'what', 'watching', 'so', 'New', 'each'],
        },
        p7={
            'title': 'The birthday cake',
            'p1': 'A boy is helping his mum to decorate a birthday cake in the kitchen.',
            'p2': 'They take the cake to the garden where a party is happening.',
            'p3': 'The boy\u2019s little sister blows out the candles and everyone claps.',
        },
    ),
    'listening': _listening(
        p1={
            'scene': 'A big party: children in different costumes – a witch, a superhero, a princess, '
                     'a robot, a dinosaur; an adult with a cake; a dog with a party hat; balloons '
                     'on the walls.',
            'example_name': 'Uncle Pete',
            'names': ['Bella', 'Fergus', 'Nina', 'Omar', 'Hero the dog'],
        },
        p2={
            'heading': 'Birthday planning',
            'example_label': 'Birthday boy/girl',
            'example': 'Amy',
            'labels': [
                'Party date (day + month)',
                'Number of friends invited',
                'Kind of cake',
                'Time: party starts at',
                'Place (name of park)',
            ],
        },
        p3={
            'instruction': 'Nathan is telling his cousin what he does every year on different holidays.',
            'example_item': 'New Year', 'example_letter': 'E',
            'items': ['Easter', 'Summer holiday', 'Halloween', 'Christmas', 'His birthday'],
            'options': [
                ('A', 'goes camping'), ('B', 'visits grandparents'), ('C', 'opens presents'),
                ('D', 'makes costumes'), ('E', 'watches fireworks'), ('F', 'paints eggs'),
                ('G', 'has a party at the pool'), ('H', 'goes to the beach'),
            ],
        },
        p4={
            'items': [
                {'q': 'What present is the girl going to give her mum?',
                 'A': 'a book', 'B': 'chocolates', 'C': 'flowers'},
                {'q': 'Where is the party going to be?',
                 'A': 'at the beach', 'B': 'in the garden', 'C': 'at the park'},
                {'q': 'What costume did the boy wear last Halloween?',
                 'A': 'a pirate', 'B': 'a wizard', 'C': 'a ghost'},
                {'q': 'What did the family do on New Year\u2019s Eve?',
                 'A': 'went to bed early', 'B': 'watched a film', 'C': 'went to a concert'},
                {'q': 'What is the girl\u2019s favourite part of her birthday?',
                 'A': 'the cake', 'B': 'the presents', 'C': 'being with friends'},
            ],
        },
        p5={
            'scene': 'A birthday party scene: a long table with a big cake, eight balloons tied to a chair, '
                     'a banner with "HAPPY BIRTHDAY", a clown juggling, a box of presents, a dog under '
                     'the table, a mirror on the wall.',
            'example': 'Colour the cake pink.',
            'items': [
                'Colour the biggest balloon red.',
                'Draw a star on the banner.',
                'Colour the clown\u2019s hat green.',
                'Write the number 9 on the biggest present.',
                'Colour the dog under the table black.',
            ],
        },
    ),
    'speaking': {
        'p1_ex': 'A birthday party: a cake with 8 candles, six children dancing, a boy with a present, '
                 'a dog on the floor, balloons in the air, a banner saying "HAPPY BIRTHDAY" in red.',
        'p1_cand': 'A birthday party: a cake with 10 candles, six children dancing, a boy with a present, '
                   'a CAT on the floor, balloons in the air, a banner saying "HAPPY BIRTHDAY" in BLUE.',
        'p1_diffs': [
            '8 candles vs 10 candles.',
            'Dog vs cat.',
            'Banner in red vs blue.',
            '(Accept other reasonable difference).',
        ],
        'p2_topic': 'Two holidays',
        'p2_cand_card': 'HOLIDAY: Winter Fun – Country: ______ – Starts: ______ – Special food: ______ – '
                        'Activities: ______ – Clothes: ______.',
        'p2_cand_qs': [
            'Where is your holiday?',
            'When does it happen?',
            'What do people eat?',
            'What\u2019s special about this holiday?',
            'Are there presents?',
        ],
        'p2_ex_card': 'HOLIDAY: Spring Flower Festival – in Japan – April – noodles and sweet rice cakes – '
                      'walking under cherry trees – families, not presents.',
        'p2_ex_qs': [
            'What\u2019s your holiday called?',
            'When does it start?',
            'What do people wear?',
            'What activities do they do?',
            'What do people eat?',
        ],
        'p3_title': 'A surprise party',
        'p3_p1': 'Children are hiding in a dark room, holding balloons and a cake.',
        'p3_p2': 'Their friend opens the door.',
        'p3_p3': 'Everyone shouts "SURPRISE!" and their friend is very surprised.',
        'p3_p4': 'They eat cake and dance together.',
        'p3_examiner_open': 'These pictures tell a story called "A surprise party". The children are hiding in a dark room. Now you tell the rest.',
        'p4_questions': [
            'What\u2019s your favourite holiday or celebration? Why?',
            'Tell me about your last birthday.',
            'Do you prefer giving or getting presents? Why?',
            'What do you do on New Year\u2019s Eve?',
            'What\u2019s a special food in your family for celebrations?',
        ],
    },
    'scripts': {
        'p1': ('Look at the big party. Uncle Pete is the adult with the cake – that\u2019s the example.\n'
               '1. Bella is the princess.\n'
               '2. Fergus is the dinosaur.\n'
               '3. Nina is the witch.\n'
               '4. Omar is the robot. — Actually wait, Omar is the superhero.\n'
               '5. Hero the dog is the dog with the party hat.'),
        'p2': ('A mum is planning a party. Example: the birthday girl is Amy.\n'
               '— What\u2019s the date?\n— On the 3rd of September.\n'
               '— How many friends?\n— She wants to invite ten friends.\n'
               '— What kind of cake?\n— A big strawberry cake.\n'
               '— What time does it start?\n— We\u2019ll start at four o\u2019clock.\n'
               '— And where?\n— At Green Park, near the lake.'),
        'p3': ('Nathan is talking about his year. Example: New Year – he watches fireworks.\n'
               '— At Easter, we always paint eggs with my grandma.\n'
               '— In the summer holiday, we go camping every year.\n'
               '— Halloween – my mum and I make our own costumes.\n'
               '— At Christmas I love going to visit my grandparents.\n'
               '— On my birthday, we always have a party at the pool – so much fun!'),
        'p4': ('1. — What are you giving Mum? — Not a book, she has too many. Chocolates? Maybe next time. '
               'I\u2019ll get a big bunch of flowers – she\u2019ll love them.\n'
               '2. — Where\u2019s the party? — Not the beach, it\u2019s raining. The garden is too small. '
               'We\u2019re going to the park this year.\n'
               '3. — Last Halloween, what were you? — Not a pirate, my sister was the pirate. Not a wizard. '
               'I was a very scary ghost!\n'
               '4. — What did you do on New Year\u2019s Eve? — Not bed – too early! No concert. We watched '
               'a film and waited for midnight.\n'
               '5. — What\u2019s your favourite part? — The cake\u2019s nice and the presents are OK, but '
               'really I love being with my friends most.'),
        'p5': ('A birthday party! Example: colour the cake pink.\n'
               '1. There are lots of balloons. Colour the biggest one red.\n'
               '2. On the banner, draw a star.\n'
               '3. The clown is juggling. Colour his hat green.\n'
               '4. On the biggest present, write the number 9.\n'
               '5. The dog under the table – colour the dog black.'),
    },
    'answers': {
        'rw': {
            'p1': '1 a candle, 2 a card, 3 fireworks, 4 a costume, 5 a cake, 6 a balloon, '
                  '7 a guest, 8 an invitation, 9 a ribbon, 10 decorations',
            'p2': '1 E, 2 B, 3 C, 4 G, 5 D, 6 A',
            'p3': '1 birthday, 2 big, 3 house, 4 cousins, 5 candles, 6 sang, 7 presents — Best title: B',
            'p4': '1 A (in), 2 B (decorations), 3 A (remember), 4 A (people), 5 A (say), 6 C (that)',
            'p5': '1 in the countryside / next to a lake, 2 60, 3 Aisha, 4 kayaking, '
                  '5 making music (around the fire), 6 Petra and Juno, 7 a magic trick (made a coin disappear)',
            'p6': '(ex) at — 1 and, 2 what, 3 watching, 4 so, 5 New, 6 each',
            'p7': 'Sample: "On Saturday morning, Leo helped his mum decorate a birthday cake for his little '
                  'sister. They used pink icing and five candles. In the afternoon, they took the cake to '
                  'the garden where all the family were waiting. Leo\u2019s sister blew out the candles '
                  'and everyone clapped. It was a perfect party!" (55 words)',
        },
        'listening': {
            'p1': 'Bella → princess; Fergus → dinosaur; Nina → witch; Omar → superhero; '
                  'Hero → dog with party hat.',
            'p2': '1 3 September (3/9), 2 10, 3 strawberry, 4 4 o\u2019clock, 5 Green (Park)',
            'p3': '1 F, 2 A, 3 D, 4 B, 5 G',
            'p4': '1 C, 2 C, 3 C, 4 B, 5 C',
            'p5': '1 Biggest balloon red; 2 Star drawn on banner; 3 Clown\u2019s hat green; '
                  '4 "9" on biggest present; 5 Dog black.',
        },
        'speaking': {
            'Part 1': '8/10 candles; dog/cat; banner red/blue; plus any 4th plausible difference.',
            'Part 2': 'Examiner info: Spring Flower Festival in Japan, April, noodles & sweet rice cakes, '
                      'walking under cherry trees, family event (no presents).',
            'Part 3': 'Accept: "Their friend opens the door. Everyone shouts SURPRISE. They eat cake and '
                      'dance together."',
            'Part 4': 'Festival vocabulary; personal narrative (past simple); opinions with reason; '
                      'cultural traditions.',
        },
    },
}
