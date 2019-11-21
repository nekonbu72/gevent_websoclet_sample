const btn = document.querySelector(".btn");
btn.addEventListener("click", () => {
  // WebSocket 接続を作成する
  const socket = new WebSocket("ws://localhost:8000/ws");

  // メッセージを待ち受ける
  socket.addEventListener("message", function(event) {
    const p = document.createElement("p");
    p.textContent = event.data;
    const tgt = document.querySelector(".log");
    tgt.appendChild(p);
  });
});
