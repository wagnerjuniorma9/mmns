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

atuacao_id = {
    'imgUrl': 'img/atu_foto1.png',
    'msg': 'O direito de família envolve uma série de assuntos que geralmente são muito pessoais, únicos e emocionalmente desafiadores. Decisões envolvendo seus \
            filhos e seu bem-estar financeiro podem ser complexas e com nuances e os resultados podem durar a vida toda. Nestas situações, você precisa mais do que\
            apenas um advogado que tenha experiência e conhecimento da lei. Você precisa de alguém que lhe proporcione orientação, pensamento criativo e que entenda\
            o quadro geral e o impacto que suas decisões terão sobre você. Os advogados de direito de família da lawyero estão empenhados em fornecer aos nossos \
            clientes a habilidade e o conhecimento necessários para atender aos objetivos e metas do cliente, fornecendo uma fonte confiável de representação. \
            Somos receptivos às necessidades de nossos clientes e nos orgulhamos de nossa atenção e disponibilidade para tratar dos assuntos dos clientes com \
            cuidado, respeito e sensibilidade.',
    'categoria': 'LEI DE FAMÍLIA'
}

noticia_id = {
    'imgUrl': 'img/noti_foto1.png',
    'data': "28 de Abril de 2018",
    'titulo': "Lei e Ordem",
    'tag': "Artigo",
    'msg': "\
        <p>Lorem ipsum dolor sente-se, consectetur adicing elit ut ullamcorper. leo, eget euismod orci. Cum sociis natoque penati bus et magnis dis. Aconselhamento \
        Aenean, lorem quis bibendum auctor, nisite elit consequat ipsum, nec sagittis sem nibh id elit. Duis sed odio sit amet nibh vulputate cursus a sit amet mauris \
        et. Morbi accumsan ipsum velit. Nam nec tellus um odio tincidunt auctor um ornare odio. Sed não mauris vitae erat consequat auctor eu in elit.</p>\
\
        <p>Você pode usar o aliquet de áudio. A sollicitudin aenean, lorem quis bibendumre autore nisi elit consequat ipsum, nec sagittis sem nibh id elit. Duis sed odio sitenent \
        amet nibh vuli putate cur sus a sit. \
        Lorem ipsum dolor sente-se, consectetur adicing elit ut ullamcorper. leo, eget euismod orci. Cum sociis natoque penati bus et magnis dis. Aconselhamento Aenean, lorem \
        quis bibendum auctor, nisite elit consequat ipsum, nec sagittis sem nibh id elit. Duis sed odio sit amet nibh vulputate cursus a sit amet mauris et. Morbi accumsan \
        ipsum velit. Nam nec tellus um odio tincidunt auctor um ornare odio. Sed não mauris vitae erat consequat auctor eu in elit.</p>\
\
        <p>Muitas pessoas não estão conscientes dos seus direitos legais e não prestam atenção à ajuda que podem obter do aconselhamento jurídico. Portanto, é muito importante \
        saber que você está ciente de seus direitos e procure ajuda legal quando necessário.</p>\
\
        <p>É um fato há muito estabelecido que um leitor se distrairá com o conteúdo legível de uma página ao analisar seu layout. O ponto de usar o Lorem Ipsum é que ele tem \
        uma distribuição de letras mais ou menos normal, em vez de usar 'Conteúdo aqui, conteúdo aqui', fazendo com que pareça legível em inglês. Muitos editores de editoração \
        eletrônica e editores de páginas da Web agora usam o Lorem Ipsum como seu texto de modelo padrão, e uma pesquisa por 'lorem ipsum' descobrirá muitos sites da Web ainda \
        em sua infância. Várias versões evoluíram ao longo dos anos, às vezes por acidente, às vezes de propósito (humor injetado e coisas do gênero).</p>\
\
        <p>O Que Fazer Primeiro Quando Encontrar Um Acidente?\
        Existem muitas variações de passagens de Lorem Ipsum disponíveis, mas a maioria sofreu alterações de alguma forma, por humor injetado, ou palavras aleatórias que não \
        parecem nem um pouco críveis. Se você vai usar uma passagem de Lorem Ipsum, você precisa ter certeza de que não há nada embaraçoso escondido no meio do texto. Todos \
        os geradores de Lorem Ipsum na Internet tendem a repetir blocos predefinidos conforme necessário, tornando este o primeiro verdadeiro gerador na Internet. Ele usa um \
        dicionário de mais de 200 palavras em latim, combinado com um punhado de estruturas de frases modelo, para gerar Lorem Ipsum que parece razoável. O Lorem Ipsum gerado \
        é, portanto, sempre livre de repetição, humor injetado ou palavras não características, etc.</p>"
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

def atuacao(request, id = None):
    return render(request, 'atuacao.html', {'id': id, 'atuacaoList': atuacaoList, 'atuacao_id': atuacao_id})

def noticia(request, id = None):
    return render(request, 'noticia.html', {'id': id, 'noticiasList': noticiasList, 'noticia_id': noticia_id})