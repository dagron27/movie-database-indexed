import random
from datetime import timedelta, datetime

genres = [
    (1, "Drama"), (2, "Crime"), (3, "Thriller"), (4, "Adventure"), (5, "Sci-Fi"),
    (6, "Action"), (7, "Horror"), (8, "War"), (9, "Superhero"), (10, "Epic"),
    (11, "Comedy"), (12, "Fantasy"), (13, "Musical"), (14, "Mystery"), (15, "Romance"),
    (16, "Western"), (17, "Documentary"), (18, "Biography"), (19, "Family"), (20, "Sport")
]

genre_descriptions = {
    1: ["A moving tale of human experience.", "An emotional journey through life's ups and downs.", "A compelling story of love and loss."],
    2: ["A gripping crime drama.", "A thrilling whodunit.", "A tale of corruption and justice."],
    3: ["A nail-biting thriller.", "A suspenseful mystery.", "A story that keeps you on the edge of your seat."],
    4: ["An adventurous journey.", "A tale of exploration and discovery.", "An epic quest."],
    5: ["A mind-bending sci-fi saga.", "A journey through space and time.", "A futuristic adventure."],
    6: ["High-octane action.", "A pulse-pounding action thriller.", "A story filled with explosive action."],
    7: ["A horrifying experience.", "A chilling tale.", "A terrifying journey."],
    8: ["A war epic.", "A story of bravery and sacrifice.", "A tale of soldiers in battle."],
    9: ["A superhero adventure.", "A battle between good and evil.", "A story of heroes and villains."],
    10: ["An epic saga.", "A grand tale of adventure.", "A story of great battles and heroes."],
    11: ["A hilarious comedy.", "A tale of laughs and fun.", "A comedic escapade."],
    12: ["A magical fantasy tale.", "A journey through fantastical realms.", "A story filled with mythical creatures and adventure."],
    13: ["A captivating musical.", "A story told through song and dance.", "An enchanting musical journey."],
    14: ["A mysterious tale.", "A story filled with intrigue and secrets.", "A thrilling mystery to unravel."],
    15: ["A heartwarming romance.", "A tale of love and relationships.", "A romantic journey."],
    16: ["A classic western.", "A tale of the wild west.", "A story of cowboys and frontier life."],
    17: ["An enlightening documentary.", "A deep dive into real-life events.", "A factual and informative story."],
    18: ["A compelling biography.", "The story of an extraordinary individual.", "A detailed life story."],
    19: ["A family-friendly tale.", "A story suitable for all ages.", "A heartwarming family adventure."],
    20: ["An exciting sports story.", "A tale of athletic achievement.", "A story of sportsmanship and competition."]
}

first_names = {
    'A': ["Alice", "Aaron", "Abigail", "Adam", "Ava"],
    'B': ["Ben", "Bella", "Brandon", "Brooke", "Blake"],
    'C': ["Cameron", "Charlotte", "Caleb", "Chloe", "Cole"],
    'D': ["Daniel", "Daisy", "David", "Delilah", "Derek"],
    'E': ["Ethan", "Emma", "Evan", "Ella", "Evelyn"],
    'F': ["Felix", "Fiona", "Finn", "Faith", "Freya"],
    'G': ["George", "Grace", "Gavin", "Gabriella", "Graham"],
    'H': ["Henry", "Hannah", "Harrison", "Hailey", "Heather"],
    'I': ["Isaac", "Isabella", "Ian", "Ivy", "Iris"],
    'J': ["James", "Julia", "Jack", "Jasmine", "Jacob"],
    'K': ["Kyle", "Kayla", "Kevin", "Katherine", "Kieran"],
    'L': ["Liam", "Lily", "Lucas", "Lauren", "Levi"],
    'M': ["Michael", "Mia", "Matthew", "Maya", "Mason"],
    'N': ["Noah", "Nora", "Nathan", "Nicole", "Neil"],
    'O': ["Oliver", "Olivia", "Owen", "Ophelia", "Oscar"],
    'P': ["Paul", "Paige", "Peter", "Piper", "Patrick"],
    'Q': ["Quinn", "Quincy", "Quentin", "Queenie", "Quest"],
    'R': ["Ryan", "Rachel", "Riley", "Rebecca", "Robert"],
    'S': ["Samuel", "Sophia", "Steven", "Scarlett", "Sebastian"],
    'T': ["Thomas", "Taylor", "Theodore", "Tessa", "Toby"],
    'U': ["Ulysses", "Una", "Uriah", "Ursula", "Umberto"],
    'V': ["Victor", "Violet", "Vincent", "Vanessa", "Vera"],
    'W': ["William", "Wendy", "Wesley", "Whitney", "Wyatt"],
    'X': ["Xander", "Xena", "Xavier", "Xanthe", "Xerxes"],
    'Y': ["Yusuf", "Yara", "Yuri", "Yasmin", "Yvonne"],
    'Z': ["Zachary", "Zoe", "Zane", "Zara", "Zelda"]
}

