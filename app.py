from flask import Flask
from flask import request, send_from_directory
from flask import json
from flask import Response

app = Flask(__name__)

##url="http://127.0.0.1:5000"

# ret =[ {"title":"Sales Enablement","values":[
#     {"Elevate":"Pending","img":url+"/images/Elevate.png","title":"Elevate","smallDesc":"ELEVATE transforms how sales engages with the customer and manages their business by providing seamless access to sales content by leveraging M-AUTH technology and removing the need for a User ID/Password/RSA FOB. ELEVATE provides a simplified single account view for the Sales Rep where they can view basic account information including Service Requests Indicators, Opportunity Details, convert Sales Plays to Opportunities, as well as Account specific news.", "version":"v2.0.2","description":"ELEVATE transforms how sales engages with the customer and manages their business by providing seamless access to sales content by leveraging M-AUTH technology and removing the need for a User ID/Password/RSA FOB. ELEVATE provides a simplified single account view for the Sales Rep where they can view basic account information including Service Requests Indicators, Opportunity Details, convert Sales Plays to Opportunities, as well as Account specific news."},
#     {"E-lab Navigator":"Pending","img":url+"/images/Elab.png","title":"E-lab Navigator","smallDesc":"E-Lab Interoperability Navigator(ELN) is a robust interoperability and solution search portal and  home of the DELL EMC Support Matrix (ESM), a collection of supported configurations and solutions for DELL EMC products. Answering over one million queries a year, E-Lab Navigator provides costumers everything they need to know about interoperability in one place.", "version":"v1.0.2","description":"E-Lab Interoperability Navigator(ELN) is a robust interoperability and solution search portal and  home of the DELL EMC Support Matrix (ESM), a collection of supported configurations and solutions for DELL EMC products. Answering over one million queries a year, E-Lab Navigator provides costumers everything they need to know about interoperability in one place."},
#     {"Tricorder":"Pending","img":url+"/images/Tricorder.png","title":"Tricorder","smallDesc":"sample Description", "version":"v1.0.0","description":"This is sample description"},
#     {"VxRail":"Pending","img":url+"/images/VxRail.png","title":"VxRail","smallDesc":"VxRail to Go is your source everything. VxRail – from bi-weekly newsletter to the ignite Xforce series. Find video, audio and documents that keep you up-to-date on the latest from the VxRail product team.", "version":"v1.0.1","description":"VxRail to Go is your source everything. VxRail – from bi-weekly newsletter to the ignite Xforce series. Find video, audio and documents that keep you up-to-date on the latest from the VxRail product team."}
#   ]},{"title":"Technical Practictioner","values":[
#     {"DellEMC":"Pending","img":url+"/images/DellEMC.png","title":"DellEMC Mobile","smallDesc":"Dell EMC Mobile is your companion for Technology Insight and Product Support. Provides visibility and situational awareness to activities occurring with your DELL EMC products at your fingertips. Stay engaged and aware of your DELL EMC activities with the ability to take command of your environment. Access/browse technical documentation, stay in touch with the latest DELL EMC news and highlights, search the Knowledgebase, manage your full service request lifecycle, and engage with peers in the community support forums. With DELL EMC MOBILE, you always have the support to help you make your next move.", "version":"v3.4.4","description":"Dell EMC Mobile is your companion for Technology Insight and Product Support. Provides visibility and situational awareness to activities occurring with your DELL EMC products at your fingertips. Stay engaged and aware of your DELL EMC activities with the ability to take command of your environment. Access/browse technical documentation, stay in touch with the latest DELL EMC news and highlights, search the Knowledgebase, manage your full service request lifecycle, and engage with peers in the community support forums. With DELL EMC MOBILE, you always have the support to help you make your next move."},
#     {"Help a Customer":"Pending","img":url+"/images/HaC.png","title":"Help a Customer","smallDesc":"The HaC (Help a Customer) Mobile App empowers all team members to take action on behalf of our customers anytime, anywhere. It provides a convenient intake method to capture customer feedback & issue details and seamlessly connect to Dell’s existing Help a Customer service and support flows.", "version":"v1.1.4","description":"The HaC (Help a Customer) Mobile App empowers all team members to take action on behalf of our customers anytime, anywhere. It provides a convenient intake method to capture customer feedback & issue details and seamlessly connect to Dell’s existing Help a Customer service and support flows."}
#   ]},{"title":"Employee Productivity","values":[
#     {"Engage":"Pending","img":url+"/images/Engage.png","title":"Engage","smallDesc":"Engage is a Mobile App which allows a user to view the day plan (calendar), know what meeting is happening now and quickly dial into the meeting, view attendees, or connect to the video portion on WebEx or Skype, see their current / upcoming meeting. Meetings can be filtered by a sender, Meetings are automatically flagged depending on the senders level in the organization. User will also be able to view participants' Org View and Profile.", "version":"v1.0.0","description":"Engage is a Mobile App which allows a user to view the day plan (calendar), know what meeting is happening now and quickly dial into the meeting, view attendees, or connect to the video portion on WebEx or Skype, see their current / upcoming meeting. Meetings can be filtered by a sender, Meetings are automatically flagged depending on the senders level in the organization. User will also be able to view participants' Org View and Profile."},
#     {"Spaces":"Pending","img":url+"/images/Spaces.png","title":"Spaces","smallDesc":"Get to where you are going and save time with SPACES. Navigate Dell offices with live turn-by-turn directions, find hotel spaces once you arrive at the office, and meet-up with colleagues for chats, coffee, breaks or whatever else is on your work-day agenda.", "version":"v1.0.0","description":"Get to where you are going and save time with SPACES. Navigate Dell offices with live turn-by-turn directions, find hotel spaces once you arrive at the office, and meet-up with colleagues for chats, coffee, breaks or whatever else is on your work-day agenda."},
#     {"Help":"Pending","img":url+"/images/Help.png","title":"Help","smallDesc":"Quickly and efficiently change your Domain/Network account password from anywhere, anytime! With HELP mobile app, you can do all that from your mobile phone", "version":"v1.0.3","description":"Quickly and efficiently change your Domain/Network account password from anywhere, anytime! With HELP mobile app, you can do all that from your mobile phone"}
#   ]},{"title":"Pipeline","values":[
#     {"Self Service Portal":"Pending","img":url+"/images/E2E.png","title":"Self Service Portal","smallDesc":"A portal for making mobile apps.", "version":"v1.0.0","description":"The Self Service portal is a website that enables"},
#     {"Sales Dashboard":"Pending","img":url+"/images/SD.png","title":"Sales Dashboard","smallDesc":"Provides the real time statistics of operations in Sales", "version":"v1.0.5","description":"Provides the real time statistics of operations in Sales"},
#     {"EZDialer":"Pending","img":url+"/images/EZDialer.png","title":"EZDialler","smallDesc":"EZ Dialer gives you a quick and easy way to join meetings from your mobile device when you’re on the go. Just tap the meeting and EZ Dialer dials the bridge number and enters the participant code.", "version":"v2.1.0","description":"EZ Dialer gives you a quick and easy way to join meetings from your mobile device when you’re on the go. Just tap the meeting and EZ Dialer dials the bridge number and enters the participant code."},
#     {"Burn Notification":"Pending","img":url+"/images/BN.png","title":"Burn Notification","smallDesc":"Burn Notification App send out notification status to the user’s smart watch.", "version":"v1.0.0","description":"Burn Notification App send out notification status to the user’s smart watch."},
#     {"E2E MRP":"Pending","img":url+"/images/E2E.png","title":"E2E MRP","smallDesc":"sample Description", "version":"v1.0.1","description":"This is sample description"}
#   ]}]

