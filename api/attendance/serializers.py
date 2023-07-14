from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    work_time = serializers.SerializerMethodField() # 總工時(小時為單位,有小數點)
    break_time = serializers.SerializerMethodField() # 休息時間

    class Meta:
        model = Attendance
        fields = ('id', 'employee_number', 'check_in', 'check_out', 'work_time', 'break_time')

    def get_work_time(self, obj):
        if obj.check_out and obj.check_in:
            return round((obj.check_out - obj.check_in).total_seconds() / 3600, 2)
        
    def get_break_time(self, obj):
        # TODO
        # 中午休息時間為 12:00 - 13:30, 直接回傳 1.5 hours           
        return 1.5
        
    def validate(self, data):            
        if data['check_in'] and data['check_out'] and data['check_in'] > data['check_out']:
        # if data['check_in'] > data['check_out']:
            raise serializers.ValidationError("上班時間不能大於下班時間")
        return data
        
