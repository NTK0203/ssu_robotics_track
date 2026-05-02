# Isaac Sim Python Scripting Practice (user_examples)

이 디렉토리는 NVIDIA Isaac Sim의 **Python 스크립팅 API(Core API)**를 활용하여 가상 환경을 구축하고, 로봇 모델을 불러와 물리 기반의 자율 주행 로직을 직접 구현한 실습 기록입니다.

---

## 1. 수업 내용 요약

### Isaac Sim Core API 핵심 개념
- **World & Scene**: 시뮬레이션의 전체 월드와 그 안의 오브젝트(로봇, 지면 등)를 관리하는 중앙 시스템입니다.
- **BaseSample**: Isaac Sim에서 제공하는 표준 프레임워크 클래스로, 씬 구성(`setup_scene`)과 데이터 로드 후 처리(`setup_post_load`) 등의 단계를 구조화합니다.
- **Physics Callback**: 시뮬레이션의 매 스텝(Step)마다 특정 함수를 실행하게 하여, 실시간으로 로봇의 상태를 읽고 제어 명령을 내리는 루프를 형성합니다.

### 로봇 제어 및 시간 관리
- **WheeledRobot 클래스**: 차륜형 로봇(Jetbot 등)의 조인트와 물리적 특성을 쉽게 정의하고 제어하기 위한 전용 클래스입니다.
- **ArticulationAction**: 로봇 관절에 구동력(Effort), 위치(Position), 속도(Velocity) 명령을 전달하는 표준 데이터 구조입니다.
- **비차단식 시간 제어**: 시뮬레이션의 `step_size`를 누적하여 경과 시간을 계산함으로써, `time.sleep()` 없이도 안정적인 시나리오 기반 동작을 구현합니다.

---

## 2. 실습 내용

### 주요 파일 및 구현 세부 사항
- **`hello_world.py` (Jetbot 자율 주행 시나리오)**
  - **구현 내용**: NVIDIA Jetbot을 가상 환경에 스폰하고, 정해진 시간표에 따라 이동 및 정지 동작을 수행하도록 설계했습니다.
  - **구현 방법**:
    1. `setup_scene`에서 Nucleus 서버의 Jetbot USD 자산을 불러와 `WheeledRobot` 인스턴스를 생성했습니다.
    2. `setup_post_load`에서 로봇의 아티큘레이션 컨트롤러를 활성화하고, 물리 콜백 함수(`send_robot_actions`)를 등록했습니다.
    3. `send_robot_actions` 내부에서 `step_size`를 `_elapsed_time`에 누적하여 **상태 기반 제어(State-based control)**를 구현했습니다.

### 주행 시나리오 흐름
- **0~3초**: 후진 (BACK)
- **3~8초**: 일시 정지 (STOP)
- **8~12초**: 좌회전 (LEFT)
- **12~15초**: 직진 (GO)
- **15초 이후**: 최종 정지 (STOP)

---

## 3. 실행 절차 및 검증

### 실행 방법
1. NVIDIA Isaac Sim을 실행합니다.
2. 상단 메뉴의 `Script Editor`를 열거나, `Extension Manager`를 통해 작성된 `hello_world.py`를 로드합니다.
3. **'LOAD'** 버튼을 클릭하여 Jetbot이 월드에 정상적으로 생성되는지 확인합니다.
4. **'PLAY'** 버튼을 클릭하여 물리 엔진 기반의 자율 주행 시나리오를 시작합니다.

### 검증 포인트
- 로봇이 소스 코드에 정의된 `velocities` 값(BACK, LEFT, GO 등)에 맞춰 물리적으로 정확히 움직이는가?
- 물리 콜백을 통해 매 스텝마다 속도 명령이 끊김 없이 인가되는가?
- 시뮬레이션 시간이 누적됨에 따라 정의된 시나리오 순서대로 동작이 전환되는가?
