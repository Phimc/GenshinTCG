from nicegui import ui
from ex4nicegui.reactive import rxui
from ex4nicegui import to_ref,ref_computed,effect
import json

@ui.page('/Library')
def create():
    with ui.header(elevated=True).style('backgroundcolor: #3874c8').classes('items-center justify-between') as header:
        ui.button(on_click=lambda:left_drawer.toggle(), icon='menu').props('flat color=white')
        with ui.tabs().classes() as tabs:
            one = ui.tab('Characters')
            two = ui.tab('Friends')
            thr = ui.tab('Equipments')
            four = ui.tab('Other')
        ui.label('Library')
        
    with ui.right_drawer(fixed=True,bordered=True) as right_drawer:
        ui.label('details')


    with ui.left_drawer(fixed=False,elevated=True).classes('bg-blue-100') as left_drawer:
        ui.label('Side menu')  
        ui.link('Main Page','/Main')
        ui.link('library','/Library')
        ui.link('Gallery')

    class Action_card:
        def __init__(self,props:dict) -> None:
            self.name = props["name"]
            self.label= props["label"]
            self.pic = props["picture_path"]
            self.eff = props["effect"]
            pass


    def load_cards_from(file_path):
        cards_library = []
        fp = open(file_path,'r',encoding='utf-8')
        cards_library_json = json.load(fp)
        for item in cards_library_json:
            cards_library.append(Action_card(item))
        fp.close()
        return cards_library

    def detail_on_right_drawer(action_card:Action_card):
        right_drawer.clear()
        with right_drawer:
            ui.image(action_card.pic)
            ui.label(action_card.eff)
        return 0
    cards_lib = load_cards_from('collection\cards_library.json')


    def a_card(action_card:Action_card=0):
        with ui.button(on_click=lambda:detail_on_right_drawer(action_card)).style("overflow: auto; min-height: 25em; max-height: 25em; min-width: 14em; max-width: 14em;"):
            ui.image(action_card.pic)
            ui.label(action_card.name)
        return 0

    with ui.tab_panels(tabs).classes('w-full'):
        with ui.tab_panel(one):
            pass
        with ui.tab_panel(two):
            ui.label('Friends')   
            with ui.grid(columns=2,rows=30).classes('full-width row wrap'):
                for card in cards_lib:
                    if card.label == "Friend":
                        a_card(card)     
        with ui.tab_panel(thr):
            ui.label('Equipments')
            with ui.grid(columns=2,rows=30).classes('full-width row wrap'):
                for card in cards_lib:
                    if card.label == "Equipment":
                        a_card(card)  
        with ui.tab_panel(four):
            ui.label("Other")
            with ui.grid(columns=2,rows=30).classes('full-width row wrap'):
                for card in cards_lib:
                    if card.label == "Other":
                        a_card(card)  