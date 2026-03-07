from flask import Flask, render_template, request
import joblib
import numpy as np

# ==========================
# LOAD TRAINED MODEL
# ==========================
model = joblib.load('laptop_model_joblib')

app = Flask(__name__)

# ==========================
# ROUTES
# ==========================

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/project')
def project():
    return render_template("project.html")


# ==========================
# DICTIONARIES (ENCODING)
# ==========================

processor_dict = {'Intel':1, 'AMD':2, 'M1':3}

brand_dict = {
    'ASUS':310, 'Lenovo':320, 'acer':330,
    'Avita':340, 'HP':350, 'DELL':360,
    'MSI':370, 'APPLE':380
}

processor_name_dict = {
    'Core i3':10, 'Core i5':20, 'Celeron Dual':30,
    'Ryzen 5':40, 'Core i7':50, 'Core i9':60,
    'M1':70, 'Pentium Quad':80,
    'Ryzen 3':90, 'Ryzen 7':100, 'Ryzen 9':111
}

processor_gnrtn_dict = {
    '10th':110, 'Not Available':120, '11th':130,
    '7th':140, '8th':150, '9th':160,
    '4th':170, '12th':180
}

ram_gb_dict = {
    '4 GB':210, '8 GB':220, '16 GB':230, '32 GB':240
}

ram_type_dict = {
    'DDR4':400, 'LPDDR4':410, 'LPDDR4X':420,
    'DDR5':430, 'DDR3':440, 'LPDDR3':450
}

ssd_dict = {
    '0 GB':0, '128 GB':128, '256 GB':256,
    '512 GB':512, '1024 GB':1024,
    '2048 GB':2048, '3072 GB':3072
}

hdd_dict = {
    '0 GB':0, '512 GB':512,
    '1024 GB':1024, '2048 GB':2048
}

os_dict = {'Windows':500, 'DOS':510, 'Mac':520}

os_bit_dict = {'64-bit':64, '32-bit':32}

warranty_dict = {
    'No warranty':0, '1 year':1,
    '2 years':2, '3 years':3
}

msoffice_dict = {'No':0, 'Yes':1}

rating_dict = {
    '1 star':1, '2 stars':2,
    '3 stars':3, '4 stars':4, '5 stars':5
}


# ==========================
# PREDICTION ROUTE
# ==========================

@app.route('/predict', methods=['GET', 'POST'])
def predict():

    if request.method == 'POST':

        # ===== GET FORM DATA =====
        brand = request.form['brand']
        processor_brand = request.form['processor_brand']
        processor_name = request.form['processor_name']
        processor_gnrtn = request.form['processor_gnrtn']
        ram_gb = request.form['ram_gb']
        ram_type = request.form['ram_type']
        ssd = request.form['ssd']
        hdd = request.form['hdd']
        os = request.form['os']
        os_bit = request.form['os_bit']
        warranty = request.form['warranty']
        msoffice = request.form['msoffice']
        rating = request.form['rating']
        num_ratings = int(request.form['num_ratings'])
        num_reviews = int(request.form['num_reviews'])

        print("Laptop data received ✅")

        # ===== ENCODING =====
        brand = brand_dict[brand]
        processor_brand = processor_dict[processor_brand]
        processor_name = processor_name_dict[processor_name]
        processor_gnrtn = processor_gnrtn_dict[processor_gnrtn]
        ram_gb = ram_gb_dict[ram_gb]
        ram_type = ram_type_dict[ram_type]
        ssd = ssd_dict[ssd]
        hdd = hdd_dict[hdd]
        os = os_dict[os]
        os_bit = os_bit_dict[os_bit]
        warranty = warranty_dict[warranty]
        msoffice = msoffice_dict[msoffice]
        rating = rating_dict[rating]

        # ===== FEATURE ORDER (MUST MATCH TRAINING) =====
        features = [[
            brand,
            processor_brand,
            processor_name,
            processor_gnrtn,
            ram_gb,
            ram_type,
            ssd,
            hdd,
            os,
            os_bit,
            warranty,
            msoffice,
            rating,
            num_ratings,
            num_reviews
        ]]

        # ===== PREDICTION =====
        prediction = model.predict(features)[0]

        result = f"Estimated Laptop Price: ₹ {round(prediction,2)}"

        return render_template('project.html', prediction=result)

    return render_template('project.html')


# ==========================
# RUN APP
# ==========================

if __name__ == '__main__':
    app.run(debug=True)