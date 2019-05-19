from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import UbuntuCorpusTrainer
from chatterbot.logic import logic_adapter


chatbot = ChatBot('Divya',
storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
                  logic_adapters=['chatterbot.logic.BestMatch', 'chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.TimeLogicAdapter'],
                  input_adapter='chatterbot.input.TerminalAdapter',
                  output_adapter='chatterbot.output.TerminalAdapter',
                  database='netdb'
                  )

chatbot.set_trainer(ListTrainer)
chatbot.train(['Hi', 'Hello'])

while True:
    try:
        response = chatbot.get_response(None)
    except(KeyboardInterrupt, EOFError, TimeoutError):
        break

print("Bye!")
