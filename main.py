import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from kot_design import Ui_MainWindow


class CatDb(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.lines = []
        self.user_info = []
        self.raw_user_info = []
        self.line = 0
        self.file_name = ""
        self.current_line = ""
        self.lst_upd = 0

        self.ui.file_locate_btn.clicked.connect(self.file_locate)
        self.ui.find_lst_update_btn.clicked.connect(self.find_lst_update)
        self.ui.save_btn.clicked.connect(self.save_info)
        self.ui.prev_line_btn.clicked.connect(self.prev_line)
        self.ui.next_line_btn.clicked.connect(self.next_line)

    def file_locate(self):
        self.file_name = QFileDialog.getOpenFileName(self)[0]
        self.ui.file_locate_le.setText(str(self.file_name))

    def find_lst_update(self):
        if self.file_name == "":
            QMessageBox.critical(self, "ERROR", "Выберите путь до файла в настройках!")
        else:
            find_upd = False
            with open(self.file_name, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.rstrip()
                    self.lines.append(line)

                    if "[UPDATE]" in line:
                        self.current_line = line
                        find_upd = True

                        if "@" in line and len(line) > 80:
                            info = line[line.find(':', line.find("@")) + 1:].split(", ")
                            info[-1] = info[-1][:info[-1].find("[UPDATE]")]
                            print(info)
                            for j in range(14):
                                if j < len(info):
                                    self.user_info.append(info[j])
                                else:
                                    self.user_info.append("")

                            self.raw_user_info = self.user_info[:]

                            self.ui.name_le.setText(self.user_info[0])
                            self.ui.age_le.setText(self.user_info[1])
                            self.ui.nick_le.setText(self.user_info[2])
                            self.ui.discord_le.setText(self.user_info[3])
                            self.ui.town_le.setText(self.user_info[4])
                            self.ui.country_le.setText(self.user_info[5])
                            self.ui.time_game_le.setText(self.user_info[6])
                            self.ui.all_time_le.setText(self.user_info[7])
                            self.ui.your_help_le.setText(self.user_info[8])
                            self.ui.our_help_le.setText(self.user_info[9])
                            self.ui.micro_le.setText(self.user_info[10])
                            self.ui.dislike_le.setText(self.user_info[11])
                            self.ui.lvl_game_le.setText(self.user_info[12])
                            self.ui.reason_le.setText(self.user_info[13])

                            self.lst_upd = self.line

                    if find_upd is False:
                        self.line += 1

        print(self.lines)

    def save_info(self):

        self.user_info[0] = self.ui.name_le.text()
        self.user_info[1] = self.ui.age_le.text()
        self.user_info[2] = self.ui.nick_le.text()
        self.user_info[3] = self.ui.discord_le.text()
        self.user_info[4] = self.ui.town_le.text()
        self.user_info[5] = self.ui.country_le.text()
        self.user_info[6] = self.ui.time_game_le.text()
        self.user_info[7] = self.ui.all_time_le.text()
        self.user_info[8] = self.ui.your_help_le.text()
        self.user_info[9] = self.ui.our_help_le.text()
        self.user_info[10] = self.ui.micro_le.text()
        self.user_info[11] = self.ui.dislike_le.text()
        self.user_info[12] = self.ui.lvl_game_le.text()
        self.user_info[13] = self.ui.reason_le.text()


        with open(self.file_name, 'r', encoding='utf-8') as f:
            bcp_file_name = self.file_name[:self.file_name.find(".")] + "_bcp.txt"
            with open(bcp_file_name, 'w', encoding="utf-8") as g:
                g.writelines(f.readlines())

        with open(self.file_name, 'w', encoding='utf-8') as f:
            for i in range(0, len(self.lines)):
                if i == self.line:
                    #s = self.current_line[:self.current_line.find(":", self.current_line.find("@")) + 1] + ", ".join(self.user_info)[:-2]
                    s = self.lines[i][:self.lines[i].find(":", self.lines[i].find("@")) + 1] + ", ".join(self.user_info)[:-2]
                    if "[UPDATE]" not in self.lines[i]:
                        s += "[UPDATE]"
                    f.write(s + "\n")
                elif i == self.lst_upd:
                    if "[UPDATE]" in self.lines[i]:
                        f.write(self.lines[i][:self.lines[i].find("[UPDATE]", self.lines[i].find(":"))] + "\n")
                else:
                    f.write(self.lines[i] + "\n")

        QMessageBox().question(self, "Сохранить изменения", "Уверены что хотите сохранить изменения?")

    def prev_line(self):

        user_info = []

        user_info.append(self.ui.name_le.text())
        user_info.append(self.ui.age_le.text())
        user_info.append(self.ui.nick_le.text())
        user_info.append(self.ui.discord_le.text())
        user_info.append(self.ui.town_le.text())
        user_info.append(self.ui.country_le.text())
        user_info.append(self.ui.time_game_le.text())
        user_info.append(self.ui.all_time_le.text())
        user_info.append(self.ui.your_help_le.text())
        user_info.append(self.ui.our_help_le.text())
        user_info.append(self.ui.micro_le.text())
        user_info.append(self.ui.dislike_le.text())
        user_info.append(self.ui.lvl_game_le.text())
        user_info.append(self.ui.reason_le.text())

        s = self.lines[self.line][
                                :self.lines[self.line].find(":", self.lines[self.line].find("@")) + 1] + ", ".join(
            user_info)[:-2]
        if "[UPDATE]" in self.lines[self.line]:
            s += "[UPDATE]"

        self.lines[self.line] = s[:] + "\n"
        print(self.lines)

        self.ui.name_le.setText("")
        self.ui.age_le.setText("")
        self.ui.nick_le.setText("")
        self.ui.discord_le.setText("")
        self.ui.town_le.setText("")
        self.ui.country_le.setText("")
        self.ui.time_game_le.setText("")
        self.ui.all_time_le.setText("")
        self.ui.your_help_le.setText("")
        self.ui.our_help_le.setText("")
        self.ui.micro_le.setText("")
        self.ui.dislike_le.setText("")
        self.ui.lvl_game_le.setText("")
        self.ui.reason_le.setText("")

        self.line -= 1
        while ("@" not in self.lines[self.line] or len(self.lines[self.line]) < 80) and self.line >= 0:
            self.line -= 1
            if self.line < 0:
                break

        print(self.line)

        if self.line < 0:
            QMessageBox.warning(self, "Warning!", "Достигнуто начало файла!")
        else:
            line = self.lines[self.line]
            self.user_info = []
            if "@" in line and len(line) > 80:
                info = line[line.find(':', line.find("@")) + 1:].split(", ")
                # info[-1] = info[-1][:info[-1].find("[UPDATE]")]
                for j in range(14):
                    if j < len(info):
                        self.user_info.append(info[j])
                    else:
                        self.user_info.append("")

                self.raw_user_info = self.user_info[:]

                self.ui.name_le.setText(self.user_info[0])
                self.ui.age_le.setText(self.user_info[1])
                self.ui.nick_le.setText(self.user_info[2])
                self.ui.discord_le.setText(self.user_info[3])
                self.ui.town_le.setText(self.user_info[4])
                self.ui.country_le.setText(self.user_info[5])
                self.ui.time_game_le.setText(self.user_info[6])
                self.ui.all_time_le.setText(self.user_info[7])
                self.ui.your_help_le.setText(self.user_info[8])
                self.ui.our_help_le.setText(self.user_info[9])
                self.ui.micro_le.setText(self.user_info[10])
                self.ui.dislike_le.setText(self.user_info[11])
                self.ui.lvl_game_le.setText(self.user_info[12])
                self.ui.reason_le.setText(self.user_info[13])

    def next_line(self):

        user_info = []

        user_info.append(self.ui.name_le.text())
        user_info.append(self.ui.age_le.text())
        user_info.append(self.ui.nick_le.text())
        user_info.append(self.ui.discord_le.text())
        user_info.append(self.ui.town_le.text())
        user_info.append(self.ui.country_le.text())
        user_info.append(self.ui.time_game_le.text())
        user_info.append(self.ui.all_time_le.text())
        user_info.append(self.ui.your_help_le.text())
        user_info.append(self.ui.our_help_le.text())
        user_info.append(self.ui.micro_le.text())
        user_info.append(self.ui.dislike_le.text())
        user_info.append(self.ui.lvl_game_le.text())
        user_info.append(self.ui.reason_le.text())

        s = self.lines[self.line][
            :self.lines[self.line].find(":", self.lines[self.line].find("@")) + 1] + ", ".join(
            user_info)[:-2]

        if "[UPDATE]" in self.lines[self.line]:
            s += "[UPDATE]"

        self.lines[self.line] = s[:] + "\n"

        self.ui.name_le.setText("")
        self.ui.age_le.setText("")
        self.ui.nick_le.setText("")
        self.ui.discord_le.setText("")
        self.ui.town_le.setText("")
        self.ui.country_le.setText("")
        self.ui.time_game_le.setText("")
        self.ui.all_time_le.setText("")
        self.ui.your_help_le.setText("")
        self.ui.our_help_le.setText("")
        self.ui.micro_le.setText("")
        self.ui.dislike_le.setText("")
        self.ui.lvl_game_le.setText("")
        self.ui.reason_le.setText("")

        self.line += 1
        while ("@" not in self.lines[self.line] or len(self.lines[self.line]) < 80) and self.line < len(self.lines):
            self.line += 1
            if self.line >= len(self.lines):
                break

        print(self.line)

        if self.line >= len(self.lines):
            QMessageBox.warning(self, "Warning!", "Достигнут конец файла!")
        else:
            line = self.lines[self.line]
            self.user_info = []
            if "@" in line and len(line) > 80:
                info = line[line.find(':', line.find("@")) + 1:].split(", ")
                # info[-1] = info[-1][:info[-1].find("[UPDATE]")]
                for j in range(14):
                    if j < len(info):
                        self.user_info.append(info[j])
                    else:
                        self.user_info.append("")

                self.raw_user_info = self.user_info[:]

                self.ui.name_le.setText(self.user_info[0])
                self.ui.age_le.setText(self.user_info[1])
                self.ui.nick_le.setText(self.user_info[2])
                self.ui.discord_le.setText(self.user_info[3])
                self.ui.town_le.setText(self.user_info[4])
                self.ui.country_le.setText(self.user_info[5])
                self.ui.time_game_le.setText(self.user_info[6])
                self.ui.all_time_le.setText(self.user_info[7])
                self.ui.your_help_le.setText(self.user_info[8])
                self.ui.our_help_le.setText(self.user_info[9])
                self.ui.micro_le.setText(self.user_info[10])
                self.ui.dislike_le.setText(self.user_info[11])
                self.ui.lvl_game_le.setText(self.user_info[12])
                self.ui.reason_le.setText(self.user_info[13])


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = CatDb()
    window.show()

    sys.exit(app.exec())
