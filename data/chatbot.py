from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

bot = ChatBot("Canteen Auntie")
trainer = ListTrainer(bot)

trainer.train(["hi", "What you want ah?"])
trainer.train(["halal","Halal only indian and nasi padang"])
trainer.train(["indian" , "ah boy ah, indian store at north spine"])
trainer.train(["miniwok", "Miniwok at north spine lah"])
trainer.train(["nasi padang", "we at northspine second floor la"])
trainer.train(["chicken rice", "Aiyo! Chicken Rice also at north spine"])
trainer.train(["drink stall", "Of course, we have drink store at northspine"])
trainer.train(["which food nice", "North Spine food all nice nice one"])
trainer.train(["bye", "Must come back tomorrow hor!"])

def ChatBotReply(userText):
    return str(bot.get_response(userText))