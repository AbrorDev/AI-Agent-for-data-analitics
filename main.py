import streamlit as st
from io import BytesIO
import os
from ai_agent import rag_agent
from langchain_core.messages import HumanMessage

def query_to_excel(query):
    result = rag_agent.invoke({"messages": [HumanMessage(content=query)]})
    if "outbox" in result and result["outbox"]:
        file_path = result["outbox"][-1]["path"]
        if os.path.exists(file_path):
            return file_path
    return None

st.title("AI Agent")

query = st.text_input("Savolingizni yozing:")

if st.button("Javobni olish"):
    if not query.strip():
        st.error("Savol yozing")
    else:
        filepath = query_to_excel(query)

        if filepath and os.path.exists(filepath):
            with open(filepath, "rb") as f:
                excel_bytes = f.read()

            st.success("Excel tayyor!")
            st.download_button(
                label="📥 Excelni yuklab olish",
                data=excel_bytes,
                file_name=os.path.basename(filepath),
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        else:
            st.error("Excel fayl topilmadi!")