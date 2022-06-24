import turtle as t

pontosjogador1 = 0      # Placar do Jogador 1
pontosjogador2 = 0      # Placar do Jogador 2

window = t.Screen()
window.title("Ping Pong Atômico")     #Título do Jogo
window.bgcolor('black')               #Cor de fundo
window.setup(width=800,height=600)    #Dimensões da Janela do jogo
window.tracer(1)                      #Taxa de atualização da tela do jogo

#Criação das barras dos jogadores

barra_esquerda = t.Turtle()           # Associação da variável barra_esquerda com a biblioteca turtle, para que assim seja possível de podermos utilizar seus métodos e funções
barra_esquerda.speed(0)               #Definição da velocidade da barra
barra_esquerda.shape('square')     #Definição da forma da barra
barra_esquerda.color('white')        #Cor da barra
barra_esquerda.shapesize(stretch_wid= 5,stretch_len= 1)   #Tamanho da forma
barra_esquerda.penup()                                    # Para que a trajetória dos objetos do jogo não deixem rastros ao se mover
barra_esquerda.goto(-350, 0)                             #Definição da localização inicial e final da barra

barra_direita = t.Turtle()
barra_direita.speed(0)
barra_direita.shape('square')
barra_direita.color('white')
barra_direita.shapesize(stretch_wid=5, stretch_len=1)
barra_direita.penup()
barra_direita.goto(350, 0)

#Criação da bolinha(átomo)

atom = t.Turtle()
atom.speed(0)           # Velocidade com que o átomo se move na tela ao receber uma função que define sua posição
atom.shape('circle')    #Formato
atom.color('purple')    #Cor
atom.penup()            #Sem traços
atom.goto(0, 0)         #Posição a qual o átomo inicia quando o game é iniciado
atom.shapesize(5)       #Tamanho do formato atômico
atomdirecaox = 5.0      #Variáveis que serão utilizadas para definir a posição e velocidade do átomo
atomdirecaoy = 5.0
velocidades_atomicas = [7,9,11,13]  #Lista de velocidades para cada átomo
cores_atomicas = ['orange', 'gray', 'blue', 'white']  #Lista de cores dos átomos
tamanhos_atomicos = [4, 3, 2, 0.5]   #Lista de tamanhos do átomo

#Definindo uma variável que atualiza o placar do jogo
att = t.Turtle()
att.speed(0)
att.color('white')
att.penup()
att.hideturtle()
att.goto(0, 260)  #A posição do placar está localizada no eixo y na coordenada 260
att.write("Pong Atômico", align='center', font=('comic sans',22, 'bold'))   #Fonte e localização do texto inicial/placar

#Movimentação das barras

def barra_direita_cima():  # Define a movimentação da barra direita para cima em 90°
    if barra_direita.ycor()> 290:
        barra_direita.sety(290)
    else:
        y = barra_direita.ycor()
        y = y + 40
        barra_direita.sety(y)

def barra_direita_baixo():   # Define a movimentação da barra direita para baixo em 90°
    if barra_direita.ycor()< -290:
        barra_direita.sety(-290)
    else:
        y = barra_direita.ycor()
        y = y - 40
        barra_direita.sety(y)

def barra_esquerda_cima():
    if barra_esquerda.ycor()>290:
        barra_esquerda.sety(290)
    else:
        y = barra_esquerda.ycor()
        y = y + 40
        barra_esquerda.sety(y)

def barra_esquerda_baixo():
    if barra_esquerda.ycor()<-290:
        barra_esquerda.sety(-290)
    else:
        y = barra_esquerda.ycor()
        y = y - 40
        barra_esquerda.sety(y)

# Definindo as teclas para controlar as barras

window.listen()          #Este método começará a coletar quando uma tecla for pressionada, e se sim, aplicará às suas devidas funções
window.onkeypress(barra_esquerda_cima, 'w')
window.onkeypress(barra_esquerda_baixo, 's')
window.onkeypress(barra_direita_cima, 'Up')
window.onkeypress(barra_direita_baixo, 'Down')

#Variáveis utilizadas como contadores.
cor = 0
vel = 0
tam = 0

