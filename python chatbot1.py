import requests

API_URL = "https://api-inference.huggingface.co/models/distilgpt2"
headers = {"Authorization": "Bearer YOUR_TOKEN"}  # ganti YOUR_TOKEN dengan token Anda

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def chat():
    print("AI Chatbot (DistilGPT-2 via API) - Ketik 'keluar' untuk berhenti")
    history = ""
    while True:
        user_input = input("Anda: ")
        if user_input.lower() == 'keluar':
            print("Sampai jumpa!")
            break
        
        history += user_input + "\n"
        data = query({"inputs": history, "max_length": 100, "temperature": 0.7})
        
        # Ambil teks hasil
        ai_response = data[0]['generated_text'].replace(history, "").strip()
        print("AI:", ai_response)
        history += ai_response + "\n"

if __name__ == "__main__":
    chat()