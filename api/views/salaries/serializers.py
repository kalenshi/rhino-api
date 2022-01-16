from rest_framework import serializers

from api.models import Salaries


class SalariesSerializer(serializers.ModelSerializer):
    """
    Class to interact with the salaries serialization
    """

    class Meta:
        model = Salaries
        fields = "__all__"

    def create(self, validated_data):
        """
        Create the salaries object
        :param validated_data:
        :return:
        """
        pass
