'''alien_0 = {"x_position" : 0, "y_position" : 25, "speed" : "slow"}
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment

print("New x_position: " + str(alien_0["x_position"]))'''



'''friend = {"firstname" : "daniel", "lastname" : "wright", "city" : "westminister"}

print(friend["firstname"])
print(friend["lastname"])
print(friend["city"])'''



'''friends_nums = {"daniel":69,"cody":47,"katie":21,"erica":24,"eric":35}
print(friends_nums)'''


'''
glossary = {"list":"holds lists of strings that can be changed.",
             "concatenation":"makes strings shorter.",
             "tuples":"a list of strings that cannot be changed.",
             "strings":"words.",
             "dictionary":"we can assign key values to strings."}

print(glossary["list"] + "\n")
print(glossary["concatenation"] + "\n")
print(glossary["tuples"] + "\n")
print(glossary["strings"] + "\n")
print(glossary["dictionary"] + "\n")

for term, description in glossary.items():
    print("\nkey: " + term)
    print("\nvalue: " + description)
'''
    
'''fave_code = {"sarah": "python","cody": "python", "daniel": "javascript"}
friends = ["sarah"]
for language in set(fave_code.values()):
    print(language.title())'''








'''glossary = {"list":"holds lists of strings that can be changed.",
             "concatenation":"makes strings shorter.",
             "tuples":"a list of strings that cannot be changed.",
             "strings":"words.",
             "dictionary":"we can assign key values to strings.",
             "items": "a way to have python loop through key values",
             "set" : " only prints unique items in list",
             "doubletempvariable" : "we can have two temp variables on loops",
             "sorted" : "sorts the results in order",
             "if rules" : "create certain rules to display results"}

for x,y in glossary.items():
    print(x + "\n" + y)'''
    
    
'''rivers = {"nile" : "egypt", "amazon" : "puru", "chiangjiang" : "china"}
for river,location in rivers.items():
        print("The " + river.title() + " river runs through " + location.title())'''
    




'''polling = {"alexa" : "yes"
         , "bobby" : "no"
         , "tristian" : "yes"
         , "billy" : "no"
         , "tony" : "yes"}
         
friends = ["edward", "kiki"]

for x,y in polling.items():
    print(x.title() + ", thank you so much for your vote!")
    
if str(friends) not in x:
    print("Please take our poll! This is an important step to change!")'''
    
    
    
    
'''alien0 = {"color" : "green", "points" : 5}
alien1 = {"color" : "blue", "points" : 10}
alien2 = {"color" : "red", "points" : 15}

aliens = [alien0, alien1, alien2]

for alien in range(30):
    print(alien)'''
    
    
    
'''aliens = []
  
for alien_number in range(0,30):
    new_alien = {"color" : "green", "points" : 5, "speed" : "slow"}
    aliens.append(new_alien)


for alien in aliens:
    if alien["color"] == "green":
        alien["color"] == "yellow"
        alien["speed"] == "medium"
        alien["points"] == 10
        

for alien in aliens[0:5]:
    print(alien)
    print("-----")
print("\n---------------------")

print("Total number of aliens are: " + str(len(aliens)))'''


'''aliens = []

for alien_number in range(0,30):
    new_alien = {"color" : "green", "points" : 5, "speed" : "slow"}
    aliens.append(new_alien)
    
for alien in aliens:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["points"] = 10
        alien["speed"] = "medium"
        
for alien in aliens[0:5]:
    print(alien)
    print("-----")
print("The total number of aliens are: " + str(len(aliens)))'''


'''aliens = [] 

for alien_num in range(0,30):
    new_alien = {"color" : "green", "points" : 5, "speed" : "slow"}
    aliens.append(new_alien)
    
for alien in aliens[0:5]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["points"] = 10
        alien["speed"] = "medium"
for alien in aliens[5:10]:
    if alien["color"] == "green":
        alien["color"] = "red"
        alien["points"] = 15
        alien["speed"] = "fast"
for alien in aliens[10:15]:
    if alien["color"] == "green":
        alien["color"] = "purple"
        alien["points"] = 20
        alien["speed"] = "fastest"
        
for alien in aliens[0:30]:
    print(alien)
print("---------------------------------")
print("The total number of aliens is : " + str(len(aliens)))'''




'''name = "bobby"
pizza = {
    "crust" : "thick",
    "toppings" : ["pepperoni", "sausage", "mushroom"]
    }
print("Hello " + name.title() + ", Your pizza crust is a " + str(pizza["crust"])
    + " crust pizza with the following toppings:")
for x in pizza["toppings"]:
    print("\t>>>" + x)
    
print("\nThe total number of toppings on your pizza is: " + str(len(pizza["toppings"])))'''





