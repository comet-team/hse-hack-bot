from .members import MembersView
from .admin import AdminView
from .notify import NotifyView

HANDLERS = (MembersView, AdminView, NotifyView)
