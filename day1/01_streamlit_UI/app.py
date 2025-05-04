import streamlit as st
import pandas as pd
import numpy as np


# ------------------------
# カスタムスタイル
# ------------------------
st.markdown("""
<style>
h1 {
    color: #4F8BF9;
}
.block {
    background-color: #f5f5f5;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ------------------------
# タイトル
# ------------------------
st.title("✨ Streamlit デモ")

# ------------------------
# 名前入力 & ボタン
# ------------------------
with st.container():
    st.markdown('<div class="block">', unsafe_allow_html=True)
    name = st.text_input("お名前を入力してください", "ゲスト")
    st.write(f"こんにちは、{name}さん！")
    if st.button("挨拶する"):
        st.success("ようこそ Streamlit へ！")
    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------
# スライダー & セレクトボックス
# ------------------------
with st.container():
    st.markdown('<div class="block">', unsafe_allow_html=True)
    age = st.slider("年齢を選択", 0, 100, 25)
    lang = st.selectbox("好きな言語は？", ["Python", "JavaScript", "C++"])
    st.write(f"年齢: {age}歳, 選択言語: {lang}")
    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------
# 表示用データ
# ------------------------
with st.container():
    st.markdown('<div class="block">', unsafe_allow_html=True)
    df = pd.DataFrame({
        "名前": ["田中", "佐藤", "鈴木"],
        "年齢": [24, 30, 28]
    })
    st.dataframe(df, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------
# グラフ
# ------------------------
with st.container():
    st.markdown('<div class="block">', unsafe_allow_html=True)
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
    st.line_chart(chart_data)
    st.markdown('</div>', unsafe_allow_html=True)
