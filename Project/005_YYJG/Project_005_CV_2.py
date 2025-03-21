# --------------------------------------------------
# program start

print('program execution succeeded')

# --------------------------------------------------
# module import

import pandas as pd
import numpy as np
import streamlit as st
import mediapipe as mp
import tensorflow as tf

import time
import cv2
from PIL import Image

import webbrowser
from sklearn.model_selection import train_test_split
from collections import deque

# --------------------------------------------------
# function settings

def cal_d(p, n) :
    d = (p[0] - n[0]) ** 2 + (p[1] - n[1]) ** 2
    return d ** (1 / 2) 

def cal_p(x, y) :
    return (x - y)

def get_score(data) :
    score = score_model.predict(data)[0][0]
    score = int(score * 10000)
    score = float(score) / 100
    return score

def get_angle(data) :
    p = angle_model.predict(data)[0][0]
    return (p - 90)

def cor_histogram(correl_imagelist) :
    hists = []
    co01 = []
    co09 = []
    
    for file in correl_imagelist :
        nowimg = file[0]
        hsv = cv2.cvtColor(nowimg, cv2.COLOR_BGR2HSV)
        hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
        cv2.normalize(hist, hist, 0, 1, cv2.NORM_MINMAX)
        hists.append(hist)

    if hists :
        query = hists[-1]
        methods = ['CORREL']
        compare_hists = []
        
        for i, histogram in enumerate(hists) :
            ret = cv2.compareHist(query, histogram, 0)
            
            if ret < 0.9 :
                co01.append(correl_imagelist[i])
            else:
                co09.append(correl_imagelist[i])

        co09 = sorted(co09, key = lambda x : x[1])

        while len(co09) > correl_save_number :
            del co09[0]

        correl_imagelist = co01 + co09
        correl_imagelist = sorted(correl_imagelist, key = lambda x : x[1])

        while len(correl_imagelist) > picture_save_number :
            del correl_imagelist[0]
            
    return correl_imagelist

# --------------------------------------------------
# model load

score_model = tf.keras.models.load_model('flp_score_predict001.h5')
angle_model = tf.keras.models.load_model('flp_horizon_correction003.h5')

# --------------------------------------------------
# title

# st.set_page_config(initial_sidebar_state = 'collapsed')

st.markdown('<h1 style = \'text-align : center;\'>웹캠으로 찍는 \'인생샷\' 제조기</h1>', unsafe_allow_html = True)
st.markdown('<h4 style = \'text-align : right\'>v0.0.2-alpha</h4>', unsafe_allow_html = True)

# --------------------------------------------------
# main page

def main_page() :
    
    print('main page on')

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
    
    print('main page end')
    
# --------------------------------------------------
# page 1 webcam
    
