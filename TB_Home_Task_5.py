from datetime import datetime
from random import randint
import re


class Interface:
    def __init__(self):
        self.content_text = ''
        self.content_name_add = ''
        self.content_name = ''
        self.flag = ''
        self.content_text_add = ''
        self.final_str = ''
        self.publish_date = datetime.now()

    def input_print(self):
        dict_publ = {'1': ['News', 'City'], '2': ['Privat Ad', 'Actual until'], '3': ['Analytics', 'Analyst']}
        while True:
            self.flag = input("\nWhat will be published? \n(1 - News , 2 - Privat Ad, 3 - Analytics, 4 - Exit) ")
            if self.flag:
                if len(self.flag) == 1:
                    if self.flag.isdigit():
                        if int(self.flag) <= 3:
                            self.content_name = dict_publ.get(self.flag, '')[0]
                            self.content_name_add = dict_publ.get(self.flag, '')[1]

                            self.content_text = input(f'{self.content_name}: ')
                            while self.content_name_add:
                                self.content_text_add = input(f'{self.content_name_add}: ')

                                self.final_str = ''
                                if self.flag == '1':
                                    news = News()
                                    self.final_str = news.news_processing()
                                    if self.final_str:
                                        break

                                elif self.flag == '2':
                                    if self.content_text:
                                        if re.search(r'\d{4}-\d{2}-\d{2}', self.content_text_add):
                                            try:
                                                valid_date = datetime.strptime(self.content_text_add, "%Y-%m-%d")
                                                adv = Advertising()
                                                self.final_str = adv.date_difference()
                                            except ValueError:
                                                print('\nInvalid date! Your date does not match the actual date.\n')
                                        else:
                                            print(f'\nWrong date! Please enter the date in YYYY-MM-DD format.\n')
                                        if self.final_str:
                                            break
                                    else:
                                        print(f'\n{self.content_name} is empty. Please enter.')
                                        break
                                else:
                                    anl = Analytics()
                                    self.final_str = anl.analyst_rate()
                                    if self.final_str:
                                        break

                            if self.final_str:
                                self.file_writer()

                        else:
                            if int(self.flag) == 4:
                                return None
                            print('\nIt is not a number from 1 to 4! Please put a number from 1 to 4.')
                    else:
                        print('\nIt is not a digit! Please put a number from 1 to 4.')
                else:
                    print('\nYou put a lot of symbols! Please put a number from 1 to 4.')
            else:
                print('\nYou did not make a choice! Please put a number from 1 to 4.')

    def file_writer(self):
        if self.content_name:
            if self.content_text:
                list_for_write = [self.content_name + '------------------', self.content_text, self.final_str + '\n']
                with open("task_5_file_TB.txt", "a") as file:
                    for line in list_for_write:
                        file.write(line + '\n')
                    print('\nPublished successfully!')
            else:
                print(f'\n{self.content_name} is empty. Not published.')
        else:
            print(f'\nNot published.')


class News(Interface):
    def news_processing(self):
        part_str = f', ' if inter.content_text_add else f''
        final = f'{inter.content_text_add}{part_str}{str(self.publish_date)[:16]}'
        return final


class Advertising(Interface):
    def date_difference(self):
        part_str = ''
        if inter.content_text_add:
            date_diff = (datetime.strptime(inter.content_text_add, "%Y-%m-%d") - self.publish_date).days
            if date_diff < 0:
                part_str = ' Outdated'
            else:
                part_str = f' {date_diff} days left' if date_diff > 1 else f' day left'
            final = f'{inter.content_name_add}: {inter.content_text_add}, {part_str}'
            return final


class Analytics(Interface):
    def analyst_rate(self):
        if inter.content_name_add:
            b = 10
            analyst_rate = randint(1, b)
            part_str = f'{inter.content_name_add} {inter.content_text_add} (rating - {analyst_rate} from {b}), ' if inter.content_text_add else f''
            final = f'{part_str}{str(self.publish_date)[:16]}'
            return final


if __name__ == '__main__':
    inter = Interface()
    inter.input_print()
