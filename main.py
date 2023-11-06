from kivy.storage.jsonstore import JsonStore
from kivy.core.window import Window
from kivy.core.image import Image as CoreImage
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from random import randint, random, shuffle
from math import floor
from os.path import exists, join
from kivy.clock import Clock
from kivy.utils import get_color_from_hex
from kivy.properties import NumericProperty, ListProperty, ObjectProperty, BooleanProperty, DictProperty, StringProperty
from kivy.graphics import Rectangle, Color
from kivy.core.audio import SoundLoader
from kivy.utils import platform
import os

if platform == 'android':
    from jnius import cast
    from jnius import autoclass
    PythonActivity = autoclass('org.renpy.android.PythonActivity')
    Intent = autoclass('android.content.Intent')
    String = autoclass('java.lang.String')
SIZE = 8
index = NumericProperty(0)
index = randint(0, 4)

class Interface(FloatLayout):
    COLORS = ListProperty()
    COLORS = ['#ff0019', '#31a8f7', '#00d695', '#fafa46', '#cf55d5']
    color = ListProperty([0, 0, 0])
    color2 = ListProperty([0, 0, 0])
    color = get_color_from_hex(COLORS[randint(0, 4)])
    cooolor = get_color_from_hex(COLORS[randint(0, 4)])
    brd_col_list = ListProperty()
    brd_col_list = [None] * 64
    col_list = ListProperty()
    col_list = [None] * 64
    temp_list = ListProperty()
    tempo_list = ListProperty()
    pop = ObjectProperty()
    nextpop = ObjectProperty()
    pos_list = ListProperty()
    pos_list = [
     [
      0, 0], [0, 0.125], [0, 0.25], [0, 0.375], [0, 0.5], [0, 0.625], [0, 0.75], [0, 0.875], [0.125, 0], [0.125, 0.125], [0.125, 0.25], [0.125, 0.375], [0.125, 0.5], [0.125, 0.625], [0.125, 0.75], [0.125, 0.875], [0.25, 0], [0.25, 0.125], [0.25, 0.25], [0.25, 0.375], [0.25, 0.5], [0.25, 0.625], [0.25, 0.75], [0.25, 0.875], [0.375, 0], [0.375, 0.125], [0.375, 0.25], [0.375, 0.375], [0.375, 0.5], [0.375, 0.625], [0.375, 0.75], [0.375, 0.875], [0.5, 0], [0.5, 0.125], [0.5, 0.25], [0.5, 0.375], [0.5, 0.5], [0.5, 0.625], [0.5, 0.75], [0.5, 0.875], [0.625, 0], [0.625, 0.125], [0.625, 0.25], [0.625, 0.375], [0.625, 0.5], [0.625, 0.625], [0.625, 0.75], [0.625, 0.875], [0.75, 0], [0.75, 0.125], [0.75, 0.25], [0.75, 0.375], [0.75, 0.5], [0.75, 0.625], [0.75, 0.75], [0.75, 0.875], [0.875, 0], [0.875, 0.125], [0.875, 0.25], [0.875, 0.375], [0.875, 0.5], [0.875, 0.625], [0.875, 0.75], [0.875, 0.875]]
    Ba_List = ListProperty()
    Ba_List = [
     'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2', 
     'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c1', 'c2', 'c3', 'c4', 
     'c5', 'c6', 'c7', 'c8', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 
     'd7', 'd8', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 
     'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'g1', 'g2', 
     'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'h1', 'h2', 'h3', 'h4', 
     'h5', 'h6', 'h7', 'h8']
    Balls_List = ListProperty()
    Balls_List = [
     'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2', 
     'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c1', 'c2', 'c3', 'c4', 
     'c5', 'c6', 'c7', 'c8', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 
     'd7', 'd8', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 
     'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'g1', 'g2', 
     'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'h1', 'h2', 'h3', 'h4', 
     'h5', 'h6', 'h7', 'h8']
    Balls1_List = ListProperty()
    Balls1_List = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2', 'b3', 'b4', 
     'b5', 'b6', 'b7', 'b8', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 
     'c7', 'c8', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 
     'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f1', 'f2', 
     'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'g1', 'g2', 'g3', 'g4', 
     'g5', 'g6', 'g7', 'g8', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 
     'h7', 'h8']
    rgg = ListProperty()
    rgb = ListProperty()
    rgb = [None] * 64
    for i in range(64):
        random_color_number = randint(0, 4)
        get_color = get_color_from_hex(COLORS[random_color_number])
        brd_col_list[i] = random_color_number
        col_list[i] = brd_col_list[i]
        rgb[i] = get_color

    col_list = list(brd_col_list)
    textures = {}
    texture1 = CoreImage('images/logo.png', mipmap=True).texture
    textures['logo'] = texture1
    texture2 = CoreImage('images/gear.png', mipmap=True).texture
    textures['gear'] = texture2

    def __init__(self, **kwargs):
        super(Interface, self).__init__(**kwargs)
        self.app = App.get_running_app()

    def texxx(self, x):
        textures = {}
        texture1 = CoreImage('images/logo.png', mipmap=True).texture
        texture2 = CoreImage('images/gear.png', mipmap=True).texture
        if x == 'logo':
            return texture1

    def reset_with_shuffle(self):
        self.temp_list = []
        self.tempo_list = []
        c = list(zip(self.col_list, self.Ba_List))
        shuffle(c)
        self.col_list[:], self.Ba_List[:] = zip(*c)
        self.Balls1_List = list(self.Ba_List)
        self.brd_col_list = list(self.col_list)
        self.Balls_List = list(self.Ba_List)
        self.clear_widgets()
        for i in range(64):
            X = self.pos_list[i][0]
            Y = self.pos_list[i][1]
            b = str(self.Balls_List[i])
            self.add_widget(self.ids[b])
            self.ids[b].pos_hint = {'x': X, 'y': Y}

        if self.app.level_score < 1100:
            Best_score = self.app.score_file.get('Best')['value']
            if self.app.score > Best_score:
                self.app.score_file.put('Best', value=self.app.score)
                self.app.best_score = self.app.score
            self.app.score = 0
        self.app.level_score = 0

    def colooy(self, i):
        random_color_number = randint(0, 4)
        get_color = get_color_from_hex(self.COLORS[random_color_number])
        self.brd_col_list[i] = random_color_number
        return get_color

    def getcolor(self):
        for i in range(64):
            random_color_number = randint(0, 4)
            get_color = get_color_from_hex(self.COLORS[random_color_number])
            self.brd_col_list[i] = random_color_number
            self.rgb[i] = get_color
            return get_color

    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            return
        else:
            self.canvas.ask_update()
            xx = touch.x - self.x
            yy = touch.y - self.y
            element_x = self.width / SIZE
            element_pos_x = floor(xx / element_x)
            element_y = self.width / SIZE
            element_pos_y = floor(yy / element_y)
            ele_pos = int(element_pos_x * 8 + element_pos_y)
            self.will_removed = ListProperty()
            self.will_removed = [
             None] * 64
            self.will_removed[ele_pos] = self.brd_col_list[ele_pos]
            computing = True
            old_no = 1
            while computing:
                for i in range(64):
                    if self.will_removed[i] is not None:
                        self.compute(i)

                ele_number = [ x for x in self.will_removed if x is not None ]
                if len(ele_number) == old_no:
                    computing = False
                else:
                    old_no = len(ele_number)

            self.remove_balls(ele_pos)
            self.rearange_col_list()
            self.rearange_ball_list()
            self.check_moves()
            return

    def compute(self, i):
        if i not in (7, 15, 23, 31, 39, 47, 55, 63):
            if self.brd_col_list[i] == self.brd_col_list[i + 1]:
                if self.will_removed[i + 1] == None:
                    self.will_removed[i + 1] = self.brd_col_list[i + 1]
        if i not in (0, 8, 16, 24, 32, 40, 48, 56):
            if self.brd_col_list[i] == self.brd_col_list[i - 1]:
                if self.will_removed[i - 1] == None:
                    self.will_removed[i - 1] = self.brd_col_list[i - 1]
        if i not in (56, 57, 58, 59, 60, 61, 62, 63):
            if self.brd_col_list[i] == self.brd_col_list[i + 8]:
                if self.will_removed[i + 8] == None:
                    self.will_removed[i + 8] = self.brd_col_list[i + 8]
        if i not in (0, 1, 2, 3, 4, 5, 6, 7):
            if self.brd_col_list[i] == self.brd_col_list[i - 8]:
                if self.will_removed[i - 8] == None:
                    self.will_removed[i - 8] = self.brd_col_list[i - 8]
        return

    def remove_balls(self, ele_pos):
        ss = [ x for x in self.will_removed if x is not None ]
        if len(ss) > 1:
            self.play_sounds()
            self.app.add3_score(len(ss))
            for index, x in enumerate(self.will_removed):
                if x == self.brd_col_list[ele_pos]:
                    b = str(self.Balls_List[index])
                    self.remove_widget(self.ids[b])
                    self.Balls_List[index] = None

            dd = self.brd_col_list[ele_pos]
            for index, x in enumerate(self.Balls_List):
                if x == None:
                    self.brd_col_list[index] = None

        return

    def rearange_col_list(self):
        l1 = [ x for x in self.brd_col_list[0:8] if x is not None ]
        l2 = [ x for x in self.brd_col_list[8:16] if x is not None ]
        l3 = [ x for x in self.brd_col_list[16:24] if x is not None ]
        l4 = [ x for x in self.brd_col_list[24:32] if x is not None ]
        l5 = [ x for x in self.brd_col_list[32:40] if x is not None ]
        l6 = [ x for x in self.brd_col_list[40:48] if x is not None ]
        l7 = [ x for x in self.brd_col_list[48:56] if x is not None ]
        l8 = [ x for x in self.brd_col_list[56:64] if x is not None ]
        self.temp_list = []
        for x in l1:
            self.temp_list.append(x)

        for n in range(len(l1), 8):
            self.temp_list.append(None)

        for x in l2:
            self.temp_list.append(x)

        for n in range(len(l2), 8):
            self.temp_list.append(None)

        for x in l3:
            self.temp_list.append(x)

        for n in range(len(l3), 8):
            self.temp_list.append(None)

        for x in l4:
            self.temp_list.append(x)

        for n in range(len(l4), 8):
            self.temp_list.append(None)

        for x in l5:
            self.temp_list.append(x)

        for n in range(len(l5), 8):
            self.temp_list.append(None)

        for x in l6:
            self.temp_list.append(x)

        for n in range(len(l6), 8):
            self.temp_list.append(None)

        for x in l7:
            self.temp_list.append(x)

        for n in range(len(l7), 8):
            self.temp_list.append(None)

        for x in l8:
            self.temp_list.append(x)

        for n in range(len(l8), 8):
            self.temp_list.append(None)

        self.brd_col_list = self.temp_list
        return

    def rearange_ball_list(self):
        b1 = [ x for x in self.Balls_List[0:8] if x is not None ]
        b2 = [ x for x in self.Balls_List[8:16] if x is not None ]
        b3 = [ x for x in self.Balls_List[16:24] if x is not None ]
        b4 = [ x for x in self.Balls_List[24:32] if x is not None ]
        b5 = [ x for x in self.Balls_List[32:40] if x is not None ]
        b6 = [ x for x in self.Balls_List[40:48] if x is not None ]
        b7 = [ x for x in self.Balls_List[48:56] if x is not None ]
        b8 = [ x for x in self.Balls_List[56:64] if x is not None ]
        self.tempo_list = []
        for x in b1:
            self.tempo_list.append(x)

        for n in range(len(b1), 8):
            self.tempo_list.append(None)

        for x in b2:
            self.tempo_list.append(x)

        for n in range(len(b2), 8):
            self.tempo_list.append(None)

        for x in b3:
            self.tempo_list.append(x)

        for n in range(len(b3), 8):
            self.tempo_list.append(None)

        for x in b4:
            self.tempo_list.append(x)

        for n in range(len(b4), 8):
            self.tempo_list.append(None)

        for x in b5:
            self.tempo_list.append(x)

        for n in range(len(b5), 8):
            self.tempo_list.append(None)

        for x in b6:
            self.tempo_list.append(x)

        for n in range(len(b6), 8):
            self.tempo_list.append(None)

        for x in b7:
            self.tempo_list.append(x)

        for n in range(len(b7), 8):
            self.tempo_list.append(None)

        for x in b8:
            self.tempo_list.append(x)

        for n in range(len(b8), 8):
            self.tempo_list.append(None)

        self.Balls_List = self.tempo_list
        for i in range(64):
            if self.tempo_list[i] == self.Balls1_List[i]:
                lp = 3
            elif self.tempo_list[i] == None:
                lp = 3
            else:
                self.reposition(i, self.tempo_list)

        return

    def reposition(self, ele_no, tmp):
        pos_list = [
         [
          0, 0], [0, 0.125], [0, 0.25], [0, 0.375], [0, 0.5], [0, 0.625], [0, 0.75], [0, 0.875], [0.125, 0], [0.125, 0.125], [0.125, 0.25], [0.125, 0.375], [0.125, 0.5], [0.125, 0.625], [0.125, 0.75], [0.125, 0.875], [0.25, 0], [0.25, 0.125], [0.25, 0.25], [0.25, 0.375], [0.25, 0.5], [0.25, 0.625], [0.25, 0.75], [0.25, 0.875], [0.375, 0], [0.375, 0.125], [0.375, 0.25], [0.375, 0.375], [0.375, 0.5], [0.375, 0.625], [0.375, 0.75], [0.375, 0.875], [0.5, 0], [0.5, 0.125], [0.5, 0.25], [0.5, 0.375], [0.5, 0.5], [0.5, 0.625], [0.5, 0.75], [0.5, 0.875], [0.625, 0], [0.625, 0.125], [0.625, 0.25], [0.625, 0.375], [0.625, 0.5], [0.625, 0.625], [0.625, 0.75], [0.625, 0.875], [0.75, 0], [0.75, 0.125], [0.75, 0.25], [0.75, 0.375], [0.75, 0.5], [0.75, 0.625], [0.75, 0.75], [0.75, 0.875], [0.875, 0], [0.875, 0.125], [0.875, 0.25], [0.875, 0.375], [0.875, 0.5], [0.875, 0.625], [0.875, 0.75], [0.875, 0.875]]
        posX = pos_list[ele_no][0]
        posY = pos_list[ele_no][1]
        b = str(tmp[ele_no])
        anime = Animation(pos_hint={'x': posX, 'y': posY}, t='out_bounce', duration=1.0)
        anime.start(self.ids[b])

    def check_moves(self):
        su = 0
        i = 1
        for i in range(63):
            if self.brd_col_list[i] is not None:
                if self.brd_col_list[i] == self.brd_col_list[i + 1]:
                    su += 1
            if i < 56:
                if self.brd_col_list[i] is not None:
                    if self.brd_col_list[i] == self.brd_col_list[i + 8]:
                        su += 1

        if su == 0:
            if self.app.level_score >= 1100:
                self.nextpop.open()
            else:
                Best_score = self.app.score_file.get('Best')['value']
                if self.app.score > Best_score:
                    self.pop.txtscore.text = 'New High Score'
                else:
                    self.pop.txtscore.text = 'Your Score'
                self.pop.open()
        return

    def play_sounds(self):
        self.bounce_sound = SoundLoader.load('bouncing.ogg')
        self.bounce_sound.volume = 0.3
        self.bounce_sound.play()

    def share_score(self):
        if platform == 'android':
            intent = Intent()
            intent.setAction(Intent.ACTION_SEND)
            intent.setType('text/plain')
            score = str(self.app.score)
            link = 'https://play.google.com/store/apps/details?id=org.ballsgravity.ballsgravity'
            share_text = ('I scored {} points on Balls Gravity Game. {}').format(score, link)
            intent.putExtra(Intent.EXTRA_TEXT, String(share_text))
            chooser = Intent.createChooser(intent, String('Share your score'))
            PythonActivity.mActivity.startActivity(chooser)


