# 🤖 SSU Robotics Track Study

이 리포지토리는 **SSU 로보틱스 트랙** 과정을 학습하며 ROS2(Robot Operating System 2)를 활용한 로봇 모델링, 시뮬레이션, 시각 제어 및 산업용 협동 로봇 제어를 학습한 기록을 담고 있습니다. 기초적인 통신 구조부터 MoveIt2를 활용한 경로 계획, 그리고 인공지능 기반의 STT 및 Vision 연동 실습 내용을 포함하고 있습니다.

# 🛠️ Tech Stacks

- **Languages**: Python, Xacro/XML (URDF)
- **Platform**: ROS2 Humble (Ubuntu 22.04), Docker
- **Simulation**: Gazebo, RViz2, MoveIt2, IsaacSim
- **Hardware & Library**: Doosan Robotics API (M0609), Intel RealSense (Depth Camera), OpenCV

# 💡 Study Details

### 1. ROS2 Core & Modeling
기초적인 통신 아키텍처와 로봇 외형 정의 방법을 학습했습니다.
- **Launch & Parameter**: 여러 노드를 효율적으로 관리하고 실행 시점에 동적으로 설정값을 변경하는 시스템 구축 (Substitutions, Event Handlers 활용).
- **URDF & Xacro**: XML 매크로 언어인 Xacro를 사용하여 복잡한 로봇 링크와 조인트를 변수화하여 효율적으로 설계 및 모델링.

### 2. Simulation & Control
가상 환경에서 물리 엔진을 연동하여 로봇의 제어를 구현했습니다.
- **Gazebo & ros2_control**: 가상 물리 환경에서의 하드웨어 인터페이스 설정 및 PID 제어를 통한 관절별 궤적 추종 성능 최적화.
- **MoveIt2 Planning**: 장애물이 존재하는 복잡한 환경에서 충돌 없는 최적 경로를 실시간으로 생성하는 '로봇의 두뇌' 역할 구현.

### 3. Industrial Robotics & HRI
산업용 로봇 인터페이스와 외부 센서를 결합한 지능형 시스템을 구축했습니다.
- **Doosan Robotics Control**: 실제 협동 로봇 인터페이스를 통한 공정 자동화 실습 및 Modbus TCP 프로토콜을 이용한 이기종 그리퍼 통합 제어.
- **STT & Vision Integration**: Google Web Speech API를 이용한 음성 명령 제어 및 Depth 카메라 캘리브레이션을 통한 시각 기반 Pick & Place 시스템 구축.

# 📦 Repository Structure

```text
┣ 📂 launch_ws          # ROS2 Launch 시스템 및 Substitution 실습
┣ 📂 param_ws           # 동적 파라미터 제어 및 실시간 설정 관리
┣ 📂 my_urdf            # 기초 URDF 모델링 및 RViz2 시각화
┣ 📂 move_urdf          # Xacro 매크로를 활용한 R2D2 로봇 모델링
┣ 📂 gazebo_ws          # Gazebo 시뮬레이션 및 ros2_control 연동 제어
┣ 📂 depth_ws           # RealSense Depth 카메라 및 OpenCV 좌표 변환 실습
┣ 📂 ros_ws
┃ ┗ 📂 dsr_practice     # 두산 로봇 MoveItPy 제어, Pick & Place, STT 연동
┗ 📜 README.md          # 전체 학습 과정 요약
