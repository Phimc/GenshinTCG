class Caract:
    def __init__(self,props:dict) -> None:
        self.name=props['character_name']
        self.pic =props['picture_path']
        self.skill=props['skill_describe']
        self.effect=props['effect_describe']
        self.energy=props['energy']
        pass