

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer




#Chatbot Code


IBA_data = []


# data in txt file is appended to list IBA_data
with open('iba_admissions.txt', 'r') as file:
    for line in file:
        if  line.startswith('Q') or line.startswith('A'):
           IBA_data.append(line.strip()[2:])

with open('iba_academics.txt', 'r') as file:
    for line in file:
        if line.startswith('Q') or line.startswith('A'):
           IBA_data.append(line.strip()[2:])

with open('iba_campus life.txt', 'r') as file:
    for line in file:
        if line.startswith('Q') or line.startswith('A'):
           IBA_data.append(line.strip()[2:])






# Create a chat bot named chatIBA
chatIBA = ChatBot('chatIBA')

# Training the chatBOT

#training the chatbot with IBA data using list trainer
trainer = ListTrainer(chatIBA)
trainer.train(IBA_data)

# training the chatbot with Corpus trainer for general conversations.
trainer = ChatterBotCorpusTrainer(chatIBA)
trainer.train('chatterbot.corpus.english')


while True:
    try:
        
        user_input = input(">>> ")

        bot_response = chatIBA.get_response(user_input)

        print("->" , bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break