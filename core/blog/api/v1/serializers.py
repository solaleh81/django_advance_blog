from rest_framework import serializers
from ...models import Post, Category


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField(max_length=255)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class PostSerializer(serializers.ModelSerializer):
    # content = serializers.CharField(read_only=True)
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_url", read_only=True)
    # category = CategorySerializer()

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "title",
            "content",
            "status",
            "created_date",
            "published_date",
            "snippet",
            "relative_url",
        ]
