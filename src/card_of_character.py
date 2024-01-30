from nicegui import ui
from ex4nicegui.reactive import rxui
from ex4nicegui import to_ref,ref_computed,effect
from Caract import *
from up_down_change import *

def card_of_character(character:Caract):
    with ui.card().tight().style('overflow: auto; min-height: 30em; max-height: 40em; min-width: 20em; max-width: 20em;').classes('justify-center items-center'):
        with ui.row().classes('justify-center items-center'):
            hp = to_ref(10)
            ui.button('-',on_click=lambda:change(hp,'-'))
            ui.label("HP")
            rxui.label(hp)
            ui.button('+',on_click=lambda:change(hp,'+'))

            energy = to_ref(0)
            ui.button('-',on_click=lambda:change(energy,'-'))
            ui.label("Energy")
            rxui.label(energy)
            ui.button('+',on_click=lambda:change(energy,'+',character.energy))

        ui.image(character.pic)
        with ui.dialog() as dialog,ui.card():
            with ui.column():
                for key in character.skill.keys():
                    ui.label(key+":")
                    ui.label(character.skill[key])
                ui.button('Close', on_click=dialog.close)
        with ui.card_section():
            with ui.row():
                ui.button(character.name,on_click=dialog.open)
                ui.select(["none","fire","water","wind","thunder","grass","ice"],value="none")
            buff = ui.label()