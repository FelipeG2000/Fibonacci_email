from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from .serializer import MyDataSerializer
from .commons import fibonacci
from django.core.mail import send_mail


class MyDataView(APIView):

    def get(self, request):
        hora_actual = datetime.today().strftime('%H:%M:%S')
        lista_hora_minutos_segundos = list(hora_actual.split(":"))
        minutos = int(lista_hora_minutos_segundos[1])
        segundos = int(lista_hora_minutos_segundos[2])
        semilla1 = minutos % 10
        semilla2 = minutos // 10
        fibonacci_list = fibonacci(segundos, semilla1, semilla2)
        data = {'message': f'Hola {fibonacci_list}'}
        serializer = MyDataSerializer(data=data)
        serializer.is_valid()

        try:
            to_email = ['pipegarcia1918@hotmail.com', 'didier.correa@proteccion.com.co', 'correalondon@gmail.com']
            subject = 'Prueba Técnica - Andres Felipe Garcia Henao'
            message = f'Prueba tecnica lista de generacion: {hora_actual}\nlista de fibonacci: {fibonacci_list}'
            send_mail(subject, message, None, to_email)
        except Exception as e:
            Response({'error': str(e)})
        return Response(serializer.data)
# Create your views here.
