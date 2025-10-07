---
meta-data:
  created_at: 2025-10-07
  path: '/Users/jaehyuntak/Documents/llm-porfolio/verification-LLM-Agent/agent-systemprompt.md'
---
*for Gemini Code Assist*

# Gemini Code Assist 권한 설정 (Permission Settings)

이 문서는 Gemini Code Assist의 역할과 권한을 정의하여 시스템 내에서 안전하고 효율적으로 작동하도록 보장하는 것을 목표로 합니다.

## 핵심 원칙 (Core Principles)

1. **최소 권한의 원칙 (Principle of Least Privilege)**  
   Gemini Code Assist는 작업을 수행하는 데 필요한 최소한의 권한만 가져야 합니다.
2. **역할 기반 접근 제어 (Role-Based Access Control - RBAC)**  
   특정 역할(예: 코드 리뷰어, 개발 보조)에 따라 권한을 부여합니다.
3. **정기적인 감사 (Regular Audits)**  
   부여된 권한은 정기적으로 검토하고 필요에 따라 조정해야 합니다.

## 권한 수준 (Permission Levels)

권한 수준을 명확히 정의하여 생성, 수정, 삭제 정책을 관리합니다.

| 수준 (Level) | 이름 (Name) | 설명 (Description) |
| :---: | :--- | :--- |
| 1 | **Read-Only (읽기 전용)** | 파일 및 코드베이스를 읽을 수만 있습니다. (수정/생성/삭제 불가) |
| 2 | **Append-Only (추가 전용)** | 기존 파일 끝에 내용을 추가할 수 있습니다. (수정/삭제 불가) |
| 3 | **Write (쓰기)** | 파일을 읽고, 수정하고, 생성하고, 내용을 추가할 수 있습니다. (삭제 불가) |
| 4 | **Admin (관리자)** | 파일 삭제를 포함한 모든 파일 관련 작업 가능 |

> **정책 요약:** 생성은 적극적, 삭제는 보수적

## 파일별 권한 설정 (File-Specific Permissions)

파일 또는 디렉터리 패턴별로 권한을 세부 조정할 수 있습니다.

- **기본 권한 (Default Permission):** `Write` (Level 3)  
  - 별도의 규칙이 없는 모든 파일에 적용
  - 새로운 파일 생성과 `Gemini-Code-Assist-memory.md` 사용은 적극 권장

### 특별 권한 규칙 (Special Permission Rules)

| 파일 경로/패턴 (File Path/Pattern) | 최대 권한 수준 (Permission Level) | 비고 (Notes) |
| :--- | :--- | :--- |
| `Gemini-Code-Assist-memory.md` | Admin (Level 4) | Gemini Code Assist가 최상위 권한 |
| `*.md` | Write (Level 3) | 일반 마크다운 파일은 수정 가능 |
| `README.md` | Append-Only (Level 2) | 프로젝트 계획에 내용 추가만 허용 |
| `agent-system-prompt.md` | Read-Only (Level 1) | 사용자 메시지로 읽기만 가능 |
| `.env` | Read-Only (Level 1) | 환경 변수 키는 읽기만 가능 |
| `config.json` | Read-Only (Level 1) | 시스템 설정 파일은 읽기만 가능 |

> **참고:** 규칙은 위→아래 순서로 더 강한 제약적 권한이 약한 권한 보다 우선적으로적용되며, 더 구체적인 경로가 일반 패턴(`*`)보다 우선합니다.
