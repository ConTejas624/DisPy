import asyncio
from dispy.types.minors.Message import Message

class Channel:
    def __init__(self, data: dict) -> None:
        self.id = data['id']
        self.type = data['type']

        self.guild_id = data.get('guild_id', 0) # Snowflake
        self.position = int(data.get('position', 0))
        self.permission_overwrites = data.get('permission_overwrites', 0)
        self.name = data.get('name', None)
        self.topic = data.get('topic', None)
        self.nsfw = data.get('nsfw', 'false') == 'true'
        self.last_message_id = data.get('last_message_id', 0) # Snowflake
        self.bitrate = int(data.get('bitrate', 0))
        self.user_limit = int(data.get('user_limit', 0))
        self.rate_limit_per_user = int(data.get('rate_limit_per_user', 0))
        self.recipients = data.get('recipients', None) # Array of user objects
        self.icon = data.get('icon', None)
        self.owner_id = data.get('owner_id', 0)     # Snowflake
        self.application_id = data.get('application_id', 0)     # Snowflake
        self.parent_id = data.get('parent_id', 0)   # Snowflake
        self.last_pin_timestamp = data.get('last_pin_timestamp', None)  # ISO8601 timestamp
        self.rtc_region = data.get('rtc_region', None)
        self.video_quality_mode = int(data.get('video_quality_mode', 0))
        self.message_count = int(data.get('message_count', 0))
        self.member_count = int(data.get('member_count', 0))
        self.thread_metadata = data.get('thread_metadata', None) # thread metadata object
        self.member = data.get('member', None) # thread member object
        self.default_auto_archive_duration = int(data.get('default_auto_archive_duration', 0))


async def get_channel(channel_id) -> Channel:
    # GET /channels/channel.id
    pass

async def modify_channel(channel) -> Channel:
    # PATCH /channels/channel.id
    pass

async def delete_channel(channel_id) -> Channel:
    # DELETE /channels/channel.id
    pass

async def get_channel_messages(channel_id) -> list(Message):
    # GET /channels/channel.id/messages
    pass

async def get_channel_message(channel_id, message_id) -> Message:
    # GET /channels/channel.id/messages/message.id
    pass

async def create_message(channel_id, message) -> Message:
    # POST /channels/channel.id/messages
    pass

async def crosspost_message(channel_id, message_id) -> Message:
    # POST /channels/channel.id/messages/message.id/crosspost
    pass

async def create_reaction(channel_id, message_id, emoji): # 204 empty
    # PUT /channels/channel.id/messages/message.id/reactions/emoji/@me
    pass

async def delete_own_reaction(channel_id, message_id, emoji): # 204 empty