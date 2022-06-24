# YT-SIWE
Extensão YouTube Shorts Em Watch (SIWE) é uma extensão para abrir vídeos no formato shorts como vídeos no formato normal.

# Começando

Essa extensão utiliza o typescript e é empacotada com o webpack.

## Instalações

Instale os pacotes necessários para o funcionamento:

    npm install

## Scripts

Dentro do *package.json* na área de scripts você pode verificar que existem dois scripts, chamados de **start** e **build**.

Você pode ler a descrição dos scripts ou clicar [aqui](#build) para aprender como fazer a build da extensão.

### Start - Script

O Start convoca o compilador do typescript para compilar os arquivo para javascript.

### Build - Script

O Build convoca o webpack para compactar os arquivos javascript gerados pelo typescript e salva-los como um único arquivo chamado de *index.js* dentro de *./siwe/extension/dist*.

Dessa os arquivos são unidos em um só, deixando a extensão mais leve e evitando ter que adicionar diversos arquivos ao *manifest* além de evitar erros de *imports*.

## Build

Caso você esteja utilizando o *tsc --watch* para compilar os arquivos, você pode só utilizar o *npm run build* para fazer a build.

Já caso queria executar os dois (start e build) eu recomendo instalar o *npm-run-all* como global, ele irá permitir a execução de mais de um script, dessa forma poupando um pouco de tempo.

Instale ele:

    npm install npm-run-all -g

Executando:

    npm-run-all start build

Dessa forma ele irá compilar para javascript e fazer a build.