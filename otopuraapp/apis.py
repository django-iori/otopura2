from rest_framework import viewsets, routers, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import *
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class HostViewSet(viewsets.ModelViewSet):
    queryset = HostModel.objects.all()
    serializer_class = HostSerializer

class BandViewSet(viewsets.ModelViewSet):
    queryset = BandModel.objects.all()
    serializer_class = BandSerializer

class MypageViewSet(viewsets.ViewSet):
    def mypage(self, request):
        queryset = UserInfo.objects.all(name=request.user)
        print(queryset)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)






    """@action(methods=['get'], detail=False)
    def msg_list(self, request):
        return print(self.get_queryset())"""




router = routers.DefaultRouter()
router.register(r'hostapi', HostViewSet)
router.register(r'bandapi', BandViewSet)
router.register(r'mypageapi', MypageViewSet, basename='mypage')

