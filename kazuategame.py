import streamlit as st
import random

st.title("🎯 数当てゲーム")
st.write("1〜100の間の数字を当ててください")

# セッション状態の初期化
if "target" not in st.session_state:
    st.session_state.target = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.message = ""

guess = st.number_input(
    "数字を入力してください",
    min_value=1,
    max_value=100,
    step=1
)

if st.button("判定"):
    st.session_state.attempts += 1

    if guess < st.session_state.target:
        st.session_state.message = "もっと大きい 👆"
    elif guess > st.session_state.target:
        st.session_state.message = "もっと小さい 👇"
    else:
        st.session_state.message = (
            f"🎉 正解！答えは {st.session_state.target} でした！\n"
            f"試行回数：{st.session_state.attempts} 回"
        )

st.write(st.session_state.message)

if st.button("もう一回遊ぶ"):
    st.session_state.target = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.message = ""
