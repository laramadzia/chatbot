# Description: This is a chatbot program

# There are broadly two variants of chatbots: Rule-Based and Self learning.
# Rule-based approach, a bot answers questions based on some rules on which it is trained on
# Self learning bots are the ones that use some Machine Learning-based approach to chat

# import libraries
from nltk.chat.util import Chat, reflections

# Pairs is a list of patterns and responses.
pairs = [
    [
        r"TAK",
        ["Ekstra. Podaj mi proszę swoj NIK w celu werfyikacji", ]
    ],
    [
        r"1234567890",
        ["Dzieki. Na co chcesz kredyt?", ],
    ],
    [
        r"nie",
        ["Na co chcesz kredyt?", ]
    ],
    [
        r"rower",
        ["Idealny bedzie kredyt gotowkoy. Cchesz zawnioskowac?", ]
    ],
[
        r"tak",
        ["Zatem chodz wypelnimy formaulrz", ]
    ],
]

# This is a dictionary that contains a set of input values and its corresponding output values.
# It is an optional dictionary that you can use unless you want to use regular expressions.
reflections


# default message at the start of chat
print(
    "Cześć, jestem doradcą kredytowym. Pomogę Ci w wyborze produktu oraz złożeniu wniosku. \nCzy jesteś klientem mBanku? ")

# Create Chat Bot
chat = Chat(pairs, reflections)

# chat._substitute('i am a programmer') #uncomment this line to see reflections example in action

# Start conversation
chat.converse()