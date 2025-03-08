# Exibição de Vídeo de Câmera RTSP com OpenCV e Tkinter

Este projeto demonstra como exibir o vídeo de uma câmera RTSP em uma interface gráfica utilizando Python, OpenCV e Tkinter. O script captura o vídeo da câmera, converte os frames para um formato compatível com Tkinter e os exibe em uma janela.

## Requisitos

Para executar este projeto, você precisará das seguintes bibliotecas Python instaladas:

- **OpenCV**: Para capturar e processar o vídeo da câmera.
- **Tkinter**: Para criar a interface gráfica.
- **Pillow (PIL)**: Para converter os frames do OpenCV em um formato que o Tkinter pode exibir.

Você pode instalar as dependências usando o seguinte comando:

```bash
pip install opencv-python-headless pillow
```

## Como Funciona

### Captura do Vídeo:

- O script utiliza a função `cv2.VideoCapture` para se conectar à câmera RTSP usando a URL fornecida.
- A URL RTSP deve seguir o formato: `rtsp://usuário:senha@endereço_ip:porta/caminho`.

### Conversão dos Frames:

- Cada frame capturado é convertido de **BGR** (formato padrão do OpenCV) para **RGB** (formato compatível com Tkinter).
- O frame é então convertido em uma imagem que pode ser exibida em um widget `Label` do Tkinter.

### Exibição em Tempo Real:

- A função `update_image` é chamada repetidamente a cada **10 milissegundos** para atualizar o frame exibido na janela.
- Isso cria a ilusão de um vídeo em tempo real.

### Interface Gráfica:

- A janela é criada usando Tkinter, com um `Label` para exibir os frames.
- O loop principal do Tkinter (`root.mainloop`) mantém a janela aberta e responsiva.

## Como Executar

Substitua a URL RTSP no código pela URL da sua câmera:

```python
rtsp_url = "rtsp://admin:123456@192.168.1.11:554/path"
```

Execute o script:

```bash
python nome_do_arquivo.py
```

Uma janela será aberta, exibindo o vídeo da câmera RTSP em tempo real.

## Estrutura do Código

### Importações:

- `cv2`: Para capturar e processar o vídeo.
- `tkinter`: Para criar a interface gráfica.
- `PIL.Image` e `PIL.ImageTk`: Para converter e exibir os frames.

### Função `update_image`:

- Captura um frame da câmera.
- Converte o frame para RGB e o exibe no `Label`.
- Agenda a próxima atualização após **10ms**.

### Inicialização:

- Conecta à câmera RTSP.
- Cria a janela Tkinter e o `Label` para exibição.

### Loop Principal:

- Mantém a janela aberta e atualiza os frames.

## Observações

- Certifique-se de que a URL RTSP está correta e que a câmera está acessível na rede.
- O desempenho pode variar dependendo da resolução do vídeo e da velocidade da rede.
- Para encerrar o programa, feche a janela do Tkinter.

## Exemplo de URL RTSP

A URL RTSP pode variar dependendo do fabricante da câmera. Aqui está um exemplo comum:

```bash
rtsp://usuário:senha@192.168.1.100:554/stream1
```

Substitua `usuário`, `senha`, `192.168.1.100` e `stream1` pelas informações da sua câmera.

## Conclusão

Este projeto é uma introdução simples à integração de câmeras RTSP com interfaces gráficas em Python. Ele pode ser expandido para incluir funcionalidades como **gravação de vídeo**, **detecção de movimento** ou **integração com outras ferramentas de segurança**.
