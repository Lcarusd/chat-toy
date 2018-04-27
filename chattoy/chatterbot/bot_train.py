# coding: utf-8

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import hug


deepThought = ChatBot("deepThought")
deepThought.set_trainer(ChatterBotCorpusTrainer)
deepThought.train("chatterbot.corpus.chinese")


@hug.get()
def get_response(user_input):
    response = deepThought.get_response(user_input).text
    return {"response": response}
