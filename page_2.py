import streamlit as st # streamlit 라이브러리 임포트
from langchain.chat_models import init_chat_model # chat model initialize
from dotenv import load_dotenv #API key를 환경변수로 불러오기 위한 라이브러리
from langchain.tools import tool #tool 데코레이터 임포트
from langchain.agents import create_agent   # 에이전트 생성
from langchain.messages import HumanMessage, AIMessage, SystemMessage   # 메시지 객체 생성
from langchain_tavily import TavilySearch

load_dotenv()

model = init_chat_model("gpt-5.4-mini") # 모델 객체 생성

@tool
def get_weather(location : str) -> str :
  "특정 지역의 날씨 정보 반환"
  return f"{location} 날씨가 맑습니다"

tavily_tool = TavilySearch(
    max_results=5,
    topic="general",
    # include_answer=False,
    # include_raw_content=False,
    # include_images=False,
    # include_image_descriptions=False,
    # search_depth="basic",
    # time_range="day",
    # include_domains=None,
    # exclude_domains=None
)

agent = create_agent(model, tools = [get_weather, tavily_tool]) # agent 객체 생성

st.title("Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

messages = st.session_state.messages

prompt = st.chat_input("Say something")
if prompt:
    response = model.invoke(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "ai", "content": response.content})

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])


