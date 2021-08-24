from bs4 import BeautifulSoup
import requests
import time
import genanki
import random
import os
# deckNameFinal = "3000 Từ vựng JLPT N1"
# URLs = ["https://jtest.net/tu-vung-n1/chapter-1/section-1", "https://jtest.net/tu-vung-n1/chapter-1/section-2", "https://jtest.net/tu-vung-n1/chapter-1/section-3", "https://jtest.net/tu-vung-n1/chapter-1/section-4", "https://jtest.net/tu-vung-n1/chapter-1/section-5", "https://jtest.net/tu-vung-n1/chapter-2/section-1", "https://jtest.net/tu-vung-n1/chapter-2/section-2", "https://jtest.net/tu-vung-n1/chapter-2/section-3", "https://jtest.net/tu-vung-n1/chapter-2/section-4", "https://jtest.net/tu-vung-n1/chapter-2/section-5", "https://jtest.net/tu-vung-n1/chapter-3/section-1", "https://jtest.net/tu-vung-n1/chapter-3/section-2", "https://jtest.net/tu-vung-n1/chapter-3/section-3", "https://jtest.net/tu-vung-n1/chapter-3/section-4", "https://jtest.net/tu-vung-n1/chapter-3/section-5", "https://jtest.net/tu-vung-n1/chapter-4/section-1", "https://jtest.net/tu-vung-n1/chapter-4/section-2", "https://jtest.net/tu-vung-n1/chapter-4/section-3", "https://jtest.net/tu-vung-n1/chapter-4/section-4", "https://jtest.net/tu-vung-n1/chapter-4/section-5", "https://jtest.net/tu-vung-n1/chapter-5/section-1", "https://jtest.net/tu-vung-n1/chapter-5/section-2", "https://jtest.net/tu-vung-n1/chapter-5/section-3", "https://jtest.net/tu-vung-n1/chapter-5/section-4", "https://jtest.net/tu-vung-n1/chapter-5/section-5", "https://jtest.net/tu-vung-n1/chapter-6/section-1", "https://jtest.net/tu-vung-n1/chapter-6/section-2", "https://jtest.net/tu-vung-n1/chapter-6/section-3", "https://jtest.net/tu-vung-n1/chapter-6/section-4", "https://jtest.net/tu-vung-n1/chapter-6/section-5", "https://jtest.net/tu-vung-n1/chapter-7/section-1", "https://jtest.net/tu-vung-n1/chapter-7/section-2", "https://jtest.net/tu-vung-n1/chapter-7/section-3", "https://jtest.net/tu-vung-n1/chapter-7/section-4", "https://jtest.net/tu-vung-n1/chapter-7/section-5", "https://jtest.net/tu-vung-n1/chapter-8/section-1", "https://jtest.net/tu-vung-n1/chapter-8/section-2", "https://jtest.net/tu-vung-n1/chapter-8/section-3", "https://jtest.net/tu-vung-n1/chapter-8/section-4", "https://jtest.net/tu-vung-n1/chapter-8/section-5", "https://jtest.net/tu-vung-n1/chapter-9/section-1", "https://jtest.net/tu-vung-n1/chapter-9/section-2", "https://jtest.net/tu-vung-n1/chapter-9/section-3", "https://jtest.net/tu-vung-n1/chapter-9/section-4", "https://jtest.net/tu-vung-n1/chapter-9/section-5", "https://jtest.net/tu-vung-n1/chapter-10/section-1", "https://jtest.net/tu-vung-n1/chapter-10/section-2", "https://jtest.net/tu-vung-n1/chapter-10/section-3", "https://jtest.net/tu-vung-n1/chapter-10/section-4", "https://jtest.net/tu-vung-n1/chapter-10/section-5", "https://jtest.net/tu-vung-n1/chapter-11/section-1", "https://jtest.net/tu-vung-n1/chapter-11/section-2", "https://jtest.net/tu-vung-n1/chapter-11/section-3", "https://jtest.net/tu-vung-n1/chapter-11/section-4", "https://jtest.net/tu-vung-n1/chapter-11/section-5", "https://jtest.net/tu-vung-n1/chapter-12/section-1", "https://jtest.net/tu-vung-n1/chapter-12/section-2", "https://jtest.net/tu-vung-n1/chapter-12/section-3", "https://jtest.net/tu-vung-n1/chapter-12/section-4", "https://jtest.net/tu-vung-n1/chapter-12/section-5", "https://jtest.net/tu-vung-n1/chapter-13/section-1", "https://jtest.net/tu-vung-n1/chapter-13/section-2", "https://jtest.net/tu-vung-n1/chapter-13/section-3", "https://jtest.net/tu-vung-n1/chapter-13/section-4", "https://jtest.net/tu-vung-n1/chapter-13/section-5", "https://jtest.net/tu-vung-n1/chapter-14/section-1", "https://jtest.net/tu-vung-n1/chapter-14/section-2", "https://jtest.net/tu-vung-n1/chapter-14/section-3", "https://jtest.net/tu-vung-n1/chapter-14/section-4", "https://jtest.net/tu-vung-n1/chapter-14/section-5"
# ]
# chapters = ["Chapter 01: Mối quan hệ giữa người với người", "Chapter 02: Cuộc sống", "Chapter 03: Ở nhà", "Chapter 04: Ở trường", "Chapter 05: Ở công ty", "Chapter 06: Thành phố của tôi", "Chapter 07: Sức khỏe", "Chapter 08: Sở thích", "Chapter 09: Thế giới", "Chapter 10: Thiên nhiên", "Chapter 11: Tin tức", "Chapter 12: Tình trạng - Hình ảnh", "Chapter 13: Các cách diễn đạt dễ bị sai ①", "Chapter 14: Các cách diễn đạt dễ bị sai ②", ]