def sub_page_1() :
    
    print('page 1 on')
    
    global correl_save_number, picture_save_number
    
    st.markdown('<h3 style = \'text-align : center;\'>내장 웹 카메라</h3>', unsafe_allow_html = True)
    st.info('웹 카메라가 실행될 때까지 잠시만 기다려주세요.')
    
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_holistic = mp.solutions.holistic
    count = 0
    BG_COLOR = (0, 0, 0)
    MASK_COLOR = (1, 1, 1)

    cap = cv2.VideoCapture(0)

    cap_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    cap_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS) * 0.8)

    print(cap_w, cap_h)

    cols_cam = st.columns(2)
    frame_window_ori = cols_cam[0].image([])
    frame_window = cols_cam[1].image([])
    st.text('Good Photos (내부 알고리즘에 의해 임시적으로 좋은 사진의 후보로 등록됩니다.)')
    count_col = 0
    cols_photo = st.columns(4)
    
    prev_time = 0
    FPS = 10
    prescore = 0
    idx = 0
    datacompare = 0

    picture_save_number = 30
    correl_save_number = 5

    imagelist = []
    correl_imagelist = []

    with mp_holistic.Holistic(
        min_detection_confidence = 0.5,
        min_tracking_confidence = 0.5) as holistic :
        
        while cap.isOpened() :
            
            idx += 1
            success, image = cap.read()
            black_window = np.zeros([cap_h, cap_w, 3], np.uint8)
            
            if not success :
                print('Ignoring empty camera frame.')
                break

            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = holistic.process(image)

            n=[]
            visibility =[]
            
            if results.pose_landmarks :
                for data_point in results.pose_landmarks.landmark :
                    n.append(data_point.x)
                    n.append(data_point.y)
                    n.append(data_point.z)
                    visibility.append(data_point.visibility)
            else :
                for _ in range(99) :
                    n.append(0)

            nowdata = [n]

            if datacompare == 0 :
                predata = [[0 for _ in range(99)]]

            datacompare += 1

            xyzd = 0
            
            for i in range(99) :
                xyzd += (nowdata[0][i]-predata[0][i]) ** 2

            lifescore = get_score(nowdata)
            lifeangle = get_angle(nowdata)

            allscore = lifescore
            predata = nowdata

            text1 = 'score : {}'.format(round(lifescore, 2))
            text2 = 'angle : {}'.format(round(lifeangle, 2))
            org1 = (30, 30)
            org2 = (30, 60)
            font=cv2.FONT_HERSHEY_SIMPLEX

            image.flags.writeable = True
            save_image = image.copy()

            mp_drawing.draw_landmarks(
                black_window,
                results.pose_landmarks,
                mp_holistic.POSE_CONNECTIONS,
                landmark_drawing_spec = mp_drawing_styles.get_default_pose_landmarks_style())
            
            image = cv2.flip(image, 1)
            black_window = cv2.flip(black_window, 1)
            
            cv2.putText(black_window, text1, org1, font, 1, (255, 0, 0) ,2)
            cv2.putText(black_window, text2, org2, font, 1, (255, 0, 0) ,2)
            
            frame_window_ori.image(image)
            frame_window.image(black_window)
            
            if abs(lifeangle) < 10 :
                if count_col == 4 :
                    count_col = 0
                    cols_photo = st.columns(4)
                correl_imagelist.append([save_image, allscore])
                cols_photo[count_col].image(save_image, width = 160)
                count_col += 1
                continue

            correl_imagelist = cor_histogram(correl_imagelist)
            prescore = lifescore

            if cv2.waitKey(10) & 0xFF == 27 :
                break
            
    cap.release()
    
    print('page 1 end')
    
# --------------------------------------------------
# page 2 video
    
def sub_page_2() :
    
    print('page 2 on')
    
    global correl_save_number, picture_save_number, correl_imagelist
    
    st.markdown('<h3 style = \'text-align : center;\'>영상 파일 (mp4 형식)</h3>', unsafe_allow_html = True)   
    
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_holistic = mp.solutions.holistic
    count = 0
    BG_COLOR = (0, 0, 0)
    MASK_COLOR = (1, 1, 1)
    
    video_file = st.file_uploader('영상 파일을 업로드해주세요.', type = ['mp4'])
    
    if video_file is not None :      
        
        vid = video_file.name
        
        with open(vid, mode = 'wb') as f :
            f.write(video_file.read())
            
        st.markdown(f'''
        ##### 영상 분석 중...
        - {vid}
        ''',
        unsafe_allow_html = True)
        
        st.info('영상 파일을 분석하는 동안 잠시만 기다려주세요.')

        vidcap = cv2.VideoCapture(vid)
        
        cap_w = int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH))
        cap_h = int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(vidcap.get(cv2.CAP_PROP_FPS) * 0.8) 
        
        print(cap_w, cap_h)

        cols_cam = st.columns(2)
        frame_window_ori = cols_cam[0].image([])
        frame_window = cols_cam[1].image([])
