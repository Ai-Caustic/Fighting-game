import pygame


class Fighter:
    def __init__(self, x, y, flip, data, sprite_sheet, animation_steps):
        self.size = data[0]
        self.image_scale = data[1]
        self.flip = flip
        self.offset = data[2]
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.action = 0  # 0:idle, 1:run, 2:jump, 3:attack1, 4:attack2, 5:hit, 6:dead
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect(x, y, 80, 180)
        self.vel_y = 0
        self.jump = False
        self.attack_type = 0
        self.attacking = False
        self.health = 100

    def load_images(self, sprite_sheet, animation_steps):
        # extract images from sprite sheets
        animation_list = []
        for y, animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(
                    x * self.size, y * self.size, self.size, self.size)
                pygame.transform.scale(temp_img, (self.size * self.image_scale, self.size * self.image_scale))
                temp_img_list.append(pygame.transform.scale(temp_img, (self.size * self.image_scale, self.size
                                                                       * self.image_scale))
)
            animation_list.append(temp_img_list)
        return animation_list

    def move(self, screen_width, screen_height, surface, target):
        speed = 10
        gravity = 2
        dx = 0
        dy = 0

        # Get key presses
        key = pygame.key.get_pressed()

        # can only perform other actions if not currently attacking
        if not self.attacking:
            # movement
            if key[pygame.K_a]:
                dx = -speed
            if key[pygame.K_d]:
                dx = speed

            # Jumping
            if key[pygame.K_w] and self.jump is False:
                self.vel_y = -30
                self.jump = True

            # Attacks
            if key[pygame.K_r] or key[pygame.K_t]:
                self.attack(surface, target)

                # Determine attack type
                if key[pygame.K_r]:
                    self.attack_type = 1
                    print('attack1')
                if key[pygame.K_t]:
                    self.attack_type = 2
                    print('attack2')

        # apply gravity
        self.vel_y += gravity
        dy += self.vel_y

        # ensure player stays on screen
        if self.rect.left + dx < 0:
            dx = - self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 110:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 110 - self.rect.bottom

        # ensure players face each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True
        # update player position
        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(
            self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            target.health -= 10
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        surface.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y -
                                  (self.offset[1] * self.image_scale)))
