from bot import telegram_chatbot
from response import message_response,train_name

bot = telegram_chatbot("config.cfg")




def make_reply(msg,name):
	global update_id
	if msg is not None:
		intent,value = message_response(msg)
		
		response = None

		if intent == "buying":
			response = "you can buy tickets from here" +"/n"
			response += "https://www.esheba.cnsbd.com/#/"

		if intent == "schedule" and value != "schedule":

			if value == "Silk City":
				response = "The Silkcity Express departs from Dhaka Komlapur station at 14:45 and arrives in Rajshahi Chapainababganj station at 08:35. In the return trip, Its leaves from Chapainababganj station at 07:40  and after 6-7 hours reaches Komlapur station at13:30. It works 6 days a week. Sunday is the weekly holiday of SIlkcity Express."
			if value == "Dhumketu Express":
				response = "The Dhumketu Express departs from Dhaka to Kamalapur railway station at 06:00 AM and arrives at Rajshahi at 11:40PM. This time it holds 769 number and Dhumketu Express doesn’t run Dhaka to Rajshahi route on Saturday. In the return trip, Dhumketu Express starts the journey from Rajshahi at 23:20 and ends the journey in Kamalapur station at 04:45. This time it holds the 770 number. Friday is the holiday of Rajshahi to Dhaka route."
			if value == "Padma":
				response = "The Padma Express departs from Dhaka Kamalapur station at 23:00 and after 5-6 hours its arrives in Rajshahi at 04:30. This time it holds the 759 number. In the return trip, Padma Express (760) starts the journey from Rajshahi station at 16:00 and ends the journey at 21:40. About 5-6 hours of time needed on this journey."
			return response

		if intent == "schedule" and value == "schedule":
			reply = "Which train you need schedule of Padma/Silk City/Dhumketu"
			bot.send_message(reply,from_)
			updates = bot.get_updates(offset=update_id)
			updates = updates['result']
			for item in updates:
				update_id = item['update_id']
				message = str(item['message']['text'])
						
			train= train_name(message)

			if train == "Silk City":
				response = "The Silkcity Express departs from Dhaka Komlapur station at 14:45 and arrives in Rajshahi Chapainababganj station at 08:35. In the return trip, Its leaves from Chapainababganj station at 07:40  and after 6-7 hours reaches Komlapur station at13:30. It works 6 days a week. Sunday is the weekly holiday of SIlkcity Express."
			if train == "Dhumketu Express":
				response = "The Dhumketu Express departs from Dhaka to Kamalapur railway station at 06:00 AM and arrives at Rajshahi at 11:40PM. This time it holds 769 number and Dhumketu Express doesn’t run Dhaka to Rajshahi route on Saturday. In the return trip, Dhumketu Express starts the journey from Rajshahi at 23:20 and ends the journey in Kamalapur station at 04:45. This time it holds the 770 number. Friday is the holiday of Rajshahi to Dhaka route."
			if train == "Padma":
				response = "The Padma Express departs from Dhaka Kamalapur station at 23:00 and after 5-6 hours its arrives in Rajshahi at 04:30. This time it holds the 759 number. In the return trip, Padma Express (760) starts the journey from Rajshahi station at 16:00 and ends the journey at 21:40. About 5-6 hours of time needed on this journey."
			return response
			
		if intent == "location_finding":

			if value == "Silk City":
				response = "Silk City is currently in Ullapara Station.It is late by 20 minutes off schedule"
			if value == "Dhumketu Express":
				response = "Dhumketu Express is currently in Sirajgong Station.It is on time to schedule"
			if value == "Padma":
				response = "Padma is currently in Tongi Station.It is late by 10 minutes"
		
		if intent == None:
			response = "Please I don't understand. \n You can only ask me about \n Buying tickets \n Schedule of train(Padma,Silk City,Dhumketu) \n Location of train(Padma,Silk City,Dhumketu) \n Thank You"
		
		if intent == "Greetings":
			response = "Hi " + name + " I am a rail bot at your service.You can only ask me about \n Buying tickets \n Schedule of train(Padma,Silk City,Dhumketu) \n Location of train(Padma,Silk City,Dhumketu) \n Thank You"
		

	return response

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            name = item["message"]["from"]["first_name"]
            reply = make_reply(message,name)
            bot.send_message(reply, from_)



