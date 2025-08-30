class ShelterPlugin(PythonPlugin):
    def onEnable(self):
        pass

    def onCommand(self, sender, command, label, args):
        ShelterPlugin.buildCube(self, sender, 5, 10,10, bukkit.Material.STONE)

        return True

    def buildCube(self, player, height, width, length, material):
        player_position = player.getLocation()                      # Get the player's current position
        dir_unit_vector = player_position.getDirection()            # Get the player's direction unit vector
        target_position = player_position.add(dir_unit_vector)      # Calculate the target position

        world = player.getWorld()                                   # Get the world object

        xStart = target_position.getX()
        yStart = target_position.getY()
        zStart = target_position.getZ()

        for x in range(0, length):
            target_position.setX(xStart + x)
            for y in range(0, height):
                target_position.setY(yStart + y)
                for z in range(0, width):
                    target_position.setZ(zStart + z)
                    block = world.getBlockAt(target_position)
                    block.setType(material)

        return True
