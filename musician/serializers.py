from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True, max_length=63)
    last_name = serializers.CharField(required=True, max_length=63)
    instrument = serializers.CharField(required=True, max_length=63)
    age = serializers.IntegerField(min_value=14)
    date_of_applying = serializers.DateField(read_only=True)
    is_adult = serializers.ReadOnlyField()

    def create(self, validated_data):
        return Musician.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            "first_name",
            instance.first_name
        )
        instance.last_name = validated_data.get(
            "last_name",
            instance.last_name
        )
        instance.instrument = validated_data.get(
            "instrument",
            instance.instrument
        )
        instance.age = validated_data.get(
            "age",
            instance.age
        )
        instance.date_of_applying = validated_data.get(
            "date_of_birth",
            instance.date_of_applying
        )
        instance.save()
        return instance


class MusicianIsAdultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Musician
        fields = ["first_name",
                  "last_name",
                  "instrument",
                  "age",
                  "is_adult",
                  "date_of_applying"]
