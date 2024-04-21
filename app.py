from fastapi import FastAPI, Request, Form, HTTPException,Header,Depends ,status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2AuthorizationCodeBearer
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from sqlalchemy import create_engine, Column, Integer, String,LargeBinary,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import requests
import uvicorn
import httpx,json
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from authlib.integrations.starlette_client import OAuth, OAuthError
from pydantic import BaseModel
from typing import Optional
from datetime import date
import google.generativeai as genai

headers={'api_key':'a5d759ef-abb3-4204-8be3-190f13155abf'}

DATABASE_URL = "sqlite:///db_directory/testdb.sqlite3"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Student_Eligibility(Base):
    __tablename__ = "student_eligibility"
    email_id=Column(String,primary_key=True, index=True)
    ph_no = Column(Integer)
    first_subject= Column(String)
    first_subject_marks_obtained= Column(Integer)
    first_subject_total_marks= Column(Integer)
    second_subject= Column(String)
    second_subject_marks_obtained= Column(Integer)
    second_subject_total_marks= Column(Integer)  
    third_subject= Column(String)
    third_subject_marks_obtained= Column(Integer)
    third_subject_total_marks= Column(Integer) 
    fourth_subject=Column(String)
    fourth_subject_marks_obtained= Column(Integer)
    fourth_subject_total_marks= Column(Integer) 
    Stream= Column(String)
    Eligibility=Column(String)
class Student_Details(Base):
    __tablename__ = "student_details"
    email_id = Column(String, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    pincode = Column(Integer)
    nationality = Column(String)
    exam_center = Column(String)
    aadhar_no = Column(Integer)
    email = Column(String)
    gender = Column(String)
    dob = Column(DateTime)
    age = Column(Integer)
    religion = Column(String)
    community = Column(String)
    caste = Column(String)
    mother_tongue = Column(String)
    ph_no = Column(Integer)
    father_ph_no = Column(Integer)
    mother_ph_no = Column(Integer)
    father_name = Column(String)
    father_occupation = Column(String)
    father_income = Column(Integer)
    mother_name = Column(String)
    mother_occupation = Column(String)
    mother_income = Column(Integer)
    _10th_exam_name = Column(String)
    _10th_register_no = Column(String)
    _10th_passing_date = Column(String)
    _10th_attempts = Column(Integer)
    _10th_maths_marks = Column(Integer)
    _10th_science_marks = Column(Integer)
    _10th_total_marks = Column(Integer)
    _10th_max_marks = Column(Integer)
    _10th_school_address = Column(String)
    Stream = Column(String)
    _12th_subject1= Column(String)
    _12th_subject1_marks_obtained = Column(Integer)
    _12th_subject1_total_marks = Column(Integer)
    _12th_subject2= Column(String)
    _12th_subject2_marks_obtained = Column(Integer)
    _12th_subject2_total_marks = Column(Integer)
    _12th_subject3= Column(String)
    _12th_subject3_marks_obtained = Column(Integer)
    _12th_subject3_total_marks = Column(Integer)
    _12th_subject4= Column(String)
    _12th_subject4_marks_obtained = Column(Integer)
    _12th_subject4_total_marks = Column(Integer)
    _12th_subject5= Column(String)
    _12th_subject5_marks_obtained = Column(Integer)
    _12th_subject5_total_marks = Column(Integer)
    passport_photo = Column(LargeBinary)
    _10th_marksheet = Column(LargeBinary)
    _12th_marksheet = Column(LargeBinary)
class FormData1(BaseModel):
    email_id: Optional[str]
    ph_no: Optional[int]
    first_subject: Optional[str]
    first_subject_marks_obtained: Optional[int]
    first_subject_total_marks: Optional[int]
    second_subject: Optional[str]
    second_subject_marks_obtained: Optional[int]
    second_subject_total_marks: Optional[int]   
    third_subject: Optional[str]
    third_subject_marks_obtained: Optional[int]
    third_subject_total_marks: Optional[int]   
    fourth_subject: Optional[str]
    fourth_subject_marks_obtained: Optional[int]
    fourth_subject_total_marks: Optional[int]  
    Stream: Optional[str] 
    Eligibility: Optional[str]
class FormData2(BaseModel):
    email_id:Optional[str]
    name: Optional[str]
    address: Optional[str]
    pincode: Optional[int]
    nationality: Optional[str]
    exam_center: Optional[str]
    aadhar_no: Optional[int]
    email: Optional[str]
    gender: Optional[str]
    dob: Optional[date]
    age: Optional[int]
    religion: Optional[str]
    community: Optional[str]
    caste: Optional[str]
    mother_tongue: Optional[str]
    ph_no: Optional[int]
    father_ph_no: Optional[int]
    mother_ph_no: Optional[int]
    father_name: Optional[str]
    father_occupation: Optional[str]
    father_income: Optional[int]
    mother_name: Optional[str]
    mother_occupation: Optional[str]
    mother_income: Optional[int]
    _10th_exam_name: Optional[str]
    _10th_register_no: Optional[str]
    _10th_passing_date: Optional[str]
    _10th_attempts: Optional[int]
    _10_maths_marks: Optional[int]
    _10th_science_marks: Optional[int]
    _10th_total_marks: Optional[int]
    _10th_max_marks: Optional[int]
    _10th_school_address: Optional[str]
    Stream: Optional[str]
    _12th_subject1: Optional[str]
    _12th_subject1_marks_obtained: Optional[int]
    _12th_subject1_total_marks: Optional[int]
    _12th_subject2: Optional[str]
    _12th_subject2_marks_obtained : Optional[int]
    _12th_subject2_total_marks: Optional[int]
    _12th_subject3: Optional[str]
    _12th_subject3_marks_obtained: Optional[int]
    _12th_subject3_total_marks: Optional[int]
    _12th_subject4: Optional[str]
    _12th_subject4_marks_obtained: Optional[int]
    _12th_subject4_total_marks: Optional[int]
    _12th_subject5: Optional[str]
    _12th_subject5_marks_obtained: Optional[int]
    _12th_subject5_total_marks: Optional[int]
    passport_photo: Optional[bytes]
    _10th_marksheet: Optional[bytes]
    _12th_marksheet: Optional[bytes]
Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")


app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="add any string...")
app.mount("/static", StaticFiles(directory="static"), name="static")

