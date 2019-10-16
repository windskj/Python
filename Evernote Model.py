# 抽取信息
MyArticle = open('c:\\Users\\Administrator\\Desktop\\MyArticle.txt', 'r', encoding="UTF-8")
Article = MyArticle.readlines()
Title = Article[0]
Tag = Article[1]
Date = Article[2]
Abstract = Article[3]
Tag = ',_'.join(Tag.split(','))
# 创建以日期命名文件
FileName = Date.replace("\n", '') + '.txt'
EvernoteArticle = open('c:\\Users\\Administrator\\Desktop\\' +
                       FileName, 'w', encoding="UTF-8")  
# XMl语言写入
EvernoteArticle.write('''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE en-export SYSTEM "http://xml.evernote.com/pub/evernote-export2.dtd">
<en-export export-date="''' + Date + '''T165032Z" application="Evernote/Windows" version="6.x">
    <note>
        <title>''' + Title + '''</title>
        <content>
            <![CDATA[
            <?xml version="1.0" encoding="UTF-8"?>
            <!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">
            <en-note>
                <div>
                    <div style="margin-top: 1em; margin-bottom: 1em; text-align: justify;">
                        <span style="font-size: 14pt; color: rgb(0, 136, 167); font-weight: bold; font-family: &quot;Tw Cen MT&quot;;-en-paragraph:true;">Keywords</span>
                        <span style="font-size: 14pt; color: rgb(0, 136, 167);-en-paragraph:true;">&nbsp;</span>''')
if Tag != '':
    EvernoteArticle.write(
        '<span style="font-size: 10pt;-en-paragraph:true;">_' + Tag + '，</span>')
EvernoteArticle.write('''<br/>
                    </div>
                    <div style="margin-top: 1em; margin-bottom: 1em; text-align: justify;">
                        <span style="font-size: 14pt; color: rgb(0, 136, 167); font-weight: bold; font-family: &quot;Tw Cen MT&quot;;-en-paragraph:true;">Abstract</span>
                    </div>
                    <div style="margin-top: 1em; margin-bottom: 1em; text-align: justify;">
                        <span style="font-size: 10pt; font-family: &quot;Tw Cen MT&quot;;-en-paragraph:true;">''' + Abstract + '''</span>
                        <br/>
                    </div>''')
for line in range(4, len(Article)):
    if Article[line][0] == '!':
        EvernoteArticle.write('''<h1 style="text-align: justify;">
                            <span style="font-size: 20pt; color: rgb(215, 19, 63); font-family: 华文中宋;">''' + Article[line].lstrip('!') + '''</span>
                        </h1>''')
    elif Article[line][0] == '@':
        EvernoteArticle.write('''<h2>
                <span style="font-size: 14pt; color: rgb(0, 136, 167); font-family: 微软雅黑;">''' + Article[line].lstrip('@') + '''</span>
                </h2>''')
    else:
        EvernoteArticle.write('''<div style="min-height: 16pt; text-align: left;">
            <span style="min-height: 16pt; font-size: 12pt;">
            <span style="font-size: 12pt; font-family: 华文中宋;">''' + Article[line] + '''</span>
            </span>
                </div>''')
EvernoteArticle.write('''                </div></en-note>]]>
            </content>
            <created>''' + Date + '''T013121Z</created>
            <updated>''' + Date + '''T085945Z</updated>
            <tag>Doing</tag>
            <note-attributes>
                <source>mobile.android</source>
            </note-attributes>
        </note>
    </en-export>''')
# 保存数据
MyArticle.close()
EvernoteArticle.close()
# 重命名文件
import os
NewName = FileName.rstrip('txt') + 'enex'
os.rename('c:\\Users\\Administrator\\Desktop\\' + FileName,
          'c:\\Users\\Administrator\\Desktop\\Evernote\\' + NewName)
print('Mission complete'.upper().ljust(100, '>'))
