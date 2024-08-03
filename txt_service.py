import os


class TXTService:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_txt(self):
        try:
            with open(self.file_path, 'r') as txtfile:
                movie_codes = [line.strip().split()[-1][:-4].replace('_', '-') for line in txtfile.readlines() if '.mp4' in line]
                return movie_codes
        except FileNotFoundError:
            print(f"Arquivo {self.file_path} não encontrado.")
            return []
