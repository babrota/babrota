from datetime import datetime
from random import randint
import re
from TB_Home_Task_4_2 import get_sent
import os


class Interface:
    def __init__(self):
        self.content_text = ''
        self.content_name_add = ''
        self.content_name = ''
        self.flag = ''
        self.content_text_add = ''
        self.final_str = ''
        self.list_nice_sent = []
        self.inc_str_list_sent = []
        self.sent = ''
        self.publish_date = datetime.now()

    def input_print(self):
        dict_publ = {'1': ['News', 'City'], '2': ['Privat Ad', 'Actual until'], '3': ['Analytics', 'Analyst']}
        while True:
            self.flag = input("\nWhat will be published? \n(1 - News , 2 - Privat Ad, 3 - Analytics, 4 - From file, 5 - Exit) ")
            if self.flag:
                if len(self.flag) == 1:
                    if self.flag.isdigit():
                        if int(self.flag) <= 4:
                            if self.flag == '4':
                                wffi = WriteFromFileInterface(self.publish_date)
                                wffi.write_from_file_input()
                            else:
                                self.content_name = dict_publ.get(self.flag, '')[0]
                                self.content_name_add = dict_publ.get(self.flag, '')[1]

                                self.content_text = input(f'{self.content_name}: ')

                                while self.content_name_add:
                                    self.content_text_add = input(f'{self.content_name_add}: ')

                                    self.final_str = ''
                                    if self.flag == '1':
                                        news = News(self.content_text_add, self.publish_date)
                                        self.final_str = news.news_processing()
                                        if self.final_str:
                                            break

                                    elif self.flag == '2':
                                        if self.content_text:
                                            if re.search(r'\d{4}-\d{2}-\d{2}', self.content_text_add):
                                                try:
                                                    valid_date = datetime.strptime(self.content_text_add, "%Y-%m-%d")
                                                    adv = Advertising(self.content_name_add, self.content_text_add, self.publish_date)
                                                    self.final_str = adv.date_difference()
                                                except ValueError:
                                                    print('\nInvalid date! Your date does not match the actual date. Please enter the date in YYYY-MM-DD format.\n')
                                            else:
                                                print(f'\nWrong date! Please enter the date in YYYY-MM-DD format.\n')
                                            if self.final_str:
                                                break
                                        else:
                                            print(f'\n{self.content_name} is empty. Please enter.')
                                            break
                                    else:
                                        anl = Analytics(self.content_name_add, self.content_text_add, self.publish_date)
                                        self.final_str = anl.analyst_rate()
                                        if self.final_str:
                                            break

                                if self.final_str:
                                    fw = FileWriter(self.content_name, self.content_text, self.final_str)
                                    fw.file_writer()
                        else:
                            if int(self.flag) == 5:
                                return None
                            print('\nIt is not a number from 1 to 5! Please put a number from 1 to 5.')
                    else:
                        print('\nIt is not a digit! Please put a number from 1 to 5.')
                else:
                    print('\nYou put a lot of symbols! Please put a number from 1 to 5.')
            else:
                print('\nYou did not make a choice! Please put a number from 1 to 5.')


class News(Interface):
    def __init__(self, content_text_add, publish_date):
        super().__init__()
        self.content_text_add = content_text_add
        self.publish_date = publish_date

    def news_processing(self):
        part_str = f', ' if self.content_text_add else f''
        final = f'{self.content_text_add}{part_str}{str(self.publish_date)[:16]}'
        return final


class Advertising(Interface):
    def __init__(self, content_name_add, content_text_add, publish_date):
        super().__init__()
        self.content_name_add = content_name_add
        self.content_text_add = content_text_add
        self.publish_date = publish_date

    def date_difference(self):
        part_str = ''
        if self.content_text_add:
            date_diff = (datetime.strptime(self.content_text_add, "%Y-%m-%d") - self.publish_date).days
            if date_diff < 0:
                part_str = ' Outdated'
            else:
                part_str = f' {date_diff} days left' if date_diff > 1 else f' day left'
            final = f'{self.content_name_add}: {self.content_text_add}, {part_str}'
            return final


class Analytics(Interface):
    def __init__(self, content_name_add, content_text_add, publish_date):
        super().__init__()
        self.content_name_add = content_name_add
        self.content_text_add = content_text_add
        self.publish_date = publish_date

    def analyst_rate(self):
        part_str = ''
        if self.content_name_add:
            b = 10
            analyst_rate = randint(1, b)
            part_str = f'{self.content_name_add} {self.content_text_add} (rating - {analyst_rate} from {b}), ' if self.content_text_add else f''
            final = f'{part_str}{str(self.publish_date)[:16]}'
            return final


class FileWriter(Interface):
    def __init__(self, content_name, content_text, final_str):
        super().__init__()
        self.content_name = content_name
        self.content_text = content_text
        self.final_str = final_str

    def file_writer(self):
        if self.final_str:
            if self.content_name:
                if self.content_text:
                    list_for_write = [self.content_name + '------------------', self.content_text, self.final_str + '\n']
                    with open("task_6_file_TB.txt", "a") as file:
                        for line in list_for_write:
                            file.write(line + '\n')
                        print('\nPublished successfully!')
                        return True
                else:
                    print(f'\n{self.content_name} is empty. Not published.')
                    return False
            else:
                print(f'\nNot published! Something is wrong with the data.')
                return False
        else:
            print(f'\nNot published. Something is wrong with the data.')
            return False


