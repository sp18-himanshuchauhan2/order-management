from rest_framework import serializers
from .models import Order, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['product_name', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'order_date', 'items']
        read_only_fields = ['order_date']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item in items_data:
            Item.objects.create(order=order, **item)
        return order
    
    def update(self, instance, validated_data):
        items_data = validated_data.pop('items')
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.save()
        instance.items.all().delete()

        for item_data in items_data:
            Item.objects.create(order=instance, **item_data)
        return instance