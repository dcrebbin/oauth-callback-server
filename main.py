from fastapi import FastAPI
import webbrowser
import uvicorn
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/")
async def callback(request):
    # Forward the callback parameters to Unity
    query = str(request.query_params)
    webbrowser.open(f'characterquest://callback?{query}')
    return PlainTextResponse('You can close this window now')

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)