class Square(FloatLayout):

    def __init__(self, **kwargs):
        super(Square, self).__init__(**kwargs)
        self.bind(pos=self.do_layout, size=self.do_layout)

    def do_layout(self, *args):
        s = self.width
        if self.width > self.height:
            s = self.height
        for child in self.children:
            child.size = (
             s, s)
            child.center = self.center

    def opp(self):
        print('opp')


class aaaaa(BoxLayout):
    main = ObjectProperty()
    pop = ObjectProperty()
    nextpop = ObjectProperty()


class Main(BoxLayout):
    inter = ObjectProperty()
    pop = ObjectProperty()
    nextpop = ObjectProperty()

    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        self.bind(pos=self.do_layout, size=self.do_layout)

    def do_layout(self, *args):
        s = self.width
        if self.width > self.height:
            s = self.height
        for child in self.children:
            child.size = (
             s, s)
            child.center = self.center

    def colol(self):
        return get_color_from_hex('#5F1114')


class nextlevelpopup(ModalView):
    pass


class gameoverpopup(ModalView):
    pass


class BallyApp(App):
    time = NumericProperty(0)
    score = NumericProperty(0)
    level_score = NumericProperty(0)
    best_score = NumericProperty()

    def build(self):
        self.file_dir = '/home/ahmed/sdcard/Android/data/org.ballsgravity/'
        if platform == 'android':
            self.file_dir = '/sdcard/Android/data/org.ballsgravity/'
        if not os.path.exists(self.file_dir):
            os.makedirs(self.file_dir)
        self.score_fn = join(self.file_dir, 'best_score.json')
        self.score_file = JsonStore(self.score_fn)
        try:
            self.score_file.get('Best')['value']
        except:
            self.score_file.put('Best', value=0)

        self.score = 0
        self.best_score = self.score_file.get('Best')['value']
        self.textures = {}
        texture1 = CoreImage('images/logo.png', mipmap=True).texture
        self.textures['logo'] = texture1
        texture2 = CoreImage('images/gear.png', mipmap=True).texture
        self.textures['gear'] = texture2
        Clock.schedule_interval(self.timer, 1.0 / 20)
        Aaaaa = aaaaa()
        return Aaaaa

    def on_pause(self):
        return True
    def on_resume(self):
        pass
    def timer(self, ti):
        self.time += ti
    def Best_score(self):
        self.best_score = self.score_file.get('Best')['value']
    def add1_score(self, ball_no):
        if ball_no == 2:
            self.score += 20
        elif ball_no > 2 and ball_no < 5:
            self.score += 40
        elif ball_no > 4 and ball_no < 7:
            self.score += 60
        elif ball_no > 6:
            self.score += 80
        print(self.score)
    def add2_score(self, ball_no):
        self.score += 10 * ball_no
    def add3_score(self, ball_no):
        if ball_no == 2:
            self.score += ball_no * 10
            self.level_score += ball_no * 10
        elif ball_no == 3:
            self.score += ball_no * 20
            self.level_score += ball_no * 20
        elif ball_no == 4:
            self.score += ball_no * 30
            self.level_score += ball_no * 30
        elif ball_no == 5:
            self.score += ball_no * 40
            self.level_score += ball_no * 40
        elif ball_no == 6:
            self.score += ball_no * 50
            self.level_score += ball_no * 50
        elif ball_no == 7:
            self.score += ball_no * 60
            self.level_score += ball_no * 60
        elif ball_no == 8:
            self.score += ball_no * 70
            self.level_score += ball_no * 70
        elif ball_no > 8:
            self.score += ball_no * 80
            self.level_score += ball_no * 80
if __name__ == '__main__':
    BallyApp().run()