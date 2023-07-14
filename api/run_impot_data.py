import json
from attendance.models import Attendance

with open('member.json') as f:
    data = json.load(f)
    for record in data:
        employee_number = record['employeeNumber']
        try:            
            check_in = record['clockIn']
        except:
            check_in = record['clockIn ']        
        check_out = record['clockOut']    

        Attendance.objects.create(employee_number=employee_number, check_in=check_in,  check_out=check_out)
