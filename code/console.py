import ai
chat = ai.AI(username="kazenoko", model=2, tmodel="gpt-3.5-turbo")
tts = ai.tts(model=chat.getModel())
while 1:
    response = chat.ask(input("You: "))
    print(f"{chat.getModel()}: {response}")
    tts.speak(message=response,mood=chat.getMood())