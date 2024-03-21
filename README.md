# AI Powerd Chatbot 


## Objective:
The objective of this project is to create a chatbot that provides information about the Institute of 
Business Administration (IBA) Karachi. The chatbot will be designed to answer common questions that 
students or prospective students might have about admissions, academics, and campus life at IBA.

## Methodology:
The chatbot was built using ChatterBot, a Python library for creating chatbots. The data used to train the 
chatbot was collected from text files containing frequently asked questions and their corresponding 
answers about IBA admissions, academics, and campus life. The data was pre-processed to remove any 
unnecessary characters or formatting and then fed into the chatbot using the ListTrainer module in 
ChatterBot.
To improve the chatbot's ability to handle general conversation, it was also trained using the 
ChatterBotCorpusTrainer module, which uses pre-existing conversational data from the ChatterBot 
corpus.
The chatbot was implemented as a web application using the Flask framework. The chatbot's responses 
were displayed in real-time on a web page, and users could interact with the chatbot by typing their 
questions into an input field.

## Results/Evaluation:
The chatbot was able to provide accurate and relevant responses to a wide range of questions related to 
IBA admissions, academics, and campus life. The responses were generated quickly and provided useful 
information to users.
However, if the question asked was not an exact match, the chatbot sometimes provided related 
questions instead of the desired answer. In these cases, users could ask the related question to receive 
the required output.

## Limitations:
One limitation of the chatbot is that it can only provide information that has been pre-programmed into 
it. While we have tried to include as much information as possible, there may be some questions that 
the chatbot is unable to answer.
Another limitation is that the chatbot's responses are based solely on the input it receives from the user. 
It does not take into account any additional contextual information that might be relevant to the 
question being asked.

## Future Directions:
There are several areas in which the chatbot could be improved in the future. One possibility is to 
incorporate natural language processing (NLP) techniques to improve the chatbot's ability to understand 
and interpret user input.
Another potential area for improvement is to expand the chatbot's knowledge base to include 
information about other universities or educational institutions in Pakistan. This would allow the chatbot 
to be more useful to a wider range of users.
Overall, this project demonstrates the potential for chatbots to provide useful and informative assistance 
to users in a variety of contexts. With continued development and improvement, chatbots have the 
potential to become an increasingly important tool for businesses and organizations looking to provide 
high-quality customer service and support.


## Steps to Run
pip install requirenments.txt <br>
run app_ChatIBA.py for UI based chatbot <br>
run chatIBA to run the chatbot in terminal <br>


## Terminal based Chatbot :
![Image of output](https://github.com/datamagic2020/Chatbot-for-Biginners/blob/main/chatbot.png)

## UI Based Chatbot :
![Image of output](https://github.com/datamagic2020/Chatbot-for-Biginners/blob/main/ui%20chatbot%20thumb.png)
