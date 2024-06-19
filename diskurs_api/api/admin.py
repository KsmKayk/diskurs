from django.contrib import admin

from .models import User, Tier, Tag, Category, Post, Comment, Like

@admin.register(Tier)
class TierAdmin(admin.ModelAdmin):
  list_display = ('name', 'price', 'max_posts_per_day', 'id')
  search_fields = ['name']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  list_display = ('name', 'email','id','display_tier')
  search_fields = ['name', 'email', 'id']
  list_filter = ['tier_id']

  def display_tier(self, obj):
    return obj.tier_id.name

  display_tier.short_description = 'TIER'

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
  list_display = ('name', 'id')
  search_fields = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name', 'id')
  search_fields = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'user_id', 'category_id','id', 'display_tags')
  search_fields = ['title', 'id']
  list_filter = ['category_id', 'user_id']

  def display_tags(self, obj):
    return ", ".join([tag.name for tag in obj.tags.all()])
  
  display_tags.short_description = 'TAGS'

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
  list_display = ('post_id', 'user_id', 'id')
  search_fields = ['post_id', 'user_id']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ('post_id', 'user_id', 'id')
  search_fields = ['post_id', 'user_id']