import os
import flask
from flask import Flask,render_template,request,redirect,jsonify, url_for
import pickle
import numpy as np



app = Flask(__name__)


@app.route("/")
def home():
	return render_template('home.html')

@app.route("/future")
def future():
	return render_template('future.html')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/predict", methods=['POST'])
def predict():
	
	data1 = request.form['a']
	data2 = request.form['b']
	data3 = request.form['c']
	data4 = request.form['d']
	data5 = request.form['e']
	data6 = request.form['f']
	data7 = request.form['g']
	data8 = request.form['h']

	arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8]])
	loaded_model = pickle.load(open('fier.pkl', 'rb'))
	pred = loaded_model.predict(arr)

	if pred == 1:
		data = {
			'title':'Mechanical Engineering',
			'overview':'Mechanical engineering is an engineering branch that combines engineering physics and mathematics principles with materials science to design, analyze, manufacture, and maintain mechanical systems. The mechanical engineering field requires an understanding of core areas including mechanics, dynamics, thermodynamics, materials science, structural analysis, and electricity. In addition to these core principles, mechanical engineers use tools such as computer-aided design (CAD), computer-aided manufacturing (CAM), and product lifecycle management to design and analyze manufacturing plants, industrial equipment and machinery, heating and cooling systems, transport systems, aircraft, watercraft, robotics, medical devices, weapons, and others. It is the branch of engineering that involves the design, production, and operation of machinery.',
			'list': [
				'Universiti Malaya (UM)',
				'Universiti Teknologi Malaysia (UTM)',
				'Universiti Teknologi MARA (UITM)',
				'Universiti Teknologi Petronas (UTP)',
				'Universiti Islam Antarabangsa Malaysia (UIAM)',
				'Universiti Kebangsaan Malaysia (UKM)',
				'Universiti Malaysia Perlis (UNIMAP)',
				'Universiti Malaysia Sabah (UMS)',
				'Universiti Malaysia Sarawak (UNIMAS)',
				'Universiti Teknikal Malaysia Melaka (UTeM)'
				]
		};
	elif pred == 2:
		data = {
			'title':'Electrical and Electronic Engineering',
			'overview':'The degree in Electical & Electronic Engineering programme is designed to equip students with a sound understanding of fundamental theories and concepts in electrical and electronic engineering from designing and manufacturing the latest consumer devices to sophisticated scientific and industrial technologies.',
			'list': [
				'Universiti Malaya (UM)',
				'Universiti Teknologi Malaysia (UTM)',
				'Universiti Teknologi MARA (UITM)',
				'Universiti Teknologi Petronas (UTP)',
				'Universiti Islam Antarabangsa Malaysia (UIAM)',
				'Universiti Kebangsaan Malaysia (UKM)',
				'Universiti Malaysia Perlis (UNIMAP)',
				'Universiti Malaysia Sabah (UMS)',
				'Universiti Malaysia Sarawak (UNIMAS)',
				'Universiti Teknikal Malaysia Melaka (UTeM)',
				'Universiti Pertahanan Nasional Malaysia (UPNM)'
				]
		};
	elif pred == 3:
		data = {
			'title':'Chemical Engineering',
			'overview':'Chemical engineering is a branch of engineering which deals with the study of design and operation of chemical plants and methods of improving production. Chemical engineers develop economical commercial processes to convert raw material into useful products.',
			'list': [
				'Universiti Malaya (UM)',
				'Universiti Sains Malaysia (USM)',
				'Universiti Putra Malaysia (UPM)',
				'Universiti Teknologi Malaysia (UTM)',
				'Universiti Teknologi MARA (UITM)',
				'Universiti Teknologi Petronas (UTP)',
				'Universiti Malaysia Sarawak (UNIMAS)'
				]
		};
	elif pred == 4:
		data = {
			'title':'Civil Engineering',
			'overview':'Civil engineering is a professional engineering discipline that deals with the design, construction, and maintenance of the physical and naturally built environment, including public works such as roads, bridges, canals, dams, airports, sewerage systems, pipelines, structural components of buildings, and railways.',
			'list': [
				'Universiti Sains Malaysia (USM)',
				'Universiti Malaya (UM)',
				'Universiti Teknologi Petronas (UTP)',
				'Universiti Putra Malaysia (USM)',
				'Universiti Islam Antarabangsa Malaysia (UIAM)',
				'Universiti Teknologi MARA (UITM)',
				'Universiti Kebangsaan Malaysia (UKM)'
				]
		};
	elif pred == 5:
		data = {
			'title':'Information Technology Program',
			'overview':'Information engineering, also known as Information technology engineering, information engineering methodology or data engineering, is a software engineering approach to designing and developing information systems.',
			'list': [
				'Universiti Sains Malaysia (USM)',
				'Universiti Malaya (UM)',
				'Universiti Kebangsaan Malaysia (UKM)',
				'Universiti Putra Malaysia (UPM)',
				'Universiti Teknologi Malaysia (UTM)',
				'Universiti Teknologi MARA (UITM)',
				'Universiti Islam Antarabangsa Malaysia (UIAM)'
				]
		};



	return render_template('result.html', data=data)
	
if __name__ == "__main__":
     app.secret_key = "!mzo53678912489"
     app.run(debug=True)