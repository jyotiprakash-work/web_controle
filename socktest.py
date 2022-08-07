from flask import Flask,render_template, request

import pyautogui

app = Flask(__name__)
pyautogui.FAILSAFE = False
# @app.route('/')
# def hello_world():
# 	return render_template("index.html")
@app.route('/')
def hello_world():
	width,hight = pyautogui.size()
	config ={'hight':hight,'width':width} 
	return render_template("test.html",config = config)

@app.route('/left_click')
def left_click():
	print('Left')
	x,y = pyautogui.position()
	pyautogui.click(x,y,clicks =1, interval=1, button='left')
	return 'ok'
@app.route('/right_click')
def right_click():
	print('Right')
	pyautogui.rightClick()
	return 'ok'
@app.route('/mouse_move', methods = ['POST'])
def mouse_move():
	print('move')
	json_data = request.json
	print(json_data)
	x,y = pyautogui.position()
	pyautogui.moveTo(json_data['x'], json_data['y'], duration=0)
	return 'ok'

if __name__ == '__main__':
   app.run(host = '0.0.0.0', port =5000)