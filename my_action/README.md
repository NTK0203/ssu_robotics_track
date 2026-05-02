# ROS2 Action Practice (my_action)

이 패키지는 ROS2의 통신 방식 중 하나인 Action을 활용하여 노드 간의 복합적인 상호작용과 중간 상태 피드백을 주고받는 시스템을 구축한 실습 기록입니다.

## 1. 수업 내용 요약

### Action의 정의
- ROS2 노드 간의 **양방향 메시지 송수신** 방식 중 하나로, 서비스(Service)와 토픽(Topic)의 특성이 결합된 형태입니다.
- 실행 시간이 오래 걸리는 작업을 수행할 때, 클라이언트의 요청에 대해 서버가 중간 진행 과정(Feedback)을 보고하고 최종 결과(Result)를 반환합니다.

### 통신 모델 (Action Client-Server)
- **Goal**: 클라이언트가 서버에게 특정 작업 수행을 요청합니다.
- **Feedback**: 서버가 작업을 수행하는 동안 주기적으로 현재 진행 상태를 클라이언트에 전송합니다.
- **Result**: 작업이 최종 완료되었을 때 서버가 클라이언트에게 전달하는 최종 결과값입니다.
- **주요 용도**: 모바일 로봇의 자율 주행 경로 이동, 복잡한 매니퓰레이터 제어 등 실시간 상태 확인이 필요한 긴 작업에 주로 사용됩니다.

## 2. 실습 내용

본 실습에서는 사용자로부터 목표 거리(m)를 입력받아 로봇이 이동하는 상황을 가정하고, 이동 중 남은 거리를 피드백으로 전송하는 액션 서버와 클라이언트를 구현했습니다.

### 패키지 구성
- **패키지명**: `my_action`
- **인터페이스 패키지**: `my_action_interface` (사용자 정의 Action 인터페이스 포함)
- **빌드 타입**: `ament_python`
- **사용 의존성**: `rclpy`, `my_action_interface`

### 주요 구현 사항
1. **Action Server 노드 (patrol_action_server.py)**
   - `my_action_interface.action.Patrol` 인터페이스를 사용합니다.
   - 클라이언트로부터 수신한 목표값에 따라 루프를 돌며 가상의 이동 과정을 수행합니다.
   - 매 주기마다 현재까지 이동한 거리와 남은 거리를 계산하여 피드백 메시지를 전송합니다.

2. **Action Client 노드 (patrol_action_client.py)**
   - 서버에 목표 거리를 전달하고 작업 시작을 요청합니다.
   - 서버에서 전송하는 피드백(중간 거리 정보)을 실시간으로 수신하여 터미널에 출력합니다.
   - 작업 완료 후 최종 결과 메시지를 출력합니다.

3. **환경 설정 (setup.py)**
   - `entry_points` 설정을 통해 액션 서버와 클라이언트를 독립적인 명령어로 실행할 수 있도록 등록했습니다.

### 실행 절차 및 검증
```bash
# 워크스페이스 빌드 (인터페이스 패키지 우선 빌드 필요)
colcon build --packages-select my_action_interface my_action
source install/setup.bash

# Action Server 실행
ros2 run my_action server

# Action Client 실행 (별도 터미널)
ros2 run my_action client

# 액션 상태 및 정보 확인
ros2 action list
ros2 action info /patrol
