
import sqlite3
import curses
from datetime import datetime

class Highscore:
	def __init__(self):
		self.win = curses.newwin(15, 40, 5, 5)

	def showHighscore(self):
		self.win.clear()
		self.win.box()
		line = 1
		for row in self.getScores():
			out = "{0:20} {1:>7} {2:>7}"
			self.win.addstr(line, 2, out.format(str(row[0]), str(row[1]), str(row[2])))
			line += 1
		self.win.refresh()

	def addScore(self, lines, blocks):
		conn = sqlite3.connect("/home/aloeee/progTest/python/ctris/scores.db")
		cursor = conn.cursor()
		cursor.execute("CREATE TABLE IF NOT EXISTS SCORES (ID INTEGER PRIMARY KEY, DATETIME TEXT, LINES INTEGER, BLOCKS INTEGER)")

		sql = "INSERT INTO SCORES (DATETIME, LINES, BLOCKS) VALUES (?, ?, ?)"
		cursor.execute(sql, [datetime.now(), lines, blocks])
		conn.commit()
		cursor.close()
		conn.close()

	def getScores(self, limit = 10):
		conn = sqlite3.connect("/home/aloeee/progTest/python/ctris/scores.db")
		cursor = conn.cursor()
		cursor.execute("CREATE TABLE IF NOT EXISTS SCORES (ID INTEGER PRIMARY KEY, DATETIME TEXT, LINES INTEGER, BLOCKS INTEGER)")

		sql = "SELECT DATETIME, BLOCKS, LINES FROM SCORES ORDER BY LINES DESC LIMIT ?"
		cursor.execute(sql, [limit])
		result = []
		for row in cursor:
			#result.append([row[0], row[1], row[2]])
			result.append([datetime.strptime(row[0].split(".")[0], "%Y-%m-%d %H:%M:%S"), row[1], row[2]])
		cursor.close()
		conn.close()
		return result


