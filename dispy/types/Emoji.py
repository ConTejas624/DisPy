class Emoji:
    def __init__(self, data: dict) -> None:
        self.id = data['id']    # Snowflake
        self.data = data

async def list_guild_emojis(guild_id) -> list(Emoji):
    # GET /guilds/guild.id/emojis
    pass

async def get_guild_emoji(guild_id, emoji_id) -> Emoji:
    # GET /guilds/guild.id/emojis/emoji.id
    pass

async def create_guild_emoji(guild_id):
    # POST /guilds/guild.id/emojis
    pass

async def modify_guild_emoji(guild_id, emoji_id):
    # PATCH /guilds/guild.id/emojis/emoji.id
    pass

async def delete_guild_emoji(guild_id, emoji_id):
    # DELETE /guilds/guild.id/emojis/emoji.id
    pass