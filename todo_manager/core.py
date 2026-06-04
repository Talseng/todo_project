class Task:
    """할 일(Task)을 관리하는 기본 부모 클래스입니다."""

    def __init__(self, title, due_date=None, priority="Medium", tags=None):
        """
        Task 객체를 초기화합니다.
        :param title: 할 일의 제목
        :param due_date: 마감 기한 (기본값: None)
        :param priority: 우선순위 (기본값: Medium)
        :param tags: 태그 목록 (기본값: 빈 리스트)
        """
        self._validate_title(title)
        self.title = title
        self.due_date = due_date
        self.priority = priority
        self.tags = tags if tags is not None else []
        self.is_completed = False

    def _validate_title(self, title):
        """제목이 유효한지 검사하는 비공개(non-public) 메서드입니다."""
        if not title or not isinstance(title, str):
            raise ValueError("제목은 비어있지 않은 문자열이어야 합니다.")

    def complete(self):
        """할 일을 완료 상태로 변경합니다."""
        self.is_completed = True

    def get_summary(self):
        """
        할 일의 요약 정보를 반환합니다.

        :return: 할 일의 상태, 제목, 마감 기한이 포함된 요약 문자열

        >>> task = Task("파이썬 과제", "2026-06-10")
        >>> task.get_summary()
        '[미완료] 파이썬 과제 (마감: 2026-06-10)'
        """
        status = "완료" if self.is_completed else "미완료"
        return f"[{status}] {self.title} (마감: {self.due_date})"

    def to_dict(self):
        """객체 데이터를 딕셔너리 형태로 반환합니다 (JSON 저장용)."""
        return {
            "title": self.title,
            "due_date": self.due_date,
            "priority": self.priority,
            "tags": self.tags,
            "is_completed": self.is_completed
        }
