from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models
from django.contrib.postgres.fields import JSONField

from django.utils.translation import ugettext_lazy as _

from model_utils import Choices
from shortuuidfield import ShortUUIDField


def skill_defaults():
    """Default settings for Instructor.skills"""
    return {"languages": [], "technologies": []}


class User(AbstractUser):
    uid = ShortUUIDField(auto=True)
    # First Name and Last Name do not cover name patterns around the globe.
    # Django Cookiecutter: https://github.com/pydanny/cookiecutter-django
    name = models.CharField(_('Full name of User'), blank=True, null=True, max_length=255)
    email = models.EmailField(_('email address'), blank=False, unique=True)
    github = models.URLField(_('Link to public Github account'), blank=True, null=True)
    website = models.URLField(_('Link to personal portfolio site'), blank=True, null=True)
    linkedin = models.URLField(_('Link to LinkedIn profile'), blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'username']

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('api:users-detail', kwargs={'pk': self.id})


class Instructor(User):
    # TODO: Issue #2 - Add properties for: courses taught, success rate, etc

    SKILL_CHOICES = Choices(
        ('frontend dev', 'fewd', 'Frontend Web Development'),
        ('backend dev', 'bewd', 'Backend Web Development'),
        ('dev ops', 'devops', 'Dev Operations (devOps)'),
        ('user experience', 'ux', 'User Experience & Interfaces'),
        ('full stack', 'fullstack', 'Full Stack Web Development')
    )

    skills = JSONField(default=skill_defaults)
    speciality = models.CharField(max_length=255, choices=SKILL_CHOICES)

    class Meta:
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructors'


class Student(User):
    OUTCOME_CHOICES = Choices(
        ('full-time work', 'ft_work', 'Full-time Employment'),
        ('part-time work', 'pt_work', 'Part-time Employment'),
        ('independent work', 'independent', 'Independent Work'),
        ('entrepreneur', 'entrepreneur', 'Start-up/Entrepreneur'),
        ('education', 'education', 'Education Goal'),
    )

    OUTCOME_STATUS_CHOICES = Choices(
        ('on track', 'on_track', 'On track for course completion'),
        ('needs support', 'on_support', 'Requires additional support'),
        ('off track', 'off_track', 'Will not complete the course')
    )

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    outcome = models.CharField(max_length=255, choices=OUTCOME_CHOICES)
    outcome_status = models.CharField(max_length=255, choices=OUTCOME_STATUS_CHOICES)
    notes = models.TextField()
