# Gemini Code Assist 권한 설정 (Permission Settings)

이 문서는 Gemini Code Assist의 역할과 권한을 정의하여 시스템 내에서 안전하고 효율적으로 작동하도록 보장하는 것을 목표로 합니다.

## 핵심 원칙 (Core Principles)

1.  **최소 권한의 원칙 (Principle of Least Privilege):** Gemini Code Assist는 작업을 수행하는 데 필요한 최소한의 권한만 가져야 합니다.
2.  **역할 기반 접근 제어 (Role-Based Access Control - RBAC):** 특정 역할(예: 코드 리뷰어, 개발 보조)에 따라 권한을 부여합니다.
3.  **정기적인 감사 (Regular Audits):** 부여된 권한은 정기적으로 검토하고 필요에 따라 조정해야 합니다.

## 권한 수준 (Permission Levels)

요청에 따라 권한 수준을 더 세분화하고 명확하게 재정의합니다.

| 수준 (Level) | 이름 (Name) | 설명 (Description) |
| :--- | :--- | :--- |
| 1 | **Read-Only (읽기 전용)** | 파일 및 코드베이스를 읽을 수만 있습니다. (수정/생성/삭제 불가) |
| 2 | **Append-Only (추가 전용)** | 기존 파일의 끝에 내용을 추가할 수 있습니다. (수정/삭제 불가) |
| 3 | **Create-Only (생성 전용)** | 새 파일을 생성하고 내용을 작성할 수 있습니다. (기존 파일 수정/삭제 불가) |
| 4 | **Write (쓰기)** | 파일을 읽고, 수정하고, 생성하고, 내용을 추가할 수 있습니다. (삭제 불가) |
| 5 | **Admin (관리자)** | 파일 삭제를 포함한 모든 파일 관련 작업을 수행할 수 있습니다. |

## 파일별 권한 설정 (File-Specific Permissions)

파일 또는 디렉터리 패턴에 따라 개별적으로 권한을 설정할 수 있습니다.

-   **기본 권한 (Default Permission):** `Write` (Level 4)
    -   별도의 규칙이 없는 모든 파일에 적용되는 기본 권한입니다.

### 특별 권한 규칙 (Special Permission Rules)

| 파일 경로/패턴 (File Path/Pattern) | 권한 수준 (Permission Level) | 비고 (Notes) |
| :--- | :--- | :--- |
| `README.md` | `Append-Only` (Level 2) | 프로젝트 요약 정보는 덮어쓰지 않고 추가만 허용합니다. |
| `*.md` | `Write` (Level 4) | 모든 마크다운 파일은 자유롭게 수정할 수 있습니다. |
| `src/core/**` | `Read-Only` (Level 1) | 핵심 로직은 안전을 위해 읽기만 가능하도록 제한합니다. |
| `config.json` | `Admin` (Level 5) | 시스템 설정 파일은 모든 권한을 가집니다. |
| `Gemini-Code-Assist-memory.md` | `Admin` (Level 5) | 이 파일은 제 권한을 정의하므로 최상위 권한을 가집니다. |

**참고:** 규칙은 위에서 아래 순서로 적용되며, 더 구체적인 경로가 일반적인 패턴(`*`)보다 우선합니다.
