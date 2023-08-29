# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCustomRainfallResponse(Action):
    def name(self) -> Text:
        return "action_custom_rainfall_response"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        latest_intent = tracker.latest_message['intent']['name']
        
        # Check the latest intent and provide appropriate responses
        if latest_intent == 'ask_rainfall_deviation_2017':
            response = "Here's the rainfall deviation for 2017."
        elif latest_intent == 'ask_rainfall_actual_2018':
            response = "Here's the actual rainfall for 2018."
        elif latest_intent == 'ask_rainfall_normal_2018':
            response = "Here's the normal rainfall for 2018."
        elif latest_intent == 'ask_rainfall_deviation_2018':
            response = "Here's the rainfall deviation for 2018."
        elif latest_intent == 'ask_rainfall_actual_2019':
            response = "Here's the actual rainfall for 2019."
        elif latest_intent == 'ask_rainfall_normal_2019':
            response = "Here's the normal rainfall for 2019."
        elif latest_intent == 'ask_rainfall_deviation_2019':
            response = "Here's the rainfall deviation for 2019."
        elif latest_intent == 'ask_rainfall_actual_2020':
            response = "Here's the actual rainfall for 2020."
        elif latest_intent == 'ask_rainfall_normal_2020':
            response = "Here's the normal rainfall for 2020."
        elif latest_intent == 'ask_rainfall_actual_2021':
            response = "Here's the actual rainfall for 2021."
        elif latest_intent == 'ask_rainfall_normal_2021':
            response = "Here's the normal rainfall for 2021."
        elif latest_intent == 'ask_rainfall_deviation_2021':
            response = "Here's the rainfall deviation for 2021."
        elif latest_intent == 'ask_rainfall_actual_cumulative':
            response = "Here's the actual cumulative rainfall."
        elif latest_intent == 'ask_rainfall_normal_cumulative':
            response = "Here's the normal cumulative rainfall."
        elif latest_intent == 'ask_rainfall_deviation_cumulative':
            response = "Here's the cumulative rainfall deviation."
        elif latest_intent == 'ask_rainfall_actual_2014':
            response = "Here's the actual rainfall for 2014."
        elif latest_intent == 'ask_rainfall_normal_2014':
            response = "Here's the normal rainfall for 2014."
        elif latest_intent == 'ask_rainfall_deviation_2014':
            response = "Here's the rainfall deviation for 2014."
        elif latest_intent == 'ask_rainfall_actual_2015':
            response = "Here's the actual rainfall for 2015."
        elif latest_intent == 'ask_rainfall_normal_2015':
            response = "Here's the normal rainfall for 2015."
        elif latest_intent == 'ask_rainfall_deviation_2015':
            response = "Here's the rainfall deviation for 2015."
        elif latest_intent == 'ask_rainfall_actual_2016':
            response = "Here's the actual rainfall for 2016."
        elif latest_intent == 'ask_rainfall_normal_2016':
            response = "Here's the normal rainfall for 2016."
        elif latest_intent == 'ask_rainfall_deviation_2016':
            response = "Here's the rainfall deviation for 2016."
        else:
            response = "I'm not sure how to respond to that affirmation."

        dispatcher.utter_message(text=response)

        return []

class ActionAskRainfallDeviation2017(Action):
    def name(self) -> Text:
        return "action_ask_rainfall_deviation_2017"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Your logic to fetch and provide rainfall deviation for 2017
        response = "The rainfall deviation for 2017 is..."
        dispatcher.utter_message(text=response)
        return []

class ActionAskRainfallActual2018(Action):
    def name(self) -> Text:
        return "action_ask_rainfall_actual_2018"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "The actual rainfall for 2018 is..."
        dispatcher.utter_message(text=response)
        return []

class ActionAskRainfallNormal2018(Action):
    def name(self) -> Text:
        return "action_ask_rainfall_normal_2018"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "The normal rainfall for 2018 is..."
        dispatcher.utter_message(text=response)
        return []

class ActionAskRainfallNormal2018(Action):
    def name(self) -> Text:
        return "action_ask_rainfall_normal_2018"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "The normal rainfall for 2018 is..."
        dispatcher.utter_message(text=response)
        return []

class ActionAskRainfallDeviation2018(Action):
    def name(self) -> Text:
        return "action_ask_rainfall_deviation_2018"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "The rainfall deviation for 2018 is..."
        dispatcher.utter_message(text=response)
        return []

class ActionAskRainfallActual2019(Action):
    def name(self) -> Text:
        return "action_ask_rainfall_actual_2019"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "The actual rainfall for 2019 is..."
        dispatcher.utter_message(text=response)
        return []

