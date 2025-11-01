import ollama

def main():
    print("Welcome to Llama Chat! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        try:
            response = ollama.chat(model='llama3.2:3b', messages=[{'role': 'user', 'content': user_input}])
            print("Llama:", response['message']['content'])
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()