from flask import Flask, render_template, request, jsonify
#import aiml
import os
from tf_idf import *
import time
# kernel = aiml.Kernel()

# def load_kern(forcereload):
# 	if os.path.isfile("bot_brain.brn") and not forcereload:
# 		kernel.bootstrap(brainFile= "bot_brain.brn")
# 	else:
# 		kernel.bootstrap(learnFiles = os.path.abspath("aiml/std-startup.xml"), commands = "load aiml b")
# 		kernel.saveBrain("bot_brain.brn")
#

import MySQLdb
from MySQLdb import escape_string as thwart
def connection():
	conn = MySQLdb.connect(host="localhost",
	                       user = "root",
	                       passwd = "",
	                       db = "thpbot")
	c = conn.cursor()
	print("connection created")
	return c, conn



app = Flask(__name__)
@app.route("/")
def hello():
	#load_kern(False)
	return render_template('index.html')

@app.route("/ask", methods=['POST','GET'])
def ask():
	message = str(request.form['chatmessage'])
	# # if message == "save":
	# #     kernel.saveBrain("bot_brain.brn")
	# #     return jsonify({"status":"ok", "answer":"Brain Saved"})
	# # elif message == "reload":
	# # 	load_kern(True)
	# # 	return jsonify({"status":"ok", "answer":"Brain Reloaded"})
	# # elif message == "quit":
	# # 	exit()
	# # 	return jsonify({"status":"ok", "answer":"exit Thank You"})
	# #
	# # # kernel now ready for use
	# else:
		# while True:
		#bot_response = kernel.respond(message)
		# print bot_response
	bot_response = previous_chats(message)
	try:
		c,conn = connection()
		# sql="""INSERT INTO messages(msg_from_user,msg_to_user) VALUES('%s')""" % message
		print("below query")
		c.execute("INSERT INTO messages(msg_from_user,msg_to_user) VALUES(%s,%s)",(thwart(message),thwart(bot_response)))
		print("i m in try block")
		conn.commit()
		print("inserted")
		c.close()
	except Exception as e:
		print(e)
	#print(type(message))
	#return message
	time.sleep(1)
	return jsonify({'status':'OK','answer':bot_response})



if __name__ == "__main__":
    app.run(debug=True)
