from django.db import models


class Order(models.Model):
    title = models.CharField(
        max_length=64
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


class AttachedFile(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='attached_files',
        on_delete=models.CASCADE
    )
    file = models.FileField(
        upload_to='attached_files/',

        blank=True,
        null=True
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )
