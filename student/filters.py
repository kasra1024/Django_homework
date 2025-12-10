from django_filters import filterset
from django_filters import rest_framework as filters
from .models import Course


class CourseFilter(filterset.FilterSet) : 
    # search = filters.CharFilter(field_name="title" , lookup_expr="contains")
    # code_max2 = filters.NumberFilter(field_name="code" , lookup_expr="gt")
    # code_exact = filters.NumberFilter(field_name="code" , lookup_expr="exact")
    # code = filters.RangeFilter(field_name="code")
    code = filters.NumberFilter(field_name="code" , method="filterset_code")
    class Meta : 
        model = Course
        fields = ["active" , "code"] 

    def filterset_code (self , queryset , name, value) : 
        print (name)
        return queryset.filter(code__gt = value)
    

# unit filters