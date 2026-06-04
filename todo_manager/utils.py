import json
from datetime import datetime


def get_current_timestamp():
    """
    현재 시간을 문자열(YYYY-MM-DD HH:MM:SS)로 반환하는 도우미 함수입니다.
    이후 할 일 생성 시간 등을 기록할 때 사용할 수 있습니다.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def save_tasks_to_json(tasks, filename="tasks.json"):
    """
    할 일(Task) 객체 리스트를 JSON 파일로 저장하는 함수입니다.
    :param tasks: Task(또는 RecurringTask) 객체들이 담긴 리스트
    :param filename: 저장할 JSON 파일 이름 (기본값: tasks.json)
    """
    # 각 Task 객체의 to_dict() 메서드를 호출해 딕셔너리로 변환
    tasks_data = [task.to_dict() for task in tasks]

    # JSON 파일로 쓰기 (한글 깨짐 방지를 위해 ensure_ascii=False 설정)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(tasks_data, f, ensure_ascii=False, indent=4)
