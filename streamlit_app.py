import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="물리 펭귄 놀이터", layout="centered")

st.title("🐧 물리 엔진 펭귄 놀이터")

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
  body {{
    margin: 0;
    overflow: hidden;
  }}
  #box {{
    position: relative;
    width: 600px;
    height: 400px;
    border: 3px solid #4A90E2;
    background: #E6F7FF;
    overflow: hidden;
  }}
  .penguin {{
    position: absolute;
    width: 60px;
  }}
</style>
</head>
<body>
<div id="box"></div>

<script>
const box = document.getElementById("box");
const boxWidth = 600;
const boxHeight = 400;
const penguins = [];

function createPenguin() {{
    const img = document.createElement("img");
    img.src = "https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif";
    img.className = "penguin";

    let penguin = {{
        el: img,
        x: Math.random() * (boxWidth - 60),
        y: Math.random() * (boxHeight - 60),
        vx: (Math.random() * 4) - 2,
        vy: (Math.random() * 4) - 2,
        size: 60
    }};

    penguins.push(penguin);
    box.appendChild(img);
}}

for (let i = 0; i < {st.session_state.count}; i++) {{
    createPenguin();
}}

function update() {{
    penguins.forEach((p, i) => {{
        p.x += p.vx;
        p.y += p.vy;

        // 벽 충돌
        if (p.x <= 0 || p.x + p.size >= boxWidth) {{
            p.vx *= -1;
        }}
        if (p.y <= 0 || p.y + p.size >= boxHeight) {{
            p.vy *= -1;
        }}

        // 펭귄끼리 충돌
        penguins.forEach((other, j) => {{
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
</script>
</body>
</html>
"""

components.html(html_code, height=450)
