# import files
from flask import Flask, render_template, request
from chatterbot import ChatBot


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)



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



# app
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatIBA.get_response(userText))


if __name__ == "__main__":
    app.run()
