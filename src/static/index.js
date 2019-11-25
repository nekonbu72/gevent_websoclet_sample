const log = document.querySelector(".log");

const start = document.querySelector(".start");
start.addEventListener("click", () => {
  // WebSocket 接続を作成する
  const socket = new WebSocket("ws://localhost:8000/ws");

  // メッセージを待ち受ける
  socket.addEventListener("message", function(event) {
    const p = document.createElement("p");
    p.textContent = event.data;
    log.appendChild(p);
  });
});

const reset = document.querySelector(".reset");
reset.addEventListener("click", async () => {
  const resp = await fetch("http://localhost:8000/reset");
  const text = await resp.text();
  console.log(text);

  while (log.firstChild) {
    log.removeChild(log.firstChild);
  }
});
