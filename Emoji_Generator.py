# Dolan, Austin
# ICS 110P Assignment 07
# October 10 2022
# Program uses functions to give a recommendation on where to go in the world by pulling a random number, taking input from user to alter a famous movie quote, and generates emojis based on your feelings. 

import math
import random
import emoji

def travel_agent(price_range, location_range):
	# Take input price_range and location_range and give travel recommendation
	if price_range == 'above' and location_range == 'local':
		print("\nYou live in Hawaii. How about a stay-cation.  You should stay at Aulani Disney Resort for 3 days!")
	elif price_range == 'below' and location_range == 'local':
		print("\nJust because you're on a budget, doesn't mean you can't have a good stay-cation. Stay at an Airbnb on the northshore for 3 days!")
	elif price_range == 'above' and location_range == 'abroad':
		print("\nLet's ball out! You should go on a 2 week surf trip in New Zealand. I know you've always wanted to go!")
	elif price_range == 'below' and location_range == 'abroad':
		print("\nDid you know Japan just reopend to international travelers! You can stay in Osaka for 3 days at an Airbnb.")
	else:
		# If user doesn't enter the prompts correctly keep their deposit and send them on their way
		print("\nYou didn't follow my instructions. I will keep your deposit. Goodbye.")

def movie_quote(word_one, word_two, word_three):
	# Print funny movie quote from Dude, Where's My Car with user input
	print("I think this is that funny movie quote:")
	print(f"\nI know you've been {word_one}ing my {word_two}, and I will catch you eventually. And when I do, I swear ta God, you will neva deliver {word_three}s in this town again!")
	print("-Mr. Pizzacoli, Dude, Where's My Car")
	print("Hm, that doesn't sound right but it's still funny!")

def emoji_generator(feeling):
	# Declare global variable draw
	global draw
	# Assign variable draw to emoji based on user's input
	if feeling == 'happy':
		draw = emoji.emojize(":slightly_smiling_face:")
	elif feeling == 'sad':
		draw = emoji.emojize(":frowning_face:")
	elif feeling == 'sleepy':
		draw = emoji.emojize(":sleeping_face:")
	elif feeling == 'stoked':
		draw = emoji.emojize(":grinning_face:")
	elif feeling == 'sleepy':
		draw = emoji.emojize(":sleeping_face:")
	elif feeling == 'beaming':
		draw = emoji.emojize(":beaming_face_with_smiling_eyes:")
	elif feeling == 'rotfl':
		draw = emoji.emojize(":rolling_on_the_floor_laughing:")
	elif feeling == 'winking':
		draw = emoji.emojize(":winking_face:")
	elif feeling == 'love':
		draw = emoji.emojize(":smiling_face_with_hearts:")
	elif feeling == 'in-love':
		draw = emoji.emojize(":smiling_face_with_heart-eyes:")
	elif feeling == 'star-struck':
		draw = emoji.emojize(":star-struck:")
	elif feeling == 'teary':
		draw = emoji.emojize(":smiling_face_with_tear:")
	elif feeling == 'zany':
		draw = emoji.emojize(":zany_face:")
	elif feeling == 'spendy':
		draw = emoji.emojize(":money-mouth_face:")
	elif feeling == 'thinking':
		draw = emoji.emojize(":thinking_face:")
	elif feeling == 'neutral':
		draw = emoji.emojize(":neutral_face:")
	elif feeling == 'relieved':
		draw = emoji.emojize(":relieved_face:")
	elif feeling == 'nauseous':
		draw = emoji.emojize(":nauseated_face:")
	elif feeling == 'hot':
		draw = emoji.emojize(":hot_face:")
	elif feeling == 'cold':
		draw = emoji.emojize(":cold_face:")
	elif feeling == 'woozy':
		draw = emoji.emojize(":woozy_face:")
	elif feeling == 'nerdy':
		draw = emoji.emojize(":nerd_face:")
	elif feeling == 'worried':
		draw = emoji.emojize(":worried_face:")
	elif feeling == 'astonished':
		draw = emoji.emojize(":astonished_face:")
	elif feeling == 'fearful':
		draw = emoji.emojize(":fearful_face:")
	elif feeling == 'anxious':
		draw = emoji.emojize(":anxious_face_with_sweat:")
	elif feeling == 'crying':
		draw = emoji.emojize(":crying_face:")
	elif feeling == 'disappointed':
		draw = emoji.emojize(":disappointed_face:")
	elif feeling == 'angry':
		draw = emoji.emojize(":angry_face:")
	elif feeling == 'enraged':
		draw = emoji.emojize(":enraged_face:")
	elif feeling == 'hungry':
		draw = emoji.emojize(":drooling_face:")
	else:
		# If feeling is not one of these then be confused and tell user I don't know that feeling yet
		draw = emoji.emojize(":confused_face:")
		print(f"I'm confused, I don't know how to express {feeling}")
	return draw

def main():
	try:
		# Welcome user and ask their name
		user_name = input("Hello and welcome to my program.\n What is your name? ")
		play = input(f"\n{user_name}, My program has 3 operations.\n Would you like to try one? (yes or no) ")
		# Loop while user doesn't enter no
		while play != 'no':
			if play == 'yes':
				choice = int(input("\nOkay! I can give you recommendations of where to go on your next vacation, tell you a funny quote from a movie, and generate an emoji based on your feelings.\n Which would you like to do? (1, 2, or 3) "))
				if choice == 1:
					# Take input from user above or below, and local or abroad and recommend some travel plans
					print("\nYou chose to access my travel agent function. You give me money and I will randomly select a destination for you, and the trip is non-refundable. Let's go!")
					price_range = input("\nOkay! First tell me your price range is it above or below $1000.00? (above or below) ")
					location_range = input("\nNow tell me would you like to travel locally or abroad? (local or abroad) ")
					travel_agent(price_range, location_range)
					play = input("\nWant to play again? (yes or no) ")
				elif choice == 2:
					# Take input from user word_one, word_two, and word_three and output funny movie quote
					print("\nYou chose to hear one of my favorite movie quotes, but I can't remember all the words. Maybe you can help!")
					word_one = input("\nWhat's the first funny word? (verb) ")
					word_two = input("\nHow about the second funny word? (noun) ")
					word_three = input("\nThere was one more funny word in there, what was it? (noun) ")
					movie_quote(word_one, word_two, word_three)
					play = input("\nWant to play again? (yes or no) ")
				elif choice == 3:
					# print(emoji.emojize(":slightly_smiling_face:")) test
					# Fun emoji generator, user enters a feeling and I output the corresponding emoji, can only be one word feelings or I will be confused
					print("\nYou chose to to use my feelings evaluation depiction program. You tell me a feeling, and I will draw what I think that feeling looks like! Let's go!")
					feeling = input("\nIn one word tell me how you are feeling.  Try something like happy, sad, love, hungry or something else! ")
					emoji_generator(feeling)
					print(f"\nYou are feeling {feeling}: ", draw)
					play = input("\nWant to play again? (yes or no) ")
				else:
					# If user doesn't enter 1, 2, or 3 tell them their response is invalid
					print("\nThat is not one of my choices!")
					play = input("\nDo you want to try the program again? (yes or no) ")
			else:
				# If user doesn't enter yes or no tell them their response is invalid
				print(f"\n{play} is not a valid response.")
				play = input("\nWould you like to try my program? (yes or no) ")
	except ValueError as e:
		print("\nThat is not a valid number. Please try again.")
		print("Error:", end = " ")
		print(e)

	# After loop breaks say Goodbye
	print("\nThank's for playing! Goodbye")
main()
