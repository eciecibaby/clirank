import os
import sys
import time
import random

running = True

try:
	while running:
		os.system('clear')
		print("CliRank | v1.1")
		print("Rank 1 is highest, rank 6 is lowest")
		print()
		ttl = input("What are you ranking (Enter title)? ")
		print()
		rk1 = input("1. ")
		rk2 = input("2. ")
		rk3 = input("3. ")
		rk4 = input("4. ")
		rk5 = input("5. ")
		rk6 = input("6. ")
		print()
		input("Press any key to exit...")
		break
		sys.exit()
except KeyboardInterrupt:
	sys.exit()
