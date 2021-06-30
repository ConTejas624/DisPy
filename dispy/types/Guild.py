
from dispy.types.User import User
import asyncio


class Guild:
    # no support for threads
    def __init__(self, args: dict) -> None:
        self.id = int(args['id'])
        self.name = args['name']
        self.icon = args.get('icon', None)
        self.icon_hash = args.get('icon_hash', None)
        self.splash = args.get('splash', None)
        self.discovery_splash = args.get('discovery_splash', None)
        self.owner = args.get('owner', False) == 'true'
        self.owner_id = int(args['owner_id'])
        self.permissions = args.get('permissions', None)
        self.region = args.get('region', None)
        self.afk_channel_id = int(args.get('afk_channel_id', None))
        self.afk_timeout = int(args.get('afk_timeout', None))
        self.widget_enabled = args.get('widget_enabled', False) == True
        self.widget_channel_id = int(args.get('widget_channel_id', 0))
        self.verification_level = int(args['verification_level'])
        self.default_message_notifications = int(args['default_me'])
        self.explicit_content_filter = int(args['explicit_content_filter'])
        self.roles = args['roles']
        self.emojis = args['emoji']
        self.features = args['features']
        self.mfa_level = int(args['mfa_level'])
        self.application_id = int(args.get('application_id', 0))
        self.system_channel_id = int(args.get('system_channel_id', 0))
        self.system_channel_flags = int(args['system_channel_flags'])
        self.rules_channel_id = int(args.get('rules_channel_id', 0))
        self.joined_at = args.get('joined_at', None) # ISO8601 timestamp
        self.large = args.get('large', False) == 'true'
        self.unavailable = args.get('unavailable', False) == 'true'
        self.member_count = int(args.get('member_count', 0))
        self.voice_states = args.get('voice_states', None)
        self.members = args.get('members', None)
        self.channels = args.get('channels', None)
        self.presences = args.get('presences', None)
        self.max_presences = int(args.get('max_presences', None))
        self.max_members = int(args.get('max_members', None))
        self.vanity_url_code = args.get('vanity_url_code', None)
        self.description = args.get('description', None)
        self.banner = args.get('banner', None)
        self.premium_tier = int(args['premium_tier'])
        self.premium_subscription_count = int(args.get('premium_subscription_count', 0))
        self.preferred_locale = args['preffered_locale']
        self.public_updates_channel_id = int(args.get('public_updates_channel_id', 0))
        self.max_video_channel_users = int(args.get('max_video_channel_users', 0))
        self.approximate_member_count = int(args.get('approximate_member_count', 0))
        self.approximate_presence_count = int(args.get('approximate_precense_count', 0))
        self.welcome_screen = args.get('welcome_screen', None)
        self.nsfw_level = int(args['nsfw_level'])
        self.stage_instances = args.get('stage_instances', None)
        self.stage_instances = args.get('stage_instances', None)

async def create_guild(guild_dict) -> Guild:
    # API: POST /guilds
    pass

async def get_guild(guild_id) -> Guild:
    # API: GET /guilds/{guild.id}
    pass

async def get_guild_preview(guid_id): # returns guild preview object
    # API: GET /guilds/{guild.id}/preview
    pass

async def modify_guild(guild_dict) -> Guild:
    # API: PATCH /guilds/{guild.id}
    pass

async def delete_guild(guild_id):
    # API: DELETE /guilds/{guild.id}
    pass

async def get_guild_channels(guild_id): # returns a list of channels
    # API: GET /guilds/{guild.id}/channels
    pass

async def create_guild_channel(guild_id, channel): # returns a channel
    # API: POST /guilds/{guild.id}/channels
    pass

async def modify_guild_channel_positions(guild_id, channels): # returns empty 204
    # API: PATCH /guilds/{guild.id}/channels
    pass

async def get_guild_member(guild_id, user_id) -> User:
    # API: GET /guilds/{guild.id}/members/{user.id}
    pass

async def list_guild_members(guild_id): # returns a list fo guild member objects
    # API: GET /guilds/{guild.id}/members
    pass

