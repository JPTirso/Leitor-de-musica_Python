from browser import init_brower
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
def main():
    driver = init_brower()
    wait = WebDriverWait(driver, 10)
    try:
        driver.get("https://www.palcomp3.com.br/ogrilo/vou-levar/")
        time.sleep(1)
        letraPanico = wait.until( EC.presence_of_element_located((By.CLASS_NAME, "_3SKTX"))).text.split("\n")
        wait.until( EC.presence_of_element_located((By.CSS_SELECTOR,'[title="Tocar música"]'))).click()
        time.sleep(16.5)
        for paragrafo in letraPanico:
            print(paragrafo)
            if paragrafo == "Do mesmo":
                time.sleep(7)
            # Pequenas alterações por que o ritmo não é 100% igual em toda a musica
            match paragrafo:
                case "E que vontade que me dá":
                    time.sleep(len(paragrafo)*0.14)
                case "Eu vou levar, vou levar":
                    time.sleep(len(paragrafo)*0.08)
                case "Os meus problemas pra dançar":
                    time.sleep(len(paragrafo)*0.06)
                case "Eu vou sair, eu vou cantar":
                    time.sleep(len(paragrafo)*0.075)
                case "Os meus segredos os meus dilemas":
                    time.sleep(len(paragrafo)*0.085)
                case "Enfrentar os meus medos em uma sala de cinema":
                    time.sleep(len(paragrafo)*0.075)
                case "Olhando bem de perto nada é fácil assim":
                    time.sleep(len(paragrafo)*0.095)
                case "Levar os meus inimigos para o bar":
                    time.sleep(len(paragrafo)*0.08)
                    time.sleep(10.5)
                case _:
                    time.sleep(len(paragrafo)*0.12)
        time.sleep(3)
        print("Não acredito que toquei essa musica pelo vs code ksaksakskaskaks")
        input("Aperte qualquer tecla para continuar")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()