oauth = OAuth()
oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_id='9310596698-kbh954efjos4gjcb1pv2gvreqi74u528.apps.googleusercontent.com',
    client_secret='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',
)

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    user = request.session.get('user')
    if user:
        return templates.TemplateResponse("Home.html", {"request": request,"email_id":user["email"]})
    else:
        return 'You need to <a href="/login">Login with Google</a> to access this page.'

@app.get("/login")
async def login(request: Request):
    url = request.url_for('auth')
    return await oauth.google.authorize_redirect(request, url,scope="openid email") # Adjust the scope based on your requirements


@app.get('/auth')
async def auth(request: Request):
    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError as e:
        return templates.TemplateResponse(
            name='error.html',
            context={'request': request, 'error': e.error}
        )
    user = token.get('userinfo')
    if user:
        request.session['user'] = dict(user)
    return RedirectResponse('/')

@app.get('/logout')
def logout(request: Request):
    request.session.pop('user')
    request.session.clear()
    return RedirectResponse('read_item')

@app.get("/personal_details", response_class=HTMLResponse)
async def read_item(request: Request):
    db = SessionLocal() 
    try:
        existing_student = db.query(Student_Details).filter(Student_Details.email_id == request.session.get('user')["email"]).first()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    return templates.TemplateResponse("personaldetails.html", {"request": request,"data":existing_student})

@app.post("/personal_details",response_class=HTMLResponse)
async def stud_det_post(request:Request):
    form_data = await request.form()
    internal_api_url = "http://127.0.0.1:8000/personal_details/post"
    try:
        async with httpx.AsyncClient() as client:
            await client.post(internal_api_url,data=json.dumps(dict(form_data)),headers=headers)
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    return templates.TemplateResponse("personaldetails.html", {"request": request})


@app.post("/",response_class=HTMLResponse)
async def create_item(request:Request): 
    form_data = await request.form()
    internal_api_url = "http://127.0.0.1:8000/api/stu_el"
    try:
        async with httpx.AsyncClient() as client:
            await client.post(internal_api_url,data=json.dumps(dict(form_data)),headers=headers)
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    return templates.TemplateResponse("Home.html", {"request": request})

async def authenticate_api_key(api_key: str):
    if api_key is None:
        raise HTTPException(status_code=401, detail="API key is missing")
    if api_key != headers['api_key']:
        raise HTTPException(status_code=403, detail="Invalid API key")
    

