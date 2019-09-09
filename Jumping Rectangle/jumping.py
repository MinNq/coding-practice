import os

import numpy as np
import pygame

class player:
	def __init__(self, x, y, width, height, h_speed = 2.5, v_speed = 600):
		self.jumping = False
		self.air_time = 0
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.h_speed = h_speed
		self.v_speed = v_speed

	def move_left(self):
		if self.x > 0:
			self.x -= self.h_speed

	def move_right(self, s_width):
		if self.x < s_width - self.width:
			self.x += self.h_speed

	def jump(self, s_height, gravity, FPS):
		if self.air_time < self.time_of_flight:
			self.air_time += 1/FPS
			self.y = s_height - self.height - self.air_time*(self.v_speed - gravity/2*self.air_time)
			print(self.time_of_flight - self.air_time)
		else:
			self.jumping = False
			self.air_time = 0

	def act(self, s_height, s_width, gravity, FPS, condition):
		if condition[0]:
			self.move_left()
		if condition[1]:
			self.move_right(s_width)

		if not self.jumping:
			if condition[2]:
				self.jumping = True
		else:
			self.jump(s_height, gravity, FPS)

class game:
	def __init__(self, gravity, random_player = True, FPS = 200, s_height = 360, s_width = 640):
		self.FPS = FPS
		self.gravity = gravity
		self.s_height = s_height
		self.s_width = s_width
		self.random_player = random_player

	def redraw(self, dude):
		self.win.fill((0,0,0))
		pygame.draw.rect(self.win, (0,0,255), (dude.x, dude.y, dude.width, dude.height))
		pygame.display.update()
	
	def main(self):
		pygame.init()
		self.win = pygame.display.set_mode((self.s_width, self.s_height))
		pygame.display.set_caption('Jumping')
		
		self.clock = pygame.time.Clock()

		dude = player(self.s_width/2 - 5, self.s_height - 10, 10, 10)

		dude.time_of_flight = 2*dude.v_speed/self.gravity

		self.running = True
		while self.running:
			self.clock.tick(self.FPS)
			self.redraw(dude)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

			keys = pygame.key.get_pressed()
			mouse_rel = pygame.mouse.get_rel()
			mouse_press = pygame.mouse.get_pressed()

			if self.random_player:
				action_set = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1]]
				choice = np.random.choice(range(6), p = [.39,.01,.29,.01,.29,.01])
				dude.act(self.s_height, self.s_width, self.gravity, self.FPS, action_set[choice])

			else:
				condition = [0,0,0]
				condition[0] = keys[pygame.K_LEFT] or mouse_rel[0] < 0
				condition[1] = keys[pygame.K_RIGHT] or mouse_rel[0] > 0
				condition[2] = keys[pygame.K_SPACE] or mouse_rel[1] < -5 or mouse_press[0]
				dude.act(self.s_height, self. s_width, self.gravity, self.FPS, condition)	

		pygame.quit()

NewGame = game(gravity = 1200, random_player = False)
NewGame.main()