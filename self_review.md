[생성형 인공지능 사용 기록]
* 사용 목적: 프로젝트 패키지 설계 및 소프트웨어 공학 원칙(PEP 8, pytest) 준수를 위한 단계별 가이드라인 자문

* 질문 및 답변 활용 내용:
	1.	프로젝트 주제로 "할 일 관리 도구"를 선정.
        * 이전에 Flutter를 기반으로 한 To-do 앱을 만들어본 경험이 있기에 To-do를 주제로 선택하는 것이 적합한지, 자유 주제를 비롯한 다른 주제를 하는 것이 적합한지 질문하여 '안정적인 점수 확보'와 '요구사항을 만족하는 것'에 집중하는 것이 중요하다는 답을 받아 To-do 앱으로 개발.
	2.	패키지 표준 디렉터리 구조를 올바르게 구성하기 위해 가상환경 세팅(.venv) 및 초기 폴더 구조 생성 명령어를 자문받아 실행.
	3.	2단계 객체지향 설계를 위해 부모 클래스(Task)의 핵심 속성과 필수 메서드, 비공개 메서드(_validate_title)의 뼈대 코드를 제공받아 활용.
    4.  3단계 자식 클래스 설계를 위해 Task를 상속받는 RecurringTask 클래스의 뼈대 코드(super() 활용 및 비공개 메서드 _validate_rule 포함)를 제공받아 subclass.py를 작성.
    5.  모듈화 및 도우미 함수 분리 요구사항을 충족하기 위해, utils.py에 현재 시간을 반환하는 함수 코드를 자문받아 적용.
    6.  4단계 문서화 및 코드 스타일 점검을 위해 core.py의 get_summary 메서드에 요구사항인 사용 예시(>>>)를 포함한 docstring을 추가. 이후 pycodestyle 실행 과정에서 발생한 공백 및 줄 바꿈(W293, E302, W292), 줄 길이 초과(E501) 등의 PEP 8 스타일 경고를 해결하기 위한 코드 수정 가이드를 받아 오류 없이 완벽하게 적용함.
        * todo_manager/core.py:30:1: W293 blank line contains whitespace
          todo_manager/core.py:32:1: W293 blank line contains whitespace
          todo_manager/subclass.py:3:1: E302 expected 2 blank lines, found 1
          todo_manager/subclass.py:36:80: E501 line too long (94 > 79 characters)
          todo_manager/subclass.py:36:95: W292 no newline at end of file
          todo_manager/utils.py:3:1: E302 expected 2 blank lines, found 1
          todo_manager/utils.py:8:56: W292 no newline at end of file
    7.  5단계 단위 테스트 작성을 위해 pytest를 활용하여 총 8개의 테스트 케이스(정상 동작 확인 5건, 빈 문자열/잘못된 타입/잘못된 규칙 입력 등의 엣지 케이스 3건) 코드를 자문받아 test_core.py에 적용하고 모든 테스트가 통과함을 확인.
    8.  6단계 패키지 배포 및 문서화 준비를 위해 setup.py와 requirements.txt의 필수 메타데이터 작성법을 가이드받고, 평가 기준의 6가지 필수 항목이 모두 포함된 README.md 초안을 제공받아 작성 후 패키지 로컬 설치(pip install .) 과정을 검증함.
        * todo_manager/README.md