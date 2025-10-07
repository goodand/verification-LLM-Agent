# Gemini Code Assist 권한 설정 (Permission Settings)

이 문서는 Gemini Code Assist의 역할과 권한을 정의하여 시스템 내에서 안전하고 효율적으로 작동하도록 보장하는 것을 목표로 합니다.

## 핵심 원칙 (Core Principles)

1.  **최소 권한의 원칙 (Principle of Least Privilege):** Gemini Code Assist는 작업을 수행하는 데 필요한 최소한의 권한만 가져야 합니다.
2.  **역할 기반 접근 제어 (Role-Based Access Control - RBAC):** 특정 역할(예: 코드 리뷰어, 개발 보조)에 따라 권한을 부여합니다.
3.  **정기적인 감사 (Regular Audits):** 부여된 권한은 정기적으로 검토하고 필요에 따라 조정해야 합니다.

## 권한 수준 (Permission Levels)

| 수준 (Level) | 이름 (Name) | 설명 (Description) |
| :--- | :--- | :--- |
| 1 | **읽기 전용 (Read-Only)** | 파일 및 코드베이스를 읽을 수만 있고, 수정/생성/삭제는 불가능합니다. |
| 2 | **제안 (Suggest)** | 코드 변경사항을 제안(예: diff 생성)할 수 있지만, 직접 적용할 수는 없습니다. |
| 3 | **쓰기 (Write)** | 파일을 읽고, 수정하고, 생성할 수 있습니다. |
| 4 | **관리자 (Admin)** | 파일 시스템 접근, 권한 변경, 시스템 설정 등 모든 작업을 수행할 수 있습니다. |

## 현재 권한 설정 (Current Permission Configuration)

-   **기본 역할 (Default Role):** 제안 (Suggest) - Level 2
-   **허용된 작업:**
    -   모든 파일 읽기 (`Read`)
    -   새 파일 생성 제안 (`Suggest New File`)
    -   기존 파일 수정 제안 (`Suggest Modification`)
-   **제한된 작업:**
    -   파일 직접 수정 또는 삭제 (`Write`, `Delete`)
    -   시스템 명령어 실행 (`Execute Commands`)
    -   권한 설정 변경 (`Change Permissions`)
