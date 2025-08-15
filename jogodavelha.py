# --- Importações de módulos ---
import pygame           # Biblioteca para criar jogos e interface gráfica
import sys              # Para manipulação de saída e encerramento do programa
import socket           # Para comunicação em rede
import json             # Para serialização/deserialização de dados
import ipaddress        # Para validar e identificar tipos de IP
import threading        # Para criar threads (execução paralela)
import time             # Para controlar delays e temporizadores
# --- Inicialização do Pygame ---
try:
    pygame.init()       # Inicializa todos os módulos do Pygame
    pygame.font.init()  # Inicializa o módulo de fontes
except Exception as e:
    print(f"Erro ao inicializar Pygame: {e}")
    sys.exit()          # Encerra o programa caso haja erro
# --- Definição de cores ---
FUNDO_ESCURO = (28, 28, 28)
CINZA_FUNDO = (40, 40, 40)
BRANCO_CLARO = (240, 240, 240)
COR_X = (255, 90, 90)
COR_O = (60, 140, 255)
VERDE_DESTAQUE = (80, 255, 80)
VERMELHO_DESTAQUE = (255, 80, 80)
# --- Configurações da tela ---
LARGURA, ALTURA = 600, 700
TAM_CELULA = 200
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Velha em Rede")
# --- Fontes ---
FONTE_TITULO = pygame.font.SysFont('Arial', 40, bold=True)
FONTE_PADRAO = pygame.font.SysFont('Arial', 32)
FONTE_MENOR = pygame.font.SysFont('Arial', 24)
FONTE_JOGADOR_GRANDE = pygame.font.SysFont('Arial', 150, bold=True)
CLOCK = pygame.time.Clock()
# --- Variáveis de estado ---
estado_jogo = {'tabuleiro': None, 'vencedor': None, 'empate': False, 'turno': 'X', 'mensagens': []}
sock_comunicacao = None
oponente_addr = None
rodando_jogo = False
conectado = False
thread_rede = None
lock_rede = threading.Lock()
def desenhar_gradiente(superfície, cor_inicio, cor_fim):
para y no intervalo(ALTURA):
r = cor_inicio[0] + (cor_fim[0] - cor_inicio[0]) * y / ALTURA
g = cor_inicio[1] + (cor_fim[1] - cor_inicio[1]) * y / ALTURA
b = cor_inicio[2] + (cor_fim[2] - cor_inicio[2]) * y / ALTURA
pygame.draw.line(superfície, (r, g, b), (0, y), (LARGURA, y))

def desenhar_texto_centralizado(surface, texto, fonte, cor, y):
texto_render = fonte.render(texto, True, cor)
ret = texto_render.get_rect(center=(LARGURA // 2, y))
surface.blit(texto_render, ret)

def desenhar_botao(x, y, largura, altura, cor, texto, fonte, texto_cor):
ret = pygame.Rect(x, y, largura, altura)
pygame.draw.rect(TELA, cor, ret, border_radius=20)
txt_render = fonte.render(texto, True, texto_cor)
TELA.blit(txt_render, txt_render.get_rect(center=ret.center))
retornar ret

def desenhar_caixa_texto(x, y, largura, altura, texto, ativo, cor_borda):
ret = pygame.Rect(x, y, largura, altura)
pygame.draw.rect(TELA, BRANCO_CLARO, ret, border_radius=10)
pygame.draw.rect(TELA, cor_borda, ret, 3, border_radius=10)
txt_render = FONTE_PADRAO.render(texto, True, FUNDO_ESCURO)
TELA.blit(txt_render, (ret.x + 10, ret.y + 10))
return ret

def desenhar_tabuleiro(surface, tabuleiro):
if not tabuleiro:
return
pygame.draw.rect(surface, CINZA_FUNDO, (0, 0, LARGURA, LARGURA))
for i in range(3):
for j in range(3):
x = j * TAM_CELULA
y = i * TAM_CELULA
rect = pygame.Rect(x, y, TAM_CELULA, TAM_CELULA)
pygame.draw.rect(surface, FUNDO_ESCURO, rect, 3)
if tabuleiro[i][j] != ' ':
simbolo = tabuleiro[i][j]
cor_simbolo = COR_X if simbolo == 'X' else COR_O
texto = FONTE_JOGADOR_GRANDE.render(simbolo, True, cor_simbolo)
texto_rect = texto.get_rect(center=rect.center)
superfície.blit(texto, texto_rect)
