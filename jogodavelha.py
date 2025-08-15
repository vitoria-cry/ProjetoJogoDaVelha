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
