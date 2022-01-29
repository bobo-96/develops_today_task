from django.db import models, IntegrityError

from apps.users.models import User


class Post(models.Model):
    title = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name='Название поста'
    )
    link = models.URLField(
        max_length=255,
        blank=True, null=True,
        verbose_name='Линк'
    )
    creation_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания поста'
    )
    amount_of_upvotes = models.PositiveIntegerField(
        default=0,
        blank=True, null=True,
        verbose_name='Количество голосов'
    )
    author_name = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='post_author',
        blank=True, null=True
    )

    @property
    def upvote(self):
        self.amount_of_upvotes += 1


    # def downvote(self, user):
    #     try:
    #         self.post_votes.create(user=user, post=self, vote_type="down")
    #         self.votes -= 1
    #         self.save()
    #     except IntegrityError:
    #         return 'already_downvoted'
    #     return 'ok'


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name='post_comment'
    )
    author_name = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='comment_author',
        blank=True, null=True
    )
    content = models.TextField(
        blank=True, null=True,
        verbose_name='Контент'
    )
    creation_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создание комментария'
    )
