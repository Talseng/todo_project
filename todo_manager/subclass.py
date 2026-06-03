from .core import Task


class RecurringTask(Task):
    """반복되는 할 일(Recurring Task)을 관리하는 자식 클래스입니다."""

    def __init__(self, title, due_date=None, recurrence_rule="daily"):
        """
        RecurringTask 객체를 초기화합니다.
        부모 클래스의 생성자를 super()로 호출하여 기본 속성을 설정합니다.
        """
        super().__init__(title, due_date)
        self._validate_rule(recurrence_rule)
        self.recurrence_rule = recurrence_rule
        self.completion_count = 0

    def _validate_rule(self, rule):
        """
        반복 규칙이 유효한지 검사하는 비공개(non-public) 메서드입니다.
        (과제 요구사항 충족용)
        """
        valid_rules = ["daily", "weekly", "monthly"]
        if rule not in valid_rules:
            raise ValueError(f"반복 규칙은 {valid_rules} 중 하나여야 합니다.")

    def complete(self):
        """
        할 일을 완료 처리하고, 완료 횟수를 1 증가시킵니다.
        부모 클래스의 complete() 메서드를 super()로 호출합니다.
        """
        super().complete()
        self.completion_count += 1

    def get_summary(self):
        """반복 할 일의 요약 정보를 반환합니다."""
        base_summary = super().get_summary()
        return (
            f"{base_summary} (반복: {self.recurrence_rule}, "
            f"누적 완료: {self.completion_count}회)"
        )
