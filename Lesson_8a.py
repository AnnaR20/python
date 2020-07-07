import random


class LotoCard:
    def __init__(self, name):
        self.name = name
        self.card1 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.card2 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.card3 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        nums = list(range(1, 91))
        random.shuffle(nums)
        nums1 = sorted(nums[0:5])
        nums2 = sorted(nums[5:10])
        nums3 = sorted(nums[10:15])
        positions1 = list(range(0, 9))
        random.shuffle(positions1)
        positions1 = sorted(positions1[0:5])
        positions2 = list(range(0, 9))
        random.shuffle(positions2)
        positions2 = sorted(positions2[0:5])
        positions3 = list(range(0, 9))
        positions3 = sorted(positions3[0:5])
        random.shuffle(positions3)
        for el in range(0, 5):
            self.card1[positions1[el]] = str(nums1[el])
            self.card2[positions2[el]] = str(nums2[el])
            self.card3[positions2[el]] = str(nums3[el])
        self.card1a = ' '.join(self.card1)
        self.card2a = ' '.join(self.card2)
        self.card3a = ' '.join(self.card3)


class LotoGame:
    def __init__(self, human_player, computer_player):
        self.human_player = human_player
        self.computer_player = computer_player

    def start(self):
        self.barrel_list = list(range(1, 91))
        random.shuffle(self.barrel_list)
        for step in range(0, 90):
            print(f'{self.human_player.name}:')
            print('-' * 22)
            print(self.human_player.card1a)
            print(self.human_player.card2a)
            print(self.human_player.card3a)
            print(f'{self.computer_player.name}:')
            print('-' * 22)
            print(self.computer_player.card1a)
            print(self.computer_player.card2a)
            print(self.computer_player.card3a)
            print(f'Новый бочонок {self.barrel_list[step]}, осталось {89-step}')
            x = input('Хотите зачеркнуть? y/n:')
            if x == 'y' and str(self.barrel_list[step]) not in self.human_player.card1:
                if str(self.barrel_list[step]) not in self.human_player.card2:
                    if str(self.barrel_list[step]) not in self.human_player.card3:
                        print('Вы проиграли')
                        return
            if x == 'n' and str(self.barrel_list[step]) in self.human_player.card1:
                print('Вы проиграли')
                return
            if x == 'n' and str(self.barrel_list[step]) in self.human_player.card2:
                print('Вы проиграли')
                return
            if x == 'n' and str(self.barrel_list[step]) in self.human_player.card3:
                print('Вы проиграли')
                return
            for ind, el in enumerate(self.human_player.card1):
                if el == str(self.barrel_list[step]):
                    self.human_player.card1[ind] = '-'
            self.human_player.card1a = ' '.join(self.human_player.card1)
            for ind, el in enumerate(self.human_player.card2):
                if el == str(self.barrel_list[step]):
                    self.human_player.card2[ind] = '-'
            self.human_player.card2a = ' '.join(self.human_player.card2)
            for ind, el in enumerate(self.human_player.card3):
                if el == str(self.barrel_list[step]):
                    self.human_player.card3[ind] = '-'
            self.human_player.card3a = ' '.join(self.human_player.card3)
            for ind, el in enumerate(self.computer_player.card1):
                if el == str(self.barrel_list[step]):
                    self.computer_player.card1[ind] = '-'
            self.computer_player.card1a = ' '.join(self.computer_player.card1)
            for ind, el in enumerate(self.computer_player.card2):
                if el == str(self.barrel_list[step]):
                    self.computer_player.card2[ind] = '-'
            self.computer_player.card2a = ' '.join(self.computer_player.card2)
            for ind, el in enumerate(self.computer_player.card3):
                if el == str(self.barrel_list[step]):
                    self.computer_player.card3[ind] = '-'
            self.computer_player.card3a = ' '.join(self.computer_player.card3)
            if len(set(self.human_player.card1a)) == 2:
                if len(set(self.human_player.card2a)) == 2:
                    if len(set(self.human_player.card3a)) == 2:
                        print('Вы выиграли')
                        return
            if len(set(self.computer_player.card1a)) == 2:
                if len(set(self.computer_player.card2a)) == 2:
                    if len(set(self.computer_player.card3a)) == 2:
                        print('Вы проиграли')
                        return


humanplayer = LotoCard('Игрок')
computerplayer = LotoCard('Компьютер')

game = LotoGame(humanplayer, computerplayer)
game.start()
