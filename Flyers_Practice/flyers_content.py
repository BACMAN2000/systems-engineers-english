"""
Content data for 10 A2 Flyers practice tests.
All content is original. Structure follows Cambridge's published A2 Flyers specification.
"""

# --------- Helper to produce p7 sample story & speaking answers placeholders ---------

def _rw(p1, p2, p3, p4, p5, p6, p7):
    return {'p1': p1, 'p2': p2, 'p3': p3, 'p4': p4, 'p5': p5, 'p6': p6, 'p7': p7}


def _listening(p1, p2, p3, p4, p5):
    return {'p1': p1, 'p2': p2, 'p3': p3, 'p4': p4, 'p5': p5}


# =====================================================================
# TEST 1 – ANIMALS & PETS
# =====================================================================
TEST_1 = {
    'number': 1,
    'theme': 'Animals & Pets',
    'rw': _rw(
        p1={
            'words': ['a butterfly', 'a rabbit', 'a parrot', 'a dolphin', 'a camel',
                      'a kangaroo', 'a spider', 'a frog', 'a peacock', 'a shark',
                      'a bat', 'a panda', 'a squirrel', 'a giraffe', 'a crocodile'],
            'example': 'a dolphin',
            'defs': [
                'This animal has long ears and likes eating carrots.',
                'It is a large, dangerous fish with very sharp teeth.',
                'This animal has eight legs and makes webs to catch flies.',
                'It is a bird with colourful feathers that can copy words.',
                'This small animal has red fur and a big tail and eats nuts.',
                'This baby animal lives inside its mother\u2019s pocket.',
                'This animal is black and white and eats bamboo in China.',
                'It has a very long neck and eats leaves from tall trees.',
                'This small flying animal has colourful wings and visits flowers.',
                'It is green or brown and can jump high from the water.',
            ],
        },
        p2={
            'speakerA': 'Mum', 'speakerB': 'Sam',
            'line0_a': 'Sam, would you like to go to the animal park on Saturday?',
            'line0_b_letter': 'B',
            'line0_b_text': 'Yes, I\u2019d love to! I really want to see the elephants.',
            'pairs': [
                {'a': 'Great. Do you want to take your camera?'},
                {'a': 'We can leave at nine o\u2019clock. Is that okay?'},
                {'a': 'Perfect. What would you like to take to eat?'},
                {'a': 'And shall we ask your cousin Emma to come with us?'},
                {'a': 'Good idea. Do you want to go to the sea animals first or the monkeys?'},
                {'a': 'Fine. Remember to wear comfortable shoes.'},
            ],
            'options': [
                ('A', 'Let\u2019s see the monkeys first, please.'),
                ('B', 'Yes, I\u2019d love to! I really want to see the elephants.'),
                ('C', 'Yes, please. I\u2019ll yes, I will!'),
                ('D', 'Yes, please. I want to take lots of photos.'),
                ('E', 'Ham sandwiches and some apples, please.'),
                ('F', 'That\u2019s perfect. I\u2019ll get ready after breakfast.'),
                ('G', 'Yes! She loves animals too.'),
                ('H', 'Okay, I\u2019ll put on my trainers.'),
            ],
        },
        p3={
            'words': ['garden', 'noisy', 'food', 'water', 'happy', 'quickly', 'friendly', 'ran'],
            'title': 'Lucy\u2019s new rabbit',
            'text': ('Lucy\u2019s favourite animal is a rabbit. Last week, her father bought her a small '
                     'white rabbit for her birthday. Lucy was very __(1)__ and gave her new pet a big hug. '
                     'She called the rabbit Snowball. Snowball lives in a little house in the __(2)__. '
                     'Every morning Lucy gives Snowball fresh __(3)__ and some clean __(4)__. '
                     'The rabbit is very __(5)__ and likes to sit next to Lucy on the grass. '
                     'Yesterday, Snowball __(6)__ around the garden for almost an hour!'),
            'title_choices': [
                ('A', 'Lucy\u2019s new rabbit'),
                ('B', 'A day at the zoo'),
                ('C', 'A very noisy dog'),
            ],
        },
        p4={
            'title': 'All about dolphins',
            'text': ('Dolphins are very clever animals. They __(1)__ in the sea and they can swim very fast. '
                     'Dolphins are not fish. They are mammals, like people and dogs. '
                     'Baby dolphins stay with their mother __(2)__ two or three years. '
                     'Dolphins eat fish and other small sea animals. They can make different sounds to __(3)__ '
                     'to other dolphins. Some dolphins live in families of ten animals __(4)__ more. '
                     'People who study dolphins say they are __(5)__ friendly and like playing games. '
                     'In many parts of the world, you can __(6)__ dolphins swimming near boats.'),
            'items': [
                {'q': '1', 'options': {'A': 'live', 'B': 'lives', 'C': 'living'}},
                {'q': '2', 'options': {'A': 'at', 'B': 'on', 'C': 'for'}},
                {'q': '3', 'options': {'A': 'talk', 'B': 'tell', 'C': 'say'}},
                {'q': '4', 'options': {'A': 'also', 'B': 'or', 'C': 'but'}},
                {'q': '5', 'options': {'A': 'very', 'B': 'much', 'C': 'too'}},
                {'q': '6', 'options': {'A': 'look', 'B': 'watch', 'C': 'see'}},
            ],
        },
        p5={
            'title': 'The lost puppy',
            'text': ('On Saturday morning, Tom and his sister Mia were playing football in the park. '
                     'After the game, they sat down under a tree to drink some water. '
                     'Suddenly, they heard a small noise behind the tree. It was a tiny brown puppy. '
                     'The puppy was hungry and very thirsty. Tom gave it some of his water and Mia gave it '
                     'a piece of her sandwich. The puppy had a red collar but there was no phone number on it. '
                     '"We can\u2019t leave it here," said Mia. "Let\u2019s take it home and ask Mum what to do." '
                     'They walked home carefully. Mum was in the kitchen. When she saw the puppy, she smiled. '
                     '"It\u2019s the same puppy that Mrs Green was looking for yesterday," she said. '
                     'Tom and Mia went to Mrs Green\u2019s house. Mrs Green was very happy and gave the children '
                     'some chocolate cake. The puppy\u2019s name was Biscuit.'),
            'example_q': 'Where were Tom and Mia playing?',
            'example_a': 'in the park',
            'questions': [
                'What did Tom and Mia do after the game?',
                'What colour was the puppy?',
                'What did Tom give to the puppy?',
                'What did Mia give the puppy to eat?',
                'Who did Mum think the puppy belonged to?',
                'What did Mrs Green give the children?',
                'What was the puppy\u2019s name?',
            ],
        },
        p6={
            'title': 'My pet parrot',
            'text': ('My name is Leo and I have a beautiful pet parrot called Kiko. Kiko has green and yellow '
                     'feathers __(ex)__ a long tail. He lives in a big cage in __(1)__ bedroom. '
                     'Kiko is very clever. He __(2)__ say "hello" and "goodbye" in English and in Spanish! '
                     'Every day I give him fresh fruit, especially apples, __(3)__ are his favourite. '
                     'In the afternoon, I open the door of his cage and __(4)__ flies around the room. '
                     'Sometimes he sits __(5)__ my shoulder when I am reading. I love Kiko very much '
                     'because he makes __(6)__ family laugh every day.'),
            'example': 'and',
            'answers': ['my', 'can', 'which', 'he', 'on', 'my/our'],
        },
        p7={
            'title': 'The naughty cat',
            'p1': 'A girl puts a bowl of milk on the kitchen table for her cat.',
            'p2': 'The cat jumps up and drinks all the milk while the girl isn\u2019t looking.',
            'p3': 'The girl sees the empty bowl and the cat runs under the sofa.',
        },
    ),
    'listening': _listening(
        p1={
            'scene': 'Children playing in a park with different animals: a boy on a bench with a dog, '
                     'a girl by a pond with a duck, a boy climbing a tree, a girl riding a pony, '
                     'a man with a parrot on his shoulder, a woman feeding a rabbit, a boy on a bike.',
            'example_name': 'Daisy',
            'names': ['Oliver', 'Jenny', 'Peter', 'Sarah', 'Ben'],
        },
        p2={
            'heading': 'Animal club – New members',
            'example_label': 'Name of club',
            'example': 'Pawprint',
            'labels': [
                'Day of meetings',
                'Time of meetings',
                'Money to pay each month (£)',
                'Favourite pet of the teacher',
                'Street where the club is',
            ],
        },
        p3={
            'instruction': 'Mia is telling her friend about the animals she saw on holiday each day.',
            'example_item': 'Monday', 'example_letter': 'C',
            'items': ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
            'options': [
                ('A', 'horses'), ('B', 'parrots'), ('C', 'turtles'),
                ('D', 'elephants'), ('E', 'kangaroos'), ('F', 'monkeys'),
                ('G', 'sharks'), ('H', 'penguins'),
            ],
        },
        p4={
            'items': [
                {'q': 'Which pet did Tom get for his birthday?',
                 'A': 'a puppy with a ball', 'B': 'a rabbit in a cage', 'C': 'a goldfish in a bowl'},
                {'q': 'Where is Granny\u2019s cat now?',
                 'A': 'on the bed', 'B': 'under the table', 'C': 'on top of the cupboard'},
                {'q': 'Which animal did the class see at the zoo?',
                 'A': 'a tiger', 'B': 'a lion', 'C': 'a bear'},
                {'q': 'What is the dog wearing?',
                 'A': 'a red coat', 'B': 'a blue collar', 'C': 'a green jumper'},
                {'q': 'What does the parrot like to eat best?',
                 'A': 'nuts', 'B': 'bananas', 'C': 'apples'},
            ],
        },
        p5={
            'scene': 'A farm scene: a large barn, a tree with apples, a fence, a pond with a duck, '
                     'a horse, a pig, a cat on the roof, a farmer with a hat, a girl with a bucket.',
            'example': 'Colour the hat of the farmer blue.',
            'items': [
                'Colour the pig pink.',
                'Write the word FARM on the door of the barn.',
                'Colour the cat on the roof grey.',
                'Draw a ball next to the duck.',
                'Colour the apples on the tree red.',
            ],
        },
    ),
    'speaking': {
        'p1_ex': 'A beach: a boy with a red bucket, a dog near the water, a yellow umbrella, '
                 'a woman reading a book, three birds flying, a sandcastle with one flag.',
        'p1_cand': 'A beach: a boy with a BLUE bucket, a dog near the water, a yellow umbrella, '
                   'a woman EATING AN ICE-CREAM, FIVE birds flying, a sandcastle with TWO flags.',
        'p1_diffs': [
            'Bucket colour (red vs blue).',
            'The woman is reading vs eating ice-cream.',
            'Three birds vs five birds.',
            'Sandcastle with one flag vs two flags.',
        ],
        'p2_topic': 'Two pet shops',
        'p2_cand_card': 'PET SHOP: Happy Paws – Address: 14 ______ Street – Open: 9 a.m. to ______ – '
                        'Sells: dogs, cats and ______ – Most popular animal: ______ – Phone: 01 234 ______.',
        'p2_cand_qs': [
            'What is the name of your pet shop?',
            'Where is it?',
            'How much is a goldfish?',
            'Can you buy food for rabbits?',
            'What time does it open?',
        ],
        'p2_ex_card': 'PET SHOP: Furry Friends – Address: 28 Market Road – Open: 10 a.m. to 7 p.m. – '
                      'Sells: rabbits, guinea pigs, birds and fish – Most popular animal: hamster – '
                      'Phone: 01 234 5678.',
        'p2_ex_qs': [
            'What\u2019s the name of your pet shop?',
            'What\u2019s the address?',
            'What animals can you buy?',
            'What time does it close?',
            'What is the phone number?',
        ],
        'p3_title': 'Lucy and the parrot',
        'p3_p1': 'Lucy opens her bedroom window.',
        'p3_p2': 'A green parrot flies into her room and sits on the bed.',
        'p3_p3': 'Lucy gives the parrot a piece of apple.',
        'p3_p4': 'Lucy\u2019s neighbour comes to collect the parrot – it\u2019s his pet.',
        'p3_examiner_open': 'These pictures tell a story. It\u2019s called "Lucy and the parrot". Look at the pictures first. Lucy is in her bedroom and she is opening the window. Now you tell the story.',
        'p4_questions': [
            'Do you have a pet at home? What is it like?',
            'What\u2019s your favourite animal? Why?',
            'Would you like to work with animals when you\u2019re older?',
            'Tell me about an animal you saw recently.',
            'Are there many animals in your city?',
        ],
    },
    'scripts': {
        'p1': ('Look at the picture. There are lots of children in the park. Can you see Daisy? Yes, Daisy is the '
               'girl feeding the rabbit. Can you see the line from Daisy to the girl feeding the rabbit? Good, this is '
               'an example. Now you listen and draw lines.\n'
               '1. Where\u2019s Oliver? – Oliver is the boy on the bike.\n'
               '2. Can you see Jenny? – Yes, Jenny is the girl by the pond, near the duck.\n'
               '3. Where is Peter? – Peter is the boy climbing the tree.\n'
               '4. Where\u2019s Sarah? – Sarah is the girl riding the pony.\n'
               '5. Can you see Ben? – Yes, Ben is the boy on the bench with the dog.'),
        'p2': ('Listen, a boy and his mum are talking about a new animal club. Can you see the example? The club\u2019s '
               'name is Pawprint. Now listen and write.\n'
               '— Mum, this club looks fun! When do they meet?\n— Every Saturday, Tom.\n'
               '— At what time?\n— In the morning, at half past ten.\n'
               '— How much do I pay?\n— It\u2019s only eight pounds a month.\n'
               '— The teacher loves animals. What\u2019s her pet?\n— Her favourite pet is a turtle.\n'
               '— Cool. And what\u2019s the street called?\n— The club is on Bridge Street. Now listen again.'),
        'p3': ('Mia is telling her friend Alex about her holiday. Each day she saw different animals. The example is: '
               'on Monday she saw turtles – that\u2019s letter C. Now listen to the rest.\n'
               '— Mia, so what did you see on Tuesday?\n— On Tuesday we went to a farm and saw lots of horses.\n'
               '— And Wednesday?\n— Oh, Wednesday was amazing – we saw penguins at the aquarium.\n'
               '— What about Thursday?\n— That day we did a safari and saw elephants!\n'
               '— Nice. And Friday?\n— Friday we went to the jungle park and the monkeys were so funny.\n'
               '— And the last day?\n— On Saturday we went on a boat and saw some sharks, quite far away!'),
        'p4': ('1. What did Tom get for his birthday? — I got a lovely puppy. He has a little ball and he plays with it '
               'all day. A rabbit? No, my sister has a rabbit.\n'
               '2. Where is Granny\u2019s cat? — She was under the table this morning. Now she\u2019s up on top of the '
               'cupboard. Silly cat!\n'
               '3. What animal did the class see at the zoo? — It was very big with brown fur. Not a tiger or a lion. '
               'It was a bear – a huge brown bear.\n'
               '4. What\u2019s the dog wearing? — Not a red coat today, it\u2019s too warm. He has a blue collar with '
               'his name on it.\n'
               '5. What does your parrot like best? — He eats nuts and apples, but his absolute favourite are '
               'bananas – he\u2019s crazy about them!'),
        'p5': ('Look at the picture of the farm. It\u2019s a sunny day. There\u2019s a farmer with a hat – the example '
               'is: colour the farmer\u2019s hat blue. Now listen and draw and colour.\n'
               '1. Can you see the pig? Yes, colour the pig pink, please.\n'
               '2. The barn has a big door. Write the word FARM on the door.\n'
               '3. There\u2019s a cat on the roof. Colour the cat grey.\n'
               '4. There\u2019s a duck on the pond. Draw a ball next to the duck.\n'
               '5. Now look at the tree – colour all the apples red.'),
    },
    'answers': {
        'rw': {
            'p1': '1 a rabbit, 2 a shark, 3 a spider, 4 a parrot, 5 a squirrel, 6 a kangaroo, 7 a panda, '
                  '8 a giraffe, 9 a butterfly, 10 a frog',
            'p2': '1 D, 2 F, 3 E, 4 G, 5 A, 6 H',
            'p3': '1 happy, 2 garden, 3 food, 4 water, 5 friendly, 6 ran — Best title: A (Lucy\u2019s new rabbit)',
            'p4': '1 A (live), 2 C (for), 3 A (talk), 4 B (or), 5 A (very), 6 C (see)',
            'p5': '1 sat under a tree / drank water, 2 brown, 3 (some) water, 4 a piece / sandwich, '
                  '5 Mrs Green, 6 (some) chocolate cake, 7 Biscuit',
            'p6': '(example) and — 1 my, 2 can, 3 which, 4 he, 5 on, 6 my (or our)',
            'p7': 'Sample: "One morning, Anna put a bowl of milk on the table for her cat, Milo. When Anna left '
                  'the kitchen, Milo jumped onto the table and drank all the milk. A minute later, Anna came '
                  'back and saw the empty bowl! Milo ran quickly under the sofa. Anna laughed because Milo '
                  'was such a naughty cat." (40 words)',
        },
        'listening': {
            'p1': 'Oliver → boy on the bike; Jenny → girl by the pond; Peter → boy in the tree; Sarah → girl on '
                  'the pony; Ben → boy on the bench with the dog.',
            'p2': '1 Saturday, 2 10:30 (half past ten), 3 8, 4 turtle, 5 Bridge',
            'p3': '1 A, 2 H, 3 D, 4 F, 5 G',
            'p4': '1 A, 2 C, 3 C, 4 B, 5 B',
            'p5': '1 Pig pink; 2 "FARM" on barn door; 3 Cat on roof grey; 4 Ball drawn next to duck; '
                  '5 Apples on tree red.',
        },
        'speaking': {
            'Part 1': 'Candidate says e.g. "In my picture the bucket is blue but in your picture it\u2019s red…", '
                      '"In my picture the woman is eating an ice-cream…", "In my picture there are five birds…", '
                      '"In my picture the sandcastle has two flags…" (4 differences).',
            'Part 2': 'Examiner answers: pet shop: Furry Friends / 28 Market Road / rabbits, guinea pigs, birds, '
                      'fish / 7 p.m. / 01 234 5678.',
            'Part 3': 'Accept any clear narrative in past or present tense, e.g. "The parrot flies into Lucy\u2019s '
                      'room. Lucy gives it an apple. Then her neighbour comes and takes the parrot home." '
                      '(use of basic linkers and vocabulary).',
            'Part 4': 'Expect full-sentence personal answers (2\u20133 sentences each); accept any lexical field '
                      'around pets, favourite animals, work, recent experience.',
        },
    },
}


