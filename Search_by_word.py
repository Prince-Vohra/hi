
file = open("english.txt", 'r', encoding="utf-8")
data = file.read()
data_list = data.split("\n")
dictionary = {}
for word in data_list:
    if "  " in word:
        word_list = word.split("  ")
        dictionary[word_list[0].lower()] = word_list[1:]
while 1:
    try:
        search_key = input("Find the definition of:")
        print(dictionary[search_key.lower()])
    except Exception :
        print("Sorry, Word not found Please check again")