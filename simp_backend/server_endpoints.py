import uvicorn 
import datetime 
from fastapi import FastAPI, File, UploadFile, status, Header, Request, Depends 
from fastapi.staticfiles import StaticFiles 
app = FastAPI() 
 
count = 0 
 
telem = [] 
telem_temp = [] 
 
@app.get("/") 
async def getR(): 
    return "Test" 
 
@app.get("/get") 
async def getUser(sum: int): 
    global count 
    count += sum 
    return {"count":count} 
 
@app.get("/telemetry") 
async def getTelemetry(temp: int, hum: int): 
    global telem 
    telem.append({"time": datetime.datetime.now(),  
    "temperature": temp,  
    "humidity": hum}) 
    return {"telemetry":telem} 
 
@app.get("/get_telemetry") 
async def getTelemetryFull(): 
    global telem 
    return {"telemetry":telem} 
 
@app.get("/get_telemetry/temp") 
async def getTelemetryByTemp(temperature: int): 
    global telem 
    global telem_temp 
    for i in range(0,len(telem)): 
        if telem[i]["temperature"] > temperature: 
            telem_temp.append(telem[i]) 
    return {"telemetry_temp":telem_temp}
