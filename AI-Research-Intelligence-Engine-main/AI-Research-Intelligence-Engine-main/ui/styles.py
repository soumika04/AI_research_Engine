def apply_custom_styles():
    return """
    <style>
    .stApp {
        background: radial-gradient(circle at 20% 20%, #1e3c72, #2a5298, #0f2027);
        color: white;
    }

    .title {
        font-size: 46px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        opacity: 0.8;
        margin-bottom: 30px;
    }

    .glass {
        background: rgba(255,255,255,0.08);
        padding: 25px;
        border-radius: 20px;
        backdrop-filter: blur(15px);
        margin-bottom: 20px;
    }

    .highlight {
        background: linear-gradient(135deg,#00c6ff,#0072ff);
        padding: 30px;
        border-radius: 20px;
        color: white;
    }
    </style>
    """