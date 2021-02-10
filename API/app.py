from flask import Flask, url_for, redirect, jsonify
import random
import array
from flask_cors import CORS
from nanoid import generate

app = Flask(__name__, static_url_path="")
CORS(app)
app.secret_key = "msayak1269"

MAX_LEN = 12

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
images = [
    "https://testreactapp.pythonanywhere.com/asphalt-dark-dawn-endless-531321.jpg",
    "https://testreactapp.pythonanywhere.com/IMG_20210128_113355.jpg",
    "https://scontent.frdp3-1.fna.fbcdn.net/v/t1.0-9/141098489_1812694508887119_1265020106594168074_o.jpg?_nc_cat=102&ccb=2&_nc_sid=09cbfe&_nc_ohc=FN_HSVaPIJUAX_aZzLb&_nc_ht=scontent.frdp3-1.fna&oh=fd9d294c6e1671b8dd90f9e4f5876a74&oe=603CC115",
    "https://scontent.frdp3-1.fna.fbcdn.net/v/t1.0-9/119456645_1697530943736810_6971064068625247940_o.jpg?_nc_cat=104&ccb=2&_nc_sid=8bfeb9&_nc_ohc=ARbkE4-s7p8AX99yLio&_nc_ht=scontent.frdp3-1.fna&oh=3c81f317faf33a46fef00d40f92bc952&oe=603C4C16",
    "https://scontent.frdp3-1.fna.fbcdn.net/v/t1.0-9/120560992_1717076821782222_1815039093400554836_o.jpg?_nc_cat=100&ccb=2&_nc_sid=8bfeb9&_nc_ohc=GbLxcvppwbcAX9ycrP8&_nc_ht=scontent.frdp3-1.fna&oh=0d86cabf59456a9fc5b1f22ed03204f3&oe=603CFCE7",
    "https://scontent.frdp3-1.fna.fbcdn.net/v/t1.0-9/80689045_1468691293287444_8613311085379846144_o.jpg?_nc_cat=106&ccb=2&_nc_sid=8bfeb9&_nc_ohc=sfoBC6VV5VsAX98V_m4&_nc_ht=scontent.frdp3-1.fna&oh=eeb486d88676b1c1338b0c498e6b011b&oe=603CFDE5",
    "https://scontent.frdp2-1.fna.fbcdn.net/v/t1.0-9/132268539_1788275991328971_2026203256541679061_o.jpg?_nc_cat=109&ccb=2&_nc_sid=e3f864&_nc_ohc=C8Bvp1nAFDoAX-UIHAO&_nc_ht=scontent.frdp2-1.fna&oh=3768b158975d81791de92bd1d3156d62&oe=603CDB4C"
]
    
addresses = [
    "11B,Beleghata,Kolkata 700010","38/3 Elgin Road,Kolkata 700020","2/8 Biren Roy Road,Kolkata 700008",
     "16,BC Street,Kolkata 700009","30C,HC Road,Kolkata 700026","16A,Bosepara Lane,Kolkata 712164","106,Vivekananda Road,Kolkata 700006",
     "Land’s End,Bandstand,Bandra West,Mumbai 400050","B/3,VL Mehta Road,Mumbai 400049",
     "Antilia,Altamount Road,Mumbai 400026"
     ]



@app.route("/api/get/user")
def getUser():
    firstNameLength = random.randrange(3, 10)
    lastNameLength = random.randrange(4, 10)

    firstName = ""
    lastName = ""

    for _ in range(firstNameLength):
        firstName += alpha[random.randrange(len(alpha))]
    for _ in range(lastNameLength):
        lastName += alpha[random.randrange(len(alpha))]

    userEmail = f"{lastName}@{firstName}.com"

    userImage = images[random.randrange(len(images))]

    date = random.randrange(1,30)
    month = random.randrange(1,13)
    year = random.randrange(1900,2000)
    dob = f"{date}/{month}/{year}"

    password = ""
    password = generate(size=10)

    address = addresses[random.randrange(0,10)]

    phoneNo=""
    for _ in range(5):
        phoneNo += str(random.randrange(7,10))
    for _ in range(5):
        phoneNo += str(random.randrange(0,10)) 
    phoneNo = "+91"+phoneNo      

    resp = {
        "firstName": firstName.capitalize(),
        "lastName": lastName.capitalize(),
        "email": userEmail,
        "dob":dob,
        "password":password,
        "address":address,
        "phoneNo":phoneNo,
        "image": userImage
    }

    return jsonify(resp)


if __name__ == "__main__":
    app.run(debug=True)
