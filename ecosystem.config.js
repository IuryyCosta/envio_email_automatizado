// ecosystem.config.js
module.exports = {
    apps: [
      {
        name: "envio-email",
        script: "main.py",
        interpreter: "python",  // <- multiplataforma!
        watch: false,
        env: {
          EXECUTION_HOUR: 8,
          EXECUTION_MINUTE: 30
        }
      }
    ]
  };