"""Restaurant rating lister."""


# put your code here
reader = open('scores.txt')
ratings_dictionary = {} 

user_restaurant = input('Enter a restaurant!\n')
user_score = input('Enter a score for that restaurant!\n')

ratings_dictionary[user_restaurant] = int(user_score)

for line in reader:
    new_line = line.split(':')
    rating = new_line[1]
    ratings_dictionary[new_line[0]] = int(rating[0])

for key,value in sorted(ratings_dictionary.items()):
    print(f'{key} is rated {value}')
    


