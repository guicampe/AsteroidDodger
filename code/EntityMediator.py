from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player


class EntityMediator:

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        if isinstance(ent1, Enemy) and isinstance(ent2, Player):
            enemy, player = ent1, ent2
        elif isinstance(ent1, Player) and isinstance(ent2, Enemy):
            enemy, player = ent2, ent1
        else:
            return

        if enemy.rect.colliderect(player.rect):
            enemy.health -= player.damage
            player.health -= enemy.damage
            enemy.last_dmg = player.name
            player.last_dmg = enemy.name


    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg != 'Player':
            for ent in entity_list:
                if ent.name == 'Player':
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)
