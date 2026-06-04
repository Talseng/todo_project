import pytest
import os
import json
from todo_manager.core import Task
from todo_manager.subclass import RecurringTask
from todo_manager.utils import save_tasks_to_json

def test_task_creation():
    """정상적인 Task 생성을 테스트합니다."""
    task = Task("파이썬 공부", priority="High", tags=["공부", "코딩"])
    assert task.title == "파이썬 공부"
    assert task.priority == "High"
    assert "코딩" in task.tags

def test_task_empty_title():
    """[엣지 케이스] 빈 제목 입력 시 예외 발생을 테스트합니다."""
    with pytest.raises(ValueError):
        Task("")

def test_task_invalid_title_type():
    """[엣지 케이스] 잘못된 타입(숫자) 입력 시 예외 발생을 테스트합니다."""
    with pytest.raises(ValueError):
        Task(123)

def test_task_completion():
    """Task 완료 처리 기능을 테스트합니다."""
    task = Task("운동하기")
    assert not task.is_completed
    task.complete()
    assert task.is_completed

def test_recurring_task_creation():
    """정상적인 RecurringTask 생성을 테스트합니다."""
    rtask = RecurringTask("매일 걷기", recurrence_rule="daily")
    assert rtask.recurrence_rule == "daily"
    assert rtask.completion_count == 0

def test_recurring_task_invalid_rule():
    """[엣지 케이스] 잘못된 반복 규칙 입력 시 예외 발생을 테스트합니다."""
    with pytest.raises(ValueError):
        RecurringTask("잘못된 규칙", recurrence_rule="yearly")

def test_recurring_task_completion():
    """RecurringTask 완료 시 누적 횟수 증가를 테스트합니다."""
    rtask = RecurringTask("물 마시기", recurrence_rule="daily")
    rtask.complete()
    assert rtask.is_completed
    assert rtask.completion_count == 1

def test_to_dict_conversion():
    """Task 객체가 딕셔너리로 올바르게 변환되는지 테스트합니다."""
    task = Task("JSON 테스트", due_date="2026-06-10", priority="Low")
    data = task.to_dict()
    assert data["title"] == "JSON 테스트"
    assert data["priority"] == "Low"
    assert data["is_completed"] is False

def test_save_tasks_to_json(tmp_path):
    """
    임시 디렉터리(tmp_path)를 사용하여 JSON 파일 저장 기능을 테스트합니다.
    (실제 바탕화면에 쓰레기 파일이 남지 않도록 해주는 pytest의 고급 기능입니다!)
    """
    tasks = [
        Task("일반 할 일"),
        RecurringTask("반복 할 일", recurrence_rule="weekly")
    ]
    
    # 가상의 임시 파일 경로 생성
    file_path = tmp_path / "test_tasks.json"
    
    # 함수 실행 (파일 저장)
    save_tasks_to_json(tasks, str(file_path))
    
    # 파일이 실제로 만들어졌는지 확인
    assert file_path.exists()
    
    # 파일 내용이 올바르게 저장되었는지 열어서 확인
    with open(file_path, "r", encoding="utf-8") as f:
        loaded_data = json.load(f)
        
    assert len(loaded_data) == 2
    assert loaded_data[0]["title"] == "일반 할 일"
    assert loaded_data[1]["recurrence_rule"] == "weekly"
