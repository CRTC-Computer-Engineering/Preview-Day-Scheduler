#!/usr/bin/env python

import wx
import logging as log
import yaml

import gui.noname as gui


# Function By Joe
def yaml_loader(fileDir, data = None):
    if data != None:
        # Write YAML file
        with open(fileDir, "w+") as outfile:
            yaml.dump(data, outfile)

    # Read YAML file
    with open(fileDir, 'r') as stream:
        return yaml.safe_load(stream)

class program_class():
    def __init__(self, long_name, capacity, progress_bar, day = None):
        self.long_name = long_name
        self.capacity = capacity
        self.day = day
        self.current_students = 0
        self.progress_bar = progress_bar
        self.day_one_list = []
        self.day_two_list = []
    
    def add_student(self, student_name):
        if len(self.day_one_list) > self.capacity:
            self.day_one_list.append(student_name)
        elif len(self.day_two_list) > self.capacity:
            self.day_two_list.append(student_name)
        else:
            return "Full"


class scheduler_program(gui.root_frame):
    def __init__(self, parent): # Runs once when init
        gui.root_frame.__init__(self, parent)

        self.settings = yaml_loader("data\\settings.yaml") # Load the settings

        self.programs = []
        for program, program_data in self.settings.items():
            self.programs.append(program_class(program_data["name"], program_data["student_limit"], self.ceGauge ))

        program_names = []
        for program in self.programs:
            program_names.append(program.name)
            print(program.size)

        self.pickOne.SetItems(program_names)
        self.pickTwo.SetItems(program_names)

if __name__ == "__main__":
    log.basicConfig(level=log.DEBUG) # Set logging level
    log.debug("Program Started.") # Debug message

    app = wx.App(redirect=False) # Show console output for errors
    root_window = scheduler_program(None) # No parent
    root_window.Show() # Show the window
    app.MainLoop() # Run the main GUI loop