class ActionAskRainfallNormal2019(Action):
    def name(self) -> Text:
        return "action_ask_rainfall_normal_2019"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "The normal rainfall for 2019 is..."
        dispatcher.utter_message(text=response)
        return []

class ActionAskRainfallDeviation2019(Action):
    def name(self) -> Text:
        return "action_ask_rainfall_deviation_2019"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "The rainfall deviation for 2019 is..."
        dispatcher.utter_message(text=response)
        return []

class ActionAskRainfallActual2020(Action):
    def name(self) -> Text:
        return "action_ask_rainfall_actual_2020"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "The actual rainfall for 2019 is..."
        dispatcher.utter_message(text=response)
        return []

class ActionAskRainfallNormal2020(Action):
    def name(self) -> Text:
        return "action_ask_rainfall_normal_2020"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "The normal rainfall for 2020 is..."
        dispatcher.utter_message(text=response)
        return []
        
class ActionAskRainfallActual2021(Action):
    def name(self) -> Text:
        return "action_ask_rainfall_actual_2021"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "The actual rainfall for 2021 is..."
        dispatcher.utter_message(text=response)
        return []
               
class ActionAskRainfallNormal2021(Action):
    def name(self) -> Text:
        return "action_ask_rainfall_normal_2021"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "The normal rainfall for 2021 is..."
        dispatcher.utter_message(text=response)
        return []               
        
class ActionAskRainfallDeviation2021(Action):
    def name(self) -> Text:
        return "action_ask_rainfall_deviation_2021"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "The rainfall deviation for 2021 is..."
        dispatcher.utter_message(text=response)
        return []

class ActionAskRainfallActualCumulative(Action):
    def name(self) -> Text:
        return "action_ask_rainfall_actual_cumulative"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "The actual cumulative rainfall is..."
        dispatcher.utter_message(text=response)
        return []
        
class ActionAskRainfallNormalCumulative(Action):
    def name(self) -> Text:
        return "action_ask_rainfall_normal_cumulative"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "The normal cumulative rainfall is..."
        dispatcher.utter_message(text=response)
        return []
                
class ActionAskRainfallDeviationCumulative(Action):
    def name(self) -> Text:
        return "action_ask_rainfall_deviation_cumulative"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "The cumulative rainfall deviation is..."
        dispatcher.utter_message(text=response)
        return []
                                
class ActionAskRainfallActual2014(Action):
    def name(self) -> Text:
        return "action_ask_rainfall_actual_2014"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "The actual rainfall for 2014 is..."
        dispatcher.utter_message(text=response)
        return []
                 
class ActionAskRainfallNormal2014(Action):
    def name(self) -> Text:
        return "action_ask_rainfall_normal_2014"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "The normal rainfall for 2014 is..."
        dispatcher.utter_message(text=response)
        return []                 
        
class ActionAskRainfallDeviation2014(Action):
    def name(self) -> Text:
        return "action_ask_rainfall_deviation_2014"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "The rainfall deviation for 2014 is..."
        dispatcher.utter_message(text=response)
        return [] 
        
class ActionAskRainfallActual2015(Action):
    def name(self) -> Text:
        return "action_ask_rainfall_actual_2015"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "The actual rainfall for 2015 is..."
        dispatcher.utter_message(text=response)
        return []         
        
class ActionAskRainfallNormal2015(Action):
    def name(self) -> Text:
        return "action_ask_rainfall_normal_2015"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "The normal rainfall for 2015 is..."
        dispatcher.utter_message(text=response)
        return []                 
        
class ActionAskRainfallDeviation2015(Action):
    def name(self) -> Text:
        return "action_ask_rainfall_deviation_2015"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "The rainfall deviation for 2015 is..."
        dispatcher.utter_message(text=response)
        return []           
        
class ActionAskRainfallActual2016(Action):
    def name(self) -> Text:
        return "action_ask_rainfall_actual_2016"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "The actual rainfall for 2016 is..."
        dispatcher.utter_message(text=response)
        return []        
        
class ActionAskRainfallNormal2016(Action):
    def name(self) -> Text:
        return "action_ask_rainfall_normal_2016"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "The normal rainfall for 2016 is..."
        dispatcher.utter_message(text=response)
        return []                
        
class ActionAskRainfallDeviation2016(Action):
    def name(self) -> Text:
        return "action_ask_rainfall_deviation_2016"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "The rainfall deviation for 2016 is..."
        dispatcher.utter_message(text=response)
        return []        