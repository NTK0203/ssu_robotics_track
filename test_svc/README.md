# ROS2 Service & Client Practice (test_svc)

이 패키지는 ROS2의 통신 방식 중 하나인 Service를 활용하여 노드 간 동기식 양방향 데이터를 주고받는 시스템을 구축한 실습 기록입니다.

## 1. 수업 내용 요약

### Service의 정의
- ROS2 노드 간 **동기식 양방향 메시지 송수신** 방식입니다.
- 클라이언트(Client)가 요청(Request)을 보내면 서버(Server)가 이를 처리한 후 응답(Response)을 반환합니다.
- 특정 동작을 수행하도록 명령하거나, 특정 시점의 데이터를 요청하고 그 결과를 확인해야 하는 경우에 주로 사용됩니다.

### 통신 모델 (Service-Client)
- **Service Server**: 특정 서비스를 제공하며, 클라이언트의 요청이 올 때까지 대기하다가 요청이 오면 지정된 로직을 수행하고 응답을 보냅니다.
- **Service Client**: 서버에 서비스를 요청하고, 서버로부터 응답이 올 때까지 기다립니다.
- **동기성**: 토픽(Topic)과 달리 요청에 대한 결과가 올 때까지 흐름이 이어지는 것이 특징입니다.

## 2. 실습 내용

본 실습에서는 Python을 사용하여 두 정수의 합을 계산해 주는 서비스 서버와 이를 호출하는 클라이언트를 구현했습니다.

### 패키지 구성
- **패키지명**: `my_svc` (실습 워크스페이스: `test_svc`)
- **빌드 타입**: `ament_python`
- **사용 의존성**: `rclpy`, `example_interfaces`

### 주요 구현 사항
1. **Service Server 노드 (my_service.py)**
   - `example_interfaces.srv.AddTwoInts` 인터페이스를 사용합니다.
   - 두 개의 정수(`a`, `b`)를 입력받아 합계(`sum`)를 계산하여 반환하는 콜백 함수를 구현했습니다.

2. **Service Client 노드 (my_client.py)**
   - 서버에 접속하여 두 개의 정수 데이터를 담은 요청을 보냅니다.
   - 서버로부터 계산된 결과값을 수신하여 터미널에 출력합니다.

3. **환경 설정 (setup.py)**
   - `entry_points` 설정을 통해 `service` 및 `client` 명령어로 각 노드를 실행할 수 있도록 등록했습니다.

### 실행 절차 및 검증
```bash
# 워크스페이스 빌드
colcon build --packages-select my_svc
source install/setup.bash

# Service Server 실행
ros2 run my_svc service

# Service Client 실행 (별도 터미널)
ros2 run my_svc client 2 3

# 서비스 리스트 및 타입 확인
ros2 service list
ros2 service type /add_two_ints
