# CBNU UTCI Map

충북대학교 캠퍼스의 그늘과 체감온도(UTCI)를 지도에 보여 주는 Android + FastAPI 프로젝트입니다.
지금은 저장소 뼈대와 `/health`만 있습니다.

## 로컬 Backend

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements-dev.txt
PYTHONPATH=backend uvicorn app.main:app --reload
PYTHONPATH=backend pytest backend/tests
```
