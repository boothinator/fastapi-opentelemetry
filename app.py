from fastapi import FastAPI
import uvicorn
import os
# Import the `configure_azure_monitor()` function from the
# `azure.monitor.opentelemetry` package.
from azure.monitor.opentelemetry import configure_azure_monitor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

app = FastAPI()

# Configure OpenTelemetry to use Azure Monitor with the 
# APPLICATIONINSIGHTS_CONNECTION_STRING environment variable.
if os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING"):
  configure_azure_monitor()
  print("Azure monitor configured")

@app.get("/")
async def root():
  return {"message": "Hello World"}

FastAPIInstrumentor.instrument_app(app)

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)
