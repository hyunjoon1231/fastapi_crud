from fastapi import FastAPI  # FastAPI라는 기능을 가져온다.

app = FastAPI()  # FastAPI를 사용해서 웸앰을 만든다.


@app.get("/hello")  # "/hello" 주소로 요청이 오면 아래 함수를 실행한다.
async def hello():  # hello라는 이름의 함수를 만든다 (비동기 함수)
    return {"message": "Hello FastAPI"}  # 딕셔너리 형태로 인사를 돌려준다.
