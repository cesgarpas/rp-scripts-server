############ Imports ############
from flask import Flask
from flask import request
import os

app = Flask(__name__)

############ Load scripts filenames ############
scripts_folder = os.popen("pwd").read().replace("\n", "")

files = [f for f in os.listdir(scripts_folder) if os.path.isfile(os.path.join(scripts_folder, f))]
sh_files = [f for f in files if f.endswith('.sh')]
sh_files.sort()

############ HTML Components ############
# Homepage

## H1
home = '<h1>Scripts runner</h1>'

## Links
home += '<p>Links:</p>'
home += '<ul>'
for filename in sh_files:
  home += '<li><a href="/' + filename.split('.')[0] + '">' + filename + '</a></li>'
home += '</ul>'

## Input
home += '<p>Run command:</p>'
home += '<form action="/run-generic-script">'
home += '<input type="text" name="script" id="script" value="" style="width:400px">'
home += '<input type="submit" value="Run Script">'
home += '</form>'

# Textarea
## Component
textarea_h = '<textarea disabled style="font-size:16px;height:50%;width:100%">'
textarea_t = '</textarea>'

## Result formation
def result_component(result):
  return "</br>Result:</br>" + textarea_h + result + textarea_t


############ Routes/controllers ############
# Home
@app.route("/")
def homepage():
  return home
  
# Generic Script Runner
@app.route("/run-generic-script")
def run_generic_script():
  script = request.args.get('script', type = str)
  if script == "":
    script = "echo 'No script entered'"
  return home + result_component(os.popen(script).read())
  
# Generic router for scripts
for filename in sh_files:
  script_name = filename.split('.')[0]
  function = '@app.route("/' + script_name + '")\n'
  function += 'def ' + script_name.replace('-','_') + '():\n'
  function += '   return home + result_component(os.popen("./' + script_name + '.sh").read())'
  exec(function)


############ Run APP ############
if __name__ == "__main__":
  app.run(host='0.0.0.0')

