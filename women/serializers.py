from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Women


# class WomenModel:
#     def __init__(self,title,content):
#         self.title = title
#         self.content = content


class  WomenSerializer(serializers.ModelSerializer):
   user = serializers.HiddenField(default=serializers.CurrentUserDefault())
   class Meta:
      model = Women
      fields = "__all__"

   #
   # def create(self, validated_data):
   #    return Women.objects.create(**validated_data)
   #
   # def update(self, instance, validated_data):
   #    instance.title = validated_data.get("title", instance.title)
   #    instance.content = validated_data.get("content", instance.content)
   #    instance.price = validated_data.get("price", instance.price)
   #    instance.description = validated_data.get("description", instance.description)
   #    instance.size = validated_data.get("size", instance.size)
   #    instance.time_create = validated_data.get("time_create", instance.time_create)
   #    instance.time_update = validated_data.get("time_update", instance.time_update)
   #    instance.is_published = validated_data.get("is_published", instance.is_published)
   #    instance.cat_id = validated_data.get("cat_id", instance.cat_id)
   #    instance.save()
   #    return instance




# def encode():
#     model = WomenModel('Ковер ЮНИКАРПЕТ 3A2378','Content: Ковер ЮНИКАРПЕТ 3A2378')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)