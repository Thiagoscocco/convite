from pathlib import Path
import base64

import streamlit as st
import streamlit.components.v1 as components


APP_DIR = Path(__file__).parent
ASSETS_DIR = APP_DIR / "assets"
IMAGE_CANDIDATES = [
    ASSETS_DIR / "arte-principal.png",
    ASSETS_DIR / "arte-principal.jpg",
    ASSETS_DIR / "arte-principal.jpeg",
    ASSETS_DIR / "arte-principal.webp",
]
INFO_IMAGE_CANDIDATES = [
    ASSETS_DIR / "detalhes.png",
    ASSETS_DIR / "detalhes.jpg",
    ASSETS_DIR / "detalhes.jpeg",
    ASSETS_DIR / "detalhes.webp",
]


def find_first_existing(paths: list[Path]) -> Path | None:
    for image_path in paths:
        if image_path.exists():
            return image_path
    return None


def image_data_uri(image_path: Path) -> str:
    mime_by_suffix = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }
    mime_type = mime_by_suffix.get(image_path.suffix.lower(), "image/png")
    encoded = base64.b64encode(image_path.read_bytes()).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"


st.set_page_config(
    page_title="Link secreto muito proibido",
    page_icon=":sparkles:",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        :root {
            --bg: #edf4f1;
            --panel: #ffffff;
            --text: #17231f;
            --muted: #5f6d68;
            --green: #00bf63;
            --green-dark: #00984f;
            --shadow: 0 18px 48px rgba(14, 38, 29, 0.16);
        }

        .stApp {
            background:
                radial-gradient(circle at 18% 10%, rgba(0, 191, 99, 0.14), transparent 28%),
                radial-gradient(circle at 88% 88%, rgba(182, 205, 91, 0.28), transparent 26%),
                var(--bg);
        }

        header, footer, [data-testid="stToolbar"], [data-testid="stDecoration"] {
            display: none;
        }

        .block-container {
            max-width: 560px;
            min-height: calc(100vh - 46px);
            padding: 18px 16px 28px;
        }

        .invite-topline {
            color: var(--muted);
            font-size: 0.92rem;
            font-weight: 700;
            letter-spacing: 0;
            text-align: center;
            text-transform: uppercase;
        }

        .invite-image-wrap {
            background: var(--panel);
            border: 1px solid rgba(23, 35, 31, 0.08);
            border-radius: 8px;
            box-shadow: var(--shadow);
            padding: 8px;
        }

        .invite-image {
            display: block;
            width: 100%;
            max-height: 74vh;
            object-fit: contain;
            border-radius: 6px;
        }

        .info-poster {
            align-items: center;
            aspect-ratio: 464 / 624;
            background: #c4ced7;
            border-radius: 8px;
            box-shadow: var(--shadow);
            color: var(--green);
            display: flex;
            flex-direction: column;
            font-weight: 900;
            justify-content: center;
            margin-top: 12px;
            overflow: hidden;
            padding: clamp(18px, 5vw, 38px) clamp(14px, 5vw, 34px);
            text-align: center;
            width: 100%;
        }

        .info-poster-title {
            color: #ff6b1a;
            font-size: clamp(1.9rem, 9vw, 3.1rem);
            line-height: 1.02;
            margin: 0 0 clamp(8px, 2.6vw, 18px);
            text-transform: uppercase;
        }

        .info-poster-line {
            font-size: clamp(1.55rem, 7vw, 2.5rem);
            line-height: 1.2;
            margin: 0 0 clamp(7px, 2.2vw, 18px);
        }

        .info-poster-gap {
            height: clamp(22px, 7vw, 52px);
        }

        .missing-image {
            background: var(--panel);
            border: 1px dashed rgba(0, 191, 99, 0.48);
            border-radius: 8px;
            box-shadow: var(--shadow);
            padding: 28px 18px;
            text-align: center;
        }

        .missing-image strong {
            color: var(--green-dark);
            display: block;
            font-size: 1.2rem;
            margin-bottom: 8px;
        }

        .missing-image span {
            color: var(--muted);
            display: block;
            font-size: 0.98rem;
            line-height: 1.45;
        }

        div[data-testid="stButton"] > button {
            background: linear-gradient(180deg, var(--green), var(--green-dark));
            border: 0;
            border-radius: 8px;
            box-shadow: 0 14px 28px rgba(0, 152, 79, 0.28);
            color: #ffffff;
            font-size: 1.16rem;
            font-weight: 800;
            min-height: 58px;
            width: 100%;
        }

        div[data-testid="stButton"] > button:hover {
            background: linear-gradient(180deg, #12cc72, var(--green-dark));
            border: 0;
            color: #ffffff;
            transform: translateY(-1px);
        }

        div[data-testid="stButton"] > button:active {
            transform: translateY(1px);
        }

        .next-step,
        .accepted-box {
            background: rgba(255, 255, 255, 0.84);
            border: 1px solid rgba(23, 35, 31, 0.08);
            border-radius: 8px;
            color: var(--text);
            line-height: 1.45;
            padding: 14px 16px;
            text-align: center;
        }

        .accepted-box {
            font-size: 1.55rem;
            font-weight: 900;
            margin-top: 14px;
        }

        @media (max-width: 420px) {
            .block-container {
                padding: 12px 10px 22px;
            }

            .invite-image-wrap {
                padding: 6px;
            }

            .invite-image,
            .info-image {
                max-height: 72vh;
            }

            div[data-testid="stButton"] > button {
                font-size: 1.08rem;
                min-height: 56px;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

image_path = find_first_existing(IMAGE_CANDIDATES)
info_image_path = find_first_existing(INFO_IMAGE_CANDIDATES)

st.markdown('<div class="invite-topline">Link secreto muito proibido</div>', unsafe_allow_html=True)

if image_path:
    st.markdown(
        f"""
        <div class="invite-image-wrap">
            <img class="invite-image" src="{image_data_uri(image_path)}" alt="Mensagem principal">
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <div class="missing-image">
            <strong>Imagem ainda não encontrada</strong>
            <span>Coloque a arte principal em <code>assets/arte-principal.png</code> para ela aparecer grande aqui.</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

if st.button("Mais Informações", type="primary", use_container_width=True):
    st.session_state.show_next_step = True

if st.session_state.get("show_next_step"):
    if info_image_path:
        st.markdown(
            f"""
            <div class="invite-image-wrap">
                <img class="invite-image info-image" src="{image_data_uri(info_image_path)}" alt="Mais informações">
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <section class="info-poster" aria-label="Mais informações">
                <h1 class="info-poster-title">Informações:</h1>
                <p class="info-poster-line">Sábado</p>
                <p class="info-poster-line">Das 16h às 21h</p>
                <p class="info-poster-line">Local não revelado</p>
                <div class="info-poster-gap"></div>
                <h2 class="info-poster-title">Pré requisitos:</h2>
                <p class="info-poster-line">Tomar banho</p>
                <p class="info-poster-line">Estar Linda</p>
                <p class="info-poster-line">Estar cheirosa</p>
                <p class="info-poster-line">Não estar braba</p>
            </section>
            """,
            unsafe_allow_html=True,
        )

    components.html(
        """
        <style>
            :root {
                --green: #00bf63;
                --green-dark: #00984f;
                --orange: #ff6b1a;
                --text: #17231f;
            }

            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                overflow: hidden;
                font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            }

            .decision-area {
                height: 230px;
                padding-top: 18px;
                position: relative;
                width: 100%;
            }

            .accept-button,
            .decline-button {
                border: 0;
                border-radius: 8px;
                color: #ffffff;
                cursor: pointer;
                font-size: 1.08rem;
                font-weight: 900;
                min-height: 56px;
                padding: 0 24px;
                position: absolute;
                transition: left 190ms ease, top 190ms ease, transform 130ms ease;
                width: min(46%, 210px);
            }

            .accept-button {
                background: linear-gradient(180deg, var(--green), var(--green-dark));
                box-shadow: 0 12px 24px rgba(0, 152, 79, 0.25);
                left: 0;
                top: 18px;
            }

            .decline-button {
                background: linear-gradient(180deg, #ff7f32, var(--orange));
                box-shadow: 0 12px 24px rgba(255, 107, 26, 0.25);
                left: 54%;
                top: 18px;
            }

            .accept-button:active,
            .decline-button:active {
                transform: scale(0.97);
            }

            .answer {
                align-items: center;
                background: rgba(255, 255, 255, 0.9);
                border: 1px solid rgba(23, 35, 31, 0.08);
                border-radius: 8px;
                color: var(--text);
                display: none;
                font-size: 1.7rem;
                font-weight: 900;
                gap: 8px;
                justify-content: center;
                margin-top: 18px;
                min-height: 74px;
                text-align: center;
            }

            .answer.is-visible {
                display: flex;
            }

            @media (max-width: 420px) {
                .decision-area {
                    height: 250px;
                }

                .accept-button,
                .decline-button {
                    font-size: 1rem;
                    min-height: 54px;
                    padding: 0 14px;
                    width: 46%;
                }
            }
        </style>

        <div class="decision-area" id="decision-area">
            <button class="accept-button" id="accept-button" type="button">Aceitar</button>
            <button class="decline-button" id="decline-button" type="button">Recusar</button>
            <div class="answer" id="answer">Combinado 😎</div>
        </div>

        <script>
            const acceptButton = document.getElementById("accept-button");
            const declineButton = document.getElementById("decline-button");
            const answer = document.getElementById("answer");

            const positions = [
                { left: 54, top: 18 },
                { left: 6, top: 96 },
                { left: 51, top: 150 },
                { left: 28, top: 142 },
                { left: 2, top: 164 },
                { left: 48, top: 88 },
                { left: 24, top: 70 },
            ];

            let currentPosition = 0;

            function moveDeclineButton() {
                currentPosition = (currentPosition + 1 + Math.floor(Math.random() * 3)) % positions.length;
                const nextPosition = positions[currentPosition];
                declineButton.style.left = `${nextPosition.left}%`;
                declineButton.style.top = `${nextPosition.top}px`;
            }

            acceptButton.addEventListener("click", () => {
                acceptButton.style.display = "none";
                declineButton.style.display = "none";
                answer.classList.add("is-visible");
            });

            declineButton.addEventListener("click", moveDeclineButton);
            declineButton.addEventListener("mouseenter", () => {
                if (window.matchMedia("(hover: hover)").matches) {
                    moveDeclineButton();
                }
            });
        </script>
        """,
        height=260,
    )
