from rest_framework import viewsets
from .models import TodoModel
from .serializers import TodoSerializer
from .permissions import IsAdminOrReadCreateUpdateOnly

class TodoViewSet(viewsets.ModelViewSet):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAdminOrReadCreateUpdateOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)