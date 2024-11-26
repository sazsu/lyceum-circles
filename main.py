from random import randint
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPoint

from ui import Ui_MainWindow


class Circles(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.do_paint = False
		self.drawButton.clicked.connect(self.paint)

	def paintEvent(self, a0):
		if self.do_paint:
			width, height = self.width(), self.height()
			qp = QPainter()
			qp.begin(self)
			for i in range(randint(3, 10)):
				x, y = randint(0, width), randint(0, height)
				radii = randint(10, 100)
				color = QColor(
					randint(0, 255),
					randint(0, 255),
					randint(0, 255),
				)
				self.draw_circle(
					qp,
					x, y,
					radii,
					color
				)
			qp.end()
		self.do_paint = False

	def paint(self):
		self.do_paint = True
		self.update()

	@staticmethod
	def draw_circle(qp: QPainter, x: int, y: int, radii: int, color: QColor):
		qp.setBrush(color)
		qp.drawEllipse(
			QPoint(x, y),
			radii,
			radii
		)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	circles = Circles()
	circles.show()
	sys.exit(app.exec())
