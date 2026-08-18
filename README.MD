# 🎵 Leitor de Música

Script em Python que abre uma música no [PalcoMP3](https://www.palcomp3.com.br/), dá play automaticamente pelo navegador e exibe a letra no terminal, linha por linha, sincronizada com o ritmo da faixa — como um teleprompter/karaokê rodando no console.

## Como funciona

O script usa Selenium para automatizar o Firefox e:

1. Abre a página da música no PalcoMP3;
2. Extrai o texto da letra diretamente do elemento HTML da página;
3. Clica no botão de play da música;
4. Aguarda o tempo de introdução (instrumental) da faixa;
5. Percorre a letra linha por linha, imprimindo cada trecho no terminal e aguardando um tempo calculado antes de mostrar o próximo, criando o efeito de sincronia com o que está tocando.

## Tecnologias

- Python 3.10+ (o código usa `match/case`)
- [Selenium](https://www.selenium.dev/)
- Firefox

## Pré-requisitos

- Python 3.10 ou superior
- Firefox instalado
- Biblioteca `selenium`
- Em versões do Selenium anteriores à 4.6, é necessário instalar o [geckodriver](https://github.com/mozilla/geckodriver/releases) manualmente e deixá-lo disponível no PATH. A partir da 4.6, o próprio Selenium Manager baixa e configura o driver automaticamente.

## Instalação

```bash
git clone <url-do-repositorio>
cd Leitor-de-musica_Python-main
pip install selenium
```

## Como usar

```bash
cd src
python main.py
```

O Firefox abre sozinho, acessa a página da música e clica em play. A letra vai aparecendo no terminal acompanhando o ritmo da faixa. No final, é só apertar qualquer tecla para o navegador fechar.

## ⚠️ Limitação atual

Por enquanto, o projeto funciona apenas com **uma única música**: ["Vou Levar", do O Grilo](https://www.palcomp3.com.br/ogrilo/vou-levar/).

Isso acontece porque a sincronização entre a letra e o áudio não é automática: cada trecho tem um tempo de espera (`time.sleep`) calibrado manualmente para o ritmo específico dessa faixa, já que a música não tem um andamento uniforme do início ao fim. Para funcionar com outras músicas, seria preciso recalcular esses tempos, pois eles não se aplicam a faixas com duração, andamento ou estrutura de letra diferentes.

## Estrutura do projeto

```
Leitor-de-musica_Python-main/
├── .gitignore
└── src/
    ├── browser.py   # Inicializa o navegador Firefox via Selenium
    └── main.py      # Abre a música, extrai a letra e sincroniza a exibição no terminal
```

## Possíveis melhorias futuras

- Permitir escolher a música (URL) em vez de deixá-la fixa no código;
- Calcular a sincronização automaticamente (ex.: a partir da duração real de cada trecho), no lugar de tempos fixos por linha;
- Suporte a outros navegadores além do Firefox;
- Tratamento de erros para quando os elementos da página não forem encontrados (ex.: se o PalcoMP3 mudar o layout).

---

Projeto pessoal e sem vínculo com o PalcoMP3. Por depender de elementos específicos da página do site, pode parar de funcionar se o layout for alterado.