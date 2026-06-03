import pytest
from todo_manager.core import Task
from todo_manager.subclass import RecurringTask


# --- 정상 케이스 (5건) ---

def test_task_creation():
    """Task 객체가 정상적으로 생성되는지 테스트"""
    task = Task("파이썬 과제", "2026-06-10")
    assert task.title == "파이썬 과제"
    assert task.due_date == "2026-06-10"
    assert task.is_completed is False


def test_task_complete():
    """Task 완료 처리가 정상적으로 작동하는지 테스트"""
    task = Task("운동하기")
    task.complete()
    assert task.is_completed is True


def test_task_get_summary():
    """Task 요약 문자열이 올바른 포맷으로 반환되는지 테스트"""
    task = Task("독서")
    assert task.get_summary() == "[미완료] 독서 (마감: None)"
    task.complete()
    assert task.get_summary() == "[완료] 독서 (마감: None)"


def test_recurring_task_creation():
    """RecurringTask 객체가 정상적으로 생성되는지 테스트"""
    rtask = RecurringTask("매일 운동", recurrence_rule="daily")
    assert rtask.title == "매일 운동"
    assert rtask.recurrence_rule == "daily"
    assert rtask.completion_count == 0


def test_recurring_task_complete():
    """RecurringTask의 완료 처리 시 누적 횟수가 증가하는지 테스트"""
    rtask = RecurringTask("주간 회의", recurrence_rule="weekly")
    rtask.complete()
    assert rtask.is_completed is True
    assert rtask.completion_count == 1
    rtask.complete()
    assert rtask.completion_count == 2


# --- 엣지 케이스 (3건) ---

def test_task_empty_title():
    """빈 문자열로 Task 생성 시 ValueError가 발생하는지 테스트"""
    with pytest.raises(ValueError, match="비어있지 않은 문자열"):
        Task("")


def test_task_invalid_type_title():
    """잘못된 타입(정수)으로 Task 생성 시 ValueError가 발생하는지 테스트"""
    with pytest.raises(ValueError, match="비어있지 않은 문자열"):
        Task(123)


def test_recurring_task_invalid_rule():
    """잘못된 반복 규칙으로 RecurringTask 생성 시 ValueError가 발생하는지 테스트"""
    with pytest.raises(ValueError, match="반복 규칙은"):
        RecurringTask("잘못된 규칙", recurrence_rule="yearly")
