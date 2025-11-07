from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Leitura, Alerta 
from .serializers import LeituraSerializer, AlertaSerializer


class LeituraViewSet(viewsets.ModelViewSet):
    queryset = Leitura.objects.all()
    serializer_class = LeituraSerializer

    @action(detail=False, methods=['get'])
    def ultima(self, request):
        """retorna a última leitura"""
        leitura = Leitura.objects.first()
        if leitura:
            serializer = self.get_serializer(leitura)
            return Response(serializer.data)
        return Response({'erro': 'Nenhuma leitura encontrada'})

    @action(detail=False, methods=['get'])
    def ultimas_24h(self, request):
        """Retorna leitura das últimas 24 horas"""
        from django.utils import timezone
        from datetime import timedelta

        agora = timezone.now()
        # Complete your logic here


class AlertaViewSet(viewsets.ModelViewSet):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer

    @action(detail=False, methods=['get'])
    def nao_lido(self, request):
        """Retorna alerta não lidos"""
        alertas = Alerta.objects.filter(lido=False)
        serializer = self.get_serializer(alertas, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def marcar_lido(self, request, pk=None):
        """Marcar alerta como lido"""
        alerta = self.get_object()
        alerta.lido = True
        alerta.save()
        serializer = self.get_serializer(alerta)
        return Response(serializer.data)
