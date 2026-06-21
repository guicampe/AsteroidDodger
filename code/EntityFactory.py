from code.Background import Background
from code.Const import WIN_WIDTH, BACKGROUND_SCENES


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0), scene: int = 1):
        match entity_name:
            case 'Bg':
                list_bg = []
                for bg_name in BACKGROUND_SCENES[scene]:
                    list_bg.append(Background(bg_name, (0, 0)))
                    list_bg.append(Background(bg_name, (WIN_WIDTH, 0)))
                return list_bg