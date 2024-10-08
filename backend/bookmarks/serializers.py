from rest_framework import serializers

from .models import Bookmark, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class BookmarkSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True,
        required=False,
        allow_null=True,
    )

    category_name = serializers.CharField(
        write_only=True, required=False, allow_blank=True
    )
    category_id_read = serializers.IntegerField(source="category.id", read_only=True)

    class Meta:
        model = Bookmark
        fields = [
            "id",
            "url",
            "title",
            "category",
            "category_id",
            "category_name",
            "category_id_read",
            "is_favorite",
        ]

    def create(self, validated_data):
        category_name = validated_data.pop("category_name", None)
        category = None

        if category_name:
            category, created = Category.objects.get_or_create(name=category_name)
        else:
            category = validated_data.pop("category_id", None)

        validated_data["category"] = category
        return super().create(validated_data)

    def update(self, instance, validated_data):
        category_name = validated_data.pop("category_name", None)
        category = None

        if category_name:
            category, created = Category.objects.get_or_create(name=category_name)
        else:
            category = validated_data.pop("category_id", None)

        validated_data["category"] = category
        return super().update(instance, validated_data)
