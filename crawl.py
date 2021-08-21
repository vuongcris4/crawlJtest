from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

URLs = ["https://jtest.net/tu-vung-n1/chapter-1/section-1", "https://jtest.net/tu-vung-n1/chapter-1/section-2", "https://jtest.net/tu-vung-n1/chapter-1/section-3", "https://jtest.net/tu-vung-n1/chapter-1/section-4", "https://jtest.net/tu-vung-n1/chapter-1/section-5", "https://jtest.net/tu-vung-n1/chapter-2/section-1", "https://jtest.net/tu-vung-n1/chapter-2/section-2", "https://jtest.net/tu-vung-n1/chapter-2/section-3", "https://jtest.net/tu-vung-n1/chapter-2/section-4", "https://jtest.net/tu-vung-n1/chapter-2/section-5", "https://jtest.net/tu-vung-n1/chapter-3/section-1", "https://jtest.net/tu-vung-n1/chapter-3/section-2", "https://jtest.net/tu-vung-n1/chapter-3/section-3", "https://jtest.net/tu-vung-n1/chapter-3/section-4", "https://jtest.net/tu-vung-n1/chapter-3/section-5", "https://jtest.net/tu-vung-n1/chapter-4/section-1", "https://jtest.net/tu-vung-n1/chapter-4/section-2", "https://jtest.net/tu-vung-n1/chapter-4/section-3", "https://jtest.net/tu-vung-n1/chapter-4/section-4", "https://jtest.net/tu-vung-n1/chapter-4/section-5", "https://jtest.net/tu-vung-n1/chapter-5/section-1", "https://jtest.net/tu-vung-n1/chapter-5/section-2", "https://jtest.net/tu-vung-n1/chapter-5/section-3", "https://jtest.net/tu-vung-n1/chapter-5/section-4", "https://jtest.net/tu-vung-n1/chapter-5/section-5", "https://jtest.net/tu-vung-n1/chapter-6/section-1", "https://jtest.net/tu-vung-n1/chapter-6/section-2", "https://jtest.net/tu-vung-n1/chapter-6/section-3", "https://jtest.net/tu-vung-n1/chapter-6/section-4", "https://jtest.net/tu-vung-n1/chapter-6/section-5", "https://jtest.net/tu-vung-n1/chapter-7/section-1", "https://jtest.net/tu-vung-n1/chapter-7/section-2", "https://jtest.net/tu-vung-n1/chapter-7/section-3", "https://jtest.net/tu-vung-n1/chapter-7/section-4", "https://jtest.net/tu-vung-n1/chapter-7/section-5", "https://jtest.net/tu-vung-n1/chapter-8/section-1", "https://jtest.net/tu-vung-n1/chapter-8/section-2", "https://jtest.net/tu-vung-n1/chapter-8/section-3", "https://jtest.net/tu-vung-n1/chapter-8/section-4", "https://jtest.net/tu-vung-n1/chapter-8/section-5", "https://jtest.net/tu-vung-n1/chapter-9/section-1", "https://jtest.net/tu-vung-n1/chapter-9/section-2", "https://jtest.net/tu-vung-n1/chapter-9/section-3", "https://jtest.net/tu-vung-n1/chapter-9/section-4", "https://jtest.net/tu-vung-n1/chapter-9/section-5", "https://jtest.net/tu-vung-n1/chapter-10/section-1", "https://jtest.net/tu-vung-n1/chapter-10/section-2", "https://jtest.net/tu-vung-n1/chapter-10/section-3", "https://jtest.net/tu-vung-n1/chapter-10/section-4", "https://jtest.net/tu-vung-n1/chapter-10/section-5", "https://jtest.net/tu-vung-n1/chapter-11/section-1", "https://jtest.net/tu-vung-n1/chapter-11/section-2", "https://jtest.net/tu-vung-n1/chapter-11/section-3", "https://jtest.net/tu-vung-n1/chapter-11/section-4", "https://jtest.net/tu-vung-n1/chapter-11/section-5", "https://jtest.net/tu-vung-n1/chapter-12/section-1", "https://jtest.net/tu-vung-n1/chapter-12/section-2", "https://jtest.net/tu-vung-n1/chapter-12/section-3", "https://jtest.net/tu-vung-n1/chapter-12/section-4", "https://jtest.net/tu-vung-n1/chapter-12/section-5", "https://jtest.net/tu-vung-n1/chapter-13/section-1", "https://jtest.net/tu-vung-n1/chapter-13/section-2", "https://jtest.net/tu-vung-n1/chapter-13/section-3", "https://jtest.net/tu-vung-n1/chapter-13/section-4", "https://jtest.net/tu-vung-n1/chapter-13/section-5", "https://jtest.net/tu-vung-n1/chapter-14/section-1", "https://jtest.net/tu-vung-n1/chapter-14/section-2", "https://jtest.net/tu-vung-n1/chapter-14/section-3", "https://jtest.net/tu-vung-n1/chapter-14/section-4", "https://jtest.net/tu-vung-n1/chapter-14/section-5"
]

