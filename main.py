from http.client import HTTPSConnection 
from sys import stderr 
from json import dumps 
from time import sleep 
  
  


header_data2 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA1MjIzNjM0NjM4NDczMjE3MA.GODLy1.mPJetELgFzHSNrOFZ94yrUsl_Rko52hS2qqcV0", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}

 
 
 
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



  
header_odikro1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization":"MTA0OTQwMzIxOTE4NjU1MjkyNA.GvTO0p.xiZCatYcyx_TFhqhZTMhw9unOAUyawNCEjhpb4", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def odikro_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_odikro1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("odikro1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def odikro_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_odikro1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("odikro2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def odikro1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	odikro_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def odikro2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	odikro_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 

 
 

  
header_andre1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization":"MTA1ODY0MDMzODQ4ODY3NjM1Mg.GTU_M-._n959wU1Zfg8JIS4TeNjXPChbNqw_ORSCnSq_4", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def andre_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_andre1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("andre1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def andre_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_andre1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("andre2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def andre1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	andre_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def andre2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	andre_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 

 
 
  
header_chang1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA1ODUwMTE3OTgyMDIzMjcyNQ.Glhs6h.-qh-UxpiKnx3d_Gc-_gH_xLIJfq7S5tYiLqwFs", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def chang_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_chang1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("chang1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def chang_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_chang1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("chang2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def chang1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	chang_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def chang2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	chang_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 


 
header_alekesi1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization":"MTA1ODY0NzAyNTQ3MTcyOTY2NA.G0MErU.29KVQOFwRM7JIvpwlBtnLKhsUU3tFBrxu4edeg", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/1057253536678825994/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def alekesi_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_alekesi1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("alekesi1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def alekesi_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_alekesi1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("aleksi2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def alekesi1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	alekesi_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def alekesi2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	alekesi_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 

 
   
header_elbir1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization":"MTA1ODcxNzA2NDE5MTI3OTE1NQ.GlXOmG.Qc6Lcxe6rOojV1RrFOkJogg5vRTQWfMIdwcLe8", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def elbir_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_elbir1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("elbir1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def elbir_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_elbir1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("ebir2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def elbir1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	elbir_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def ebir2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	elbir_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 


  
header_ubril1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization":"MTA1ODcxODQyNjU1OTkzODYwMQ.Gw7hGD.miT6KtP65EaCgqRXyIoOIUi5Qi3VPjK-L5j78A", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def ubril_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_ubril1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("ubril1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def ubril_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_ubril1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("ubril2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def ubril1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	ubril_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def ubril2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	ubril_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 

 
  
header_ishmael1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization":"MTA1ODcyNjkzNDkyNzkwMDc1Mg.GixUhS.h1ckTj5TZKdLSfcH2RVcNorhjCMNotrjdhFdTM", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def ishmael_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_ishmael1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("ishmael1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def ishmael_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_ishmael1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("ishmael2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def ishmael1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	ishmael_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def ishmael2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	ishmael_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 

 

  
header_syn1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA0ODUxNjAwMDA3NDY5NDczNg.GDu4QA.qvT0Klmj4GZ6Wy-nU1Y22ObDrLmakRPuwrSV08", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/1057253536678825994/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def syn_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_syn1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("sydney1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def syn_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_syn1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("syn2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def syn1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	syn_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def Syn2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	syn_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 


  
header_darko1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA1MDc0MzIzMjExNzYwNDQ0Mw.GEPp1H.5gPj38OfRcX-exmJ0AXrwMJsX-DJApHuSGEWC4", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def darko_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_darko1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("darko1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def darko_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_darko1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("darko2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def darko1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	darko_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def dark2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	darko_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 


  
header_sammy1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA1MDU3Njc5MzUyODE3Njc3Mg.GHecGj.h1tLln8InBIogwcDka3VNngv7iXjMv2Ec9LR7A", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def sammy_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_sammy1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("sam1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def sammy_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_sammy1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("sammy2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def sammy(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	sammy_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def sammy2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	sammy_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 


  
header_lilD1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA0NzU5MDI0NTI1Nzk2OTc3Nw.GYWVYz.Y0EQvtCq3_0d28WjhafwnkvLjrMZwNDAJ0RIV8", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def lilD_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_lilD1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("littleDra1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def lilD_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_lilD1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("lilD2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def lilD1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	lilD_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def lilD2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	lilD_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 


  
header_penalty1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA0ODM0NTQ3NTgwMTE1MzY3OA.G6i9iC.iliWXHJJWNeeSbRVCYm-53luFpIB-_yDp8xf8M", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def penalty_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_penalty1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("penalty1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def penalty_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_penalty1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("penalty2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def penalty1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	penalty_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def penalty2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	penalty_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 


  
header_drialian1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA1MDczNjU3MTYxNzM5NDY5OQ.GtjIAq.gCdbSstKoFGGi9AyiWYkV2WTOu46RtkB4fWfpU", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def drialian_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_drialian1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("drialain1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def drialian_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_drialian1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("drialian2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def drailian1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	drialian_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def drialian2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	drialian_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 

 
   
header_data1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA1MDUyNjU0NjM4MjgyMzQ3NA.Gc3ZXp.cTl9Aka_Ioj2OOvsXiB1LEppJ-gIfcb3FwnWyY", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def send_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_data1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("qqwert_1") 
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
            print("qqwert_2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def qqwert_1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	send_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def qqwert_2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	send_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 



  
header_turger1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA1MjAwNzU2NTA4MjQ5NzA2NA.GlrS_C.QOGEcNojEdlZtg71nDj-ULWCTGc381XcgzjWWc", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def turger_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_turger1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("turger1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def turger_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_turger1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("turger2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def turger1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	turger_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def turger2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	turger_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 


  
header_kollie1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA1Mjg5NDExMzU5NjQ1NzA3MQ.G-1UUt.qngnAs9bWOSUpairQMNWgYxLWP-W0V01g6MLQo", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}

 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def kollie_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_kollie1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("kelfile1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def kollie_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_kollie1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("kollie2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def kollie1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	kollie_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def kollie2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	kollie_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 

header_trumu1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA1MjIzMDQyNjI1NDYzOTExNA.G8P8_S.5qLkCX7SHIUCHMKlKET0N089D4a37S2On4GRlM", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def trumu_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_trumu1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("trumu1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def trumu_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_trumu1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("trumu2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def trumu1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	trumu_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def trumu2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	trumu_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 

  
header_big1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA0OTYzNzU1NjM4MTI4NjQ2MQ.GNcn6H.Pdl8-qvF9LdT3IuZTRHqlPUal4vfy8a9dZi7hY", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def big_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_big1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("big1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def big_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_big1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("big2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def big1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	big_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def bigr2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	big_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 
 

  
header_capebrown1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA1MDc0NzkwMDAyOTgzMzI2Ng.GIKJz3.WgnWcEyWmn-af4Nh3Qh2QyRjo_QbJCpq0C6YFA", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def capebrown_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_capebrown1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("capebrown1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def capebrown_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_capebrown1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("capebrown2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def capebrown1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	capebrown_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def capebrown2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	capebrown_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 


  
header_eddyie1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA1MDc3ODAwNDc5NzgwNDY5NQ.GwrGnz.65gsnNaRGGgaB5Ng1wqO7xLkDNf-jCQE22SW48", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def eddyie_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_eddyie1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("eddyie1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def eddyie_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_eddyie1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("eddyie2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def eddyie1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	eddyie_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def eddyie2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	eddyie_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 

 

 
header_obaapa1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA0MjMzOTI3NzA5NjM2MTk5NA.GIimid.jDFm1ilWWR_osV-5OAed6HavoraZiVtxZ5Kko0", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def obaapa_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_obaapa1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("obaapa1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def obaapa_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_obaapa1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("obaapa2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def obaapa1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	obaapa_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def obaapa2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	obaapa_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 

 

  
header_blood1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA0MjIwODQ2Mjk3ODk0NTIwNg.G-G__p.g3Rr4vFSAGqKN_69AWnkHGSnpxxeYsz35h9mNQ", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def blood_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_blood1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("blood1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def blood_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_blood1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("blood2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def blood1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	blood_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def blood2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	blood_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 


  
header_addo1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA1MDcyODc1MDU0OTA1NzU0Ng.GM0Ie1.e3gOqdVnn4K8cAlndJRuRKdjMFsM8aEcGp2D2A", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/1057253536678825994/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def send_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_addo1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("addo1") 
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
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_addo1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("addo2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def addo1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	send_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def addo2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	send_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 

 




  
header_maxy1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA0OTY0MDU1ODY5MzQ3MDI1OQ.GSml2k.DP1h3987JgKfJX1RE3RU8mzIUVNJQzLgz1xMOo", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def maxy_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_maxy1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("maxy1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def maxy_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_maxy1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("maxy2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def maxy1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	maxy_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def maxy2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	maxy_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 


 
header_AB1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA0ODM1NDYzMzQ1OTk3MDA1OQ.G0_6SF.S7woMjAWKranR7xqH8UG5ZMPmdSpV_fU3gm5Js", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/1057253536678825994/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def AB_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_AB1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("AB1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def AB_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_AB1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("AB2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def AB1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	AB_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def AB2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	AB_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 




  
header_messi1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA0OTYzODIxNzE3MjkyMjM4OA.GmPa3g.0tWxgKLcxwWu-Seqoq_pQZtY2diNh0RrCL-oi0", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def messi_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_messi1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("messi1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def messi_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_messi1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("messi2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def messi1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	messi_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def messi2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	messi_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 


 
header_omar1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA0OTY0MDE5MjE4MjU4NzQzMg.GWwPRW.SgRqaVMQkqb-XX62t-_-KMkaIM4EaQ8ONoXqag", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/1057253536678825994/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def omar_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_omar1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("Omar1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def omar_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_omar1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("omar2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def omar1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	omar_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def omar2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	omar_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 


 
header_baffor1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA1MDc1MDM3ODE5MjQyNTAwMw.GTS-Ys.ca9Z9cnVBFH-mhOT1E2zzbFobMxwzKaZBSLKMw", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def baffor_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_baffor1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("baffor1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def baffor_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_baffor1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("baffor2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def baffor1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	baffor_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def baffor2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	baffor_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 




header_derek1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA0ODUxMTE1OTE5MzU3MTM0OQ.GRnXC7.yBkDLGwXYqgD6p7_mVuSHaQMaTuBhy0PqV9F9U", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def derek_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_derek1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("DEre1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def derek_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_derek1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("dere2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def derek1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	derek_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def derek2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	derek_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 


  
header_kelfie1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA1MDczNTIwODUxNDcyNzk4Nw.Gj-8mm.ERPVirAwtKopO5NFiqSAvkYOKDRHfFVBWz87wM", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def kelfie_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_kelfie1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("kelfile1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def kelfie_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_kelfie1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("kelfie2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def kelfie1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	kelfie_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def kelfie2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	kelfie_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 


  
header_steve1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA0ODUwMTY2MjU2MzcwODk0OQ.GTWTN2.gxhufrhmlgV2lXDIYf1JjFiWJfdFhHi2e-UHFc", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def steve_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_steve1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("steve1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def steve_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_steve1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("steve2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def steve1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	steve_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def steve2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	steve_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 


  
header_adamu1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA1OTA2NzI0NzI4NjU1MDU4OA.GDKmht.x8RwStUALfkJdTmNeoo-FqKs1nUJTLLQhtmkI4", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/1057253536678825994/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def send_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_adamu1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("adamu1") 
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
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_adamu1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("adamu2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def adamu1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	send_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def adamu2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	send_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 


  
header_bokamoso1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA1OTA2NjExNDczMjIxMjI1NQ.GFmISy.tqw3pomr1Jyv6UYsqmHQnFMlVEgKxIcKZfw6GA", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def bokamoso_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_bokamoso1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("bokamoso1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def bokamoso_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_bokamoso1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("bokamoso2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def bokamoso1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	bokamoso_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def bokamoso2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	bokamoso_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 



  
header_Thato1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA1OTA2NDAyNDY0NzYxNDQ5NQ.GhqsLm.B_h50Qb4IO4R_WJDdHGBRdWpa-7Ha5Wh_JHTJg", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def Thato_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_Thato1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("Thato1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def Thato_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_Thato1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("Thato2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def Thato1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	Thato_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def Thato2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	Thato_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 




 
header_kugawo1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization":"MTA1OTA1ODY5MTA2NTc4NjM4OQ.GwvLJO.CVzWePxDfLy4fdeitWTNHWiSIOKjMHGmfotV7o", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def kugawo_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_kugawo1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("kungawo1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def kugawo_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_kugawo1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("kungawo2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def kungawo1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	kugawo_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def kungawo2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	kugawo_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 



  
header_jose1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization":"MTA1OTAzMzYwMTIwNDgyMjA2Ng.GhY35O.nAH_vrmI82HcJcFJXjI8aJglecGs7Lauecy9uM", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def jose_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_jose1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("jose1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def jose_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_jose1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("jose2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def jose1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	jose_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def jose2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	jose_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 

 


header_lucas1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization":"MTA1OTAzMTY4MTc0MDMxMjU5Ng.GAJKpL.DZrwfc28g83uzOP6JWAoLY3I3ALX_DPSfbyaw4", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def lucas_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_lucas1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("lucas1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def lucas_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_lucas1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("lucas2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def licas1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	lucas_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def lucas2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	lucas_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 

 
header_matteo1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization":"MTA1OTAyNjE2NjE2MzQ0Nzg2OA.GRV1NF.uWzhbwyO0vyspDfWUiWZrvA6Rfb7GZh3loJNMI", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def matteo_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_matteo1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("matteo1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def matteo_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_matteo1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("matteo2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def matteo1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	matteo_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def matteo2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	matteo_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 

 
 
  
header_derek1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization":"MTA1OTAyNDgwMTI0MDQ2MTMzMg.GRntF9.42jFaqWQDtOr0bEdfx7tOFGZpD2SNq6JqkjFsU", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def derek_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_derek1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("derek1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def derek_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_derek1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("derekk2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def derekk1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	derek_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def derekk2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	derek_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 


header_oliver1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization":"MTA1OTAyMjY2NzQ0MjgyMzI0OA.G_-QRc.fzSGahVLYGRigR5l9fIWzmXVdmDSDQHn-42lW8", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def oliver_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_oliver1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("oliver1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def oliver_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_oliver1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("oliver2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def oliver1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	oliver_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def oliver2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	oliver_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 


 
header_laim1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization":"MTA1ODgwMjk2Mjc4MjIzNjc5NA.GvvTFv.gMogri1OCQonKqDOMy7d2pKRSIPJ3w7m694nvs", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/918948319328350258/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def laim_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_laim1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("laim1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def laim_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_laim1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("laim2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def liam1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	laim_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def laim2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	laim_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 



  
header_lhadi1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA1OTA2ODk5MjQ3MzU1MDg0OA.Gnhf5L.s233ux5LOBHusQRxnS3_a5Hs05KRVhy3vWkO6o", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/1057253536678825994/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def lhadi_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_lhadi1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("alhaadi1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def lhadi_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_lhadi1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("alhadi2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def alhadi1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	lhadi_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def alhasi2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	lhadi_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 


 
header_absko1 = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "MTA1OTA3MjcxNjMxMDg1OTg5OQ.GTTLCB.SBk6syBISZ9Hin_JEszdQ6so4MRyQw4sKq7ei8", 
	"host": "discordapp.com", 
	"referer": "https://discord.com/channels/1057253536678825994/1030349344949407745" 
}




 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def absko_word_message1(conn1, channel_id, work_message): 
    try: 
        conn1.request("POST", f"/api/v6/channels/{channel_id}/messages", work_message, header_absko1) 
        resp = conn1.getresponse() 
         
        if 199 < resp.status < 300: 
            print("absko1") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 

def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 

def absko_collect_message1(conn2, channel_id, collect_message): 

    try: 
        conn2.request("POST", f"/api/v6/channels/{channel_id}/messages", collect_message, header_absko1) 
        resp = conn2.getresponse() 
        if 199 < resp.status < 300: 
            print("absko2") 
            pass 
 
        else: 
            stderr.write(f"HTTP recibido {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
       
 
 
def absko1(): 
	work_message = { 
		"content": "*work", 
		"tts": "false", 
	}
 
	absko_word_message1(get_connection(), "1030349344949407745", dumps(work_message)) 

 
def absko2(): 
	collect_message = { 
		"content": "*collect", 
		"tts": "false", 
	}
 
	absko_collect_message1(get_connection(), "1030349344949407745", dumps(collect_message)) 

 
 
 
 
 
 
 
 
 
if __name__ == '__main__': 
	while True:    
		work2()
		sleep(5) 
		collect2()
		sleep(5) 
		odikro1()
		sleep(5)
		odikro2()
		sleep(5) 
		# andre1()
		# sleep(5) 
		# andre2()
		# sleep(5)
		# chang1()
		# sleep(5) 
		# chang2()
		sleep(5)
		alekesi1()
		sleep(5) 
		alekesi2()
		sleep(5)
		elbir1()
		sleep(5) 
		ebir2()
		sleep(5)
		ubril1()
		sleep(5) 
		ubril2()
		sleep(5)
		ishmael1()
		sleep(5) 
		ishmael2()
		sleep(5)
		# syn1()
		# sleep(5) 
		# Syn2()
		# sleep(5)
		darko1()
		sleep(5) 
		dark2()
		sleep(5)
		# sammy()
		# sleep(5) 
		# sammy2()
		# sleep(5)
		# lilD1()
		# sleep(5) 
		# lilD2()
		# sleep(5)
		penalty1()
		sleep(5) 
		penalty2()
		sleep(5)
		drailian1()
		sleep(5) 
		drialian2()
		sleep(5)
		qqwert_1()
		sleep(5) 
		qqwert_2()
		sleep(5)
		# kollie1()
		# sleep(5) 
		# kollie2()
		# sleep(5)
		# collect1()
		# sleep(5) 
		# collect2()
		# sleep(5)
		turger1()
		sleep(5) 
		turger2()
		sleep(5)
		trumu1()
		sleep(5) 
		trumu2()
		sleep(5)
		big1()
		sleep(5) 
		bigr2()
		sleep(5)
		capebrown1()
		sleep(5) 
		capebrown2()
		sleep(5)
		eddyie1()
		sleep(5) 
		eddyie2()
		sleep(5)
		obaapa1()
		sleep(5) 
		obaapa2()
		sleep(5)
		blood1()
		sleep(5) 
		blood2()
		sleep(5)
		addo1()
		sleep(5) 
		addo2()
		sleep(5)
		maxy1()
		sleep(5) 
		maxy2()
		sleep(5)
		AB1()
		sleep(5) 
		AB2()
		sleep(5)
		messi1()
		sleep(5) 
		messi2()
		sleep(5)
		omar1()
		sleep(5) 
		omar2()
		sleep(5)
		baffor1()
		sleep(5) 
		baffor2()
		sleep(5)
		derek1()
		sleep(5) 
		derek2()
		sleep(5)
		kelfie1()
		sleep(5) 
		kelfie2()
		sleep(5)
		steve1()
		sleep(5) 
		steve2()
		sleep(5)
		adamu1()
		sleep(5) 
		adamu2()
		sleep(5)
		bokamoso1()
		sleep(5) 
		bokamoso2()
		sleep(5)
		Thato1()
		sleep(5) 
		Thato2()
		sleep(5)
		kungawo1()
		sleep(5) 
		kungawo2()
		sleep(5)
		jose1()
		sleep(5) 
		jose2()
		sleep(5)
		licas1()
		sleep(5) 
		lucas2()
		sleep(5)
		matteo1()
		sleep(5) 
		matteo2()
		sleep(5)
		derekk1()
		sleep(5) 
		derekk2()
		sleep(5)
		oliver1()
		sleep(5) 
		oliver2()
		sleep(5)
		liam1()
		sleep(5) 
		laim2()
		sleep(5)
		alhadi1()
		sleep(5) 
		alhasi2()
		sleep(5)
		absko1()
		sleep(5) 
		absko2()
		sleep(5)
		# collect1()
		# sleep(5) 
		# collect2()
		# sleep(5)
		# collect1()
		# sleep(5) 
		# collect2()
		# sleep(5)


  
  
 

  
