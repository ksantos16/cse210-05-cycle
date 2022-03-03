from game.scripting.action import Action

# ksantos16
# TODO: Implement MoveActorsAction class here!


class MoveActorsAction(Action):
    # Override the execute(cast, script) method as follows:

    def execute(self, cast, script):
        # 1) get all the actors from the cast
        actors = cast.get_all_actors()
        # 2) loop through the actors
        for actors in actors:
            # 3) call the move_next() method on each actor
            actors.move_next()
