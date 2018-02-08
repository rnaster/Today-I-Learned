import pymysql.cursors
import re
import pandas as pd
import os

os.chdir('c:/users/user/downloads')

class Recovery:
    def __init__(self, filename):
        self._filename = filename
        self.undo = []
        self.read_log()
        self.parse_log()
        self.connect_db()
        self.get_pk_list()
    def connect_db(self):
        self.conn = pymysql.connect(
        host = '147.46.15.66',
        user = 'blpomspo',
        password = 'bde1234',
        db = 'blpomspo',
        charset = 'utf8',
        cursorclass = pymysql.cursors.DictCursor
        )
    def parse_log(self):
        self.log_parsing = list(map(lambda x: re.split('[, ]+', x), self._log))
        self.find_ckpt()
        self.generating_undo()
    def read_log(self):
        self._log = []
        with open(self._filename, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                self._log.append(line.rstrip())
    def find_ckpt(self):
        self.startpt = 0
        for idx in range(len(self.log_parsing)-1, -1, -1):
            if self.log_parsing[idx][0] == 'checkpoint':
                self.startpt = idx
                break
    def generating_undo(self):
        undo, pt = [], self.startpt
        log = self.log_parsing
        undo.extend(log[pt][1:])
        for idx in range(pt, len(log)):
            if log[idx][-1] in ['start', 'abort', 'commit']:
                if log[idx][0] in undo:
                    undo.remove(log[idx][0])
                else : undo.append(log[idx][0])
        self.undo = undo
    def redo_phase(self, pt, logs):
        for idx in range(pt, len(logs)):
            if logs[idx][0] not in self.undo and logs[idx][1] not in ['start', 'commit', 'abort']:
                self._recovery(logs[idx])
    def _recovery(self, log):
        if len(log) == 4: change, _ = log[-2:]
        else: change = log[-1]
        table, pk_val, col = log[1].split('.')
        pk = self.pk_list.loc[table][0]
        with self.conn.cursor() as cursor:
            sql = 'update %s set %s = "%s" where %s = "%s"'
            cursor.execute(sql %(table, col, change, pk, pk_val))
        self.conn.commit()
    def undo_phase(self, pt, logs):
        for idx in range(len(logs)-1, pt-1, -1):
            if logs[idx][0] in self.undo:
                if logs[idx][1] == 'start': self.undo.remove(logs[idx][0]); continue
                self._recovery(logs[idx])
    def recovery(self):
        pt, logs = self.startpt+1, self.log_parsing
        self.redo_phase(pt, logs)
        self.undo_phase(pt, logs)
        print('Recovery Done!')
    def get_pk_list(self):
        with self.conn.cursor() as cursor:
            sql = 'SELECT TABLE_NAME, GROUP_CONCAT(COLUMN_NAME) as pk \
                  FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE \
                  WHERE TABLE_SCHEMA = "%s" AND CONSTRAINT_NAME="%s" \
                  GROUP BY TABLE_NAME'
            cursor.execute(sql %('blpomspo', 'primary'))
            self.pk_list = pd.DataFrame(cursor.fetchall()).set_index('TABLE_NAME')


a = Recovery('recovery.txt')
a.recovery()

