import requests

def payload(bot_token, chat_id, text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, data=payload)
    return response.json()

if __name__ == "__main__":
    try:
        # Ambil token dan chat_id dari user
        bot_token = input("Bot Token: ")
        chat_id = input("Chat ID: ")
        
        # Validasi token dan chat_id
        if not bot_token or not chat_id:
            raise ValueError("Bot token dan Chat ID tidak boleh kosong!")

        # Detail Pesan Yang Ingin Dikirim
        jumlah = int(input("Berapa kali pesan ingin dikirim? "))
        pesan = input("Masukkan isi pesan: ")

        print("\nSending pesan...\n")
        for i in range(jumlah):
            result = payload(bot_token, chat_id, pesan)
            if result['ok']:
                print(f"[{i+1}] Berhasil ! Message ID: {result['result']['message_id']}")
            else:
                print(f"[{i+1}] Gagal !: {result.get('description', 'Unknown error')}")
                
    except ValueError as ve:
        print("Error: Masukkan angka yang valid untuk jumlah pesan!")
    except Exception as e:
        print("Terjadi error:", str(e))
