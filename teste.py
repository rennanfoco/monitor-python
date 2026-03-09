import requests
import time

HEALTHCHECK_URL = "https://hc-ping.com/70f89754-ef69-476e-aa0e-595b67765cf6"

def main():
    print("Executando rotina de teste...")
    time.sleep(2)

    # Simulação de sucesso
    print("Rotina finalizada com sucesso")

    # Envia ping de sucesso
    requests.get(HEALTHCHECK_URL)
    print("Ping realizado com sucesso")


if __name__ == "__main__":
    main()
