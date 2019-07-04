"""
This is a Python template for Alexa to get you building skills (conversations) quickly.
"""

from __future__ import print_function


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------
def get_test_response():
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """
    session_attributes = {}
    card_title = "GetTime"
    speech_output = "Lylescenter opens from 7:00am to 3:30pm from Monday to Friday in Summer."
    reprompt_text = "I can't hear you, please say it again"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def get_name_response(intent,session):
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """
    # session_attributes = {}
    card_title = "GetName"
    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    # print(intent)
    name=intent['slots']['name']['value']
    session_attributes={'name':name.lower()}
    # print(session)
    # # print(name)
    # print (session)
    switcher={
        "stanley":"Stanley is a charming guy",
        "erick":"Erick has a fancy car",
        "sif":"sif is a doufas",
        "ravi":"Ravi is the most powerful of all the gods and he is on earth to spare mercy on humanity",
        "max":"Max is the boss",
        "sharma": "sharma is a fake mexican"
    }
    speech_output = switcher.get(name.lower(),"This person is not in the lylescenter")
    reprompt_text = "I can't hear you, please say it again"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_location_response(intent,session):
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """
    
    # session_attributes = {}
    # print("!!!!!!!!!!!!!!")
    # print(session)
    #print(session['attributes']['name'])
    card_title = "GetLocation"
    # print(intent)
    name=intent['slots']['namelocation']['value']
    # session_attributes={}
    session_attributes={'name':name.lower()}##if session_attributes is empty before this command
    # print(session)
    #print(session['attributes']['name'])
    # speech_output="HI"
    if name.lower()=="he":
        switcher={
            "stanley":"he is in the lyles center",
            "max":"he is everywhere",
            "sif":"he is in his spot",
            "ravi":"He is on mount olympus accepting prayers",
            "erick":"he is next to you"
        }
        # session_attributes={'name':session['attributes']['name']}
        speech_output =switcher.get(session['attributes']['name'],"I don't know who is he")
        session_attributes={'name':session['attributes']['name']}
    else:
        switcher={
            "stanley":"Stanley is in the lyles center",
            "max":"Max is everywhere",
            "sif":"Sif is in his spot",
            "ravi":"he is with poseidon surfing on the high tides",
            "erick":"Erick is next to you"
        }
        # session_attributes={'name':session['attributes']['name']}
        speech_output =switcher.get(name.lower(),"I never heard this person")
        # session_attributes={'name':session['attributes']['name']}
    reprompt_text = "I can't hear you, please say it again"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_job_response(intent,session):
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """
    # session_attributes = {}
    card_title = "GetJob"
    # print("!!!!!!!!!!")
    # print(intent)
    name=intent['slots']['namejob']['value']
    session_attributes={'name':name.lower()}##if session_attributes is empty before this command
    # print(name)
    # print(session)
    if name.lower()=="his" or name.lower()=="he":
        switcher={
            "stanley":"he wants to take care everyone",
            "max":"he has lots of meetings",
            "sif":"he is good at programming",
            "ravi":"he is the greatest warrior of all time",
            "erick":"he is leader in lyles center"
        }
        session_attributes={'name':session['attributes']['name']}
        speech_output =switcher.get(session['attributes']['name'],"I don't know who is he")
    else:
        switcher={
            "stanley":"Stanley wants to take everyone",
            "max":"Max has lots of meetings",
            "sif":"Sif is good at programming",
            "ravi":"Ravi is the greatest warrior of all time",
            "erick":"Erick is leader in lyles center"
        }
        speech_output =switcher.get(name.lower(),"I never heard this person")
    reprompt_text = "I can't hear you, please say it again"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to Lylescenter, how can I help you?"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "I don't know if you heard me, welcome to Lylescenter!"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_cancel_request():
    card_title = "Session Ended"
    speech_output = "you're welcome, see you later!"
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))
        
def handle_session_stop_request():
    card_title = "Session Ended"
    speech_output = "OK"
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts.
        One possible use of this function is to initialize specific 
        variables from a previous state stored in an external database
    """
    # Add additional code here as needed
    pass

    

def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    # Dispatch to your skill's launch message
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "GetTime":
        return get_test_response()
    elif intent_name=="GetName":
        return get_name_response(intent,session) 
    elif intent_name=="GetLocation":
        return get_location_response(intent,session)
    elif intent_name=="GetJob":
        return get_job_response(intent,session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.StopIntent":
        return handle_session_stop_request()
    elif intent_name == "AMAZON.CancelIntent":
        return handle_session_cancel_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("Incoming request...")
    # print(event)
    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
