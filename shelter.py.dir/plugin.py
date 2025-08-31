class ShelterPlugin(PythonPlugin):
    def onEnable(self):
        pass

    def onCommand(self, sender, command, label, args):
        player_position = sender.getLocation()                              # Get the player's current position
        dir_unit_vector = player_position.getDirection()                    # Get the player's direction unit vector
        target_position = player_position.add(dir_unit_vector.multiply(15)) # Calculate the target position

        ShelterPlugin.buildCube(self, sender, target_position,4, 6,6, bukkit.Material.STONE)
        target_position.setX(target_position.getX() + 1)
        target_position.setY(target_position.getY() + 1)
        target_position.setZ(target_position.getZ() + 1)
        ShelterPlugin.buildCube(self, sender, target_position,2, 4,4, bukkit.Material.AIR)

        return True

    def buildCube(self, player, target_position, height, width, length, material):
        position = target_position.clone()
        world = player.getWorld()                                           # Get the world object

        xStart = position.getX()
        yStart = position.getY()
        zStart = position.getZ()

        for x in range(0, length):
            position.setX(xStart + x)
            for y in range(0, height):
                position.setY(yStart + y)
                for z in range(0, width):
                    position.setZ(zStart + z)
                    block = world.getBlockAt(position)
                    block.setType(material)

        return True
