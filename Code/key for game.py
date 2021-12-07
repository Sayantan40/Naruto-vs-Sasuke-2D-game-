
keys = pygame.key.get_pressed()

if keys[pygame.K_SPACE] and throwspeed == 0:

	if naruto.left == True:
		facing = -1

	else:
		facing = 1

if len(shurikens) < 5:
	shurikens.append(
		weapon(round(naruto.x + naruto.width // 2), round(naruto.y + naruto.height // 2), 40, 40, facing))

	throwspeed = 1

######for left movedment left key######

if keys[pygame.K_LEFT] and naruto.x > naruto.speed:

	naruto.x -= naruto.speed

	naruto.left = True

	naruto.right = False
######for right movedment left key######

elif keys[pygame.K_RIGHT] and naruto < 690 - naruto.width - naruto.speed:
	naruto.x += naruto.speed

	naruto.left = False

	naruto.right = True

else:
	naruto.left = False

naruto.right = False

naruto.walkcount = 0

naruto.standing = True

if not (naruto.isJump):
	if keys[pygame.K_UP]:
		naruto.isJump = True
		naruto.right = False
		naruto.left = False
		naruto.walkCount = 0
else:
	if naruto.jumpheight >= -10:
		neg = 1
		if naruto.jumpheight < 0:
			neg = -1
		naruto.y -= (naruto.jumpheight ** 2) * 0.5 * neg
		naruto.jumpheight -= 1

	else:

		naruto.isJump = False

		naruto.jumpheight = 10

redrawganewindow()

pygame.quit()