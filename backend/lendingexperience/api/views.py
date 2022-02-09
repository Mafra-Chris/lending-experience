
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OffersSerializers, CompanySerializer, CreditProposalsSerializer
from .models import Company, Offer, CreditProposal
from django.core import serializers


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'CreditProposals': '/credit-proposals/<num:pk>',
        'Signup': '/signup/',
        'Login': '/login/',
        'offers': '/offers/',
        'chosen-offer': '/chosen-offer/<num:pk>'
    }
    return Response(api_urls)


@api_view(['GET'])
def offersList(request):
    offers = Offer.objects.all()
    serializer = OffersSerializers(offers, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def offerDetail(request, pk):
    offer = Offer.objects.get(id_offer=pk)
    serializer = OffersSerializers(offer, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def offerCreate(request):
    serializer = OffersSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def offerUpdate(request, pk):
    offer = Offer.objects.get(id_offer=pk)
    serializer = OffersSerializers(instance=offer, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def offerDelete(request, pk):
    offer = Offer.objects.get(id_offer=pk)
    offer.delete()

    return Response('Item succsesfully delete!')


@api_view(['GET'])
def companyDetail(request, pk):
    company = Company.objects.get(id_company=pk)
    serializer = CompanySerializer(company, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def companyCreate(request):

    serializer = CompanySerializer(data=request.data)

    if serializer.is_valid():
        offer = None
        company = serializer.save()
        print(company.id_company)
        if serializer.data['monthly_revenue'] <= 10000:
            offer = Offer.objects.get(type='lower')

        elif serializer.data['monthly_revenue'] > 10000:
            offer = Offer.objects.filter(type='bigger')

        proposal = CreditProposal(
            id_company=company)
        proposal.save()
        proposal.offers.add(*offer)

    else:
        print(serializer.errors)

    return Response(serializer.data)


@api_view(['GET'])
def proposalDetail(request, id_company):
    proposal = CreditProposal.objects.get(id_company=id_company)
    offers = []
    for offer in proposal.offers.all():
        offers.append(OffersSerializers(offer).data)

    return Response(offers)


@api_view(['POST'])
def chooseOffer(request, id_company):
    company = Company.objects.get(id_company=id_company)

    data = {"chosen_offer": request.data['id_offer']}
    serializer = CompanySerializer(company, data=data, partial=True)
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)
