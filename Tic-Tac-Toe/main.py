import random
print('*******************Tik Tac Toe************************* \n \n')


print('Rules :- \n',
	   'Each square in tic tac toe board is represent by a number. \n',
	   'The user must enter the number which represent the square where he will play his move. \n \n')

box = [[ '0', '|', '1', '|', '2'],
	   [ '3', '|', '4', '|', '5'],
	   [ '6', '|', '7', '|', '8']]

dash = [[ '--', '--', '--'],
		['--','--','--']]

class UI:
	@staticmethod
	def display_board(box, dash):
		main_list = [[],[],[],[],[]]
		for i in range(len(box)):
				main_list[i] = box[i]
		main_list.reverse()
		for i in range (len(dash)):
			main_list[i] = dash[i]
		main_list.reverse()
		order = [0 , 3, 1, 4, 2]
		main_list = [main_list[i] for i in order]
		for i in range(len(main_list)):
			board = main_list[i]
			for i in range(len(board)):
				if(i != len(board)-1):
					print(board[i] , end="")
				else:
					print(board[i])


class Players:

	@staticmethod
	def user_input(value):
		status = False
		for i in range(len(box)):
			current_list = box[i]
			for i in range(len(current_list)):
				if(str(value) == current_list[i] and str(value) != '|'):
					current_list[i] = 'X'
					status = True
					break
			if(status == True):
				break
		if(status == False):
			return False
		UI.display_board(box,dash)
		if(status == True):
			return True

	@staticmethod
	def computer_input():
		arr = box[0] + box[1] + box[2] 
		arr = list(filter(lambda x: x!='X' and x!='C' and x!='|',arr))
		value = random.choice(arr)
		for i in range(len(box)):
			current_list = box[i]
			for i in range(len(current_list)):
				if(value == current_list[i]):
					current_list[i] = 'C'
					break
		UI.display_board(box,dash)	



class game:
	@staticmethod
	def check_win():
		win = False
		list1 = list(filter(lambda x: x!='|', box[0]))
		list2 = list(filter(lambda x: x!='|', box[1]))
		list3 = list(filter(lambda x: x!='|', box[2]))
		for i in range(len(box)):
			if(i == 0):
				if(list1[0] == list1[1] == list1[2] or list1[0] == list2[0] == list3[0] or list1[0] == list2[1] == list3[2]):
					win = True
					break

				if(list1[2] == list2[2] == list3[2] or list1[2] == list2[1] == list3[0]):
					win = True
					break
				if(list1[1] == list2[1] == list3[1]):
					win = True 
					break
			elif(i == 1):
				if(list2[0] == list2[1] == list2[2]):
					win = True 
					break
			else:
				if(list3[0] == list3[1] == list3[2]):
					win = True 
					break
		return win	

	@staticmethod
	def play_game():
		game_status = True
		turn = 0
		winner = 'You'
		while(game_status == True):
			if(turn % 2 == 0):
				user_value = False
				while(user_value == False):
					user_value = input(('\nEnter the position where you want to display the number :- '))
					if(Players.user_input(user_value) == False):
						user_value = False
					else:
						Players.user_input(user_value)
						result = game.check_win()
						if(result == True):
							winner = 'You'
						turn = turn + 1

			else:
				print('\n\nComputer played a move represented as C\n\n')
				Players.computer_input()
				result = game.check_win()
				if(result == True):
					winner = 'Computer'
				turn = turn + 1
			if(result == True):
				print(f'\n{winner} won the game\n')
				print('Thanks for playing !!\n')
				game_status = False

			


UI.display_board(box, dash)
game.play_game()