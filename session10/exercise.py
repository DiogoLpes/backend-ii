from fastapi import FastAPI

app = FastAPI()

@app.get("/safe-input")
async def safe_input(user_input: str):
    # Basic sanitization: remove potential script tags
    sanitized = user_input.replace("<script>", "").replace("</script>", "")
    return {"sanitized_input": sanitized}