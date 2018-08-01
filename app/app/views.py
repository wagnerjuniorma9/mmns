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

equipeList = [
    {
        'imgUrl': 'img/equipe_foto1.png',
        'facebookLink': '',
        'googleMaisLink': '',
        'TwitterLink': '',
        'email': 'wagner.junior@ma9.com.br',
        'nome': 'Eduardo Collin',
        'categoria': 'Advogado Titular'
    },
    {
        'imgUrl': 'img/equipe_foto2.png',
        'facebookLink': 'http://google.com.br',
        'googleMaisLink': 'http://google.com.br',
        'twitterLink': 'http://google.com.br',
        'email': 'wagnerjunior645@hotmail.com',
        'nome': 'Maria Alcantara',
        'categoria': 'Advogado Titular'
    },
    {
        'imgUrl': 'img/equipe_foto3.png',
        'facebookLink': '',
        'googleMaisLink': '',
        'TwitterLink': '',
        'email': '',
        'nome': 'Bruno Linhares',
        'categoria': 'Advogado Titular'
    },
    {
        'imgUrl': 'img/equipe_foto4.png',
        'facebookLink': '',
        'googleMaisLink': '',
        'TwitterLink': '',
        'email': '',
        'nome': 'Alberto Braga',
        'categoria': 'Advogado Titular'
    }
]

equipe_id = {
    'imgUrl': 'img/equipe_foto3.png',
    'msg': 'Obteve seu doutorado em Direito pela Villanova University School of Law em Villanova, Pensilvânia, em 2001. Ele obteve seu diplo\
            ma de graduação da Denison University em 1998, tendo estudado \
            Filosofia com ênfase adicional no pensamento político antigo. Enquanto estudava na Faculdade de Direito da Universidade de Villanova, R\
            obert trabalhou como associado de verão \
            na Greenberg Traurig, em Los Angeles, Califórnia, e também como editor de artigos externos da Escola de Direito Ambiental da Faculda\
            de de Direito da Universidade Villanova. Acredita \
            firmemente que, para poder ter sucesso nesta indústria, você tem que dedicar seu tempo, trabalho e emoções para que os clientes obten\
            ham o melhor resultado e man\
            tenham os clientes em um estado de espírito que eles podem confiar.Ele ajudou seus clientes a recuperar mais de US $ 150.000 em vá\
            rios casos e tem uma taxa de sucesso quase perfeita.',
    'nome': 'EDUARDO COLLIN'
}


def index(request):
    return render(request, 'index.html',{'atuacaoList': atuacaoList, 'noticiasList': noticiasList, 'equipeList': equipeList})

def contato(request):
    return render(request, 'contato.html')

def carreira(request):
    return render(request, 'carreira.html')

def sobrenos(request):
    return render(request, 'sobrenos.html')

def equipe(request, id = None):
    return render(request, 'equipe.html', {'id': id, 'equipeList': equipeList, 'equipe_id': equipe_id})