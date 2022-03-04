from flask import Flask, render_template, request
from prediction_service.prediction import load_model
import os

webapp_root = 'webapp'

params_path = "params.yaml"

static_path = os.path.join(webapp_root, "static")
template_path = os.path.join(webapp_root, "templates")

app = Flask(__name__, static_folder=static_path, template_folder=template_path)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        
        #Profile
        Profile = request.form ['Profile']
        if(Profile == "Ayurveda"):
            Profile_Ayurveda = 1
            Profile_Dentist = 0
            Profile_Dermatologists = 0
            Profile_ENT_Specialist = 0
            Profile_General_Medicine = 0
            Profile_Homeopath = 0
            
        elif(Profile == 'Dentsit'):
            Profile_Ayurveda = 0
            Profile_Dentist = 1
            Profile_Dermatologists = 0
            Profile_ENT_Specialist = 0
            Profile_General_Medicine = 0
            Profile_Homeopath = 0
            
        elif(Profile == 'Dermatologists'):
            Profile_Ayurveda = 0
            Profile_Dentist = 0
            Profile_Dermatologists = 1
            Profile_ENT_Specialist = 0
            Profile_General_Medicine = 0
            Profile_Homeopath = 0
            
        elif(Profile == 'ENT_Specialist'):
            Profile_Ayurveda = 0
            Profile_Dentist = 0
            Profile_Dermatologists = 0
            Profile_ENT_Specialist = 1
            Profile_General_Medicine = 0
            Profile_Homeopath = 0
            
        elif(Profile == 'General_Medicine'):
            Profile_Ayurveda = 0
            Profile_Dentist = 0
            Profile_Dermatologists = 0
            Profile_ENT_Specialist = 0
            Profile_General_Medicine = 1
            Profile_Homeopath = 0
            
        elif(Profile == 'Homeopath'):
            Profile_Ayurveda = 0
            Profile_Dentist = 0
            Profile_Dermatologists = 0
            Profile_ENT_Specialist = 0
            Profile_General_Medicine = 0
            Profile_Homeopath = 1
            
        else:
            Profile_Ayurveda = 0
            Profile_Dentist = 0
            Profile_Dermatologists = 0
            Profile_ENT_Specialist = 0
            Profile_General_Medicine = 0
            Profile_Homeopath = 0
            
        #Qualification
        Qualification = request.form["Qualification"]
        if (Qualification == "MBBS"):
            MBBS = 1
            BDS = 0
            BAMS = 0
            BHMS = 0
            MD_Dermatology = 0
            MS_ENT = 0
            Venereology_Leprosy = 0
            MD_General_Medicine = 0
            Diploma_in_Otorhinolaryngology = 0
            MD_Homeopathy = 0
            
        elif (Qualification == "BDS"):
            MBBS = 0
            BDS = 1
            BAMS = 0
            BHMS = 0
            MD_Dermatology = 0
            MS_ENT = 0
            Venereology_Leprosy = 0
            MD_General_Medicine = 0
            Diploma_in_Otorhinolaryngology = 0
            MD_Homeopathy = 0
            
        elif (Qualification == "BAMS"):
            MBBS = 0
            BDS = 0
            BAMS = 1
            BHMS = 0
            MD_Dermatology = 0
            MS_ENT = 0
            Venereology_Leprosy = 0
            MD_General_Medicine = 0
            Diploma_in_Otorhinolaryngology = 0
            MD_Homeopathy = 0
            
        elif (Qualification == "BHMS"):
            MBBS = 0
            BDS = 0
            BAMS = 0
            BHMS = 1
            MD_Dermatology = 0
            MS_ENT = 0
            Venereology_Leprosy = 0
            MD_General_Medicine = 0
            Diploma_in_Otorhinolaryngology = 0
            MD_Homeopathy = 0
            
        elif (Qualification == "MD Dermatology"):
            MBBS = 0
            BDS = 0
            BAMS = 0
            BHMS = 0
            MD_Dermatology = 1
            MS_ENT = 0
            Venereology_Leprosy = 0
            MD_General_Medicine = 0
            Diploma_in_Otorhinolaryngology = 0
            MD_Homeopathy = 0
            
        elif (Qualification == "MS ENT"):
            MBBS = 0
            BDS = 0
            BAMS = 0
            BHMS = 0
            MD_Dermatology = 0
            MS_ENT = 1
            Venereology_Leprosy = 0
            MD_General_Medicine = 0
            Diploma_in_Otorhinolaryngology = 0
            MD_Homeopathy = 0
            
        elif (Qualification == "Venereology and Leprosy"):
            MBBS = 0
            BDS = 0
            BAMS = 0
            BHMS = 0
            MD_Dermatology = 0
            MS_ENT = 0
            Venereology_Leprosy = 1
            MD_General_Medicine = 0
            Diploma_in_Otorhinolaryngology = 0
            MD_Homeopathy = 0
            
        elif (Qualification == "MD General Medicine"):
            MBBS = 0
            BDS = 0
            BAMS = 0
            BHMS = 0
            MD_Dermatology = 0
            MS_ENT = 0
            Venereology_Leprosy = 0
            MD_General_Medicine = 1
            Diploma_in_Otorhinolaryngology = 0
            MD_Homeopathy = 0
            
        elif (Qualification == "Diploma in Otorhinolaryngology"):
            MBBS = 0
            BDS = 0
            BAMS = 0
            BHMS = 0
            MD_Dermatology = 0
            MS_ENT = 0
            Venereology_Leprosy = 0
            MD_General_Medicine = 0
            Diploma_in_Otorhinolaryngology = 1
            MD_Homeopathy = 0
            
        elif (Qualification == "MD Homeopathy"):
            MBBS = 0
            BDS = 0
            BAMS = 0
            BHMS = 0
            MD_Dermatology = 0
            MS_ENT = 0
            Venereology_Leprosy = 0
            MD_General_Medicine = 0
            Diploma_in_Otorhinolaryngology = 0
            MD_Homeopathy = 1
            
        else:
            MBBS = 0
            BDS = 0
            BAMS = 0
            BHMS = 0
            MD_Dermatology = 0
            MS_ENT = 0
            Venereology_Leprosy = 0
            MD_General_Medicine = 0
            Diploma_in_Otorhinolaryngology = 0
            MD_Homeopathy = 0
            
        #Experience
        Experience = request.form["Experience"]
        Experience = int(Experience)
        
        #Ratings
        Rating = request.form["Rating"]
        Rating = int(Rating)
        if (Rating < 0):
            Rating = 0
        elif(Rating >= 0) & (Rating <10):
            Rating = 1
        elif(Rating >= 10) & (Rating <20):
            Rating = 2
        elif(Rating >= 20) & (Rating <30):
            Rating = 3
        elif(Rating >= 30) & (Rating <40):
            Rating = 4
        elif(Rating >= 40) & (Rating <50):
            Rating = 5
        elif(Rating >= 50) & (Rating <60):
            Rating = 6
        elif(Rating >= 60) & (Rating <70):
            Rating = 7
        elif(Rating >= 70) & (Rating <80):
            Rating = 8
        elif(Rating >= 80) & (Rating <90):
            Rating = 9
        elif(Rating >= 90) & (Rating <=100):
            Rating = 10
        else:
            Rating = 0
            
        #City
        City = request.form['City'] 
        if(City == 'Banglore'):
            City_Bangalore = 1
            City_Chennai = 0
            City_Coimbatore = 0
            City_Delhi = 0
            City_Ernakulam = 0
            City_Hyderabad = 0
            City_Mumbai = 0            
            City_Thiruvananthapuram = 0
            City_Unknown = 0
            
        elif(City == "Chennai"):
            City_Bangalore = 0
            City_Chennai = 1
            City_Coimbatore = 0
            City_Delhi = 0
            City_Ernakulam = 0
            City_Hyderabad = 0
            City_Mumbai = 0            
            City_Thiruvananthapuram = 0
            City_Unknown = 0
            
        elif(City == "Coimbatore"):
            City_Bangalore = 0
            City_Chennai = 0
            City_Coimbatore = 1
            City_Delhi = 0
            City_Ernakulam = 0
            City_Hyderabad = 0
            City_Mumbai = 0            
            City_Thiruvananthapuram = 0
            City_Unknown = 0
            
        elif(City == "Delhi"):
            City_Bangalore = 0
            City_Chennai = 0
            City_Coimbatore = 0
            City_Delhi = 1
            City_Ernakulam = 0
            City_Hyderabad = 0
            City_Mumbai = 0            
            City_Thiruvananthapuram = 0
            City_Unknown = 0
            
        elif(City == "Ernakulam"):
            City_Bangalore = 0
            City_Chennai = 0
            City_Coimbatore = 0
            City_Delhi = 0
            City_Ernakulam = 1
            City_Hyderabad = 0
            City_Mumbai = 0            
            City_Thiruvananthapuram = 0
            City_Unknown = 0
            
        elif(City == "Hyderabad"):
            City_Bangalore = 0
            City_Chennai = 0
            City_Coimbatore = 0
            City_Delhi = 0
            City_Ernakulam = 0
            City_Hyderabad = 1
            City_Mumbai = 0            
            City_Thiruvananthapuram = 0
            City_Unknown = 0
            
        elif(City == "Mumbai"):
            City_Bangalore = 0
            City_Chennai = 0
            City_Coimbatore = 0
            City_Delhi = 0
            City_Ernakulam = 0
            City_Hyderabad = 0
            City_Mumbai = 1            
            City_Thiruvananthapuram = 0
            City_Unknown = 0
            
        elif(City == "Thiruvananthapuram"):
            City_Bangalore = 0
            City_Chennai = 1
            City_Coimbatore = 0
            City_Delhi = 0
            City_Ernakulam = 0
            City_Hyderabad = 0
            City_Mumbai = 0            
            City_Thiruvananthapuram = 1
            City_Unknown = 0
            
        else:
            City_Bangalore = 0
            City_Chennai = 0
            City_Coimbatore = 0
            City_Delhi = 0
            City_Ernakulam = 0
            City_Hyderabad = 0
            City_Mumbai = 0            
            City_Thiruvananthapuram = 0
            City_Unknown = 1

        model = load_model(params_path) 

        prediction =[[Experience,Rating,MBBS,BDS,BAMS,BHMS,MD_Dermatology,MS_ENT,Venereology_Leprosy,
                    MD_General_Medicine,Diploma_in_Otorhinolaryngology,MD_Homeopathy,City_Bangalore,City_Chennai,
                    City_Coimbatore,City_Delhi,City_Ernakulam,City_Hyderabad,City_Mumbai,City_Thiruvananthapuram,
                    City_Unknown,Profile_Ayurveda,Profile_Dentist,Profile_Dermatologists,Profile_ENT_Specialist,
                    Profile_General_Medicine,Profile_Homeopath]]
                    
        
        Fees = model.predict(prediction)
        # round(prediction[0],2)  
        
        return render_template('home.html', prediction_text="Your Doctor consultancy Fees is Rs. {}".format(Fees))
     	    
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    