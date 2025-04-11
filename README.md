# 🎵 Billboard to Spotify Playlist Generator
Este script em Python automatiza a criação de uma playlist no Spotify com as Top 100 músicas da Billboard de uma data específica.

## 🔧 Tecnologias utilizadas
BeautifulSoup – Para fazer web scraping da Billboard Hot 100

requests – Para requisições HTTP ao site da Billboard

Spotipy – Cliente da API do Spotify para criação e gerenciamento de playlists

python-dotenv – Para gerenciar variáveis de ambiente com segurança

## 📌 Como funciona
O usuário insere uma data no formato YYYY-MM-DD.

O script faz uma requisição ao site da Billboard e busca o ranking Hot 100 correspondente.

Utilizando o BeautifulSoup, são extraídos os títulos das 100 músicas da lista.

Cada música é pesquisada no Spotify via Spotipy, e os URIs são coletados.

Uma nova playlist privada é criada no Spotify do usuário com as 100 músicas daquele período.

## ✅ Requisitos
Conta no Spotify

Configuração de variáveis de ambiente com SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET e SPOTIPY_REDIRECT_URI
