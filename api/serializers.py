from rest_framework import serializers
from api.models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('answerID', 'answer', 'isEnteredAnswerYN')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    answers = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'productAuthenticationQuestionID', 'question', 'answerStatusInd', 'questionPointValue',
                  'requiredNoOfAnswers', 'answers')

    def create(self, validated_data):
        profile_data = validated_data.pop('answers')

        user = User(**validated_data)

        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('answers')
        answers = instance.answers
        instance.save()

        answers.answerID = profile_data.get('answerID', answers.answerID)
        answers.answer = profile_data.get('answer', answers.answer)
        answers.isEnteredAnswerYN = profile_data.get('answer', answers.isEnteredAnswerYN)
        profile.save()

        return instance
