# 자기 평가서

## 1. 가장 잘했다고 생각하는 부분
강의 시간에 처음으로 소프트웨어 엔지니어링 원칙을 적용해 패키지 구조를 체계적으로 설계하고, 객체지향의 상속(Task -> RecurringTask)을 활용해 코드 중복을 줄인 점이 가장 뿌듯합니다. 또한, 기능 구현에만 벅차했던 과거와 달리 PEP 8 스타일 가이드를 준수하고 pytest를 작성해 코드의 신뢰성을 높인 점이 만족스럽습니다. 그리고 무엇보다 이런 절차를 GitHub Actions를 이용한 CI(지속적 통합) 자동화 파이프라인을 구축한 것이 매우 만족스럽습니다.

## 2. 아쉬운 부분
처음 패키지 구조를 잡고 가상환경을 세팅하는 과정에서 파일 경로 설정 등 낯선 환경에 적응하느라 약간의 시행착오를 겪은 점이 아쉽습니다. 또한 예외 처리(ValueError 등)를 더 다양한 상황에 대해 촘촘하게 설계하지 못한 부분이 조금 아쉽습니다.

## 3. 다음에 개선하고 싶은 점
이번 프로젝트에서는 보너스 목표 중 하나인 테스트 커버리지(pytest-cov) 측정까지 완료하여 코드의 안정성을 수치로 확인했습니다. 다음 프로젝트에서는 여기서 한 걸음 더 나아가, Sphinx를 활용해 공식 문서를 웹페이지로 배포하는 작업까지 도전해 보고 싶습니다.


[생성형 인공지능 사용 기록]
* 사용 목적: 프로젝트 패키지 설계 및 소프트웨어 엔지니어링 원칙(PEP 8, pytest) 준수를 위한 단계별 가이드라인 자문

* 질문 및 답변 활용 내용:
	1.	프로젝트 주제로 "할 일 관리 도구"를 선정.
        * 이전에 Flutter를 기반으로 한 To-do 앱을 만들어본 경험이 있기에 To-do를 주제로 선택하는 것이 적합한지, 자유 주제를 비롯한 다른 주제를 하는 것이 적합한지 질문하여 '안정적인 점수 확보'와 '요구사항을 만족하는 것'에 집중하는 것이 중요하다는 답을 받아 To-do 앱으로 개발.
	2.	패키지 표준 디렉터리 구조를 올바르게 구성하기 위해 가상환경 세팅(.venv) 및 초기 폴더 구조 생성 명령어를 자문받아 실행.
	3.	2단계 객체지향 설계를 위해 부모 클래스(Task)의 핵심 속성과 필수 메서드, 비공개 메서드(_validate_title)의 뼈대 코드를 제공받아 활용.
    4.  3단계 자식 클래스 설계를 위해 Task를 상속받는 RecurringTask 클래스의 뼈대 코드(super() 활용 및 비공개 메서드 _validate_rule 포함)를 제공받아 subclass.py를 작성.
    5.  모듈화 및 도우미 함수 분리 요구사항을 충족하기 위해, utils.py에 현재 시간을 반환하는 함수 코드를 자문받아 적용.
    6.  4단계 문서화 및 코드 스타일 점검을 위해 core.py의 get_summary 메서드에 요구사항인 사용 예시(>>>)를 포함한 docstring을 추가. 이후 pycodestyle 실행 과정에서 발생한 공백 및 줄 바꿈(W293, E302, W292), 줄 길이 초과(E501) 등의 PEP 8 스타일 경고를 해결하기 위한 코드 수정 가이드를 받아 오류 없이 적용.
        * todo_manager/core.py:30:1: W293 blank line contains whitespace
          todo_manager/core.py:32:1: W293 blank line contains whitespace
          todo_manager/subclass.py:3:1: E302 expected 2 blank lines, found 1
          todo_manager/subclass.py:36:80: E501 line too long (94 > 79 characters)
          todo_manager/subclass.py:36:95: W292 no newline at end of file
          todo_manager/utils.py:3:1: E302 expected 2 blank lines, found 1
          todo_manager/utils.py:8:56: W292 no newline at end of file
    7.  5단계 단위 테스트 작성을 위해 pytest를 활용하여 총 8개의 테스트 케이스(정상 동작 확인 5건, 빈 문자열/잘못된 타입/잘못된 규칙 입력 등의 엣지 케이스 3건) 코드를 자문받아 test_core.py에 적용하고 모든 테스트가 통과함을 확인.
        * todo_manager/README.md
    8.  6단계 패키지 배포 및 문서화 준비를 위해 setup.py와 requirements.txt의 필수 메타데이터 작성법을 가이드받고, 평가 기준의 6가지 필수 항목이 모두 포함된 README.md 초안을 제공받아 작성 후 패키지 로컬 설치(pip install .) 과정을 검증.
        * todo_manager/README.md
    9. 보너스 점수(+10점) 획득을 위해 pytest-cov 도구를 활용하여 테스트 커버리지를 측정하는 명령어를 자문받아 실행하고 그 결과를 확인 및 캡처함.
        * todo_manager/README.md
    10. 누락되었던 우선순위, 태그 설정 및 JSON 저장 기능을 추가하기 위해 core.py와 subclass.py에 to_dict() 메서드를 구현하고, utils.py에 저장 함수를 추가함. 이후 테스트 코드를 보완하여 9개의 테스트와 90% 커버리지를 달성함.
        * todo_manager/README.md