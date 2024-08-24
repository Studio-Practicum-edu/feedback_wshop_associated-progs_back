from rest_framework import serializers

from feedback.models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    def validate_name(self, value):
        """Проверка, что имя не содержит цифр."""
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError(
                {"detail": "Имя не должно содержать цифры."}
            )
        return value

    # def validate(self, data):
    #     """Проверка уникальности сообщения."""
    #     message = data.get('message')
    #     if Feedback.objects.filter(message=message).exists():
    #         raise serializers.ValidationError(
    #             {"detail": "Сообщение с таким же содержимым уже существует."}
    #         )
    #     return data

    class Meta:
        model = Feedback
        fields = ['id', 'name', 'email', 'message', 'created_at']


# class FeedbackDetailSerializer(serializers.ModelSerializer):
#     """Сериализатор для исключения поля {id} из ответа."""
#     class Meta:
#         model = Feedback
#         fields = ['name', 'email', 'message', 'created_at']
