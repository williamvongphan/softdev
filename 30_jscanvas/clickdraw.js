let canvas = document.getElementById("slate");
let ctx = canvas.getContext("2d");

let mode = "rect";

let drawRect = function(e) {
  let x = e.offsetX;
  let y = e.offsetY;
  ctx.fillStyle = "#ff0000";
  ctx.fillRect(x, y, 100, 100);
}

let drawCirc = function(e) {
  let x = e.offsetX;
  let y = e.offsetY;
  ctx.fillStyle = "#0000ff";
  ctx.beginPath();
  ctx.arc(x, y, 50, 0, 2 * Math.PI);
  ctx.fill();
}

let draw = function(e) {
  if (mode == "rect") {
    drawRect(e);
  } else {
    drawCirc(e);
  }
}

let wipeCanvas = function(e) {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}

canvas.addEventListener("click", draw);
let clear = document.getElementById("buttonClear");
clear.addEventListener("click", wipeCanvas);

let toggleMode = function(e) {
  if (mode == "rect") {
    mode = "circ";
    toggle.innerHTML = "Circle";
  } else { 
    mode = "rect";
    toggle.innerHTML = "Rectangle";
  }
  console.log("toggled to " + mode);
}

let toggle = document.getElementById("buttonToggle");
toggle.addEventListener("click", toggleMode);
