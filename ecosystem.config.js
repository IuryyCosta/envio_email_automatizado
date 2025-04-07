module.exports = {
  apps: [
    {
      name: "envio-email",
      script: "main.py",
      interpreter: "python",
      watch: false,
      env: {
        // Pode passar outras variáveis se quiser, mas o .env já cobre isso
      }
    }
  ]
}
