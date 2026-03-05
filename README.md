Monitor de Execução com Python + GitHub Actions (Protótipo)

Este repositório é um protótipo simples que demonstra como executar uma tarefa Python de forma agendada utilizando GitHub Actions e monitorar sua execução através do Healthchecks.

Visão Geral

O projeto executa um script Python em intervalos regulares usando o scheduler do GitHub Actions. Ao final da execução, o script envia um ping (heartbeat) para o Healthchecks para informar que a rotina foi executada com sucesso.

Caso a execução não ocorra ou falhe antes de enviar o ping, o Healthchecks pode detectar o problema e gerar alertas.

Arquitetura

GitHub Actions (cron scheduler)
→ Executa script Python
→ Script envia ping
→ Healthchecks registra a execução

Tecnologias Utilizadas

Python

GitHub Actions

Healthchecks

Como Funciona

O GitHub Actions executa o workflow em um intervalo definido por cron.

O workflow instala as dependências e executa o script Python.

O script envia um ping para o endpoint do Healthchecks.

O Healthchecks registra que a execução ocorreu corretamente.

Exemplo do Script Python
import requests

HEALTHCHECK_URL = "https://hc-ping.com/70f89754-ef69-476e-aa0e-595b67765cf6"

def main():
    print("Executando tarefa agendada...")
    requests.get(HEALTHCHECK_URL)
    print("Ping enviado com sucesso!")

if __name__ == "__main__":
    main()
Workflow do GitHub Actions

Exemplo de configuração do workflow:

name: Monitor Script

on:
  schedule:
    - cron: "*/15 * * * *"
  workflow_dispatch:

jobs:
  run:
    runs-on: ubuntu-latest
    timeout-minutes: 5

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Instalar dependências
        run: pip install requests

      - name: Executar script
        run: python app.py
Executando Localmente

Para testar o script localmente:

pip install requests
python app.py
Monitoramento

O Healthchecks monitora a execução do job. Caso o ping esperado não seja recebido dentro do intervalo configurado, o sistema marca a rotina como falha e pode disparar notificações.

Objetivo do Projeto

Este repositório foi criado como um protótipo para experimentar uma arquitetura simples de agendamento e monitoramento de tarefas utilizando serviços gratuitos.

Possíveis Melhorias Futuras

Adicionar logs estruturados

Utilizar GitHub Secrets para armazenar URLs sensíveis

Enviar sinais de início (/start) e falha (/fail) para o Healthchecks

Implementar tratamento de erros e retentativas
