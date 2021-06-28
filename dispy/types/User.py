import asyncio

class User:
    def __init__(self, args: dict) -> None:
        self.id = args['id'] # snowflake
        self.username = args['username']
        self.discriminator = args['discriminator']
        
        # following are optional or can be null -> use .get()
        self.avatar = args.get('avatar', None)
        self.bot = args.get('bot', False) == 'true'
        self.system = args.get('system', False) == 'true'
        self.mfa_enabled = args.get('mfa_enabled', False) == 'true'
        self.locale = args.get('locale', None)
        self.verified = args.get('verified', False) == 'true'
        self.email = args.get('email', None)
        self.flags = int(args.get('flags', 0))
        self.premium_type = int(args.get('premium_type', 0))
        self.public_flags = int(args.get('public_flags', 0))
    
async def get_self_user() -> User:
    # TODO: HTTP request
    pass

async def get_user(user_id) -> User:
    # API: GET /users/{user.id}
    pass

async def modify_self() -> User:
    # API: PATCH /users/@me
    pass

async def get_guilds(): # returns a list of partial guilds
    # API: GET /users/@me/guilds
    pass

async def leave_guild(guild_id): # returns a 204 empty
    # API: DELETE /users/@me/guilds/{guild.id}
    pass

async def create_dm(recipient_id): # returns a dm channel object
    # API: POST /users/@me/channels
    pass

async def get_connections(): # returns list of connections objects
    # API: GET /users/@me/connections
    pass

# skipped methods for create group dm