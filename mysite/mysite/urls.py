"""
お試し おすすめのラジオ番組を表示するアプリを作成する
平日の昼間に生活の知恵=ジェーン・スー
笑って楽しみたい＝スマイルサミット
今売れている音楽を聴きたい＝ファンフラpart1
今売れている洋楽を聴きたい＝ファンフラpart2
秀逸な話を聴きたい=ファンフラpart3
発売されたばかりの音楽を聴きたい=水曜キラスタ
最終目的の音楽だけ決めて、そこに辿り着くまではリスナーが選曲リレー形式で楽しめる＝水曜九の音域

URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('selectradioproject.urls')),
    ]
