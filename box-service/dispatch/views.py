from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Box, Item
from .serializers import BoxSerializer, ItemSerializer

class BoxViewSet(viewsets.ModelViewSet):
    queryset = Box.objects.all()  # Define the queryset to return all Box instances
    serializer_class = BoxSerializer  # Define the serializer class to serialize the Box model


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Box, Item
from .serializers import BoxSerializer, ItemSerializer

class CreateBoxView(APIView):
    def post(self, request):
        serializer = BoxSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoadBoxView(APIView):
    def post(self, request, txref):
        try:
            box = Box.objects.get(txref=txref)
        except Box.DoesNotExist:
            return Response({'error': 'Box not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if box.battery_capacity < 25:
            return Response({'error': 'Battery too low for loading'}, status=status.HTTP_400_BAD_REQUEST)
        
        if box.state != 'LOADING':
            return Response({'error': 'Box is not in LOADING state'}, status=status.HTTP_400_BAD_REQUEST)
        
        items = request.data.get('items', [])
        total_weight = sum(item['weight'] for item in items)
        if total_weight > box.weight_limit:
            return Response({'error': 'Weight limit exceeded'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Save items
        for item_data in items:
            serializer = ItemSerializer(data=item_data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'message': 'Items loaded successfully'}, status=status.HTTP_200_OK)

class CheckLoadedItemsView(APIView):
    def get(self, request, txref):
        items = Item.objects.filter(box__txref=txref)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

class AvailableBoxesView(APIView):
    def get(self, request):
        boxes = Box.objects.filter(state='IDLE', battery_capacity__gte=25)
        serializer = BoxSerializer(boxes, many=True)
        return Response(serializer.data)

class CheckBatteryLevelView(APIView):
    def get(self, request, txref):
        try:
            box = Box.objects.get(txref=txref)
            return Response({'battery_level': box.battery_capacity})
        except Box.DoesNotExist:
            return Response({'error': 'Box not found'}, status=status.HTTP_404_NOT_FOUND)