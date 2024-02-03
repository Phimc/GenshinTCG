from nicegui import ui
from ex4nicegui.reactive import rxui
from ex4nicegui import to_ref,ref_computed,effect

from up_down_change import *
from card_of_character import *
from load_characters_from import *

import library_page

@ui.page('/Main')
def create():
    with ui.header(elevated=True).style('backgroundcolor: #3874c8').classes('items-center justify-between') as header:
        ui.button(on_click=lambda:left_drawer.toggle(), icon='menu').props('flat color=white')
        ui.label('Main Page')

    with ui.left_drawer(fixed=False).classes('bg-blue-100') as left_drawer:
        ui.label('Side menu')  
        ui.link('Main Page','/Main')
        ui.link('library','/Library')
        ui.link('Gallery')

    with ui.tabs().classes('w-full') as tabs:
        one = ui.tab('Friends')
        two = ui.tab('Characters')
        thr = ui.tab('Summons')

    def card_of_friends():
        with ui.card().style('overflow: auto; min-height: 20em; max-height: 20em; min-width: 20em; max-width: 20em;').classes(' justify-around items-center'):
            cou = to_ref(0)
            rxui.label(cou).style( ' font-weight: bold;font-size: 48px;text-align: center;').classes('full-width ')

            with ui.row().classes('items-center justify-between'):
                ui.button(icon='+',on_click=lambda:change(cou,'+'))
                ui.button(icon='-',on_click=lambda:change(cou,'-'))

    def card_of_summons():
        with ui.card().style('overflow: auto; min-height: 20em; max-height: 20em; min-width: 20em; max-width: 20em;').classes(' justify-around items-center'):
            cou = to_ref(0)
            rxui.label(cou).style( ' font-weight: bold;font-size: 48px;text-align: center;').classes('full-width ')

            with ui.row().classes('items-center justify-between'):
                ui.button(icon='+',on_click=lambda:change(cou,'+'))
                ui.button(icon='-',on_click=lambda:change(cou,'-'))

    with ui.tab_panels(tabs).classes('w-full'):
        with ui.tab_panel(one):
            with ui.row().classes('full-width row wrap justify-center items-center'):
                with ui.grid(rows=2,columns=2):
                    for i in range(4):
                        card_of_friends()

        with ui.tab_panel(two):
            with ui.row().classes('full-width row wrap justify-center items-center'):
                chosen = load_characters_from('./COL/characters.json')
                for someone in chosen:
                    card_of_character(someone)

        with ui.tab_panel(thr):
            with ui.row().classes('full-width row wrap justify-center items-center'):
                with ui.grid(rows=2,columns=2):
                    for i in range(4):
                        card_of_summons()

create()
#library_page.create()
ui.run(title='Genshin TCG')