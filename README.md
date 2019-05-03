Utilizando o [ThingSpeak](https://thingspeak.com/) estou fazendo o monitoramento em tempo real da temperatura e da umidade do Laboratório Didático de Circuitos Elétricos da Universidade Federal de Rondônia (UNIR).

O meu canal pode ser acessado aqui:
https://thingspeak.com/channels/770648

O sensor utilizado foi um DHT11, que está conectado com uma Raspberry Pi.

A Raspberry Pi coleta as informações, processa os valores e os envia para o ThingSpeak.

O canal do ThingSpeak recebe as informações e as transforma em um gráfico que pode ser observado em tempo real via computador, ou ainda através de um aplicativo de celular.

Para sistema Android: https://play.google.com/store/apps/details?id=com.cinetica_tech.thingview&hl=pt_BR

Para iOS: https://itunes.apple.com/us/app/thingview/id1284878579?mt=8

No *site* do ThingSpeak qualquer pessoa pode encontrar o meu canal através do meu *user_ID* ou através das *tags* que eu usei.  <br/>
**user ID:** larissaspf  <br/>
**tags:** temperatura, sensoriamento, unir, porto velho, brasil, engenharia elétrica, umidade, universidade federal de rondônia.

Pelos aplicativos *mobile* é necessário o *ID do Canal*.  <br/>
**ID do Canal:** 770648

O *script* em python (https://github.com/EmeraldL/web-monitoring-DHT11/blob/master/dht11_rasp.py) roda automaticamente com a inicialização do sistema da Raspberry Pi, pois foi configurado para assim fazer. Eu indico esse site para saber mais a respeito: https://cadernodelaboratorio.com.br/2015/06/10/inicializando-um-programa-automaticamente-no-raspberrypi/
