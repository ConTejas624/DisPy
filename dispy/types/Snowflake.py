import datetime

class Snowflake:
    def __init__(self, id: int) -> None:
        self.id = id
        self.timestamp = None

    def __time__(self) -> datetime.datetime:
        if self.timestamp == None:
            # TODO: implement parsing of timestamp from snowflake id
            pass
        else:
            return self.timestamp