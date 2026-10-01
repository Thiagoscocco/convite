# Link secreto muito proibido

Projeto simples para enviar um link surpresa.

## Como usar

1. Coloque a imagem inicial em `assets/arte-principal.png`.
   - Também funciona com `arte-principal.jpg`, `arte-principal.jpeg` ou `arte-principal.webp`.
2. Opcionalmente, coloque a imagem de informações em `assets/detalhes.png`.
   - Se esse arquivo não existir, o app renderiza o cartaz de informações direto na página.
3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Rode o app:

```bash
streamlit run app.py
```

## Publicar

Para gerar um link `*.streamlit.app`:

1. Crie um repositório no GitHub da conta correta.
2. Envie este projeto para esse repositório.
3. Acesse `https://share.streamlit.io/`.
4. Clique em **Create app**.
5. Escolha o repositório.
6. Em **Main file path**, use:

```text
app.py
```

7. Publique o app.

O Streamlit vai gerar um link parecido com:

```text
https://nome-do-app-xxxxx.streamlit.app/
```
