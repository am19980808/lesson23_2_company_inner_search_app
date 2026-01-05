import streamlit as st

st.title("社内検索アプリ")

query = st.text_input("検索キーワードを入力してください")

if query:
    st.success(f"「{query}」で検索しました（仮）")
    st.write("※ ここに検索結果が表示されます")

