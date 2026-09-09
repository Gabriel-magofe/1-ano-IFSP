param(
    [string]$File
)

$Folder = Split-Path -Parent $File
$Name = Split-Path -Leaf $File

Set-Location -LiteralPath $Folder
live-server . --open=$Name

# Configuração do VS Code — Code Runner + Live Server
# Objetivo

# Quero configurar o VS Code para que, ao usar Run Code (Ctrl + Alt + N) em qualquer arquivo .html:

# O Live Server sirva a pasta onde o HTML está.
# O navegador abra o próprio arquivo HTML que está aberto.
# O nome do HTML pode ser qualquer coisa (index.html, formulario.html, teste.html, etc.).
# CSS e JS devem funcionar normalmente.
# Estou usando Windows + PowerShell.
# O terminal aparece com (.venv), porque existe um ambiente virtual Python ativado, mas isso não é o problema.
# Node.js

# O Node.js foi instalado com sucesso.

# Estes comandos funcionaram:

# node --version
# npm --version


# Também apareceu o Chocolatey durante a instalação. Isso não é um problema; não é necessário mexer nele agora.

# Live Server

# O pacote live-server foi instalado com:

# npm install -g live-server


# A instalação terminou com:

# added 191 packages in 30s


# Houve alguns avisos npm warn deprecated, mas a instalação funcionou.

# O comando:

# live-server


# também funciona.

# Problema inicial

# Quando o Code Runner executava:

# live-server "PASTA\index.html"


# o Live Server dava problema porque ele deve servir a pasta, não receber o HTML como raiz.

# O comando manual que FUNCIONOU foi:

# live-server "C:\Users\gabri\OneDrive\Documents\1° ano IF\Tecnico\INGI\HTML\Aulas\2° Bimestre\26.08.2026 trabalho\formulario 1" --open="index.html"


# Esse comando:

# serve a pasta formulario 1;
# abre index.html;
# CSS funciona.
# Estrutura do projeto

# O projeto usado nos testes está em:

# C:\Users\gabri\OneDrive\Documents\1° ano IF\Tecnico\INGI\HTML\Aulas\2° Bimestre\26.08.2026 trabalho\formulario 1


# Existe um:

# index.html


# na pasta.

# settings.json atual/relevante

# O VS Code tem:

# "code-runner.runInTerminal": true,


# e um:

# "code-runner.executorMap": {


# A configuração original/atual do HTML foi sendo alterada durante os testes.

# O Code Runner demonstrou que as variáveis funcionam:

# $dir


# retorna a pasta do arquivo.

# $fileName


# retorna o nome do arquivo.

# $fullFileName


# retorna o caminho completo do arquivo.

# Teste que revelou isso

# Quando o HTML foi configurado temporariamente para:

# "html": "echo DIR=$dir && echo FILE=$fileName"


# o Code Runner executou:

# echo DIR="c:\Users\gabri\OneDrive\Documents\1° ano IF\Tecnico\INGI\HTML\Aulas\2° Bimestre\26.08.2026 trabalho\formulario 1\" ; if ($?) { echo FILE=index.html }


# e mostrou:

# DIR=c:\Users\gabri\OneDrive\Documents\1° ano IF\Tecnico\INGI\HTML\Aulas\2° Bimestre\26.08.2026 trabalho\formulario 1\
# FILE=index.html


# Portanto, o Code Runner sabe corretamente onde está o arquivo.

# Script criado

# Foi criado um arquivo:

# run-html.ps1


# na pasta do projeto.

# O script inicialmente era:

# param(
#     [string]$File
# )

# $Folder = Split-Path -Parent $File
# $Name = Split-Path -Leaf $File

# live-server $Folder --open=$Name


# Depois foi sugerido usar:

# param(
#     [string]$File
# )

# $Folder = Split-Path -Parent $File
# $Name = Split-Path -Leaf $File

# Set-Location -LiteralPath $Folder
# live-server . --open=$Name


# O script foi testado manualmente e FUNCIONOU.

# O comando manual usado foi:

# .\run-html.ps1 "C:\Users\gabri\OneDrive\Documents\1° ano IF\Tecnico\INGI\HTML\Aulas\2° Bimestre\26.08.2026 trabalho\formulario 1\index.html"

# Problema atual

# O problema está somente em fazer o Code Runner chamar o script corretamente.

# Tentamos:

# "html": "live-server \"$dir\" --open=\"$fileName\""


# Depois:

# "html": "live-server \"$dir\" --open=index.html"


# Depois uma chamada usando:

# powershell -ExecutionPolicy Bypass -Command


# Mas o Code Runner/PowerShell começou a produzir comandos com aspas e barras extras.

# Um exemplo do comando problemático foi:

# powershell -ExecutionPolicy Bypass -Command "& '"c:\Users\gabri\OneDrive\Documents\1° ano IF\Tecnico\INGI\HTML\Aulas\2° Bimestre\26.08.2026 trabalho\formulario 1\"\run-html.ps1' '"c:\Users\gabri\OneDrive\Documents\1° ano IF\Tecnico\INGI\HTML\Aulas\2° Bimestre\26.08.2026 trabalho\formulario 1\index.html"'"


# O erro foi:

# & : O termo ' c:\Users\gabri\...\formulario 1\\run-html.ps1' não é reconhecido...


# O problema evidente é a combinação de:

# aspas duplicadas;
# barra invertida extra;
# caminhos do Windows com espaços;
# Code Runner executando através do PowerShell.
# Última tentativa

# Foi sugerido usar:

# "html": "powershell -ExecutionPolicy Bypass -File \"$dirWithoutTrailingSlash\\run-html.ps1\" \"$fullFileName\"",


# Mas essa tentativa também não funcionou.

# Estado atual

# O mais importante:

# Node.js: FUNCIONANDO
# npm: FUNCIONANDO
# live-server: INSTALADO E FUNCIONANDO
# Live Server manual: FUNCIONANDO
# CSS pelo Live Server: FUNCIONANDO
# run-html.ps1 manualmente: FUNCIONANDO
# .venv: não é o problema
# Único problema restante: Code Runner → executar run-html.ps1 corretamente
# Comandos comprovadamente funcionais

# Servir a pasta e abrir o HTML:

# live-server "C:\Users\gabri\OneDrive\Documents\1° ano IF\Tecnico\INGI\HTML\Aulas\2° Bimestre\26.08.2026 trabalho\formulario 1" --open="index.html"


# Script:

# .\run-html.ps1 "C:\Users\gabri\OneDrive\Documents\1° ano IF\Tecnico\INGI\HTML\Aulas\2° Bimestre\26.08.2026 trabalho\formulario 1\index.html"

# Próximo passo

# Quando continuar, NÃO precisa reinstalar Node, npm ou Live Server.

# O próximo objetivo é encontrar uma forma confiável de o Code Runner executar:

# run-html.ps1


# passando automaticamente:

# $fullFileName


# sem o Code Runner estragar as aspas/caminhos.

# Também é importante lembrar que quero uma solução que funcione com qualquer nome de arquivo HTML, e que o Live Server deve servir a pasta, não o arquivo.