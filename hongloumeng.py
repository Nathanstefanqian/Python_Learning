#Task1 分割章回
import re

f=open('data/红楼梦.txt','r',encoding='utf-8')
s=f.read()
lst_chapter=[]
chapter= re.findall("第[\u4E00-\u9FA5]+回",s) #返回第和回之间的内容
for x in chapter:
    if x not in lst_chapter and len(x)<=5:
         lst_chapter.append(x)
print(lst_chapter)
lst_start_chapterindex=[]
for x in lst_chapter:
    lst_start_chapterindex.append(s.index(x))
print(lst_start_chapterindex)
lst_end_chapterindex =lst_start_chapterindex[1:]+[len(s)]
lst_chapterindex=list(zip(lst_start_chapterindex,lst_end_chapterindex))
print(lst_chapterindex)

#Task2 计算每回苦笑悲喜次数
cnt_laugh=[]
cnt_cry=[]
for i in range(120):
    start=lst_chapterindex[i][0]
    end=lst_chapterindex[i][1]
    cnt_laugh.append(s[start:end].count("笑")+s[start:end].count('喜'))
    cnt_cry.append(s[start:end].count("哭")+s[start:end].count("悲"))
print('快乐的次数'+str(cnt_laugh))
print('悲伤的次数'+str(cnt_cry))

#Task3 计算每回刘姥姥出现的次数
cnt_liulaolao=[]
for i in range(120):
    start=lst_chapterindex[i][0]
    end=lst_chapterindex[i][1]
    cnt_liulaolao.append(s[start:end].count('刘姥姥'))
print('每回刘姥姥出现的次数'+str(cnt_liulaolao))

