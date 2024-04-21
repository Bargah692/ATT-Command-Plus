from py_tale import Py_Tale
import asyncio, json

bot = Py_Tale()

bot.config(client_id = 'your client id', # This sets your bot  credentials
            user_id = your user id, int object,
            scope_string = 'ws.group ws.group_members ws.group_servers ws.group_bans ws.group_invites group.info group.join group.leave group.view group.members group.invite server.view server.console',
            client_secret = 'your client secret',
           debug = True) # Replace with your credentials

server_id = 430116864  # Replace with the server ID you want to run the bot on.

async def on_event(event):
    global server_id


async def on_invited(data):                 # This is called everytime you get an invite to a server
    server_id = data["content"]["id"]
    print("I've been invited to group:", server_id)
    await bot.request_accept_invite(server_id)     
    print("Accepted invite to:", server_id)


async def on_commandexecuted(data):
    command = data['data']['Command']
    command = command.lower()

# Player teleport-coordinate
    if command.startswith("player teleport-coordinate "):
        parts = command.split()

        persontotp = parts[-2]
        coordtotp = parts[-1]

        await bot.send_command_console(server_id, f"player set-home {persontotp} {coordtotp}")
        await bot.send_command_console(server_id, f"player tp {persontotp} home")
        await bot.send_command_console(server_id, f"player set-home {persontotp} -690.474,129.249008,72.79")
        await bot.send_command_console(server_id, f"player message {persontotp} 'Successfully Teleported To Coordinates \n {coordtotp}!'")
        print(persontotp)

# Player overpower
    elif command.startswith("player overpower "):
        parts = command.split()

        person = parts[2]
        duration = parts[-1]

        await bot.send_command_console(server_id, f"player modify-stat {person} damage 999999 {duration}")
        await bot.send_command_console(server_id, f"player modify-stat {person} speed 2 {duration}")
        await bot.send_command_console(server_id, f"player god-mode {person}")
        await bot.send_command_console(server_id, f"player message {person} 'You Have Become Unstoppable For\n {duration} seconds!'")

# Player RemoveStats
    elif command.startswith("player removestats "):
        parts = command.split()

        person = parts[2]
                    
        Result = await bot.send_command_console(server_id, f"player detailed {person}")
        # Extracting the list of coordinates
        coordinates_list = Result["data"]["Result"]["Position"]
        coordinates = ",".join(map(str, coordinates_list))


        await bot.send_command_console(server_id, "settings changesetting server DownedStateDuration 0")
        await bot.send_command_console(server_id, f"player set-home {person} {coordinates}")
        await bot.send_command_console(server_id, f"player kill {person}")
        await asyncio.sleep(6)
        await bot.send_command_console(server_id, f"player set-home {person} -691.332,129.249008,74.268")
        await bot.send_command_console(server_id, f"player message {person} 'Stats Removed'")
        await bot.send_command_console(server_id, "settings changesetting server DownedStateDuration 60")

# Player smite
    elif command.startswith("player smite "):
        parts = command.split()

        person = parts[2]
        await bot.send_command_console(server_id, "settings changesetting server DownedStateDuration 0")
        await bot.send_command_console(server_id, 'Settings changesetting server DropAllOnDeath true')
        await bot.send_command_console(server_id, f"player kill {person}")
        await bot.send_command_console(server_id, 'Settings changesetting server DropAllOnDeath false')
        await bot.send_command_console(server_id, "settings changesetting server DownedStateDuration 60")

# Player Stun
    elif command.startswith("player stun "):
        parts = command.split()

        person = parts[2]
        duration = parts[-1]

        await bot.send_command_console(server_id, f"player modify-stat {person} damage -999999999999999999999999999999 {duration}")
        await bot.send_command_console(server_id, f"player modify-stat {person} frost 10 {duration}")
        await bot.send_command_console(server_id, f"player cripple {person} {duration}")

# Player Fling
    elif command.startswith("player fling "):
        parts = command.split()

        person = parts[2]

        Result = await bot.send_command_console(server_id, f"player detailed {person}")
        coordinates_list = Result["data"]["Result"]["Position"]
        coordinates = ",".join(map(str, coordinates_list))
        x_str, y_str, z_str = coordinates.split(',')
        x_coordinate = float(x_str)
        y_coordinate = float(y_str)
        z_coordinate = float(z_str)

        y_coordinate = float(y_coordinate) + 300

        updated_coordinates = f"{x_coordinate},{y_coordinate},{z_coordinate}"
        print(updated_coordinates)
        await bot.send_command_console(server_id, f"player set-home {person} {updated_coordinates}")
        await bot.send_command_console(server_id, f"player message {person} 'You are about to be teleported a million miles in the air in 3!' 2")
        await asyncio.sleep(2)
        await bot.send_command_console(server_id, f"player message {person} '2' 1")
        await asyncio.sleep(1)
        await bot.send_command_console(server_id, f"player message {person} '1!' 1")
        await asyncio.sleep(1)
        await bot.send_command_console(server_id, f"player tp {person} home")
        await bot.send_command_console(server_id, f"player set-home {person} -691.332,129.249008,74.268")

# Wacky Clear-inventory
    elif command.startswith("wacky clear-inventory "):
        parts = command.split()

        person = parts[-1]

        pockets_list = await bot.send_command_console(server_id, f"player inventory {person}")
        print(pockets_list)

        pocket_items = [item for item in pockets_list['data']['Result'][0]['All'] if item and item['Name'] != 'Hoarder Bag(Clone)' and item['Name'] != 'Bag(Clone)']

        for item in pocket_items:
            await bot.send_command_console(server_id, f"wacky destroy {item['Identifier']}")
            await bot.send_command_console(server_id, f"player message {person} 'deleted {item['Name']}'")

# Trade atm withdrawl
    elif command.startswith("trade atm withdrawl "):
        parts = command.split()

        amount = parts[-1]
        person = parts[-2]

        await bot.send_command_console(server_id, f"trade atm add {person} -{amount}")

# Player Curse
    elif command.startswith("player curse "):
        parts = command.split()
        person = parts[-1]
        await bot.send_command_console(server_id, f"time set night")
        await asyncio.sleep(5)
        await bot.send_command_console(server_id, f"player setstat {person} nightmare 5")
                                       




        





        




async def main():
    asyncio.create_task(bot.run())                  # Runs the bot
    print("Logging in...")
    await bot.wait_for_ws()          

    await bot.main_sub("subscription/me-group-invite-create/" + str(bot.user_id), on_invited) # Tells you when you get invited

    await bot.create_console(430116864)             # Replace the id in here with the server you will use this bot in.

    await bot.console_sub("CommandExecuted", on_commandexecuted, server_id=server_id)       # Also replace the id in here with the server you will use this bot with

    print("Successfully Logged in! \n Everything is ready!")

    while True:
        await asyncio.sleep(1) 

asyncio.run(main())
