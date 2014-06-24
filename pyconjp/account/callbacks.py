def account_delete_expunge(deletion):
    deletion.user.delete()
    deletion.user = None
