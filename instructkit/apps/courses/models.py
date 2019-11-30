import uuid

from django.db import models
from model_utils.choices import Choices


class BaseModule(models.Model):
    DURATION_UNITS = Choices(
        ('hours', 'hours', 'Hours'),
        ('days', 'days', 'Days'),
        ('weeks', 'weeks', 'Weeks'),
        ('months', 'months', 'Months')
    )

    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=300, null=False)
    description = models.TextField(null=False)
    duration_type = models.CharField(max_length=20,
                                     choices=DURATION_UNITS,
                                     default=DURATION_UNITS.days,
                                     null=False,
                                     help_text='Default is days. Set to hours, weeks, months.')
    start = models.DateTimeField(null=False)
    end = models.DateTimeField(null=False)


    class Meta:
        abstract = True

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title

    @property
    def duration(self):
        # TODO Issue #6 - Duration can be shown in weeks as well. Map to duration_type
        delta = self.end - self.start
        return delta.days


class Course(BaseModule):
    instructors = models.ManyToManyField('accounts.Instructor',
                                         related_name='courses')
    students = models.ManyToManyField('accounts.Student',
                                      related_name='courses')


class Unit(BaseModule):
    # Levels should reflect complexity, not skill
    LEVELS = Choices(
        ('low', 'low', 'Low'),
        ('normal', 'normal', 'Normal'),
        ('medium', 'medium', 'Medium'),
        ('high', 'high', 'High')
    )

    course = models.ForeignKey('Course',
                               on_delete=models.CASCADE,
                               related_name='units',
                               help_text='The course associated with this module.')
    level = models.CharField(max_length=300, choices=LEVELS,
                             help_text='The level of relative difficulty of the material.')


class Lesson(BaseModule):
    instructor = models.ForeignKey('accounts.Instructor',
                                   on_delete=models.DO_NOTHING,
                                   related_name='lessons',
                                   help_text='The instructor for this lesson.')
    unit = models.ForeignKey('Unit',
                             on_delete=models.CASCADE,
                             related_name='lessons',
                             help_text='The unit this lesson belongs to.')


class Assignment(BaseModule):
    CATEGORIES = Choices(
        ('homework', 'homework', 'Homework'),
        ('project', 'project', 'Project'),
        ('exercise', 'exercise', 'Exercise')
    )

    lesson = models.ForeignKey('Lesson',
                               on_delete=models.DO_NOTHING,
                               related_name='assignments',
                               help_text='The lesson this assignment relates to.')
    category = models.CharField(max_length=300, choices=CATEGORIES)
    # TODO: Make url and document optional
    url = models.URLField()
    document = models.TextField()
    is_complete = models.BooleanField(default=False)
