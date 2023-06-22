from calnedar import MYcalendar
import utils.utils as Utils
from flet import (
    Column,
    Container,
    ElevatedButton,
    Page,
    Row,
    Text,
    UserControl,
    border_radius,
    colors,
    Image,
    Ref,
    Divider,
    Text

)
import re

import mode
import consts as consts


class eventHandles():
    def __init__(self, calculator):
        self.app = calculator

    def one_var_handle_click(self, e):
        self.app.reset()
        if (self.app.modeText.value == "one variable solver"):
            self.app.mode = mode.Mode.REGULAR
            self.app.solverRef.current.on_click = self.app.calculate
            self.app.modeText.value = ""
            self.app.selectedFunctionRef = None
            e.control.opacity = 0.5
        else:
            self.app.solverRef.current.on_click = self.app.one_var_solver
            self.app.mode = mode.Mode.ONE_VARIABLE_SOLVER
            self.app.modeText.value = "one variable solver"
            e.control.opacity = 1
            if (self.app.selectedFunctionRef):
                self.app.selectedFunctionRef.opacity = 0.5
            self.app.selectedFunctionRef = e.control

        self.app.update()

    def scheduler_handle_click(self, e):
        MYcalendar()

    def quadratic_handle_click(self, e):
        self.app.reset()
        if (self.app.modeText.value == "quadratic solver"):
            self.app.rowQuadraticRef.current.controls[0].value = None
            self.app.rowQuadraticRef.current.controls[1].value = None
            self.app.rowQuadraticRef.current.controls[2].value = None
            self.app.mode = mode.Mode.REGULAR
            self.app.solverRef.current.on_click = self.app.calculate
            self.app.modeText.value = ""
            self.app.selectedFunctionRef = None
            self.app.rowQuadraticRef.current.visible = False
            self.app.expressionRef.current.visible = True

            e.control.opacity = 0.5
        else:
            self.app.solverRef.current.on_click = self.app.quadratic_solver
            self.app.mode = mode.Mode.QUADRATIC_SOLVER
            self.app.modeText.value = "quadratic solver"
            e.control.opacity = 1
            if (self.app.selectedFunctionRef):
                self.app.selectedFunctionRef.opacity = 0.5
            self.app.selectedFunctionRef = e.control
            self.app.rowQuadraticRef.current.visible = True
            self.app.expressionRef.current.visible = False

        self.app.update()

    def button_clicked_special_functions(self):
        pass

    def button_clicked(self, e):
        data = e.control.data
        if self.app.result.value == "Error" or data == "AC":
            self.app.reset()

        if data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "X"):

            if (self.app.present_state == True or self.app.expression.value == "0"):
                self.app.present_state = False
                self.app.result.size = consts.default_size
                self.app.expression.value = data
            else:
                self.app.expression.value = str(self.app.expression.value)+data
        # replace nRoot with pow
        pattern = r'([-+]?[0-9]*\.?[0-9]+)nRoot(\d+)(?:\^(\d+))?'
        if (re.search(pattern,  self.app.expression.value)):
            self.app.expression.value = Utils.replaceNRoot(
                pattern,  self.app.expression)

        elif data in ("+", "-", "*", "/", "**", "nRoot"):
            self.app.operator = data
            if str(self.app.expression.value)[-1] in ("+", "-", "*", "/", "**", "nRoot"):
                self.app.expression.value = self.app.expression.value[:-1] + data
            elif self.app.present_state == True:
                self.app.present_state = False
                self.app.expression.value = str(self.app.result.value)+data
            else:
                self.app.expression.value = str(
                    self.app.expression.value) + data

        elif data in ("="):
            try:
                if self.app.mode == mode.Mode.REGULAR:
                    res = self.app.calculate(self.app.expression.value)
                    self.app.present_state = True
                    if res == "Error":
                        self.app.result.value = "Error"
                    else:
                        self.app.result.value = res
                else:
                    self.app.expression.value = str(
                        self.app.expression.value)+"="
            except:
                self.app.result.value = "Error"

        elif data in ("%"):
            self.app.result.value = float(self.app.result.value) / 100
            self.app.expression.value = f'({str(self.app.expression.value)})*0.01'

        elif data in ("C"):
            self.app.expression.value = self.app.expression.value[:-1]
        self.app.update()
        if (self.app.present_state == True):
            self.app.result.size = consts.enlrage_size

    def expand_clicked(self, e):
        self.app.row1Ref.current.visible = not self.app.row2Ref.current.visible
        self.app.row2Ref.current.visible = not self.app.row2Ref.current.visible
        self.app.dividerRef.current.visible = not self.app.dividerRef.current.visible
        self.app.update()