#Agora criaremos um loop que constantemente atualizará a posição da bola(átomo).
while True:
    window.update()  #Atualizará a janela do jogo, e como está dentro de um While True, sempre atualizará a janela do jogo, para manter o jogo rodando

    # Abaixo definiremos que tanto a posição do átomo no eixo x ou y, será dada pela sua coordenada atual, + a sua direção no seu eixo
    atom.setx(atom.xcor()+atomdirecaox)
    atom.sety(atom.ycor()+atomdirecaoy)

    #Limite da tela no eixo vertical
    if atom.ycor()> 290:
        atom.sety(290)
        atomdirecaoy = atomdirecaoy * -1        # Após a colisão, o átomo sairá em uma direção perpendicular a qual veio

    if atom.ycor()<-290:
        atom.sety(-290)
        atomdirecaoy = atomdirecaoy * -1

    #Limite da tela no eixo horizontal
    if atom.xcor() > 390:       #Caso o átomo tenha ultrapassado a coordenada 390, será um ponto, então:
        atom.goto(0, 0)         #A bola retorna ao centro;
        pontosjogador1 = pontosjogador1 + 1     #O placar é aumentado em 1
        cor += 1    # Os contadores são atualizados
        vel += 1    #
        tam += 1    #
        if cor >= len(cores_atomicas):  # Verificando se o contador não será maior que o len() da lista de cores, e se for, então o contador será 4
            cor = 4
        else:
            #Atualizações das propriedades atômicas
            cores = cores_atomicas[cor]  #A cor do átomo será agora dada por uma cor na lista de cores, com base no contador, que dirá qual index da lista será
                                         #pego para passar a cor à função de cores.
            velocidade = velocidades_atomicas[vel]      #O mesmo vale para a velocidade, e tamanho logo abaixo
            tamanho = tamanhos_atomicos[tam]
            atom.shapesize(tamanho)      #O tamanho agora será dado pela variável tamanho, que conterá um índice da lista de tamanhos.
            atom.color(cores)            #O mesmo vale para as cores
            atomdirecaox = velocidade * -1  # A velocidade agora é atualizada, e a direção será contrária a quem marcou o ponto
            atomdirecaoy = velocidade * -1
        att.clear()    # Limpando o placar, para que não haja sobreposição de placares
        att.write("Nelson:{}               Bohr:{}".format(pontosjogador1, pontosjogador2),align= 'center' ,font=('comic sans',22, 'bold'))  #Placar do jogo

    #As mesmas situações ocorrem caso o segundo jogador marque o ponto
    if atom.xcor() < -390:
        atom.goto(0, 0)
        att.clear()
        pontosjogador2 = pontosjogador2 + 1
        cor += 1
        vel += 1
        tam += 1
        if cor >= len(cores_atomicas):
            cor = 4
        else:
            #Atualizações das propriedades atômicas
            cores = cores_atomicas[cor]
            velocidade = velocidades_atomicas[vel]
            tamanho = tamanhos_atomicos[tam]
            atom.color(cores)
            atom.shapesize(tamanho)
            atomdirecaox = velocidade * -1
            atomdirecaoy = velocidade * -1
        att.clear()
        att.write("Nelson:{}               Bohr:{}".format(pontosjogador1, pontosjogador2), align='center', font=('comic sans', 22, 'bold'))


# Definição das Colisões do átomo com as barras

    # Se a posição do átomo estiver entre as coordenadas 340 e 350 para ambos os lados, e a barra estiver na mesma posição na coordenada y que a bolinha, esta terá seu sentido alterado, dando uma impressão de colisão
    if (atom.xcor() > 340)and(atom.xcor() < 350)and(atom.ycor() < barra_direita.ycor()+40 and atom.ycor() > barra_direita.ycor()-40):
        atom.setx(340)
        atomdirecaox = atomdirecaox * -1
    #A mesma situação também se aplica para caso o outro jogador defenda a bolinha
    if (atom.ycor() > -340)and(atom.xcor() < -350)and((atom.ycor() < barra_esquerda.ycor()+40) and atom.ycor() > barra_esquerda.ycor()-40):
        atom.setx(-340)
        atomdirecaox = atomdirecaox*-1