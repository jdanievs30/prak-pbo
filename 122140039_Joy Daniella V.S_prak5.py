import pygame
import random

# Abstraction: Membuat kelas Game sebagai kontrol utama permainan
class Game:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.player_score = 0
        self.enemy_score = 0
        self.font = pygame.font.SysFont(None, 48)

    def run(self):
        running = True
        while running:
            self.screen.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_g:
                        self.play("gunting")
                    elif event.key == pygame.K_b:
                        self.play("batu")
                    elif event.key == pygame.K_k:
                        self.play("kertas")

            player_text = self.font.render(f"Player: {self.player_score}", True, (0, 0, 0))
            enemy_text = self.font.render(f"Enemy: {self.enemy_score}", True, (0, 0, 0))
            self.screen.blit(player_text, (20, 20))
            self.screen.blit(enemy_text, (self.width - enemy_text.get_width() - 20, 20))

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def play(self, player_choice):
        choices = ["gunting", "batu", "kertas"]
        enemy_choice = random.choice(choices)

        if player_choice == enemy_choice:
            pass
        elif (player_choice == "gunting" and enemy_choice == "kertas") or \
             (player_choice == "batu" and enemy_choice == "gunting") or \
             (player_choice == "kertas" and enemy_choice == "batu"):
            self.player_score += 1
        else:
            self.enemy_score += 1

        print(f"Player: {player_choice}, Enemy: {enemy_choice}")

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()
