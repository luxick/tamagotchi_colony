#!/usr/bin/python
# coding=UTF-8

from mayorgotchi import Mayorgotchi
from kinggotchi import Kinggotchi
from config import *
import curses
import time

class cursesUI:
    kingdomview = True
    villagenr = 0
    percentage = True
    running = True
    ticks = 0
    king = Kinggotchi()
    
    def __init__(self):
        self.kingdomview = True
        self.villagenr = 0
        self.percentage = True
        self.running = True
        self.paused = start_paused

        self.stdscr = curses.initscr()
        curses.noecho()
        curses.curs_set(0)
        self.stdscr.keypad(1)
        self.stdscr.nodelay(1)

        height, width = self.stdscr.getmaxyx()
        self.win = curses.newpad(16383, width)
        
        self.king.createKingdom(50)

        while self.running:
            self.build_screen(self.king, self.ticks)
            
            if not self.paused:
                self.king.step()
                self.ticks += 1

    def build_screen(self, king, ticks):

        height, width = self.stdscr.getmaxyx()
        self.win.addstr(0, 0, 'Tamagotchi Colony (alpha) - currently at tick '+str(ticks)+'.')

        if self.kingdomview:
            self.win.addstr(1, 0, '-----------------------------------')
            self.win.addstr(2, 0, '[q]Exit [p]Pause [v]Village View')
            self.win.addstr(3, 0, '-----------------------------------')
            self.win.addstr(5, 0, king.show_kingdom())
        else:
            self.win.addstr(1, 0, '------------------------------------------------------------------')
            self.win.addstr(2, 0, '[q]Exit [p]Pause [v]Kingdom View [n/m]Previous/Next [s]Percentage')
            self.win.addstr(3, 0, '------------------------------------------------------------------')
            self.win.addstr(5, 0, king.myvillages[self.villagenr].give_status(self.percentage))

        self.win.clrtoeol()
        self.win.clrtobot()
        self.win.refresh(0, 0, 0, 0, height-1, width-1)

        key = self.stdscr.getch()
        if key == ord('q'):
            self.running = False
        elif key == ord('p'):
            self.paused = not self.paused
        elif key == ord('v'):
            self.win.move(0, 0)
            self.win.clrtobot()
            self.kingdomview = not self.kingdomview
        elif key == ord('n'):
            if not self.kingdomview:
                self.villagenr -= 1
        elif key == ord('m'):
            if not self.kingdomview:
                self.villagenr += 1
        elif key == ord('s'):
            if not self.kingdomview:
                self.percentage = not self.percentage
        elif key < 0:
            time.sleep(ticklenght)
        if not self.running:
            curses.endwin()

ui = cursesUI()