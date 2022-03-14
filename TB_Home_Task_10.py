from datetime import datetime
from random import randint
import re
from TB_Home_Task_4_2 import get_sent
import os
import string
import csv
from collections import Counter
import json
import xml.etree.cElementTree as ET
import sqlite3


class Interface:
    def __init__(self):
        self.def_path = ''
        self.content_text = ''
        self.content_name_add = ''
        self.content_name = ''
        self.flag = ''
        self.content_text_add = ''
        self.final_str = ''
        self.list_nice_sent = []
        self.inc_str_list_sent = []
        self.sent = ''
        self.file_str = ''
        self.publish_date = datetime.now()
        self.a_rate = 0
        self.my_file = r'publications_TB.txt'
        self.def_txt_path = r'c:\ccc\template_TB.txt'
        self.def_json_path = r'c:\ccc\template_TB.json'
        self.def_xml_path = r'c:\ccc\template_TB.xml'
        self.def_db = r'publications.db'

    def input_print(self):
        dict_publ = {'1': ['News', 'City'], '2': ['Privat Ad', 'Actual until'], '3': ['Analytics', 'Analyst']}
        while True:
            self.flag = input(
                "\nWhat will be published? \n(1 - News , 2 - Privat Ad, 3 - Analytics, 4 - From TEXT file, 5 - From JSON file, 6 - From XML file, 7 - Exit) ")
            if self.flag:
                if len(self.flag) == 1:
                    if self.flag.isdigit():
                        if int(self.flag) <= 6:
                            if self.flag in ('4', '5', '6'):
                                if self.flag == '4':
                                    self.def_path = self.def_txt_path
                                elif self.flag == '5':
                                    self.def_path = self.def_json_path
                                elif self.flag == '6':
                                    self.def_path = self.def_xml_path
                                wffi = WriteFromFileInterface(self.publish_date, self.my_file, self.def_path, self.flag, self.a_rate)
                                wffi.write_from_file_input()
                            else:
                                self.content_name = dict_publ.get(self.flag, '')[0]
                                self.content_name_add = dict_publ.get(self.flag, '')[1]

                                self.content_text = input(f'{self.content_name}: ')

                                while self.content_name_add:
                                    self.content_text_add = input(f'{self.content_name_add}: ')

                                    self.final_str = ''
                                    if self.flag == '1':
                                        if self.content_text_add:
                                            news = News(self.content_text_add, self.publish_date)
                                            self.final_str = news.news_processing()
                                        else:
                                            print(f'\n{self.content_name_add} is empty. Please enter.')
                                        if self.final_str:
                                            break

                                    elif self.flag == '2':
                                        if self.content_text:
                                            if re.search(r'\d{4}-\d{2}-\d{2}', self.content_text_add):
                                                try:
                                                    valid_date = datetime.strptime(self.content_text_add, "%Y-%m-%d")
                                                    adv = Advertising(self.content_name_add, self.content_text_add,
                                                                      self.publish_date)
                                                    self.final_str = adv.date_difference()
                                                except ValueError:
                                                    print(
                                                        '\nInvalid date! Your date does not match the actual date. Please enter the date in YYYY-MM-DD format.\n')
                                            else:
                                                print(f'\nWrong date! Please enter the date in YYYY-MM-DD format.\n')
                                            if self.final_str:
                                                break
                                        else:
                                            print(f'\n{self.content_name} is empty. Please enter.')
                                            break
                                    else:
                                        if self.content_text_add in ('None', ''):
                                            self.content_text_add = 'TASS'
                                        self.a_rate = randint(1, 10)
                                        anl = Analytics(self.content_name_add, self.content_text_add, self.publish_date, self.a_rate)
                                        self.final_str = anl.analyst_rate()
                                        if self.final_str:
                                            break

                                if self.final_str:
                                    fw = FileWriter(self.content_name, self.content_text, self.final_str, self.my_file,
                                                    self.content_text_add, self.publish_date, self.a_rate)
                                    fw.file_writer()
                        else:
                            if int(self.flag) == 7:
                                claw = CountLetterAndWords(self.my_file)
                                self.file_str = claw.open_file()
                                claw.letters_count()
                                claw.words_count()
                                return None
                            print('\nIt is not a number from 1 to 7! Please put a number from 1 to 7.')
                    else:
                        print('\nIt is not a digit! Please put a number from 1 to 7.')
                else:
                    print('\nYou put a lot of symbols! Please put a number from 1 to 7.')
            else:
                print('\nYou did not make a choice! Please put a number from 1 to 7.')


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
    def __init__(self, content_name_add, content_text_add, publish_date, a_rate):
        super().__init__()
        self.content_name_add = content_name_add
        self.content_text_add = content_text_add
        self.publish_date = publish_date
        self.a_rate = a_rate

    def analyst_rate(self):
        part_str = ''
        if self.content_name_add:
            if self.content_text_add in ('None', ''):
                self.content_text_add = 'TASS'
            part_str = f'{self.content_name_add} {self.content_text_add} (rating - {self.a_rate} from {10}), ' if self.content_text_add else f''
            final = f'{part_str}{str(self.publish_date)[:16]}'
            return final


