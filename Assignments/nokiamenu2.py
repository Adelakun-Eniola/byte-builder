menu_option = """
        1 -> PhoneBook
	2 -> Messages
	3 -> Chat
	4 -> Call
	5 ->Tones
	6 ->Settings
	7 -> Call Divert
	8 -> Games
	9 -> Calculator
	10 -> Reminders
	11 -> Clock
	12 -> Profiles
	13 -> SIM Services

"""
print(menu_option)
user_input = int(input("Enter A Number:"))

match user_input:
    case 1:
        print("PhoneBook")
        menu_option1 = '''
                1.Search
                    2. Service No
                    3. Add Name
                    4. Erase
                    5. Edit
                    6. Assign Tone
                    7. Send b'card
                    8. Option
                    9. Speed Dials
                    10. Voice Tags
                '''
        print(menu_option1)

        sub_option_one = int(input("Enter An Option:"))
        match sub_option_one:
            case 1:
                print("Search")
            case 2:
                print("Service Nos")
            case 3:
                print("Add Name")
            case 4:
                print("Erase")
            case 5:
                print("Edit")
            case 6:
                print("Assign Tone")
            case 7:
                print("Send b'card")
            case 8:
                print("Option")
                optionfor8 = '''
                    1. Types Of View
                    2. Memory Status
                '''
                print(optionfor8)
                suboptiononecase8 = int(input("Enter A SUb Option:"))
                if suboptiononecase8 == 1:
                    print("Types Of Views")
                else:
                    print("Memory Status")
    
            
    case 2:
        print("Messages")
        menu_option2 = '''
                1.Write Messages
		2.Inbox
		3.Outbox
		4.Picture messages
		5.Templates
		6.Smileys
		7.Message settings
		8.Info Service
		9.Voice Mailbox Number
		10. Service Command

        '''
        print(menu_option2)
        option_two = int(input("Enter An Option:"))
        match option_two:
            case 1:
                print("Write Messages")
            case 2:
                print("Inbox")
            case 3:
                print("Outbox")
            case 4:
                print("Picture Messages")
            case 5:
                print("Template")
            case 6:
                print("Smileys")
            case 7:
                print("Message Settings")
                sub_option_seven = '''
                1.Set
                2.Common
                '''
                print(sub_option_seven)

                option_seven_input = int(input("Enter An Option:"))

                match option_seven_input:
                    case 1:
                        print (" 1. Message Centre Number")
                        print (" 2. Message Sent As")
                        print (" 3. Message Validity")
                        option_sevenforone = int(input("Enter An Option:"))
                        match option_sevenforone:
                            case 1:
                                print("Message Centre Number")
                            case 2:
                                print("Message Sent As")
                            case 3:
                                print("Message Validity")
                    case 2:
                        print (" 1. Delivery Reports")
                        print (" 2. Reply Via Same Centre")
                        print (" 3.Character Support")
                        option_sevenfortwo = int(input("Enter An Option:"))
                        match option_sevenfortwo:
                            case 1:
                                print("Delivery Reports")
                            case 2:
                                print("Reply Via Same Centre")
                            case 3:
                                print("Character Support")

            case 8:
                print("Info Service")
            case 9:
                print("Voice Mailbox Number")
            case 10:
                print("Service Command")

    case 3: print("Chat")

    case 4:
        numberfour = '''
        1.Missed Calls
	2.Received Calls
	3.Dialled Numbers
	4.Erase Recent Call Lists
	5.Show Call Duration
	6.Show call costs
        7.Call cost settings
	8.Prepaid credit
        '''
        print(numberfour)
        number_four_option = int(input("Enter An Option Here:"))
        match number_four_option:
            case 1: print("Missed Calls")
            case 2: print("Received Calls")
            case 3: print("Dialled NUmber")
            case 4: print("Erase Recent Call Lists")
            case 5:
                numberfive_options = '''
                    1.Last Call Duration
                    2.All Calls Duration
                    3.Received Calls' Duration
                    4.Dialled Calls' Duration
                    5.Clear Timer
                    '''
                print(numberfive_options)
                numberfive_mainfour = int(input("Choose Please"))
                match numberfive_mainfour:
                        case 1: print("Last Call Duration")
                        case 2: print("All Calls Duration")
                        case 3: print("Received Calls' Duration")
                        case 4: print("Dialled Calls' Duration")
                        case 5: print("Clear Timer")
            case 6:
                call_cost_options = '''
                    1.Last Call Cost
                     2.All calls cost
                     3.Clear counters
                '''
                print(call_cost_options)
                menusix_optionfour = int(input("Choose: "))
                match menusix_optionfour:
                    case 1: print("Last Call Cost")
                    case 2: print("All Call Cost")
                    case 3: print("Clear Counter")

            case 7:
                call_cost_settings = '''
                1.Call cost limit
		2. Show costs in
                '''
                print (call_cost_settings)
                menuseven_optionfour = int(input("Choose: "))
                match menuseven_optionfour:
                    case 1: print("Call cost limit")
                    case 2: print("Show costs in")

    case 5:
        menufortones = """
            1.Ringing tone
            2.Ringing volume
            3.Incoming call alert
            4.Composer
            5.Message alert tone
            6.Keypad tones
            7.Warning and game tones
            8.Keypad tones
            9.Screen saver
            """
        print(menufortones)
        menufive = int(input("Choose: "))
        match menufive:
            case 1: print("Ringing tone")
            case 2: print("Ringing volume")
            case 3: print("Incoming call alert")
            case 4:print("Composer")
            case 5:print("Message alert tone")
            case 6: print("Keypad tones")
            case 7:print("Warning and game tones")
            case 8: print("Keypad tones")
            case 9: print("Screen saver")

    case 6:
        menusix = """
	    1.Call settings
	    2.Phone settings
	    3.Security settings
	    4. Restore factory settings
        """
        print(menusix)
        newMenu6 = int(input("Choose: "))
        match newMenu6:
            case 1:
                subMenuSix = """
			1.Automatic redial
			2.Speed dialling
			3.Call waiting options
			4.Own number sending
			5. Phone line in use
			6.Automatic answer
					"""
                print(subMenuSix)
                optionsix_optionone = int(input("Choose: "))
                match optionsix_optionone:
                    case 1:print("Automatic redial")
                    case 2:print("Speed dialling")
                    case 3:print("Call Waiting Options")
                    case 4:print("Own Number Sending")
                    case 5:print("Phone LIne In Use")
                    case 6:print("Automatic answer")

            case 2:
                subMenuSix2 = """ 
			1. Language
			2. Cell info display
			3. Welcome note
			4. Network selection
			5. Lights
			6. Confirm SIM service actions
			"""
                print(subMenuSix2)
                optionsix_optiontwo = int(input("Choose: "))
                match optionsix_optiontwo:
                    case 1: print("Language")
                    case 2: print("Cell Info Display")
                    case 3: print("Welcome Note")
                    case 4: print("Network Selection")
                    case 5: print("Lights")
                    case 6: print("Confirm SIM service actions")
                    










                    
