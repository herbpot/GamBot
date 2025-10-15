# GamBot V1

Slack 봇을 통해 Slack에서 일기를 작성하고 자동으로 Notion에 동기화하는 생산성 도구입니다.

## 개요

GamBot은 Slack과 Notion을 연동하여 일기 작성 워크플로우를 간소화합니다. Slack에서 봇을 멘션하여 일기를 작성하면 자동으로 지정된 Notion 데이터베이스에 저장됩니다.

## 주요 기능

- Slack 메시지를 Notion 데이터베이스에 자동 동기화
- 이미지 첨부 파일 지원
- 사용자별 Notion DB 설정
- 실시간 일기 작성 및 저장

## 기술 스택

### Slack Bot (Python)
- **Python 3.x**
- **slack-bolt** - Slack Bot 프레임워크
- **slack-sdk** - Slack API 클라이언트
- **python-dotenv** - 환경 변수 관리

### Notion Server (TypeScript)
- **Node.js** + **TypeScript**
- **Express.js** - 웹 프레임워크
- **@notionhq/client** - Notion API 클라이언트
- **Mongoose** - MongoDB ODM
- **Nodemon** - 개발 서버

## 프로젝트 구조

```
GamBot/
├── slack/
│   ├── main.py              # Slack 봇 메인 로직
│   ├── schema.py            # 데이터 스키마
│   └── interfaces/
│       └── notion/
│           └── main.py      # Notion 인터페이스
└── servers/
    └── notion/
        ├── index.ts         # Express 서버
        ├── controllers/     # 비즈니스 로직
        ├── routes/          # API 라우트
        └── schema/          # TypeScript 스키마
```

## 설치 및 실행

### 사전 요구사항

- Python 3.x
- Node.js 16+
- Slack Workspace 관리자 권한
- Notion API 키

### 1. 환경 변수 설정

`.env` 파일을 생성하고 다음 항목들을 설정하세요:

```env
SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_SIGNING_SECRET=your-signing-secret
SLACK_APP_TOKEN=xapp-your-app-token
BOT_ID=your-bot-id
NOTION_API_KEY=your-notion-api-key
```

### 2. Slack 봇 실행

```bash
cd slack
pip install slack-bolt slack-sdk python-dotenv
python main.py
```

### 3. Notion 서버 실행

```bash
cd servers/notion
npm install
npm run dev
```

## 사용 방법

### 1. Notion DB 설정

Slack에서 다음 명령어로 Notion 데이터베이스 ID를 등록합니다:

```
/setup-db [your-notion-database-id]
```

### 2. 일기 작성

Slack 채널에서 봇을 멘션하여 일기를 작성합니다:

```
@GamBot 오늘 좋은 하루를 보냈다. 프로젝트가 순조롭게 진행되고 있다.
```

### 3. 이미지 첨부

메시지와 함께 이미지를 첨부하면 Notion에도 함께 저장됩니다.

## Slack Commands

- `/setup-db [database-id]` - Notion 데이터베이스 ID 설정
- `@GamBot [내용]` - 일기 작성 및 Notion에 저장

## Roadmap

- [ ] Markdown 형식 지원
- [ ] 일기 작성 알림 기능
- [ ] 태그 시스템
- [ ] 검색 기능
- [ ] 일기 통계 및 분석

## 개발

### 로그 확인

Slack 봇 로그는 `slack/slackBot.log`에 저장됩니다.

### 개발 모드

Notion 서버는 nodemon을 사용하여 파일 변경 시 자동으로 재시작됩니다.

```bash
npm run dev
```

## 라이선스

MIT License

## 기여

이슈 및 풀 리퀘스트는 언제나 환영합니다!
