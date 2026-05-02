# ROS2 Parameter Practice (param_ws)

이 패키지는 ROS2의 Parameter 시스템을 이해하고, 노드의 설정값을 실시간으로 관리 및 변경하여 로봇의 동작을 제어하는 환경을 구축한 실습 기록입니다.

## 1. 수업 내용 요약

### Parameter의 정의 및 특징
- **정의**: ROS2 노드 내부에서 사용되는 설정값을 의미하며, 노드 실행 중에도 외부에서 값을 조회하거나 수정할 수 있습니다.
- **데이터 형식**: 정수(Integer), 실수(Float), 불리언(Boolean), 문자열(String), 리스트(List) 등 다양한 형식을 지원합니다.
- **필요성**: 소스 코드를 수정하고 재빌드할 필요 없이, 실행 시점에 로봇의 속도, 센서 임계값, 동작 모드 등을 유연하게 변경하기 위해 사용합니다.

### 주요 명령어 (CLI)
- **list**: 현재 활성화된 노드들의 파라미터 목록을 확인합니다.
- **get**: 특정 파라미터의 현재 값을 조회합니다.
- **set**: 특정 파라미터의 값을 실시간으로 변경합니다.
- **dump**: 노드의 현재 파라미터 설정 상태를 YAML 파일로 저장합니다.

## 2. 실습 내용

본 실습에서는 `turtle_param_controller` 노드를 구현하여 파라미터 값에 따라 Turtlesim의 움직임을 실시간으로 제어하는 기능을 구현했습니다.

### 주요 구현 사항 (turtle_param_controller)
1. **파라미터 선언**: `mode`, `linear_speed`, `angular_speed` 등의 파라미터를 노드에 등록하여 외부 제어가 가능하도록 설계했습니다.
2. **동적 파라미터 제어 (Dynamic Control)**: `ros2 param set` 명령을 통해 노드 재실행 없이 거북이의 움직임을 즉각적으로 변경했습니다.
3. **제어 모드 구현**:
   - **circle**: 선속도와 각속도를 조합하여 원운동 수행
   - **zigzag**: 특정 주기마다 방향을 전환하여 지그재그 이동 수행
   - **stop**: 모든 속도 값을 0으로 설정하여 정지

### 실행 절차 및 검증

실습에서는 터미널에서 직접 파라미터를 수정하며 Turtlesim의 반응을 확인했습니다.

```bash
# 1. 파라미터 제어 노드 실행
ros2 run param_pkg turtle_param_controller

# 2. 파라미터 목록 및 현재 모드 확인
ros2 param list
ros2 param get /turtle_param_controller mode

# 3. 실시간 파라미터 변경 테스트
# 원운동 모드로 변경
ros2 param set /turtle_param_controller mode circle

# 지그재그 모드로 변경 및 각속도 조절
ros2 param set /turtle_param_controller mode zigzag
ros2 param set /turtle_param_controller angular_speed 3.0

# 정지 명령
ros2 param set /turtle_param_controller mode stop

# 4. 검증 결과
# - "Set parameter successful" 메시지 출력 확인
# - Turtlesim의 거북이가 설정된 파라미터(circle, zigzag 등)에 맞춰 즉시 동작을 바꾸는 것을 확인
