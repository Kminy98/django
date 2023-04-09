from django.shortcuts import render,redirect
from .models import UserModel

# HttpResponse 화면에 글자를 띄울 때 사용
from django.http import HttpResponse

# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    elif request.method == 'POST':
        # request.POST는 POST로 온 데이터를 받는다는 의미
        # .get('username',None)는
        # 많은 데이터중에 'username'이라는 이름으로 되어있는 데이터를 가지고 오는데
        # username이 없으면 None으로 빈칸 처리하겠다는 의미
        # 이렇게 가져온 정보를 username이라는 변수에 저장
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        password2 = request.POST.get('password2',None)
        bio = request.POST.get('bio',None)
        
        # password가 같아야 회원가입이 되도록하기
        # password와 password2가 같지 않으면 다시한번 화면을 보여주기
        if password != password2:
            return render(request, 'user/signup.html')
        # 같으면 user를 저장
        else:
            new_user = UserModel()
            # request.POST해온 username을  UserModel()의 username에 담는다
            new_user.username = username
            new_user.password = password
            new_user.bio = bio
            # new_user는 저장이 되어있지만 
            # 실제로 우리 데이터베이스에는 저장이 안되어있는 상태임
            # 실제로 데이터베이스에 저장하기 위해 코드작성
            new_user.save()

        # 회원가입이 완료되었을때만 실행
        # 회원가입페이지말고 로그인페이지를 보여주고 싶음
        # return에 redirect()함수를 사용하여 sign-in url을 작성
        return redirect('/sign-in')



def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)

        # 기존에 유저가 있으면
        # UserModel을 .objects로 불러오기
        # UserModel은 이미 데이터베이스와 연결되어있는 객체(클래스)라고 생각하면 됨
        # .get(username=username) 어떤 데이터를 가져올껀지 조건을 써줌
        # (username(UserModel안에있던것)=username(post에서 받아온 값))
        # 이러면 me는 회원가입한 사용자들만 불러올 수 있게됨
        me = UserModel.objects.get(username=username)

        return HttpResponse("로그인 성공!")
        
    elif request.method == 'GET':
        return render(request, 'user/signin.html')
        
        
        
        

