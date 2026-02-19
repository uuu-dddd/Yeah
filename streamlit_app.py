import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="지속 물리 펭귄", layout="centered")

st.title("🐧 계속 움직이는 펭귄 놀이터")

if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("🐧 펭귄 추가"):
    st.session_state.count += 1

st.write(f"현재 펭귄 수: {st.session_state.count}")

html_code = f"""
<!DOCTYPE html>
<html>
<head>
<style>
  body {{ margin:0; overflow:hidden; }}
  #box {{
    position: relative;
    width: 650px;
    height: 420px;
    border-radius: 20px;
    border: 4px solid #4A90E2;
    background: linear-gradient(to bottom, #DFF3FF, #FFFFFF);
    overflow: hidden;
  }}
  .penguin {{
    position: absolute;
    width: 50px;
  }}
</style>
</head>
<body>
<div id="box"></div>

<script>
const box = document.getElementById("box");
const boxWidth = 650;
const boxHeight = 420;

// 🔥 이미 존재하면 유지
if (!window.penguins) {{
    window.penguins = [];
}}

if (!window.animationStarted) {{
    window.animationStarted = true;

    function update() {{
        window.penguins.forEach((p, i) => {{
            p.x += p.vx;
            p.y += p.vy;

            if (p.x <= 0 || p.x + p.size >= boxWidth) p.vx *= -1;
            if (p.y <= 0 || p.y + p.size >= boxHeight) p.vy *= -1;

            window.penguins.forEach((other, j) => {{
                if (i !== j) {{
                    let dx = p.x - other.x;
                    let dy = p.y - other.y;
                    let dist = Math.sqrt(dx*dx + dy*dy);
                    if (dist < p.size) {{
                        p.vx *= -1;
                        p.vy *= -1;
                    }}
                }}
            }});

            p.el.style.left = p.x + "px";
            p.el.style.top = p.y + "px";
        }});

        requestAnimationFrame(update);
    }}

    update();
}}

// 🐧 귀여운 SVG
const penguinSVG = `
<svg viewBox="0 0 100 120" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="50" cy="65" rx="35" ry="45" fill="#222"/>
  <ellipse cx="50" cy="75" rx="22" ry="30" fill="white"/>
  <circle cx="40" cy="40" r="6" fill="white"/>
  <circle cx="60" cy="40" r="6" fill="white"/>
  <circle cx="40" cy="40" r="3" fill="black"/>
  <circle cx="60" cy="40" r="3" fill="black"/>
  <polygon points="50,50 45,60 55,60" fill="orange"/>
  <ellipse cx="30" cy="110" rx="10" ry="5" fill="orange"/>
  <ellipse cx="70" cy="110" rx="10" ry="5" fill="orange"/>
</svg>
`;

// 🔥 현재 펭귄 수만큼 부족한 수만 추가
let currentCount = window.penguins.length;
let targetCount = {st.session_state.count};

for (let i = currentCount; i < targetCount; i++) {{
    const div = document.createElement("div");
    div.className = "penguin";
    div.innerHTML = penguinSVG;

    let penguin = {{
        el: div,
        x: Math.random() * (boxWidth - 50),
        y: Math.random() * (boxHeight - 50),
        vx: (Math.random() * 4) - 2,
        vy: (Math.random() * 4) - 2,
        size: 50
    }};

    window.penguins.push(penguin);
    box.appendChild(div);
}}
</script>
</body>
</html>
"""

components.html(html_code, height=470)
