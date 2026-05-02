# ROS2 URDF Robot Modeling Practice (my_urdf)

이 패키지는 URDF(Unified Robot Description Format)를 사용하여 가상 환경에서 로봇의 형태를 정의하고, 시각화 도구인 RViz2를 통해 모델을 확인하는 과정을 실습한 기록입니다.

## 1. 수업 내용 요약

### URDF의 정의 및 구성
- **정의**: 가상 환경에서의 로봇 모델을 규격화하여 정의하는 포맷으로, 보통 XML 형식을 사용합니다.
- **장점**: OS 호환성이 뛰어나며 가상 환경에서 로봇의 동작을 손쉽게 구현할 수 있습니다.
- **핵심 요소**:
  - **Link**: 로봇의 물리적인 부분(뼈대, 링크)을 정의합니다.
  - **Joint**: 링크와 링크 사이의 연결(관절)을 정의합니다.

### 주요 Joint Type
로봇의 관절 종류에 따라 다음과 같이 구분하여 설정합니다.
- **fixed**: 부모와 자식 링크 간의 움직임이 없는 고정 상태입니다.
- **revolute**: 특정 각도 범위 내에서 회전하는 관절입니다.
- **continuous**: 바퀴처럼 각도 제한 없이 무한 회전하는 관절입니다.
- **prismatic**: 직선 방향으로 이동하는 슬라이드형 관절입니다.

## 2. 실습 내용

본 실습에서는 직접 my_urdf 패키지를 생성하고, 원통형 링크를 가진 기초적인 로봇 모델을 설계하여 RViz2로 구동했습니다.

### 주요 구현 사항 (myfirst.urdf)
1. **패키지 구조**: urdf, rviz, launch 폴더를 생성하여 각각 모델 파일, 설정 파일, 실행 스크립트를 관리하도록 구성했습니다.
2. **모델 정의**: base_link라는 이름의 링크를 생성하고, 높이 0.6, 반지름 0.2의 실린더(Cylinder) 형상으로 구성했습니다.
3. **시각화 및 충돌 설정**: <visual> 태그를 통해 파란색 외관을 지정하고, <collision> 태그를 추가하여 물리적 충돌 범위를 설정했습니다.
4. **런칭 시스템 구현**: simple_display.launch.py를 작성하여 robot_state_publisher와 rviz2 노드가 동시에 실행되도록 설정했습니다.

### 실행 절차 및 검증

작성한 모델을 빌드하고 RViz2를 통해 정상적으로 출력되는지 확인했습니다.

```bash
# 1. 패키지 빌드 및 환경 활성화
cd ~/my_urdf
colcon build
source install/local_setup.bash

# 2. URDF 런치 파일 실행
ros2 launch my_urdf simple_display.launch.py

# 3. RViz2 초기 설정 및 검증
# - 실행 후 RViz 창에서 'Add' 버튼 클릭 후 'RobotModel' 추가
# - 'Description Topic' 항목을 '/robot_description'으로 선택
# - 'Global Options'의 'Fixed Frame'을 'base_link'로 변경
# - 화면 중앙에 파란색 원통 모델이 정상적으로 출력되는지 확인
