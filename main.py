from http.client import HTTPSConnection 
from sys import stderr 
from json import dumps 
from time import sleep 
  
  
header_data1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA0MjIwODQ2Mjk3ODk0NTIwNg.G0HjMz.6YVbTcJhGuyl24thhbVCDNLl1lybzslLyFXxIE", 
	"host": "discordapp.com", 
	"referer": "https://discordapp.com/channels/918948319328350258/1030349344949407745" 
}


header_data2 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA0ODM1NDYzMzQ1OTk3MDA1OQ.GESjBT.wI0yVYBnZTnlHBcwXozHd1Ke-5QrvnB_hnEIbU", 
	"host": "discordapp.com", 
	"referer": "https://discordapp.com/channels/918948319328350258/1030349344949407745" 
}


 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def send_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_data1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("Work1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def send_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_data1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("Collect1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def work1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	send_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def collect1(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	send_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 

 
 
 
 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def send_word_message2(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_data2) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("Work2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def send_collect_message2(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_data2) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("Collect2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
 
 
 
 
def work2(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	send_word_message2(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def collect2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	send_collect_message2(get_connection(), "1030349344949407745", dumps(collect_message)) 

 
 
 
 
 
 
if __name__ == '__main__': 
	while True:    
		work1()
		collect1()
		work2()
		collect2()
		sleep(2) #every 1 hour = 3600
  