class FileWriter(Interface):
    def __init__(self, content_name, content_text, final_str, my_file, content_text_add, publish_date, a_rate):
        super().__init__()
        self.content_name = content_name
        self.content_text = content_text
        self.final_str = final_str
        self.my_file = my_file
        self.content_text_add = content_text_add
        self.publish_date = publish_date
        self.a_rate = a_rate

    def file_writer(self):
        if self.final_str:
            if self.content_name:
                if self.content_text not in ('', 'None'):
                    list_for_write = [self.content_name + '------------------', self.content_text,
                                      self.final_str + '\n']
                    with open(self.my_file, "a") as file:
                        for line in list_for_write:
                            file.write(line + '\n')

                        db_publ = DBConnection(self.def_db, self.publish_date, self.content_text, self.content_text_add, self.a_rate)
                        if self.content_name == 'News':
                            db_publ.create_table_news()
                        elif self.content_name == 'Privat Ad':
                            db_publ.create_table_ad()
                        elif self.content_name == 'Analytics':
                            db_publ.create_table_anl()
                        db_publ.close_cursor()

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
    def __init__(self, publish_date, my_file, def_path, osn_flag, a_rate):
        super().__init__()
        self.disk = ''
        self.folder = ''
        self.file_name = ''
        self.path = ''
        self.flag = ''
        self.publish_date = publish_date
        self.my_file = my_file
        self.def_path = def_path
        self.osn_flag = osn_flag
        self.a_rate = a_rate

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
                                # print(f'\nDefault path {self.path}')
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
                                wff = WriteFromFile(self.path, self.publish_date, self.my_file, self.def_path, self.osn_flag, self.a_rate)
                                if self.osn_flag == '4':
                                    wff.write_from_file_text()
                                elif self.osn_flag == '5':
                                    wff.write_from_file_json()
                                elif self.osn_flag == '6':
                                    wff.write_from_file_xml()
                        else:
                            print('\nIt is not a number from 1 to 3! Please put a number from 1 to 3.')
                    else:
                        print('\nIt is not a digit! Please put a number from 1 to 3.')
                else:
                    print('\nYou put a lot of symbols! Please put a number from 1 to 3.')
            else:
                print('\nYou did not make a choice! Please put a number from 1 to 3.')


class CountLetterAndWords(Interface):
    def __init__(self, my_file):
        super().__init__()
        self.my_file = my_file
        self.file_str = ''

    def open_file(self):
        self.file_str = ''
        try:
            f = open(self.my_file)
            f.close()
        except FileNotFoundError:
            print(f'\nFile {self.my_file} does not exists.')
        else:
            with open(self.my_file, "r") as f:
                self.file_str = f.read()
        return self.file_str

    def letters_count(self):
        let_list = string.ascii_lowercase
        with open('letters_count.csv', 'w', newline='') as csvfile:
            if self.file_str:
                headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
                writer = csv.DictWriter(csvfile, fieldnames=headers)
                writer.writeheader()
                len_txt = len(self.file_str)
                for i in let_list:
                    cnt_let = self.file_str.lower().count(i)
                    if cnt_let > 0:
                        cnt_let_upp = self.file_str.count(i.upper())
                        perc_let = round(cnt_let / len_txt * 100, 1) if len_txt > 0 else 0
                        writer.writerow(
                            {headers[0]: i, headers[1]: cnt_let, headers[2]: cnt_let_upp, headers[3]: perc_let})

    def words_count(self):
        self.file_str = self.file_str.lower().replace('--', '').replace(' - ', ' ')
        words = self.file_str.split()
        words = [word.strip('.,!;()[]:') for word in words]
        word_dict = Counter(words)
        with open('words_count.csv', 'w', newline='') as csvfile:
            csv.register_dialect('my_dialect', delimiter='-', quoting=csv.QUOTE_NONNUMERIC)
            writer = csv.writer(csvfile, dialect='my_dialect')
            for item in word_dict.items():
                if item[0].isalpha():
                    writer.writerow(item)


