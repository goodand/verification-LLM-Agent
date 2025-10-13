import os
from dotenv import load_dotenv

# .env 파일 로드를 시도합니다.
# load_dotenv()는 .env 파일을 찾으면 True, 못 찾으면 False를 반환합니다.
found_dotenv = load_dotenv()

# 환경 변수를 가져옵니다.
api_key = os.getenv("LANGSMITH_API_KEY")
tracing_v2 = os.getenv("LANGSMITH_TRACING_V2")

print(f".env 파일을 찾았나요?: {found_dotenv}")
print("-" * 30)
print(f"LANGSMITH_API_KEY: {api_key}")
print(f"LANGSMITH_TRACING_V2: {tracing_v2}")
print("-" * 30)

if api_key:
    print("✅ 성공: LangSmith API 키를 환경 변수에서 찾았습니다.")
else:
    print("❌ 실패: LangSmith API 키를 찾을 수 없습니다.")
    print("    - .env 파일이 이 스크립트와 같은 폴더에 있는지 확인해주세요.")
    print("    - .env 파일 안에 LANGSMITH_API_KEY='ls__...' 형식으로 키가 올바르게 입력되었는지 확인해주세요.")

