from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import subprocess
import os
import glob
app = Flask(__name__)
img_path = '/home/my_hands_on/static/'

@app.route('/upload')
def require_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      img_save_path = img_path + secure_filename(f.filename) 
      f.save(img_save_path)
      subprocess.run(["python3", "resize.py", img_save_path])
      return 'file uploaded successfully <a href="/view" />view</a>'

@app.route('/view')
def view_thumbs():
   file_list = []
   image_names = glob.glob('/home/my_hands_on/static/*_thumb.*')

   for i, name in enumerate(image_names):
      filename = os.path.basename(name)
      file_list.append(filename)

   return render_template('view_thumbs.html', image_names=file_list)
		
if __name__ == '__main__':
   app.run(debug = True)
   app.run(host='0.0.0.0',port=5000)