deckNameFinal = "2500 Từ vựng JLPT N2"
URLs = ["https://jtest.net/tu-vung-n2/chapter-1/section-1", "https://jtest.net/tu-vung-n2/chapter-1/section-2", "https://jtest.net/tu-vung-n2/chapter-1/section-3", "https://jtest.net/tu-vung-n2/chapter-1/section-4", "https://jtest.net/tu-vung-n2/chapter-1/section-5", "https://jtest.net/tu-vung-n2/chapter-2/section-1", "https://jtest.net/tu-vung-n2/chapter-2/section-2", "https://jtest.net/tu-vung-n2/chapter-2/section-3", "https://jtest.net/tu-vung-n2/chapter-2/section-4", "https://jtest.net/tu-vung-n2/chapter-2/section-5", "https://jtest.net/tu-vung-n2/chapter-3/section-1", "https://jtest.net/tu-vung-n2/chapter-3/section-2", "https://jtest.net/tu-vung-n2/chapter-3/section-3", "https://jtest.net/tu-vung-n2/chapter-3/section-4", "https://jtest.net/tu-vung-n2/chapter-3/section-5", "https://jtest.net/tu-vung-n2/chapter-4/section-1", "https://jtest.net/tu-vung-n2/chapter-4/section-2", "https://jtest.net/tu-vung-n2/chapter-4/section-3", "https://jtest.net/tu-vung-n2/chapter-4/section-4", "https://jtest.net/tu-vung-n2/chapter-4/section-5", "https://jtest.net/tu-vung-n2/chapter-5/section-1", "https://jtest.net/tu-vung-n2/chapter-5/section-2", "https://jtest.net/tu-vung-n2/chapter-5/section-3", "https://jtest.net/tu-vung-n2/chapter-5/section-4", "https://jtest.net/tu-vung-n2/chapter-5/section-5", "https://jtest.net/tu-vung-n2/chapter-6/section-1", "https://jtest.net/tu-vung-n2/chapter-6/section-2", "https://jtest.net/tu-vung-n2/chapter-6/section-3", "https://jtest.net/tu-vung-n2/chapter-6/section-4", "https://jtest.net/tu-vung-n2/chapter-6/section-5", "https://jtest.net/tu-vung-n2/chapter-7/section-1", "https://jtest.net/tu-vung-n2/chapter-7/section-2", "https://jtest.net/tu-vung-n2/chapter-7/section-3", "https://jtest.net/tu-vung-n2/chapter-7/section-4", "https://jtest.net/tu-vung-n2/chapter-7/section-5", "https://jtest.net/tu-vung-n2/chapter-8/section-1", "https://jtest.net/tu-vung-n2/chapter-8/section-2", "https://jtest.net/tu-vung-n2/chapter-8/section-3", "https://jtest.net/tu-vung-n2/chapter-8/section-4", "https://jtest.net/tu-vung-n2/chapter-8/section-5", "https://jtest.net/tu-vung-n2/chapter-9/section-1", "https://jtest.net/tu-vung-n2/chapter-9/section-2", "https://jtest.net/tu-vung-n2/chapter-9/section-3", "https://jtest.net/tu-vung-n2/chapter-9/section-4", "https://jtest.net/tu-vung-n2/chapter-9/section-5", "https://jtest.net/tu-vung-n2/chapter-10/section-1", "https://jtest.net/tu-vung-n2/chapter-10/section-2", "https://jtest.net/tu-vung-n2/chapter-10/section-3", "https://jtest.net/tu-vung-n2/chapter-10/section-4", "https://jtest.net/tu-vung-n2/chapter-10/section-5", "https://jtest.net/tu-vung-n2/chapter-11/section-1", "https://jtest.net/tu-vung-n2/chapter-11/section-2", "https://jtest.net/tu-vung-n2/chapter-11/section-3", "https://jtest.net/tu-vung-n2/chapter-11/section-4", "https://jtest.net/tu-vung-n2/chapter-11/section-5", "https://jtest.net/tu-vung-n2/chapter-12/section-1", "https://jtest.net/tu-vung-n2/chapter-12/section-2", "https://jtest.net/tu-vung-n2/chapter-12/section-3", "https://jtest.net/tu-vung-n2/chapter-12/section-4", "https://jtest.net/tu-vung-n2/chapter-12/section-5", 
]
chapters = ["Chapter 01: Quan hệ giữa người với người", "Chapter 02: Đời sống", "Chapter 03: Ở nhà", "Chapter 04: Phố xá", "Chapter 05: Tại trường học", "Chapter 06: Tại công ty", "Chapter 07: Yêu thích", "Chapter 08: Thiên nhiên - Thư giãn", "Chapter 09: Vì sức khỏe", "Chapter 10: Tin tức", "Chapter 11: Trạng thái - Hình ảnh", "Chapter 12: Cách nói dễ nhầm lẫn", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 
]

