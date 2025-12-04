def chatbot():
    print("🤖 Welcome to CodeAlpha Chatbot! ")

    while True:
        user_input = input("You: ").lower()
   
        if user_input == "hello":
            print("Bot: Hi!")
        elif user_input == "how are you":
            print("Bot: I am fine Thanks!")
        elif user_input == "bye":
            print("GoodBye, Have a great day! ")
            break
        else:
            print("I dont understand")
       
chatbot()

 


