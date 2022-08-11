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
# from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration

import av
import mediapipe as mp

from sklearn.datasets import load_iris

# --------------------------------------------------
# title, introduction

st.title('넌 이렇게 찍혀야 제일 멋있어!')
st.subheader('By Team YYJG - 양창은, 공찬우, 양현모, 이경영, 이동재')

# --------------------------------------------------
# contents

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

st.info('아래는 실행 예시입니다.')

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

# img_file_buffer = st.camera_input('')

# if img_file_buffer is not None :
#     bytes_data = img_file_buffer.getvalue()
#     cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
#     st.write(type(cv2_img))
#     st.write(cv2_img.shape)

# img = Image.open('project005/iu_sample.jpg')
# st.image(img, width = 400, caption = '샘플 이미지입니다.')

# vid = open('project005/traindata02.avi', 'rb').read()
# st.video(vid, start_time = 2)

st.success('Successful')

# --------------------------------------------------
# program end

print('program execution complited')

# --------------------------------------------------