# =====================================================================
# TEST 2 – SCHOOL & LEARNING
# =====================================================================
TEST_2 = {
    'number': 2,
    'theme': 'School & Learning',
    'rw': _rw(
        p1={
            'words': ['a ruler', 'a pencil case', 'a rubber', 'a calculator', 'a dictionary',
                      'a blackboard', 'a timetable', 'a uniform', 'a classroom', 'a playground',
                      'a notebook', 'a chair', 'a scissors', 'a teacher', 'a library'],
            'example': 'a pencil case',
            'defs': [
                'You use this to draw straight lines.',
                'You sit on this inside the classroom.',
                'This is the place where children play during break time.',
                'This person helps children to learn.',
                'You use this to find the meaning of new words.',
                'You wear these special clothes when you go to school.',
                'This shows you which subjects you have each day.',
                'This room in a school has many books to read and borrow.',
                'You can do difficult maths quickly with this.',
                'You use this to rub out mistakes on paper.',
            ],
        },
        p2={
            'speakerA': 'Lara', 'speakerB': 'Dan',
            'line0_a': 'Hi Dan. Did you enjoy your first day at the new school?',
            'line0_b_letter': 'E',
            'line0_b_text': 'Yes, it was really exciting! I met lots of new friends.',
            'pairs': [
                {'a': 'Great. Which is your favourite subject so far?'},
                {'a': 'Really? Who is your maths teacher?'},
                {'a': 'Oh, I know Mrs Perez. She\u2019s very nice. Where\u2019s your classroom?'},
                {'a': 'That\u2019s near mine! What time do your lessons start?'},
                {'a': 'Same as me. Do you have a lot of homework today?'},
                {'a': 'Well, good luck! See you tomorrow at break.'},
            ],
            'options': [
                ('A', 'It\u2019s on the second floor, next to the music room.'),
                ('B', 'At half past eight, the same as before.'),
                ('C', 'Yes, some maths and a short text for English.'),
                ('D', 'Thanks! See you then.'),
                ('E', 'Yes, it was really exciting! I met lots of new friends.'),
                ('F', 'It\u2019s maths – I love numbers.'),
                ('G', 'Her name is Mrs Perez. She is so friendly.'),
                ('H', 'I usually take a ham sandwich.'),
            ],
        },
        p3={
            'words': ['early', 'books', 'teacher', 'break', 'lunch', 'project', 'happy', 'walked'],
            'title': 'Maria\u2019s school day',
            'text': ('Maria is eight years old and she loves going to school. Today she got up very __(1)__ '
                     'because she wanted to finish her science __(2)__ about the planets. '
                     'She __(3)__ to school with her best friend Luna. '
                     'Their first lesson was English and the __(4)__, Mr Stone, read them a funny story. '
                     'At eleven o\u2019clock the children had a __(5)__. Maria ate an apple and played football. '
                     'After that they had maths and then they all went home very __(6)__.'),
            'title_choices': [
                ('A', 'A boring morning'),
                ('B', 'Maria\u2019s school day'),
                ('C', 'The football match'),
            ],
        },
        p4={
            'title': 'School libraries',
            'text': ('Libraries are very important places in every school. In a library, students can __(1)__ '
                     'new books about animals, sports, science or adventure stories. '
                     'In most school libraries, children __(2)__ borrow three books and take them home for two weeks. '
                     'There is usually a librarian who helps the students __(3)__ the right book. '
                     'Libraries are quiet places __(4)__ you should not talk loudly. '
                     'Today, many libraries also __(5)__ computers so children can use the internet for projects. '
                     'Libraries help children love __(6)__ and learn lots of new things.'),
            'items': [
                {'q': '1', 'options': {'A': 'hear', 'B': 'read', 'C': 'listen'}},
                {'q': '2', 'options': {'A': 'can', 'B': 'must', 'C': 'should'}},
                {'q': '3', 'options': {'A': 'find', 'B': 'found', 'C': 'finding'}},
                {'q': '4', 'options': {'A': 'because', 'B': 'so', 'C': 'but'}},
                {'q': '5', 'options': {'A': 'has', 'B': 'have', 'C': 'having'}},
                {'q': '6', 'options': {'A': 'read', 'B': 'reads', 'C': 'reading'}},
            ],
        },
        p5={
            'title': 'The school trip',
            'text': ('Last Friday, class 5B went on a school trip to the Science Museum. '
                     'They took the bus at nine o\u2019clock and arrived at ten. Their teacher, Mrs Brown, '
                     'told them to stay together. First, they visited the dinosaur room. '
                     'Ben\u2019s favourite was a very big dinosaur called Diplodocus, which was 25 metres long. '
                     'Then they went to the space room and Emma drew a rocket in her notebook. '
                     'At twelve o\u2019clock they had lunch in the museum garden. Emma shared her cheese sandwich '
                     'with Ben because he forgot his lunchbox at home. '
                     'After lunch, they watched a short film about the planets. Everyone got a small poster of Mars '
                     'as a present. They returned to school at half past three, very tired but happy.'),
            'example_q': 'Where did class 5B go?',
            'example_a': 'to the Science Museum',
            'questions': [
                'What time did they arrive at the museum?',
                'Who is their teacher?',
                'Which room did they visit first?',
                'How long is the Diplodocus?',
                'Why did Emma share her sandwich?',
                'What was the film about?',
                'What present did everyone get?',
            ],
        },
        p6={
            'title': 'My favourite lesson',
            'text': ('My favourite lesson at school __(ex)__ art. On Thursday afternoons, we always have art '
                     'with Miss Cook. She is very funny __(1)__ she teaches us lots of things. '
                     'Last week, __(2)__ painted pictures of our pets. I painted my dog Toby. Miss Cook said '
                     'my picture __(3)__ very good. Sometimes, we also make models with paper and glue. '
                     'I never get bored in Miss Cook\u2019s class __(4)__ it is always different. '
                     'After art, I usually __(5)__ home with my friend Elena and we talk about what '
                     '__(6)__ did in class.'),
            'example': 'is',
            'answers': ['and', 'we', 'was', 'because', 'walk/go', 'we'],
        },
        p7={
            'title': 'The missing pencil case',
            'p1': 'A boy can\u2019t find his pencil case in his school bag.',
            'p2': 'He looks everywhere in the classroom – under the desks and on the shelves.',
            'p3': 'The teacher finds the pencil case on the floor in the playground.',
        },
    ),
    'listening': _listening(
        p1={
            'scene': 'A school playground at break time with children doing different things: a girl reading a '
                     'book on a bench, a boy with a skipping rope, two girls playing basketball, a boy eating '
                     'an apple, a girl drawing on paper, a boy with a football.',
            'example_name': 'Mark',
            'names': ['Hannah', 'Fred', 'Paula', 'Jim', 'Lisa'],
        },
        p2={
            'heading': 'Summer Camp – English lessons',
            'example_label': 'Name of camp',
            'example': 'Sunnydale',
            'labels': [
                'First day: date (month, day)',
                'Number of students in each class',
                'Price per week (£)',
                'Teacher\u2019s last name',
                'Book to bring: colour',
            ],
        },
        p3={
            'instruction': 'Paul is telling his mother which subject he has each day next week.',
            'example_item': 'Monday', 'example_letter': 'E',
            'items': ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday (extra club)'],
            'options': [
                ('A', 'history'), ('B', 'music'), ('C', 'maths'), ('D', 'PE / sports'),
                ('E', 'English'), ('F', 'science'), ('G', 'art'), ('H', 'geography'),
            ],
        },
        p4={
            'items': [
                {'q': 'What did Mia forget to bring to school today?',
                 'A': 'her ruler', 'B': 'her pencil case', 'C': 'her lunch'},
                {'q': 'What is the teacher wearing?',
                 'A': 'a green jumper', 'B': 'a white shirt and a black skirt', 'C': 'a blue dress'},
                {'q': 'Where is the book?',
                 'A': 'on the chair', 'B': 'in the bag', 'C': 'on the shelf'},
                {'q': 'What subject does Ben like best?',
                 'A': 'maths', 'B': 'English', 'C': 'science'},
                {'q': 'What did the children do in PE today?',
                 'A': 'ran around the field', 'B': 'played basketball', 'C': 'did swimming'},
            ],
        },
        p5={
            'scene': 'A classroom with: a blackboard, a teacher\u2019s desk, three student desks, a window with '
                     'a plant, a clock above the door, a map of the world on the wall, a bookshelf in the corner.',
            'example': 'Colour the clock yellow.',
            'items': [
                'Colour the plant in the window green.',
                'Draw a book on the teacher\u2019s desk.',
                'Colour the map blue.',
                'Write the number 5B on the door.',
                'Colour the biggest book on the shelf red.',
            ],
        },
    ),
    'speaking': {
        'p1_ex': 'A classroom: a boy writing with a pencil, a girl with a red school bag, a clock showing 10:00, '
                 'a teacher at the board writing "maths", a window showing the sun, three books on a shelf.',
        'p1_cand': 'A classroom: a boy writing with a PEN, a girl with a BLUE school bag, a clock showing 10:00, '
                   'a teacher at the board writing "SCIENCE", a window showing the sun, FIVE books on a shelf.',
        'p1_diffs': [
            'Pencil vs pen.',
            'Red bag vs blue bag.',
            'Maths on the board vs science.',
            'Three books vs five books.',
        ],
        'p2_topic': 'Two schools',
        'p2_cand_card': 'SCHOOL: Oakwood Primary – Number of classrooms: ______ – Subjects: ______ – '
                        'Sports: football and ______ – Head teacher: Mr ______ – Break time at ______.',
        'p2_cand_qs': [
            'What\u2019s the name of your school?',
            'How many students go there?',
            'When is the school open? / What time does it finish?',
            'What sports do children do?',
            'What is the uniform like?',
        ],
        'p2_ex_card': 'SCHOOL: Riverside School – 240 students – Open 8:30 to 3:30 – '
                      'Sports: football, tennis, swimming – Uniform: white shirt, grey trousers, red tie.',
        'p2_ex_qs': [
            'What\u2019s your school\u2019s name?',
            'How many classrooms are there?',
            'Which subjects can students study?',
            'What time is the break?',
            'Who is the head teacher?',
        ],
        'p3_title': 'The science experiment',
        'p3_p1': 'Two children put some water in a small plant pot with a seed.',
        'p3_p2': 'They put the pot next to a sunny window.',
        'p3_p3': 'One week later, a little green plant grows in the pot.',
        'p3_p4': 'The children show the plant proudly to their teacher, who smiles.',
        'p3_examiner_open': 'Look at these pictures. They tell a story called "The science experiment". Two children are in the classroom and they are putting some water on a seed in a small pot. Now you tell the rest of the story.',
        'p4_questions': [
            'What\u2019s your favourite subject? Why?',
            'Tell me about your best friend at school.',
            'How do you go to school every day?',
            'What do you usually do after school?',
            'Do you prefer maths or English? Why?',
        ],
    },
    'scripts': {
        'p1': ('Look at the picture. Lots of children are in the playground. Can you see Mark? Mark is the boy with '
               'the football. The line goes from Mark to the boy with the football – that\u2019s the example. Now listen.\n'
               '1. Can you find Hannah? Hannah is reading a book on the bench.\n'
               '2. Where\u2019s Fred? Fred is the boy eating an apple.\n'
               '3. Now Paula. Paula is the girl drawing on paper.\n'
               '4. Where\u2019s Jim? Jim is the boy with the skipping rope.\n'
               '5. And Lisa? Lisa is one of the girls playing basketball – the taller one.'),
        'p2': ('Listen to a woman telling a father about an English summer camp. The example is: the camp is called '
               'Sunnydale. Now listen and write.\n'
               '— What\u2019s the first day, please?\n— The camp starts on July 4th.\n'
               '— How many students are there in each class?\n— We only have 12 students per class.\n'
               '— And how much is it per week?\n— It\u2019s 95 pounds a week.\n'
               '— Who\u2019s the main teacher?\n— Her name is Miss Adams.\n'
               '— Shall we bring a notebook?\n— Yes, please bring a green notebook.'),
        'p3': ('Paul is showing his mum his new school timetable. Example: on Monday he has English. Now listen.\n'
               '— What about Tuesday, Paul?\n— Tuesday mornings I have maths, Mum.\n'
               '— And Wednesday?\n— Wednesday\u2019s my favourite – we have PE.\n'
               '— OK. Thursday?\n— Thursday, we always have science.\n'
               '— And on Friday?\n— Friday\u2019s a good day – we have music!\n'
               '— What about the Saturday club?\n— The extra club on Saturday is art.'),
        'p4': ('1. What did Mia forget? — I didn\u2019t forget my ruler or my lunch – I have them. But I left my '
               'pencil case on the kitchen table!\n'
               '2. What\u2019s the teacher wearing? — Not a jumper or a dress. She\u2019s wearing a white shirt '
               'and a long black skirt.\n'
               '3. Where is the book? — I looked on the chair and in my bag. Oh! It\u2019s here on the shelf.\n'
               '4. Ben, what do you like best? — Maths is OK. English is nice but I love science. Science is '
               'definitely my favourite.\n'
               '5. What did you do in PE? — No running today. We didn\u2019t go swimming. We played basketball '
               'all lesson.'),
        'p5': ('This is a classroom. Example: colour the clock yellow. Do you see it? Good. Now listen and colour.\n'
               '1. There\u2019s a plant in the window. Colour the plant green.\n'
               '2. On the teacher\u2019s desk, draw a book.\n'
               '3. There\u2019s a map of the world on the wall. Colour it blue.\n'
               '4. Now write 5B on the classroom door.\n'
               '5. On the shelf there are three books. Colour the biggest book red.'),
    },
    'answers': {
        'rw': {
            'p1': '1 a ruler, 2 a chair, 3 a playground, 4 a teacher, 5 a dictionary, 6 a uniform, '
                  '7 a timetable, 8 a library, 9 a calculator, 10 a rubber',
            'p2': '1 F, 2 G, 3 A, 4 B, 5 C, 6 D',
            'p3': '1 early, 2 project, 3 walked, 4 teacher, 5 break, 6 happy — Best title: B',
            'p4': '1 B (read), 2 A (can), 3 A (find), 4 B (so), 5 B (have), 6 C (reading)',
            'p5': '1 at ten (10 o\u2019clock), 2 Mrs Brown, 3 the dinosaur room, 4 25 metres, '
                  '5 Ben forgot his lunchbox, 6 the planets, 7 a (small) poster of Mars',
            'p6': '(ex) is — 1 and, 2 we, 3 was, 4 because, 5 walk (or go), 6 we',
            'p7': 'Sample: "Yesterday at school, Jake couldn\u2019t find his pencil case. He looked in his bag, '
                  'under the desks and on all the shelves. He was very sad! Then the teacher, Miss Hill, '
                  'came into the classroom with his pencil case. She found it in the playground. Jake said '
                  '"Thank you!" and smiled." (55 words)',
        },
        'listening': {
            'p1': 'Hannah → girl reading on bench; Fred → boy eating apple; Paula → girl drawing on paper; '
                  'Jim → boy with skipping rope; Lisa → taller girl playing basketball.',
            'p2': '1 July 4 (4th July), 2 12, 3 95, 4 Adams, 5 green',
            'p3': '1 C, 2 D, 3 F, 4 B, 5 G',
            'p4': '1 B, 2 B, 3 C, 4 C, 5 B',
            'p5': '1 Plant green; 2 Book drawn on teacher\u2019s desk; 3 Map blue; 4 "5B" on door; '
                  '5 Biggest book on shelf red.',
        },
        'speaking': {
            'Part 1': 'Candidate finds: pencil/pen, red/blue bag, maths/science on board, 3/5 books.',
            'Part 2': 'Examiner\u2019s info: Riverside School, 240 students, 8:30–3:30, football/tennis/swimming, '
                      'uniform white shirt, grey trousers, red tie.',
            'Part 3': 'Accept e.g. "They put the pot by the window. After one week a plant grew. The children '
                      'show it to the teacher and she is happy."',
            'Part 4': 'Expect: favourite subject + reason; friend description; transport; afternoon activities; '
                      'preference with justification.',
        },
    },
}


