############ Imports ############
from flask import Flask
from flask import request
import os

app = Flask(__name__)

############ Load scripts filenames ############
scripts_folder = os.popen("pwd").read().replace("\n", "")

############ HTML Components ############

# Homepage
def home():
  ## Obtain sh filenames
  files = [f for f in os.listdir(scripts_folder) if os.path.isfile(os.path.join(scripts_folder, f))]
  sh_files = [f for f in files if f.endswith('.sh')]
  sh_files.sort()
  
  
  ## H1
  home = '<h1>Scripts runner</h1>'
  
  ## Links
  home += '<p>Links:</p>'
  home += '<ul>'
  for filename in sh_files:
    home += '<li><a href="/run-script?script=' + filename + '">' + filename + '</a></li>'
  home += '</ul>'
  
  ## Input
  home += '<p>Run command:</p>'
  home += '<form action="/run-generic-script">'
  home += '<input type="text" name="script" id="script" value="" placeholder="Enter command" style="width:400px">'
  home += '<input type="submit" value="Run Script">'
  home += '</form>'
  
  return home

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
  return home()
  
# Script runner
@app.route("/run-script")
def run_script():
  script = request.args.get('script', type = str)
  run_result = os.popen("./" + script).read()
  return home() + result_component(run_result)
  
# Generic Script Runner
@app.route("/run-generic-script")
def run_generic_script():
  script = request.args.get('script', type = str)
  if script == "":
    script = "echo 'No commands entered'"
  run_result = os.popen(script).read()
  return home() + result_component(run_result)

############ Run APP ############
if __name__ == "__main__":
  app.run(host='0.0.0.0')