@app.route('/', methods=["GET","POST"])
def get_json():
    url="https://desolate-reaches-50064.herokuapp.com"

    ret =[ {"title":"Sales Enablement","values":[
        # {"desc_type":"description","img":url+"/images/Elevate.png","title":"Elevate","smallDesc":"ELEVATE transforms how sales engages with the customer and manages their business by providing seamless access to sales content by leveraging M-AUTH technology and removing the need for a User ID/Password/RSA FOB. ELEVATE provides a simplified single account view for the Sales Rep where they can view basic account information including Service Requests Indicators, Opportunity Details, convert Sales Plays to Opportunities, as well as Account specific news.", "version":"v2.0.2","description":"ELEVATE transforms how sales engages with the customer and manages their business by providing seamless access to sales content by leveraging M-AUTH technology and removing the need for a User ID/Password/RSA FOB. ELEVATE provides a simplified single account view for the Sales Rep where they can view basic account information including Service Requests Indicators, Opportunity Details, convert Sales Plays to Opportunities, as well as Account specific news."},
        {"E-lab Navigator":"Pending","img":url+"/images/Elab.png","title":"E-lab Navigator","smallDesc":"E-Lab Interoperability Navigator(ELN) is a robust interoperability and solution search portal and  home of the DELL EMC Support Matrix (ESM), a collection of supported configurations and solutions for DELL EMC products. Answering over one million queries a year, E-Lab Navigator provides costumers everything they need to know about interoperability in one place.", "version":"v1.0.2","description":"E-Lab Interoperability Navigator(ELN) is a robust interoperability and solution search portal and  home of the DELL EMC Support Matrix (ESM), a collection of supported configurations and solutions for DELL EMC products. Answering over one million queries a year, E-Lab Navigator provides costumers everything they need to know about interoperability in one place."},
        {"Tricorder":"Pending","img":url+"/images/Tricorder.png","title":"Tricorder","smallDesc":"sample Description", "version":"v1.0.0","description":"This is sample description"},
        {"VxRail":"Pending","img":url+"/images/VxRail.png","title":"VxRail","smallDesc":"VxRail to Go is your source everything. VxRail – from bi-weekly newsletter to the ignite Xforce series. Find video, audio and documents that keep you up-to-date on the latest from the VxRail product team.", "version":"v1.0.1","description":"VxRail to Go is your source everything. VxRail – from bi-weekly newsletter to the ignite Xforce series. Find video, audio and documents that keep you up-to-date on the latest from the VxRail product team."}
      ]},{"title":"Technical Practictioner","values":[
        {"DellEMC":"Pending","img":url+"/images/DellEMC.png","title":"DellEMC Mobile","smallDesc":"Dell EMC Mobile is your companion for Technology Insight and Product Support. Provides visibility and situational awareness to activities occurring with your DELL EMC products at your fingertips. Stay engaged and aware of your DELL EMC activities with the ability to take command of your environment. Access/browse technical documentation, stay in touch with the latest DELL EMC news and highlights, search the Knowledgebase, manage your full service request lifecycle, and engage with peers in the community support forums. With DELL EMC MOBILE, you always have the support to help you make your next move.", "version":"v3.4.4","description":"Dell EMC Mobile is your companion for Technology Insight and Product Support. Provides visibility and situational awareness to activities occurring with your DELL EMC products at your fingertips. Stay engaged and aware of your DELL EMC activities with the ability to take command of your environment. Access/browse technical documentation, stay in touch with the latest DELL EMC news and highlights, search the Knowledgebase, manage your full service request lifecycle, and engage with peers in the community support forums. With DELL EMC MOBILE, you always have the support to help you make your next move."},
        {"Help a Customer":"Pending","img":url+"/images/HaC.png","title":"Help a Customer","smallDesc":"The HaC (Help a Customer) Mobile App empowers all team members to take action on behalf of our customers anytime, anywhere. It provides a convenient intake method to capture customer feedback & issue details and seamlessly connect to Dell’s existing Help a Customer service and support flows.", "version":"v1.1.4","description":"The HaC (Help a Customer) Mobile App empowers all team members to take action on behalf of our customers anytime, anywhere. It provides a convenient intake method to capture customer feedback & issue details and seamlessly connect to Dell’s existing Help a Customer service and support flows."}
      ]},{"title":"Employee Productivity","values":[
        {"Engage":"Pending","img":url+"/images/Engage.png","title":"Engage","smallDesc":"Engage is a Mobile App which allows a user to view the day plan (calendar), know what meeting is happening now and quickly dial into the meeting, view attendees, or connect to the video portion on WebEx or Skype, see their current / upcoming meeting. Meetings can be filtered by a sender, Meetings are automatically flagged depending on the senders level in the organization. User will also be able to view participants' Org View and Profile.", "version":"v1.0.0","description":"Engage is a Mobile App which allows a user to view the day plan (calendar), know what meeting is happening now and quickly dial into the meeting, view attendees, or connect to the video portion on WebEx or Skype, see their current / upcoming meeting. Meetings can be filtered by a sender, Meetings are automatically flagged depending on the senders level in the organization. User will also be able to view participants' Org View and Profile."},
        {"Spaces":"Pending","img":url+"/images/Spaces.png","title":"Spaces","smallDesc":"Get to where you are going and save time with SPACES. Navigate Dell offices with live turn-by-turn directions, find hotel spaces once you arrive at the office, and meet-up with colleagues for chats, coffee, breaks or whatever else is on your work-day agenda.", "version":"v1.0.0","description":"Get to where you are going and save time with SPACES. Navigate Dell offices with live turn-by-turn directions, find hotel spaces once you arrive at the office, and meet-up with colleagues for chats, coffee, breaks or whatever else is on your work-day agenda."},
        {"Help":"Pending","img":url+"/images/Help.png","title":"Help","smallDesc":"Quickly and efficiently change your Domain/Network account password from anywhere, anytime! With HELP mobile app, you can do all that from your mobile phone", "version":"v1.0.3","description":"Quickly and efficiently change your Domain/Network account password from anywhere, anytime! With HELP mobile app, you can do all that from your mobile phone"}
      ]},{"title":"Pipeline","values":[
        {"Self Service Portal":"Pending","img":url+"/images/E2E.png","title":"Self Service Portal","smallDesc":"A portal for making mobile apps.", "version":"v1.0.0","description":"The Self Service portal is a website that enables"},
        {"Sales Dashboard":"Pending","img":url+"/images/SD.png","title":"Sales Dashboard","smallDesc":"Provides the real time statistics of operations in Sales", "version":"v1.0.5","description":"Provides the real time statistics of operations in Sales"},
        {"EZDialer":"Pending","img":url+"/images/EZDialer.png","title":"EZDialler","smallDesc":"EZ Dialer gives you a quick and easy way to join meetings from your mobile device when you’re on the go. Just tap the meeting and EZ Dialer dials the bridge number and enters the participant code.", "version":"v2.1.0","description":"EZ Dialer gives you a quick and easy way to join meetings from your mobile device when you’re on the go. Just tap the meeting and EZ Dialer dials the bridge number and enters the participant code."},
        {"Burn Notification":"Pending","img":url+"/images/BN.png","title":"Burn Notification","smallDesc":"Burn Notification App send out notification status to the user’s smart watch.", "version":"v1.0.0","description":"Burn Notification App send out notification status to the user’s smart watch."},
        {"E2E MRP":"Pending","img":url+"/images/E2E.png","title":"E2E MRP","smallDesc":"sample Description", "version":"v1.0.1","description":"This is sample description"}
      ]}]
    
    try:
        ##print("inside here");
        if request.method=="GET":
            # if 'id' in request.args:
            #     ret['id'] = request.args['id']
            # if 'name' in request.args:
            #     ret['name'] = request.args['name']
            print(ret);
            print(request.headers);
            # if request.headers['Content-Type'] == 'application/json':
            #     print("headers work my lord")
            return Response(json.dumps(ret), status=200, mimetype='application/json')
        elif request.method=="POST":
            #print(request.headers);
            print(request.get_json());
            if request.headers['Content-Type'] == 'application/json':
                content = request.get_json();
                if content['username'] == 'admin' and content['password']=='admin':
                	print("admin");
                	return '{"status":"success"}'

                elif content['username'] == 'sankar' and content['password']=='sankar@123':
                	print("sankar");
                	return '{"status":"success"}'

                elif content['username'] == 'sheenam.ohrie' and content['password']=='sheenam@123':
                	print("sheenam");
                	return '{"status":"success"}'

                elif content['username'] == 'akta.jain' and content['password']=='akta@123':
                	print("akta");
                	return '{"status":"success"}'
                
                elif content['username'] == 'mathew.basilthomas' and content['password']=='mathew@123':
                	print("mathew");
                	return '{"status":"success"}'
                else:
                	print("wrong");
                	return '{"status":"failure"}'
            else:
                return '{"status":"failure"}'
    except Exception as e:
    	print('error');
    	ret = "error"
    	return Response(json.dumps(ret),status=400,mimetype='application/json')

@app.route('/images/<path:path>')
def send_img(path):
    return send_from_directory('AppIcons',path);

# @app.route('/updateStatusApprove',methods=["POST"])
# def updateStatus():
#     print("inside here");
#     if request.method=="POST":
#         print("POST");
#         if request.headers['Content-Type'] == 'application/json':
#             print("inside headers");
#             content = request.get_json()
#             print(content);
#             for ele in ret:
#                 val=ele["values"]
#                 for row in val:
#                     print(row)
#                     if row[content['title']] == "Pending":
#                         row[content['title']] = "Approved";
#                         return '{"Success":"Approved"}'
#                     else:
#                         return '{"Success":"Already Approved"}'
#         else:
#             return '{"Failure":"failed"}'

if __name__  == '__main__':
    app.run()