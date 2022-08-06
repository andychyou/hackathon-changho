from django.db import models
from django.conf import settings


class UserHashtag(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    hashtag = models.CharField(max_length=100, null=True)  # 해시태그
    def __str__(self):
        return str(self.hashtag)


class UserDetails(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    belongs = models.CharField(max_length=30)  # 학교/직업
    major = models.CharField(max_length=30)  # 전공
    position = models.CharField(max_length=30)  # 메인포지션
    subposition = models.CharField(max_length=30, null=True)  # 서브포지션
    introduction = models.CharField(max_length=200, null=True)  # 자기소개
    def __str__(self):
        return str(self.user)


class UserOngoing(models.Model):  # 현재 진행 중
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ongoing = models.TextField()
    def __str__(self):
        return str(self.ongoing)


class UserSkills(models.Model):  # 기술스택
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    skill_type = models.CharField(max_length=100, null=True)
    skill_name = models.CharField(max_length=100, null=True)
    def __str__(self):
        return str(self.skill_name)

class UserSkillsDetails(models.Model):
    skill_detail = models.CharField(max_length=100, null=True)
    skill_name = models.ForeignKey(
        "UserSkills",
        on_delete=models.CASCADE,
        related_name='detail',
        db_column='skill_name'
    )
    def __str__(self):
        return str(self.skill_detail)

class UserStudy(models.Model):  # 개인공부
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name= "study"
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    study_type = models.CharField(max_length=100, null=True)
    study_name = models.CharField(max_length=100, null=True)
    def __str__(self):
        return str(self.study_name)

class UserStudyDetails(models.Model):
    study_detail = models.CharField(max_length=100, null=True)
    study_name = models.ForeignKey(
        "UserStudy",
        on_delete=models.CASCADE,
        related_name='detail',
        db_column='study_name'
    )
    def __str__(self):
        return str(self.study_detail)


class UserCert(models.Model):  # 자격증
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    certification = models.CharField(max_length=100, null=True)
    def __str__(self):
        return str(self.certification)


class UserCareer(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="user_email",
        on_delete=models.CASCADE,
        db_column="user_email")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    career_at = models.CharField(max_length=30)
    career_who = models.CharField(max_length=30)
    career_when = models.CharField(max_length=30)
    career_what = models.CharField(max_length=100)
    career_achieve = models.CharField(max_length=100)
    career_skills = models.CharField(max_length=100)
    def __str__(self):
        return str(self.career_at)


class Follow(models.Model):
    follower = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='follower'
    )
    following = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='following'
    )

    class Meta:
        db_table = 'follow'