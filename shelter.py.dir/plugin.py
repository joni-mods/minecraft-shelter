class ShelterPlugin(PythonPlugin):
    def onEnable(self):
        pass

    def onCommand(self, sender, command, label, args):
        player_position = sender.getLocation()                      # Get the player's current position
        dir_unit_vector = player_position.getDirection()            # Get the player's direction unit vector
        target_position = player_position.add(dir_unit_vector)      # Calculate the target position

        world = sender.getWorld()                                   # Get the world object
        block = world.getBlockAt(target_position)                   # Get the block at the target position
        block.setType(bukkit.Material.SLIME_BLOCK)                  # Set the block type to gold

        return True
