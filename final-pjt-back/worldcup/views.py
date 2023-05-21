from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import WorldCupItem
from .serializers import WorldCupItemSerializer


class WorldCupItemViewSet(ViewSet):
    queryset = WorldCupItem.objects.all()
    serializer_class = WorldCupItemSerializer()

    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        worldcup_item = self.queryset.get(pk=pk)
        serializer = self.serializer_class(worldcup_item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        worldcup_item = self.queryset.get(pk=pk)
        serializer = self.serializer_class(worldcup_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        worldcup_item = self.queryset.get(pk=pk)
        worldcup_item.delete()
        return Response(status=204)

    @action(detail=True, methods=['post'])
    def vote(self, request, pk=None):
        worldcup_item = self.queryset.get(pk=pk)
        worldcup_item.votes += 1
        worldcup_item.save()
        return Response({'detail': 'Vote successful.'})
