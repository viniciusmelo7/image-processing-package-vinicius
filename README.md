# Image Processing Package Vinicius

Pacote Python simples para processamento de imagens, desenvolvido como parte do curso da DIO.

O projeto reúne funções utilitárias para leitura, salvamento, visualização e transformações básicas de imagens usando `numpy`, `matplotlib` e `scikit-image`.

## Funcionalidades

- Leitura e salvamento de imagens
- Redimensionamento com proporção
- Comparação entre duas imagens
- Transferência de histograma
- Exibição de imagens e resultados
- Plotagem de histogramas RGB

## Estrutura do Projeto

```text
image-processing-package-vinicius/
├── image_processing/
│   ├── processing/
│   │   ├── combination.py
│   │   └── transformation.py
│   ├── utils/
│   │   ├── io.py
│   │   └── plot.py
│   └── __init__.py
├── requirements.txt
├── setup.py
└── README.md
```

## Tecnologias Utilizadas

- Python 3
- NumPy
- Matplotlib
- scikit-image

## Instalação

Clone o repositório:

```bash
git clone https://github.com/viniciusmelo7/image-processing-package-vinicius.git
```

Entre na pasta do projeto:

```bash
cd image-processing-package-vinicius
```

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Se quiser instalar o pacote localmente em modo editável:

```bash
pip install -e .
```

## Como Usar

### Importando funções diretamente do pacote

```python
from image_processing import (
    read_image,
    save_image,
    resize_image,
    find_difference,
    transfer_histogram,
    plot_image,
    plot_result,
    plot_histogram,
)
```

### Exemplo de leitura e redimensionamento

```python
from image_processing import read_image, resize_image, plot_result

image = read_image("foto.jpg")
image_resized = resize_image(image, 0.5)

plot_result(image, image_resized)
```

### Exemplo de comparação entre imagens

```python
from image_processing import read_image, find_difference, plot_result

image1 = read_image("imagem1.jpg")
image2 = read_image("imagem2.jpg")

difference = find_difference(image1, image2)
plot_result(image1, image2, difference)
```

### Exemplo de transferência de histograma

```python
from image_processing import read_image, transfer_histogram, plot_result

image1 = read_image("imagem1.jpg")
image2 = read_image("imagem2.jpg")

result = transfer_histogram(image1, image2)
plot_result(image1, image2, result)
```

## Módulos

### `image_processing.processing`

- `resize_image(image, proportion)`: redimensiona a imagem com base em uma proporção entre `0` e `1`
- `find_difference(image1, image2)`: calcula a diferença estrutural entre duas imagens do mesmo tamanho
- `transfer_histogram(image1, image2)`: transfere o histograma de uma imagem para outra

### `image_processing.utils`

- `read_image(path, is_gray=False)`: lê uma imagem a partir de um caminho
- `save_image(image, path)`: salva uma imagem em disco
- `plot_image(image)`: exibe uma imagem
- `plot_result(*args)`: exibe imagens lado a lado
- `plot_histogram(image)`: exibe histogramas RGB da imagem

## Objetivo do Projeto

Este projeto foi desenvolvido com fins educacionais, com foco em praticar:

- organização de um pacote Python
- modularização de código
- uso de bibliotecas para processamento de imagens
- preparação de um projeto para publicação no GitHub

## Autor

Vinicius Melo

## Licença

Este projeto pode ser utilizado para fins de estudo e aprendizagem.
