from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from myapp.models import Project  # Asegúrate de importar tu modelo correctamente

class IndexView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        projects = Project.objects.all()  # Aquí obtienes el queryset
        print("Proyectos obtenidos:", projects)  # Depuración
        context = {
            'mensaje': 'Hola desde APIView con HTML!',
            'projects': projects  # Pasas la lista al template
        }
        return Response(context)
class ProjectsListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'projects_list.html'

    def get(self, request):
        projects = Project.objects.all()  # Aquí obtienes el queryset
        print("asdasdsa")
        print("Proyecto obtenido:", projects)
        context = {
            'mensaje': 'Hola desde APIView con HTML!',
            'projects': projects  # Pasas la lista al template
        }
        return Response(context)
    
class ProjectDetailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'project_detail.html'

    def get(self, request, slug):
        project = Project.objects.get(slug=slug)  # Aquí obtienes el queryset
        
        context = {
            'mensaje': 'Hola desde APIView con HTML!',
            'project': project  # Pasas la lista al template
        }
        return Response(context)
