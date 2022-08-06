from django.shortcuts import render
from django.views import View

import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt

from .models import Score

# Create your views here.
class Game_view(View):

    @csrf_exempt
    def get(self, request, *args, **kwargs):

        #レスポンスオブジェクトを作り、その上で.set_cookie()を使い、Cookieを生成する。
        response = render(request, "game/index.html")
        response.set_cookie("user_name", "syungsan")

        return response

    # @ensure_csrf_cookie
    @csrf_exempt
    def post(self, request, *args, **kwargs):

        if request.method == 'GET':
            return JsonResponse({})

        # JSON文字列
        datas = json.loads(request.body)
        print(datas)

        score = Score(userName=datas["userName"],
                      questionNumber=datas["questionNumber"],
                      question=datas["question"],
                      correctAnswer=datas["correctAnswer"],
                      userAnswer=datas["userAnswer"],
                      responseTime=datas["responseTime"])
        score.save()

        ret = {"data": "userName:" + datas["userName"] +
                       ", questionNumber:" + datas["questionNumber"] +
                       ", question:" + datas["question"] +
                       ", correctAnswer:" + datas["correctAnswer"] +
                       ", userAnswer:" + datas["userAnswer"] +
                       ", responseTime:" + datas["responseTime"]}

        # JSONに変換して戻す
        return JsonResponse(ret)

game = Game_view.as_view()
