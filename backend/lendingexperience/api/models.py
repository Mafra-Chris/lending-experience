from django.db import models


class Offer(models.Model):
    id_offer = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    amount_perc = models.FloatField()
    interest = models.FloatField()
    tax_value = models.FloatField()


class Company(models.Model):
    id_company = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    cnpj = models.CharField(unique=True, max_length=100)
    segment = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    monthly_revenue = models.FloatField()
    money_purpose = models.CharField(max_length=100)
    email = models.EmailField()
    chosen_offer = models.ForeignKey(
        Offer, on_delete=models.CASCADE, blank=True, null=True)
    installments = models.IntegerField(blank=True, null=True)


class CreditProposal(models.Model):
    id_proposal = models.AutoField(primary_key=True)
    id_company = models.OneToOneField(Company, on_delete=models.CASCADE)
    offers = models.ManyToManyField(Offer)