async def search_guild_members(guild_id, query): # returns a list of guild members
    # API: GET /guilds/{guild.id}/members/search
    pass

async def add_guild_member(guild_id, user_id): # returns 201 created or 204 no content
    # API: PUT /guilds/{guild.id}/members/{user.id}
    pass

async def modify_guild_member(guild_id, user_id): # returns a 200 ok
    # API: PATCH /guilds/{guild.id}/members/{user.id}
    pass

async def modify_self_nickname(guild_id): # 200 on success
    # API: PATCH /guilds/{guild.id}/members/@me/nick
    pass

async def add_guild_member_role(guild_id, user_id, role_id): #204 empty on success
    # API: PUT /guilds/{guild.id}/members/{user.id}/roles/{role.id}
    pass

async def remove_guild_member_role(guild_id, user_id, role_id): # 204 empty on success
    # API: DELETE /guilds/{guild.id}/members/{user.id}/roles/{role.id}
    pass

async def remove_guild_member(guild_id, user_id): #204 empty on success
    # API: DELETE /guilds/{guild.id}/member/{user.id}
    pass

async def get_guild_bans(guild_id): # list of ban objects
    # API: GET /guilds/{guild.id}/bans
    pass

async def get_guild_ban(guild_id, user_id): # ban object or 404
    # API: GET /guilds/{guild.id}/bans/{user.id}
    pass

async def create_guild_ban(guild_id, user_id): #204 empty on success
    # API: PUT /guilds/{guild.id}/bans/{user.id}
    pass

async def remove_guild_ban(guild_id, user_id): #204 empty on success
    # API: DELETE /guilds/{guild.id}/bans/{user.id}
    pass

async def get_guild_roles(guild_id): # returns a list of role objects
    # API: GET /guilds/{guild.id}/roles
    pass

async def create_guild_role(guild_id, role): # returns role oobject
    # API: POST /guilds/{guild.id}/roles
    pass

async def modify_guild_role_positions(guild_id, params): # returns list of guild's role objects
    # API: PATCH /guilds/{guild.id}/roles
    pass

async def modify_guild_role(guild_id, role): # returns updated role
    # API: GET /guilds/{guild.id}/roles/{role.id}
    pass

async def delete_guild_role(guild_id, role_id): # returns 204 on success
    # API: DELETE /guilds/{guild.id}/roles/{role.id}
    pass

async def get_guild_prune_count(guild_id, params):
    # GET /guilds/{guild.id}/prune
    pass

async def begin_guild_prune(guild_id, params):
    # POST /guilds/{guild.id}/prune
    pass

async def get_guild_voice_regions(guild_id):
    # GET /guilds/{guild.id}/regions
    pass

async def get_guild_invites(guild_id):
    # GET /guilds/{guild.id}/invites
    pass

async def get_guild_integrations(guild_id):
    # GET /guilds/{guild.id}/integrations
    pass

async def delete_guild_integration(guild_id, integration):
    # DELETE /guilds/{guild.id}/integrations/{integration.id}
    pass

async def get_guild_widget_settings(guild_id):
    # GET /guilds/{guild.id}/widget
    pass

async def modify_guild_widget(guild_id, widget):
    # PATCH /guilds/{guild.id}/widget
    pass

async def get_guild_widget(guild_id):
    # GET /guilds/{guild.id}/widget.json
    pass

async def get_guild_vanity_url(guild_id):
    # GET /guilds/{guild.id}/vanity-url
    pass

async def get_guild_widget_image(guild_id):
    # GET /guilds/{guild.id}/widget.png
    pass

async def get_guild_welcome_screen(guild_id):
    # GET /guilds/{guild.id}/welcome-screen
    pass

async def modify_guild_welcome_screen(guild_id, params):
    # PATCH /guilds/{guild.id}/welcome-screen
    pass

async def modify_self_user_state(guild_id, params):
    # PATCH /guilds/{guild.id}/voice-states/@me
    pass

async def modify_user_voice_state(guild_id, user, params):
    # PATCH /guilds/{guild.id}/voice-states/{user.id}
    pass