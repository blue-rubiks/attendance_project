from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from .models import Attendance
from .serializers import AttendanceSerializer
from datetime import datetime, date, time


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    parser_classes = (JSONParser,)

    # [GET] api/attendance/
    # [GET] api/attendance/?date=value
    # ex : http://0.0.0.0/api/attendance/?date=2022-01-05
    def list(self, request, **kwargs):
        date_value = request.query_params.get('date')
        if date_value:
            attends = Attendance.objects.filter(check_in__date = date_value)
        else:
            # today
            date_value = date.today()
            attends = Attendance.objects.filter(check_in__date = date_value)
        
        serializer = AttendanceSerializer(attends, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # [POST] api/attendance/
    # 實現一 API,提供打卡功能    
    def create(self, request, **kwargs):
        serializer = AttendanceSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)        
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # [PATCH] api/attendance/<attendance_id>/
    # 實現一 API,提供補打卡功能,使漏打上班或下班員工可以進行補打卡
    def partial_update(self, request, *args, **kwargs):        
        instance = self.get_object()
        serializer = AttendanceSerializer(instance, data=request.data, partial=True)        
        serializer.is_valid(raise_exception=True)  
        self.perform_update(serializer)

        return Response(serializer.data)
    
    # 實現一 API,可以列出 指定日期,當天前五名 最早打卡上班 的員工
    # [GET] /api/attendance/earliest_clock_in_employees/?date=value
    # http://0.0.0.0/api/attendance/earliest_clock_in_employees/?date=2022-01-05
    @action(detail=False, methods=['get'], url_path='earliest_clock_in_employees')
    def earliest_clock_in_employees(self, request):        
        date_value = request.query_params.get('date')
        attends = Attendance.objects.filter(check_in__date = date_value).order_by('check_in')[:5]
        serializer = AttendanceSerializer(attends, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 實現一 API,可以列出指定 日期區間 未打下班卡的員工清單
    # [GET] /api/attendance/no_check_out_employees/?start_date=value&end_date=value2
    # http://0.0.0.0/api/attendance/no_check_out_employees/?start_date=2022-01-03&end_date=2022-01-06
    @action(detail=False, methods=['get'], url_path='no_check_out_employees')
    def no_check_out_employees(self, request):        
        start_date_value = request.query_params.get('start_date')
        end_date_value = request.query_params.get('end_date')

        start_date_obj = datetime.strptime(start_date_value, '%Y-%m-%d').date()
        end_date_obj = datetime.strptime(end_date_value, '%Y-%m-%d').date()

        start_dt = datetime.combine(start_date_obj, time.min)
        end_dt = datetime.combine(end_date_obj, time.max)

        attends = Attendance.objects.filter(check_in__range = [start_dt, end_dt], check_out__isnull=True)
        serializer = AttendanceSerializer(attends, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    