class Stationery:
    def __init__(self, title, size=None, draw_type=None):
        self.title = title
        self.size = size
        self.draw_type = draw_type

    def draw(self):
        res = ""
        if self.size is not None:
            res += f"Я рисую толщиной в {self.size}px. "
        else:
            res += f"Я красивый {self.title}! "
        if self.draw_type is not None:
            res += f"Я рисую {self.draw_type}"
        print(res)


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title, 1, None)


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title, None, 'штриховкой')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title, 5, 'жирненько')


pen = Pen('Ручка')
pen.draw()

pencil = Pencil('Карандаш')
pencil.draw()

handle = Handle('Ручка')
handle.draw()
