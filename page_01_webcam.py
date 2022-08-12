# --------------------------------------------------
# program start

print('page_1')

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
# contents - webcam

st.set_page_config(initial_sidebar_state = 'collapsed')

button = st.button('< Back to main page')

if button :
    webbrowser.open('http://192.168.1.39:8501', new = 0)

st.markdown('<h3 style = \'text-align : center;\'>내장 웹 카메라</h3>', unsafe_allow_html = True)

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

st.info('웹 카메라가 실행될 때까지 잠시만 기다려주세요.')

cap = cv2.VideoCapture(0)

cap_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cap_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS) * 0.8)

print(cap_w, cap_h)

cols_cam = st.columns(2)
frame_window_ori = cols_cam[0].image([])
frame_window = cols_cam[1].image([])
st.text('Best Lifeshot (임시 : 오른손을 화면 상단으로 들면 찍힙니다.)')
count = 0
cols_photo = st.columns(4)

with mp_pose.Pose(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as pose :

    while True :
        ret, frame = cap.read()
        black_window = np.zeros([cap_h, cap_w, 3], np.uint8)

        if not ret :
            print('empty camera frame')
            break

        frame.flags.writeable = False
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame)
        frame.flags.writeable = True

        landmarks = results.pose_landmarks.landmark

        mp_drawing.draw_landmarks(
            black_window,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec = mp_drawing_styles.get_default_pose_landmarks_style())
        frame = cv2.flip(frame, 1)
        black_window = cv2.flip(black_window, 1)
        frame_window_ori.image(frame)
        frame_window.image(black_window)

        if landmarks[mp_pose.PoseLandmark.RIGHT_INDEX.value].y <= 0.1 :
            if count == 4 :
                count = 0
                cols_photo = st.columns(4)
            cols_photo[count].image(frame, width = 160)
            count += 1
            continue

cap.release()

st.success('Successful')

# --------------------------------------------------
# program end

print('page_1 load complited')

# --------------------------------------------------