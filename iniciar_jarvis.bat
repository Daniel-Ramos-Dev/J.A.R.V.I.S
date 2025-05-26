@echo off
title Iniciando JARVIS...

:: Abre o Ollama (LLaMA 3) em segundo plano
start "" /MIN cmd /C "ollama run llama3"

:: Aguarda alguns segundos para a IA estar pronta
echo Aguardando o Ollama iniciar...
timeout /t 5 >nul

:: Executa o Jarvis
echo Iniciando o Jarvis...
python main.py

pause
+