# 영차
> 실시간 주식 정보 조회용 서버

![Generic badge](https://img.shields.io/badge/version-1.0.1-green.svg)

<img src="/_images/image.png" title="영차" alt="영차" width="22%"></img>

## Introduction
### 주식 및 비트코인 투자 현황 통합 관리 앱

- 보유한 국내 주식, 해외 주식, 비트코인을 통합적으로 관리하고 실시간 현재가를 확인할 수 있어요!
- 보유한 전체 주식과 비트코인에 대한 나의 최종 자산, 수익률 등 투자 현황을 확인할 수 있어요!
- 어제 대비 오늘의 수익금을 확인할 수 있어요!

## Download
[AppStore(IOS)](https://apps.apple.com/kr/app/%EC%98%81%EC%B0%A8/id1571507288)

## Features
### 로그인
- 애플 로그인 (IOS)
- 카카오 로그인 (AOS, IOS)

### 현재 등록할 수 있는 종목 조회
매일 거래할 수 있는 종목을 갱신합니다.
- 국내 주식 (KOSPI, KOSDAQ, KONEX): 약 3000개의 종목 존재.
- 해외주식 (NASDAQ, NYSE): 약 7000개의 종목 존재.
- 비트코인 (업비트): 약 100개의 종목 존재.

### 보유한 주식/비트코인 통합 관리
- 국내 주식, 비트코인: 원화를 통한 보유 주식 등록 및 관리할 수 있습니다..
- 해외 주식: 달러를 통한 보유 주식 등록 및 관리할 수 있습니다.
- 현재가를 원화와 달러로 모두 조회할 수 있습니다. (통화 변환 시 실시간 환율 정보를 이용합니다.)
- 현재가를 실시간으로 가져오고, 수익률을 계산할 수 있습니다.

### 보유한 최종 자산, 수익률 계산
- 모든 주식/비트 코인의 시드 값과 총자산을 원화로 조회할 수 있습니다.
- 모든 주식/비트 코인의 수익률을 계산할 수 있습니다.

### 어제 대비 오늘의 수익금 계산
- 어제 대비 오늘의 수익금 및 수익률 계산할 수 있습니다.


## Installation

### with docker-compose

```bash
docker-compose up --build
```


## Links
[API Server Repository](https://github.com/depromeet/9th_muyaho_backend)