const char *HTML_CONTENT = R""""(
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>OLED Logos</title>
  <style>
    :root {
      color-scheme: dark;
      --bg1: #0f172a;
      --bg2: #1d4ed8;
      --card: rgba(15, 23, 42, 0.78);
      --text: #f8fafc;
      --accent: #38bdf8;
      --accent2: #f97316;
    }

    * { box-sizing: border-box; }

    html, body {
      margin: 0;
      min-height: 100%;
      font-family: Arial, Helvetica, sans-serif;
      color: var(--text);
      background: radial-gradient(circle at top, #2563eb 0%, var(--bg1) 55%, #020617 100%);
    }

    body {
      display: grid;
      place-items: center;
      padding: 24px;
    }

    .panel {
      width: min(100%, 360px);
      padding: 28px 22px;
      border-radius: 24px;
      background: var(--card);
      border: 1px solid rgba(148, 163, 184, 0.22);
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.35);
      text-align: center;
      backdrop-filter: blur(10px);
    }

    h1 {
      margin: 0 0 10px;
      font-size: 1.5rem;
    }

    p {
      margin: 0 0 24px;
      color: #cbd5e1;
      line-height: 1.4;
    }

    .buttons {
      display: grid;
      gap: 14px;
    }

    .button {
      display: inline-block;
      width: 100%;
      border: 0;
      border-radius: 16px;
      padding: 16px 18px;
      font-size: 1rem;
      font-weight: 700;
      letter-spacing: 0.04em;
      cursor: pointer;
      color: white;
      transition: transform 0.15s ease, filter 0.15s ease;
    }

    .button:active {
      transform: scale(0.98);
    }

    .gears {
      background: linear-gradient(135deg, var(--accent) 0%, #2563eb 100%);
    }

    .halo {
      background: linear-gradient(135deg, var(--accent2) 0%, #f59e0b 100%);
    }

    .status {
      margin-top: 18px;
      font-size: 0.95rem;
      color: #94a3b8;
      min-height: 1.2em;
    }
  </style>
</head>
<body>
  <main class="panel">
    <h1>OLED Logos</h1>
    <p>Selecciona un logo para mostrarlo en la pantalla OLED.</p>

    <div class="buttons">
      <button class="button gears" onclick="sendLogo('/gears')">GEARS</button>
      <button class="button halo" onclick="sendLogo('/halo')">HALO</button>
    </div>

    <div id="status" class="status">Listo</div>
  </main>

  <script>
    function sendLogo(path) {
      fetch(path)
        .then(function () {
          document.getElementById('status').innerText = 'Enviado: ' + path.replace('/', '').toUpperCase();
        })
        .catch(function () {
          document.getElementById('status').innerText = 'Error al enviar la orden';
        });
    }
  </script>
</body>
</html>
)"""";