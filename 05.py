from nltk.stem import SnowballStemmer

my_cocktail_bar = [
    'gin', 'tonic', 'lemon', 'lemon peel', 'lemon juice',
    'water', 'whisky', 'angostura bitters',
    'dry vermouth', 'gin',
    'ice', 'sugar cube', 'sugar', 'orange',
    'orange peel', 'vodka', 'grapefruit juice',
    'drambuie', 'cranberry juice', 'orange juice', 'grapefruit juice'
]

# These are cocktail recipes:
old_fashioned = ['whisky', 'angostura bitters', 'sugar', 'water', 'lemon peel', 'ice']
dry_martini = ['dry vermouth', 'gin', 'ice']
rusty_nail = ['drambuie', 'whisky', 'ice']
espresso_martini = ['kahlua', 'vodka', 'espresso', 'sugar']
rob_roy = ['angostura bitters', 'sweet vermouth', 'whisky', 'ice']
margarita = ['cointreau', 'lime juice', 'tequila', 'ice']
whisky_sour = ['lemon juice', 'bourbon', 'egg', 'sugar']


cocktail_recipe_book = {
    'Old Fashioned': old_fashioned,
    'Dry Martini': dry_martini,
    'Rusty Nail': rusty_nail,
    'Espresso Martini': espresso_martini,
    'Rob Roy': rob_roy,
    'Margarita': margarita,
    'Whisky Sour': whisky_sour
}

for item in my_cocktail_bar:
    print(item)



# can I make an old fashioned cocktail?
i_can_make_it = True

for ingredient in old_fashioned:
    if ingredient not in my_cocktail_bar:
        i_can_make_it = False

print(i_can_make_it)



# can I make a margarita cocktail?
for ingredient in margarita:
    if ingredient not in my_cocktail_bar:
        i_can_make_it = False

print(i_can_make_it)



# ASIDE: strings and lists

my_string = 'hello world!'
# we can strip characters from a string
my_string = my_string.strip('!')


# we can join all elements of a list with the .join() method:
food_at_home = ['bread', 'cucumber', 'curly kale', 'soba noodles', 'miso soup']
foods = ' '.join(food_at_home)

# we can join them using any character:
foods = ', '.join(food_at_home)


# we can split a string into a list
my_string = 'bread cucumber potato banana'
my_list = my_string.split()


# opening a file
# word counting
# looping


## WORKING WITH FILES

# opening a file
freq_words_file = open('hungarian.txt', 'r')

common_words = []

# reading a file, line by line
for word in freq_words_file:
    common_words.append(word.strip())

# we have to close the file after we are done with it
freq_words_file.close()


# a better way of opening a file - this way, we don't have to close it,
# as it will be closed automatically
common_words = []
with open('hungarian.txt', 'r') as freq_words_file:
    for word in freq_words_file:
        common_words.append(word.strip())


# reading a file, line by line
with open('kenyer_bor.txt', 'r') as text_file:
    for line in text_file:
        print(line)



# counting words in a file, excluding common words
word_count = {}
stemmer = SnowballStemmer('hungarian')
with open('kosztol.txt', 'r') as text_file:
    for line in text_file:
        for word in line.split():
            word = word.lower()
            for trailing_char in [' ', '.', '!', '?', ',', '"', '\'']:
                word = word.strip(trailing_char)
            if word in common_words:
                continue
            try:
                word =  stemmer.stem(word)
            except:
                continue
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1

def get_n_most_frequent_words(word_count, n=10):
    sorted_words = sorted(list(word_count.items()), key=lambda item: item[1], reverse=True)
    return sorted_words[:n]

