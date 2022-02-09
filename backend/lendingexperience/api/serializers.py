from pyexpat import model

from rest_framework import serializers

from .models import Company, CreditProposal, Offer


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id_company',
                  'name',
                  'cnpj',
                  'segment',
                  'website',
                  'monthly_revenue',
                  'money_purpose',
                  'email',
                  'chosen_offer',
                  'installments')


class CreditProposalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditProposal
        fields = '__all__'


class OffersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'