# =====================================================================
# TEST 3 – FOOD & DRINK
# =====================================================================
TEST_3 = {
    'number': 3,
    'theme': 'Food & Drink',
    'rw': _rw(
        p1={
            'words': ['a melon', 'a strawberry', 'a mushroom', 'a pineapple', 'a potato',
                      'a cucumber', 'a pepper', 'a lemon', 'a pear', 'a coconut',
                      'a carrot', 'an onion', 'a tomato', 'a mango', 'a grape'],
            'example': 'a strawberry',
            'defs': [
                'This vegetable is orange and long. Rabbits love it.',
                'This vegetable makes you cry when you cut it.',
                'This fruit is yellow and sour, and it grows on trees.',
                'It is long, green and you often put it in salads.',
                'This vegetable is brown outside and white inside. People make chips with it.',
                'It is a small sweet fruit that grows in bunches, green or purple.',
                'This fruit is big, round or oval, and very sweet inside. It is a summer fruit.',
                'It is a round red fruit that you often put on pizzas.',
                'This fruit has hard brown hair outside and white sweet food inside, with milk inside too.',
                'This big yellow fruit from hot countries has sharp leaves on top.',
            ],
        },
        p2={
            'speakerA': 'Eva', 'speakerB': 'Chef',
            'line0_a': 'Hello! I\u2019d like to order some lunch, please.',
            'line0_b_letter': 'F',
            'line0_b_text': 'Of course. What would you like to eat today?',
            'pairs': [
                {'a': 'I\u2019d like the tomato soup to start, please.'},
                {'a': 'And for my main, can I have the chicken with rice?'},
                {'a': 'Is the soup very hot?'},
                {'a': 'OK. Do you have any fresh fruit for dessert?'},
                {'a': 'Perfect. And can I drink some orange juice, please?'},
                {'a': 'Thank you. How long will the food be?'},
            ],
            'options': [
                ('A', 'Yes, we have strawberries or a fruit salad today.'),
                ('B', 'About fifteen minutes – is that OK?'),
                ('C', 'Sure. Small, medium or large glass?'),
                ('D', 'Yes, but we can put some ice if you prefer.'),
                ('E', 'Certainly. Would you like potatoes with it instead?'),
                ('F', 'Of course. What would you like to eat today?'),
                ('G', 'Excellent choice – the chef makes it today with fresh tomatoes.'),
                ('H', 'We don\u2019t have chicken. We have fish instead.'),
            ],
        },
        p3={
            'words': ['vegetables', 'cooking', 'sugar', 'kitchen', 'happy', 'tasty', 'family', 'bought'],
            'title': 'Daniel\u2019s birthday cake',
            'text': ('Yesterday was Daniel\u2019s ninth birthday. His dad is very good at __(1)__ and he made '
                     'Daniel a special chocolate cake. First, they went to the supermarket and __(2)__ lots '
                     'of ingredients, like eggs, flour and __(3)__. At home, they worked together in the __(4)__ '
                     'for two hours. The cake was very big and __(5)__! In the evening, all the __(6)__ came '
                     'to sing and eat the cake. Daniel had a wonderful birthday.'),
            'title_choices': [
                ('A', 'A trip to the farm'),
                ('B', 'Daniel\u2019s birthday cake'),
                ('C', 'My favourite restaurant'),
            ],
        },
        p4={
            'title': 'Breakfast around the world',
            'text': ('Breakfast is different in many parts of the world. In the United Kingdom, some people __(1)__ '
                     'eggs with bacon and beans for breakfast. In Japan, children often have rice and soup __(2)__ '
                     'they go to school. People in Spain like to __(3)__ a hot chocolate with sweet bread called '
                     'churros. In the morning, families in Turkey eat cheese, olives, bread __(4)__ tomatoes. '
                     'Breakfast in many African countries __(5)__ porridge from corn or other grains. '
                     'Every country is different but a good breakfast gives you __(6)__ to start your day!'),
            'items': [
                {'q': '1', 'options': {'A': 'eats', 'B': 'eat', 'C': 'eating'}},
                {'q': '2', 'options': {'A': 'before', 'B': 'after', 'C': 'until'}},
                {'q': '3', 'options': {'A': 'drink', 'B': 'eat', 'C': 'bring'}},
                {'q': '4', 'options': {'A': 'or', 'B': 'and', 'C': 'but'}},
                {'q': '5', 'options': {'A': 'are', 'B': 'is', 'C': 'be'}},
                {'q': '6', 'options': {'A': 'energy', 'B': 'school', 'C': 'book'}},
            ],
        },
        p5={
            'title': 'The picnic disaster',
            'text': ('Last Sunday, my family went on a picnic by the lake. My mum made lots of sandwiches and '
                     'my dad brought apples, crisps and a big bottle of lemonade. My little sister Holly brought '
                     'her favourite chocolate biscuits. We sat under a big tree and started to eat. '
                     'Suddenly, a very hungry duck came out of the water. It was huge and it wanted our food! '
                     'The duck took a whole sandwich from my brother and ran away. We all laughed a lot. '
                     'Then a second problem started: it began to rain! We quickly put everything in our bags '
                     'and ran to the car. In the car, we drank the lemonade and ate the chocolate biscuits. '
                     'It wasn\u2019t the picnic we wanted, but everyone was really happy.'),
            'example_q': 'Where did they go on a picnic?',
            'example_a': 'by the lake',
            'questions': [
                'Who made the sandwiches?',
                'What did Dad bring to drink?',
                'What did Holly bring?',
                'Where did they sit?',
                'Which animal took their food?',
                'Why did they run to the car?',
                'What did they eat in the car?',
            ],
        },
        p6={
            'title': 'Our class cooking day',
            'text': ('Last Friday __(ex)__ class went to a kitchen and we cooked pizzas. The teacher, Mr Rossi, '
                     'gave us flour, water and salt. __(1)__ hands were very dirty! First, we made a ball '
                     'with the dough. __(2)__ we put tomato sauce on top. I put lots of cheese on __(3)__ pizza. '
                     'My friend Mia put mushrooms and onions __(4)__ hers. When the pizzas were ready, '
                     'we ate them __(5)__ our classmates. They were delicious! I want to learn to __(6)__ '
                     'more things at home.'),
            'example': 'my',
            'answers': ['Our', 'Then', 'my', 'on', 'with', 'cook'],
        },
        p7={
            'title': 'The big ice cream',
            'p1': 'A boy buys a very big ice cream at an ice cream shop.',
            'p2': 'He is walking and a dog jumps up and eats his ice cream.',
            'p3': 'The boy cries but his mum buys him a new small ice cream.',
        },
    ),
    'listening': _listening(
        p1={
            'scene': 'A busy café with people at different tables: a man reading a newspaper and drinking tea, '
                     'a boy eating a chocolate cake, a woman with a coffee, a girl drinking orange juice, '
                     'a man having spaghetti, a woman with a baby and a banana, a waiter carrying a tray.',
            'example_name': 'Harry',
            'names': ['Mandy', 'Tom', 'Kate', 'Rosa', 'Alex'],
        },
        p2={
            'heading': 'Restaurant booking – telephone call',
            'example_label': 'Customer\u2019s name',
            'example': 'Mr Parker',
            'labels': [
                'Day and month',
                'Time (evening)',
                'Number of people',
                'Special food (one child cannot eat)',
                'Table by the ______ (window / door)',
            ],
        },
        p3={
            'instruction': 'Ben is telling his grandma what he cooks on different days.',
            'example_item': 'Sunday', 'example_letter': 'B',
            'items': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
            'options': [
                ('A', 'pasta'), ('B', 'rice'), ('C', 'soup'), ('D', 'salad'),
                ('E', 'pizza'), ('F', 'burgers'), ('G', 'fish'), ('H', 'pancakes'),
            ],
        },
        p4={
            'items': [
                {'q': 'What does the boy want for lunch?',
                 'A': 'a cheese sandwich', 'B': 'a chicken salad', 'C': 'a bowl of soup'},
                {'q': 'Where is the cake?',
                 'A': 'in the fridge', 'B': 'on the table', 'C': 'in the cupboard'},
                {'q': 'What did the family eat at the restaurant?',
                 'A': 'pizza', 'B': 'pasta', 'C': 'burgers'},
                {'q': 'What is the girl drinking?',
                 'A': 'water', 'B': 'milk', 'C': 'juice'},
                {'q': 'What fruit did Mum buy?',
                 'A': 'pears', 'B': 'grapes', 'C': 'pineapples'},
            ],
        },
        p5={
            'scene': 'A kitchen: a fridge on the left, a table in the centre with a bowl of fruit, '
                     'a cat under the table, a small shelf with three jars, a cupboard with plates, '
                     'a window with curtains.',
            'example': 'Colour the fridge blue.',
            'items': [
                'Colour the smallest jar on the shelf yellow.',
                'Draw a glass of milk on the table.',
                'Colour the cat under the table black.',
                'Write the word SUGAR on the biggest jar.',
                'Colour the curtains red.',
            ],
        },
    ),
    'speaking': {
        'p1_ex': 'A kitchen: a cook wearing a white hat, four eggs on the table, a blue apron, a small cat, '
                 'a window with the sun, two tomatoes on a plate.',
        'p1_cand': 'A kitchen: a cook wearing a BLACK hat, SIX eggs on the table, a blue apron, a small DOG, '
                   'a window with the sun, FOUR tomatoes on a plate.',
        'p1_diffs': [
            'White hat vs black hat.',
            'Four eggs vs six eggs.',
            'Cat vs dog.',
            'Two tomatoes vs four tomatoes.',
        ],
        'p2_topic': 'Two cafés',
        'p2_cand_card': 'CAFÉ: Yummy Corner – Open: 8 a.m. – Closes: ______ – Best cake: ______ – '
                        'Drink of the day: ______ – Near the ______ – Friday: special ______ menu.',
        'p2_cand_qs': [
            'What is the name of your café?',
            'When does it open?',
            'What food can you eat there?',
            'How much is a juice?',
            'Can you sit outside?',
        ],
        'p2_ex_card': 'CAFÉ: The Green Leaf – Open 9 a.m. to 6 p.m. – Best food: vegetable soup – '
                      'Juice: 2.50 – Near the park – Yes, big garden outside.',
        'p2_ex_qs': [
            'What\u2019s the café called?',
            'What time does it close?',
            'What is the best cake?',
            'What\u2019s the drink of the day?',
            'Where is it?',
        ],
        'p3_title': 'A cake for Granny',
        'p3_p1': 'Two children are making a cake in the kitchen.',
        'p3_p2': 'They put the cake in the oven.',
        'p3_p3': 'They take out the cake – it looks perfect!',
        'p3_p4': 'Granny arrives and eats a piece with them, smiling.',
        'p3_examiner_open': 'These pictures tell a story called "A cake for Granny". Two children are in the kitchen – they are making a cake. Now you tell the rest of the story.',
        'p4_questions': [
            'What\u2019s your favourite food? Why?',
            'Do you help at home in the kitchen?',
            'Tell me about your lunch yesterday.',
            'Do you prefer fruit or cake? Why?',
            'What do you usually drink for breakfast?',
        ],
    },
    'scripts': {
        'p1': ('Look at the picture – people in a café. Harry is the man reading the newspaper and drinking tea. '
               'Do you see the line from Harry to that man? That\u2019s the example.\n'
               '1. Can you see Mandy? Mandy is the woman with the baby holding a banana.\n'
               '2. Where\u2019s Tom? Tom is the boy eating the chocolate cake.\n'
               '3. Now Kate. Kate is the woman drinking a coffee.\n'
               '4. Where is Rosa? Rosa is the girl with orange juice.\n'
               '5. And Alex? Alex is the man eating spaghetti.'),
        'p2': ('Listen, a man is booking a table at a restaurant. Example: his name is Mr Parker. Now listen and write.\n'
               '— When would you like to come?\n— On the 17th of May, please.\n'
               '— What time?\n— At eight o\u2019clock in the evening.\n'
               '— How many people?\n— There will be five of us.\n'
               '— Any special food?\n— Yes, one of the children can\u2019t eat peanuts. Please, no peanuts.\n'
               '— Where would you like to sit?\n— A table by the window would be lovely.'),
        'p3': ('Ben is telling his grandma what he cooks each day. Example: on Sunday he cooks rice.\n'
               '— Monday, grandma, I make my favourite – burgers!\n'
               '— Tuesday I try a new pasta dish with tomato sauce.\n'
               '— Wednesday is easy: a big salad with lettuce and tomatoes.\n'
               '— Thursday we had pancakes for breakfast and dinner – yum!\n'
               '— On Friday, Dad and I made homemade pizza – delicious!'),
        'p4': ('1. — What do you want for lunch, Jack? — A cheese sandwich? No. A chicken salad? No, I\u2019m cold. '
               'Can I have a bowl of soup, please?\n'
               '2. — Where\u2019s the cake? — Not in the fridge. Not on the table. I put it in the cupboard '
               'last night.\n'
               '3. — What did you eat at the restaurant? — We wanted pizza but the menu was different. We didn\u2019t '
               'have burgers. We ate lovely pasta.\n'
               '4. — What are you drinking, Emma? — Not water. Not juice. It\u2019s a glass of milk. I love milk.\n'
               '5. — What fruit did Mum buy? — Not pears, they were expensive. Not pineapples. She bought some '
               'beautiful red grapes.'),
        'p5': ('This is a kitchen. Example: colour the fridge blue.\n'
               '1. There are three jars on the shelf. Colour the smallest one yellow.\n'
               '2. On the table, draw a glass of milk.\n'
               '3. Can you see the cat under the table? Colour the cat black.\n'
               '4. Now write SUGAR on the biggest jar.\n'
               '5. The curtains – colour the curtains red.'),
    },
    'answers': {
        'rw': {
            'p1': '1 a carrot, 2 an onion, 3 a lemon, 4 a cucumber, 5 a potato, 6 a grape, 7 a melon, '
                  '8 a tomato, 9 a coconut, 10 a pineapple',
            'p2': '1 G, 2 E, 3 D, 4 A, 5 C, 6 B',
            'p3': '1 cooking, 2 bought, 3 sugar, 4 kitchen, 5 tasty, 6 family — Best title: B',
            'p4': '1 B (eat), 2 A (before), 3 A (drink), 4 B (and), 5 B (is), 6 A (energy)',
            'p5': '1 (my) mum, 2 (a big bottle of) lemonade, 3 (her favourite) chocolate biscuits, '
                  '4 under a (big) tree, 5 a (hungry) duck, 6 (because) it began to rain, '
                  '7 lemonade and chocolate biscuits',
            'p6': '(ex) my — 1 Our, 2 Then, 3 my, 4 on, 5 with, 6 cook',
            'p7': 'Sample: "Harry went to buy a very big ice cream. It had three colours and looked amazing! '
                  'He walked home, but a big dog jumped up and ate all his ice cream! Harry started to cry. '
                  'His mum was near and she bought him another small ice cream. Harry was happy again." (55 words)',
        },
        'listening': {
            'p1': 'Mandy → woman with baby/banana; Tom → boy with chocolate cake; Kate → woman with coffee; '
                  'Rosa → girl with orange juice; Alex → man with spaghetti.',
            'p2': '1 17th May (17/5), 2 8 p.m. (eight), 3 5, 4 peanuts, 5 window',
            'p3': '1 F, 2 A, 3 D, 4 H, 5 E',
            'p4': '1 C, 2 C, 3 B, 4 B, 5 B',
            'p5': '1 Smallest jar yellow; 2 Glass of milk on table; 3 Cat black; 4 SUGAR on biggest jar; '
                  '5 Curtains red.',
        },
        'speaking': {
            'Part 1': 'Differences: white/black hat; 4/6 eggs; cat/dog; 2/4 tomatoes.',
            'Part 2': 'Examiner card: The Green Leaf, 9 a.m.–6 p.m., vegetable soup, juice £2.50, near the park, '
                      'garden outside.',
            'Part 3': 'Acceptable: "They put the cake in the oven. Then they take the cake out. Finally, '
                      'Granny eats a piece."',
            'Part 4': 'Expect personal, full-sentence answers with reasons; use of comparatives ("I prefer …").',
        },
    },
}