excelName = "3000 Từ vựng JLPT N1.xlsx"

list_name_final = []
list_content_final = []
list_audio_error=[]

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
    list_name_final.append(title)  # Bài 1: Gia đình
    print(title)

    # Get content
    table = soup.find_all('tr')
    del table[0]  # Xóa tr (heading) đầu tiên

    cotWord = []
    cotFurigana = []
    cotMeaningOfWord = []
    cotExample = []
    cotMeaningOfExample = []
    cotAudio = []

    for index, tr in enumerate(table):
        tdTuVung = tr.td  # Cột từ vụng
        wordAndFurigana = tdTuVung.find_all("small")
        if len(wordAndFurigana) == 2:
            word = wordAndFurigana[0].text  # word
            furigana = wordAndFurigana[1].text   # furigana
        elif len(wordAndFurigana) == 1:
            word = wordAndFurigana[0].text
            furigana = ""
        meaningOfWord = tdTuVung.span.text  # meaningOfWord
        tdViDu = tdTuVung.next_sibling.next_sibling  # Cột ví dụ
        example = tdViDu.p  # example
        meaningOfExample = tdViDu.span.text  # meaningOfExample

        audio = tr.th.button['value']   # Âm thanh
        # url = audio
        # extension = '{} _{}. {}.mp3'.format(title, index+1, word)
        # try:
        #     myfile = requests.get(url)
        #     fileName = 'D:/workspace/python/ta/crawlJtest/audio/'+extension
        #     open(fileName, 'wb').write(myfile.content)  # Save audio file
        # except:
        #     list_audio_error.append(url)
        #     print("error_audio" + extension)

        # audio = "[sound:"+extension+"]"  # write to excel

        cotWord.append(word)
        cotFurigana.append(furigana)
        cotMeaningOfWord.append(meaningOfWord)
        cotExample.append(example)
        cotMeaningOfExample.append(meaningOfExample)
        cotAudio.append(audio)

    df = pd.DataFrame()
    df["Word"] = cotWord
    df["Furigana"] = cotFurigana
    df["MeaningOfWord"] = cotMeaningOfWord
    df["Example"] = cotExample
    df["MeaningOfExample"] = cotMeaningOfExample
    df["Audio"] = cotAudio


    list_content_final.append(df)

# Write to excel
writer = pd.ExcelWriter(excelName, engine='xlsxwriter')

for index, sheet_name in enumerate(list_name_final):
    list_content_final[index].to_excel(
        writer, sheet_name=sheet_name[:31], index=False, header = None)

writer.save()
writer.close()

























"""
list_name_final[list_name_final.index("Bài 1. Trạng từ ①")]="Bài 1. Trạng từ"
list_name_final[list_name_final.index("Bài 2. Trạng từ ②")]="Bài 2. Trạng từ"
list_name_final[list_name_final.index("Bài 3. Trạng từ ③")]="Bài 3. Trạng từ"
list_name_final[list_name_final.index("Bài 4. Từ dễ nhầm lẫn ①")]="Bài 4. Từ dễ nhầm lẫn"
list_name_final[list_name_final.index("Bài 5. Từ dễ nhầm lẫn ②")]="Bài 5. Từ dễ nhầm lẫn"
list_name_final[list_name_final.index("Bài 1. Thành ngữ: Khuôn mặt")]="Bài 1. Thành ngữ _ Khuôn mặt"
list_name_final[list_name_final.index("Bài 2. Thành ngữ: Thân thể")]="Bài 2. Thành ngữ _ Thân thể"
list_name_final[list_name_final.index("Bài 3. Thành ngữ: Bộ phận khác")]="Bài 3. Thành ngữ _ Bộ phận khác"
"""