# _________________________________ Tạo Model Field Cho deck Anki _________________________________________________________

wd = os.path.join(os.getcwd(),'crawlJtest','card')
with open(os.path.join(wd, 'front.html'), encoding='utf-8') as f:
    frontHtml = f.read()
    f.close()
with open(os.path.join(wd, 'back.html'), encoding='utf-8') as f:
    backHtml = f.read()
    f.close()
with open(os.path.join(wd, 'style.css'), encoding='utf-8') as f:
    cssLoaded = f.read()
    f.close()

my_model = genanki.Model(
    112252932,
    'Jtest Vocabulary',
    model_type=genanki.Model.FRONT_BACK,
    fields = [                                   #["Word", "Furigana", "MeaningOfWord", "Example", "MeaningOfExample", "Audio"]
        {'name': 'Word'},
        {'name': 'Furigana'},
        {'name': 'MeaningOfWord'},
        {'name': 'Example'},
        {'name': 'MeaningOfExample'},
        {'name': 'Audio'},
    ],
    templates=[
      {
        'name': 'Card 1',
        'qfmt': frontHtml,
        'afmt': backHtml,
      },
    ],
    css=cssLoaded
)

my_deck = []

def createDeck(deckName):
    my_deck.append(
      genanki.Deck(
      deck_id= int( str(int.from_bytes(deckName.encode(), 'little'))[:18] ),
      name=deckName,
      )
    )

def addNote(fields):
    my_note = genanki.Note(
    model= my_model,
    fields = fields, guid= (random.randrange(1 << 30, 1 << 31)))
    my_deck[-1].add_note(my_note)

def saveAnkiPackage(packageName):
    genanki.Package(my_deck).write_to_file(packageName + '.apkg')

# ___________________________________ Bắt đầu Crawl ___________________________

countNote=0
for urlInd, URL in enumerate(URLs):
    page = requests.get(URL)
    print(page.status_code)
    time.sleep(0.3)
    soup = BeautifulSoup(page.content, 'lxml')

    # Get title
    title_Index = soup.p.find_all('span')[-1].text  # Bài 1
    title_Name = soup.head.title.text  # Gia đình
    title_Name = title_Name[:title_Name.find(' -')]
    title = title_Index + ". " + title_Name
    # print(title)

    # Get content
    table = soup.find_all('tr')
    del table[0]  # Xóa tr (heading) đầu tiên

    if ("Bài 1") in title:
        chapter = chapters.pop(0)

    deckName = deckNameFinal+"::"+chapter+"::"+title
    print(deckName)
    createDeck(deckName=deckName)   # _________ Tạo Deck

    for index, tr in enumerate(table):
        tdTuVung = tr.td  # Cột từ vụng
        wordAndFurigana = tdTuVung.find_all("small")
        if len(wordAndFurigana) == 2:
            word = wordAndFurigana[0].text  # word
            furigana = wordAndFurigana[1].text   # furigana
        elif len(wordAndFurigana) == 1:
            word = wordAndFurigana[0].text
            furigana = " "
        meaningOfWord = tdTuVung.span.text+" "  # meaningOfWord     Cộng thêm dấu cách ddeer đề phòng rỗng
        tdViDu = tdTuVung.next_sibling.next_sibling  # Cột ví dụ
        example = tdViDu.p  # example
        meaningOfExample = tdViDu.span.text+" "  # meaningOfExample

        audio = tr.th.button['value']+" "   # Âm thanh

        addNote([word, furigana, meaningOfWord, str(example), meaningOfExample, audio])       # ___________ Add Note vào Deck
        countNote +=1

saveAnkiPackage(deckNameFinal)  # ___________ DONE!
print("Tổng số Note: {}".format(countNote))