# =====================================================================
# TEST 4 – FAMILY & HOME
# =====================================================================
TEST_4 = {
    'number': 4,
    'theme': 'Family & Home',
    'rw': _rw(
        p1={
            'words': ['a bathroom', 'a kitchen', 'a garage', 'a balcony', 'a garden',
                      'a fridge', 'a sofa', 'a cushion', 'a mirror', 'a cupboard',
                      'a shower', 'a carpet', 'a blanket', 'a lamp', 'a wardrobe'],
            'example': 'a sofa',
            'defs': [
                'You keep your food cold in this.',
                'This is the room where people cook food.',
                'You look in this to see your face.',
                'You have a wash or clean your teeth in this room.',
                'You put your clothes inside this in your bedroom.',
                'You use this to see things better at night. It has a light.',
                'Small bag of soft things you put on the sofa to be comfortable.',
                'You put your car in here at home.',
                'This covers your floor – it is often soft.',
                'This is a place outside your house with flowers and grass.',
            ],
        },
        p2={
            'speakerA': 'Alice', 'speakerB': 'Dad',
            'line0_a': 'Dad, can you help me tidy my bedroom, please?',
            'line0_b_letter': 'C',
            'line0_b_text': 'Of course, love. Where would you like to start?',
            'pairs': [
                {'a': 'Let\u2019s start with the clothes on the floor.'},
                {'a': 'OK. Can you pass me the hangers, please?'},
                {'a': 'Thanks! What about all these books?'},
                {'a': 'Good idea. And my toys?'},
                {'a': 'Perfect. Can I keep the teddy on my bed?'},
                {'a': 'Thanks, Dad. Now the room looks great!'},
            ],
            'options': [
                ('A', 'Sure, the shelves in the wardrobe are empty.'),
                ('B', 'Put them in the blue box under the window.'),
                ('C', 'Of course, love. Where would you like to start?'),
                ('D', 'I think they go in the wardrobe now.'),
                ('E', 'Yes, of course. He can stay on the pillow.'),
                ('F', 'I\u2019m really happy with you – well done!'),
                ('G', 'Here you are. How many do you need?'),
                ('H', 'No, put them in the bathroom.'),
            ],
        },
        p3={
            'words': ['living', 'sister', 'pictures', 'friendly', 'house', 'small', 'kitchen', 'built'],
            'title': 'My new house',
            'text': ('Last month my family moved to a new __(1)__ in a quiet street. It has three bedrooms, '
                     'a big __(2)__ with a round table and a nice garden. My favourite room is the __(3)__ '
                     'room because there is a big window and a soft sofa. '
                     'I share a bedroom with my little __(4)__, but we have fun together. '
                     'On the walls we put some __(5)__ of our old home. The neighbours are very __(6)__ '
                     'and the little dog next door always says hello.'),
            'title_choices': [
                ('A', 'A camping weekend'),
                ('B', 'My new house'),
                ('C', 'A noisy party'),
            ],
        },
        p4={
            'title': 'Grandparents\u2019 houses',
            'text': ('Many grandparents live in houses that are different __(1)__ our own. '
                     'Often, their houses have a lot of photos on the walls and interesting objects in every room. '
                     'My grandma\u2019s kitchen is __(2)__ but always warm, and there is a nice smell of cakes. '
                     'Some grandparents live in a small house with a garden __(3)__ they can grow vegetables. '
                     'Others live in a flat in town and go to the park every day. Children __(4)__ visiting '
                     'their grandparents because they tell funny stories __(5)__ the past. '
                     'When I visit my grandparents, I always want to __(6)__ for dinner.'),
            'items': [
                {'q': '1', 'options': {'A': 'of', 'B': 'from', 'C': 'than'}},
                {'q': '2', 'options': {'A': 'old', 'B': 'new', 'C': 'easy'}},
                {'q': '3', 'options': {'A': 'where', 'B': 'when', 'C': 'which'}},
                {'q': '4', 'options': {'A': 'love', 'B': 'loves', 'C': 'loved'}},
                {'q': '5', 'options': {'A': 'on', 'B': 'about', 'C': 'for'}},
                {'q': '6', 'options': {'A': 'stay', 'B': 'stayed', 'C': 'staying'}},
            ],
        },
        p5={
            'title': 'A busy Saturday',
            'text': ('Every Saturday morning, my family wakes up early. Mum starts making pancakes and Dad makes '
                     'tea for everyone. My baby brother Jamie usually wakes up first, at about 7:30. '
                     'After breakfast, we all help to clean the house. I always tidy the living room and my sister '
                     'Ellie cleans our bedroom. Mum does the washing and Dad cleans the bathroom. '
                     'At 11 o\u2019clock, we stop and have some fruit juice. Last Saturday, Jamie made a huge '
                     'mess in the kitchen with his cereal! Mum wasn\u2019t angry, she just laughed. '
                     'After lunch, we went to the park with our dog, Rocky. Rocky ran for two hours and '
                     'then slept for the rest of the day. In the evening, we all watched a film together '
                     'with some popcorn. It was the best day of my week.'),
            'example_q': 'Who wakes up first?',
            'example_a': 'Jamie (baby brother)',
            'questions': [
                'What does Mum make for breakfast?',
                'Who tidies the living room?',
                'What does Dad clean?',
                'At what time does the family have fruit juice?',
                'What did Jamie make a mess with?',
                'What is the name of the family\u2019s dog?',
                'What did they do in the evening?',
            ],
        },
        p6={
            'title': 'My cousin\u2019s flat',
            'text': ('My cousin Oscar lives in a beautiful flat in the city. The flat __(ex)__ on the fifth floor '
                     'and it has a lovely balcony. From __(1)__ balcony, you can see the whole city. '
                     'Oscar\u2019s bedroom is __(2)__ big as mine. He has a little white dog called Milo who '
                     'always sleeps __(3)__ the sofa. On weekends, I sometimes go to visit Oscar __(4)__ '
                     'we play video games. His mum, my aunt, is very kind and makes __(5)__ the best biscuits '
                     'in the world. When it is late, my dad comes to pick me __(6)__ in the car.'),
            'example': 'is',
            'answers': ['the/his', 'as', 'on', 'and', 'us', 'up'],
        },
        p7={
            'title': 'The noisy neighbours',
            'p1': 'A boy is sleeping in his bedroom at night.',
            'p2': 'The neighbours make a lot of noise with loud music – the boy covers his ears.',
            'p3': 'The next morning the boy\u2019s dad talks to the neighbours and everyone smiles.',
        },
    ),
    'listening': _listening(
        p1={
            'scene': 'A family party in a living room: grandpa in an armchair reading a card, a girl giving a '
                     'present to her mother, a man playing the guitar, a boy with a balloon, a woman with '
                     'a camera, a toddler eating cake on the floor, a teenage girl taking photos on a phone.',
            'example_name': 'Grandpa Roy',
            'names': ['Uncle Ben', 'Aunt Mary', 'Cousin Jake', 'Emma', 'Grandma Sue'],
        },
        p2={
            'heading': 'Party at Sarah\u2019s house',
            'example_label': 'Party for (person\u2019s name)',
            'example': 'Sarah',
            'labels': [
                'Day and month',
                'Starting time',
                'Number of guests',
                'Sarah\u2019s favourite cake',
                'Address: number of the house',
            ],
        },
        p3={
            'instruction': 'Lily is telling her friend which family member she visited each day last week.',
            'example_item': 'Monday', 'example_letter': 'D',
            'items': ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
            'options': [
                ('A', 'uncle'), ('B', 'grandma'), ('C', 'aunt'), ('D', 'cousin Mark'),
                ('E', 'big brother'), ('F', 'grandpa'), ('G', 'little sister'),
                ('H', 'cousin Amy'),
            ],
        },
        p4={
            'items': [
                {'q': 'Where is Mum now?',
                 'A': 'in the kitchen', 'B': 'in the garden', 'C': 'in the bathroom'},
                {'q': 'What colour is the new sofa?',
                 'A': 'green', 'B': 'brown', 'C': 'grey'},
                {'q': 'How many brothers does Jack have?',
                 'A': 'one', 'B': 'two', 'C': 'three'},
                {'q': 'Who is the boy on the phone?',
                 'A': 'his father', 'B': 'his grandpa', 'C': 'his teacher'},
                {'q': 'Where is the cat hiding?',
                 'A': 'under the bed', 'B': 'on the wardrobe', 'C': 'behind the curtains'},
            ],
        },
        p5={
            'scene': 'A family living room: a big sofa, a TV on a small table, a lamp in the corner, '
                     'a round rug on the floor, a picture of a mountain on the wall, a toy box, a cat.',
            'example': 'Colour the TV black.',
            'items': [
                'Colour the sofa orange.',
                'Draw a book on the small table next to the TV.',
                'Colour the rug yellow.',
                'Write the word HOME above the picture.',
                'Colour the cat next to the toy box grey.',
            ],
        },
    ),
    'speaking': {
        'p1_ex': 'A living room: a woman reading a book on the sofa, a boy playing with a train, a dog '
                 'on the carpet, a green plant by the window, one clock, a yellow lamp on the table.',
        'p1_cand': 'A living room: a woman reading a NEWSPAPER on the sofa, a boy playing with a TRUCK, '
                   'a CAT on the carpet, a green plant by the window, TWO clocks, a yellow lamp on the table.',
        'p1_diffs': [
            'Book vs newspaper.',
            'Train vs truck.',
            'Dog vs cat.',
            'One clock vs two clocks.',
        ],
        'p2_topic': 'Two families',
        'p2_cand_card': 'FAMILY: Mike\u2019s family – Father\u2019s job: ______ – Mother\u2019s job: ______ – '
                        'Children: Mike, ______ and ______ – Pet: ______ – House: in the ______.',
        'p2_cand_qs': [
            'What\u2019s the father\u2019s name?',
            'Where does the family live?',
            'How many brothers or sisters?',
            'Do they have a pet? What is it?',
            'What is the mother\u2019s job?',
        ],
        'p2_ex_card': 'FAMILY: The Parker family – Father David (doctor) – Mother Rachel (teacher) – '
                      'Children: Lisa, Tom and baby Anna – Pet: a cat – House: in the countryside.',
        'p2_ex_qs': [
            'What\u2019s the family\u2019s name?',
            'What does the father do?',
            'What is the mother\u2019s job?',
            'How many children are in the family?',
            'Where is their house?',
        ],
        'p3_title': 'A surprise for Mum',
        'p3_p1': 'Two children wake up early on Mother\u2019s Day.',
        'p3_p2': 'They make breakfast: tea, toast and flowers on a tray.',
        'p3_p3': 'They take the tray to Mum\u2019s bedroom.',
        'p3_p4': 'Mum is surprised and gives her children a big hug.',
        'p3_examiner_open': 'These pictures tell a story called "A surprise for Mum". Two children wake up early – it\u2019s Mother\u2019s Day. Now you tell the rest of the story.',
        'p4_questions': [
            'Tell me about the people in your family.',
            'Do you have a favourite room in your house? Why?',
            'What do you do with your family on weekends?',
            'What\u2019s your bedroom like?',
            'Do you help at home? What do you do?',
        ],
    },
    'scripts': {
        'p1': ('Look at the family party. Grandpa Roy is the man in the armchair reading a card – that\u2019s the '
               'example.\n'
               '1. Can you see Uncle Ben? He\u2019s the man playing the guitar.\n'
               '2. Aunt Mary? She\u2019s the woman with the camera.\n'
               '3. Cousin Jake? He\u2019s the boy with the balloon.\n'
               '4. Where\u2019s Emma? Emma is the teenage girl taking photos on a phone.\n'
               '5. And Grandma Sue? She\u2019s the toddler – no, wait – she\u2019s giving a present to her daughter.\n'
               '     Actually Grandma Sue is the woman giving the present.'),
        'p2': ('Sarah\u2019s mum is telling a friend about Sarah\u2019s party. Example: the party is for Sarah.\n'
               '— When is the party?\n— On the 11th of June.\n'
               '— And what time does it start?\n— At four o\u2019clock in the afternoon.\n'
               '— How many guests?\n— Fourteen children and a few parents.\n'
               '— What cake would you like?\n— Sarah\u2019s favourite is strawberry – strawberry cake, please.\n'
               '— What\u2019s the number of the house again?\n— Our house is number 46.'),
        'p3': ('Lily is telling her friend about her week. Example: on Monday she visited her cousin Mark.\n'
               '— Tuesday? My big brother came home from university – I sat with him all day.\n'
               '— Wednesday I went to see my aunt – she was sick.\n'
               '— Thursday afternoon – I visited my grandpa.\n'
               '— Friday we had dinner at my uncle\u2019s flat.\n'
               '— And Saturday was for my little sister – we played all day at her house.'),
        'p4': ('1. — Where\u2019s Mum? — She was in the kitchen but now she\u2019s outside – yes, in the garden.\n'
               '2. — Do you like the new sofa? — It\u2019s not green and not brown. Actually it\u2019s a nice '
               'grey colour.\n'
               '3. — How many brothers, Jack? — I\u2019ve got my older brother, a twin brother and a baby '
               'brother. Three altogether.\n'
               '4. — Who\u2019s on the phone? — Grandpa Roy! He\u2019s calling from Spain.\n'
               '5. — I can\u2019t find the cat! — Look under the bed. No… On the wardrobe? No… Oh, there '
               'she is, behind the curtains!'),
        'p5': ('This is a living room. Example: colour the TV black.\n'
               '1. The sofa – colour it orange.\n'
               '2. On the small table next to the TV, draw a book.\n'
               '3. The round rug on the floor – colour it yellow.\n'
               '4. Above the picture of the mountain, write the word HOME.\n'
               '5. The cat next to the toy box – colour the cat grey.'),
    },
    'answers': {
        'rw': {
            'p1': '1 a fridge, 2 a kitchen, 3 a mirror, 4 a bathroom, 5 a wardrobe, 6 a lamp, '
                  '7 a cushion, 8 a garage, 9 a carpet, 10 a garden',
            'p2': '1 D, 2 G, 3 A, 4 B, 5 E, 6 F',
            'p3': '1 house, 2 kitchen, 3 living, 4 sister, 5 pictures, 6 friendly — Best title: B',
            'p4': '1 C (than), 2 A (old), 3 A (where), 4 A (love), 5 B (about), 6 A (stay)',
            'p5': '1 pancakes, 2 the writer (I), 3 the bathroom, 4 (at) 11 o\u2019clock, 5 (his) cereal, '
                  '6 Rocky, 7 watched a film (with popcorn)',
            'p6': '(ex) is — 1 the (or his), 2 as, 3 on, 4 and, 5 us, 6 up',
            'p7': 'Sample: "Last night Sam was sleeping in his bedroom. At 11 p.m. the neighbours started '
                  'playing very loud music! Sam covered his ears with a pillow but he couldn\u2019t sleep. '
                  'The next morning, Sam\u2019s dad went to talk to the neighbours. They said sorry and '
                  'now everyone in the street is happy again." (55 words)',
        },
        'listening': {
            'p1': 'Uncle Ben → guitar; Aunt Mary → camera; Cousin Jake → balloon; Emma → phone/photos; '
                  'Grandma Sue → giving a present.',
            'p2': '1 11th June (11/6), 2 4 o\u2019clock / 4 p.m., 3 14, 4 strawberry, 5 46',
            'p3': '1 E, 2 C, 3 F, 4 A, 5 G',
            'p4': '1 B, 2 C, 3 C, 4 B, 5 C',
            'p5': '1 Sofa orange; 2 Book drawn on the small table next to the TV; 3 Rug yellow; '
                  '4 "HOME" above the picture; 5 Cat grey.',
        },
        'speaking': {
            'Part 1': 'Book/newspaper; train/truck; dog/cat; one clock / two clocks.',
            'Part 2': 'Examiner info: Parker family, David (doctor), Rachel (teacher), children Lisa, Tom & '
                      'baby Anna, a cat, in the countryside.',
            'Part 3': 'Accept: "The children make breakfast / a tray with tea, toast and flowers. They bring it '
                      'to Mum\u2019s bedroom. Mum is happy and hugs them."',
            'Part 4': 'Full personal answers; extended family vocabulary; rooms; weekend routines; '
                      'household chores.',
        },
    },
}


