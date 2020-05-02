# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatterbot = ChatBot("Training Elle")
chatterbot.set_trainer(ListTrainer)

file = open("conversations.txt", "r")
conversation = file.read().splitlines()

chatterbot.train(conversation)

while True:
	question = input("Você: ")
	response = chatterbot.get_response(question)
	if float(response.confidence) > 0.5:
		print("Elle: ", response)
	else:
		print("Elle: Me desculpe, eu não sei.")