from flask import Flask
import os

app = Flask(__name__)

# Load scripts filenames
scripts_folder = os.popen("pwd").read().replace("\n", "")

files = [f for f in os.listdir(scripts_folder) if os.path.isfile(os.path.join(scripts_folder, f))]
sh_files = [f for f in files if f.endswith('.sh')]
sh_files.sort()

# Homepage
home = '<h1>Scripts runner</h1>'
home += '<p>Links:</p>'

home += '<ul>'
for filename in sh_files:
  home += '<li><a href="/' + filename.split('.')[0] + '">' + filename + '</a></li>'
home += '</ul>'


# Textarea
textarea_h = '<textarea disabled style="font-size:16px;height:50%;width:100%">'
textarea_t = '</textarea>'


# Home
@app.route("/")
def hello_world():
  return home

# Generic router
for filename in sh_files:
  script_name = filename.split('.')[0]
  function = '@app.route("/' + script_name + '")\n'
  function += 'def ' + script_name.replace('-','_') + '():\n'
  function += '   return home + "</br>Result:</br>" + textarea_h + os.popen("./' + script_name + '.sh").read() + textarea_t'
  exec(function)

if __name__ == "__main__":
  app.run(host='0.0.0.0')
