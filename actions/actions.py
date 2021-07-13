# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ActionService(Action):

    def name(self) -> Text:
        return "main_action_service"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons = [
            {"payload":'/jetski{"content_type":"jetski"}', "title":"Jetski"},
            {"payload":'/towablerides{"content_type":"towable_rides"}', "title":"Towable Rides"},
            {"payload":'/flyboards{"content_type":"fly_boards"}', "title":"Fly Boards"},
            {"payload":'/kayaks{"content_type":"kayaks"}', "title":"Kayaks"},
            {"payload":'/paddleboard{"content_type":"paddle_board"}', "title":"Stand Up Paddle Board"},
            {"payload":'/wakeboarding{"content_type":"wake_boarding"}', "title":"Wake Boarding"},
            {"payload":'/waterskiing{"content_type":"water_skiing"}', "title":"Water Skiing"},
            {"payload":'/wakesurfing{"content_type":"wake_surfing"}', "title":"Wake Surfing"},
            {"payload":'/kitesurfing{"content_type":"kite_surfing"}', "title":"Kite Surfing"},
            {"payload":'/discoverdive{"content_type":"discover_dive"}', "title":"Discover Dive"},
            {"payload":'/juniorpadi{"content_type":"junior_padi"}', "title":"Junior PADI Courses"},
            {"payload":'/adultpadi{"content_type":"adult_padi"}', "title":"Adult PADI Courses"},
            {"payload":'/divingexcursions{"content_type":"diving_excursions"}', "title":"Diving Excursions"},
            {"payload":'/snorkling{"content_type":"snorkling"}', "title":"Pearl Driver or Snorkling"},
            {"payload":'/discoversailing{"content_type":"discover_sailing"}', "title":"Discover Sailing"},
            {"payload":'/adultsailing{"content_type":"adult_sailing"}', "title":"Adult Sailing"},
            {"payload":'/youthsailing{"content_type":"youth_sailing"}', "title":"Youth Sailing"},
            {"payload":'/powerboat{"content_type":"power_boat"}', "title":"Power Boat"},
            {"payload":'/sailingboatrentals{"content_type":"sailing_boat_rentals"}', "title":"Sailing Boat Rentals"},
            {"payload":'/boatcharters{"content_type":"boat_charters"}', "title":"Boat Charters"},
            {"payload":'/embraceadventure{"content_type":"embrace_adventure"}', "title":"Embrace Adventure"},
        ]

        dispatcher.utter_message(text="How would you like to learn with?",buttons=buttons)

        return []


class ActionLocationService(Action):

    def name(self) -> Text:
        return "location_service"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons = [
            {"payload":'/location_service{"location_type":"Al Bandar Resort"}', "title":"Al Bandar Resort"},
            {"payload":'/location_service{"location_type":"The Art Hotel & Resorts"}', "title":"The Art Hotel & Resorts"},
            {"payload":'/location_service{"location_type":"The Grove Resort"}', "title":"The Grove Resort"},
            {"payload":'/location_service{"location_type":"Bahrain Yacht Club"}', "title":"Bahrain Yacht Club"},
        ]
        content_type = tracker.get_slot('content_type')
        dispatcher.utter_message(text=f"Where would you like to book for {content_type}?",buttons=buttons)

        return []

class ActionLocationConfirmation(Action):

    def name(self) -> Text:
        return "location_confirmation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        service_type = tracker.get_slot('content_type')
        loc_type = tracker.get_slot('location_type')

        dispatcher.utter_message(text=f"I am confirming you booking for Site {loc_type} for {service_type}")

        return []

class ActionTowableridesTypeService(Action):

    def name(self) -> Text:
        return "towablerides_service_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons = [
            {"payload":'/towablerides_service{"towablerides_type":"Banana Boat"}', "title":"Banana Boat"},
            {"payload":'/towablerides_service{"towablerides_type":"Subwing"}', "title":"Subwing"},
        ]
        content_type = tracker.get_slot('content_type')
        dispatcher.utter_message(text=f"Select {content_type} section type?",buttons=buttons)

        return []

class ActionTowableridesTypeConfirmation(Action):

    def name(self) -> Text:
        return "towablerides_service_conformation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        towablerides_type = tracker.get_slot('towablerides_type')

        dispatcher.utter_message(text=f"You have selected {towablerides_type} in Towable Rides Section.")

        return []