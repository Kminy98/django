from django.http import HttpResponse
from django.shortcuts import render


def base_response(request):
    return HttpResponse("안녕하세요! 장고의 시작입니다!")

#my_test.html을 보여주는 함수
def first_view(request):
    return render(request, 'my_test.html')


from django.shortcuts import render