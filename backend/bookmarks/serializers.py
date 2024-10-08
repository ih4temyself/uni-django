from rest_framework import serializers

from bookmarks.models import Bookmark, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class BookmarkSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(write_only=True, required=False)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Bookmark
        fields = ["id", "url", "title", "category", "category_name", "is_favorite"]

    def create(self, validated_data):
        category_name = validated_data.pop("category_name", None)
        if category_name:
            category, created = Category.objects.get_or_create(name=category_name)
            validated_data["category"] = category
        return super().create(validated_data)

    def update(self, instance, validated_data):
        category_name = validated_data.pop("category_name", None)
        if category_name:
            category, created = Category.objects.get_or_create(name=category_name)
            validated_data["category"] = category
        return super().update(instance, validated_data)
