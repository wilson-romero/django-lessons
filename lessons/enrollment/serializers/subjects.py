from rest_framework import serializers
from enrollment.models import Subject


class SubjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('__all__')
        read_only_fields = ('enrolled_students','created','modified')
