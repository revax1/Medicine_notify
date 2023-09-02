import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget, QVBoxLayout, QWidget
from PyQt5.QtGui import QColor  # เพิ่มบรรทัดนี้

class ChessboardApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chessboard")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.chessboard = QTableWidget(5, 8)
        self.chessboard.horizontalHeader().setVisible(False)
        self.chessboard.verticalHeader().setVisible(False)
        self.chessboard.setEditTriggers(QTableWidget.NoEditTriggers)
        self.chessboard.setSelectionMode(QTableWidget.NoSelection)

        layout.addWidget(self.chessboard)
        
        self.showFullScreen()

        self.populateChessboard()

    def populateChessboard(self):
        for row in range(5):
            for col in range(8):
                item = QTableWidgetItem()
                if (row + col) % 2 == 0:
                    item.setBackground(QColor(255, 206, 158))  # Light color
                else:
                    item.setBackground(QColor(209, 139, 71))   # Dark color
                self.chessboard.setItem(row, col, item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChessboardApp()
    window.show()
    sys.exit(app.exec_())
