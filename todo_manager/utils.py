from datetime import datetime


def get_current_timestamp():
    """
    현재 시간을 문자열(YYYY-MM-DD HH:MM:SS)로 반환하는 도우미 함수입니다.
    이후 할 일 생성 시간 등을 기록할 때 사용할 수 있습니다.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
