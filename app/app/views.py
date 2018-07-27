from django.shortcuts import render
from django.http import HttpResponse

# Variaveis para simular um banco de dados para ajudar o back
# Apenas para testes depois tirar

atuacaoList = [
    {
        'imgUrl': "img/atu_foto1.png",
        'titulo': "Lei de Família",
        'mensagemPequena': "O direito de família envolve uma série de assuntos que geralmente são muito pessoais, únicos\
                                    e emocionalmente desafiadores.",
        'link': "/"
    },
    {
        'imgUrl': "img/atu_foto2.png",
        'titulo': "Lei de Família",
        'mensagemPequena': "A custódia de crianças envolve uma série de assuntos que geralmente são muito pessoais, únicos\
                                    e emocionalmente desafiadores.",
        'link': "/"
    },
    {
        'imgUrl': "img/atu_foto3.png",
        'titulo': "Lei de Família",
        'mensagemPequena': "Os acidentes automobilísticos são difíceis de resolver, porque geralmente são inesperados.\
                                    Naquela época você precisa de alguém ...",
        'link': "/"
    }
]

noticiasList = [
    {
        'imgUrl': 'img/noti_foto1.png',
        'data': "28 de Abril de 2018",
        'titulo': "Lei e Ordem",
        'tag': "Artigo",
        'mensagem': "Realizadas exclusivamente por ordem expressa da Presidência da República, as missões de Garantia da Lei e da Ordem (GLO)",
        'link': "/"
    },
    {
        'imgUrl': 'img/noti_foto2.png',
        'data': "28 de Abril de 2018",
        'titulo': "Lei e Ordem",
        'tag': "Notícias",
        'mensagem': "Realizadas exclusivamente por ordem expressa da Presidência da República, as missões de Garantia da Lei e da Ordem (GLO)",
        'link': "/"
    },
    {
        'imgUrl': 'img/noti_foto3.png',
        'data': "04 de Outubro de 2018",
        'titulo': "Lei e Legal",
        'tag': "Notícias",
        'mensagem': "Realizadas exclusivamente por ordem expressa da Presidência da República, as missões de Garantia da Lei e da Ordem (GLO)",
        'link': "/"
    }
]

def index(request):
    return render(request, 'index.html',{'atuacaoList': atuacaoList, 'noticiasList': noticiasList})