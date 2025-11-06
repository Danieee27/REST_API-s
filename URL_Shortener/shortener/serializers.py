#allows you to convert complex data types such as querysets and model instances into native Python datatypes that can then be easily rendered into JSON, XML or other content types.
from rest_framework import serializers
from .models import URL

class URLSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()

    #items listed in the api response
    class Meta:
        model = URL
        fields = ['id', 'long_url', 'short_code', 'short_url', 'created_at']
        
    def get_short_url(self, obj):
        #making a request from the user
        request = self.context.get('request')
        if request:
            #gives us the url of our local host plus the short code
            #"build_absolute_uri" builds a full absolute URI from the given location - local host path in our case
            return request.build_absolute_uri(f'/{obj.short_code}')
        return f'/{obj.short_code}'