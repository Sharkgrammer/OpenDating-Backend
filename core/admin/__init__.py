from .user import *
from .user_image import *
from .interest import *
from .interest_cat import *
from .stat import *
from .like import *
from .message import *

from core.models.user import User
from core.models.user_image import UserImage
from core.models.interest import Interest
from core.models.interest_cat import InterestCategory
from core.models.stat import Stat
from core.models.like import Like
from core.models.message import Message

admin.site.register(User, UserAdmin)
admin.site.register(UserImage, UserImageAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(InterestCategory, InterestCategoryAdmin)
admin.site.register(Stat, StatAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Message, MessageAdmin)
