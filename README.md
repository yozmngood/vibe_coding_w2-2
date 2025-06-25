# vibe-coding-w2-1-v2

Python 기반 AI 챗봇 프로젝트

## 프로젝트 구조

```
vibe_coding_w2-1.v2/
├── backend/                    # FastAPI 백엔드
│   ├── app/
│   │   ├── agent.py           # LangGraph Agent
│   │   ├── config.py          # 설정
│   │   ├── main.py            # FastAPI 애플리케이션
│   │   ├── models/            # 데이터 모델
│   │   └── routers/           # API 라우터
│   ├── tests/                 # 테스트 코드
│   ├── requirements.txt       # Python 의존성
│   └── run.py                # 실행 스크립트
├── frontend/                  # Streamlit 프론트엔드
│   ├── app.py                # Streamlit 애플리케이션
│   └── requirements.txt      # Python 의존성
├── .github/workflows/        # GitHub Actions
├── .cursor/rules/           # 개발 규칙 및 가이드라인
└── docs/                    # 문서
```

## 기술 스택

- **백엔드**: FastAPI, Python 3.11+
- **프론트엔드**: Streamlit
- **AI**: LangGraph, Gemini-2.5
- **도구**: DuckDuckGo Search
- **패키지 관리**: Poetry

## GitHub 워크플로우

프로젝트에는 다음과 같은 자동화된 GitHub Actions가 설정되어 있습니다:

### 1. 테스트 자동 실행 (`test.yml`)
- **트리거**: Push 및 PR (main 브랜치)
- **기능**: 
  - Python 3.11, 3.12에서 테스트 실행
  - 백엔드 및 프론트엔드 테스트
  - 코드 커버리지 리포트

### 2. PR 관리 자동화

#### PR 자동 댓글 (`pr-comment.yml`)
- **트리거**: PR 생성 시
- **기능**: 환영 메시지와 체크리스트 제공

#### PR 자동 할당 (`pr-assigner.yml`)
- **트리거**: PR 생성 시
- **기능**: 리뷰어 및 담당자 자동 할당

#### PR 자동 라벨링 (`pr-labeler.yml`)
- **트리거**: PR 생성/동기화 시
- **기능**: 제목, 파일 변경사항 기반 자동 라벨링

#### PR 코드 리뷰 (`pr-code-review.yml`)
- **트리거**: PR 생성/동기화 시
- **기능**: 자동 코드 리뷰 체크리스트 제공

### 3. 이슈 관리 자동화

#### 이슈 자동 댓글 (`issue-comment.yml`)
- **트리거**: 이슈 생성 시
- **기능**: 환영 메시지와 처리 절차 안내

#### 이슈 자동 할당 및 라벨링 (`issue-assigner.yml`)
- **트리거**: 이슈 생성 시
- **기능**: 
  - 이슈 내용 기반 담당자 자동 할당
  - 제목/내용 기반 자동 라벨링 (type, priority, area)

## 개발 규칙

프로젝트의 개발 규칙과 가이드라인은 `.cursor/rules/` 디렉토리에서 확인할 수 있습니다:

- `github-management.mdc`: GitHub PR 및 이슈 관리 규칙
- `development-policy.mdc`: 개발 정책 및 원칙
- `tech-stack.mdc`: 기술 스택 정보
- `project-structure.mdc`: 프로젝트 구조 설명

### PR 규칙

1. **브랜치 네이밍**:
   - `feature/기능명`: 새로운 기능
   - `fix/버그명`: 버그 수정
   - `refactor/리팩토링명`: 코드 리팩토링
   - `docs/문서명`: 문서 업데이트

2. **PR 제목**: `[타입] 간단한 설명`
   - 예: `[feat] 채팅 기능 구현`, `[fix] 로그인 오류 수정`

3. **검토 프로세스**: 최소 1명의 승인 필요

### 이슈 규칙

1. **이슈 제목**: `[타입] 간단한 설명`
   - 예: `[bug] 로그인 시 오류 발생`, `[feat] 새로운 기능 요청`

2. **라벨 분류**:
   - 타입: `type/bug`, `type/feature`, `type/enhancement`
   - 우선순위: `priority/high`, `priority/medium`, `priority/low`
   - 영역: `area/backend`, `area/frontend`, `area/tests`

## 개발 시작하기

1. **저장소 클론**:
   ```bash
   git clone <repository-url>
   cd vibe_coding_w2-1.v2
   ```

2. **백엔드 설정**:
   ```bash
   cd backend
   poetry install
   poetry run python run.py
   ```

3. **프론트엔드 설정**:
   ```bash
   cd frontend
   pip install -r requirements.txt
   streamlit run app.py
   ```

4. **환경 변수 설정**:
   - `.env` 파일 생성
   - `LANGSMITH_API_KEY` 설정
   - `GEMINI_API_KEY` 설정

## 테스트 실행

```bash
# 백엔드 테스트
cd backend
poetry run pytest tests/ -v

# 프론트엔드 테스트
cd frontend
python -m pytest -v
```

## 기여하기

1. 이슈를 생성하거나 기존 이슈를 선택합니다
2. 적절한 브랜치를 생성합니다
3. 변경사항을 구현합니다
4. 테스트를 작성하고 실행합니다
5. PR을 생성합니다

자세한 개발 가이드라인은 `.cursor/rules/` 디렉토리의 문서들을 참고해주세요.