'''fav_lang = {
    "michelle" : ["python", "java"],
    "bobby" : ["c", "java"],
    "billy" : ["html", "css"]
    }
    
for name, lang in fav_lang.items():
    print(name.title() + ",s favorite languages are:")
    for lan in lang:
        print("\t>>>" + lan)'''
'''print("Runescape Usernames\n")
usernames = {
    "codyblom" : {"firstname" : "cody",
                  "lastname" : "blomberg",
                  "location" : "cypress"
                      },
    "brandonarmy" : {"firstname" : "brandon",
                  "lastname" : "denham",
                  "location" : "anaheim"
                      }
            }

for username, user_info in usernames.items():
    print("Username: " + username)
    print("\tFirst name: " + user_info["firstname"].title())
    print("\tLast name: " + user_info["lastname"].title())
    print("\tLocation: " + user_info["location"].title())
    print("\n")
    
    
print("The total amount of usernames are: " + str(len(usernames)))'''


'''person_1 = { 
    "firstname" : "cody",
    "lastname" : "blomberg",
    "location" : "california"
        }
person_2 = { 
    "firstname" : "brandon",
    "lastname" : "denham",
    "location" : "arkansas"
        }
person_3 = { 
    "firstname" : "christian",
    "lastname" : "gambina",
    "location" : "california"
        }
people = [person_1, person_2, person_3]

for person in people:
    print(person)'''



'''animal_1 = {
    "animal_type" : "dog",
    "owner_name" : "cody"
        }
animal_2 = {
    "animal_type" : "turtle",
    "owner_name" : "tony"
        }
animal_3 = {
    "animal_type" : "cat",
    "owner_name" : "bobby"
        }

animals = [animal_1, animal_2, animal_3]

for animal in animals:
    print(animal)
    print("\n")'''

'''    
fav_places = {
    "bobby" : ["rome", "italy", "germany"],
    "tony" : ["usa", "phillipines", "italy"],
    "yancy" : ["new york", "colorado", "oregon"]
        }
print("Favorite places to visit survey:")
for name , location in fav_places.items():
    print("\n" + name.title() + " wants to travel to " + str(len(location)) + " places:")
    print("\t" + str(location).title())

print("The total amount of people in this survery are: " + str(len(fav_places)))
'''
'''
message = input("Please tell me your name: ")

print("Hello " + message.title() + ", it's very nice to meet you. My name is Blomberg software.\n")
print("We are a software company creating next generation hybrid attachment parts for gasoline vehicles.")
message_2 = input("Would you like to join our software development team? If so please print your first and last initial: ")
print("User: " + message.title() + " registered to Blomberg Database.")
print("Successful")
'''
'''prompt = "Hello, I need your name because it is vitaly important to our "
prompt += "database so that we can collect a lot of information."
prompt += "please enter your name: "

name = input(prompt)
print("Thank you for your contribution " + name.title())'''

'''drinking_age = input("How old are you? ")
drinking_age = int(drinking_age)
if drinking_age < 21:
    print("You are too young to drink!")
else:
    print("You are old enough to drink!\n")
    drinks = input("What would you like to drink? ")
    print("I'll go grab a " + drinks + " for you!")'''

'''message = input("Tell me a number and I will tell you if the number is odd or even: ") 
message = int(message)
if message % 2 == 0:
    print("Your number " + str(message) + " is an even number.")
else:
    print("Your number " + str(message) + " is an odd number.")'''
    
'''rental_car = input("What brand of car are you looking for? ")
print("Let me see if I can find you a " + rental_car + " for you to drive.")'''

'''guests = input("How many guests are in your party? ")
guests = int(guests)
print("\n")
if guests < 8:
    print("We will have you seated in aproximately 30 minutes.")
else:
    print("We will have you seated in aproximately 1 hour.")'''
    
'''numbers = input("Please enter a multiple of the number 10: ")
numbers = int(numbers)

if numbers % 10 == 0:
    print("Your number is a multiple of 10.")
else:
    print("Your number is NOT a multiple of 10.")'''


'''current_number = 1

while current_number:
    print(current_number)
    current_number += 1'''
    
'''import sklearn

from sklearn.linear_model import LinearRegression

predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)

X_TEST = [[10, 20, 30]]
outcome = predictor.predict(X=X_TEST)
coefficients = predictor.coef_

print('Outcome : {}\nCoefficients : {}'.format(outcome, coefficients))'''













    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    














