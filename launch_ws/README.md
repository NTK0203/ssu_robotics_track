# ROS2 Launch System Practice (launch_ws)

이 패키지는 ROS2의 Launch 시스템을 활용하여 여러 노드를 효율적으로 관리하고, 실행 시점에 동적으로 경로를 지정하거나 이벤트를 처리하는 환경을 구축한 실습 기록입니다.

## 1. 수업 내용 요약

### Launch의 정의 및 필요성
- **정의**: 하나 이상의 노드를 실행하기 위한 정보를 담은 설정 파일(Python, XML, YAML)을 통해 전체 시스템을 구동하는 방식입니다.
- **필요성**: 프로젝트 규모가 커짐에 따라 실행해야 할 노드, 파라미터, 변수(Argument)가 많아질 때 이를 한꺼번에 제어하기 위해 사용합니다.

### 주요 기능
- **Substitutions**: 실행 시점(Launch time)에 평가되는 기능입니다. `FindPackageShare`와 같은 기능을 사용하여 특정 패키지의 설치 경로를 하드코딩하지 않고 동적으로 찾아낼 수 있습니다. 이를 통해 환경이 변해도 코드 수정 없이 실행이 가능합니다.
- **Event Handlers**: 프로세스의 상태 변화를 감지합니다. 특정 노드가 시작되거나(`OnProcessStart`) 종료될 때(`OnProcessExit`) 미리 정의된 액션(예: 다른 노드 실행, 로그 출력)이 수행되도록 설정할 수 있습니다.

## 2. 실습 내용

본 실습에서는 Python 기반의 Launch 파일을 작성하여 Turtlesim 환경에서 노드 간의 의존성을 제어하고 동적 경로 참조를 구현했습니다.

### 주요 구현 사항 (substitutions.py)
1. **노드 구성**: `turtlesim` 패키지의 `turtlesim_node`를 실행하도록 설정했습니다.
2. **Substitutions 활용**: `FindPackageShare`를 사용하여 `turtlesim` 패키지의 위치를 자동으로 참조하도록 구성했습니다.
3. **이벤트 처리**: 
   - `RegisterEventHandler`를 사용하여 `turtlesim_node`가 완전히 실행된 후(`OnProcessStart`)에만 다음 동작이 일어나도록 설계했습니다.
   - 노드 시작 이벤트가 발생하면 `LogInfo`를 통해 "Turtlesim started, spawning turtle" 메시지를 출력하고, 새로운 거북이를 생성하는 명령이 순차적으로 실행되도록 구현했습니다.

### 실행 절차 및 검증
실습에서는 작성된 Python 스크립트 파일을 직접 실행하여 동작을 확인했습니다.

```bash

# 1. launch 파일을 직접 실행
ros2 launch substitutions_py main_launch.py

# 2. 이벤트 핸들러 런치 실행
ros2 launch substitutions_py event_handlers_launch.py turtlesim_ns:='turtlesim3' use_provided_red:='True' new_background_r:=200

# 3. 검증
# - 첫 번째 turtlesim_node가 정상적으로 실행됨
# - 터미널에 "Turtlesim started, spawning turtle" 로그가 출력됨
# - 이벤트 핸들러에 의해 자동으로 두 번째 거북이가 spawn 됨과 배경 색상이 변한 것을 확인
