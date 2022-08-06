from django.contrib import admin

# Register your models here.

# モデルをインポート
from . models import Score

# 管理ツールに登録
admin.site.register(Score)
