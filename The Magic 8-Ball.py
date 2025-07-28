# The Magic 8-Ball

name = "Roger"
question = "Is planet Earth flat?"
answer = ""

# All possible fortune outcomes

import random

random_number = random.randint(1, 10)
print(random_number)

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"

print(name + ' asks: ' + question)
print("Magic 8-Ball's answer: " + answer)

# Optional Task

name = "question:"
question = "Is Mars habitable for life"
answer = ""

random_number = random.randint(10, 16)
print(random_number)

if random_number == 10:
  answer = "No"
elif random_number == 11:
  answer = "Absolutly"
elif random_number == 12:
  answer = "Probably not"
elif random_number == 13:
  answer = "Probably so"
elif random_number == 14:
  answer = "Try asking again"
elif random_number == 15:
  answer = "Anythings possible"
else:
  answer = "Shake me again"

print(name + " " + question)
print("Magic 8-Ball's answer " + str(answer))