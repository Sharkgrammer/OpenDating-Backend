from .user import *
from .user_image import *

from core.models.user import User
from core.models.user_image import UserImage

admin.site.register(User, UserAdmin)
admin.site.register(UserImage, UserImageAdmin)
