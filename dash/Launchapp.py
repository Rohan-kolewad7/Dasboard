import subprocess

app1_command =['streamlit','run','dash1']
app2_command =['streamlit','run','Dash2']

#launching both dasboard parallel

subprocess.Popen(app1_command)
subprocess.Popen(app2_command)