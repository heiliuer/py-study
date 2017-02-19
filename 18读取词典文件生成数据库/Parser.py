import re
import sqlite3
from xpinyin import Pinyin


def handle_line(line):
    # print(line)
    line_raw = line
    if line.startswith("【"):
        # 获取词语
        cis = re.findall('【(.*?)】', line)
        ci = cis[0]
        print(ci)
        line = line.replace("【" + ci + "】", "", 1)

        # 获取拼音
        pinyins = re.findall('([a-zA-Z\u0020-\u2459\u2488\u25f0]+)', line)
        pinyin = ''
        if len(pinyins) > 0:
            pinyin = pinyins[0]
            print(pinyin)
            line = line.replace(pinyin, "", 1)

        yisi = line

        yisi_list = re.split('[\u2460-\u2487]', line)
        if len(yisi_list) > 1:
            yisi = "###".join(yisi_list)
        print(yisi)

        return {"ci": ci, "pinyin": pinyin, "yisi": yisi}


# '【阿尔茨海默病】ā’ěrcíhǎimòbìnɡ名老年性痴呆的一种，多发生于中年或老年的早期，因德国医生阿尔茨海默（AloisAlzheimer）最先描述而得名。症状是短期记忆丧失，认识能力退化，逐渐变得呆傻，以至生活完全不能自理。
# [a-zà-ǜ]

if __name__ == "__main1__":
    handle_line(
        "")

if __name__ == "__main__":
    file = open("dic.txt", "r", encoding="utf_16")
    dura_index = 1
    dura = 23
    total = dura * dura_index
    count = total

    conn = sqlite3.connect("test2.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS dic ")
    cursor.execute('CREATE TABLE IF NOT EXISTS dic ('
                   'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                   'ci VARCHAR(30),'
                   'py VARCHAR(30),'
                   'pinyin VARCHAR(30),'
                   'yisi VARCHAR(30),'
                   'status INT  DEFAULT  0'
                   ')')

    py = Pinyin()

    for line in file:
        count -= 1
        print("count:", count, line)
        # if 0 < count < dura:
        result = handle_line(line)
        if result is not None:
            pyG = py.get_pinyin(result["ci"], '')
            cursor.execute(
                'INSERT INTO dic (ci,py,pinyin,yisi) VALUES (?,?,?,?)',
                (result["ci"], pyG, result["pinyin"], result["yisi"]))

            # if count <= 0:
            #     break
    cursor.close()
    conn.commit()
