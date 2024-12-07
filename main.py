meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            }

word = input("ANG")

if word in meme_dict.keys():
    print(meme_dict[word]("tertawa terbahak bahak"))
else:
    print(meme_dict[word]("untuk menertawakan sesuatu"))
