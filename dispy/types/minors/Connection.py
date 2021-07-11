class Connection:
    def __init__(self, data: dict) -> None:
        self.id = data['id']    # Snowflake
        self.name = data['names']
        self.type = data['type']
        self.revoked = data.get('revoked', 'false') == 'true'
        self.integrations = data.get('integrations', None)  # partial server integrations array
        self.verified = data['verified']
        self.friend_sync = data['friend_sync'] == 'true'
        self.show_activity = data['show_activity'] == 'true'
        self.visibility = int(data['visibility'])   # 0 (only self-visible) or 1 (everyone visible)
