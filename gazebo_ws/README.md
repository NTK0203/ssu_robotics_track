# ROS2 Simulation and Control Practice (gazebo_ws)

이 워크스페이스는 Gazebo 시뮬레이터와 ros2_control 프레임워크를 연동하여 가상 환경에서 로봇 팔(simple_arm)을 물리적으로 구동하고, MoveIt2를 통해 정교한 경로 계획 및 충돌 감지를 구현한 실습 기록입니다.

---

## [7차시] Gazebo 기초 및 ros2_control 설정 (18, 19장)

### 1. 주요 패키지 및 파일
- **package**: `simple_arm_description`
- **files**:
  - `urdf/simple_arm.urdf.xacro`: 물리 시뮬레이션을 위한 관성(Inertial), 충돌(Collision), ros2_control 태그가 포함된 로봇 모델링 파일
  - `launch/gazebo_spawn_launch.py`: Gazebo 월드를 실행하고 로봇 모델을 스폰(Spawn)하는 핵심 런치 파일

### 2. 수업 및 실습 요약
- **Gazebo 기초**: 가상 공간 시뮬레이터 설치 및 로봇 모델의 물리적 특성(질량, 관성) 정의 방법 습득
- **ros2_control 설정**: 로봇의 시각적 형태(URDF)에 '근육' 역할을 하는 제어 인터페이스를 부여
- **주요 동작**: `effort_controller`를 활성화하여 관절에 직접적인 힘(Effort) 명령을 내리고 동작 확인

---

## [8차시] 실전 로봇 제어 및 PID 튜닝 (20장)

### 1. 주요 패키지 및 파일
- **package**: `simple_arm_description`
- **files**:
  - `config/controllers.yaml`: Controller Manager가 관리할 컨트롤러(JTC, Joint State Broadcaster) 종류와 관절별 PID 게인 값을 설정한 파일
  - `launch/gazebo_spawn.launch.py`: 컨트롤러 매니저를 함께 구동하도록 업데이트된 실행 스크립트

### 2. 수업 및 실습 요약
- **Controller Manager**: 여러 컨트롤러의 생명주기를 관리하고 하드웨어 인터페이스와 연결
- **Joint Trajectory Controller (JTC)**: 여러 관절의 목표 궤적을 받아 동시 제어 수행
- **PID 튜닝**: 실시간으로 `p`, `i`, `d` 값을 수정하며 로봇 팔이 흔들림 없이 목표 자세를 유지하도록 최적화

---

## [9차시] MoveIt2 연동 및 고급 제어 (22, 23, 24장)

### 1. 주요 패키지 및 파일
- **package 1**: `simple_arm_moveit` (MoveIt Setup Assistant로 생성된 설정 패키지)
  - `config/moveit.rviz`: MoveIt2 전용 시각화 설정 파일
- **package 2**: `simple_arm_trajectory` (궤적 추적 노드 패키지)
  - `simple_arm_trajectory/send_waypoint.py`: 여러 목표 지점을 순차적으로 전송하는 노드
  - `simple_arm_trajectory/waypoint_action_follower.py`: 액션 통신 기반의 궤적 추종 노드

### 2. 수업 및 실습 요약
- **MoveIt2-Gazebo 통합**: MoveIt2(계획) → ros2_control(연결) → Gazebo(실행)로 이어지는 제어 파이프라인 완성
- **궤적 추적 (Trajectory Tracking)**: 시간에 따라 변하는 목표를 따라가기 위한 Waypoint-follow 로직 구현
- **충돌 감지 (Collision Detection)**: Planning Scene에 장애물(Box)을 추가하고, 로봇이 스스로 충돌을 피해 경로를 생성하는지 검증

---

## 실행 및 검증 절차 요약

작성된 패키지들을 통합하여 로봇을 구동하는 표준 절차입니다.

```bash
# 1. 시뮬레이션 환경 실행
ros2 launch simple_arm_description gazebo_spawn_launch.py

# 2. MoveIt2 인터페이스 실행
ros2 launch simple_arm_moveit demo_launch.py

# 3. 궤적 추적 실습
ros2 run simple_arm_trajectory send_waypoint

# 4. 검증 포인트
# - Gazebo 상에서 로봇이 물리 법칙에 따라 정상 동작하는지 확인
# - RViz의 Planning Scene에 장애물 추가 시 우회 경로가 생성되는지 확인
# - 컨트롤러 상태 확인: ros2 control list_controllers
