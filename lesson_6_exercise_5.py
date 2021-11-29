class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start rendering')


class Pen(Stationery):
    def draw(self):
        print('Pen rendering')


class Pencil(Stationery):
    def draw(self):
        print('Pencil rendering')


class Handle(Stationery):
    def draw(self):
        print('Handle rendering')

pen = Pen('Ball pen')
pencil = Pencil('Graphite pencil')
handle = Handle('Permanent marker')

pen.draw()
pencil.draw()
handle.draw()

print(pen.title)
print(pencil.title)
print(handle.title)
