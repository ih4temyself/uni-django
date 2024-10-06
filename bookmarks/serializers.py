from rest_framework import serializers

from bookmarks.models import Bookmark, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BookmarkSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category", write_only=True
    )

    class Meta:
        model = Bookmark
        fields = ["id", "url", "title", "category", "category_id", "is_favorite"]
