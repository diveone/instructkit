# Instructkit

Top Priorities:
* Track assignment completion.
* Track attendance.
* Give students feedback in a unified interface.
* Track progress towards goals.

Integrations:
* Google API: Drive (Docs, Slideshow)
* Github: Auth for instructors
* Calendar, REPL

__MVP Features__

- Schedule
- Features
- Instructor panel: Add classes, students and assignments
- Student panel: Submit work, view schedule

__Relationships__

User > Student User > Instructor Course has many Units has many Lessons has many assignments Schedule has many attendees

Attendance Notes
```py
# Unit model
def attendance(self, student_id):
    # Each unit has multiple lessons which have Lesson.attendance
    total = 0
    total_lessons = len(Unit.lessons)
    lessons_attended = []
    for lesson in Unit.lessons:
        if student_id in lesson.attendance.students:
            total += 1
            lessons_attended.push(lesson.uid)
    # attendance as a percentage
    ratio = (decimal(total / total_lessons, 2))
    # Return a tuple containing attendance percentage and the lessons attended
    return (ratio, lessons_attended,)

# Course model
def attendance(self, student_id):
    # Each course has multiple units which have Unit.attendance
    lessons = 0
    total_units = len(Course.units)
    for unit in Course.units:
        a = unit.attendance(student_id):
        lessons += len(a[1])
    # attendance as a percentage
    return (decimal(lessons / total_units, 2))
```

