from transformers import pipeline, set_seed

generator = pipeline('text-generation', model='distilgpt2')
set_seed(42)

def chat():
    print("AI Chatbot (DistilGPT-2) - Ketik 'keluar' untuk berhenti")
    history = ""
    while True:
        user_input = input("Anda: ")
        if user_input.lower() == 'keluar':
            print("Sampai jumpa!")
            break
        
        history += user_input + "\n"
        
        responses = generator(history, max_length=100, num_return_sequences=1, temperature=0.7)
        ai_response = responses[0]['generated_text'].replace(history, "").strip()
        
        print("AI:", ai_response)
        history += ai_response + "\n"

if __name__ == "__main__":
    chat()