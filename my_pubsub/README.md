# ROS2 Topic Practice (my_pubsub)

이 패키지는 ROS2의 가장 기본적인 통신 방식인 Topic을 활용하여 노드 간 데이터를 비동기적으로 주고받는 시스템을 구축한 실습 기록입니다.

## 1. 수업 내용 요약

### Topic의 정의
- ROS2 노드 간 데이터를 주고받는 **비동기식 단방향 메시지 송수신** 방식입니다.
- 연속적으로 변화하는 센서 데이터나 로봇의 상태 정보를 실시간으로 모니터링하기 위해 주로 사용됩니다.

### 통신 모델 (Publisher-Subscriber)
- **Publisher**: 특정 데이터 타입(Interface)을 가진 메시지를 생성하여 특정 토픽으로 발행합니다.
- **Subscriber**: 발행된 메시지를 구독하여, 메시지가 도착할 때마다 미리 정의된 콜백(Callback) 함수를 실행합니다.
- **다대다 통신**: 하나의 토픽에 대해 여러 개의 Publisher와 Subscriber가 동시에 연결될 수 있습니다.

## 2. 실습 내용

본 실습에서는 Python을 사용하여 문자열 데이터를 주기적으로 발행하는 Talker 노드와 이를 수신하는 Listener 노드를 구현했습니다.

### 패키지 구성
- **패키지명**: `my_pubsub`
- **빌드 타입**: `ament_python`
- **사용 의존성**: `rclpy`, `std_msgs`

### 주요 구현 사항
1. **Publisher 노드 (my_pub.py)**
   - `rclpy.node.Node`를 상속받아 구현되었습니다.
   - `std_msgs.msg.String` 타입을 사용하여 "Hello World" 메시지를 생성합니다.
   - 0.5초 주기의 Timer를 설정하여 토픽을 지속적으로 발행합니다.

2. **Subscriber 노드 (my_sub.py)**
   - 동일한 토픽 이름을 구독하도록 설정되었습니다.
   - 수신된 메시지의 `data` 필드를 터미널에 출력하는 로그 기능을 포함합니다.

3. **환경 설정 (setup.py)**
   - `entry_points`를 통해 작성한 스크립트를 `talker` 및 `listener`라는 명령어로 실행할 수 있도록 등록했습니다.

### 실행 절차 및 검증
```bash
# 워크스페이스 빌드
colcon build --packages-select my_pubsub
source install/setup.bash

# Publisher 실행
ros2 run my_pubsub talker

# Subscriber 실행 (별도 터미널)
ros2 run my_pubsub listener

# 통신 상태 확인
ros2 topic list
ros2 topic echo /topic_name
