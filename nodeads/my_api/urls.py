from django.urls import path, include
from . import views
from .resources import GroupResource, ElementResource

group_resource = GroupResource()
element_resource = ElementResource()

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(group_resource.urls)),
    path('', include(element_resource.urls))

]
