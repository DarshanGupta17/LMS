from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from app.models import *
from django.contrib import messages

@login_required(login_url='/')
def home(request):
    student_cnt = Student.objects.all().count()
    staff_cnt = Staff.objects.all().count()
    course_cnt = Course.objects.all().count()
    subject_cnt = Subject.objects.all().count()
    student_result = Student_Result.objects.all()
    student_gender_male = Student.objects.filter(gender='Male').count()
    student_gender_female = Student.objects.filter(gender='Female').count()
    activity = Student_Activity.objects.all()
    star_stud = []
    for i in student_result:
        if i.assignment_mark + i.exam_mark >= 80:
            star_stud.append(i)
    cntxt = {
        'student_cnt':student_cnt,
        'staff_cnt':staff_cnt,
        'course_cnt':course_cnt,
        'subject_cnt':subject_cnt,
        'student_gender_male':student_gender_male,
        'student_gender_female':student_gender_female,
        'star_stud':star_stud,
        'activity':activity,
    }
    return render(request,'HOD/home.html', cntxt)

@login_required(login_url='/')
def Add_Student(request):
    course = Course.objects.all()
    session_yr = Session_Year.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        address = request.POST.get('address')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is Already Taken')
            return redirect('Add_Student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username is Already Taken')
            return redirect('Add_Student')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 3
            )
            user.set_password(password)
            user.save()
            course = Course.objects.get(id=course_id)
            session_year = Session_Year.objects.get(id=session_year_id)

            student = Student(
                admin = user,
                address = address,
                session_year_id = session_year,
                course_id = course,
                gender = gender,
            )
            student.save()
            messages.success(request, 'Student Added Successfully.')
            return redirect('View_Student')

    cntxt = {"course":course,"session_yr":session_yr}
    return render(request,'HOD/add_student.html',cntxt)

@login_required(login_url='/')
def VIEW_STUDENT(request):
    student = Student.objects.all()
    cntxt = {'student':student}
    return render(request, 'HOD/view_student.html', cntxt)

@login_required(login_url='/')
def EDIT_STUDENT(request,id):
    student = Student.objects.filter(id=id)
    course = Course.objects.all()
    session_yr = Session_Year.objects.all()
    cntxt = {'student':student,'course':course,'session_yr':session_yr}
    return render(request, 'HOD/edit_student.html', cntxt)

@login_required(login_url='/')
def UPDATE_STUDENT(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        address = request.POST.get('address')

        user = CustomUser.objects.get(id=student_id)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        if password != None and password != "":
            user.set_password(password)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        user.save()

        student = Student.objects.get(admin = student_id)
        student.address = address
        student.gender = gender

        course = Course.objects.get(id = course_id)
        student.course_id = course

        session_year = Session_Year.objects.get(id = session_year_id)
        student.session_year_id = session_year

        student.save()
        messages.success(request, "Student Record Updated Successfully !!!")
        return redirect('View_Student')

    return render(request, 'HOD/edit_student.html')

@login_required(login_url='/')
def DELETE_STUDENT(request,admin):
    student = CustomUser.objects.get(id = admin)
    student.delete()
    messages.success(request, "Student Record Deleted Successfully !!!")
    return redirect('View_Student')

@login_required(login_url='/')
def ADD_COURSE(request):
    if request.method == "POST":
        course_name = request.POST.get('course_name')
        course = Course(
            name = course_name,
        )
        course.save()
        messages.success(request, "Course Added Successfully.")
        return redirect('Add_Course')
    return render(request, 'HOD/add_course.html')

@login_required(login_url='/')
def VIEW_COURSE(request):
    course = Course.objects.all()
    cntxt = {'course':course}
    return render(request, "HOD/view_course.html", cntxt)

@login_required(login_url='/')
def EDIT_COURSE(request,id):
    course = Course.objects.get(id = id)
    cntxt = {'course':course}
    return render(request, "HOD/edit_course.html", cntxt)

@login_required(login_url='/')
def UPDATE_COURSE(request):
    if request.method == "POST":
        name = request.POST.get('name')
        course_id = request.POST.get('course_id')

        course = Course.objects.get(id=course_id)
        course.name = name
        course.save()
        messages.success(request, "Course Record Updated Successfully.")
        return redirect('View_Course')
    return render(request, "HOD/edit_course.html")

@login_required(login_url='/')
def DELETE_COURSE(request,id):
    course = Course.objects.get(id = id)
    course.delete()
    messages.success(request, "Course Record Deleted Successfully.")
    return redirect('View_Course')

@login_required(login_url='/')
def ADD_STAFF(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "Email is Already in Use.")
            return redirect('Add_Staff')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "Username is Already in Use.")
            return redirect('Add_Staff')
        else:
            user = CustomUser(username=username, first_name=first_name, last_name=last_name, email=email, profile_pic=profile_pic, user_type = 2)
            user.set_password(password)
            user.save()

            staff = Staff(
                admin = user,
                address = address,
                gender = gender ,
            )
            staff.save()
            messages.success(request, "Staff Added Successfully.")
            return redirect('Add_Staff') 
    return render(request, "HOD/add_staff.html")

