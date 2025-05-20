# 🐛 Detecção de Pragas Agrícolas com YOLOv8

Este projeto tem como objetivo identificar pragas agrícolas (como **pulgões**, **lagartas** e **percevejos**) em imagens usando **Visão Computacional com YOLOv8**.

---

## 🔍 O que o projeto faz

- Detecta as seguintes pragas:
  - 🐞 **Pulgão** (`aphid`)
  - 🐛 **Lagarta** (`caterpillar`, `cutworm`, `armyworm`)
  - 🪲 **Percevejo** (`stink_bug`)
- Usa um modelo YOLOv8 treinado localmente com imagens anotadas
- Permite testar o modelo com novas imagens
- Mostra os resultados com nomes das classes traduzidos para português

---

## 🛠 Tecnologias usadas

- [Python]
- [Ultralytics YOLOv8]
- [OpenCV]
- Dataset do [Roboflow Universe]

---

## 🚀 Como usar

### 1. Instale as dependências

```bash
pip install -r requirements.txt
```

### 2. Treine o modelo

```bash
python treino.py
```

### 3. Faça uma predição

```bash
python detectar.py
```

> O script vai abrir a imagem e mostrar o nome da praga detectada (em português), com uma caixa verde ao redor.

---

## 🧠 Dataset

Utilizamos o [Plant Pest Dataset](https://universe.roboflow.com/school-class-wndjm/plant-pest), disponível gratuitamente no Roboflow Universe.

- 🔗 Link: [https://universe.roboflow.com/school-class-wndjm/plant-pest](https://universe.roboflow.com/school-class-wndjm/plant-pest)
- 📜 Licença: **CC BY 4.0** (Creative Commons Attribution 4.0 International)

> ✅ Você pode usar, adaptar, modificar e compartilhar — desde que dê os devidos créditos ao autor.

---

## 📸 Exemplo de resultado

![deteccao](exemplo_resultado.jpg) *(adicione uma imagem gerada pelo seu modelo aqui)*

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT.  
O dataset utilizado está sob a Licença **CC BY 4.0**, conforme fornecido pelo Roboflow.

---

Desenvolvido com ❤️ para fins de aprendizado e prática de Visão Computacional.