class WriteFromFile(WriteFromFileInterface):
    def __init__(self, path, publish_date, my_file, def_path, flag, a_rate):
        super().__init__(publish_date, my_file, def_path, flag, a_rate)
        self.i = 0
        self.root = None
        self.xml_file = None
        self.tree = None
        self.m = 0
        self.n = 0
        self.i_dict = {}
        self.json_dict_list = []
        self.json_data = []
        self.ext = None
        self.rec_flag = None
        self.err_path = ''
        self.part_list = []
        self.paragraph = ''
        self.paragraph_list = []
        self.file_str = ''
        self.path = path
        self.publish_date = publish_date
        self.my_file = my_file
        self.def_path = def_path
        self.flag = flag
        self.a_rate = a_rate

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
            if self.flag == '4':
                file.write(self.paragraph + '\n\n')
            elif self.flag == '5':
                json.dump(self.i_dict, file)
            elif self.flag == '6':
                file.write(str(ET.tostring(self.root[self.i])))
            file.close()

    def gen_err_name(self):
        self.ext = len(self.path.split('.')[-1])
        self.err_path = self.path[:-(self.ext + 1)] + '_err' + self.path[-(self.ext + 1):]
        return self.err_path

    def proc_publ(self):
        if self.content_name == 'News':
            self.content_name_add = 'City'
            if self.content_text_add not in ('None', ''):
                news_from_file = News(self.content_text_add, self.publish_date)
                self.final_str = news_from_file.news_processing()
            else:
                print(f'\nThere is no {self.content_name_add}. Please enter a {self.content_name_add}.')
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
            if self.content_text_add in ('None', ''):
                self.content_text_add = 'TASS'
            self.a_rate = randint(1, 10)
            anl_from_file = Analytics(self.content_name_add, self.content_text_add, self.publish_date, self.a_rate)
            self.final_str = anl_from_file.analyst_rate()
        return self.final_str

    def proc_fin_res(self):
        if (self.m == 0) or (self.m != 0 and self.n != 0):
            if os.path.exists(self.path):
                os.remove(self.path)
        if self.m == 0:
            print(f'\nAll {self.n} publications have been published from {self.path} file.')
        else:
            if self.n > 0:
                print(
                    f'\n{self.n} publications have been published from {self.path} file. See {self.m} unpublished in {self.err_path} file.')

    def processing(self):
        fw_from_file = FileWriter(self.content_name, self.content_text, self.final_str, self.my_file,
                                  self.content_text_add, self.publish_date, self.a_rate)
        self.rec_flag = fw_from_file.file_writer()

        if self.rec_flag:
            self.n = self.n + 1
            db_publ = DBConnection(self.def_db, self.publish_date, self.content_text, self.content_text_add, self.a_rate)
            if self.content_name == 'News':
                db_publ.create_table_news()
            elif self.content_name == 'Privat Ad':
                db_publ.create_table_ad()
            elif self.content_name == 'Analytics':
                db_publ.create_table_anl()
            db_publ.close_cursor()
        else:
            self.m = self.m + 1
            self.file_err_proc()

    def write_from_file_text(self):
        # self.path - path from interface for file read and load
        claw_path = CountLetterAndWords(self.path)
        self.file_str = claw_path.open_file()

        if self.file_str:
            self.paragraph_list = self.file_str.split('\n\n')
            self.n = 0
            self.m = 0
            self.err_path = self.gen_err_name()

            for p in range(len(self.paragraph_list)):
                print(f'\n{p + 1} publication:')
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
                    self.final_str = self.proc_publ()

                self.processing()

            self.proc_fin_res()

    def write_from_file_json(self):
        try:
            f = open(self.path)
            f.close()
        except FileNotFoundError:
            print(f'\nFile {self.path} does not exists.')
        else:
            try:
                with open(self.path, 'r') as json_file:
                    self.json_data = json.load(open(self.path))
            except json.decoder.JSONDecodeError:
                print(f'\nFile {self.path} is not a json file.')

        if self.json_data:
            self.n = 0
            self.m = 0
            self.err_path = self.gen_err_name()

            for i_dict in self.json_data:
                self.i_dict = i_dict
                print(f'\n{self.json_data.index(self.i_dict) + 1} publication:')

                self.final_str = ''
                try:
                    self.json_dict_list = [k for (k, v) in i_dict.items()]
                    self.content_name = str(i_dict.get(self.json_dict_list[0]))
                    self.content_text = str(i_dict.get(self.json_dict_list[1])).rstrip()
                    self.content_text_add = str(i_dict.get(self.json_dict_list[2]))
                except IndexError:
                    pass
                else:
                    self.final_str = self.proc_publ()

                self.processing()

            self.proc_fin_res()

    def write_from_file_xml(self):
        try:
            f = open(self.path)
            f.close()
        except FileNotFoundError:
            print(f'\nFile {self.path} does not exists.')
        else:
            try:
                self.xml_file = ET.parse(self.path)
            except ET.ParseError:
                print(f'\nFile {self.path} has an incorrect structure. Please check and correct.')

        if self.xml_file:
            self.root = self.xml_file.getroot()

            self.n = 0
            self.m = 0
            self.err_path = self.gen_err_name()

            for self.i in range(0, len(self.root)):
                print(f'\n{self.i + 1} publication:')

                self.final_str = ''
                try:
                    self.content_name = str(self.root[self.i][0].text)
                    self.content_text = str(self.root[self.i][1].text).rstrip()
                    self.content_text_add = str(self.root[self.i][2].text)
                except IndexError:
                    pass
                else:
                    self.final_str = self.proc_publ()

                self.processing()

            self.proc_fin_res()


