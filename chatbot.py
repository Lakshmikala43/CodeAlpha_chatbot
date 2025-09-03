def chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. Say 'bye' to exit.")
    
    while True:
        # Get user input and convert to lowercase for case-insensitive matching
        user_input = input("You: ").lower()
        
        # Check for predefined inputs and respond
        if "hello" in user_input:
            print("Chatbot: Hi!")
        elif "how are you" in user_input:
            print("Chatbot: I'm fine, thanks!")
        elif "bye" in user_input:
            print("Chatbot: Goodbye!")
            break  # Exit the loop
        else:
            # Default response for unrecognized input
            print("Chatbot: I don't understand. Try saying 'hello', 'how are you', or 'bye'.")

# Start the chatbot
if __name__ == "__main__":
    chatbot()