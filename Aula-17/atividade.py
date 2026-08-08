
# são duas vareaveis cada uma com valores de altura e largura
largura, altura = 400, 400

# uma variavel chamada "tela" que gyardas funçoes de uma bibioteca do py game os valores da funçao são duas vareaveis para inicializar o modulo de exibição
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Labirinto")

# tres vareaiveis toda guarda valores difertes e o tipo de daodos são um codigo hexadecimal para escolha de cores do jogo
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# a variavel "tamnho_celula" são valores da quntidade de pixel para formar o "personagem" ela determina a altura e largura
# "labirinto" e mais uma declaração de uma varealvel porem o tipo de dado que ela contem é tupla onde esse tipo de dado onde depois de declarado nao pode alterar
tamanho_celula = 40
labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 
x, y = 1 * tamanho_celula, 1 * tamanho_celula
velocidade = 40
# uma declaração de uma funçao onde guardas as vereaveis
def desenhar_labirinto():
    for linha in range(len(labirinto)):
        for coluna in range(len(labirinto[linha])):
            cor = preto if labirinto[linha][coluna] == 1 else branco
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))

# esse bloco de codigo esta guando tipo de dados de verdadeiro ou falso, que define todos os evendos utilzando funçoes, como atualizar a surpefice de exibicçao, Fps  
#dentro desse bloco é ultilizado uma estrutura de repeticçao onde vai  ser repetido ate o usuario escolher "quit" para fechar o jogo
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False


    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        novo_x = x - velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_RIGHT]:
        novo_x = x + velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_UP]:
        novo_y = y - velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y
    if teclas[pygame.K_DOWN]:
        novo_y = y + velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y


    tela.fill(branco)

    
    desenhar_labirinto()
    pygame.draw.rect(tela, vermelho, (x, y, tamanho_celula, tamanho_celula))


    pygame.display.flip()


    pygame.time.Clock().tick(10)


pygame.quit()

