from rest_framework import serializers
from .models import Location, Department, Category, SubCategory, SKU

class RelatedFieldAlternative(serializers.PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = kwargs.pop('serializer', None)
        if self.serializer is not None and not issubclass(self.serializer, serializers.Serializer):
            raise TypeError('"serializer" is not a valid serializer class')

        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False if self.serializer else True

    def to_representation(self, instance):

        if self.serializer:
            return self.serializer(instance, context=self.context).data
        return super().to_representation(instance)

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    location = RelatedFieldAlternative(queryset=Location.objects.all(), serializer=LocationSerializer)
    
    class Meta:
        model = Department
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    department = RelatedFieldAlternative(queryset=Department.objects.all(), serializer=DepartmentSerializer)

    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    category = RelatedFieldAlternative(queryset=Category.objects.all(), serializer=CategorySerializer)

    class Meta:
        model = SubCategory
        fields = '__all__'

class SKUSerializer(serializers.ModelSerializer):

    location = RelatedFieldAlternative(queryset=Location.objects.all(), serializer=LocationSerializer)
    department = RelatedFieldAlternative(queryset=Department.objects.all(), serializer=DepartmentSerializer)
    category = RelatedFieldAlternative(queryset=Category.objects.all(), serializer=CategorySerializer)
    subcategory = RelatedFieldAlternative(queryset=SubCategory.objects.all(), serializer=SubCategorySerializer)

    class Meta:
        model = SKU
        fields = '__all__'