Favorite_languages = {
    'Fred' : 'Python',
    'John' : 'C#',
    'Mary' : 'C++',
    'Susan' : 'Java'
}

People = ['Fred', 'John', 'Mary', 'Susan', 'Eric', 'Ophelia']

for person in People:
    if person in Favorite_languages:
        language = Favorite_languages[person]
        print(f"\nHi {person}! I see you like {language}!")
    else:
        print(f"\n{person}, you should take the poll!")