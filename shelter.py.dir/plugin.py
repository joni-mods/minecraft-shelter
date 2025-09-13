from org.bukkit.entity import Player
from org.bukkit.block import BlockFace
from org.bukkit.block.data import BlockData
from org.bukkit.block.data import Bisected
from org.bukkit.block.data.type import Door
from org.bukkit.block.data.type import Bed


class ShelterPlugin(PythonPlugin):

    def onEnable(self):
        pass

    @staticmethod
    def onCommand(sender, command, label, args):
        player_position = sender.getLocation()
        dir_unit_vector = player_position.getDirection()
        target_position = player_position.add(dir_unit_vector.multiply(10))

        # build outer walls
        ShelterPlugin.buildCube(sender, target_position, 4, 6, 6, bukkit.Material.STONE)

        # build door
        target_position.setX(target_position.getX() + 1)
        target_position.setY(target_position.getY() + 1)
        ShelterPlugin.buildDoor(sender, target_position, bukkit.Material.DARK_OAK_DOOR, bukkit.Material.JUNGLE_DOOR)

        # build inner space
        target_position.setZ(target_position.getZ() + 1)
        ShelterPlugin.buildCube(sender, target_position, 2, 4, 4, bukkit.Material.AIR)

        # build the torch
        target_position.setZ(target_position.getZ() + 3)
        target_position.setY(target_position.getY() + 1)
        ShelterPlugin.buildTorch(sender, target_position)

        # build the bed
        target_position.setX(target_position.getX() + 2)
        target_position.setY(target_position.getY() - 1)
        ShelterPlugin.buildBed(sender, target_position)

        return True

    @staticmethod
    def buildCube(player, target_position, height, width, length, material):
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

    @staticmethod
    def buildDoor(player, target_position, material_lower, material_upper):
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

    @staticmethod
    def buildBed(player, target_position):
        position = target_position.clone()
        world = player.getWorld()
        
        bed_footer_block = world.getBlockAt(position)
        bed_footer_block.setType(bukkit.Material.RED_BED)
        bed_footer_block_data = bed_footer_block.getBlockData()
        bed_footer_block_data.setPart(Bed.Part.FOOT)
        bed_footer_block_data.setFacing(BlockFace.EAST)
        bed_footer_block.setBlockData(bed_footer_block_data)
        
        bed_header_block = bed_footer_block.getRelative(BlockFace.EAST)
        bed_header_block.setType(bukkit.Material.RED_BED, False)
        bed_header_block_data = bed_footer_block.getBlockData()
        bed_header_block_data.setPart(Bed.Part.HEAD)
        bed_header_block_data.setFacing(BlockFace.EAST)
        bed_header_block.setBlockData(bed_header_block_data)
        
        return True        

    @staticmethod
    def buildTorch(player, target_position):
        position = target_position.clone()
        world = player.getWorld()

        torch_block = world.getBlockAt(position)
        torch_block.setType(bukkit.Material.WALL_TORCH, False)
        torch_block_data = torch_block.getBlockData()
        torch_block_data.setFacing(BlockFace.EAST)
        torch_block.setBlockData(torch_block_data)

        return True
