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

from typing import TypedDict, Callable
from langgraph.graph import StateGraph, END

# 1. 최소 State 정의 (messages 리스트 대신 단일 str)
class MinimalState(TypedDict):
    """그래프에서 공유될 최소 데이터 구조"""
    input_text: str

# 2. 최소 Node 함수 정의 (1개)
def initial_process_node(state: MinimalState) -> MinimalState:
    """
    input_text를 받아 간단히 처리하는 노드. 
    LangGraph는 이 반환값을 기존 State와 병합합니다.
    """
    # 실제 작업 수행: 입력 텍스트를 대문자로 변경
    processed_text = state["input_text"].upper()
    print(f"Node Executed. Input: {state['input_text']}, Output: {processed_text}")
    
    # State의 내용을 업데이트하여 반환
    return {"input_text": processed_text} 

# 3. 최소 Graph 빌드 및 실행
def run_minimal_graph():
    # StateGraph 초기화
    graph = StateGraph(MinimalState) 
    
    # 노드 추가
    graph.add_node("process_node", initial_process_node) 
    
    # 시작점 설정 (START 대신 사용)
    graph.set_entry_point("process_node") 
    
    # 엣지 추가 (노드 실행 후 바로 END로 이동)
    graph.add_edge("process_node", END) 
    
    # 컴파일
    app = graph.compile()
    
    # --- 실행 ---
    initial_input = {"input_text": "hello langgraph minimal"}
    print(f"\n--- LangGraph 실행 시작 ---")
    result = app.invoke(initial_input)
    
    print(f"--- 최종 결과 ---")
    print(result)

# run_minimal_graph()

# (https://g.co/gemini/share/742a9027e017)