
## ipynb
### 1. 기본 이미지 처리:
이미지 데이터의 표현 및 색상 공간 이해 (RGB).
히스토그램 분석 및 이미지의 명암, 밝기 조절.
노이즈 제거, 필터링 등 이미지 전처리 기법.

### 2. 이미지 특징 추출:
이미지의 경계선 감지 및 형태학적 연산(모폴로지)을 통한 객체 분리 및 정제.
이미지 내 특정 객체(예: 새)를 계수하는 방법론 학습.

### 3. 고급 이미지 변환:
이미지 크기 조절, 회전, 이동 등 기하학적 변환.
보다 복잡한 이미지 변형 기술인 워핑(Warping) 및 모핑(Morphing) 실습.

### 4. 인공지능 기반 객체 인식:
사람의 얼굴을 감지하는 다양한 기법(Haar Cascade, Dlib 등)과 이론 학습.
최신 딥러닝 기반의 객체 검출 모델인 YOLO(You Only Look Once)를 활용한 실시간 객체 인식 구현.

## mobels
### 얼굴 감지 (Face Detection):
#### 고전적 방식: haarcascade_frontalface_default.xml
##### Haar Cascade 분류기는 빠르고 경량화된 얼굴 감지에 사용
---
#### 딥러닝 기반: deploy.prototxt.txt, res10_300x300_ssd_iter_140000.caffemodel
##### Caffe 프레임워크 기반의 SSD(Single Shot MultiBox Detector) 모델로, 높은 정확도로 얼굴을 감지
---
#### 정확도 높은 감지: mmod_human_face_detector.dat
##### Dlib 라이브러리에서 사용되는 MMOD 기반 모델로, 정확한 얼굴 감지에 기여
---
#### 얼굴 랜드마크 추적 (Face Landmark Detection): shape_predictor_68_face_landmarks.dat
##### 감지된 얼굴 영역 내에서 눈, 코, 입 등 68개의 주요 특징점(랜드마크)을 정밀하게 찾아내는 데 사용되며 이는 표정 분석이나 얼굴 변형 등에 활용됨
---
### 일반 객체 인식 (General Object Recognition): yolov8m.pt
##### 최신 딥러닝 모델인 YOLOv8(You Only Look Once version 8)의 가중치 파일이다. 
##### 이 모델은 실시간으로 이미지나 비디오 내의 다양한 객체(예: 사람, 자동차, 동물 등)를 빠르고 정확하게 감지하고 분류하는 데 탁월한 성능을 발휘
---
