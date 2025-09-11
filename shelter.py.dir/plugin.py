class ShelterPlugin(PythonPlugin):

    def onEnable(self):
        pass

    def onCommand(self, sender, command, label, args):
        player_position = sender.getLocation()
        dir_unit_vector = player_position.getDirection()
        target_position = player_position.add(dir_unit_vector.multiply(10))

        # build outer walls
        ShelterPlugin.buildCube(self, sender, target_position, 4, 6, 6, bukkit.Material.STONE)

        # build door
        target_position.setX(target_position.getX() + 1)
        target_position.setY(target_position.getY() + 1)
        ShelterPlugin.buildDoor(self, sender, target_position, bukkit.Material.DARK_OAK_DOOR,
                                bukkit.Material.JUNGLE_DOOR)

        # build inner space
        target_position.setZ(target_position.getZ() + 1)
        ShelterPlugin.buildCube(self, sender, target_position, 2, 4, 4, bukkit.Material.AIR)

        return True

    def buildCube(self, player, target_position, height, width, length, material):
        position = target_position.clone()
        world = player.getWorld()

        x_start = position.getX()
        y_start = position.getY()
        z_start = position.getZ()

        for x in range(0, length):
            position.setX(x_start + x)
            for y in range(0, height):
                position.setY(y_start + y)
                for z in range(0, width):
                    position.setZ(z_start + z)
                    block = world.getBlockAt(position)
                    block.setType(material)

        return True

    def buildDoor(self, player, target_position, material_lower, material_upper):
        position = target_position.clone()
        world = player.getWorld()

        door_lower = world.getBlockAt(position)
        door_lower.setType(material_lower)
        door_lower_data = door_lower.getBlockData()
        door_lower_data.setHalf(Bisected.Half.BOTTOM)
        door_lower_data.setFacing(BlockFace.SOUTH)
        door_lower.setBlockData(door_lower_data)

        position.setY(position.getY() + 1)
        door_upper = world.getBlockAt(position)
        door_upper.setType(material_upper, False)
        door_upper_data = door_upper.getBlockData()
        door_upper_data.setHalf(Bisected.Half.TOP)
        door_upper_data.setFacing(BlockFace.SOUTH)
        door_upper.setBlockData(door_upper_data)

        return True