class DBConnection(WriteFromFileInterface):
    def __init__(self, database_name, publish_date, content_text, content_text_add, a_rate, my_file=None, def_path=None,
                 flag=None):
        super().__init__(publish_date, my_file, def_path, flag, a_rate)
        self.publish_date = publish_date
        self.content_text = content_text
        self.content_text_add = content_text_add
        self.a_rate = a_rate
        with sqlite3.connect(database_name) as self.conn:
            self.cur = self.conn.cursor()

    def close_cursor(self):
        self.cur.close()

    def create_table_news(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS news (text text, city varchar(256), date datetime)")
        self.cur.execute(f"SELECT 1 FROM news WHERE rtrim(text) =? and rtrim(city) =?",
                         (self.content_text.rstrip(), self.content_text_add.rstrip()))
        if len(self.cur.fetchall()) == 0:
            self.cur.execute(f"INSERT INTO news VALUES (?,?,?)",
                             (self.content_text.rstrip(), self.content_text_add.rstrip(), str(self.publish_date)[:16]))
            self.conn.commit()

    def create_table_ad(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS advertising (text text, exp_date datetime, diff_days int)")
        self.cur.execute(f"SELECT 1 FROM advertising WHERE rtrim(text) =?", (self.content_text.rstrip(),))
        if len(self.cur.fetchall()) == 0:
            self.cur.execute(f"INSERT INTO advertising VALUES (?,?,?)", (
                self.content_text.rstrip(), self.content_text_add.rstrip(),
                (datetime.strptime(self.content_text_add, "%Y-%m-%d") - self.publish_date).days))
            self.conn.commit()

    def create_table_anl(self):
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS analytics (text text, analyst varchar(256), rating varchar(256), date datetime)")
        self.cur.execute(f"SELECT 1 FROM analytics WHERE rtrim(text) =? and rtrim(analyst) =?",
                         (self.content_text.rstrip(), self.content_text_add.rstrip()))
        if len(self.cur.fetchall()) == 0:
            self.cur.execute(f"INSERT INTO analytics VALUES (?,?,?,?)", (
                self.content_text.rstrip(), self.content_text_add.rstrip(), self.a_rate,
                str(self.publish_date)[:16]))
            self.conn.commit()


if __name__ == '__main__':
    inter = Interface()
    inter.input_print()
