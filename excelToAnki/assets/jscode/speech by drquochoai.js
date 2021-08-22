/*
Thêm audio tag vào trong html
1. Nguồn audio, US sound: http://dict.youdao.com/dictvoice?type=0&audio=
2. Nội dung đọc là nội dung của front
*/
mp3= "https://dict.youdao.com/dictvoice?type=0&audio="
auTag = '<audio controls autoplay>' +
'<source src="_mp3" type="audio/mp3">' +
'Trình duyệt không hỗ trợ audio.' +
'</audio>'
content = mp3 + $(".front").text()
                    .replace(/\[.*\]/g, "")
                    .replace("autocloze", "").trim()
setTimeout(() => {
    $(".footer").before( auTag.replace("_mp3", content) )
}, 300);