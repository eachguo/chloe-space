import streamlit as st
import requests

# 网页标题和图标
st.set_page_config(page_title="Chloe's Space", page_icon="🚀")

# 1. 安全地获取您的 API Key (我们将通过 Streamlit 后台设置)
GOOGLE_API_KEY="AIzaSyBKQO_tJ7EiVAQ8Dq3kC0rOXGKe5ko3xRw"

# 2. 侧边栏装饰
with st.sidebar:
    st.markdown("# 🦄 Chloe's Lab")
    st.info("Welcome back, Commander! 欢迎回来，指挥官！")
    subject = st.radio("Choose Mission 选择任务:", ("Math Lab 数学", "French Corner 法语"))

# 3. 聊天界面
st.title("✨🌈 Chloe's Summit Space 🌈✨")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ready for adventure? 准备好开始了吗？"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 老师人设引导
    instruct = f"You are Chloe's funny bilingual teacher. Subject: {subject}. Always use emojis and be encouraging!"
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
    payload = {"contents": [{"parts": [{"text": f"System: {instruct}\nUser: {prompt}"}]}]}
    
    try:
        response = requests.post(url, json=payload)
        ans = response.json()['candidates'][0]['content']['parts'][0]['text']
        with st.chat_message("assistant"):
            st.markdown(ans)
        st.session_state.messages.append({"role": "assistant", "content": ans})
    except:
        st.error("Space Signal Weak! Please try again. 信号微弱，请重试！")
