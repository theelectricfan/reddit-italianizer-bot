import random
from langdetect import detect

# Set of fun Italian phrases
italian_phrases = [
    "Mamma mia!", "It's-a me, Mario!", "Pizza pasta mandolino!",
    "El Pasole Quesa El Italia!", "Pasta, pizza, and amore!",
    "Spaghetti-a, ravioli-a, mamma mia!", "Bada bing bada boom!",
    "Ciao bella!", "Grazie, grazie!", "Bellissimo!", "Mangia, mangia!",
    "La dolce vita!", "Espresso and gelato for everyone!", "Viva Italia!",
    "Don’t-a make-a me pull out-a da cannoli!", "Che bella giornata!",
    "You talk-a more than-a the piazza on Sunday!",
    "This is more exciting than-a watching-a football in Napoli!",
    "Bello! As fun as a festa in Venice!"
]

# Fun sound effects
sound_effects = [
    "Cha-ching!", "Vroom vroom!", "Bada bing!", "Boom boom!",
    "Woooah!", "Ring-a ding-a!", "Snap-a snap-a!", "Zoom zoom!",
    "Pop-pop-pop!", "Ding-a ling!"
]

# Over-the-top Italian compliments
italian_compliments = [
    "Bravo! You-a da Michelangelo of words!", "Bellissimo! You deserve-a golden pizza!",
    "Fantastico! As sweet as gelato on a summer day!",
    "You-a just painted-a masterpiece like-a da Vinci!",
    "Magnifico! As perfect as a sunset in Sicily!",
    "You got-a da flavor of-a mamma's Sunday sauce!",
    "You're-a spicier than-a pepperoni on-a pizza!",
    "Hotter than-a fresh pasta from-a da pot!",
    "Sharp as-a Parmigiano!",
    "You-a sparkle like-a fresh olive oil on-a bruschetta!",
    "This is as beautiful as Venezia!", "Rome wasn’t built in a day, but your words are-a masterpiece!",
    "As stunning as the Colosseum!", "You-a shine brighter than-a the Amalfi coast!",
    "More legendary than-a da Leaning Tower of Pisa!",
    "Like-a strolling through da vineyards in Tuscany!",
    "You-a hit da bullseye, like-a Cupid in da Trevi Fountain!",
    "Like-a a moonlit night in da rolling hills of-a Sicily!",
    "As good as nonna's lasagna!", "Better than a hot plate of spaghetti!",
    "Like mamma's homemade pizza!", "A slice of heaven, just like tiramisu!",
    "As fresh as mozzarella!", "Smoother than a cappuccino!",
    "Crispier than-a fresh cannoli!", "Richer than-a da creamy ricotta!",
    "Sweeter than-a da fresh gelato!", "Hotter than-a da espresso shot at noon!"
]

# Set of Italian emojis
italian_emojis = ["🍕", "🍝", "🍷", "🍇", "🇮🇹", "🎶", "🏛️", "🎭", "🤌", "👏",
                  "💃", "👨‍🍳", "🕺", "🎉", "🇮🇹🤌", "👏🍷"]

# Name replacements
name_replacements = {
    "John": "Giovanni", "Mary": "Maria", "Michael": "Michele",
    "New York": "Nuova York", "Rome": "Roma", "Paris": "Parigi",
    "James": "Giacomo", "Lucy": "Lucia", "David": "Davide",
    "Henry": "Enrico", "Charles": "Carlo", "Robert": "Roberto",
    "Elizabeth": "Elisabetta", "Victoria": "Vittoria"
}

# Word/phrase replacements
word_replacements = {
    "eat": "mangia", "cook": "cuoca", "love": "amore", "run": "corre",
    "friend": "amico", "family": "famiglia", "amazing": "fantastico",
    "yes": "sì", "no": "no", "beautiful": "bellissimo",
    "walk": "cammina", "speak": "parla", "dream": "sogna",
    "strong": "forte", "fast": "veloce", "happy": "felice"
}

# Replace "the", "this", "that" with "da", "dis", "dat"
replacements = {
    " the ": " da ", "this ": "dis ", "that ": "dat ",
    " The ": " Da ", "This ": "Dis ", "That ": "Dat "
}


# Function to randomly double consonants in words
def double_consonants(word):
    consonants = ['l', 't', 'p', 'r', 'n', 's']
    return ''.join(char * 2 if char in consonants and random.random() > 0.7 else char for char in word)


# Function to randomly add accents on some vowels
def add_accents(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    accented_vowels = ['à', 'è', 'ì', 'ò', 'ù']
    return ''.join(
        random.choice([char, accented_vowels[vowels.index(char)]]) if char in vowels else char for char in word)


# Function to randomly duplicate words for emphasis
def duplicate_words(comment):
    words = comment.split()
    for i in range(len(words)):
        if random.random() > 0.8:  # 20% chance to duplicate a word
            words[i] = words[i] + " " + words[i]
    return ' '.join(words)


# Function to Italianize text
def italianize_text(comment):
    # Detect language
    try:
        lang = detect(comment)
        if lang == "it":
            return "Ah, you-a already speak-a Italiano! 🍕"
    except:
        pass

    # Apply replacements to the comment
    for key, value in replacements.items():
        comment = comment.replace(key, value)

    # Replace common verbs/words with Italianized versions
    for key, value in word_replacements.items():
        comment = comment.replace(key, value)

    # Replace common names/places
    for key, value in name_replacements.items():
        comment = comment.replace(key, value)

    # Randomly Italianize verb endings with "a", "o", "e"
    italianized_comment = ' '.join(
        double_consonants(word) + random.choice(["a", "o", "e"]) if len(word) > 2 and word.isalpha() else word for word
        in comment.split())

    # Randomly add accents on vowels in the comment
    italianized_comment = add_accents(italianized_comment)

    # Duplicate words randomly for emphasis
    italianized_comment = duplicate_words(italianized_comment)

    # Add random Italian phrases, food idioms, compliments, and landmarks
    if random.random() > 0.7:  # 30% chance to add a fun sound effect
        italianized_comment += f" {random.choice(sound_effects)}"

    if random.random() > 0.7:  # 30% chance to add a compliment
        italianized_comment += f" {random.choice(italian_compliments)}"

    # Randomly select an Italian phrase and emoji
    random_phrase = random.choice(italian_phrases)
    random_emoji = random.choice(italian_emojis)

    # Add Italian phrase, emoji, and gesture
    italianized_comment = f"{random_phrase} {italianized_comment} 🤌 {random_emoji}"

    return italianized_comment


# Example usage
comment = "we live in a beautiful world"
print(italianize_text(comment))
