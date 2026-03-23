
print("Simple Chatbot")
print("Type 'bye' to exit")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! How can I help you today?")

    elif "name" in user:
        print("Bot: I am a simple rule-based chatbot.")

    elif "how are you" in user:
        print("Bot: I am doing well. Thank you!")

    elif "course" in user:
        print("Bot: I can help answer simple questions related to studies.")

    elif "bye" in user:
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I didn't understand that.")