# =====================================================================
# TEST 5 – SPORTS & HOBBIES
# =====================================================================
TEST_5 = {
    'number': 5,
    'theme': 'Sports & Hobbies',
    'rw': _rw(
        p1={
            'words': ['a helmet', 'a goal', 'a swimming pool', 'a skateboard', 'a tennis court',
                      'a racket', 'a bicycle', 'a hockey stick', 'a whistle', 'a gym',
                      'a medal', 'a golf club', 'trainers', 'a ball', 'a rope'],
            'example': 'a bicycle',
            'defs': [
                'You wear this on your head to be safe when you ride.',
                'You use this to play tennis.',
                'You get this when you win a race or a competition.',
                'A special place with machines where people do exercise.',
                'Teachers and referees blow this to make a sound.',
                'A place full of water where you can swim.',
                'Comfortable shoes for running and sport.',
                'A long piece of string you can jump with.',
                'A flat board with small wheels that children ride.',
                'This is a place to play tennis or basketball.',
            ],
        },
        p2={
            'speakerA': 'Coach', 'speakerB': 'Ethan',
            'line0_a': 'Hi Ethan, are you ready for today\u2019s football training?',
            'line0_b_letter': 'D',
            'line0_b_text': 'Yes, coach. I\u2019m really excited!',
            'pairs': [
                {'a': 'Great. Did you bring your water bottle?'},
                {'a': 'Good. We\u2019re going to practise goals today.'},
                {'a': 'Excellent. Who\u2019s your favourite player?'},
                {'a': 'Nice choice. Have you seen him on TV?'},
                {'a': 'Amazing. Do you want to be a goalkeeper today?'},
                {'a': 'OK. After training, let\u2019s have a short race.'},
            ],
            'options': [
                ('A', 'Yes, and I brought my mum, too – she wants to watch.'),
                ('B', 'Perfect! I love practising shooting.'),
                ('C', 'Yes, many times – he scored three goals last match!'),
                ('D', 'Yes, coach. I\u2019m really excited!'),
                ('E', 'No, I prefer playing in attack.'),
                ('F', 'Sure, but only a short one – I get tired!'),
                ('G', 'My favourite player is Leo. He\u2019s from Spain.'),
                ('H', 'Yes, I put it in my bag this morning.'),
            ],
        },
        p3={
            'words': ['team', 'played', 'cold', 'goals', 'happy', 'classmates', 'sports', 'school'],
            'title': 'The football match',
            'text': ('Last weekend, my __(1)__ had a football match against another school. '
                     'The morning was very __(2)__ but we ran a lot, so soon we felt warm. '
                     'I __(3)__ for 60 minutes and I scored two __(4)__! '
                     'Our __(5)__ came to watch us with their families. When we won, everyone was very __(6)__ '
                     'and we took a team photo.'),
            'title_choices': [
                ('A', 'A trip to the mountains'),
                ('B', 'The football match'),
                ('C', 'My new piano lessons'),
            ],
        },
        p4={
            'title': 'Why we do sport',
            'text': ('Sport is very important for our bodies and our minds. When we play sport, we breathe lots '
                     '__(1)__ fresh air and we move our muscles. It __(2)__ us strong and healthy. '
                     'Sport can also be fun. Many children __(3)__ different sports at school – football, '
                     'basketball, swimming or tennis. Other people prefer __(4)__ types of sport, like yoga '
                     'or gymnastics. Sport also teaches us __(5)__ work with other people and not give up. '
                     'After sport, many people __(6)__ very happy and tired at the same time.'),
            'items': [
                {'q': '1', 'options': {'A': 'of', 'B': 'in', 'C': 'from'}},
                {'q': '2', 'options': {'A': 'make', 'B': 'makes', 'C': 'making'}},
                {'q': '3', 'options': {'A': 'try', 'B': 'tries', 'C': 'trying'}},
                {'q': '4', 'options': {'A': 'quiet', 'B': 'quieter', 'C': 'quietest'}},
                {'q': '5', 'options': {'A': 'to', 'B': 'for', 'C': 'with'}},
                {'q': '6', 'options': {'A': 'feel', 'B': 'like', 'C': 'look'}},
            ],
        },
        p5={
            'title': 'The painting competition',
            'text': ('Every summer, my town has a big painting competition in the park. '
                     'This year, my best friend Nico and I decided to try it for the first time. '
                     'We walked to the park at nine o\u2019clock with our pencils, paper and colours. '
                     'There were more than 50 children in the competition! Each child had two hours to paint. '
                     'I painted a beautiful dragon flying over the mountains. Nico painted a football player '
                     'scoring a goal. It was difficult because the sun was strong and we got very hot. '
                     'In the end, Nico won a silver medal for his picture. I didn\u2019t win a prize, but the '
                     'judges said my dragon was amazing. We ate an ice cream each to celebrate. '
                     'Next year, I will paint a castle with a princess and a dragon!'),
            'example_q': 'Where is the competition?',
            'example_a': 'in the park',
            'questions': [
                'At what time did they arrive?',
                'How many children were in the competition?',
                'How long did they have to paint?',
                'What did the writer paint?',
                'What did Nico paint?',
                'Which prize did Nico win?',
                'What did they eat to celebrate?',
            ],
        },
        p6={
            'title': 'My brother\u2019s hobby',
            'text': ('My brother Leo is twelve years old and his favourite hobby __(ex)__ playing the guitar. '
                     'He started __(1)__ two years ago with a teacher called Mrs Diaz. '
                     'Leo practises every day in __(2)__ bedroom. At first his music was not very good, but now '
                     'it is really beautiful! Last month, he played __(3)__ a small concert in the library. '
                     'Our whole family went, and many of __(4)__ cousins came too. Leo was a little nervous '
                     'but he played perfectly. After the concert, everybody clapped and __(5)__ a lot of '
                     'photos. I want to learn __(6)__ play an instrument too – maybe the piano.'),
            'example': 'is',
            'answers': ['(learning)', 'his', 'at', 'our', 'took', 'to'],
        },
        p7={
            'title': 'The new bike',
            'p1': 'A girl gets a new bike for her birthday.',
            'p2': 'She rides it in the park but falls off near a tree.',
            'p3': 'She gets up, smiles at her dad and rides home safely.',
        },
    ),
    'listening': _listening(
        p1={
            'scene': 'A sports centre: a boy playing table tennis, a girl swimming in a pool, a man lifting '
                     'weights, a woman doing yoga on a mat, a boy climbing a wall, a girl running on a '
                     'treadmill, a coach with a clipboard.',
            'example_name': 'Coach Bob',
            'names': ['Laura', 'Nick', 'Olivia', 'Sam', 'Grace'],
        },
        p2={
            'heading': 'New swimming lessons',
            'example_label': 'Sport club name',
            'example': 'Bluewave',
            'labels': [
                'First lesson: day',
                'First lesson: time',
                'Teacher\u2019s first name',
                'Number of children per group',
                'Cost of one month (£)',
            ],
        },
        p3={
            'instruction': 'Helen is telling her dad which sport she does each day.',
            'example_item': 'Monday', 'example_letter': 'C',
            'items': ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
            'options': [
                ('A', 'basketball'), ('B', 'karate'), ('C', 'football'), ('D', 'dance'),
                ('E', 'tennis'), ('F', 'swimming'), ('G', 'running'), ('H', 'chess'),
            ],
        },
        p4={
            'items': [
                {'q': 'What colour is the team\u2019s new shirt?',
                 'A': 'red', 'B': 'yellow', 'C': 'blue'},
                {'q': 'What did Ben win last week?',
                 'A': 'a medal', 'B': 'a cup', 'C': 'a book'},
                {'q': 'Which sport does the girl like best?',
                 'A': 'horse riding', 'B': 'swimming', 'C': 'tennis'},
                {'q': 'What time does the match start?',
                 'A': '2:30', 'B': '3:00', 'C': '3:15'},
                {'q': 'Where did the boys play football on Sunday?',
                 'A': 'at the park', 'B': 'at school', 'C': 'at the beach'},
            ],
        },
        p5={
            'scene': 'A skate park: a big ramp, a boy on a skateboard, a bench with a bag, a tree, '
                     'a sign with the name of the park, a bin, a dog on a lead with a girl.',
            'example': 'Colour the skateboard green.',
            'items': [
                'Colour the bag on the bench purple.',
                'Draw a ball near the bin.',
                'Colour the dog brown.',
                'Write the word SKATE on the sign.',
                'Colour the tree\u2019s leaves orange.',
            ],
        },
    ),
    'speaking': {
        'p1_ex': 'A sports scene: a boy playing football, a girl on a bike, a red ball, a big tree, '
                 'two birds in the sky, a bench with a cap on it.',
        'p1_cand': 'A sports scene: a boy playing BASKETBALL, a girl on a bike, a GREEN ball, a big tree, '
                   'FOUR birds in the sky, a bench with a BOOK on it.',
        'p1_diffs': [
            'Football vs basketball.',
            'Red ball vs green ball.',
            'Two birds vs four birds.',
            'Cap on bench vs book on bench.',
        ],
        'p2_topic': 'Two sports clubs',
        'p2_cand_card': 'SPORTS CLUB: Action Kids – Address: ______ Avenue – Sports: ______, ______ '
                        'and ______ – Best day for families: ______ – Clothes to wear: ______.',
        'p2_cand_qs': [
            'What\u2019s the name of your sports club?',
            'Where is it?',
            'What sports can you do there?',
            'How many people train there?',
            'Is there a café?',
        ],
        'p2_ex_card': 'SPORTS CLUB: Lion Sports Centre – 12 High Street – swimming, tennis, judo, '
                      'football – 60 members – yes, café with sandwiches.',
        'p2_ex_qs': [
            'What\u2019s the club called?',
            'Where is Action Kids?',
            'What sports can you do there?',
            'Which day is best for families?',
            'What should you wear?',
        ],
        'p3_title': 'The big race',
        'p3_p1': 'Children are at the start of a running race at school.',
        'p3_p2': 'A girl is running very fast and is in first place.',
        'p3_p3': 'She crosses the finish line and everyone cheers.',
        'p3_p4': 'The head teacher gives her a gold medal and she smiles.',
        'p3_examiner_open': 'These pictures tell a story about "The big race". Children are at the start of a running race at school. Now you tell the rest of the story.',
        'p4_questions': [
            'What sports do you like playing?',
            'What hobbies do you have at the weekend?',
            'Do you prefer team sports or playing alone? Why?',
            'Tell me about a game you played recently.',
            'Do you watch sports on TV? Which ones?',
        ],
    },
    'scripts': {
        'p1': ('Look at the sports centre. Coach Bob is the man with the clipboard – that\u2019s the example.\n'
               '1. Where\u2019s Laura? She\u2019s the girl swimming in the pool.\n'
               '2. Can you see Nick? Nick is the boy playing table tennis.\n'
               '3. Now Olivia. Olivia is the woman doing yoga on a mat.\n'
               '4. Sam? Sam is the boy climbing the wall.\n'
               '5. And Grace? Grace is the girl running on the treadmill.'),
        'p2': ('A father is calling a swimming club. Example: the club\u2019s name is Bluewave.\n'
               '— When\u2019s the first lesson?\n— Next Wednesday.\n'
               '— What time?\n— At a quarter to six in the afternoon.\n'
               '— Who\u2019s the teacher?\n— Her first name is Rachel.\n'
               '— How many children per group?\n— Eight children maximum.\n'
               '— And the cost?\n— Thirty-five pounds a month.'),
        'p3': ('Helen is telling her dad about her sports. Example: on Monday she plays football.\n'
               '— Tuesday I go to karate – I\u2019ve got a new belt!\n'
               '— Wednesday afternoon is tennis.\n'
               '— Thursday I go swimming with my cousin.\n'
               '— Friday is basketball day.\n'
               '— And Saturday, I love to go running in the park.'),
        'p4': ('1. — What colour is the new team shirt? — Not red or blue. It\u2019s a bright yellow. Very cool!\n'
               '2. — What did Ben win? — He got a lovely silver medal last week at the gymnastics competition.\n'
               '3. — What\u2019s your favourite sport? — I used to love tennis. Now horse riding is my absolute '
               'favourite.\n'
               '4. — What time is the match? — The match starts at three fifteen, not two thirty.\n'
               '5. — Where did you play on Sunday? — Not at the park – it was closed. At school. We played '
               'football at school all afternoon.'),
        'p5': ('This is a skate park. Example: colour the skateboard green.\n'
               '1. On the bench there\u2019s a bag – colour it purple.\n'
               '2. Near the bin, draw a ball.\n'
               '3. Can you see the dog? Colour the dog brown.\n'
               '4. The sign has the name of the park. Write the word SKATE on the sign.\n'
               '5. The tree has leaves – colour the leaves orange.'),
    },
    'answers': {
        'rw': {
            'p1': '1 a helmet, 2 a racket, 3 a medal, 4 a gym, 5 a whistle, 6 a swimming pool, '
                  '7 trainers, 8 a rope, 9 a skateboard, 10 a tennis court',
            'p2': '1 H, 2 B, 3 G, 4 C, 5 E, 6 F',
            'p3': '1 school, 2 cold, 3 played, 4 goals, 5 classmates, 6 happy — Best title: B',
            'p4': '1 A (of), 2 B (makes), 3 A (try), 4 A (quiet), 5 A (to), 6 A (feel)',
            'p5': '1 at nine o\u2019clock, 2 more than 50, 3 two hours, 4 a dragon (flying over mountains), '
                  '5 a football player (scoring a goal), 6 a silver medal, 7 an ice cream',
            'p6': '(ex) is — 1 learning, 2 his, 3 at, 4 our, 5 took, 6 to',
            'p7': 'Sample: "Jenny got a beautiful red bike for her birthday. She was so happy! In the afternoon, '
                  'she rode the bike in the park. She was very fast, but then she fell off near a big tree. '
                  'She wasn\u2019t hurt. She smiled at her dad, got up, and rode back home safely." (55 words)',
        },
        'listening': {
            'p1': 'Laura → swimming; Nick → table tennis; Olivia → yoga; Sam → climbing wall; '
                  'Grace → treadmill.',
            'p2': '1 Wednesday, 2 5:45 (quarter to 6), 3 Rachel, 4 8, 5 35',
            'p3': '1 B, 2 E, 3 F, 4 A, 5 G',
            'p4': '1 B, 2 A, 3 A, 4 C, 5 B',
            'p5': '1 Bag purple; 2 Ball drawn near bin; 3 Dog brown; 4 "SKATE" on sign; 5 Tree leaves orange.',
        },
        'speaking': {
            'Part 1': 'Football/basketball; red/green ball; 2/4 birds; cap/book on bench.',
            'Part 2': 'Examiner info: Lion Sports Centre, 12 High Street, swimming/tennis/judo/football, '
                      '60 members, café with sandwiches.',
            'Part 3': 'Accept: "The girl runs very fast. She\u2019s the first. She finishes first. The teacher '
                      'gives her a gold medal."',
            'Part 4': 'Personal answers with reason; use of "prefer", frequency adverbs; past simple for '
                      '"Tell me about a game you played…".',
        },
    },
}
