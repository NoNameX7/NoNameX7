from transformers import pipeline, set_seed

# Inisialisasi model AI (gunakan model kecil untuk hemat RAM)
chatbot = pipeline('text-generation', model='gpt2-small')  # Ganti 'gpt2-small' jika model tidak tersedia

def main():
    set_seed(42)
    print("\nAI Chatbot (Tekan Ctrl+C untuk keluar)")
    while True:
        user_input = input("Anda: ")
        if user_input.lower() in ["keluar", "exit"]:
            break
        
        # Generate respons AI
        response = chatbot(
            user_input,
            max_length=50,
            num_return_sequences=1,
            temperature=0.7,
            pad_token_id=50256
        )
        
        print(f"AI: {response[0]['generated_text']}\n")

if __name__ == "__main__":
    main()