@login_required(login_url='/')
def VIEW_STAFF(request):
    staff = Staff.objects.all()
    cntxt = {'staff':staff}
    return render(request, "HOD/view_staff.html", cntxt)

@login_required(login_url='/')
def EDIT_STAFF(request, id):
    staff = Staff.objects.get(id=id)
    cntxt = {'staff':staff}
    return render(request, "HOD/edit_staff.html", cntxt)

@login_required(login_url='/')
def UPDATE_STAFF(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        user = CustomUser.objects.get(id=staff_id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        if password != None and password != "":
            user.set_password(password)

        user.save()

        staff = Staff.objects.get(admin=staff_id)
        staff.gender = gender
        staff.address = address
        staff.save()
        messages.success(request, "Staff Record Updated Successfully...")
        return redirect('View_Staff')
    return render(request, 'HOD/edit_staff.html')

@login_required(login_url='/')
def DELETE_STAFF(request,admin):
    staff = CustomUser.objects.get(id=admin)
    staff.delete()
    messages.success(request, "Staff Record Deleted Successfully...")
    return redirect('View_Staff')

@login_required(login_url='/')
def ADD_SUBJECT(request):
    course = Course.objects.all()
    staff = Staff.objects.all()

    if request.method == "POST":
        subject_name = request.POST.get("subject_name")
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course = Course.objects.get(id = course_id)
        staff = Staff.objects.get(id = staff_id)

        subject = Subject(
            name = subject_name,
            course = course,
            staff = staff
        )

        subject.save()
        messages.success(request, "Subject Added Successfully...")
        return redirect('View_Subject')

    cntxt = {'course':course, 'staff':staff}
    return render(request, "HOD/add_subject.html", cntxt)

@login_required(login_url='/')
def VIEW_SUBJECT(request):
    subject = Subject.objects.all()
    cntxt = {'subject':subject}
    return render(request, "HOD/view_subject.html", cntxt)

@login_required(login_url='/')
def EDIT_SUBJECT(request,id):
    subject = Subject.objects.get(id = id)
    course = Course.objects.all()
    staff = Staff.objects.all()
    cntxt = {'subject':subject,'course':course,'staff':staff}
    return render(request, "HOD/edit_subject.html",cntxt)

@login_required(login_url='/')
def UPDATE_SUBJECT(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course = Course.objects.get(id = course_id)
        staff = Staff.objects.get(id = staff_id)

        subject = Subject(
            id = subject_id,
            name = subject_name,
            course = course,
            staff = staff,
        )
        subject.save()
        messages.success(request, "Subject Details Updated Successfully...")
        return redirect('View_Subject')
    
@login_required(login_url='/')
def DELETE_SUBJECT(request,id):
    subject = Subject.objects.filter(id = id)
    subject.delete()
    messages.success(request, "Subject Record Deleted Successfully...")
    return redirect('View_Subject')

@login_required(login_url='/')
def ADD_SESSION(request):
    if request.method == "POST":
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')

        session = Session_Year(
            session_start = session_start,
            session_end = session_end,
        )

        session.save()
        messages.success(request, "Session Year Added Successfully...")
        return redirect('View_Session')
    return render(request, "HOD/add_session.html")

@login_required(login_url='/')
def VIEW_SESSION(request):
    session = Session_Year.objects.all()
    cntxt = {'session':session}
    return render(request, "HOD/view_session.html", cntxt)

@login_required(login_url='/')
def EDIT_SESSION(request,id):
    session = Session_Year.objects.filter(id=id)
    cntxt = {'session':session}
    return render(request, "HOD/edit_session.html", cntxt)

@login_required(login_url='/')
def UPDATE_SESSION(request):
    if request.method == "POST":
        session_id = request.POST.get('session_id')
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')

        session = Session_Year(
            id = session_id,
            session_start = session_start,
            session_end = session_end,
        )
        session.save()
        messages.success(request, "Session Record Updated Successfully...")
        return redirect('View_Session')

@login_required(login_url='/')  
def DELETE_SESSION(request,id):
    session = Session_Year.objects.get(id=id)
    session.delete()
    messages.success(request, "Session Record Deleted Successfully...")
    return redirect('View_Session')

@login_required(login_url='/') 
def STAFF_SEND_NOTI(request):
    staff = Staff.objects.all()
    see_notification = Staff_Notification.objects.all()
    cntxt = {'staff':staff,'see_notification':see_notification}
    return render(request, "HOD/staff_notification.html", cntxt)

@login_required(login_url='/') 
def SAVE_STAFF_NOTI(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        message = request.POST.get('message')

        staff = Staff.objects.get(admin=staff_id)
        notification = Staff_Notification(
            staff_id = staff,
            message = message,
        )
        notification.save()
        messages.success(request, "Notification Send Successfully...")
        return redirect('Staff_Send_Noti')

@login_required(login_url='/')  
def STAFF_LEAVE_VIEW(request):
    staff_leave = Staff_Leave.objects.all()
    cntxt = {'staff_leave':staff_leave}
    return render(request, "HOD/staff_leave.html", cntxt)

@login_required(login_url='/') 
def STAFF_APPROVE_LEAVE(request,id):
    leave = Staff_Leave.objects.get(id=id)
    leave.status = 1
    leave.save()
    messages.success(request, "Leave Approved...")
    return redirect('Staff_Leave_View')

@login_required(login_url='/') 
def STAFF_DISAPPROVE_LEAVE(request,id):
    leave = Staff_Leave.objects.get(id=id)
    leave.status = 2
    leave.save()
    messages.success(request, "Leave Disapproved...")
    return redirect('Staff_Leave_View')

@login_required(login_url='/') 
def STAFF_FEEDBACK_REPLY(request):
    feedback = Staff_Feedback.objects.all()
    notification = Staff_Feedback.objects.all()
    cntxt = {'feedback':feedback,'notification':notification}
    return render(request, "HOD/staff_feedback.html", cntxt)

@login_required(login_url='/') 
def STAFF_FEEDBACK_REPLY_SAVE(request):
    if request.method == "POST":
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = Staff_Feedback.objects.get(id = feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status = 1
        feedback.save()
        messages.warning(request, "Reply sent for the Feedback")
        return redirect('Staff_Feedback_Reply')

@login_required(login_url='/')     
def STUD_SEND_NOTI(request):
    student = Student.objects.all()
    notification = Student_Notification.objects.all()
    cntxt = {'student':student,'notification':notification}
    return render(request, "HOD/stud_notification.html", cntxt)

@login_required(login_url='/') 
def SAVE_STUD_NOTI(request):
    if request.method == "POST":
        message = request.POST.get('message')
        student_id = request.POST.get('student_id')

        student = Student.objects.get(admin = student_id)
        stud_noti = Student_Notification(
            student_id = student,
            message = message,
        )
        stud_noti.save()
        messages.success(request, "Notification Send Successfully...")
        return redirect('Student_Send_Noti')

@login_required(login_url='/')     
def STUD_FEEDBACK_REPLY(request):
    feedback = Student_Feedback.objects.all()
    feedback_history = Student_Feedback.objects.all().order_by('-id')[0:5]
    cntxt = {'feedback':feedback,'feedback_history':feedback_history}
    return render(request, "HOD/stud_feedback.html", cntxt)

@login_required(login_url='/') 
def STUD_FEEDBACK_REPLY_SAVE(request):
    if request.method == "POST":
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = Student_Feedback.objects.get(id = feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status = 1
        feedback.save()
        messages.warning(request, "Reply sent for the Feedback")
        return redirect('Stud_Feedback_Reply')

@login_required(login_url='/')     
def STUD_LEAVE_VIEW(request):
    stud_leave = Student_Leave.objects.all()
    cntxt = {'stud_leave':stud_leave}
    return render(request, "HOD/student_leave.html", cntxt)

@login_required(login_url='/') 
def STUD_APPROVE_LEAVE(request,id):
    leave = Student_Leave.objects.get(id=id)
    leave.status = 1
    leave.save()
    messages.success(request, "Leave Approved...")
    return redirect('Stud_Leave_View')

@login_required(login_url='/') 
def STUD_DISAPPROVE_LEAVE(request,id):
    leave = Student_Leave.objects.get(id=id)
    leave.status = 1
    leave.save()
    messages.success(request, "Leave Rejected...")
    return redirect('Stud_Leave_View')

@login_required(login_url='/') 
def HOD_VIEW_ATTENDANCE(request):
    subject = Subject.objects.all()
    session = Session_Year.objects.all()
    action = request.GET.get('action')
    get_subject = None
    get_session_year = None
    attendance_date = None
    attendance_report = None

    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            attendance_date = request.POST.get('attendance_date')

            get_subject = Subject.objects.get(id = subject_id)
            get_session_year = Session_Year.objects.get(id = session_year_id)
            attendance = Attendance.objects.filter(subject_id = get_subject,attendance_data = attendance_date)

            for i in attendance:
                attendance_id = i.id
                attendance_report = Attendance_Report.objects.filter(attendance_id = attendance_id)


    cntxt = {'subject':subject,
             'session':session,
             'action':action,
             'get_subject':get_subject,
             'get_session_year':get_session_year,
             'attendance_date':attendance_date,
             'attendance_report':attendance_report
             }

    return render(request,'HOD/view_attendance.html',cntxt)

@login_required(login_url='/') 
def ADD_STUDENT_ACTIVITY(request):
    student = Student.objects.all()
    cntxt = {'student' : student}
    return render(request,'HOD/add_student_activity.html',cntxt)

@login_required(login_url='/') 
def SAVE_STUDENT_ACTIVITY(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        date_of_event = request.POST.get('date_of_event')
        activity = request.POST.get('activity')
        medal = request.POST.get('medal')
        get_student = Student.objects.get(admin = student_id)
        stud_activity = Student_Activity(
            student_id = get_student,
            date = date_of_event,
            activity = activity,
            medal = medal
        )
        stud_activity.save()
        messages.success(request,'Student Activity added Successfully , Please Check on Dashboard')
        return redirect('add_student_activity')