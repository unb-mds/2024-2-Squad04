---

# Introdução ao Socket.IO

Socket.IO é uma biblioteca que permite a comunicação bidirecional em tempo real entre clientes e servidores, baseada em WebSockets, mas também oferecendo suporte a outras tecnologias para garantir a compatibilidade máxima. [Veja a documentação](https://socket.io/pt-br/docs/v4/).

## Funcionamento Básico

1. **Estabelecimento de Conexão**:
   - O cliente inicia a conexão com o servidor Socket.IO.
   - O Socket.IO tenta primeiramente usar WebSocket. Se não for possível, ele faz fallback para outras opções, como polling.

2. **Emissão e Recebimento de Eventos**:
   - **Emit**: Tanto o cliente quanto o servidor podem enviar mensagens ou dados entre si usando `emit`.
   - **On**: Para lidar com eventos recebidos, ambos os lados usam o método `on` para ouvir eventos específicos.

3. **Rooms e Namespaces**:
   - **Namespaces**: Permitem que um servidor organize diferentes canais de comunicação para gerenciar diferentes funcionalidades (por exemplo, `/chat`, `/game`).
   - **Rooms**: Permitem organizar os clientes em grupos, facilitando a comunicação com um subconjunto de clientes conectados.

4. **Fluxo Básico de Mensagens**:
   - Um cliente emite uma mensagem usando `socket.emit("evento", dados)`.
   - O servidor escuta a mensagem com `socket.on("evento", (dados) => { ... })`.
   - O servidor pode responder ou retransmitir a mensagem para outros clientes, criando um fluxo de comunicação interativo.

## Exemplo de Código

### Servidor (Node.js)

```javascript
const io = require('socket.io')(3000);

io.on('connection', (socket) => {
    console.log('Cliente conectado:', socket.id);

    socket.on('mensagem', (data) => {
        console.log('Mensagem recebida:', data);
        socket.emit('resposta', 'Mensagem recebida com sucesso!');
    });
});
```

--- 