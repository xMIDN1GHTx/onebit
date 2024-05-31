from rest_framework import serializers
from .models import Order, AttachedFile


class AttachedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttachedFile
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    attached_files = AttachedFileSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = "__all__"


class OrderCreateSerializer(serializers.ModelSerializer):
    attached_files = serializers.ListField(
        child=serializers.FileField(max_length=100000, allow_empty_file=False, use_url=False),
        write_only=True,
        required=False
    )

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        attached_files = validated_data.pop('attached_files', [])
        order = Order.objects.create(**validated_data)

        for file in attached_files:
            AttachedFile.objects.create(order=order, file=file)

        return order
