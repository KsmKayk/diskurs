from django.db import models
import uuid


class Tier(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  max_posts_per_day = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class User(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  password_hash = models.CharField(max_length=255)
  tier_id = models.ForeignKey(Tier, on_delete=models.DO_NOTHING, verbose_name='Tier')
  tiered_at = models.DateTimeField()
  tier_expires_at = models.DateTimeField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class Tag(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=255, unique=True)

  def __str__(self):
    return self.name

class Category(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=255, unique=True)

  class Meta:
        verbose_name_plural = "Categories"

  def __str__(self):
    return self.name

class Post(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
  category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='Category')
  title = models.CharField(max_length=255)
  tags = models.ManyToManyField(Tag)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


  def __str__(self):
    return self.title

class Like(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  post_id = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')
  user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
  created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  post_id = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')
  user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
  content = models.TextField()
  likes = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.content