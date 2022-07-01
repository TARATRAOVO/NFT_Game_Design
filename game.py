from matplotlib.font_manager import json_load
from nbformat import read
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Image
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import sys,time

import json
from tqdm import tqdm


def printer(text):
    sys.stdout.write("\r " + " " * 60 + "\r") # /r 光标回到行首
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.flush() #把缓冲区全部输出
    sys.stdout.write('\n')

def write_pdf():

    # 注册字体

    pdfmetrics.registerFont(TTFont("SimSun", "SimSun.ttf"))

    c = Canvas("demo1.pdf")

    image_url = '/Users/administrator/work-collection/NFT_Game_Design/lion.jpeg'
    
    image = Image(image_url)
    image_height = image.drawHeight
    image_width = image.drawWidth

    c.drawImage(image_url, 10, 700, image_width, image_height, 'auto')
    
    
    # 应用注册的字体

    c.setFont("SimSun", 14)
    c.drawString(0, 650, "普通毕业：生物学研究生【可选装饰：白色实验服】")
    c.drawString(0, 600, "成就：")
    c.drawString(0, 550, "普通：无聊的恋爱【可选装饰：爱心】")
    c.drawString(0, 500, "稀有：图书馆警察【可选装饰：黄心】")
    c.drawString(0, 450, "收集：《恋文的技术》【可选装饰：书】")
    
    

    c.save()

f = open('game_start.json')
f = f.read()
f = json.loads(f)
print(f)

print('分析行径......')
for i in tqdm(range(100)):
    time.sleep(0.01)
    
print('生成数值......')
for i in tqdm(range(100)):
    time.sleep(0.001)
    


print('===================')
printer('大一')
input('图书馆')


printer('上学期第二周周四下午，像往常一样来到最喜欢的XXX图书馆')


printer('对着上届同学的作业本抄完了本周的生物数学作业')

printer('今天图书馆的氛围不太一般.......')

input('灵视--CHECK')
for i in tqdm(range(100)):
    time.sleep(0.001)
input('SUCCESS!')

printer('收到加入图书馆警察的邀请，并且加入了图书馆警察')

printer('图书馆警察是隶属于图书馆的神秘机关，专门负责追讨逾期书籍')

printer('需要应对各种各样的难以应付的人物')

printer('图书馆警察手段阴险狡诈，无所不用其极，了解的人无不敬而远之，但是普通人一般接触不到他们')

print('===================')
printer('大二')
input('学院球队选拔————足球队')

printer('参加球队选拔')
input("运动--CHECK")
for i in tqdm(range(100)):
    time.sleep(0.001)
input('SUCCESS!')
printer('凭借较好的球感以及相对扎实的技术加入了球队')

printer('参加球队的第一次训练赛')
input("体能--CHECK")
for i in tqdm(range(100)):
    time.sleep(0.001)
input('FAIL!')
printer('刚上场15分钟就像被曝晒了15分钟的🐟')
printer('退出了球队')

print('===================')
printer('大二')
input('图书馆警察任务')

printer('图书馆警察策略部门通过伪装成美少女与逾期者通信，欺骗逾期者携带逾期书籍赴约')

printer('傍晚的思源湖边，埋伏在阴影中的图书馆警察将逾期者团团围住')

printer('逾期者向你冲来，妄图从你这里突破包围')
input('体能--CHECK')
for i in tqdm(range(100)):
    time.sleep(0.001)
input('SUCESS!')
printer('你成功拦住了他：瘦弱的阿宅')
printer('立功')

print('===================')
printer('大三')
input('《恋文的技术》')

printer('传说此书潜藏着如何使用文字解决世界上最大难题的秘密，由于力量过于强大，被图书馆警察高层定为“限制借出”')
printer('好书！')

input('灵视--CHECK')
for i in tqdm(range(100)):
    time.sleep(0.001)
input('SUCCESS!')

printer('此书在从逾期者追回后又马上被标记为“遗失”')
printer('图书馆警察高层下达了死命令，一定要追回书籍')

input('智力--CHECK')
for i in tqdm(range(100)):
    time.sleep(0.001)
input('SEUCESS!')

printer('《恋文的技术》成为图书馆警察之耻')
printer('事件逐渐平息')

input('智力--CHECK')
for i in tqdm(range(100)):
    time.sleep(0.001)
input('SEUCESS!')

printer("你在恋文失窃案平息后退出了图书馆警察")

printer('傍晚的思源湖边，与你见面的笔友是图书馆警察策略部门的后辈明石')
printer('情书的技术：“诀窍就是不要当情书写”')
printer('没有什么比有情人终成眷属的爱情更不值一提的了')


print('======毕业======')
printer('毕业')
input('经过了多年的努力，你最终......')
printer('成为了：')
input('生物学研究生')

print('======END======')
input('生成毕业结果......')
print('生成形象......')
for i in tqdm(range(100)):
    time.sleep(0.01)
print('生成成就......')
for i in tqdm(range(100)):
    time.sleep(0.001)
print('SUCESS!')
write_pdf()