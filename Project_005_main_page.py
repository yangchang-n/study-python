# --------------------------------------------------
# program start

print('program execution succeeded')

# --------------------------------------------------
# module import

import pandas as pd
import numpy as np
import cv2
from PIL import Image

import streamlit as st
import mediapipe as mp
import webbrowser

# --------------------------------------------------
# homepage

st.set_page_config(initial_sidebar_state = 'collapsed')

st.markdown('<h1 style = \'text-align : center;\'>웹캠으로 찍는 \'인생샷\' 제조기</h1>', unsafe_allow_html = True)
st.markdown('<h4 style = \'text-align : right\'>v0.0.1-alpha</h4>', unsafe_allow_html = True)

st.text('\n')
st.text('\n')

options = st.selectbox('사용할 소스 형태를 선택해주세요.', ('Default', '내장 웹 카메라 - alpha test', '영상 파일 (mp4 형식) - coming soon!', '사진 파일 (jpg 형식) - coming soon!'))
button = st.button('시작하기')

if (options == '내장 웹 카메라 - alpha test') and button :
    webbrowser.open('http://192.168.1.39:8501/page_01_webcam', new = 0)
elif (options == '영상 파일 (mp4 형식) - coming soon!') and button :
    webbrowser.open('http://192.168.1.39:8501/page_02_video', new = 0)
elif (options == '사진 파일 (jpg 형식) - coming soon!') and button :
    webbrowser.open('http://192.168.1.39:8501/page_03_image', new = 0)

st.text('\n')
st.text('\n')

st.markdown(
'''
누군가의 사진을 찍을 때마다 포즈나 구도 때문에 망설이셨나요?\n
정말 잘 나온 사진을 건져내고 싶었는데 어떤 사진이 제일 잘 나왔는지 결정하기 어려우셨나요?\n
'''
)

st.text('\n')

st.markdown(
'''
당신의 고민, 저희가 해결해드리겠습니다!\n
이 사이트는 모델과 인플루언서들이 다양하게 찍힌 잘 나온 사진들을 딥러닝으로 학습하여\n
최적의 포즈나 구도를 잡아줄 수 있도록 당신의 가이드가 되어주고,\n
내부 알고리즘에 의해 소위 '인생샷'이라고 판단되면 자동으로 촬영해드립니다.\n
촬영할 소스 형태를 선택해 당신의 베스트 인생샷을 건져내보세요!\n
'''
)

st.text('\n')
st.text('\n')

st.text(
'''
영우글로벌러닝 AI과정 7기 (2022.04.25 ~ 2022.10.05)
팀 영양제공 (양창은, 공찬우, 양현모, 이경영, 이동재)
'''
)
st.text(
'''
Project 001 넌 이렇게 찍혀야 제일 멋있어!
- Project Manager : 양창은
- Backend Developer : 공찬우, 이경영
- Frontend Developer : 양창은
- Data Manager : 양현모, 이동재
'''
)
st.text('Copyright 2022. Team YYJG. All rights reserved.')

# --------------------------------------------------
# program end

print('program execution complited')

# --------------------------------------------------