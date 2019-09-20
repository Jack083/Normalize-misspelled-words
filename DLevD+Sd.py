import jellyfish as jf

with open("misspell.txt") as f1:
    misspell = f1.readlines()
with open("correct.txt") as f2:
    correct = f2.readlines()
with open("dict.txt") as f3:
    dictionary = f3.readlines()

misspell = [x.strip() for x in misspell]
misspell = [x.replace("'", '').replace("(", "").replace(")", "").replace("/", "").replace("-", "") for x in misspell]
correct = [x.strip() for x in correct]
correct = [x.replace("'", '').replace("(", "").replace(")", "").replace("/", "").replace("-", "") for x in correct]
dictionary = [x.strip() for x in dictionary]


token_size = 10
total_predict = 0
total_success = 0
distance_limit = 1
nd = 0

for i in range(token_size):
    predict = []
    matching = []
    p = True
    encoded_misspell = jf.soundex(misspell[i])
    for j in range(len(dictionary)):
        if jf.levenshtein_distance(misspell[i], dictionary[j]) <= distance_limit:
            shortest_distance = jf.levenshtein_distance(misspell[i], dictionary[j])
            matching.append([shortest_distance, dictionary[j]])
        else:
            encoded_dictionary = jf.soundex(dictionary[j])
            if jf.levenshtein_distance(encoded_misspell, encoded_dictionary) == 0:
                encoded_distance = jf.levenshtein_distance(encoded_misspell, encoded_dictionary)
                matching.append([encoded_distance, dictionary[j]])
    matching.sort()
    for k in range(len(matching)):
        if correct[i] == matching[k][1]:
            total_success += 1
            p = False
    total_predict = total_predict + len(matching)
    if p is True:
        if misspell[i] == correct[i]:
            nd += 1
        print("Misspell word: ", misspell[i])
        print("The correct word: ", correct[i])
        print('-' * 80)

pc = "Prediction count: " + str(total_predict) + "\n"
sp = "Success predicted: " + str(total_success) + "\n"
ts = "Tested size: " + str(token_size) + "\n"
r = "Recall: " + str(round(100*total_success/token_size, 2)) + "%" + "\n"
p = "Precision: " + str(round(100*total_success/total_predict, 2)) + "%" + "\n"
n = "Not in dictionary: " + str(nd) + "\n"
result = pc + sp + ts + r + p + n
print(result)
