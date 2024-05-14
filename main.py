meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "AFK": "Klavyeden uzakta",
            "GG": "Güzel oyundu",
            "WP": "İyi Oynadık",
            "F2P": "Parasız oyuncu",
            "NT": "Iyi denedin",
            "FPS": "Saniyedeki kare sayısı",
            "GLHF": "İyi Şanslar iyi eğlenceler",
            }
            


for i in range(5):
    kelime = input("Kelime girin")

    
    if kelime in meme_dict.keys():
        print(meme_dict[kelime])
    
    else:
        print("Kelime listede yok...")
