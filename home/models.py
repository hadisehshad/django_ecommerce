from django.db import models


class Testimonial(models.Model):
    user = models.CharField(max_length=255, verbose_name="نام مشتری")
    feedback = models.TextField(verbose_name="نظر")
    rating = models.PositiveIntegerField(default=5, verbose_name="امتیاز")
    image = models.ImageField(upload_to="testimonials/", blank=True, null=True, verbose_name="تصویر مشتری")
    is_active = models.BooleanField(default=True, verbose_name="فعال")

    class Meta:
        verbose_name = "نظر مشتری"
        verbose_name_plural = "نظرات مشتریان"

    def __str__(self):
        return self.user
