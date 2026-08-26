# manwookhan95.github.io

Manwook Han 개인 학술 홈페이지. 정적 HTML만 사용하며 빌드 과정이 없습니다.

---

## 1. GitHub Pages 배포

GitHub 계정이 필요합니다. 계정 생성은 직접 하셔야 합니다 (제가 대신 만들 수 없습니다).

1. GitHub에 로그인 → 새 repository 생성
2. repository 이름을 **정확히** `<사용자명>.github.io` 로 지정
   - 예: 사용자명이 `manwookhan` 이면 repository 이름은 `manwookhan95.github.io`
   - 이 이름이어야 `https://<사용자명>.github.io` 최상위 주소가 나옵니다
3. Public 으로 설정, README 자동 생성은 체크 해제
4. 이 폴더의 파일 전부를 repository 최상단에 업로드
   - 웹 UI: `Add file` → `Upload files` → 드래그
   - `.nojekyll` 는 숨김 파일이라 Finder에서 `Cmd+Shift+.` 로 표시한 뒤 함께 올리세요
5. `Settings` → `Pages` → Source를 `Deploy from a branch`, branch를 `main` / `/ (root)` 로 지정
6. 1~2분 뒤 `https://<사용자명>.github.io` 접속 확인

### 사용자명이 `manwookhan` 이 아닌 경우

`sitemap.xml`, `robots.txt`, 그리고 각 HTML 파일의 `<link rel="canonical">`, `og:url` 에 주소가
하드코딩되어 있습니다. 폴더에서 아래 명령을 한 번 실행하세요.

```bash
grep -rl 'manwookhan95.github.io' . | xargs sed -i '' 's|manwookhan\.github\.io|실제사용자명.github.io|g'
```

(Linux면 `sed -i ''` 대신 `sed -i`)

---

## 2. Search Console 재설정

기존 `sites.google.com/view/manwookhan/` 속성은 그대로 두고 **새 속성을 추가**하세요.

1. Search Console → 속성 추가 → **URL 접두어** → `https://<사용자명>.github.io/`
2. 소유권 확인: `HTML 파일` 방식 선택 → 받은 `google<문자열>.html` 을 이 폴더 최상단에 넣고 push → 확인
3. `Sitemaps` → `sitemap.xml` 입력 → 제출
4. `URL 검사` → 홈 URL → `색인 생성 요청`
5. 나머지 6개 페이지도 각각 URL 검사 → 색인 생성 요청

며칠~2주 걸립니다. 사이트맵 제출만으로 즉시 색인되지는 않습니다.

### 기존 Google Sites 처리

바로 지우지 마세요. 새 사이트가 색인된 것을 확인한 뒤,
Google Sites About 페이지에 새 주소 링크를 걸어두고 두는 편이 낫습니다.

---

## 3. 외부 링크 — 이게 가장 중요합니다

색인이 안 되던 근본 원인은 **이 사이트를 가리키는 외부 링크가 0개**라는 점이었습니다.
파일을 올리는 것만으로는 해결되지 않습니다. 아래에 새 주소를 등록하세요.

- [ ] arXiv 저자 프로필 (Homepage 필드)
- [ ] Google Scholar 프로필 (Homepage)
- [ ] ORCID (Websites & Social Links)
- [ ] ResearchGate 프로필
- [ ] zbMATH Open / MathSciNet author profile
- [ ] 충북대 수학과 홈페이지 — 졸업생/구성원 링크 요청 (**`.ac.kr` 링크 1개가 나머지 전부보다 강합니다**)
- [ ] 다음 preprint의 저자 각주에 URL 기입
- [ ] 공저자 홈페이지에서 링크 (Granada, UCM)

`index.html` 의 "Elsewhere" 섹션에도 위 프로필 주소를 채워 넣으세요.
현재 `#` 와 `← paste ...` 표시로 비워 두었습니다. **양방향 링크**가 목적입니다.

---

## 4. 파일 구조

```
index.html          About (연구 소개, JSON-LD Person schema)
papers.html         Preprints 3 + Publications 4
talks.html          강연 18건
teaching.html       조교·멘토링
activities.html     수상·방문
collaborators.html  공동연구자
cv.html             CV 다운로드
style.css           전체 스타일
sitemap.xml         검색엔진용 페이지 목록
robots.txt          크롤링 허용 + sitemap 위치
.nojekyll           GitHub Pages의 Jekyll 처리 비활성화
assets/favicon.svg  파비콘
assets/             ← CV PDF를 여기 넣으세요
```

페이지를 추가하면 `sitemap.xml` 과 각 HTML의 `<nav>` 에 항목을 손으로 추가하면 됩니다.

---

## 5. CV

`assets/Manwook-Han-CV.pdf` 로 파일을 넣으세요. 파일명이 다르면 `cv.html` 의 링크도 고치세요.
Google Drive 대신 여기 두는 이유는 Google이 PDF 본문까지 색인하기 때문입니다.

---

## 6. 원본에서 수정한 부분 — 확인 필요

- **연락처**: 휴대폰 번호를 넣지 않았습니다. 색인이 되면 스크래핑 대상이 되므로 판단해서 넣으세요.
- **오타**: `conjecure` → `conjecture`, `Assistent` → `Assistant`,
  `Moñoz` → `Muñoz`, `Gyungju` → `Gyeongju`
- **저널명 전체 표기**: `Linear Multilinear Algebra` → `Linear and Multilinear Algebra`,
  `J. Math. Anal. Appl.` → 전체 명칭. 검색 쿼리가 약어보다 전체 명칭을 쓰기 때문입니다.
- **DOI 통일**: RACSAM·BKMS 링크를 `doi.org` 형식으로 바꿨습니다.
- **연구 소개 확장**: About의 관심 분야 5줄을 문장으로 늘렸습니다.
  thin content 문제를 풀려면 본문 텍스트가 필요합니다. **내용이 정확한지 반드시 검토하세요.**
- **지도교수 명시**: About에 Sun Kwang Kim 추가.
- **Collaborators**: 논문 1의 공저자 Daewoong Cheong 추가.
- **arXiv 저자 페이지 주소는 추측입니다.** `index.html`에서 확인 후 고치세요.