#         st.text('Good Photos (내부 알고리즘에 의해 임시적인 좋은 사진의 후보로 등록됩니다.)')
#         count_col = 0
#         cols_photo = st.columns(4)

        prev_time = 0
        FPS = 10
        prescore = 0
        idx = 0
        datacompare = 0

        picture_save_number = 30
        correl_save_number = 5

        imagelist = []
        correl_imagelist = []       

        with mp_holistic.Holistic(
            min_detection_confidence = 0.5,
            min_tracking_confidence = 0.5) as holistic :

            while vidcap.isOpened() :

                idx += 1
                success, image = vidcap.read()
                black_window = np.zeros([cap_h, cap_w, 3], np.uint8)

                if not success :
                    print('Ignoring empty camera frame.')
                    break

                image.flags.writeable = False
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = holistic.process(image)

                n=[]
                visibility =[]

                if results.pose_landmarks :
                    for data_point in results.pose_landmarks.landmark :
                        n.append(data_point.x)
                        n.append(data_point.y)
                        n.append(data_point.z)
                        visibility.append(data_point.visibility)
                else :
                    for _ in range(99) :
                        n.append(0)

                nowdata = [n]

                if datacompare == 0 :
                    predata = [[0 for _ in range(99)]]

                datacompare += 1

                xyzd = 0

                for i in range(99) :
                    xyzd += (nowdata[0][i]-predata[0][i]) ** 2

                lifescore = get_score(nowdata)
                lifeangle = get_angle(nowdata)

                allscore = lifescore
                predata = nowdata

                text1 = 'score : {}'.format(round(lifescore, 2))
                text2 = 'angle : {}'.format(round(lifeangle, 2))
                org1 = (30, 30)
                org2 = (30, 60)
                font=cv2.FONT_HERSHEY_SIMPLEX

                image.flags.writeable = True
                save_image = image.copy()

                mp_drawing.draw_landmarks(
                    black_window,
                    results.pose_landmarks,
                    mp_holistic.POSE_CONNECTIONS,
                    landmark_drawing_spec = mp_drawing_styles.get_default_pose_landmarks_style())

                cv2.putText(black_window, text1, org1, font, 1, (255, 0, 0) ,2)
                cv2.putText(black_window, text2, org2, font, 1, (255, 0, 0) ,2)

                frame_window_ori.image(image)
                frame_window.image(black_window)

                if (abs(lifeangle) < 10) and (xyzd < 0.002) :
#                     if count_col == 4 :
#                         count_col = 0
#                         cols_photo = st.columns(4)
                    correl_imagelist.append([save_image, allscore])
#                     cols_photo[count_col].image(save_image, width = 160)
#                     count_col += 1
#                     continue

                correl_imagelist = cor_histogram(correl_imagelist)
                prescore = lifescore

                if cv2.waitKey(10) & 0xFF == 27 :
                    break

        vidcap.release()
        
        st.text('Best Photos (내부 알고리즘에 의해 최종적으로 제일 잘 나온 30개의 사진을 선정했습니다.)')
        count2 = 0
        count_col_2 = 0
        cols_photo_2 = st.columns(4)
        for bestpicture in correl_imagelist :
            if count_col_2 == 4 :
                count_col_2 = 0
                cols_photo_2 = st.columns(4)
            count2 += 1
            cols_photo_2[count_col_2].image(bestpicture[0], width = 160)
            bestpicture[0] = cv2.cvtColor(bestpicture[0], cv2.COLOR_BGR2RGB)
            cv2.imwrite('saved_image/best_image{:0>4}_s{}'.format(count2, int(bestpicture[1])) + '.png', bestpicture[0])
            count_col_2 += 1

    print('page 2 end')

# --------------------------------------------------
# page 3 image
    
def sub_page_3() :
    
    print('page 3 on')
    
    st.markdown('<h3 style = \'text-align : center;\'>사진 파일 (jpg 형식)</h3>', unsafe_allow_html = True)
    st.subheader('Coming soon!')
    
    print('page 3 end')
    
# --------------------------------------------------
# main page select box

page_names_to_funcs = {
    'Default (이 옵션을 선택할 시 메인 페이지로 이동합니다.)' : main_page,
    '내장 웹 카메라 - alpha test' : sub_page_1,
    '영상 파일 (mp4 형식) - alpha test' : sub_page_2,
    '사진 파일 (jpg 형식) - coming soon!' : sub_page_3
}

selected_page = st.selectbox('사용할 소스 형태를 선택해주세요.', page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

# --------------------------------------------------
# program end

print('program execution complited')

# --------------------------------------------------
