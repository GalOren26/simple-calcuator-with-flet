from calendar import Calendar
import flet
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
    Text,
    ElevatedButton,
    FloatingActionButton,
    TextField


)
from sympy import symbols, Eq, solve, sympify, init_printing, pprint
import re as re
from calnedar import MYcalendar
import mode
import utils.utils as Utils
from eventHandles import eventHandles


class CalculatorApp(UserControl):

    def build(self):
        x = Calendar()

        # refactor to mixin- problem with multi inheritance
        # refs to objects
        init_printing()
        self.row1Ref = Ref[Row]()
        self.row2Ref = Ref[Row]()
        self.rowQuadraticRef = Ref[Row]()
        self.selectedFunctionRef = Ref[Row]()
        self.expressionRef = Ref[Row]()
        self.dividerRef = Ref[Divider]()
        self.event_handles = eventHandles(self)
        self.solverRef = Ref[FloatingActionButton]()
        self.mode = mode.Mode.REGULAR
        self.present_state = False
        self.expression = Text(
            value="0", color=colors.WHITE, size=18)
        self.modeText = Text(
            value="", color=colors.RED_400, size=15)
        self.result = Text(value="0", color=colors.RED_700,
                           size=22)
        self.reset()
        return Container(
            width=400,
            bgcolor=colors.BLACK,
            border_radius=border_radius.all(20),
            padding=20,
            content=Column(
                controls=[
                    Row(controls=[
                        self.modeText], alignment="center"),
                    Row(ref=self.rowQuadraticRef, visible=False, controls=[TextField(expand=1, bgcolor=colors.WHITE, label="a="),
                                                                           TextField(expand=1, bgcolor=colors.WHITE,
                                                                                     label="b="),
                        TextField(expand=1, bgcolor=colors.WHITE, label="c=")]),
                    Row(ref=self.expressionRef, controls=[
                        self.expression], alignment="start"),
                    Row(controls=[
                        self.result], alignment="end"),
                    Row(ref=self.row1Ref, visible=False, controls=[
                        Container(
                            opacity=0.5,
                            data="quadratic",
                            expand=1,
                            on_click=self.event_handles.quadratic_handle_click,
                            content=Image(width=50,
                                          height=50,
                                          src='assets/quadratic.jpeg')),
                        Container(
                            opacity=0.5,
                            data="one-var",
                            expand=1,
                            on_click=self.event_handles.one_var_handle_click,
                            content=Image(width=50,
                                          height=50,
                                          src='assets/one-var.png')),

                        Container(
                            opacity=0.5,
                            data="schedule",
                            expand=1,
                            on_click=self.event_handles.scheduler_handle_click,
                            content=Image(width=50,
                                          height=50,
                                          src='assets/scheduleTime.png')),
                        FloatingActionButton(
                            text="X",
                            data="X",
                            bgcolor=colors.BLUE_GREY_100,
                            on_click=self.event_handles.button_clicked,
                            expand=1,
                            width=50,
                            height=50
                        ),
                    ]
                    ),
                    Row(ref=self.row2Ref, visible=False, controls=[
                        Container(
                            data='nRoot',
                            expand=1,
                            on_click=self.event_handles.button_clicked,
                            content=Image(width=50,
                                          height=50,
                                          src='assets/nroot.png')),
                        Container(
                            data='**',
                            expand=1,
                            on_click=self.event_handles.button_clicked,
                            content=Image(width=50,
                                          height=50,
                                          src='assets/pow.png')),
                        FloatingActionButton(
                            ref=self.solverRef,
                            text="solve",
                            data="solve",
                            bgcolor=colors.BLUE_GREY_100,
                            on_click=self.calculate,
                            expand=1,
                            width=50,
                            height=50
                        ),

                    ]
                    ),
                    Divider(ref=self.dividerRef, visible=False,
                            color=colors.WHITE),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="AC",
                                data="AC",
                                bgcolor=colors.BLUE_GREY_100,
                                on_click=self.event_handles.button_clicked,
                                color=colors.BLACK,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="C",
                                data="C",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                on_click=self.event_handles.button_clicked,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="%",
                                data="%",
                                bgcolor=colors.BLUE_GREY_100,
                                on_click=self.event_handles.button_clicked,
                                color=colors.BLACK,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="/",
                                data="/",
                                bgcolor=colors.ORANGE,
                                on_click=self.event_handles.button_clicked,
                                color=colors.WHITE,
                                expand=1,

                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="7",
                                data="7",
                                bgcolor=colors.WHITE24,
                                on_click=self.event_handles.button_clicked,
                                color=colors.WHITE,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="8",
                                data="8",
                                bgcolor=colors.WHITE24,
                                on_click=self.event_handles.button_clicked,
                                color=colors.WHITE,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="9",
                                data="9",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                on_click=self.event_handles.button_clicked,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="*",
                                data="*",
                                bgcolor=colors.ORANGE,
                                on_click=self.event_handles.button_clicked,
                                color=colors.WHITE,
                                expand=1,
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="4",
                                data="4",
                                bgcolor=colors.WHITE24,
                                on_click=self.event_handles.button_clicked,
                                color=colors.WHITE,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="5",
                                data="5",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                on_click=self.event_handles.button_clicked,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="6",
                                data="6",
                                bgcolor=colors.WHITE24,
                                on_click=self.event_handles.button_clicked,
                                color=colors.WHITE,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="-",
                                data="-",
                                bgcolor=colors.ORANGE,
                                on_click=self.event_handles.button_clicked,
                                color=colors.WHITE,
                                expand=1,
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="1",
                                data="1",
                                bgcolor=colors.WHITE24,
                                on_click=self.event_handles.button_clicked,
                                color=colors.WHITE,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="2",
                                data="2",
                                bgcolor=colors.WHITE24,
                                on_click=self.event_handles.button_clicked,
                                color=colors.WHITE,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="3",
                                data="3",
                                bgcolor=colors.WHITE24,
                                on_click=self.event_handles.button_clicked,
                                color=colors.WHITE,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="+",
                                data="+",
                                bgcolor=colors.ORANGE,
                                on_click=self.event_handles.button_clicked,
                                color=colors.WHITE,
                                expand=1,
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            Container(
                                expand=1,
                                on_click=self.event_handles.expand_clicked,
                                content=Image(
                                    src=Utils.getSvgImage(
                                        'assets/expand.svg'),
                                    width=50,
                                    height=50,
                                )),
                            ElevatedButton(
                                text="0",
                                data="0",
                                bgcolor=colors.WHITE24,
                                on_click=self.event_handles.button_clicked,
                                color=colors.WHITE,
                                expand=1,),
                            ElevatedButton(
                                text=".",
                                data=".",
                                bgcolor=colors.WHITE24,
                                on_click=self.event_handles.button_clicked,
                                color=colors.WHITE,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="=",
                                data="=",
                                bgcolor=colors.ORANGE,
                                on_click=self.event_handles.button_clicked,
                                color=colors.WHITE,
                                expand=1,
                            ),
                        ]
                    ),
                ]
            ),

        )

    def calculate(self, e):
        try:
            return Utils.format_number(eval(self.expression.value))
        except:
            return "Error"

    def one_var_solver(self, e):
        try:
            X = symbols('X')
            self.expression.value = re.sub(
                r'(\d)(X)', r'\1*\2', self.expression.value)
            left_side, right_side = self.expression.value.split("=")
            # add('*') before variable of the user forfot
            left_side = sympify(str(left_side))
            right_side = sympify(str(right_side))
            equation = Eq(left_side, right_side)
            # Solve the equation symbolically
            val = solve(equation, X)
            self.result.value = val[0]
            self.present_state = True
            self.update()
        except:
            return "Error"

    def quadratic_solver(self, e):
        try:
            X = symbols('X')
            a = self.rowQuadraticRef.current.controls[0].value
            b = self.rowQuadraticRef.current.controls[1].value
            c = self.rowQuadraticRef.current.controls[2].value
            expression = f"{a}*X**2+{b}*X+{c}=0"
            left_side, right_side = expression.split("=")
            left_side = sympify(str(left_side))
            right_side = sympify(str(right_side))
            equation = Eq(left_side, right_side)
            # Solve the equation symbolically
            val = solve(equation, X)
            self.result.value = f"x1,2={val}"
            self.present_state = True
            self.update()
        except:
            return "Error"

    def reset(self):
        self.result.value = "0"
        self.expression.value = "0"
        self.present_state = False


def main(page: Page):
    page.title = "Calc App"
    # create application instance
    calc = CalculatorApp()
    page.window_width = 500
    page.window_height = 800
    # add application's root control to the page
    page.add(calc)


flet.app(target=main)
