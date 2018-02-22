from chatterbot import ChatBot


chatbot = ChatBot('Divya',
                  storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
                  logic_adapters=['chatterbot.logic.BestMatch', 'chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.TimeLogicAdapter'],
                  input_adapter='chatterbot.input.TerminalAdapter',
                  output_adapter='chatterbot.output.TerminalAdapter',
                  database='chatterbotdb',  # Enter database name here (default: chatterbot-database)
                  )


while True:
    try:
        response = chatbot.get_response(None)
    except(KeyboardInterrupt, EOFError, TimeoutError):
        break

print("Bye!")
