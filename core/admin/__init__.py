from .user import *
from .user_image import *
from .interest import *
from .interest_cat import *

from core.models.user import User
from core.models.user_image import UserImage
from core.models.interest import Interest
from core.models.interest_cat import InterestCategory

admin.site.register(User, UserAdmin)
admin.site.register(UserImage, UserImageAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(InterestCategory, InterestCategoryAdmin)
