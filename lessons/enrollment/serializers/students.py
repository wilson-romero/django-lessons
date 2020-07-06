from rest_framework import serializers
from enrollment.models import Student


class SubjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('__all__')
        read_only_fields = ('created','modified')
