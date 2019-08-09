from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import chatterbot_corpus
from chatterbot import filters

chatbot = ChatBot('Freeman',
                  logic_adapters=[
                      'chatterbot.logic.MathematicalEvaluation',
                      'chatterbot.logic.TimeLogicAdapter'
                  ]
                  )

conversation = [
    "你好",
    "你好啊!",
    "你好嗎?",
    "我很好",
    "聽上去不錯",
    "謝謝.",
    "不客氣"
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

while 1:
    try:
        a = input()
        r = chatbot.get_response(a)
        print(r)
    except KeyboardInterrupt:
        break