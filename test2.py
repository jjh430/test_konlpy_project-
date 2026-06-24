# test2.py
# konlpy 모듈에서 제공하는 메소드의 매개변수 사용 테스트

from konlpy.tag import Okt ## 클래스 임포트
from konlpy.utils import read_txt # 함수 임포트

# 형태소 분석 + 태깅 : pos(), morphs(), nouns() 등에 사용하는 매개변수들
# stem : 형태소의 원형을 찾아서 반환해 줌
# norm : 형태소를 깔끔하게 정리해 주고, 불필요한 데이터 지움

okt = Okt()

# data 폴더에서 텍스트 파일을 읽어와서 분석에 사용하기
text = read_txt('./data/sample.txt', encoding='utf-8')

print('norm = True, stem = True-----------------')
mal_list = okt.pos(text,norm=True,stem=True)
print(mal_list)

print('norm = False, stem = False---------------------')
mal_list = okt.pos(text,norm=False,stem=False)
print(mal_list)

# 명사들을 수집해서 반복되는 명사를 count 함
word_dic = {}

for word in mal_list:
    # print(word)
    if word[1] == 'Noun':
        if not word[0] in word_dic: #
            word_dic[word[0]] = 0 # {단어:0} 저장
        # if -------------------------------
        word_dic[word[0]] += 1 # 해당 단어가 있다면, 단어(키)의 값을 1 증가 시킴

# print(word_dic)

# 단어 빈도수에 대해 내림차순정렬 처리
keys = sorted(word_dic.items(), key=lambda x: x[1], reverse=True)

# 50개까지 정렬 결과 출력
# for word, count in keys[:50]:
    # print(f'{word}: {count}',end=',')

#wordcloud (말구름) 차트 만들기
#wordcloud 패키지 설치하고 사용함 = > matplotlib 도 자동 같이 설치됨

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# wordcloud = WordCloud(font_path='./fonts/malgunsl.ttf',
#                       background_color='white',
#                       width=1000,
#                       height=800
#                         ).generate(text)
# wordcloud.generate_from_frequencies(word_dic)
#
# plt.figure(figsize = (10,10))
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.show()

# wordcloud 모양을 원하는 도형 모양으로 변경하기
# mask 옵션 사용함
from PIL import Image # 이미지 파일 열기용 클래스
import numpy as np # 배열 다루는 모듈

img = Image.open('./images/heart.png')
imgArray = np.array(img) # 이미지의 각 픽셀을 숫자 배열로 변환함

wordcloud = WordCloud(
    font_path='./font/malgunsl.ttf',
    background_color='white',
    width=400,
    height=400,
    max_words=100,       # 빈도수가 가장 큰 글자의 크기 지정
    mask=imgArray,       # 사용하고자 하는 이미지의 수치 배열
)

wordcloud.generate_from_frequencies(word_dic)

plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()