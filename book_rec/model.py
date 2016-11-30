# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class BxBookAvg(models.Model):
    isbn = models.CharField(db_column='ISBN', primary_key=True, max_length=13)  # Field name made lowercase.
    rating_sum = models.BigIntegerField(blank=True, null=True)
    rating_num = models.BigIntegerField(blank=True, null=True)
    rating_avg = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bx-book-avg'


class BxBookRatings(models.Model):
    user_id = models.IntegerField(db_column='User-ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    isbn = models.CharField(db_column='ISBN', max_length=13)  # Field name made lowercase.
    book_rating = models.IntegerField(db_column='Book-Rating')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'bx-book-ratings'
        unique_together = (('user_id', 'isbn'),)


class BxBooks(models.Model):
    isbn = models.CharField(db_column='ISBN', primary_key=True, max_length=13)  # Field name made lowercase.
    book_title = models.CharField(db_column='Book-Title', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    book_author = models.CharField(db_column='Book-Author', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    year_of_publication = models.IntegerField(db_column='Year-Of-Publication', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    publisher = models.CharField(db_column='Publisher', max_length=255, blank=True, null=True)  # Field name made lowercase.
    image_url_s = models.CharField(db_column='Image-URL-S', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    image_url_m = models.CharField(db_column='Image-URL-M', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    image_url_l = models.CharField(db_column='Image-URL-L', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'bx-books'


class BxUsers(models.Model):
    user_id = models.CharField(db_column='User-ID', primary_key=True, max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bx-users'
