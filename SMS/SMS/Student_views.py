from django.shortcuts import redirect,render
from app.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def HOME(request):
    return render(request, "Student/home.html")

@login_required(login_url='/')
def STUD_NOTIFICATION(request):
    student = Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id = i.id
        notification = Student_Notification.objects.filter(student_id=student_id)
        cntxt = {'notification':notification}
        return render(request, "Student/notification.html", cntxt)

@login_required(login_url='/')    
def NOTI_MARK_AS_DONE(request,status):
    notification = Student_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('Stud_Notification')

@login_required(login_url='/')
def STUD_FEEDBACK(request):
    student_id = Student.objects.get(admin=request.user.id)
    feedback_history = Student_Feedback.objects.filter(student_id=student_id)
    cntxt = {'feedback_history':feedback_history}
    return render(request, "Student/feedback.html", cntxt)

@login_required(login_url='/')
def STUD_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')
        stud_id = Student.objects.get(admin=request.user.id)
        feedbacks = Student_Feedback(
            student_id = stud_id,
            feedback = feedback,
            feedback_reply = "",
        )
        messages.success(request, "Feedback Send Successfully...")
        feedbacks.save()
        return redirect('Stud_Feedback')

@login_required(login_url='/')    
def APPLY_FOR_LEAVE(request):
    student = Student.objects.get(admin = request.user.id)
    leave_history = Student_Leave.objects.filter(student_id = student)
    cntxt = {'leave_history':leave_history}
    return render(request, "Student/apply_leave.html", cntxt)

@login_required(login_url='/')
def STUD_APPLY_LEAVE_SAVE(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')

        student_id = Student.objects.get(admin = request.user.id)
        stud_leave = Student_Leave(
            student_id = student_id,
            data = leave_date,
            message = leave_message,
        )
        stud_leave.save()
        messages.success(request, "Your Leave Applied Successfully...")
        return redirect('Stud_Apply_Leave')

@login_required(login_url='/')    
def STUD_VIEW_ATTENDANCE(request):
    student = Student.objects.get(admin = request.user.id)
    subject = Subject.objects.filter(course = student.course_id)
    action = request.GET.get('action')
    get_subject = None
    attendance_report = None
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            get_subject = Subject.objects.get(id = subject_id)
            attendance_report = Attendance_Report.objects.filter(student_id = student , attendance_id__subject_id = subject_id)
    cntxt = {
        'subject':subject,
        'action':action,
        'get_subject':get_subject,
        'attendance_report':attendance_report,
    }
    return render(request,'student/view_attendance.html',cntxt)

@login_required(login_url='/')
def VIEW_RESULT(request):
    student = Student.objects.get(admin = request.user.id)
    result = Student_Result.objects.filter(student_id = student)
    cntxt = {
        'result':result,
    }
    return render(request,'Student/view_result.html',cntxt)

