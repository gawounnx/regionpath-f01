import json

# 샘플 입력 데이터
sample_input = {
    "target_job": "백엔드 개발자",
    "target_region": "충청권",
    "skills": ["Python", "SQL"],
    "certificates": ["정보처리기사 필기"],
    "projects": []
}

# 포트폴리오 생성 함수 (간단 버전)
def create_portfolio(data):
    return {
        "portfolio_summary": f"{data['target_region']} {data['target_job']}를 희망하는 구직자입니다.",
        "skill_tags": data["skills"],
        "ncs_tags": ["응용SW엔지니어링", "데이터베이스"]
    }

# 실행 테스트
result = create_portfolio(sample_input)

print(json.dumps(result, ensure_ascii=False, indent=2))
