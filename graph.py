# app/graph.py

import os
from dotenv import load_dotenv

# LangChain/LangGraph의 핵심 모듈
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages

# --- 환경 변수 로드 강화 ---
# 현재 파일(graph.py)의 절대 경로를 기준으로 .env 파일의 경로를 계산합니다.
# 이렇게 하면 어떤 위치에서 스크립트를 실행하더라도 항상 정확한 .env 파일을 찾을 수 있습니다.
project_root = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(project_root, '.env')

load_dotenv(dotenv_path=dotenv_path)

# 1. (옵션) Graph State 정의 (create_react_agent가 내부적으로 State를 사용하므로 여기서는 필수 아님)
class AgentState(TypedDict):
    """ReAct 에이전트 상태. messages는 필수입니다."""
    messages: Annotated[list[BaseMessage], add_messages]

# 2. Tool 함수 정의 (스크린샷 4번 섹션에서 가져옴)
# 이 함수는 에이전트가 사용할 도구입니다.
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    # 실제 API 호출 대신 더미 응답을 반환
    return f"It's always sunny in {city}!"

# 3. 그래프 빌드 함수 정의 (langgraph.json에서 참조할 단일 함수)
def get_minimal_graph():
    """
    OpenAI LLM과 get_weather 도구를 사용하는 ReAct 에이전트를 생성합니다.
    """
    # --- 1. Fail-Fast: 필수 환경 변수 검증 ---
    # langgraph dev 서버가 시작될 때 키가 없으면 즉시 에러를 발생시켜 원인을 명확히 합니다.
    print("--- 환경 변수 검증 시작 ---")
    required_keys = ["OPENAI_API_KEY", "LANGSMITH_API_KEY"]
    for key in required_keys:
        if not os.getenv(key):
            # 키가 없으면 서버 로그에 명확한 에러를 남기고 실행을 중단합니다.
            raise ValueError(f"CRITICAL: Missing required environment variable '{key}'. Server cannot start.")
    print("✅ 모든 필수 환경 변수가 성공적으로 로드되었습니다.")

    # --- 2. LLM 객체 명시적 생성 ---
    # 모델을 명시적으로 초기화하면 temperature, model_kwargs 등 추가 옵션 설정이 용이하며
    # 코드가 더 명확해집니다.
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    # --- 3. 에이전트 생성 ---
    agent = create_react_agent(
        model=llm,                   # 생성된 LLM 객체를 전달
        tools=[get_weather],         # 정의한 도구 목록
        prompt="You are a helpful assistant who uses the provided tool to answer questions about the weather.", 
    )
    
    # create_react_agent는 이미 컴파일된 그래프 객체(Runnable)를 반환합니다.
    return agent