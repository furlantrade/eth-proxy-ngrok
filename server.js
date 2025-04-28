const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const ngrok = require('ngrok');
const bodyParser = require('body-parser');

const app = express();
const targetRPC = 'https://eth.public-rpc.com'; // RPC real para onde vamos redirecionar

// Middleware para parsear JSON
app.use(bodyParser.json());

// Proxy
app.use('/', createProxyMiddleware({
  target: targetRPC,
  changeOrigin: true,
  onProxyReq: (proxyReq, req, res) => {
    console.log(`Interceptando chamada: ${req.method} para ${req.originalUrl}`);
  }
}));

const PORT = 8545;

app.listen(PORT, async () => {
  const url = await ngrok.connect({
    addr: PORT,
    proto: 'http',
    authtoken: 'SEU_NGROK_AUTHTOKEN_AQUI', // Coloque seu ngrok authtoken
  });
  console.log(`Proxy RPC Ethereum rodando em http://localhost:${PORT}`);
  console.log(`Ngrok URL: ${url}`);
});
