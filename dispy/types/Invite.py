class Invite:
    def __init__(self, data: dict) -> None:
        self.data = data

async def get_invite(invite_code):
    # GET /invites/invite.code
    pass

async def delete_invite(invite_code):
    # DELETE /invites/invite.code
    pass