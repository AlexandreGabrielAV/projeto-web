from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime


app = Flask(__name__)

print (__name__)

@app.route('/')
def inicio():
    return '<h1>oiiiiii </h1>'

@app.route('/sobre')
def sobre():
    return '''
<h1 style='color:red'>Meu nome é: </h1>
<p>Alexandre Gabriel de <b>Agostini Viaro</b>
<!-- Tudo que eu pensar em HTML pode vir aqui -->
'''

@app.route('/curso')
def curso():
    return '''

<h1 style='color:blue'> O nome do curso é: </h1>
<p> <b>G.T.I</b> </P>
<p> Gestão da Tecnologia da Informação</p>
'''

@app.route('/var')
def variavel():
    palavra = 'Alexandre'
    return f'<h1>Adicionando texto de var: {palavra}</h1>'

@app.route('/idade/<int:ano>')
def idade(ano):
    calculoIdade = 2026 - ano 
    return f'Você tem {calculoIdade} anos!'

@app.route('/salvar/<nome>/produtos')
def salvar(nome):
    return f'Você salvou o produto [ {nome} ] com sucesso!'

@app.route('/html')
def pagina_html():
    return render_template('index.html')

@app.route('/cardapio')
def cardapio():
    return render_template('cardapio.html')











@app.route('/calcular/<nome>/<int:ano>')
def calcular(nome, ano):
    ano_atual = datetime.now().year
    idade = ano_atual - ano

    if idade > 18:
        status = 'Maior de idade'

    else:
        status = 'Menor de idade - ACESSO NEGADO!'

    return render_template('variaveis.html', nome_usuario = nome, ano_atual = ano_atual, nascimento = ano, idade = idade, status = status)





@app.route('/dicio')
def dicionario():
    dados= {
        'chave' : 'valor',
        'curso' : 'GTI',
        'local' : 'Fatec Jahu',
        'semestre' : 4,
    }
    return render_template('dicionario.html', **dados)





@app.route('/condicao/<int:numero>')
def condicao(numero):
    return render_template('condicao.html', numero=numero)



@app.route('/formulario', methods=['GET', 'POST'])
def formulario():

    if request.method == 'POST':
        nome = request.form.get['nome', 'Nada enviado']
        num1 = int(request.form['numero1'])
        num2 = float(request.form['numero2'])

        soma = num1 + num2
        sub = num1 - num2
        mult = num1 * num2
        div = num1 / num2

        # redireciona para outra rota
        # url_for chama a função, não a rota
        return redirect(url_for('exibir_resultado', nome=nome, 
                                                    soma=soma,
                                                    sub=sub,
                                                    mult=mult,
                                                    div=div))


    return render_template('formulario.html')

@app.route('/exibir')
def exibir_resultado():
    nome = request.args.get('nome')
    soma = request.args.get('soma')
    sub = request.args.get('sub')
    mult = request.args.get('mult')
    div = request.args.get('div')

    return render_template('exibir.html',   nome=nome, 
                                            soma=soma,
                                            sub=sub,
                                            mult=mult,
                                            div=div)

























#   --- ULTIMA COISA DO ARQUIVO --- 
if __name__ == '__main__':
    app.run(debug=True)