last_names = {
    'A': ["Anderson", "Adams", "Armstrong", "Austin", "Allen"],
    'B': ["Brown", "Baker", "Brooks", "Bell", "Barnes"],
    'C': ["Clark", "Campbell", "Carter", "Collins", "Cook"],
    'D': ["Davis", "Diaz", "Dunn", "Duncan", "Daniels"],
    'E': ["Edwards", "Evans", "Ellis", "Elliott", "Eaton"],
    'F': ["Foster", "Fleming", "Fisher", "Ford", "Francis"],
    'G': ["Green", "Garcia", "Gordon", "Grant", "Gray"],
    'H': ["Harris", "Hughes", "Hernandez", "Hamilton", "Hayes"],
    'I': ["Ingram", "Irving", "Ibarra", "Iverson", "Isaac"],
    'J': ["Jackson", "Johnson", "Jones", "James", "Jenkins"],
    'K': ["King", "Kelley", "Kennedy", "Kim", "Knight"],
    'L': ["Lewis", "Lee", "Lopez", "Long", "Lawson"],
    'M': ["Miller", "Martin", "Mitchell", "Moore", "Murphy"],
    'N': ["Nelson", "Nguyen", "Nichols", "Norton", "Newton"],
    'O': ["Owen", "Ortega", "Osborne", "Owens", "Oliver"],
    'P': ["Parker", "Perez", "Powell", "Price", "Perry"],
    'Q': ["Quinn", "Quinlan", "Quintana", "Quimby", "Quezada"],
    'R': ["Robinson", "Rodriguez", "Rivera", "Reed", "Rogers"],
    'S': ["Smith", "Scott", "Sanders", "Sullivan", "Stewart"],
    'T': ["Taylor", "Thomas", "Thompson", "Turner", "Tate"],
    'U': ["Underwood", "Upton", "Uribe", "Ullman", "Ulrich"],
    'V': ["Vargas", "Vaughn", "Vega", "Vance", "Vincent"],
    'W': ["Williams", "Walker", "White", "Wood", "Wright"],
    'X': ["Xiong", "Xander", "Ximenez", "Xiao", "Xue"],
    'Y': ["Young", "York", "Yoder", "Yates", "Yeager"],
    'Z': ["Zimmerman", "Zuniga", "Ziegler", "Zavala", "Zane"]
}

adjectives = [
    "Amazing", "Bewitched", "Charming", "Dazzling", "Enigmatic",
    "Fantastic", "Glorious", "Harmonious", "Incredible", "Jubilant",
    "Magical", "Radiant", "Spectacular", "Thrilling", "Wonderous",
    "Astonishing", "Breathtaking", "Captivating", "Delightful", "Elegant",
    "Fabulous", "Gorgeous", "Heavenly", "Illustrious", "Joyous",
    "Majestic", "Noble", "Opulent", "Picturesque", "Quaint",
    "Remarkable", "Splendid", "Terrific", "Unbelievable", "Vibrant",
    "Whimsical", "Xenodochial", "Youthful", "Zestful", "Alluring",
    "Blissful", "Courageous", "Dramatic", "Enchanting", "Flourishing",
    "Gallant", "Heroic", "Iconic", "Jolly", "Kind-hearted",
    "Lavish", "Magnificent", "Nostalgic", "Optimistic", "Passionate",
    "Quixotic", "Resplendent", "Sensational", "Timeless", "Unique",
    "Victorious", "Winsome", "Xenophilic", "Yearning", "Zealous",
    "Adventurous", "Bright", "Calm", "Dignified", "Eager",
    "Fierce", "Grand", "Humble", "Impressive", "Joyful",
    "Keen", "Luminous", "Mystical", "Nurturing", "Opportune",
    "Peaceful", "Radiant", "Sublime", "Transcendent", "Uplifting",
    "Valiant", "Wise", "Xotic", "Yielding", "Zephyr-like"
]

nouns = [
    "Adventure", "Dream", "Escape", "Fantasy", "Journey",
    "Mystery", "Odyssey", "Quest", "Voyage", "Legend",
    "Miracle", "Enchantment", "Whisper", "Wonder", "Treasure",
    "Saga", "Tale", "Discovery", "Expedition", "Chronicle",
    "Myth", "Marvel", "Fable", "Prophecy", "Serenade",
    "Wanderlust", "Glimpse", "Vista", "Reverie", "Oasis",
    "Vision", "Echo", "Revelation", "Parable", "Trilogy",
    "Labyrinth", "Spectrum", "Phenomenon", "Legacy", "Solstice",
    "Artifact", "Pathway", "Illusion", "Resonance", "Anecdote",
    "Radiance", "Monument", "Phantasm", "Wonderland", "Dimension",
    "Elysium", "Sanctuary", "Realm", "Enigma", "Euphoria",
    "Wilderness", "Mirage", "Apocalypse", "Horizon", "Serenity",
    "Epoch", "Alchemy", "Infinity", "Eclipse", "Paradise",
    "Genius", "Mosaic", "Genesis", "Ascension", "Icon",
    "Paradox", "Beacon", "Sensation", "Whirlwind", "Tapestry",
    "Aura", "Haven"
]

def generate_genre():
    return random.choice(genres)

def generate_first_name():
    letter = random.choice(list(first_names.keys()))
    return random.choice(first_names[letter])

def generate_last_name():
    letter = random.choice(list(last_names.keys()))
    return random.choice(last_names[letter])

def random_date(start=None, end=None): 
    if start is None: start = datetime(1920, 1, 1) 
    if end is None: end = datetime(2006, 12, 31) 
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

def generate_person():
    fname = generate_first_name()
    lname = generate_last_name()
    bdate = random_date().strftime("%Y-%m-%d")
    return { "name": f"{fname} {lname}", "birthday": bdate }

def generate_movie_title():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    random_number = random.randint(1000, 9999)
    return f"{adjective} {noun} {random_number}"

def random_rating():
    return round(random.uniform(1.0, 10.0), 1)

def new_description(genre_id):
    return random.choice(genre_descriptions[genre_id])

def generate_movie(genre_id, n_director_id):
    title = generate_movie_title()
    year = random.randint(1938, 2024)
    rating = random_rating()
    #description = random.choice(genre_descriptions[genre_id])
    option = random.randint(0, 2)
    description = genre_descriptions[genre_id][option]
    director_id = n_director_id
    movie = (title, year, rating, description, director_id)
    
    return movie
