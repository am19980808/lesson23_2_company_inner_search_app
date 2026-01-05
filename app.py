import streamlit as st

st.title("社内検索アプリ")

query = st.text_input("検索キーワードを入力してください")

if query:
    st.write(f"「{query}」で検索しました（仮）")
