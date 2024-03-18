from fastapi import FastAPI, HTTPException
from models import *
from utils import *

app = FastAPI()

@app.get("/stu-number/{stuNumber}")
async def stuNumber(stuNumber: str):
    errors = []
    if len(stuNumber) != 11:
        errors.append("اشتباه. تعداد کاراکترهای ورودی باید 11 باشد.")
    elif int(stuNumber[0:3]) not in range(400,403):
        errors.append("اشتباه. بخش سال نادرست است.")
    elif stuNumber[3:9] != "114150":
        errors.append("اشتباه. بخش ثابت نادرست است.")
    elif int(stuNumber[9:]) not in range(0,100):
        errors.append("اشتباه. بخش اندیس نادرست است.")
    else:
        errors.append("شماره دانشجویی : {data}")



@app.get("/stu-number/")
async def stuNumber(stuNumber: str):
    errors = []
    if len(stuNumber) != 11:
        errors.append(". تعداد کاراکترهای ورودی باید 11 باشد.")
    elif int(stuNumber[0:3]) not in range(400,403):
        errors.append("اشتباه. بخش سال نادرست است.")
    elif stuNumber[3:9] != "114150":
        errors.append("اشتباه. بخش ثابت نادرست است.")
    elif int(stuNumber[9:]) not in range(0,100):
        errors.append("اشتباه. بخش اندیس نادرست است.")
    if errors != []:
        raise HTTPException(status_code=400, detail=errors)
    else:
        return {
            "message": f" {stuNumber} داده ورودی معتبر است."
        }




@app.post("/stu-number/")
async def stuNumber(body: StudentNumber):
    errors = []
    if len(body.studentNumber) != 11:
        errors.append("شماره دانشجویی باید 11 رقم باشد.تعداد ارقام شماره دانشجوییوارد شدهنادرست است.")
    if int(body.studentNumber[0:3]) not in range(400,403):
        errors.append("error قسمت سال نادرست است.")
    if body.studentNumber[3:9] != "114150":
        errors.append("error قسمت ثابت نادرست است.")
    if int(body.studentNumber[9:]) not in range(0,100):
        errors.append("error قسمت اندیس نادرست است.")

    if errors != []:
        raise HTTPException(status_code=400, detail=errors)
    else:
        return {
            "message": "شماره دانشجویی معتبر است."
        }

@app.post("/validate-name/")
async def validate_name(body: Name):
    errors = []
    if is_persian(body.name):
        errors.append("نام باید فقط حاوی حروف فارسی باشد.")
    if len(body.name) > 10:
        errors.append("طول نام نباید بیشتر از 10 باشد.")
    if body.name.isdigit() or not body.name.isalnum():
        errors.append("نام نباید شامل عدد یا علائم خاص باشد.")
    if errors != []:
        raise HTTPException(status_code=400, detail=errors)
    else:
        return {
            "message": "نام معتبر است."
        }


@app.post("/validate-birth/")
async def validate_birth(body: Date):
    errors = []
    if not is_date(body.date):
        errors.append("تاریخ نا معتبر است.")
    if errors != []:
        raise HTTPException(status_code=400, detail=errors)
    else:
        return {
            "message": "تاریخ معتبر است."
        }


@app.post("/validate-serial/")
async def validate_serial(body: Serial):
    errors = []
    if not is_serial(body.serial):
        errors.append("سریال نا معتبر است.")
    if errors != []:
        raise HTTPException(status_code=400, detail=errors)
    else:
        return {
            "message": "سریال معتبر است."
        }


@app.post("/validate-city/")
async def validate_city(body: City):
    errors = []
    if not is_city(body.city):
        errors.append("مرکز نا معتبر است.")
    if errors != []:
        raise HTTPException(status_code=400, detail=errors)
    else:
        return {
            "message": "مرکز معتبر است."
        }


@app.post("/validate-province/")
async def validate_province(body: Province):
    errors = []
    if not is_province(body.province):
        errors.append("استان نا معتبر است.")
    if errors != []:
        raise HTTPException(status_code=400, detail=errors)
    else:
        return {
            "message": "استان معتبر است."
        }

@app.post("/validate-address/")
async def validate_address(body: Address):
    errors = []
    if len(body.address) > 100:
        errors.append("آدرس نا معتبر است.")
    if errors != []:
        raise HTTPException(status_code=400, detail=errors)
    else:
        return {
            "message": "آدرس معتبر است."
        }


@app.post("/validate-post/")
async def validate_address(body: Post):
    errors = []
    if len(body.post) != 10:
        errors.append("کد پستی نا معتبر است.")
    if errors != []:
        raise HTTPException(status_code=400, detail=errors)
    else:
        return {
            "message": "کد پستی معتبر است."
        }

@app.post("/validate-phone/")
async def validate_address(body: Phone):
    errors = []
    if not is_phone(body.phone):
        errors.append("تلفن همراه نا معتبر است.")
    if errors != []:
        raise HTTPException(status_code=400, detail=errors)
    else:
        return {
            "message": "تلفن همراه معتبر است."
        }

@app.post("/validate-landline/")
async def validate_address(body: Landline):
    errors = []
    if is_landline(body.landline):
        errors.append("تلفن ثابت نا معتبر است.")
    if errors != []:
        raise HTTPException(status_code=400, detail=errors)
    else:
        return {
            "message": "تلفن ثابت معتبر است."
        }

@app.post("/validate-faculty/")
async def validate_faculty(body: Faculty):
    errors = []
    if is_faculty(body.faculty):
        errors.append("دانشکده نا معتبر است.")
    if errors != []:
        raise HTTPException(status_code=400, detail=errors)
    else:
        return {
            "message": "دانشکده معتبر است."
        }

@app.post("/validate-field/")
async def validate_field(body: Field):
    errors = []
    if is_field(body.field):
        errors.append("رشته تحصیلی نا معتبر است.")
    if errors != []:
        raise HTTPException(status_code=400, detail=errors)
    else:
        return {
            "message": "رشته تحصیلی معتبر است."
        }

@app.post("/validate-marriage/")
async def validate_marriage(body: Marriage):
    errors = []
    if not body.marriage == "مجرد" or body.marriage == "متاهل":
        errors.append("وضعیت تاهل نا معتبر است.")
    if errors != []:
        raise HTTPException(status_code=400, detail=errors)
    else:
        return {
            "message": "وضعیت تاهل معتبر است."
        }

@app.post("/validate-code/")
async def validate_marriage(body: Code):
    errors = []
    if len(body.code) != 10:
        errors.append("کد ملی نا معتبر است.")
    if errors != []:
        raise HTTPException(status_code=400, detail=errors)
    else:
        return {
            "message": "کد ملی معتبر است."
        }

