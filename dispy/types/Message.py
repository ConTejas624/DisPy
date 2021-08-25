class Message:
    def __init__(self, data: dict) -> None:
        self.id = data['id']
        self.data = data