class WriteFromFileInterface(Interface):
    def __init__(self, publish_date):
        super().__init__()
        self.flag = ''
        self.disk = ''
        self.folder = ''
        self.file_name = ''
        self.path = ''
        # self.def_path = r'c:\ccc\template_6_TB.txt'
        self.def_path = r'c:\ccc\ccc.txt'
        self.publish_date = publish_date

    def write_from_file_input(self):
        while True:
            self.flag = input("\nEnter file path (1 - Default , 2 - Your own, 3 - Exit) ")

            self.path = ''
            if self.flag:
                if len(self.flag) == 1:
                    if self.flag.isdigit():
                        if int(self.flag) <= 3:
                            if self.flag == '1':
                                self.path = os.path.join(self.path, self.def_path)
                                print(f'\nDefault path {self.path}')
                            elif self.flag == '2':
                                while True:
                                    self.disk = input("\nDisk name: ")
                                    if self.disk:
                                        if len(self.disk) == 1:
                                            if self.disk.isalpha():
                                                self.path = os.path.join(self.path, self.disk)
                                            else:
                                                print('\nYou put a digit! Please put one character.')
                                                break
                                        else:
                                            print('\nYou put a lot of symbols! Please put one character.')
                                            break
                                        while True:
                                            self.folder = input("Folder (if not needed, press enter): ")
                                            if self.folder:
                                                self.path = os.path.join(self.path, self.folder)
                                            else:
                                                while True:
                                                    self.file_name = input("File name: ")
                                                    if self.file_name:
                                                        self.path = os.path.join(self.path, self.file_name)
                                                        self.path = self.path[0] + ':' + self.path[1:]
                                                        # my code
                                                        break
                                                    else:
                                                        print('\nFile name is empty! Please enter it.')
                                                break
                                        break
                                    else:
                                        print('\nDisk name is empty! Please enter it.')
                            else:
                                return None

                            if self.path:
                                wff = WriteFromFile(self.path, self.publish_date)
                                wff.write_from_file()
                        else:
                            print('\nIt is not a number from 1 to 3! Please put a number from 1 to 3.')
                    else:
                        print('\nIt is not a digit! Please put a number from 1 to 3.')
                else:
                    print('\nYou put a lot of symbols! Please put a number from 1 to 3.')
            else:
                print('\nYou did not make a choice! Please put a number from 1 to 3.')


class WriteFromFile(WriteFromFileInterface):
    def __init__(self, path, publish_date):
        super().__init__(publish_date)
        self.rec_flag = None
        self.err_path = ''
        self.part_list = []
        self.paragraph = ''
        self.paragraph_list = []
        self.file_str = ''
        self.path = path
        self.publish_date = publish_date

    def normalization(self):
        self.list_nice_sent = []
        self.inc_str_list_sent = self.content_text.split('.')
        for self.sent in self.inc_str_list_sent:
            if self.sent:
                self.sent = get_sent(self.sent)
                self.list_nice_sent.append(self.sent)
        self.content_text = ''.join(self.list_nice_sent)
        return self.content_text

    def file_err_proc(self):
        with open(self.err_path, "a") as file:
            file.write(self.paragraph + '\n\n')
            file.close()

    def write_from_file(self):
        try:
            f = open(self.path)
            f.close()
        except FileNotFoundError:
            print(f'\nFile does not exists in {self.path}. Please put it to the proper folder.')
        else:
            with open(self.path, "r") as f:
                self.file_str = f.read()

            self.paragraph_list = self.file_str.split('\n\n')
            n = 0
            m = 0
            self.err_path = self.path[:-4] + '_err' + self.path[-4:]

            for p in range(len(self.paragraph_list)):
                print(f'\n{p+1} publication:')
                self.paragraph = self.paragraph_list[p]
                self.part_list = self.paragraph.split('\n|')

                self.final_str = ''
                try:
                    self.content_name = self.part_list[0]
                    self.content_text = self.part_list[1].rstrip()
                    self.content_text_add = self.part_list[2]
                except IndexError:
                    pass
                else:
                    self.content_text = self.normalization()

                    if self.content_name == 'News':
                        news_from_file = News(self.content_text_add, self.publish_date)
                        self.final_str = news_from_file.news_processing()

                    elif self.content_name == 'Privat Ad':
                        self.content_name_add = 'Actual until'
                        try:
                            valid_date = datetime.strptime(self.content_text_add, "%Y-%m-%d")
                        except ValueError:
                            print(f'\nInvalid date! Please put correct date in YYYY-MM-DD format.')
                        else:
                            adv_from_file = Advertising(self.content_name_add, self.content_text_add, self.publish_date)
                            self.final_str = adv_from_file.date_difference()

                    elif self.content_name == 'Analytics':
                        self.content_name_add = 'Analyst'
                        anl_from_file = Analytics(self.content_name_add, self.content_text_add, self.publish_date)
                        self.final_str = anl_from_file.analyst_rate()

                fw_from_file = FileWriter(self.content_name, self.content_text, self.final_str)
                self.rec_flag = fw_from_file.file_writer()

                if self.rec_flag:
                    n = n + 1
                else:
                    m = m + 1
                    self.file_err_proc()

            if os.path.exists(self.path):
                os.remove(self.path)

            if m == 0:
                print(f'\nAll {n} publications have been published from {self.path} file.')
            else:
                print(f'\n{n} publications have been published from {self.path} file. See {m} unpublished in {self.err_path} file.')


if __name__ == '__main__':
    inter = Interface()
    inter.input_print()
