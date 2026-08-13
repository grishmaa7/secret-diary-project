from rest_framework import serializers
from .models import Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = [
            'id',
            'owner',
            'title',
            'content',
            'mood',
            'is_private',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Title cannot be empty."
            )
        return value

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Content cannot be empty."
            )
        return value