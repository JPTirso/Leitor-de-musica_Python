from browser import init_brower

import time
def main():
    driver = init_brower()
    try:
        driver.get("https://duckduckgo.com")
        campoPesquisa = driver.find_element("class name", "search-input_searchInput__Avyuh")
        campoPesquisa.send_keys("Vou levar - O Grilo letra")
        campoPesquisa.submit()
        time.sleep(1)
        link = driver.find_elements("class name", "react-results--main")
        link[0].click()
        time.sleep(1)
        driver.find_element("class name", "player-media-play").click()
        letraPanico = driver.find_element("class name", "lyric-original").text.split("\n")
        input("Aperte quando começar a musica")
        time.sleep(16.5)
        for paragrafo in letraPanico:
            print(paragrafo)
            if paragrafo == "Do mesmo":
                time.sleep(6.5)
            match paragrafo:
                case "Eu vou levar, vou levar":
                    time.sleep(len(paragrafo)*0.08)
                case "Eu vou sair, eu vou cantar":
                    time.sleep(len(paragrafo)*0.06)
                case "Os meus segredos os meus dilemas":
                    time.sleep(len(paragrafo)*0.06)
                case "Enfrentar os meus medos em uma sala de cinema":
                    time.sleep(len(paragrafo)*0.08)
                case "Levar os meus inimigos para o bar":
                    time.sleep(len(paragrafo)*0.08)
                    time.sleep(9)
                case _:
                    time.sleep(len(paragrafo)*0.125)
        time.sleep(3)
        print("Não acredito que toquei essa musica pelo vs code ksaksakskaskaks")
        input("Aperte qualquer tecla para continuar")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()