@app.post("/api/stu_el")
async def validate_data(request:Request,form_data: FormData1):
    await authenticate_api_key(request.headers.get('api_key'))
    db = SessionLocal() 
    try:
        existing_student = db.query(Student_Eligibility).filter(Student_Eligibility.email_id == form_data.email_id).first()
        if existing_student:
            for key, value in form_data.dict().items():
                setattr(existing_student, key, value)
        else:
            new_student = Student_Eligibility(**form_data.dict())
            db.add(new_student)
        db.commit()
        db.refresh(new_student if not existing_student else existing_student)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    return {"message": "Data validated successfully", "form_data": "fwegf"}

@app.post("/personal_details/post",response_class=HTMLResponse)
async def stud_det_post(request:Request,form_data: FormData2):
    await authenticate_api_key(request.headers.get('api_key'))
    db = SessionLocal() 
    try:
        new_student = Student_Details(**form_data.dict())
        db.add(new_student)
        db.commit()
        db.refresh()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    return {"message": "Data validated successfully"}


@app.post("/eligibility_api")
async def eligibility_reason(request:Request):
    form_data = await request.form()
    eligibility_info=form_data['Stream']+","+form_data['first_subject']+"="+form_data['first_subject_marks_obtained']+","+form_data['second_subject']+"="+form_data['second_subject_marks_obtained']+","+form_data['third_subject']+"="+form_data['third_subject_marks_obtained']+","+form_data['fourth_subject']+"="+form_data['fourth_subject_marks_obtained']
    
    genai.configure(api_key="AIzaSyC5DXjyN4Udbb9xONanYvGVL5sOrA1jaHU")
    try:
        generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
    }
        safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_LOW_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_LOW_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_LOW_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_LOW_AND_ABOVE"
    },
    ]
        model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                generation_config=generation_config,
                                safety_settings=safety_settings)
        convo = model.start_chat(history=[
    {
        "role": "user",
        "parts": ["You are chatbot which only outputs the reason for a student's eligibility .This is the criteria \nThe eligibility criteria:\n\nTotal four subjects\nFor Science:\nSubjects:\n1.Maths\n2.Physics\n3.Chemistry\n4.Computer Science/Information Practices\nAll the four subjects should have more than 50%  .maths, physics and the  maximum of any one ( chemistry and computer science) should have more than 75%   or else if information practices is selected then maths ,physics and chemistry  should have more than 75%.\n\nFor Arts:\n\nSubjects:\n1.Mathematics/ Business Mathematics /\nStatistics/Applied Mathematics / Business Mathematics and\nStatistics\n2. Commerce / Economics / Accountancy \n3. Commerce / Economics / Accountancy \n4.Computer Science/Information Practices\n\nAll the four subjects should have more than 50% . If computer science is selected then  subject1 should should have more than 75% and the two subjects with the maximum marks (any two) among the three remaining subjects should have more than 75% or else if information practices is selected  then subjects 1 , 2 and 3 should have more 75%.\n\nWith respect to the above criteria you should determine the eligibility and the reason if the candidate is not eligible given the marks and stream of the candaite"]
    },
    {
        "role": "model",
        "parts": ["Okay, I can help you determine student eligibility based on the criteria you've provided. \n\n**Here's how I'll work:**\n\n*   You'll provide me with the student's stream (Science or Arts) and their marks in each of the four subjects. \n*   I will then analyze the marks and determine if the student meets the eligibility requirements for their chosen stream. \n*   If eligible, I'll simply state \"Eligible\". \n*   If not, I'll provide the specific reason why they are ineligible. \n\n**Example:**\n\n*   **Input:** Science, Maths=80, Physics=60, Chemistry=90, Computer Science=85 \n*   **Output:** Eligible\n\n*   **Input:** Arts, Maths=70, Economics=80, Accountancy=90,  Information Practices = 70\n*   **Output:** Not eligible - Information Practices requires 75% in Maths, Economics, and Accountancy."]
    },
    {
        "role": "user",
        "parts": ["Science ,Maths=78,Physics=90,Chemistry=65,Information Practices=100"]
    },
    {
        "role": "model",
        "parts": ["Not eligible - Information Practices requires 75% in Maths, Physics, and Chemistry."]
    },
    {
        "role": "user",
        "parts": ["Science ,Maths=78,Physics=90,Chemistry=65, Computer Science=100"]
    },
    {
        "role": "model",
        "parts": ["Eligible"]
    },
    ])
        convo.send_message(eligibility_info)
        response=convo.last.text
    except Exception as e:
        pass
    return {"data":response}



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)